"""The public response contract, independent of operational diagnostics."""
from __future__ import annotations

import os
import re
from . import config

def _configured_names() -> str:
    """The deployment's own database and table names, from configuration."""
    names = {config.NEWS_TABLE, config.AUTH_DB,
             os.environ.get("PRISM_EVENTS_TABLE", ""), os.environ.get("PRISM_FUNDING_TABLE", "")}
    parts = {n for name in names if name for n in (name, name.split(".")[0] + ".")}
    return "|".join(sorted(map(re.escape, parts), key=len, reverse=True))


_INTERNAL = re.compile(
    r"clickhouse|mongodb|mongo(?:db)?\b|redis|\bshards?\b|\bcluster\b|\bsubcats?\b|"
    r"\btags\b|country_pri|pri_organization|pri_person|target_id|collection_name|"
    + _configured_names() +
    r"|/home/|/mnt/|/srv/|127\.0\.0\.1|\b(?:10|192\.168|172\.(?:1[6-9]|2\d|3[01])|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7]))\.\d{1,3}\.\d{1,3}|"
    r"\bSELECT\b.+\bFROM\b|article.store|\bnode\s+\d+|"
    r"\bCH\s*\d{3}\b|\w+Error\b|\w*Exception\b|DB::|Code:\s*\d+|Traceback|connection tries", re.I)
_PRIVATE_KEYS = {"table", "tables", "article_store", "sql", "extra_sql", "query_sql", "subcats",
                 "tags", "collection_name", "strict_shard_read", "ring_nodes", "node",
                 "expected", "floor", "ttl_seconds", "checked_at", "address", "host"}
_FAILURES = {
    "internal": "The request could not be completed. Please try again later.",
    "upstream": "News data is temporarily unavailable. Please try again later.",
    "coverage_unavailable": "Reliable coverage is temporarily unavailable. Please try again later.",
}


def archive() -> dict:
    return {"article_count_display": config.ARCHIVE_SIZE_DISPLAY,
            "scope": "Fliar historical and real-time news",
            "note": "The article count is supplied by Fliar. Query counts reflect available matching coverage."}


def coverage(value: dict | None) -> dict:
    value = value or {}
    if "available" in value:
        return {"available": bool(value["available"])}
    # Reachability is not evidence of complete ingestion, so do not report completeness percent.
    return {"available": bool(value) and not bool(value.get("partial", True))}


def _note(value):
    if not isinstance(value, str):
        return None
    if _INTERNAL.search(value):
        return "Some coverage or article details may be incomplete; check the response window."
    return value


def _data(value):
    if isinstance(value, list):
        return [_data(x) for x in value]
    if not isinstance(value, dict):
        # Article text and quoted source material are returned verbatim.
        return value
    out = {}
    for k, v in value.items():
        if k in _PRIVATE_KEYS:
            continue
        if k == "coverage" and isinstance(v, dict) and ("partial" in v or "expected" in v):
            out[k] = coverage(v)
        elif k == "notes" and isinstance(v, list):
            out[k] = list(dict.fromkeys(n for n in (_note(x) for x in v) if n))
        elif k in {"note", "reason", "freshness", "empty_reason"}:
            out[k] = _note(v)
        else:
            out[k] = _data(v)
    return out


def response(env: dict) -> dict:
    """Sanitize service metadata; preserve article facts and measured query counts."""
    out = _data(env)
    meta = env.get("meta") or {}
    # Error metadata is never allowed to forward arbitrary exception diagnostics.
    allowed = {"seconds", "request_seconds", "plan", "quota", "notes", "coverage", "validation"}
    out["meta"] = {k: _data(v) for k, v in meta.items() if k in allowed}
    if "coverage" in meta:
        out["meta"]["coverage"] = coverage(meta["coverage"])
    if "notes" in meta:
        out["meta"]["notes"] = list(dict.fromkeys(n for n in (_note(x) for x in meta["notes"]) if n))
    if "validation" in meta:
        out["meta"]["validation"] = [{"loc": e.get("loc"), "msg": _note(e.get("msg"))}
                                      for e in meta["validation"][:5]]
    error = env.get("error")
    if error:
        kind = error.get("kind", "internal")
        out["error"] = {"kind": kind, "reason": _FAILURES.get(kind) or _note(error.get("reason"))}
        for k in ("upgrade_url", "retry_after", "limit", "remaining"):
            if k in error:
                out["error"][k] = error[k]
    return out
