"""ch — the ClickHouse client, strict reads, the coverage gate, data_through.

Ported from prism-mcp/prism/ch.py and narrowed to the one table this API
serves. The rules are the same, because each one has already produced a
confidently wrong answer on this cluster:

  * Reads are STRICT (`skip_unavailable_shards=0`). A shard outage on a
    distributed table returns SMALLER numbers, not an error; a strict read
    fails instead, and a failed strict read is a 503 `coverage_unavailable`
    — never a partial count presented as a fact.
  * The coverage gate compares a strict `count()` against the measured row
    floor (255,586,690 on 2026-09-13), re-measured hourly. Passing it
    establishes reachability and the floor, not completeness of ingestion.
  * `data_through` is `max(datetime)` (cached hourly) and is the default
    upper bound of every window. Ingest thins after May 2026 (514k Jun, 52k
    Jul, 9k Aug against 2-4M/month before), so a window that ran to "today"
    would read as a collapse that never happened. Every payload carries the
    freshness note.
  * A count that raises is never rendered as zero. `scalar_int` raises on an
    empty result; 0 means the corpus holds nothing, an exception means the
    cluster did not answer, and the two are different facts.
"""
from __future__ import annotations

import json
import logging
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from . import config
from .envelope import ApiError

log = logging.getLogger("prism_news_api.ch")

TABLE = config.NEWS_TABLE

# ── column expressions (measured semantics, ───────────────
# `sentiments` holds up to three graded labels per article, so per-label
# percentages sum past 100. One article, one label: the highest-scoring wins.
TOP_SENTIMENT = "arraySort(x -> -x.2, sentiments)[1].1"
TOP_SENTIMENT_TUPLE = "arraySort(x -> -x.2, sentiments)[1]"
TOP_PRIORITY = "arraySort(x -> -x.2, priorities)[1].1"
POLARITY = (f"if(position({TOP_SENTIMENT}, 'neg') > 0, 'neg', "
            f"if(position({TOP_SENTIMENT}, 'pos') > 0, 'pos', 'neutral'))")
HAS_SENTIMENT = "length(sentiments) > 0"
HAS_PRIORITY = "length(priorities) > 0"
HAS_SUBCATS = "notEmpty(subcats)"
HAS_CLASSIFICATION = "notEmpty(classification)"
GRANULARITY_SQL = {
    "daily": "toDate(datetime)",
    "weekly": "toMonday(datetime)",
    "monthly": "toStartOfMonth(datetime)",
}


class CHError(RuntimeError):
    pass


def _params(timeout: int | None) -> dict:
    return {
        "user": config.CH_USER,
        "password": config.CH_PASSWORD,
        # strict, unless partial serving is switched on (config.PARTIAL_CAPTURE)
        "skip_unavailable_shards": "1" if config.PARTIAL_CAPTURE else "0",
        "max_execution_time": str(timeout or config.CH_MAX_EXECUTION_TIME),
        "priority": str(config.CH_PRIORITY),
        "max_threads": str(config.CH_MAX_THREADS),
        # count() is UInt64 and the JSON formats quote 64-bit ints by default
        "output_format_json_quote_64bit_integers": "0",
    }


def query(sql: str, timeout: int | None = None) -> str:
    """Run SQL, return the raw body. ClickHouse puts the diagnosis in the
    response BODY of an error and urllib throws that away with the HTTPError,
    so it is re-raised carrying the body."""
    t = timeout or config.CH_MAX_EXECUTION_TIME
    url = config.CH_HOST + "/?" + urllib.parse.urlencode(_params(t))
    req = urllib.request.Request(url, data=sql.encode("utf-8"))
    try:
        with urllib.request.urlopen(req, timeout=t + 5) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode(errors="replace")[:600].strip()
        except Exception:
            pass
        raise CHError(f"CH {e.code}: {body}\n  SQL: {' '.join(sql.split())[:400]}") from None
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        raise CHError(f"CH unreachable: {type(e).__name__}: {e}") from None


def rows(sql: str, timeout: int | None = None) -> list:
    """JSONCompactEachRow -> list of rows (lists). Tuples come back as arrays,
    NULL as None, arrays as lists — no TSV re-parsing of array literals."""
    body = query(sql.rstrip().rstrip(";") + " FORMAT JSONCompactEachRow", timeout)
    return [json.loads(ln) for ln in body.split("\n") if ln]


def one(sql: str, timeout: int | None = None):
    r = rows(sql, timeout)
    return r[0] if r else None


def scalar_int(sql: str, timeout: int | None = None) -> int:
    """A single integer. RAISES on an empty result — never falls back to 0."""
    r = one(sql, timeout)
    if not r or r[0] in (None, ""):
        raise CHError("empty result for a count query")
    return int(r[0])


def parallel(fns: list, workers: int = 4) -> list:
    """Run independent reads concurrently. Unlike prism-mcp's version this
    RAISES the first failure: a list endpoint with a count but no rows (or the
    reverse) is not a usable answer."""
    if not fns:
        return []
    with ThreadPoolExecutor(max_workers=min(workers, len(fns))) as ex:
        futs = [ex.submit(f) for f in fns]
        return [f.result() for f in futs]


# ── SQL literals ─────────────────────────────────────────────────────────────
def sql_str(x) -> str:
    return "'" + str(x).replace("\\", "\\\\").replace("'", "\\'") + "'"


def sql_arr(xs) -> str:
    return "[" + ",".join(sql_str(x) for x in xs) + "]"


def sql_in(xs) -> str:
    return "(" + ",".join(sql_str(x) for x in xs) + ")"


def sql_int(x) -> str:
    return str(int(x))


# ── error classification ─────────────────────────────────────────────────────
_SHARD_MARKERS = ("ALL_CONNECTION_TRIES_FAILED", "Code: 279", "NETWORK_ERROR",
                  "Code: 210", "unavailable", "Connection refused",
                  "CH unreachable", "TIMEOUT_EXCEEDED", "Code: 159")


def as_api_error(e: Exception) -> ApiError:
    """A CH failure is either the cluster being thin (503 coverage_unavailable,
    and the coverage cache is invalidated so the next call re-measures) or a
    query the server rejected (502 upstream)."""
    msg = str(e)
    if any(m in msg for m in _SHARD_MARKERS):
        invalidate_coverage()
        return ApiError("coverage_unavailable",
                        "a strict read of the corpus failed; one or more shards "
                        "did not answer. No partial count is returned. " + msg[:300])
    return ApiError("upstream", "ClickHouse rejected the query: " + msg[:400])


# ── coverage gate ────────────────────────────────────────────────────────────
_COV_LOCK = threading.Lock()
_COV: dict | None = None


def invalidate_coverage() -> None:
    global _COV
    with _COV_LOCK:
        _COV = None


def coverage(force: bool = False) -> dict:
    """Is the whole table there right now? Strict count() vs the measured floor,
    cached for COVERAGE_TTL (a failure is retried after COVERAGE_FAILURE_TTL)."""
    global _COV
    with _COV_LOCK:
        hit = _COV
        if hit and not force:
            ttl = config.COVERAGE_FAILURE_TTL if hit.get("error") else config.COVERAGE_TTL
            age = time.time() - hit["checked_at"]
            if age < ttl:
                return {**hit, "age_seconds": round(age, 1)}
        _COV = _measure()
        return {**_COV, "age_seconds": 0.0}


def _measure() -> dict:
    exp = config.EXPECTED_ROWS
    base = {"table": TABLE, "expected": exp, "strict_shard_read": True,
            "checked_at": time.time(), "ttl_seconds": config.COVERAGE_TTL}
    try:
        n = scalar_int(f"SELECT count() FROM {TABLE}", timeout=20)
    except Exception as e:
        log.warning("coverage measurement failed: %s", e)
        return {**base, "rows": None, "pct": None, "partial": True,
                "error": f"{type(e).__name__}: {e}"[:300]}
    return {**base, "rows": n, "pct": round(100.0 * n / exp, 2) if exp else 100.0,
            "partial": n < exp,
            "completeness": ("reachability and the historical row floor, not an "
                             "ingest completeness proof")}


def coverage_summary() -> dict:
    c = coverage()
    return {k: c.get(k) for k in ("rows", "expected", "pct", "partial",
                                   "strict_shard_read", "age_seconds", "error")
            if k in c}


def require_coverage() -> dict:
    """Called BEFORE any query a payload depends on. Partial → 503."""
    c = coverage()
    if c.get("partial") and config.PARTIAL_CAPTURE and c.get("rows"):
        log.warning("partial serving: %s of %s rows", c["rows"], c["expected"])
        return c
    if c.get("partial"):
        why = c.get("error") or (f"strict row count {c.get('rows'):,} is below the "
                                 f"measured floor {c['expected']:,}")
        raise ApiError("coverage_unavailable",
                       "the corpus is not fully available right now; no partial "
                       "answer is returned. " + why,
                       meta={"coverage": coverage_summary()})
    return c


def partial_note() -> str | None:
    """The lower-bound note added to every response while partial serving answers
    from the reachable part of the archive. None when the archive is complete."""
    if not config.PARTIAL_CAPTURE:
        return None
    try:
        c = coverage()
    except Exception:                      # the note never fails a request
        return None
    if not c.get("partial"):
        return None
    share = f"about {c['pct']:.0f}% of" if c.get("pct") else "part of"
    return (f"Part of the archive is temporarily offline; this answer uses {share} archived "
            "articles, so counts are lower bounds.")


# ── data_through ─────────────────────────────────────────────────────────────
_DT_LOCK = threading.Lock()
_DT: tuple[str, float] | None = None


def data_through(force: bool = False) -> str:
    """`max(datetime)` as an ISO date, cached hourly. The default window ends
    here, never at "today"."""
    global _DT
    with _DT_LOCK:
        if _DT and not force and time.time() - _DT[1] < config.DATA_THROUGH_TTL:
            return _DT[0]
        try:
            r = one(f"SELECT toString(toDate(max(datetime))) FROM {TABLE}", timeout=20)
        except CHError as e:
            if _DT:                       # stale is better than no bound
                return _DT[0]
            raise as_api_error(e)
        if not r or not r[0] or r[0].startswith("1970"):
            raise ApiError("coverage_unavailable", "could not determine data_through")
        _DT = (r[0], time.time())
        return _DT[0]


def freshness_note() -> str:
    return config.FRESHNESS_NOTE
