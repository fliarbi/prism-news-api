"""Deterministic function and HTTP tests; all data and quotas stay in memory."""
from __future__ import annotations

import json
import re
import socket
import sqlite3
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import ValidationError

from prism_news_api import articles, auth, ch, config, filters, quota, taxonomy
from prism_news_api.envelope import ApiError
from prism_news_api.explore_routes import router
from prism_news_api.features import _common as c, explore
from prism_news_api.routers import install_handlers

DT = "2026-08-24"
KEY = "pna_" + "ab" * 20
HEADERS = {"X-API-Key": KEY}


def aid(n):
    return f"{n:024x}"


def doc(n, text, country, sentiment, priority, themes, date="2026-08-20 10:00:00"):
    return {"id": aid(n), "date": date, "text": text, "country": country,
            "sentiment": sentiment, "priority": priority, "themes": themes,
            "classes": [[taxonomy.path_of(0), 0.8]], "tags": ["energy"] if "energy" in text else [],
            "organizations": [], "people": []}


DOCS = [
    doc(1, "solar wind energy", "india", "very_neg", 7,
        [["a", .9], ["a", .85], ["b", .8], ["c", .7], ["d", .6], ["e", .5], ["f", .4]]),
    doc(2, "solar energy", "india", "slight_pos", 8, [["a", .8], ["user-topic", .7]]),
    doc(3, "solar energy", "japan", "none", 2, [["a", .8]]),
    doc(4, "wind energy", "united states", "slight_pos", 4, [["b", .8]]),
    doc(5, "solar energy", "japan", "very_neg", 9, [["user-topic", .8]]),
    doc(6, "solar energy", None, None, None, [["a", .8]]),
    doc(7, "energy update", "germany", "none", 1, []),
    doc(8, "energy update", "france", "slight_pos", 5, [["c", .8]]),
    doc(9, "energy update", "united kingdom", "very_neg", 7, [["c", .8]]),
    doc(10, "solar energy", "india", "very_neg", 7, [["a", .8]], "2020-01-01 10:00:00"),
    doc(11, "energy update", "canada", "slight_pos", 8, []),
    doc(12, "unrelated seed", "", "unrecognized", None, [[" ", .5]]),
    doc(13, "solar energy", "india", "very_neg", 7, [["f", .8]]),
]


class FixtureData:
    """Execute emitted predicates/aggregates against a small SQLite corpus.

    Translate only the fixed query expressions used by the features. Counts
    come from actual fixture rows, never from hand-picked SQL-shaped answers.
    This is an offline semantic test, not a production dialect integration test.
    """

    def __init__(self):
        self.db = sqlite3.connect(":memory:", check_same_thread=False)
        self.sql = []
        self.docs = {d["id"]: d for d in DOCS}
        self.details = {d["id"]: {"headline": d["text"], "url": f"https://news.example/{d['id']}",
                                  "publisher": "news.example"} for d in DOCS}
        self.errors = []
        self.detail_calls = []
        self.db.execute("CREATE TABLE corpus(target_id TEXT, datetime TEXT, text TEXT, country_pri TEXT, "
                        "sentiment TEXT, priority INTEGER, subcats TEXT, tags TEXT, Organization TEXT, "
                        "Person TEXT, classification TEXT, seed_themes TEXT)")
        for d in DOCS:
            seed = list(dict.fromkeys(t[0].strip().lower() for t in sorted(d["themes"], key=lambda t: -t[1])
                                      if t[0].strip()))[:5]
            self.db.execute("INSERT INTO corpus VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
                d["id"], d["date"], d["text"], d["country"], d["sentiment"], d["priority"],
                json.dumps(d["themes"]), json.dumps(d["tags"]), json.dumps(d["organizations"]),
                json.dumps(d["people"]), json.dumps(d["classes"]), json.dumps(seed)))
        self.db.create_function("match", 2, lambda text, pattern: bool(re.search(pattern, text or "")))
        self.db.create_function("has", 2, lambda arr, value: value in json.loads(arr))
        self.db.create_function("entity_contains", 2, lambda arr, value: any(value in x for x in json.loads(arr)))
        self.db.create_function("theme_overlap", 2, lambda arr, want: any(x[0].strip().lower() in json.loads(want)
                                                                 for x in json.loads(arr)))
        self.db.create_function("theme_available", 1, lambda arr: any(x[0].strip() for x in json.loads(arr)))
        self.db.create_function("class_overlap", 3, lambda arr, want, threshold:
                                any(x[0] in json.loads(want) and x[1] > threshold for x in json.loads(arr)))
        self.db.create_function("notEmpty", 1, lambda value: bool(value))
        class CountIf:
            def __init__(self):
                self.n = 0
            def step(self, value):
                self.n += bool(value)
            def finalize(self):
                return self.n
        self.db.create_aggregate("countIf", 1, CountIf)

    def rows(self, sql, timeout=None):
        self.sql.append(sql)
        headline = c.HEADLINE_COLS in sql
        seed = sql.startswith("SELECT arraySlice(arrayDistinct(")
        if headline:
            sql = sql.replace(c.HEADLINE_COLS, "target_id")
        if seed:
            sql = "SELECT seed_themes FROM " + sql.split(" FROM ", 1)[1]
        sql = sql.replace(ch.TABLE, "corpus").replace(ch.TOP_SENTIMENT, "sentiment")
        sql = sql.replace(ch.TOP_PRIORITY, "coalesce(priority, 0)")
        sql = sql.replace(ch.HAS_SENTIMENT, "(sentiment IS NOT NULL)")
        sql = sql.replace(ch.HAS_PRIORITY, "(priority IS NOT NULL)")
        sql = sql.replace(explore._THEME, "theme_available(subcats)")
        sql = re.sub(r"arrayExists\(x -> x\.1 IN \((.*?)\) AND x\.2 > ([\d.]+), classification\)",
                     r"class_overlap(classification, json_array(\1), \2)", sql)
        sql = re.sub(r"arrayExists\(x -> (?:lowerUTF8\(trimBoth\(x\.1\)\)|x\.1) IN \((.*?)\), subcats\)",
                     r"theme_overlap(subcats, json_array(\1))", sql)
        sql = re.sub(r"arrayExists\(x -> position\(x, (.*?)\) > 0, (Organization|Person)\)",
                     r"entity_contains(\2, \1)", sql)
        sql = re.sub(r"assumeNotNull\((\w+)\)", r"coalesce(\1, '')", sql)
        sql = sql.replace("lowerUTF8(", "lower(").replace("trimBoth(", "trim(")
        sql = sql.replace("toDateTime(", "(")
        # Convert escaped literals to SQLite quoting (values remain literals).
        def literal(m):
            value = re.sub(r"\\(.)", r"\1", m.group()[1:-1])
            return "'" + value.replace("'", "''") + "'"
        sql = re.sub(r"'(?:\\.|[^'\\])*'", literal, sql)
        result = [list(row) for row in self.db.execute(sql).fetchall()]
        if headline:
            return [self.headline(row[0]) for row in result]
        if seed:
            return [[json.loads(row[0])] for row in result]
        if sql.startswith("SELECT count()"):
            result = [[0 if value is None else value for value in row] for row in result]
        return result

    def headline(self, article_id):
        d = self.docs[article_id]
        return [d["id"], d["date"], d["priority"], [d["sentiment"], .8] if d["sentiment"] else [],
                d["classes"], d["themes"][:8], d["country"], d["organizations"], d["people"], d["text"]]

    def one(self, sql, timeout=None):
        rows = self.rows(sql, timeout)
        return rows[0] if rows else None

    def details_for(self, ids, full=False):
        self.detail_calls.append((ids, full))
        return {i: self.details[i] for i in ids if i in self.details}, self.errors


@pytest.fixture
def corpus(monkeypatch):
    # A regression must fail instead of silently making a live connection.
    def no_network(*args, **kwargs):
        raise AssertionError("Offline test attempted a network connection")
    monkeypatch.setattr(socket, "create_connection", no_network)
    monkeypatch.setattr(socket.socket, "connect", no_network)
    data = FixtureData()
    monkeypatch.setattr(ch, "rows", data.rows)
    monkeypatch.setattr(ch, "one", data.one)
    monkeypatch.setattr(ch, "parallel", lambda fns, **kw: [fn() for fn in fns])
    monkeypatch.setattr(ch, "coverage", lambda **kw: {"rows": config.EXPECTED_ROWS, "partial": False})
    data.bound = Mock(return_value=DT)
    monkeypatch.setattr(ch, "data_through", data.bound)
    monkeypatch.setattr(articles, "resolve", data.details_for)
    yield data
    data.db.close()


@pytest.fixture
def client(monkeypatch, fake_redis, principal, corpus):
    def authenticate(headers):
        key = headers.get("x-api-key") or (headers.get("authorization") or "")[7:]
        if not key:
            raise ApiError("unauthenticated", "missing")
        if key != KEY:
            raise ApiError("invalid_key", "invalid")
        return principal
    monkeypatch.setattr(auth, "authenticate", authenticate)
    monkeypatch.setattr(quota, "record_daily", lambda *a, **kw: None)
    app = FastAPI()
    install_handlers(app)
    app.include_router(router)
    with TestClient(app, raise_server_exceptions=False) as http:
        yield http


def comparison(*queries):
    return explore.CompareRequest(queries=[{"name": name, "filters": f} for name, f in queries])


def test_overview_measured_tone_and_critical(corpus, principal):
    result = explore.overview(principal, filters.Filters(q="solar", match="opening"))
    data = result["data"]
    assert data["matched"] == 6
    assert data["tone"]["carrying"] == 5
    assert data["tone"]["groups"] == [
        {"group": "negative", "count": 3, "share_pct": 60.0},
        {"group": "neutral", "count": 1, "share_pct": 20.0},
        {"group": "positive", "count": 1, "share_pct": 20.0}]
    assert data["critical"] == {"min_priority": 7, "carrying": 5, "count": 4, "share_pct": 80.0}
    assert result["window"]["data_through"] == DT
    assert "2020-01-01" not in result["window"].values()


def test_coverage_actual_missing_signals_and_zero(corpus, principal):
    data = explore.coverage(principal, filters.Filters(q="solar"))["data"]
    assert data["matched"] == 6
    assert data["availability"] == {"sentiment": {"count": 5, "percentage": 83.33},
                                    "theme": {"count": 6, "percentage": 100.0},
                                    "location": {"count": 5, "percentage": 83.33}}
    unknown = explore.coverage(principal, filters.Filters(q="unrelated"))["data"]
    assert all(item["count"] == 0 for item in unknown["availability"].values())
    empty = explore.coverage(principal, filters.Filters(q="no matches"))["data"]
    assert empty["matched"] == 0
    assert all(item == {"count": 0, "percentage": None} for item in empty["availability"].values())
    assert explore.overview(principal, filters.Filters(q="no matches"))["data"]["critical"]["share_pct"] is None


def test_compare_exact_union_shared_bound_overlap_and_empty(corpus, principal):
    corpus.bound.side_effect = [DT, "2026-09-01"]
    result = explore.compare(principal, comparison(("Solar", {"q": "solar"}), ("Wind", {"q": "wind"})))
    assert corpus.bound.call_count == 1
    assert result["data"]["matched"] == 7
    assert [(x["name"], x["count"], x["share_pct"]) for x in result["data"]["items"]] == [
        ("Solar", 6, 85.71), ("Wind", 2, 28.57)]
    assert all(x["window"]["data_through"] == DT for x in result["data"]["items"])
    assert len(corpus.sql) == 1
    corpus.bound.side_effect = None
    result = explore.compare(principal, comparison(("A", {"q": "absent"}), ("B", {"q": "missing"})))
    assert result["data"]["matched"] == 0
    assert all(i["count"] == 0 and i["share_pct"] is None for i in result["data"]["items"])


def test_compare_resolves_every_history_window_before_scan(corpus, principal):
    principal.plan_cfg["history_days"] = 30
    principal.plan_cfg["max_results"] = 3
    good = comparison(("A", {"since": "2020-01-01", "limit": 900}), ("B", {"until": "2030-01-01"}))
    result = explore.compare(principal, good)
    for item in result["data"]["items"]:
        assert item["window"]["since"] == "2026-07-25"
        assert item["window"]["until"] == DT
        assert item["filters"]["limit"] == 3
    assert any("clamped" in note for note in result["meta"]["notes"])
    corpus.sql.clear()
    bad = comparison(("A", {"q": "solar"}), ("B", {"until": "2020-01-01"}))
    with pytest.raises(ApiError) as error:
        explore.compare(principal, bad)
    assert error.value.kind == "bad_request" and not corpus.sql


@pytest.mark.parametrize("names", [["A"], [str(i) for i in range(6)], ["A", " a "], ["A B", "a  b"]])
def test_comparison_set_constraints(names):
    with pytest.raises(ValidationError):
        comparison(*[(name, {}) for name in names])


def test_geography_top_five_with_measured_denominator(corpus, principal):
    data = explore.geography(principal, filters.Filters(q="energy", limit=999))["data"]
    assert data["matched"] == 11 and data["carrying"] == 10
    assert data["availability_pct"] == 90.91
    assert [i["country"] for i in data["items"]] == ["india", "japan", "canada", "france", "germany"]
    assert data["items"][0] == {"country": "india", "count": 3, "share_pct": 27.27}
    assert data["returned"] == 5 and data["other_located_count"] == 2
    assert all("solar" not in s for s in corpus.sql)
    principal.plan_cfg["max_results"] = 2
    assert explore.geography(principal, filters.Filters(q="energy"))["data"]["returned"] == 2


@pytest.mark.parametrize("q", [None, "", "   "])
def test_discovery_requires_q_before_data_reads(corpus, principal, q):
    for call in (lambda: explore.geography(principal, filters.Filters(q=q)),
                 lambda: explore.related(principal, aid(1), filters.Filters(q=q))):
        with pytest.raises(ApiError) as error:
            call()
        assert error.value.kind == "bad_request"
    assert not corpus.sql and not corpus.bound.called


def test_related_intersects_user_themes_and_seed_themes(corpus, principal):
    f = filters.Filters(q="solar", themes="user-topic", classes="0", country="india", priority_min=7,
                        sentiment="positive")
    result = explore.related(principal, aid(1), f)
    data = result["data"]
    assert data["total_estimate"] == 1
    assert [i["id"] for i in data["items"]] == [aid(2)]
    assert data["limit"] == 100 and corpus.detail_calls[-1][1] is False
    assert "seed_themes" not in data and all("themes" not in i for i in data["items"])
    assert result["subject"]["filters"]["themes"] == ["user-topic"]
    candidate_sql = next(s for s in corpus.sql if c.HEADLINE_COLS in s)
    assert "x.1 IN ('user-topic')" in candidate_sql
    assert "IN ('a','b','c','d','e')" in candidate_sql and "'f'" not in candidate_sql
    assert f"target_id != '{aid(1)}'" in candidate_sql
    assert "LIMIT 101" in candidate_sql


def test_related_pagination_limit_dedupe_and_unresolved(corpus, principal):
    first = explore.related(principal, aid(1), filters.Filters(q="solar", limit=2))["data"]
    assert first["total_estimate"] == 3
    assert [x["id"] for x in first["items"]] == [aid(6), aid(3)]
    second = explore.related(principal, aid(1), filters.Filters(q="solar", limit=2,
                                                               cursor=first["next_cursor"]))["data"]
    assert [x["id"] for x in second["items"]] == [aid(2)]
    assert second["total_estimate"] == 3 and second["next_cursor"] is None
    corpus.details.pop(aid(6))
    corpus.details[aid(2)]["url"] = corpus.details[aid(3)]["url"]
    corpus.errors = [{"node": "192.168.1.1", "error": "Mongo secret diagnostic"}]
    result = explore.related(principal, aid(1), filters.Filters(q="solar"))
    assert result["data"]["unresolved"] == 1 and result["data"]["duplicates_dropped"] == 1
    assert result["data"]["returned"] == 1 and result["data"]["total_estimate"] == 3
    assert "Mongo" not in json.dumps(result) and "192.168" not in json.dumps(result)
    principal.plan_cfg["max_results"] = 1
    assert explore.related(principal, aid(1), filters.Filters(q="solar", limit=900))["data"]["limit"] == 1


@pytest.mark.parametrize("seed", [aid(10), aid(12), aid(999)])
def test_related_seed_must_be_in_window_and_have_themes(corpus, principal, seed):
    with pytest.raises(ApiError) as error:
        explore.related(principal, seed, filters.Filters(q="solar"))
    assert error.value.kind == "no_data"
    assert len(corpus.sql) == 1 and not corpus.detail_calls


def test_related_empty_intersection_is_exact_zero(corpus, principal):
    data = explore.related(principal, aid(1), filters.Filters(q="absent"))["data"]
    assert data["total_estimate"] == 0 and data["items"] == []
    assert not corpus.detail_calls


def test_injection_is_literal_and_extra_sql_not_an_input(corpus, principal):
    value = "solar') OR 1=1 --"
    with pytest.raises(ValidationError):
        explore.ExplorationFilters(q=value, extra_sql=["1=1"], sql="SELECT secret", extra_where="1=1")
    f = explore.ExplorationFilters(q=value)
    assert explore.overview(principal, f)["data"]["matched"] == 0
    assert "extra_sql" not in f.model_dump()
    assert ch.sql_str(value.lower()) in corpus.sql[-1]
    with pytest.raises(ApiError) as error:
        explore.related(principal, value, filters.Filters(q="solar"))
    assert error.value.kind == "bad_request"


ENDPOINTS = [("GET", "/v1/overview", {"q": "solar"}), ("POST", "/v1/overview", {"q": "solar"}),
             ("GET", "/v1/coverage", {"q": "solar"}), ("POST", "/v1/coverage", {"q": "solar"}),
             ("GET", "/v1/geography", {"q": "energy"}), ("POST", "/v1/geography", {"q": "energy"}),
             ("POST", "/v1/compare", {"queries": [{"name": "A", "filters": {"q": "solar"}},
                                                  {"name": "B", "filters": {"q": "wind"}}]}),
             ("GET", f"/v1/articles/{aid(1)}/related", {"q": "solar"})]


def request(client, method, path, data, headers=HEADERS):
    return client.request(method, path, headers=headers, **({"params": data} if method == "GET" else {"json": data}))


@pytest.mark.parametrize("method,path,data", ENDPOINTS)
def test_api_metering_auth_and_headers(client, corpus, fake_redis, method, path, data):
    assert request(client, method, path, data, {}).status_code == 401
    assert request(client, method, path, data, {"X-API-Key": "bad"}).status_code == 401
    assert not corpus.sql
    response = request(client, method, path, data)
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["ok"] and body["window"]["data_through"] == DT
    assert body["meta"]["quota"]["requests"]["used"] == 1
    assert response.headers["X-Quota-Requests-Remaining"] == "999"
    assert response.headers["X-Quota-Exports-Remaining"] == "100"
    assert response.headers["X-Plan"] == "free"
    assert not fake_redis.keys("pna:exp:*")


@pytest.mark.parametrize("method,path,data", ENDPOINTS)
def test_api_rate_and_request_quota_block_before_data(client, principal, corpus, method, path, data):
    principal.plan_cfg["requests_per_month"] = 1
    assert request(client, method, path, data).status_code == 200
    corpus.sql.clear()
    blocked = request(client, method, path, data)
    assert blocked.status_code == 402 and not corpus.sql
    principal.plan_cfg["rate_per_minute"] = 2
    blocked = request(client, method, path, data)
    assert blocked.status_code == 429 and "Retry-After" in blocked.headers and not corpus.sql


@pytest.mark.parametrize("method,path,data", ENDPOINTS)
def test_api_coverage_gate_no_partial_answers(client, corpus, monkeypatch, method, path, data):
    monkeypatch.setattr(ch, "require_coverage", Mock(side_effect=ApiError(
        "coverage_unavailable", "ClickHouse Redis Mongo at 192.168.1.1 subcats tags")))
    response = request(client, method, path, data)
    assert response.status_code == 503 and response.json()["data"] is None
    assert not corpus.sql
    assert not re.search(r"ClickHouse|Redis|Mongo|192\.168|subcats|\btags\b", response.text)


@pytest.mark.parametrize("path", ["/v1/geography", f"/v1/articles/{aid(1)}/related"])
@pytest.mark.parametrize("params", [{}, {"q": " "}, {"q": "a"}, {"q": "solar", "match": "tags"}])
def test_api_discovery_validation_without_diagnostics(client, corpus, path, params):
    response = client.get(path, params=params, headers=HEADERS)
    assert response.status_code == 400 and not corpus.sql
    assert "input" not in response.text and "tags" not in response.text


def test_api_compare_shape_and_validation(client, corpus):
    for body in ({"queries": []}, {"sets": [{"name": "A", "filters": {}}]},
                 {"queries": [{"name": "A", "filters": {}}, {"name": "a", "filters": {}}]}):
        assert client.post("/v1/compare", json=body, headers=HEADERS).status_code == 400
    assert not corpus.sql


@pytest.mark.parametrize("method", ["GET", "POST"])
@pytest.mark.parametrize("data", [{"q": "energy", "limit": 6}, {"q": " "}, {}])
def test_api_geography_requires_phrase_and_bounded_limit(client, corpus, method, data):
    assert request(client, method, "/v1/geography", data).status_code == 400
    assert not corpus.sql


@pytest.mark.parametrize("sort,first_ids,last_id", [("oldest", [2, 3], 6), ("priority", [2, 3], 6)])
def test_related_other_sorts_keep_count_and_cursor(corpus, principal, sort, first_ids, last_id):
    first = explore.related(principal, aid(1), filters.Filters(q="solar", sort=sort, limit=2))["data"]
    assert [i["id"] for i in first["items"]] == [aid(i) for i in first_ids]
    following = explore.related(principal, aid(1), filters.Filters(q="solar", sort=sort, limit=2,
                                                                   cursor=first["next_cursor"]))["data"]
    assert [i["id"] for i in following["items"]] == [aid(last_id)]
    assert following["total_estimate"] == first["total_estimate"] == 3


@pytest.mark.parametrize("method,path,data", ENDPOINTS)
def test_api_history_is_enforced_on_every_path(client, corpus, principal, method, path, data):
    principal.plan_cfg["history_days"] = 30
    data = json.loads(json.dumps(data))
    if "queries" in data:
        data["queries"][-1]["filters"].update(since="2020-01-01", until="2020-01-31")
    else:
        data.update(since="2020-01-01", until="2020-01-31")
    response = request(client, method, path, data)
    assert response.status_code == 400 and not corpus.sql


def test_whole_history_plan_uses_requested_seed_window(corpus, principal):
    principal.plan_cfg["history_days"] = None
    result = explore.related(principal, aid(10), filters.Filters(q="solar", since="2020-01-01"))
    assert result["window"]["since"] == "2020-01-01"
    assert result["data"]["total_estimate"] == 4
    assert aid(10) not in {i["id"] for i in result["data"]["items"]}


def test_get_post_equivalence_and_public_match_modes(client):
    for path in ("overview", "coverage", "geography"):
        params = {"q": "energy", "match": "focused", "country": "india", "sentiment": "negative"}
        get = client.get(f"/v1/{path}", params=params, headers=HEADERS).json()
        post = client.post(f"/v1/{path}", json=params, headers=HEADERS).json()
        assert get["ok"] and post["ok"]
        assert get["data"] == post["data"] and get["subject"] == post["subject"]


@pytest.mark.parametrize("failure,status", [(ch.CHError("ClickHouse rejected SELECT tags FROM private at 192.168.1.1"), 502),
                                           (ch.CHError("CH unreachable Redis Mongo 192.168.1.1"), 503),
                                           (RuntimeError("secret password /home/private"), 500)])
def test_api_raw_errors_are_private(client, monkeypatch, failure, status):
    monkeypatch.setattr(ch, "one", Mock(side_effect=failure))
    response = client.get("/v1/overview", headers=HEADERS)
    assert response.status_code == status
    assert response.json()["data"] is None
    assert not re.search(r"ClickHouse|Redis|Mongo|192\.168|secret|password|/home/|SELECT|tags", response.text)


@pytest.mark.parametrize("bad_row", [None, [], [None] * 7, [-1] * 7])
def test_missing_counts_never_become_zero(corpus, principal, monkeypatch, bad_row):
    monkeypatch.setattr(ch, "one", lambda *a, **kw: bad_row)
    with pytest.raises(ApiError) as error:
        explore.overview(principal, filters.Filters(q="solar"))
    assert error.value.kind == "upstream"


def test_openapi_paths_models_and_no_internal_descriptions(client):
    schema = client.get("/openapi.json").json()
    assert set(schema["paths"]) == {path for _, path, _ in ENDPOINTS if "related" not in path} | {
        "/v1/articles/{article_id}/related"}
    schemas = schema["components"]["schemas"]
    assert {"CompareRequest", "ComparisonSet", "ExplorationFilters", "GeographyFilters"} <= set(schemas)
    query = schemas["CompareRequest"]["properties"]["queries"]
    assert query["minItems"] == 2 and query["maxItems"] == 5
    text = json.dumps(schema)
    assert not re.search(r"ClickHouse|Redis|Mongo|subcats|country_pri|target_id|extra_where|extra_sql|\btags\b|192\.168", text, re.I)
    for path in ("/v1/geography", "/v1/articles/{article_id}/related"):
        q = next(p for p in schema["paths"][path]["get"]["parameters"] if p["name"] == "q")
        assert q["required"] is True
    limit = next(p["schema"] for p in schema["paths"]["/v1/geography"]["get"]["parameters"]
                 if p["name"] == "limit")
    assert limit["default"] == 5 and limit["maximum"] == 5
    limit = next(p["schema"] for p in schema["paths"]["/v1/articles/{article_id}/related"]["get"]["parameters"]
                 if p["name"] == "limit")
    assert limit["default"] == 100 and "maximum" not in limit


def test_parent_app_wiring_uses_the_same_metered_routes(client, corpus):
    from prism_news_api.main import app

    with TestClient(app, raise_server_exceptions=False) as parent:
        for used, (method, path, data) in enumerate(ENDPOINTS, 1):
            response = request(parent, method, path, data)
            assert response.status_code == 200, response.text
            assert response.json()["meta"]["quota"]["requests"]["used"] == used
        schema = parent.get("/v1/openapi.json").json()
        for path in ("/v1/overview", "/v1/compare", "/v1/coverage", "/v1/geography",
                     "/v1/articles/{article_id}/related"):
            assert path in schema["paths"]
