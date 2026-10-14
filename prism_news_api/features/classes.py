"""classes — the GCP class code map, with volumes.

    GET /v1/classes?q=&prefix=      code, path, depth, parent, articles_30d
    GET /v1/classes/{code}          one class: volume + top themes (30 days)
    GET /v1/classes/{code}/headlines  = /v1/headlines with classes=code

The code map is static; `articles_30d` comes from a corpus baseline cached
24 h (`pna:baseline:classes`). These paths are unmetered, so when the cluster
is thin the map is still served with `articles_30d: null` and a note rather
than a 503 — a volume that is absent is not a partial count."""
from __future__ import annotations

import time

from .. import ch, config, envelope, filters, quota, taxonomy
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c
from . import headlines as _headlines

CLASS_LABEL_EXPR = f"arrayMap(x -> x.1, arrayFilter(x -> x.2 > {config.CLASS_THRESHOLD}, classification))"
CLASS_CARRIER = f"arrayExists(x -> x.2 > {config.CLASS_THRESHOLD}, classification)"


def _volumes() -> tuple[dict | None, str | None, str | None]:
    try:
        ch.require_coverage()
        dt = ch.data_through()
        return c.baseline("classes", CLASS_LABEL_EXPR, CLASS_CARRIER, dt), dt, None
    except ApiError as e:
        return None, None, f"30-day volumes unavailable: {e.reason[:160]}"


def list_classes(p: Principal, q: str | None = None, prefix: str | None = None, limit: int = 5) -> dict:
    t0 = time.time()
    if not (q and len(q.strip()) >= 2 and sum(c.isalnum() for c in q) >= 2) and not (prefix and prefix.strip("/ ")):
        raise ApiError("bad_request", "Provide q or a content class prefix to find up to five class codes.")
    if prefix and not taxonomy.expand_prefix(prefix):
        raise ApiError("bad_request", f"no GCP class under prefix {taxonomy.normalise_prefix(prefix)!r}")
    entries = taxonomy.search(q, prefix)
    base, dt, note = _volumes()
    for e in entries:
        e["articles_30d"] = (base["counts"].get(e["path"], 0) if base else None)
    entries.sort(key=lambda e: (-(e["articles_30d"] or 0), e["code"]))
    data = envelope.list_data(entries[:max(1, min(int(limit), 5))], total_estimate=None, next_cursor=None,
                              class_count=taxonomy.CLASS_COUNT,
                              score_threshold=config.CLASS_THRESHOLD,
                              baseline=c.baseline_block(base) if base else None)
    window = ({"since": base["since"], "until": base["until"], "data_through": dt,
               "freshness": ch.freshness_note()} if base else {"freshness": ch.freshness_note()})
    return envelope.ok("news.classes", data,
                       subject={"q": q, "prefix": taxonomy.normalise_prefix(prefix) if prefix else None},
                       window=window, meta=c.meta(t0, [note]))


def one_class(p: Principal, code: int) -> dict:
    t0 = time.time()
    try:
        [code_i] = taxonomy.validate_codes([code])
    except ValueError as e:
        raise ApiError("bad_request", str(e))
    entry = taxonomy.class_entry(code_i)
    entry["children"] = [taxonomy.class_entry(k) for k in taxonomy.children_of(entry["path"])[:5]]
    base, dt, note = _volumes()
    entry["articles_30d"] = base["counts"].get(entry["path"], 0) if base else None
    notes = [note]
    window = ({"since": base["since"], "until": base["until"], "data_through": dt,
               "freshness": ch.freshness_note()} if base else {"freshness": ch.freshness_note()})
    return envelope.ok("news.class", entry, subject={"code": code_i}, window=window,
                       meta=c.meta(t0, notes))


def class_headlines(p: Principal, code: int, f: filters.Filters) -> dict:
    try:
        [code_i] = taxonomy.validate_codes([code])
    except ValueError as e:
        raise ApiError("bad_request", str(e))
    return _headlines.headlines(p, f, feature="news.class_headlines", extra_classes=[code_i])
