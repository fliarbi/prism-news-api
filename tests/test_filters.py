"""filters -> SQL: every parameter, combinations, injection-safe quoting,
plan bounds, cursor round-trip."""
from __future__ import annotations

import pytest

from prism_news_api import filters, taxonomy
from prism_news_api.envelope import ApiError
from prism_news_api.filters import Filters

DT = "2026-08-24"
FREE = {"max_results": 100, "history_days": 365}
PRO = {"max_results": 100, "history_days": None}


def res(cfg=FREE, **kw):
    return filters.resolve(Filters(**kw), cfg, DT)


# ── window defaults / clamps ─────────────────────────────────────────────────
def test_default_window_is_90_days_ending_at_data_through():
    r = res()
    assert r.until == DT and r.since == "2026-05-26" and r.until_exclusive == "2026-08-25"
    w = filters.where_sql(r)
    assert "datetime >= '2026-05-26'" in w and "datetime < '2026-08-25'" in w
    assert r.limit == 100 and r.sort == "newest" and r.notes == []


def test_until_past_data_through_is_clamped_with_note():
    r = res(until="2026-12-31")
    assert r.until == DT and any("data_through" in n for n in r.notes)


def test_since_clamped_to_plan_history_days():
    r = res(since="2020-01-01")
    assert r.since == "2025-08-24"
    assert any("history_days" in n for n in r.notes)


def test_pro_plan_reaches_the_whole_corpus():
    r = res(PRO, since="2020-01-01")
    assert r.since == "2020-01-01" and not r.notes


def test_window_entirely_before_history_floor_is_400_with_upgrade_url():
    with pytest.raises(ApiError) as e:
        res(since="2020-01-01", until="2020-02-01")
    assert e.value.kind == "bad_request" and "upgrade_url" in e.value.fields


def test_since_after_until_is_400():
    with pytest.raises(ApiError):
        res(since="2026-08-01", until="2026-07-01")


def test_bad_date_is_400():
    with pytest.raises(ApiError) as e:
        res(since="yesterday")
    assert e.value.kind == "bad_request"


# ── limit ────────────────────────────────────────────────────────────────────
def test_limit_over_cap_is_clamped_with_note():
    r = res(limit=5000)
    assert r.limit == 100 and any("clamped" in n for n in r.notes)


def test_limit_cap_from_plan():
    r = filters.resolve(Filters(limit=400), {"max_results": 500}, DT)
    assert r.limit == 400


def test_limit_below_one_rejected_by_model():
    with pytest.raises(Exception):
        Filters(limit=0)


# ── q ────────────────────────────────────────────────────────────────────────
def test_q_builds_lede_tags_and_entity_lanes():
    r = res(q="Electric  Vehicle")
    assert r.q == "electric vehicle"
    w = filters.where_sql(r)
    assert "match(lower(assumeNotNull(text)), '(^|[^a-z0-9])electric vehicle([^a-z0-9]|$)')" in w
    assert "has(tags, 'electric vehicle')" in w
    assert "arrayExists(x -> position(x, 'electric vehicle') > 0, Organization)" in w
    assert "arrayExists(x -> position(x, 'electric vehicle') > 0, Person)" in w


def test_q_regex_metachars_are_escaped_and_quotes_are_safe():
    r = res(q="o'reilly (auto).parts+*")
    w = filters.where_sql(r)
    assert "o\\'reilly" in w                              # SQL-escaped quote
    assert "\\\\(auto\\\\)\\\\.parts\\\\+\\\\*" in w       # regex escapes, doubled for the SQL literal
    assert "; DROP" not in w


def test_q_injection_attempt_stays_inside_the_literal():
    r = res(q="x') OR 1=1 --")
    w = filters.where_sql(r)
    assert "has(tags, 'x\\') or 1=1 --')" in w
    assert w.count("'") % 2 == 0


def test_q_length_bounds():
    with pytest.raises(ApiError):
        res(q="a")
    with pytest.raises(ApiError):
        res(q="x" * 121)
    assert res(q="ab").q == "ab"


# ── sentiment ────────────────────────────────────────────────────────────────
def test_sentiment_groups_expand_to_labels_in_order():
    r = res(sentiment="negative")
    assert r.sentiment == ["extreme_neg", "very_neg", "fair_neg", "slight_neg"]
    assert "arraySort(x -> -x.2, sentiments)[1].1 IN ('extreme_neg','very_neg','fair_neg','slight_neg')" in filters.where_sql(r)


def test_sentiment_mixed_labels_and_groups_dedupe():
    r = res(sentiment="very_pos, positive,neutral")
    assert r.sentiment == ["none", "slight_pos", "fair_pos", "very_pos", "extreme_pos"]


def test_unknown_sentiment_is_400():
    with pytest.raises(ApiError) as e:
        res(sentiment="angry")
    assert "unknown sentiment" in e.value.reason


# ── classes ──────────────────────────────────────────────────────────────────
def test_classes_by_code_use_threshold_and_paths():
    r = res(classes="0,55")
    assert r.classes == [0, 55]
    w = filters.where_sql(r)
    assert ("arrayExists(x -> x.1 IN ('/News/Business News/Company News',"
            "'/Business & Industrial/Business Finance/Venture Capital') AND x.2 > 0.39, classification)") in w


def test_unknown_class_code_is_400():
    with pytest.raises(ApiError) as e:
        res(classes="0,999999")
    assert e.value.kind == "bad_request" and "999999" in e.value.reason


def test_non_integer_class_is_400():
    with pytest.raises(ApiError):
        res(classes="abc")


def test_class_prefix_expands_and_unions_with_codes():
    r = res(class_prefix="/Finance", classes="0")
    fin = taxonomy.expand_prefix("/Finance")
    assert len(fin) > 5 and r.classes[0] == 0 and set(fin) <= set(r.classes)
    assert r.class_prefix == "/Finance"


def test_class_prefix_case_insensitive_and_trailing_slash():
    assert res(class_prefix="/finance/").classes == res(class_prefix="/Finance").classes


def test_unknown_prefix_is_400():
    with pytest.raises(ApiError):
        res(class_prefix="/Nonexistent Thing")


# ── themes ───────────────────────────────────────────────────────────────────
def test_themes_csv_lowercased_exact():
    r = res(themes="Professional League Updates, athlete transfer rumors")
    assert r.themes == ["professional league updates", "athlete transfer rumors"]
    assert "arrayExists(x -> x.1 IN ('professional league updates','athlete transfer rumors'), subcats)" in filters.where_sql(r)


def test_themes_pipe_separator_keeps_commas():
    r = res(themes="economic indicators (gdp, cpi, unemployment)|athlete transfer rumors")
    assert r.themes == ["economic indicators (gdp, cpi, unemployment)", "athlete transfer rumors"]


def test_themes_json_list_accepted():
    f = Filters(themes=["A", "B"])
    assert filters.resolve(f, FREE, DT).themes == ["a", "b"]


# ── priority ─────────────────────────────────────────────────────────────────
def test_priority_bounds_add_carrier_guard():
    w = filters.where_sql(res(priority_min=7))
    assert "length(priorities) > 0" in w and "arraySort(x -> -x.2, priorities)[1].1 >= 7" in w
    w = filters.where_sql(res(priority_max=3))
    assert "arraySort(x -> -x.2, priorities)[1].1 <= 3" in w


def test_priority_min_over_max_is_400():
    with pytest.raises(ApiError):
        res(priority_min=8, priority_max=2)


def test_priority_out_of_range_rejected_by_model():
    with pytest.raises(Exception):
        Filters(priority_min=10)


# ── country ──────────────────────────────────────────────────────────────────
def test_country_lowercased_with_enrichment_note():
    r = res(country="United States")
    assert "lower(assumeNotNull(country_pri)) = 'united states'" in filters.where_sql(r)
    assert any("Location coverage" in n for n in r.notes)


# ── sort / order / combos ────────────────────────────────────────────────────
def test_sort_orders():
    assert filters.order_sql(res()) == "datetime DESC, target_id DESC"
    assert filters.order_sql(res(sort="oldest")) == "datetime ASC, target_id ASC"
    assert filters.order_sql(res(sort="priority")).startswith("arraySort(x -> -x.2, priorities)[1].1 DESC")


def test_unknown_sort_is_400():
    with pytest.raises(ApiError):
        res(sort="relevance")


def test_full_combination_where():
    r = res(q="tesla", sentiment="negative", classes="0", themes="layoffs", priority_min=7,
            priority_max=9, country="india", since="2026-06-01", until="2026-06-30")
    w = filters.where_sql(r)
    for frag in ("datetime >= '2026-06-01'", "datetime < '2026-07-01'", "has(tags, 'tesla')",
                 "IN ('extreme_neg'", "classification)", "subcats)", ">= 7", "<= 9",
                 "lower(assumeNotNull(country_pri)) = 'india'"):
        assert frag in w
    assert w.count(" AND ") == 10            # 10 predicates joined + the `AND x.2 > 0.39` inside the class lambda
    subj = r.subject()
    assert subj["q"] == "tesla" and subj["classes"] == [0] and subj["since"] == "2026-06-01"


def test_no_filters_where_is_just_dates():
    assert filters.where_sql(res()).count(" AND ") == 1
    assert filters.where_sql(res(), with_dates=False) == "1"


# ── cursors ──────────────────────────────────────────────────────────────────
def test_cursor_round_trip_newest():
    r = res()
    cur = filters.cursor_for(r, "2026-08-24 10:11:12", "69f881d343843dd771cf50f2")
    d = filters.decode_cursor(cur)
    assert d == {"v": 1, "s": "newest", "d": "2026-08-24 10:11:12", "i": "69f881d343843dd771cf50f2"}
    r2 = res(cursor=cur)
    assert "(datetime, target_id) < (toDateTime('2026-08-24 10:11:12'), '69f881d343843dd771cf50f2')" in filters.where_sql(r2)


def test_cursor_round_trip_oldest_and_priority():
    r = res(sort="oldest")
    cur = filters.cursor_for(r, "2026-06-01 00:00:00", "69f881d343843dd771cf50f2")
    assert "(datetime, target_id) > (" in filters.where_sql(res(sort="oldest", cursor=cur))
    r = res(sort="priority")
    cur = filters.cursor_for(r, "2026-06-01 00:00:00", "69f881d343843dd771cf50f2", 7)
    assert filters.decode_cursor(cur)["p"] == 7
    w = filters.where_sql(res(sort="priority", cursor=cur))
    assert "(arraySort(x -> -x.2, priorities)[1].1, datetime, target_id) < (7, toDateTime(" in w


def test_cursor_sort_mismatch_is_400():
    cur = filters.cursor_for(res(), "2026-08-24 10:11:12", "69f881d343843dd771cf50f2")
    with pytest.raises(ApiError) as e:
        res(sort="oldest", cursor=cur)
    assert "issued for sort" in e.value.reason


@pytest.mark.parametrize("bad", ["garbage", "eyJ2IjoxfQ", "e30", "////",
                                 filters.encode_cursor("newest", "not a date", "69f881d343843dd771cf50f2")])
def test_bad_cursors_are_400(bad):
    with pytest.raises(ApiError) as e:
        res(cursor=bad)
    assert e.value.kind == "bad_request"


def test_cursor_is_urlsafe():
    cur = filters.cursor_for(res(), "2026-08-24 10:11:12", "69f881d343843dd771cf50f2")
    assert "=" not in cur and "+" not in cur and "/" not in cur


def test_re2_escape_leaves_spaces_alone():
    assert filters.re2_escape("a b-c/d") == "a b-c/d"
    assert filters.re2_escape("a.b*c") == "a\\.b\\*c"


# ── match modes ──────────────────────────────────────────────────────────────
def test_match_default_is_any_and_sql_unchanged():
    r = res(q="electric vehicle")
    assert r.match == "any"
    w = filters.where_sql(r)
    assert "(match(lower(assumeNotNull(text)), " in w
    assert "OR has(tags, 'electric vehicle') OR arrayExists" in w
    assert r.subject()["match"] == "any"


def test_match_lede_only_uses_the_regex_lane():
    w = filters.where_sql(res(q="electric vehicle", match="opening"))
    assert "match(lower(assumeNotNull(text))" in w
    assert "has(tags" not in w and "Organization" not in w


def test_internal_match_mode_is_not_supported():
    with pytest.raises(ApiError) as e:
        res(q="electric vehicle", match="tags")
    assert "tags" not in e.value.reason
    assert "focused" in e.value.reason


def test_match_central_requires_tag_and_lede_or_entity_and_no_digest():
    w = filters.where_sql(res(q="electric vehicle", match="FOCUSED"))
    assert "has(tags, 'electric vehicle') AND (match(lower(assumeNotNull(text))" in w
    assert "OR arrayExists(x -> position(x, 'electric vehicle') > 0, Person)) AND length(tags) <= 45)" in w


def test_match_unknown_is_400():
    with pytest.raises(ApiError) as e:
        res(q="electric vehicle", match="fuzzy")
    assert e.value.kind == "bad_request" and "match" in e.value.reason


def test_match_without_q_is_ignored_in_sql():
    w = filters.where_sql(res(match="focused"))
    assert "has(tags" not in w and "match(lower" not in w
