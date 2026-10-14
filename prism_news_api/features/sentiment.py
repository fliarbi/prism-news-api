"""sentiment — GET /v1/sentiment: 9-label + 3-group distribution and a timeline.

One article, one label (the highest-scoring of up to three). Shares divide by
articles that CARRY `sentiments` (99.8%). The negative:positive ratio is shown
against the 30-day corpus baseline because news runs negative in general — a
set at 1.3 is not "mostly negative", it is twice as negative as ordinary
coverage."""
from __future__ import annotations

import time

from .. import ch, envelope, filters, taxonomy
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.sentiment"


def _groups(counts: dict) -> dict:
    g = {k: 0 for k in taxonomy.GROUPS}
    for lbl, n in counts.items():
        grp = taxonomy.group_of(lbl)
        if grp:
            g[grp] += n
    return g


def sentiment(p: Principal, f: filters.Filters, granularity: str | None = None) -> dict:
    t0 = time.time()
    g = c.check_granularity(granularity)
    r, window, dt = c.begin(p, f)
    r.cursor = None
    where = filters.where_sql(r, with_cursor=False)
    sql = (f"SELECT toString({ch.GRANULARITY_SQL[g]}) AS period, {ch.TOP_SENTIMENT} AS label, count() "
           f"FROM {ch.TABLE} WHERE {where} AND {ch.HAS_SENTIMENT} GROUP BY period, label ORDER BY period")
    sql_tot = f"SELECT count() FROM {ch.TABLE} WHERE {where}"
    rows, matched = c.run_ch(lambda: ch.parallel([lambda: ch.rows(sql), lambda: ch.scalar_int(sql_tot)]))
    if matched == 0:
        raise ApiError("no_data", "no article matches these filters in the window", meta={"notes": r.notes})

    totals = {l: 0 for l in taxonomy.SENTIMENTS}
    by_period: dict[str, dict] = {}
    for period, label, n in rows:
        n = int(n)
        if label in totals:
            totals[label] += n
        by_period.setdefault(period, {l: 0 for l in taxonomy.SENTIMENTS})
        if label in by_period[period]:
            by_period[period][label] += n
    carrying = sum(totals.values())
    groups = _groups(totals)
    ratio = round(groups["negative"] / groups["positive"], 3) if groups["positive"] else None

    base = c.baseline("sentiment", f"[{ch.TOP_SENTIMENT}]", ch.HAS_SENTIMENT, dt)
    b_groups = _groups(base["counts"])
    b_carry = sum(b_groups.values())
    b_ratio = round(b_groups["negative"] / b_groups["positive"], 3) if b_groups["positive"] else None

    timeline = []
    for per in c.periods(r.since, r.until, g):
        lab = by_period.get(per["period"], {l: 0 for l in taxonomy.SENTIMENTS})
        gr = _groups(lab)
        tot = sum(lab.values())
        timeline.append({"period": per["period"], "total": tot, **gr,
                         "negative_share": c.pct(gr["negative"], tot),
                         "positive_share": c.pct(gr["positive"], tot),
                         "labels": lab, "partial_period": per["partial_period"]})

    data = {
        "matched": matched, "carrying": carrying, "carrier_share_pct": c.pct(carrying, matched),
        "labels": [{"label": l, "group": taxonomy.group_of(l), "count": totals[l],
                    "share": c.pct(totals[l], carrying)} for l in taxonomy.SENTIMENTS],
        "groups": [{"group": k, "count": v, "share": c.pct(v, carrying)} for k, v in groups.items()],
        "negative_to_positive_ratio": ratio,
        "baseline": {**c.baseline_block(base),
                     "groups": {k: {"count": v, "share": c.pct(v, b_carry)} for k, v in b_groups.items()},
                     "negative_to_positive_ratio": b_ratio},
        "vs_baseline_ratio": round(ratio / b_ratio, 2) if ratio and b_ratio else None,
        "granularity": g, "timeline": timeline,
    }
    notes = list(r.notes) + ["shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)"]
    return envelope.ok(FEATURE, data, subject={"filters": r.subject(), "granularity": g},
                       window={**window, "granularity": g}, meta=c.meta(t0, notes))
