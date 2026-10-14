"""priority — GET /v1/priority: the 1–9 distribution, critical share (>= 7),
against the 30-day corpus baseline. Shares divide by articles that CARRY
`priorities` (99.9%)."""
from __future__ import annotations

import time

from .. import ch, config, envelope, filters, taxonomy
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.priority"


def priority(p: Principal, f: filters.Filters) -> dict:
    t0 = time.time()
    r, window, dt = c.begin(p, f)
    r.cursor = None
    where = filters.where_sql(r, with_cursor=False)
    sql = (f"SELECT {ch.TOP_PRIORITY} AS band, count() FROM {ch.TABLE} "
           f"WHERE {where} AND {ch.HAS_PRIORITY} GROUP BY band ORDER BY band")
    sql_tot = f"SELECT count() FROM {ch.TABLE} WHERE {where}"
    rows, matched = c.run_ch(lambda: ch.parallel([lambda: ch.rows(sql), lambda: ch.scalar_int(sql_tot)]))
    if matched == 0:
        raise ApiError("no_data", "no article matches these filters in the window", meta={"notes": r.notes})
    counts = {b: 0 for b in taxonomy.PRIORITY_BANDS}
    for band, n in rows:
        if int(band) in counts:
            counts[int(band)] += int(n)
    carrying = sum(counts.values())
    critical = sum(v for b, v in counts.items() if b >= config.CRITICAL_PRIORITY)
    mean = round(sum(b * v for b, v in counts.items()) / carrying, 3) if carrying else None

    base = c.baseline("priority", f"[{ch.TOP_PRIORITY}]", ch.HAS_PRIORITY, dt)
    b_counts = {int(k): v for k, v in base["counts"].items() if str(k).lstrip("-").isdigit()}
    b_carry = sum(b_counts.values())
    b_critical = sum(v for b, v in b_counts.items() if b >= config.CRITICAL_PRIORITY)
    crit_share, b_crit_share = c.pct(critical, carrying), c.pct(b_critical, b_carry)

    data = {
        "matched": matched, "carrying": carrying, "carrier_share_pct": c.pct(carrying, matched),
        "bands": [{"band": b, "count": counts[b], "share": c.pct(counts[b], carrying),
                   "critical": b >= config.CRITICAL_PRIORITY,
                   "baseline_share": c.pct(b_counts.get(b, 0), b_carry)} for b in taxonomy.PRIORITY_BANDS],
        "critical": {"min_band": config.CRITICAL_PRIORITY, "count": critical, "share": crit_share},
        "mean_priority": mean,
        "baseline": {**c.baseline_block(base), "critical_share": b_crit_share,
                     "mean_priority": round(sum(b * v for b, v in b_counts.items()) / b_carry, 3) if b_carry else None},
        "vs_baseline_critical": round(crit_share / b_crit_share, 2) if crit_share and b_crit_share else None,
    }
    notes = list(r.notes) + ["shares divide by articles carrying a priority band (the top-scoring one)"]
    return envelope.ok(FEATURE, data, subject={"filters": r.subject()}, window=window,
                       meta=c.meta(t0, notes))
