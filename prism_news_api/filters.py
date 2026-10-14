"""filters — the common ✱ parameters: validation, plan bounds, SQL, cursors.

Every list and distribution endpoint accepts the same filter set (GET query
string or POST JSON body, same names). This module turns it into

  * a normalised `Resolved` (what actually ran — echoed in `subject.filters`),
  * a ClickHouse WHERE clause built only from quoted literals,
  * an opaque keyset cursor on (datetime, target_id) (+ priority for that sort).

Measured facts baked in:

  * `text` is a ~320-char LEDE, lowercased in the corpus, not the body. So `q`
    is a lede match OR a `tags` match (Prism's own subject labels, on 100% of
    articles) OR a substring match on the canonical Organization / Person
    arrays — substring because those hold canonical names ('tesla, inc.'),
    and an equality test there finds literally nothing.
  * The word boundary is spelled out as `(^|[^a-z0-9])…([^a-z0-9]|$)`:
    re2 has no lookaround, and `\\b` treats '_' as a word char.
  * Class filter: `arrayExists(x -> x.1 IN (...) AND x.2 > 0.39, classification)`
    — the pipeline's own threshold, applied per element, not to the array.
  * Top sentiment / priority: `arraySort(x -> -x.2, arr)[1].1`.
  * Theme names are exact lowercase `subcats` names; 75 of ~4,000 contain a
    comma, so `|` is accepted as the list separator when present.
  * Windows default to 90 days ending at `data_through`, never at "today";
    `since` is clamped to the plan's `history_days` and says so in `meta.notes`.
"""
from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from . import ch, config, taxonomy
from .envelope import ApiError

Q_MIN, Q_MAX = 2, 120
CURSOR_VERSION = 1


def split_list(v) -> list[str]:
    """csv (or `|`-separated when a value contains commas) or list -> clean list."""
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        items = [str(x) for x in v]
    else:
        s = str(v)
        items = s.split("|") if "|" in s else s.split(",")
    return [x.strip() for x in items if x and x.strip()]


class Filters(BaseModel):
    """Combine search, sentiment, content classes, themes, importance and dates."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    q: Optional[str] = Field(None, description="Search phrase, 2-120 characters; case-insensitive")
    match: Optional[str] = Field(None, description="Search breadth: any (broad), opening (article introduction), focused (strong subject relevance)")
    sentiment: Optional[str] = Field(None, description="csv of labels and/or groups (negative, neutral, positive); the article's top label")
    classes: Optional[str] = Field(None, description="csv of GCP class codes (any-of, score > 0.39)")
    class_prefix: Optional[str] = Field(None, description="e.g. /News/Business News — every code under it")
    themes: Optional[str] = Field(None, description="csv of exact theme names (use | as separator if a name has a comma)")
    priority_min: Optional[int] = Field(None, ge=1, le=9)
    priority_max: Optional[int] = Field(None, ge=1, le=9)
    country: Optional[str] = Field(None, description="Country name; location coverage may be incomplete")
    since: Optional[str] = Field(None, description="ISO date; default = 90 days before until")
    until: Optional[str] = Field(None, description="ISO date, inclusive; default = data_through")
    limit: Optional[int] = Field(None, ge=1, description="default 100; cap = plan max_results")
    sort: str = Field("newest", description="newest | oldest | priority")
    cursor: Optional[str] = Field(None, description="next_cursor from a previous page")

    @field_validator("sentiment", "classes", "themes", mode="before")
    @classmethod
    def _lists_to_csv(cls, v):
        if isinstance(v, (list, tuple)):
            return "|".join(str(x) for x in v)
        return v

    @field_validator("q", "country", "class_prefix", mode="before")
    @classmethod
    def _none_if_blank(cls, v):
        if isinstance(v, str) and not v.strip():
            return None
        return v

    def extra_where(self, r: "Resolved") -> list[str]:
        """Extension point for subclasses (the business API's `company` /
        `event_type` lanes): SQL fragments appended to where_sql() after the
        common filters. Called by resolve() once the window is known; raise
        ApiError("bad_request") to reject a value. Default: none."""
        return []


@dataclass
class Resolved:
    since: str                      # inclusive ISO date
    until: str                      # inclusive ISO date
    until_exclusive: str            # until + 1 day, for SQL
    limit: int
    sort: str
    q: Optional[str] = None
    q_regex: Optional[str] = None
    match: str = "any"
    sentiment: list = field(default_factory=list)
    classes: list = field(default_factory=list)      # ints
    class_prefix: Optional[str] = None
    themes: list = field(default_factory=list)
    priority_min: Optional[int] = None
    priority_max: Optional[int] = None
    country: Optional[str] = None
    cursor: Optional[dict] = None
    notes: list = field(default_factory=list)
    requested_limit: Optional[int] = None
    extra_sql: list = field(default_factory=list)   # from Filters.extra_where()

    def subject(self) -> dict:
        """The normalised filter set that was run — never the raw input."""
        out = {"since": self.since, "until": self.until, "limit": self.limit,
               "sort": self.sort}
        if self.q:
            out["q"] = self.q
            out["match"] = self.match
        if self.sentiment:
            out["sentiment"] = self.sentiment
        if self.classes:
            out["classes"] = self.classes
        if self.class_prefix:
            out["class_prefix"] = self.class_prefix
        if self.themes:
            out["themes"] = self.themes
        if self.priority_min is not None:
            out["priority_min"] = self.priority_min
        if self.priority_max is not None:
            out["priority_max"] = self.priority_max
        if self.country:
            out["country"] = self.country
        if self.cursor:
            out["cursor"] = True
        return out

    @property
    def days(self) -> int:
        return (date.fromisoformat(self.until) - date.fromisoformat(self.since)).days + 1

    def has_content_filter(self) -> bool:
        return bool(self.q or self.sentiment or self.classes or self.themes
                    or self.priority_min is not None or self.priority_max is not None
                    or self.country)


# ── regex escaping for re2 ───────────────────────────────────────────────────
_RE2_SPECIAL = set("\\.^$*+?()[]{}|")


def re2_escape(s: str) -> str:
    """Escape regex metacharacters for ClickHouse's re2. Python's re.escape also
    escapes spaces and other non-word characters, which re2 may reject."""
    return "".join("\\" + c if c in _RE2_SPECIAL else c for c in s)


def q_regex(q: str) -> str:
    return "(^|[^a-z0-9])" + re2_escape(q) + "([^a-z0-9]|$)"


# How `q` must match. Measured on this corpus for "electric vehicle" over
# Jan–Apr 2026: lede 16,329 / tagged 15,005 / both 1,644 — the two lanes mostly
# disagree, because the lede is only the first ~320 characters and the tagger
# reads the whole body. `any` is recall-first and is the default; `central`
# is the feed-quality mode Prism's own reports use (the term is one of the
# article's tags AND appears in the lede or its entities, and the article is
# not a round-up), which is what stops a tagger error such as a crash into an
# "electric power pole" surfacing for "electric vehicle".
MATCH_MODES = ("any", "opening", "focused")
DIGEST_TAGS = 45      # p90 of tags-per-article is 43; a round-up carries 48–89


# ── dates ────────────────────────────────────────────────────────────────────
def _parse_date(v: str, name: str) -> date:
    s = str(v).strip()
    try:
        return date.fromisoformat(s[:10]) if len(s) >= 10 else date.fromisoformat(s)
    except ValueError:
        raise ApiError("bad_request", f"`{name}` must be an ISO date (YYYY-MM-DD), got {v!r}")


def _bad(reason: str, **fields) -> ApiError:
    return ApiError("bad_request", reason, fields=fields or None)


# ── resolution ───────────────────────────────────────────────────────────────
def resolve(f: Filters, plan_cfg: dict, data_through: str, *,
            default_limit: int = config.DEFAULT_LIMIT, cap: int | None = None,
            extra_classes=(), extra_themes=()) -> Resolved:
    """Validate + normalise + bound by plan. Raises ApiError(bad_request)."""
    notes: list[str] = []
    cap = int(cap or plan_cfg.get("max_results") or config.DEFAULT_LIMIT)

    # limit
    requested = f.limit
    limit = int(requested if requested is not None else default_limit)
    if limit > cap:
        notes.append(f"limit {limit} exceeds the plan cap of {cap}; clamped to {cap}")
        limit = cap

    # sort
    sort = (f.sort or "newest").strip().lower()
    if sort not in taxonomy.SORTS:
        raise _bad(f"`sort` must be one of {', '.join(taxonomy.SORTS)}")

    # window
    dt = _parse_date(data_through, "data_through")
    until = _parse_date(f.until, "until") if f.until else dt
    if until > dt:
        notes.append(f"until {until} is past data_through {dt}; clamped")
        until = dt
    since = (_parse_date(f.since, "since") if f.since
             else until - timedelta(days=config.DEFAULT_WINDOW_DAYS))
    if since > until:
        raise _bad(f"`since` ({since}) is after `until` ({until})")
    history_days = plan_cfg.get("history_days")
    if history_days is not None:
        floor = dt - timedelta(days=int(history_days))
        if until < floor:
            raise _bad(f"the requested window ends before your plan's history floor "
                       f"({floor}, history_days={history_days}); upgrade for whole-corpus access",
                       upgrade_url=config.UPGRADE_URL)
        if since < floor:
            notes.append(f"since {since} is earlier than the plan's history_days "
                         f"({history_days}); clamped to {floor}")
            since = floor

    r = Resolved(since=since.isoformat(), until=until.isoformat(),
                 until_exclusive=(until + timedelta(days=1)).isoformat(),
                 limit=limit, sort=sort, notes=notes, requested_limit=requested)

    # q
    if f.q:
        q = " ".join(f.q.split()).lower()
        if len(q) < Q_MIN or len(q) > Q_MAX:
            raise _bad(f"`q` must be between {Q_MIN} and {Q_MAX} characters")
        r.q, r.q_regex = q, q_regex(q)
    mode = (f.match or "any").strip().lower()
    if mode not in MATCH_MODES:
        raise _bad(f"`match` must be one of {', '.join(MATCH_MODES)}")
    r.match = mode

    # sentiment
    if f.sentiment:
        try:
            r.sentiment = taxonomy.expand_sentiment(split_list(f.sentiment))
        except ValueError as e:
            raise _bad(str(e))

    # classes
    codes: list[int] = []
    if f.classes:
        try:
            codes.extend(taxonomy.validate_codes(split_list(f.classes)))
        except ValueError as e:
            raise _bad(str(e))
    if f.class_prefix:
        prefix = taxonomy.normalise_prefix(f.class_prefix)
        under = taxonomy.expand_prefix(prefix)
        if not under:
            raise _bad(f"no GCP class under prefix {prefix!r} — see /v1/classes")
        r.class_prefix = prefix
        codes.extend(under)
    for c in extra_classes:
        codes.extend(taxonomy.validate_codes([c]))
    r.classes = list(dict.fromkeys(codes))

    # themes
    themes = [t.lower() for t in split_list(f.themes)] + [str(t).strip().lower()
                                                           for t in extra_themes if t]
    r.themes = list(dict.fromkeys(t for t in themes if t))
    if len(r.themes) > 5:
        raise _bad("Use at most five themes in one query.")

    # priority
    if f.priority_min is not None and f.priority_max is not None \
            and f.priority_min > f.priority_max:
        raise _bad("`priority_min` is greater than `priority_max`")
    r.priority_min, r.priority_max = f.priority_min, f.priority_max

    # country
    if f.country:
        r.country = f.country.strip().lower()
        notes.append(config.COUNTRY_NOTE)

    # cursor
    if f.cursor:
        try:
            cur = decode_cursor(f.cursor)
        except ValueError as e:
            raise _bad(f"invalid cursor: {e}")
        if cur.get("s") != sort:
            raise _bad(f"cursor was issued for sort={cur.get('s')!r}, not {sort!r}")
        r.cursor = cur
    r.extra_sql = [x for x in (f.extra_where(r) or []) if x]
    return r


# ── SQL ──────────────────────────────────────────────────────────────────────
def where_sql(r: Resolved, *, with_dates: bool = True, with_cursor: bool = True,
              since: str | None = None, until_exclusive: str | None = None) -> str:
    parts: list[str] = []
    if with_dates:
        parts.append(f"datetime >= {ch.sql_str(since or r.since)}")
        parts.append(f"datetime < {ch.sql_str(until_exclusive or r.until_exclusive)}")
    if r.q:
        qs = ch.sql_str(r.q)
        lede = f"match(lower(assumeNotNull(text)), {ch.sql_str(r.q_regex)})"
        tags = f"has(tags, {qs})"
        ents = (f"arrayExists(x -> position(x, {qs}) > 0, Organization) "
                f"OR arrayExists(x -> position(x, {qs}) > 0, Person)")
        if r.match == "opening":
            parts.append(f"({lede})")
        elif r.match == "focused":
            parts.append(f"({tags} AND ({lede} OR {ents}) AND length(tags) <= {DIGEST_TAGS})")
        else:
            parts.append(f"({lede} OR {tags} OR {ents})")
    if r.sentiment:
        parts.append(f"{ch.TOP_SENTIMENT} IN {ch.sql_in(r.sentiment)}")
    if r.classes:
        paths = [taxonomy.path_of(c) for c in r.classes]
        parts.append(f"arrayExists(x -> x.1 IN {ch.sql_in(paths)} AND x.2 > "
                     f"{config.CLASS_THRESHOLD}, classification)")
    if r.themes:
        parts.append(f"arrayExists(x -> x.1 IN {ch.sql_in(r.themes)}, subcats)")
    if r.priority_min is not None or r.priority_max is not None:
        parts.append(ch.HAS_PRIORITY)
        if r.priority_min is not None:
            parts.append(f"{ch.TOP_PRIORITY} >= {ch.sql_int(r.priority_min)}")
        if r.priority_max is not None:
            parts.append(f"{ch.TOP_PRIORITY} <= {ch.sql_int(r.priority_max)}")
    if r.country:
        parts.append(f"lower(assumeNotNull(country_pri)) = {ch.sql_str(r.country)}")
    parts.extend(r.extra_sql)
    if with_cursor and r.cursor:
        parts.append(_keyset_sql(r))
    return " AND ".join(parts) if parts else "1"


def order_sql(r: Resolved) -> str:
    if r.sort == "oldest":
        return "datetime ASC, target_id ASC"
    if r.sort == "priority":
        return f"{ch.TOP_PRIORITY} DESC, datetime DESC, target_id DESC"
    return "datetime DESC, target_id DESC"


def _keyset_sql(r: Resolved) -> str:
    c = r.cursor or {}
    d, i = ch.sql_str(c["d"]), ch.sql_str(c["i"])
    if r.sort == "oldest":
        return f"(datetime, target_id) > (toDateTime({d}), {i})"
    if r.sort == "priority":
        return (f"({ch.TOP_PRIORITY}, datetime, target_id) < "
                f"({ch.sql_int(c.get('p') or 0)}, toDateTime({d}), {i})")
    return f"(datetime, target_id) < (toDateTime({d}), {i})"


# ── cursors ──────────────────────────────────────────────────────────────────
_DT_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
_ID_RE = re.compile(r"^[0-9a-fA-F]{24}$")


def encode_cursor(sort: str, datetime_str: str, target_id: str,
                  priority: int | None = None) -> str:
    payload = {"v": CURSOR_VERSION, "s": sort, "d": datetime_str, "i": target_id}
    if sort == "priority":
        payload["p"] = int(priority or 0)
    raw = json.dumps(payload, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def decode_cursor(s: str) -> dict:
    try:
        pad = "=" * (-len(s) % 4)
        obj = json.loads(base64.urlsafe_b64decode((s + pad).encode()).decode())
    except Exception:
        raise ValueError("not a cursor this API issued")
    if not isinstance(obj, dict) or obj.get("v") != CURSOR_VERSION:
        raise ValueError("unknown cursor version")
    if obj.get("s") not in taxonomy.SORTS:
        raise ValueError("unknown sort in cursor")
    if not isinstance(obj.get("d"), str) or not _DT_RE.match(obj["d"]):
        raise ValueError("bad datetime in cursor")
    if not isinstance(obj.get("i"), str) or not _ID_RE.match(obj["i"]):
        raise ValueError("bad id in cursor")
    if obj["s"] == "priority":
        if not isinstance(obj.get("p"), int) or not 0 <= obj["p"] <= 9:
            raise ValueError("bad priority in cursor")
    return obj


def cursor_for(r: Resolved, datetime_str: str, target_id: str,
               priority: int | None = None) -> str:
    return encode_cursor(r.sort, datetime_str, target_id, priority)


# ── window block ─────────────────────────────────────────────────────────────
def window_of(r: Resolved, data_through: str, **extra) -> dict:
    w = {"since": r.since, "until": r.until, "days": r.days,
         "data_through": data_through, "freshness": ch.freshness_note()}
    w.update(extra)
    return w
