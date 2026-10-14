"""themes — GET /v1/themes: "most potential themes" inside a filter set.

A theme's LIFT is its share among the filter set's theme-carrying articles
divided by its share in the 30-day corpus baseline (cached 24 h in Redis
`pna:baseline:subcats`). Raw counts alone rank the corpus, not the filter
set — 'professional league updates' tops everything — and lift is what
isolates what is unusually common HERE.

Ranking is lift weighted by sqrt(count): with a floor of only 5 articles,
pure lift would be won by whichever rare label five syndicated copies of one
story happened to carry. `meta.ranked_by` says so.

Each row also carries the count in the immediately preceding window of the
same length under the same filters (`previous_period_count`, `delta_pct`).
Shares divide by articles that CARRY `subcats` (~59% of the corpus, 57% in
the default window), and the payload says how many that was."""
from __future__ import annotations

import math
import time
from datetime import date, timedelta

from .. import ch, config, envelope, filters
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.themes"
LABEL_EXPR = "arrayDistinct(arrayMap(x -> x.1, subcats))"


def themes(p: Principal, f: filters.Filters) -> dict:
    # Enforce this here too: business routes and composed features call this directly.
    query = (f.q or "").strip()
    if len(query) < 2 or len(query) > 120 or sum(c.isalnum() for c in query) < 2:
        raise ApiError("bad_request", "Provide a specific search phrase in q (2-120 characters) to discover themes.")
    if f.cursor:
        raise ApiError("bad_request", "Theme discovery returns up to five suggestions and does not support pagination.")
    t0 = time.time()
    r, window, dt = c.begin(p, f, default_limit=config.THEMES_DEFAULT_LIMIT,
                            cap=config.THEMES_MAX_LIMIT)
    r.cursor = None
    since = date.fromisoformat(r.since)
    prev_since = (since - timedelta(days=r.days)).isoformat()
    prev_until = (since - timedelta(days=1)).isoformat()
    history = p.plan_cfg.get("history_days")
    comparison_available = history is None or date.fromisoformat(prev_since) >= date.fromisoformat(dt) - timedelta(days=int(history))
    if not comparison_available:
        prev_since = r.since
        r.notes.append("Previous-period comparison is unavailable within your plan's history allowance.")
    inner = filters.where_sql(r, with_dates=False, with_cursor=False)
    both = (f"datetime >= {ch.sql_str(prev_since)} AND datetime < {ch.sql_str(r.until_exclusive)}"
            + (f" AND {inner}" if inner != "1" else ""))
    sql_dist = (
        f"SELECT label, countIf(recent) AS n, countIf(NOT recent) AS prev "
        f"FROM (SELECT arrayJoin({LABEL_EXPR}) AS label, datetime >= {ch.sql_str(r.since)} AS recent "
        f"      FROM {ch.TABLE} WHERE {both} AND {ch.HAS_SUBCATS}) "
        f"GROUP BY label HAVING n >= {config.THEMES_MIN_ARTICLES} ORDER BY n DESC LIMIT 4000")
    sql_tot = (f"SELECT count(), countIf({ch.HAS_SUBCATS}) FROM {ch.TABLE} "
               f"WHERE {filters.where_sql(r, with_cursor=False)}")
    rows, tot = c.run_ch(lambda: ch.parallel([lambda: ch.rows(sql_dist), lambda: ch.one(sql_tot)]))
    matched, carrying = int(tot[0]), int(tot[1])
    if matched == 0:
        raise ApiError("no_data", "no article matches these filters in the window",
                       meta={"notes": r.notes})
    if not rows:
        raise ApiError("no_data", f"no theme reaches {config.THEMES_MIN_ARTICLES} articles in this "
                                  f"filter set ({matched:,} articles, {carrying:,} carrying themes)",
                       meta={"notes": r.notes})

    base = c.baseline("subcats", LABEL_EXPR, ch.HAS_SUBCATS, dt)
    b_carry = base["carrying"] or 0
    items, ranked = [], []
    for label, n, prev in rows:
        n, prev = int(n), int(prev)
        if n < config.THEMES_MIN_ARTICLES:          # the HAVING says so too; belt and braces
            continue
        share = n / carrying if carrying else 0.0
        bn = base["counts"].get(label, 0)
        b_share = bn / b_carry if b_carry else 0.0
        lift = round(share / b_share, 2) if b_share else None
        # A theme absent from the baseline has no finite lift. Rank it by the
        # conservative bound "as if one baseline article carried it" rather
        # than a magic constant; the payload still says lift: null, new: true.
        rank_lift = share / max(b_share, (1.0 / b_carry) if b_carry else 1.0)
        ranked.append((rank_lift * math.sqrt(n),
                       {"theme": label, "count": n, "share": round(100 * share, 2),
                        "lift": lift, "baseline_count": bn,
                        "previous_period_count": prev if comparison_available else None,
                        "delta_pct": round(100.0 * (n - prev) / prev, 1) if prev and comparison_available else None,
                        "new_vs_baseline": bn == 0}))
    ranked.sort(key=lambda t: -t[0])
    items = [it for _, it in ranked[:r.limit]]
    data = envelope.list_data(
        items, total_estimate=None, next_cursor=None,
        matched=matched, carrying=carrying, carrier_share_pct=c.pct(carrying, matched),
        previous_period={"since": prev_since, "until": prev_until} if comparison_available else None,
        baseline=c.baseline_block(base), min_articles=config.THEMES_MIN_ARTICLES,
        ranked_by="lift over the theme's corpus-wide share, weighted by sqrt(count)")
    notes = list(r.notes) + ["Theme shares use articles with identified themes; articles may have more than one theme."]
    return envelope.ok(FEATURE, data, subject={"filters": r.subject()}, window=window,
                       meta=c.meta(t0, notes))
