"""Measured exploration over the common, plan-bounded article filters.

Counts are exact query results, including zero. Percentages with an empty
denominator are null. Discovery always requires a user-supplied phrase.
No feature generates text or accepts query fragments from the caller.
"""
from __future__ import annotations

import re
import time
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .. import articles, ch, config, envelope, filters, taxonomy
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c


class ExplorationFilters(filters.Filters):
    """The shared article filters with public-facing field descriptions."""

    q: str | None = Field(None, description="Phrase to explore; 2–120 characters.")
    match: Literal["any", "opening", "focused"] | None = Field(
        None, description="Search breadth: any, opening, or focused.")
    country: str | None = Field(None, description="Country name; location availability varies by period.")


class DiscoveryFilters(ExplorationFilters):
    """Article filters for phrase-scoped discovery."""

    q: str = Field(..., min_length=2, max_length=120, description="Required phrase to explore.")
    limit: int = Field(100, ge=1, description="Headlines per page; bounded by your plan.")


class GeographyFilters(DiscoveryFilters):
    """Phrase-scoped country ranking, never a country directory."""

    limit: int = Field(5, ge=1, le=5, description="Countries to return, from 1 to 5.")


class ComparisonSet(BaseModel):
    """A display name and one complete set of article filters."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    name: str = Field(..., min_length=1, max_length=80)
    filters: ExplorationFilters


class CompareRequest(BaseModel):
    """Two to five sets; names must be unique ignoring case and whitespace."""

    model_config = ConfigDict(extra="forbid")
    queries: list[ComparisonSet] = Field(..., min_length=2, max_length=5)

    @model_validator(mode="after")
    def unique_names(self):
        names = [" ".join(s.name.split()).casefold() for s in self.queries]
        if len(set(names)) != len(names):
            raise ValueError("Comparison names must be unique.")
        return self


def _input(f: filters.Filters, *, discovery: bool = False) -> filters.Filters:
    if discovery and not (f.q and f.q.strip()):
        raise ApiError("bad_request", "A nonempty `q` is required for discovery.")
    return f


def _subject(r: filters.Resolved) -> dict:
    return r.subject()


def _notes(r: filters.Resolved) -> list[str]:
    return ["Location information is incomplete and varies by period."
            if n == config.COUNTRY_NOTE else n for n in r.notes]


def _meta(t0: float, notes=()) -> dict:
    # Operational diagnostics belong in the parent application's private logs.
    return {"seconds": round(time.time() - t0, 3), "notes": list(notes)}


def _begin(p: Principal, f: filters.Filters, *, discovery=False):
    return c.begin(p, _input(f, discovery=discovery), default_limit=100)


def _counts(sql: str, size: int) -> list[int]:
    row = c.run_ch(lambda: ch.one(sql))
    if row is None or len(row) != size or any(v is None for v in row):
        raise ApiError("upstream", "The requested counts could not be retrieved.")
    counts = [int(v) for v in row]
    if any(n < 0 for n in counts):
        raise ApiError("upstream", "The requested counts could not be retrieved.")
    return counts


_SENTIMENT = f"({ch.HAS_SENTIMENT} AND {ch.TOP_SENTIMENT} IN {ch.sql_in(taxonomy.SENTIMENTS)})"
_PRIORITY = f"({ch.HAS_PRIORITY} AND {ch.TOP_PRIORITY} BETWEEN 1 AND 9)"
_THEME = "arrayExists(x -> notEmpty(trimBoth(x.1)), subcats)"
_COUNTRY = "lowerUTF8(trimBoth(ifNull(country_pri, '')))"
_LOCATION = f"notEmpty({_COUNTRY})"


def overview(p: Principal, f: filters.Filters) -> dict:
    """Counts, tone shares among labelled articles, and critical priority share."""
    t0 = time.time()
    r, window, _ = _begin(p, f)
    r.cursor = None
    expressions = ["count()", f"countIf({_SENTIMENT})"]
    expressions.extend(f"countIf({_SENTIMENT} AND {ch.TOP_SENTIMENT} IN {ch.sql_in(labels)})"
                       for labels in taxonomy.GROUPS.values())
    expressions.extend([f"countIf({_PRIORITY})",
                        f"countIf({_PRIORITY} AND {ch.TOP_PRIORITY} >= {config.CRITICAL_PRIORITY})"])
    n, carrying, negative, neutral, positive, priority_n, critical = _counts(
        f"SELECT {', '.join(expressions)} FROM {ch.TABLE} WHERE {filters.where_sql(r, with_cursor=False)}", 7)
    data = {
        "matched": n,
        "tone": {"carrying": carrying, "availability_pct": c.pct(carrying, n),
                 "groups": [{"group": group, "count": count, "share_pct": c.pct(count, carrying)}
                            for group, count in zip(taxonomy.GROUPS, (negative, neutral, positive))]},
        "critical": {"min_priority": config.CRITICAL_PRIORITY, "carrying": priority_n,
                     "count": critical, "share_pct": c.pct(critical, priority_n)},
    }
    return envelope.ok("news.overview", data, subject={"filters": _subject(r)}, window=window,
                       meta=_meta(t0, _notes(r) + ["Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating."]))


def compare(p: Principal, req: CompareRequest) -> dict:
    """One measured date bound, one exact union and a count for every set.

    Shares use the union as denominator. Overlapping sets can sum above 100%.
    Each set retains its own requested, plan-bounded window.
    """
    t0 = time.time()
    first, _, dt = _begin(p, req.queries[0].filters)
    resolved = [first]
    # Resolve every set BEFORE the scan so an invalid later set cannot result
    # in a partial comparison. Never fetch another date bound inside this loop.
    for named in req.queries[1:]:
        resolved.append(filters.resolve(_input(named.filters), p.plan_cfg, dt, default_limit=100))
    for r in resolved:
        r.cursor = None
    predicates = [filters.where_sql(r, with_cursor=False) for r in resolved]
    expressions = ["count()"] + [f"countIf({where})" for where in predicates]
    union_where = " OR ".join(f"({where})" for where in predicates)
    total, *counts = _counts(f"SELECT {', '.join(expressions)} FROM {ch.TABLE} WHERE {union_where}",
                            len(resolved) + 1)
    items = [{"name": named.name, "count": count, "share_pct": c.pct(count, total),
              "filters": _subject(r), "window": filters.window_of(r, dt)}
             for named, r, count in zip(req.queries, resolved, counts)]
    data = {"items": items, "matched": total, "share_basis": "articles matching at least one set",
            "sets_may_overlap": True}
    return envelope.ok("news.compare", data, subject={"names": [s.name for s in req.queries]},
                       window={"data_through": dt, "freshness": ch.freshness_note()},
                       meta=_meta(t0, [f"{s.name}: {n}" for s, r in zip(req.queries, resolved) for n in _notes(r)]
                                  + ["Set windows are shown individually. Overlapping shares may sum above 100%."]))


def geography(p: Principal, f: filters.Filters) -> dict:
    """Up to five countries for a phrase, with availability and exact totals."""
    t0 = time.time()
    r, window, _ = _begin(p, f, discovery=True)
    r.cursor = None
    where = filters.where_sql(r, with_cursor=False)
    limit = min(5, r.limit)
    totals_sql = f"SELECT count(), countIf({_LOCATION}) FROM {ch.TABLE} WHERE {where}"
    countries_sql = (f"SELECT {_COUNTRY} AS country, count() AS articles FROM {ch.TABLE} "
                     f"WHERE {where} AND {_LOCATION} GROUP BY country "
                     f"ORDER BY articles DESC, country ASC LIMIT {limit}")
    totals, rows = c.run_ch(lambda: ch.parallel([lambda: _counts(totals_sql, 2), lambda: ch.rows(countries_sql)]))
    matched, carrying = totals
    items = [{"country": country, "count": int(count), "share_pct": c.pct(int(count), matched)}
             for country, count in rows]
    data = {"matched": matched, "carrying": carrying, "availability_pct": c.pct(carrying, matched),
            "items": items, "returned": len(items), "limit": limit,
            "other_located_count": carrying - sum(i["count"] for i in items)}
    return envelope.ok("news.geography", data, subject={"filters": _subject(r)}, window=window,
                       meta=_meta(t0, _notes(r) + ["Country shares use all matching articles. Location information is incomplete and varies by period."]))


def coverage(p: Principal, f: filters.Filters) -> dict:
    """Availability of sentiment, theme and location within the matching set."""
    t0 = time.time()
    r, window, _ = _begin(p, f)
    r.cursor = None
    n, sentiment, theme, location = _counts(
        f"SELECT count(), countIf({_SENTIMENT}), countIf({_THEME}), countIf({_LOCATION}) "
        f"FROM {ch.TABLE} WHERE {filters.where_sql(r, with_cursor=False)}", 4)
    data = {"matched": n, "availability": {
        name: {"count": count, "percentage": c.pct(count, n)}
        for name, count in (("sentiment", sentiment), ("theme", theme), ("location", location))}}
    return envelope.ok("news.coverage", data, subject={"filters": _subject(r)}, window=window,
                       meta=_meta(t0, _notes(r) + ["Availability is measured within these filters; zero matches have null percentages."]))


def related(p: Principal, article_id: str, f: filters.Filters) -> dict:
    """Headlines sharing any of five seed themes AND all caller filters.

    The seed must exist within the resolved date window. Caller theme filters
    form a separate predicate; merging the two theme lists would broaden them.
    Pagination and the count exclude the seed. Headline delivery uses no exports.
    """
    t0 = time.time()
    aid = (article_id or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{24}", aid):
        raise ApiError("bad_request", "Article id must be a 24-character hexadecimal headline id.")
    r, window, _ = _begin(p, f, discovery=True)
    theme_expr = ("arraySlice(arrayDistinct(arrayFilter(x -> notEmpty(x), "
                  "arrayMap(x -> lowerUTF8(trimBoth(x.1)), arraySort(x -> -x.2, subcats)))), 1, 5)")
    seed_sql = (f"SELECT {theme_expr} FROM {ch.TABLE} WHERE target_id = {ch.sql_str(aid)} "
                f"AND datetime >= {ch.sql_str(r.since)} AND datetime < {ch.sql_str(r.until_exclusive)} LIMIT 1")
    seed = c.run_ch(lambda: ch.one(seed_sql))
    if not seed:
        raise ApiError("no_data", "The seed article is not available in the permitted date window.")
    seed_themes = list(dict.fromkeys(str(t).strip().lower() for t in seed[0] if str(t).strip()))[:5]
    if not seed_themes:
        raise ApiError("no_data", "The seed article has no themes available for related discovery.")
    r.extra_sql.extend([f"target_id != {ch.sql_str(aid)}",
                        f"arrayExists(x -> lowerUTF8(trimBoth(x.1)) IN {ch.sql_in(seed_themes)}, subcats)"])
    where = filters.where_sql(r)
    count_sql = f"SELECT count() FROM {ch.TABLE} WHERE {filters.where_sql(r, with_cursor=False)}"
    rows_sql = (f"SELECT {c.HEADLINE_COLS} FROM {ch.TABLE} WHERE {where} "
                f"ORDER BY {filters.order_sql(r)} LIMIT {r.limit + 1}")
    rows, total = c.run_ch(lambda: ch.parallel([lambda: ch.rows(rows_sql), lambda: ch.scalar_int(count_sql)]))
    page = rows[:r.limit]
    next_cursor = None
    if len(rows) > r.limit and page:
        last = page[-1]
        next_cursor = filters.cursor_for(r, last[1], last[0], int(last[2] or 0))
    recs, errors = articles.resolve([row[0] for row in page], full=False) if page else ({}, [])
    items, seen, unresolved, duplicates = [], set(), 0, 0
    for row in page:
        rec = recs.get(row[0])
        if not rec or not rec.get("url"):
            unresolved += 1
        elif rec["url"] in seen:
            duplicates += 1
        else:
            seen.add(rec["url"])
            items.append(c.item_of(row, rec))
    notes = _notes(r)
    if errors:
        notes.append("Some article details are temporarily unavailable.")
    if unresolved:
        notes.append("Some matching articles have no retrievable headline details.")
    data = envelope.list_data(items, total_estimate=total, next_cursor=next_cursor,
                              unresolved=unresolved, duplicates_dropped=duplicates,
                              limit=r.limit, sort=r.sort)
    return envelope.ok("news.related", data, subject={"id": aid, "filters": _subject(r)},
                       window=window, meta=_meta(t0, notes))
