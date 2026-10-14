"""articles — turning a ClickHouse `target_id` into an article a person can read.

Port of prism-mcp/prism/articles.py. The corpus is split in two on purpose:
ClickHouse holds the SIGNAL (one row per article: sentiment, priority, classes,
themes, geography, lede) and answers "which articles, how many, when". The
article RECORD (url, title, publisher, full body, authors, image) lives in
MongoDB, sharded across a 31-node consistent-hash ring:

    target_id -> get_node_for_id -> node
    node.inferences_analysis2.main -> which partition holds it
    node.news_chunks2.<partition>  -> the record

The ring module is IMPORTED from the cluster's own common/ directory (env
`PRISM_NEWS_COMMON`, fallback `PRISM_NEWS_COMMON_FALLBACK`), never
copied: a stale node map silently reads the wrong shard, which returns nothing
rather than failing.

Three details that produce an empty feed rather than an error if wrong:
  * the partition defaults to `from_2020_to_now` when the routing doc is missing;
  * the TITLE is not a column — it is inside a JSON string of scraped meta
    tags under og:title / twitter:title; an article with neither gets the first
    line of its body, never dropped;
  * `json_data.text` IS the full body (773 / 826 / 16,031 chars measured on
    three May-2026 articles), while ClickHouse `text` is the ~320-char lede.
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

from . import config

log = logging.getLogger("prism_news_api.articles")

DEFAULT_PARTITION = "from_2020_to_now"
_LOCK = threading.Lock()
_CLIENTS: dict = {}
_ROUTER = None

_PROJECTION_LITE = {"url": 1, "website": 1, "json_data.text": 1,
                    "json_data.meta_data": 1, "var.published_date": 1}
_PROJECTION_FULL = {**_PROJECTION_LITE, "json_data.authors": 1,
                    "json_data.top_image": 1, "json_data.meta_description": 1,
                    "json_data.publish_date": 1, "json_data.meta_lang": 1}


def _router():
    global _ROUTER
    if _ROUTER is None:
        path = next((p for p in (config.NEWS_COMMON, config.NEWS_COMMON_FALLBACK)
                     if p and os.path.exists(os.path.join(p, "main.py"))), None)
        if path is None:
            raise RuntimeError("article store router not configured: set PRISM_NEWS_COMMON")
        if path not in sys.path:
            sys.path.insert(0, path)
        from main import get_node_for_id, mongo_map_raw  # type: ignore
        _ROUTER = (get_node_for_id, mongo_map_raw)
    return _ROUTER


def _client(node_id: int):
    with _LOCK:
        if node_id not in _CLIENTS:
            import pymongo
            _, mp = _router()
            _CLIENTS[node_id] = pymongo.MongoClient(
                f"mongodb://{mp[node_id]}", serverSelectionTimeoutMS=4000,
                socketTimeoutMS=20000, connectTimeoutMS=4000, maxPoolSize=8)
        return _CLIENTS[node_id]


# ── record shaping ───────────────────────────────────────────────────────────
def title_of(doc: dict) -> tuple[str, str]:
    """(title, first_line). Titles live in a JSON string of scraped meta tags."""
    jd = doc.get("json_data") or {}
    text = (jd.get("text") or "").strip()
    first = text.split("\n")[0][:300] if text else ""
    raw = jd.get("meta_data")
    if raw:
        try:
            md = json.loads(raw) if isinstance(raw, str) else raw
            t = ((md.get("og") or {}).get("title")
                 or (md.get("twitter") or {}).get("title")
                 or md.get("title"))
            if t:
                return str(t).strip()[:300], first
        except Exception:
            pass
    return "", first


def publisher_of(doc: dict) -> str:
    """The publishing host, normalised: scheme and path dropped, `www.`
    stripped (the same outlet is stored both ways)."""
    raw = (doc.get("website") or "").strip() or (doc.get("url") or "")
    host = re.sub(r"^https?://", "", raw).split("/")[0].strip().lower()
    return re.sub(r"^www\d?\.", "", host)


def _iso(v):
    if v is None or isinstance(v, str):
        # The scraper stores a missing date as the STRING "None"; a client
        # must never see that as a value.
        return None if (v or "").strip().lower() in ("", "none", "null") else v
    try:
        return v.isoformat(sep=" ", timespec="seconds")
    except Exception:
        return str(v)


def _authors(v) -> list:
    """Scraped author lists carry junk ('Https', 'Read Full Bio', bios). Keep
    short, distinct, non-URL entries; never invent a name."""
    if not isinstance(v, list):
        return []
    out = []
    for a in v:
        s = str(a or "").strip()
        if not s or len(s) > 60 or "http" in s.lower() or "." in s.split(" ")[0].lower() and len(s.split(" ")) == 1:
            continue
        if s.lower() in ("read full bio", "staff", "admin", "https"):
            continue
        if s not in out:
            out.append(s)
    return out[:8]


def _record(doc: dict, part: str, full: bool) -> dict:
    tid = str(doc["_id"])
    title, first = title_of(doc)
    jd = doc.get("json_data") or {}
    rec = {"id": tid, "headline": title or first or None, "url": doc.get("url"),
           "publisher": publisher_of(doc),
           "store_published_at": _iso((doc.get("var") or {}).get("published_date")),
           "partition": part}
    if full:
        body = (jd.get("text") or "").strip()
        rec.update({
            "body": body or None,
            "body_chars": len(body),
            "authors": _authors(jd.get("authors")),
            "top_image": jd.get("top_image") or None,
            "meta_description": (jd.get("meta_description") or "").strip() or None,
            "publish_date": _iso(jd.get("publish_date")),
            "language": jd.get("meta_lang") or None,
        })
    return rec


# ── resolution ───────────────────────────────────────────────────────────────
def resolve(target_ids, full: bool = False) -> tuple[dict, list]:
    """ids -> ({id: record}, [node errors]). Batched per node, nodes in
    parallel. Missing ids are simply absent from the dict: a record rotated
    out of the store is not a failure of the query."""
    ids = [str(t) for t in (target_ids or []) if t]
    if not ids:
        return {}, []
    from bson import ObjectId
    get_node, _ = _router()
    by_node: dict[int, list] = {}
    for t in ids:
        try:
            oid = ObjectId(t)
        except Exception:
            continue
        by_node.setdefault(int(get_node(str(oid))), []).append(oid)
    proj = _PROJECTION_FULL if full else _PROJECTION_LITE

    def fetch(node_id: int, oids: list) -> tuple[dict, dict | None]:
        found: dict = {}
        try:
            cli = _client(node_id)
            parts: dict[str, list] = {}
            for inf in cli.inferences_analysis2.main.find(
                    {"_id": {"$in": oids}}, {"collection_name": 1}):
                parts.setdefault(inf.get("collection_name") or DEFAULT_PARTITION,
                                 []).append(inf["_id"])
            routed = {i for v in parts.values() for i in v}
            missing = [o for o in oids if o not in routed]
            if missing:
                parts.setdefault(DEFAULT_PARTITION, []).extend(missing)
            for part, want in parts.items():
                for doc in cli.news_chunks2[part].find({"_id": {"$in": want}}, proj):
                    found[str(doc["_id"])] = _record(doc, part, full)
            return found, None
        except Exception as e:
            log.warning("article store node %s failed: %s: %s", node_id, type(e).__name__, e)
            return found, {"node": node_id, "requested": len(oids),
                           "error": f"{type(e).__name__}: {str(e)[:160]}"}

    out: dict = {}
    errors: list = []
    with ThreadPoolExecutor(max_workers=min(8, max(1, len(by_node)))) as pool:
        for found, err in pool.map(lambda kv: fetch(*kv), by_node.items()):
            out.update(found)
            if err:
                errors.append(err)
    return out, errors


def health(all_nodes: bool = False) -> dict:
    """Can the article store be reached, and how many nodes are in the ring."""
    try:
        get_node, mp = _router()
    except Exception as e:
        return {"available": False, "reason": f"ring module unavailable: {type(e).__name__}: {e}"}
    if all_nodes:
        def probe(node):
            try:
                _client(node).admin.command("ping")
                return {"node": node, "available": True}
            except Exception as e:
                return {"node": node, "available": False, "error": str(e)[:120]}
        with ThreadPoolExecutor(max_workers=min(16, len(mp))) as pool:
            nodes = list(pool.map(probe, sorted(mp)))
        return {"available": all(n["available"] for n in nodes),
                "ring_nodes": len(mp), "probed_nodes": len(nodes),
                "unavailable": [n for n in nodes if not n["available"]]}
    try:
        node = int(get_node("65f1c2a4b1e2c3d4e5f60718"))
        _client(node).admin.command("ping")
        return {"available": True, "ring_nodes": len(mp), "probed_node": node}
    except Exception as e:
        return {"available": False, "ring_nodes": len(mp),
                "reason": f"{type(e).__name__}: {str(e)[:160]}"}
