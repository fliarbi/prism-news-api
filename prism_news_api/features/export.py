"""export — POST /v1/export: full article bodies for a filter set.

    reserve N -> fetch via the ring (batched per node) -> deliver -> refund
    whatever was not delivered

so a failure after the reserve never burns quota (radar's export-credit
pattern, in Redis). Formats:

    json    the envelope, articles in data.items
    ndjson  line 1 = the envelope with "stream": true and no items; then one
            article object per line
    csv     id, headline, url, publisher, published_at, sentiment, priority,
            classes, themes, body

Charged per article DELIVERED. Default and cap 100 per call on every tier
(plan `max_export_batch`), bounded further by the month's remaining exports.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import time
from typing import Optional

from pydantic import Field

from .. import articles, ch, config, envelope, filters, quota
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.export"
CSV_COLUMNS = ("id", "headline", "url", "publisher", "published_at", "sentiment",
               "priority", "classes", "body")


class ExportRequest(filters.Filters):
    format: Optional[str] = Field("json", description="json | ndjson | csv")


def run(p: Principal, req: ExportRequest, endpoint: str = "/v1/export") -> dict:
    """-> {"format", "envelope", "items"}; the router serialises per format."""
    t0 = time.time()
    fmt = (req.format or "json").strip().lower()
    if fmt not in config.EXPORT_FORMATS:
        raise ApiError("bad_request", f"`format` must be one of {', '.join(config.EXPORT_FORMATS)}")

    r, window, _dt = c.begin(p, req, default_limit=config.DEFAULT_LIMIT,
                             cap_field="max_export_batch")
    limit = int(p.plan_cfg.get("exports_per_month") or 0)
    remaining = quota.exports_remaining(p.user_id, p.key_id, limit)
    if remaining <= 0:
        raise ApiError("quota_exceeded",
                       f"monthly export quota reached ({limit:,}/{limit:,}); resets on the 1st (UTC). "
                       f"Upgrade at {config.UPGRADE_URL}",
                       fields={"upgrade_url": config.UPGRADE_URL})
    if r.limit > remaining:
        r.notes.append(f"only {remaining} export(s) left this month; limit reduced from {r.limit}")
        r.limit = remaining

    where = filters.where_sql(r)
    sql_rows = (f"SELECT {c.HEADLINE_COLS} FROM {ch.TABLE} WHERE {where} "
                f"ORDER BY {filters.order_sql(r)} LIMIT {r.limit + 1}")
    sql_count = f"SELECT count() FROM {ch.TABLE} WHERE {filters.where_sql(r, with_cursor=False)}"
    rows, total = c.run_ch(lambda: ch.parallel([lambda: ch.rows(sql_rows),
                                                lambda: ch.scalar_int(sql_count)]))
    if total == 0:
        raise ApiError("no_data", "no article matches these filters in the window",
                       meta={"notes": r.notes})
    has_more = len(rows) > r.limit
    page = rows[:r.limit]

    granted = quota.reserve_exports(p.user_id, p.key_id, len(page), limit)
    if granted < len(page):
        r.notes.append(f"export batch reduced to {granted} by the remaining monthly quota")
        page, has_more = page[:granted], True
    try:
        recs, store_errors = articles.resolve([row[0] for row in page], full=True)
        items, seen, unresolved, dups = [], set(), 0, 0
        for row in page:
            rec = recs.get(row[0])
            if not rec or not rec.get("url"):
                unresolved += 1
                continue
            # Republished copies often differ only in a URL suffix (…-175/, …-176/):
            # the same body from the same publisher is one article, delivered once.
            body_key = (rec.get("publisher"), hashlib.sha1((rec.get("body") or "").encode()).hexdigest()) \
                if rec.get("body") else None
            if rec["url"] in seen or (body_key and body_key in seen):
                dups += 1
                continue
            seen.add(rec["url"])
            if body_key:
                seen.add(body_key)
            items.append(c.item_of(row, rec, full=True))
    except BaseException:
        quota.refund_exports(p.user_id, p.key_id, granted)
        raise
    delivered = len(items)
    quota.refund_exports(p.user_id, p.key_id, granted - delivered)
    quota.record_daily(p.user_id, p.key_id, endpoint, requests=0, exports=delivered)

    next_cursor = None
    if has_more and page:
        last = page[-1]
        next_cursor = filters.cursor_for(r, last[1], last[0], int(last[2] or 0))
    notes = list(r.notes) + c.store_notes(store_errors)
    if unresolved:
        notes.append(f"{unresolved} requested article(s) are unavailable; not charged")
    data = envelope.list_data(items, total_estimate=total, next_cursor=next_cursor,
                              unresolved=unresolved, duplicates_dropped=dups,
                              charged_exports=delivered, format=fmt, limit=r.limit)
    env = envelope.ok(FEATURE, data, subject={"filters": r.subject(), "format": fmt},
                      window=window, meta=c.meta(t0, notes))
    return {"format": fmt, "envelope": env, "items": items}


# ── serialisers ──────────────────────────────────────────────────────────────
def _dumps(o) -> str:
    return json.dumps(o, ensure_ascii=False, default=str)


def to_ndjson(result: dict) -> str:
    env = dict(result["envelope"])
    data = dict(env["data"])
    data.pop("items", None)
    data["stream"] = True
    env["data"] = data
    lines = [_dumps(env)] + [_dumps(it) for it in result["items"]]
    return "\n".join(lines) + "\n"


def to_csv(result: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(CSV_COLUMNS)
    for it in result["items"]:
        s = it.get("sentiment") or {}
        w.writerow([
            it.get("id"), it.get("headline"), it.get("url"), it.get("publisher"),
            it.get("published_at"), s.get("label"), it.get("priority"),
            "|".join(f"{k['code']}:{k['path']}" for k in it.get("classes") or []),
            it.get("body") or "",
        ])
    return buf.getvalue()
