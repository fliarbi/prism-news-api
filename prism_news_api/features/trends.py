"""trends — GET /v1/trends: article volume over time for the filter set, with
the critical (priority >= 7) and tone series beside it. Empty buckets are
filled with zeros; buckets the window only partly covers are flagged
`partial_period` so a half-week at either edge is not read as a drop."""
from __future__ import annotations

import time

from .. import ch, config, envelope, filters
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.trends"


def trends(p: Principal, f: filters.Filters, granularity: str | None = None) -> dict:
    t0 = time.time()
    g = c.check_granularity(granularity)
    r, window, _dt = c.begin(p, f)
    r.cursor = None
    where = filters.where_sql(r, with_cursor=False)
    sql = (f"SELECT toString({ch.GRANULARITY_SQL[g]}) AS period, count() AS n, "
           f"countIf({ch.TOP_PRIORITY} >= {config.CRITICAL_PRIORITY}) AS critical, "
           f"countIf({ch.POLARITY} = 'neg') AS neg, countIf({ch.POLARITY} = 'pos') AS pos "
           f"FROM {ch.TABLE} WHERE {where} GROUP BY period ORDER BY period")
    rows = c.run_ch(lambda: ch.rows(sql))
    if not rows:
        raise ApiError("no_data", "no article matches these filters in the window", meta={"notes": r.notes})
    got = {row[0]: row for row in rows}
    points = []
    for per in c.periods(r.since, r.until, g):
        row = got.get(per["period"])
        n, crit, neg, pos = (int(row[1]), int(row[2]), int(row[3]), int(row[4])) if row else (0, 0, 0, 0)
        points.append({"period": per["period"], "articles": n, "critical": crit,
                       "critical_pct": c.pct(crit, n, 1), "negative": neg, "positive": pos,
                       "partial_period": per["partial_period"]})
    total = sum(p_["articles"] for p_ in points)
    complete = [p_ for p_ in points if not p_["partial_period"]]
    data = {"granularity": g, "points": points, "total": total,
            "critical_total": sum(p_["critical"] for p_ in points),
            "complete_periods": len(complete), "partial_periods": len(points) - len(complete),
            "peak": max(points, key=lambda x: x["articles"])["period"] if points else None}
    notes = list(r.notes) + ["zero-count periods are included; partial_period marks buckets the window only partly covers"]
    return envelope.ok(FEATURE, data, subject={"filters": r.subject(), "granularity": g},
                       window={**window, "granularity": g}, meta=c.meta(t0, notes))
