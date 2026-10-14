"""quota — Redis counters exactly as, plus the daily ledger.

    pna:req:u:{user_id}:{YYYYMM}     INCR per metered request, EXPIRE 45 days
    pna:exp:u:{user_id}:{YYYYMM}     INCRBY articles exported, EXPIRE 45 days
    pna:req:k:{key_id}:{YYYYMM}      same, per key (display only)
    pna:exp:k:{key_id}:{YYYYMM}
    pna:rl:u:{user_id}:{epoch_min}   INCR, EXPIRE 120 s  -> rate_per_minute
    pna:lastused:{key_id}            epoch seconds (written by auth.touch_last_used)

Quotas are per ACCOUNT per UTC calendar month. Exports are charged by
RESERVE-then-REFUND, mirroring radar's export credit path: INCRBY the requested
count before fetching, DECRBY whatever was not delivered, so a 500 never burns
quota. Rate and quota are checked BEFORE ClickHouse.

Redis unavailable is fail-CLOSED (502 `upstream`): a public API that silently
stops metering when its counter store blinks is a billing bug, not resilience.

`redis_client()` is the single seam: tests monkeypatch it with an in-memory stub.
"""
from __future__ import annotations

import datetime as _dt
import json
import logging
import threading
import time

from . import config
from .envelope import ApiError

log = logging.getLogger("prism_news_api.quota")

_R = None
_R_LOCK = threading.Lock()
P = config.REDIS_PREFIX


def redis_client():
    global _R
    with _R_LOCK:
        if _R is None:
            import redis
            _R = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT,
                             db=config.REDIS_DB, socket_timeout=3,
                             socket_connect_timeout=3, decode_responses=True)
        return _R


def _r():
    try:
        return redis_client()
    except Exception as e:
        raise ApiError("upstream", f"quota store unavailable: {type(e).__name__}")


def _guard(fn):
    """Run a Redis operation; a transport failure is a 502, never a free pass."""
    try:
        return fn()
    except ApiError:
        raise
    except Exception as e:
        log.error("redis failure: %s: %s", type(e).__name__, e)
        raise ApiError("upstream", "quota store unavailable; the request was not served")


def month_key(now: _dt.datetime | None = None) -> str:
    return (now or _dt.datetime.utcnow()).strftime("%Y%m")


def _keys(user_id: str, key_id: str, month: str | None = None) -> dict:
    m = month or month_key()
    return {"req_u": f"{P}req:u:{user_id}:{m}", "exp_u": f"{P}exp:u:{user_id}:{m}",
            "req_k": f"{P}req:k:{key_id}:{m}", "exp_k": f"{P}exp:k:{key_id}:{m}"}


def _quota_exceeded(what: str, used: int, limit: int, usage: dict) -> ApiError:
    return ApiError("quota_exceeded",
                    f"monthly {what} quota reached ({used:,}/{limit:,}); resets on the 1st (UTC). "
                    f"Upgrade at {config.UPGRADE_URL}",
                    fields={"upgrade_url": config.UPGRADE_URL}, meta={"quota": usage})


# ── rate limit ───────────────────────────────────────────────────────────────
def check_rate(user_id: str, limit: int) -> dict:
    """INCR the current-minute bucket. Over the limit -> 429 with Retry-After."""
    def run():
        now = int(time.time())
        key = f"{P}rl:u:{user_id}:{now // 60}"
        r = _r()
        pipe = r.pipeline()
        pipe.incr(key)
        pipe.expire(key, config.RATE_KEY_TTL)
        n = int(pipe.execute()[0])
        remaining = max(0, int(limit) - n)
        retry = 60 - (now % 60)
        if n > int(limit):
            raise ApiError("rate_limited",
                           f"rate limit of {limit} requests/minute exceeded; retry in {retry}s",
                           headers={"Retry-After": str(retry)},
                           meta={"quota": {"rate": {"limit": int(limit), "remaining": 0,
                                                    "retry_after_seconds": retry}}})
        return {"limit": int(limit), "remaining": remaining, "window": "minute"}
    return _guard(run)


# ── request quota ────────────────────────────────────────────────────────────
def check_requests(user_id: str, key_id: str, limit: int) -> dict:
    """INCR the account's monthly request counter; roll back and 402 past the
    limit. Returns the usage snapshot after the increment."""
    def run():
        k = _keys(user_id, key_id)
        r = _r()
        n = int(r.incr(k["req_u"]))
        if n > int(limit):
            r.decr(k["req_u"])
            usage = _snapshot(r, k, limit, None)
            raise _quota_exceeded("request", n - 1, int(limit), usage)
        pipe = r.pipeline()
        pipe.expire(k["req_u"], config.QUOTA_KEY_TTL)
        pipe.incr(k["req_k"])
        pipe.expire(k["req_k"], config.QUOTA_KEY_TTL)
        pipe.execute()
        return k
    return _guard(run)


# ── exports: reserve / refund ────────────────────────────────────────────────
def exports_remaining(user_id: str, key_id: str, limit: int) -> int:
    def run():
        k = _keys(user_id, key_id)
        used = int(_r().get(k["exp_u"]) or 0)
        return max(0, int(limit) - used)
    return _guard(run)


def reserve_exports(user_id: str, key_id: str, n: int, limit: int) -> int:
    """INCRBY n BEFORE fetching. If that overshoots the monthly limit the
    overshoot is rolled back and only the remainder is granted; 0 remaining
    -> 402. Returns the number granted (<= n)."""
    n = int(n)
    if n <= 0:
        return 0

    def run():
        k = _keys(user_id, key_id)
        r = _r()
        new = int(r.incrby(k["exp_u"], n))
        granted = n
        if new > int(limit):
            over = min(n, new - int(limit))
            granted = n - over
            if over:
                r.decrby(k["exp_u"], over)
        if granted <= 0:
            usage = _snapshot(r, k, None, limit)
            raise _quota_exceeded("export", int(limit), int(limit), usage)
        pipe = r.pipeline()
        pipe.expire(k["exp_u"], config.QUOTA_KEY_TTL)
        pipe.incrby(k["exp_k"], granted)
        pipe.expire(k["exp_k"], config.QUOTA_KEY_TTL)
        pipe.execute()
        return granted
    return _guard(run)


def refund_exports(user_id: str, key_id: str, n: int) -> None:
    """DECRBY what was reserved but not delivered. Best-effort: a failure here
    is logged, never raised — the caller is already on its way out."""
    n = int(n)
    if n <= 0:
        return
    try:
        k = _keys(user_id, key_id)
        pipe = _r().pipeline()
        pipe.decrby(k["exp_u"], n)
        pipe.decrby(k["exp_k"], n)
        pipe.execute()
    except Exception as e:
        log.error("export refund of %s failed for user %s: %s", n, user_id, e)


# ── snapshot ─────────────────────────────────────────────────────────────────
def _snapshot(r, k: dict, req_limit, exp_limit) -> dict:
    pipe = r.pipeline()
    pipe.get(k["req_u"])
    pipe.get(k["exp_u"])
    pipe.get(k["req_k"])
    pipe.get(k["exp_k"])
    ru, eu, rk, ek = [int(x or 0) for x in pipe.execute()]
    out = {"month": month_key(),
           "requests": {"used": ru, "limit": req_limit,
                        "remaining": max(0, int(req_limit) - ru) if req_limit is not None else None},
           "exports": {"used": eu, "limit": exp_limit,
                       "remaining": max(0, int(exp_limit) - eu) if exp_limit is not None else None},
           "this_key": {"requests": rk, "exports": ek}}
    return out


def usage(user_id: str, key_id: str, plan_cfg: dict, rate: dict | None = None) -> dict:
    def run():
        k = _keys(user_id, key_id)
        snap = _snapshot(_r(), k, plan_cfg.get("requests_per_month"),
                         plan_cfg.get("exports_per_month"))
        snap["rate"] = rate or {"limit": plan_cfg.get("rate_per_minute"), "window": "minute"}
        return snap
    return _guard(run)


# ── daily ledger (Mongo, best-effort) ────────────────────────────────────────
def record_daily(user_id: str, key_id: str, endpoint: str, requests: int = 1,
                 exports: int = 0) -> None:
    """<auth db>.api_usage_daily `$inc` upsert per request, for the dashboard."""
    try:
        from bson import ObjectId
        from .auth import mongo_db
        now = _dt.datetime.utcnow()
        ep = endpoint.replace(".", "_").replace("$", "_")
        inc = {"requests": int(requests), "exports": int(exports)}
        if requests:
            inc[f"endpoints.{ep}"] = int(requests)
        mongo_db().api_usage_daily.update_one(
            {"user_id": ObjectId(user_id), "key_id": ObjectId(key_id),
             "day": now.strftime("%Y-%m-%d")},
            {"$inc": inc, "$set": {"updated_at": now}}, upsert=True)
    except Exception as e:
        log.warning("api_usage_daily write skipped: %s", e)


# ── shared JSON cache (baselines) ────────────────────────────────────────────
def cache_get(name: str):
    try:
        raw = _r().get(f"{P}{name}")
        return json.loads(raw) if raw else None
    except Exception as e:
        log.debug("cache miss (%s): %s", name, e)
        return None


def cache_put(name: str, obj, ttl: int = config.BASELINE_TTL) -> None:
    try:
        _r().set(f"{P}{name}", json.dumps(obj, separators=(",", ":")), ex=int(ttl))
    except Exception as e:
        log.debug("cache put skipped (%s): %s", name, e)


def headers_for(snapshot: dict | None, plan: str) -> dict:
    """The five response headers every authenticated call carries."""
    h = {"X-Plan": plan}
    if not snapshot:
        return h
    rate = snapshot.get("rate") or {}
    req = snapshot.get("requests") or {}
    exp = snapshot.get("exports") or {}
    if rate.get("limit") is not None:
        h["X-RateLimit-Limit"] = str(rate["limit"])
    if rate.get("remaining") is not None:
        h["X-RateLimit-Remaining"] = str(rate["remaining"])
    if req.get("remaining") is not None:
        h["X-Quota-Requests-Remaining"] = str(req["remaining"])
    if exp.get("remaining") is not None:
        h["X-Quota-Exports-Remaining"] = str(exp["remaining"])
    return h
