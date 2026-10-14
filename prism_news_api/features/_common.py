"""_common — what every feature does before and after its query."""
from __future__ import annotations

import time
from datetime import date, timedelta

from .. import ch, config, filters, quota, taxonomy
from ..auth import Principal
from ..ch import CHError
from ..envelope import ApiError

# The signal columns every headline/article payload is built from. Kept as one
# string so headlines, export and the single-article fetch read identical rows.
HEADLINE_COLS = (
    f"target_id, toString(datetime), {ch.TOP_PRIORITY}, {ch.TOP_SENTIMENT_TUPLE}, "
    f"arrayFilter(x -> x.2 > {config.CLASS_THRESHOLD}, classification), "
    f"arraySlice(subcats, 1, 5), country_pri, pri_organization, pri_person, "
    f"assumeNotNull(text)"
)


def begin(p: Principal, f: filters.Filters, *, default_limit: int = config.DEFAULT_LIMIT,
          cap: int | None = None, cap_field: str = "max_results",
          extra_classes=(), extra_themes=()) -> tuple[filters.Resolved, dict, str]:
    """Coverage gate -> data_through -> plan-bounded filters -> window block.
    The gate runs FIRST so a thin cluster is a 503 before any work."""
    ch.require_coverage()
    dt = ch.data_through()
    plan_cap = p.plan_cfg.get(cap_field) or config.DEFAULT_LIMIT
    use_cap = min(int(cap), int(plan_cap)) if cap else int(plan_cap)
    r = filters.resolve(f, p.plan_cfg, dt, default_limit=min(default_limit, use_cap),
                        cap=use_cap, extra_classes=extra_classes, extra_themes=extra_themes)
    return r, filters.window_of(r, dt), dt


def run_ch(fn):
    """A CH failure becomes the right envelope kind (503 thin cluster / 502)."""
    try:
        return fn()
    except CHError as e:
        raise ch.as_api_error(e)


def meta(t0: float, notes=None, **extra) -> dict:
    m = {"seconds": round(time.time() - t0, 3), "coverage": ch.coverage_summary(),
         "notes": [n for n in (notes or []) if n]}
    m.update(extra)
    return m


def pct(n, d, digits: int = 2):
    return round(100.0 * n / d, digits) if d else None


# ── row -> payload pieces ────────────────────────────────────────────────────
def sentiment_of(tup) -> dict | None:
    if not tup or not isinstance(tup, (list, tuple)) or not tup[0]:
        return None
    label = str(tup[0])
    return {"label": label, "score": round(float(tup[1]), 3) if len(tup) > 1 else None,
            "group": taxonomy.group_of(label)}


def classes_of(arr) -> list:
    out = []
    for x in arr or []:
        path = x[0]
        out.append({"code": taxonomy.code_of(path), "path": path,
                    "score": round(float(x[1]), 3)})
    out.sort(key=lambda c: -(c["score"] or 0))
    return out


def themes_of(arr) -> list:
    return [{"name": x[0], "score": round(float(x[1]), 3)} for x in (arr or [])[:5]]


def signals_of(row: list) -> dict:
    """HEADLINE_COLS row -> the signal half of an item."""
    pri = row[2]
    return {"id": row[0], "published_at": row[1].replace(" ", "T"),
            "lede": row[9] or None,
            "sentiment": sentiment_of(row[3]),
            "priority": int(pri) if pri not in (None, 0) else None,
            "classes": classes_of(row[4]), "themes": themes_of(row[5]),
            "country": row[6] or None,
            "organizations": list(row[7] or []), "people": list(row[8] or [])}


def item_of(row: list, rec: dict, full: bool = False) -> dict:
    """Signals + the article-store record -> one headline (or full) item."""
    sig = signals_of(row)
    item = {"id": sig["id"],
            "headline": rec.get("headline") or (sig["lede"] or "")[:160] or None,
            "url": rec.get("url"), "publisher": rec.get("publisher"),
            "published_at": sig["published_at"], "lede": sig["lede"],
            "sentiment": sig["sentiment"], "priority": sig["priority"],
            "classes": sig["classes"],
            "country": sig["country"], "organizations": sig["organizations"],
            "people": sig["people"]}
    if full:
        item.update({k: rec.get(k) for k in ("body", "body_chars", "authors", "top_image",
                                              "meta_description", "publish_date", "language")})
    return item


def store_notes(errors: list) -> list:
    return ["Some requested articles are temporarily unavailable."] if errors else []


# ── corpus baselines (30 days ending data_through, cached 24 h in Redis) ─────
def _range(dt: str) -> tuple[str, str]:
    end = date.fromisoformat(dt)
    start = end - timedelta(days=config.BASELINE_DAYS - 1)
    return start.isoformat(), (end + timedelta(days=1)).isoformat()


def baseline(name: str, label_expr: str, carrier: str, dt: str) -> dict:
    """{counts: {label: n}, articles, carrying, since, until}. One scan over the
    baseline month; computing it inside every request was what made a themes
    panel take 132 s in the product."""
    key = f"baseline:{name}"
    hit = quota.cache_get(key)
    if hit and hit.get("data_through") == dt:
        return hit
    since, until_x = _range(dt)
    where = f"datetime >= {ch.sql_str(since)} AND datetime < {ch.sql_str(until_x)}"

    def q():
        counts = ch.rows(f"SELECT label, count() FROM (SELECT arrayJoin({label_expr}) AS label "
                         f"FROM {ch.TABLE} WHERE {where} AND {carrier}) GROUP BY label")
        tot = ch.one(f"SELECT count(), countIf({carrier}) FROM {ch.TABLE} WHERE {where}")
        return counts, tot
    counts, tot = run_ch(q)
    out = {"data_through": dt, "since": since,
           "until": (date.fromisoformat(until_x) - timedelta(days=1)).isoformat(),
           "days": config.BASELINE_DAYS, "articles": int(tot[0]), "carrying": int(tot[1]),
           "counts": {str(r[0]): int(r[1]) for r in counts}}
    quota.cache_put(key, out, config.BASELINE_TTL)
    return out


def baseline_block(b: dict) -> dict:
    return {"since": b["since"], "until": b["until"], "days": b["days"],
            "articles": b["articles"], "carrying": b["carrying"],
            "note": "Archive comparison over the 30 days ending at data_through"}


# ── time buckets ─────────────────────────────────────────────────────────────
def check_granularity(g: str | None) -> str:
    g = (g or config.DEFAULT_GRANULARITY).strip().lower()
    if g not in config.GRANULARITIES:
        raise ApiError("bad_request", f"`granularity` must be one of {', '.join(config.GRANULARITIES)}")
    return g


def _bucket_start(d: date, g: str) -> date:
    if g == "daily":
        return d
    if g == "weekly":
        return d - timedelta(days=d.weekday())
    return d.replace(day=1)


def _next_bucket(d: date, g: str) -> date:
    if g == "daily":
        return d + timedelta(days=1)
    if g == "weekly":
        return d + timedelta(days=7)
    y, m = d.year + (d.month // 12), d.month % 12 + 1
    return date(y, m, 1)


def periods(since: str, until: str, g: str) -> list[dict]:
    """Every bucket touching [since, until], with a partial flag when the
    window does not cover the whole bucket."""
    s, u = date.fromisoformat(since), date.fromisoformat(until)
    out, b = [], _bucket_start(s, g)
    while b <= u:
        nb = _next_bucket(b, g)
        out.append({"period": b.isoformat(),
                    "partial_period": b < s or (nb - timedelta(days=1)) > u})
        b = nb
    return out
