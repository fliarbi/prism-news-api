"""headlines — GET /v1/headlines (and the /themes/{name}/headlines,
/classes/{code}/headlines aliases).

ClickHouse returns `limit + 1` signal rows under the filter set (keyset order)
plus a `count()` under the same WHERE for `total_estimate`. The ids are
resolved against the article-store ring; ids with no record are dropped and
counted in `data.unresolved` (rotated out of the store — not an error), and
duplicates by URL are dropped. `next_cursor` is the keyset position of the
last CH row on the page, so a page that shrank through dedupe still pages on
without skipping."""
from __future__ import annotations

import time

from .. import articles, ch, envelope, filters
from ..auth import Principal
from . import _common as c


def headlines(p: Principal, f: filters.Filters, *, feature: str = "news.headlines",
              extra_classes=(), extra_themes=()) -> dict:
    t0 = time.time()
    r, window, _dt = c.begin(p, f, extra_classes=extra_classes, extra_themes=extra_themes)
    where = filters.where_sql(r)
    where_nocursor = filters.where_sql(r, with_cursor=False)
    sql_rows = (f"SELECT {c.HEADLINE_COLS} FROM {ch.TABLE} WHERE {where} "
                f"ORDER BY {filters.order_sql(r)} LIMIT {r.limit + 1}")
    sql_count = f"SELECT count() FROM {ch.TABLE} WHERE {where_nocursor}"
    rows, total = c.run_ch(lambda: ch.parallel([lambda: ch.rows(sql_rows),
                                                lambda: ch.scalar_int(sql_count)]))
    if total == 0:
        raise envelope.ApiError("no_data", "no article matches these filters in the window",
                                meta={"seconds": round(time.time() - t0, 3),
                                      "coverage": ch.coverage_summary(), "notes": r.notes})
    has_more = len(rows) > r.limit
    page = rows[:r.limit]
    next_cursor = None
    if has_more and page:
        last = page[-1]
        next_cursor = filters.cursor_for(r, last[1], last[0], int(last[2] or 0))

    recs, store_errors = articles.resolve([row[0] for row in page], full=False)
    items, seen, unresolved, dups = [], set(), 0, 0
    for row in page:
        rec = recs.get(row[0])
        if not rec or not rec.get("url"):
            unresolved += 1
            continue
        if rec["url"] in seen:
            dups += 1
            continue
        seen.add(rec["url"])
        items.append(c.item_of(row, rec))

    notes = list(r.notes) + c.store_notes(store_errors)
    if unresolved:
        notes.append(f"{unresolved} requested article(s) are unavailable")
    data = envelope.list_data(items, total_estimate=total, next_cursor=next_cursor,
                              unresolved=unresolved, duplicates_dropped=dups,
                              limit=r.limit, sort=r.sort)
    return envelope.ok(feature, data, subject={"filters": r.subject()}, window=window,
                       meta=c.meta(t0, notes))
