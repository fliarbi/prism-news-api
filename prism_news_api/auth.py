"""auth — API key -> account -> plan context.

    X-API-Key: pna_…        or        Authorization: Bearer pna_…
      -> sha256 -> <auth db>.api_keys (product prism_api, status active)
      -> <auth db>.users -> entitlements.prism_api -> plan (free if missing,
         expired, or the account is switched off)

Plan resolution mirrors fliarbi_auth.core._product_entitlement + its expiry
rule for the product `prism_api` (copied, not imported — this repo is
standalone). No cross-grant from radar/marketai plans, by design.

The only write here is `api_keys.last_used_at`, throttled to once per five
minutes per key through a Redis `SET NX EX` — a per-request Mongo write on a
public API is a self-inflicted load test.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import logging
import re
import threading
import time
from dataclasses import dataclass, field
from typing import Mapping, Optional

from . import config
from .envelope import ApiError

log = logging.getLogger("prism_news_api.auth")

KEY_RE = re.compile(r"^pna_[0-9a-f]{40}$")
_CLIENT = None
_CLIENT_LOCK = threading.Lock()
_CACHE: dict[str, tuple] = {}
_CACHE_LOCK = threading.Lock()


@dataclass
class Principal:
    user_id: str
    key_id: str
    key_prefix: str
    key_name: str
    email: Optional[str]
    plan: str
    plan_cfg: dict
    source: str
    expired: bool
    expires: Optional[str]
    account_flag: Optional[str]
    notes: list = field(default_factory=list)

    def as_me(self) -> dict:
        return {"key": {"id": self.key_id, "name": self.key_name, "prefix": self.key_prefix},
                "account": {"user_id": self.user_id, "email": self.email},
                "plan": {"name": self.plan, "label": self.plan_cfg.get("label"),
                         "source": self.source, "expired": self.expired,
                         "expires": self.expires, "account_flag": self.account_flag},
                "limits": config.public_plan(self.plan_cfg)}


# ── stores ───────────────────────────────────────────────────────────────────
def mongo_db():
    """The auth database (PRISM_AUTH_DB), one client per process."""
    global _CLIENT
    with _CLIENT_LOCK:
        if _CLIENT is None:
            import pymongo
            _CLIENT = pymongo.MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=4000,
                                          socketTimeoutMS=8000, connectTimeoutMS=4000)
        return _CLIENT[config.AUTH_DB]


# ── key handling ─────────────────────────────────────────────────────────────
def extract_key(headers: Mapping[str, str]) -> Optional[str]:
    k = headers.get("x-api-key") or headers.get("X-API-Key")
    if k and k.strip():
        return k.strip()
    a = headers.get("authorization") or headers.get("Authorization") or ""
    if a.lower().startswith("bearer "):
        return a[7:].strip() or None
    return None


def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


# ── plan resolution (mirror of fliarbi_auth.core for product prism_api) ──────
def _product_entitlement(user: dict, product: str = config.PRODUCT):
    """(plan_name, expires, source) from user.entitlements.<product>; free when
    absent. No legacy-field fallback: that exists only for radar."""
    ent = (user.get("entitlements") or {}).get(product)
    if isinstance(ent, dict) and ent.get("plan"):
        return (str(ent.get("plan")).lower(), ent.get("expires"),
                ent.get("source") or "dedicated")
    return "free", None, "free"


def plan_context(user: dict, catalog: dict | None = None,
                 now: _dt.datetime | None = None) -> dict:
    """Pure: user doc -> {plan, plan_cfg, source, expired, expires, account_flag, notes}."""
    cat = catalog if catalog is not None else config.plans()
    now = now or _dt.datetime.utcnow()
    plan, expires, source = _product_entitlement(user)
    notes: list[str] = []
    expired = False
    if plan != "free" and isinstance(expires, _dt.datetime) and expires < now:
        plan, expired = "free", True
        notes.append("plan expired; serving the free tier")
    if plan not in cat:
        notes.append(f"plan {plan!r} is not in the catalog; serving the free tier")
        plan = "free"
    account_flag = None
    if user.get("banned"):
        account_flag = "banned"
    elif user.get("disabled"):
        account_flag = "disabled"
    elif user.get("email_verified") is False:
        account_flag = "email_unverified"
    if account_flag:
        plan = "free"
        notes.append(f"account flag {account_flag}: serving the free tier")
    cfg = config.plan_cfg(plan, cat)
    override = config.test_request_limit()
    if override is not None:
        cfg["requests_per_month"] = override
        notes.append(f"PRISM_TEST_REQUEST_LIMIT={override} override active")
    exp_s = expires.isoformat(sep=" ", timespec="seconds") if isinstance(expires, _dt.datetime) else (
        str(expires) if expires else None)
    return {"plan": plan, "plan_cfg": cfg, "source": source, "expired": expired,
            "expires": exp_s, "account_flag": account_flag, "notes": notes}


# ── authentication ───────────────────────────────────────────────────────────
def authenticate(headers: Mapping[str, str]) -> Principal:
    key = extract_key(headers)
    if not key:
        raise ApiError("unauthenticated",
                       "no API key: send `X-API-Key: pna_…` or `Authorization: Bearer pna_…`. "
                       "Keys are issued in the Fliar dashboard (Fliar Prism workspace → API keys).")
    if not KEY_RE.match(key):
        raise ApiError("invalid_key", "malformed key: expected pna_ followed by 40 hex characters")
    h = hash_key(key)
    now = time.time()
    with _CACHE_LOCK:
        hit = _CACHE.get(h)
    if hit and now - hit[1] < config.AUTH_CACHE_TTL:
        p = hit[0]
    else:
        p = _lookup(h)
        with _CACHE_LOCK:
            _CACHE[h] = (p, now)
            if len(_CACHE) > 5000:
                _CACHE.clear()
    touch_last_used(p.key_id)
    return p


def _lookup(key_hash: str) -> Principal:
    try:
        db = mongo_db()
        doc = db.api_keys.find_one({"key_hash": key_hash, "product": config.PRODUCT})
    except Exception as e:
        log.error("auth store unavailable: %s", e)
        raise ApiError("upstream", "the key store did not answer; try again shortly")
    if not doc:
        raise ApiError("invalid_key", "unknown API key")
    if doc.get("status") != "active":
        raise ApiError("invalid_key", "this API key has been revoked")
    try:
        user = db.users.find_one({"_id": doc["user_id"]},
                                 {"email": 1, "entitlements": 1, "disabled": 1,
                                  "banned": 1, "email_verified": 1})
    except Exception as e:
        log.error("auth store unavailable: %s", e)
        raise ApiError("upstream", "the account store did not answer; try again shortly")
    if not user:
        raise ApiError("invalid_key", "this API key belongs to no account")
    ctx = plan_context(user)
    return Principal(user_id=str(user["_id"]), key_id=str(doc["_id"]),
                     key_prefix=doc.get("prefix") or "", key_name=doc.get("name") or "",
                     email=user.get("email"), plan=ctx["plan"], plan_cfg=ctx["plan_cfg"],
                     source=ctx["source"], expired=ctx["expired"], expires=ctx["expires"],
                     account_flag=ctx["account_flag"], notes=ctx["notes"])


def touch_last_used(key_id: str) -> None:
    """api_keys.last_used_at, at most once per LASTUSED_TTL seconds per key."""
    try:
        from . import quota
        r = quota.redis_client()
        if not r.set(f"{config.REDIS_PREFIX}lastused:{key_id}", int(time.time()),
                     nx=True, ex=config.LASTUSED_TTL):
            return
        from bson import ObjectId
        mongo_db().api_keys.update_one({"_id": ObjectId(key_id)},
                                       {"$set": {"last_used_at": _dt.datetime.utcnow()}})
    except Exception as e:                    # best-effort, never fails a request
        log.debug("last_used_at skipped: %s", e)


def clear_cache() -> None:
    with _CACHE_LOCK:
        _CACHE.clear()
