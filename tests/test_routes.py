"""HTTP surface with every store stubbed: the envelope on success and on each
failure path, headers, the metered/unmetered split, export formats."""
from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from prism_news_api import articles, auth, ch, quota
from prism_news_api.envelope import ApiError
from prism_news_api.main import app

ROW = ["69f881d343843dd771cf50f2", "2026-08-20 10:00:00", 7, ["very_neg", 0.51],
       [["/News/Business News/Company News", 0.44]], [["bankruptcy filings and restructuring proceedings", 0.96]],
       None, ["spirit airlines"], [], "spirit airlines could cease operations soon"]
ROW2 = ["6a2ec2438e67a2fcb3c9a517", "2026-08-19 09:00:00", 5, ["slight_pos", 0.56], [], [], None, [], [],
        "uwmc issues superior offer"]
REC = {"69f881d343843dd771cf50f2": {"id": "69f881d343843dd771cf50f2", "headline": "Spirit could cease",
                                    "url": "https://www.cbsnews.com/x", "publisher": "cbsnews.com",
                                    "body": "full body " * 50, "body_chars": 500, "authors": ["A"],
                                    "top_image": None, "meta_description": "d", "publish_date": None,
                                    "language": "en"},
       "6a2ec2438e67a2fcb3c9a517": {"id": "6a2ec2438e67a2fcb3c9a517", "headline": "UWMC", "url": "https://m/x",
                                    "publisher": "minichart.com.sg", "body": "b" * 900, "body_chars": 900,
                                    "authors": [], "top_image": None, "meta_description": None,
                                    "publish_date": None, "language": "en"}}


class FakeCH:
    """Answers by SQL shape. Records every SQL so tests can assert on it."""

    def __init__(self):
        self.sql = []
        self.total = 2

    def rows(self, sql, timeout=None):
        self.sql.append(sql)
        s = " ".join(sql.split())
        if "GROUP BY label HAVING" in s:                              # themes
            return [["bankruptcy filings and restructuring proceedings", 40, 20], ["tiny", 3, 0]]
        if "arrayJoin(" in s and "GROUP BY label" in s:                # baselines
            if "subcats" in s:
                return [["bankruptcy filings and restructuring proceedings", 10], ["professional league updates", 900]]
            if "sentiments" in s:
                return [["very_neg", 300], ["slight_pos", 500], ["none", 100]]
            if "priorities" in s:
                return [[7, 700], [4, 400]]
            return [["/News/Business News/Company News", 1234]]
        if "GROUP BY period, label" in s:
            return [["2026-08-17", "very_neg", 3], ["2026-08-17", "slight_pos", 1]]
        if "AS band" in s:
            return [[7, 5], [4, 5]]
        if "GROUP BY period" in s:
            return [["2026-08-17", 10, 4, 3, 2]]
        if "ORDER BY" in s and "LIMIT" in s and "target_id" in s:      # headline rows
            return [ROW, ROW2][: (3 if "LIMIT 2" in s else 2)]
        return []

    def one(self, sql, timeout=None):
        self.sql.append(sql)
        s = " ".join(sql.split())
        if "countIf(" in s:
            if "'2026-07-26'" in s:                                    # the 30-day baseline window
                return [2000, 1200]
            return [self.total, self.total]
        if "target_id =" in s:
            return ROW if "69f881d343843dd771cf50f2" in s else None
        return [self.total]

    def scalar_int(self, sql, timeout=None):
        self.sql.append(sql)
        return self.total


@pytest.fixture
def client(monkeypatch, fake_redis, principal):
    fake = FakeCH()
    monkeypatch.setattr(ch, "rows", fake.rows)
    monkeypatch.setattr(ch, "one", fake.one)
    monkeypatch.setattr(ch, "scalar_int", fake.scalar_int)
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 255_586_690, "expected": 255_586_690,
                                                             "pct": 100.0, "partial": False, "checked_at": 0})
    monkeypatch.setattr(ch, "data_through", lambda force=False: "2026-08-24")
    monkeypatch.setattr(articles, "resolve", lambda ids, full=False: ({i: REC[i] for i in ids if i in REC}, []))
    monkeypatch.setattr(articles, "health", lambda all_nodes=False: {"available": True, "ring_nodes": 31})
    monkeypatch.setattr(quota, "record_daily", lambda *a, **k: None)

    def fake_auth(headers):
        k = headers.get("x-api-key") or (headers.get("authorization") or "")[7:]
        if not k:
            raise ApiError("unauthenticated", "no key")
        if k != "pna_" + "ab" * 20:
            raise ApiError("invalid_key", "unknown API key")
        return principal
    monkeypatch.setattr(auth, "authenticate", fake_auth)
    c = TestClient(app, raise_server_exceptions=False)
    c.fake, c.key = fake, "pna_" + "ab" * 20
    return c


def H(c):
    return {"X-API-Key": c.key}


def _env(r):
    b = r.json()
    assert set(b) >= {"ok", "feature", "subject", "data", "window", "meta"}
    return b


def test_no_key_401_envelope_and_bad_key_401(client):
    r = client.get("/v1/headlines")
    b = _env(r)
    assert r.status_code == 401 and b["error"]["kind"] == "unauthenticated"
    r = client.get("/v1/headlines", headers={"Authorization": "Bearer pna_" + "cd" * 20})
    assert r.status_code == 401 and r.json()["error"]["kind"] == "invalid_key"


def test_headlines_ok_headers_and_meta(client):
    r = client.get("/v1/headlines", params={"q": "spirit airlines", "limit": 2}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["ok"] and b["feature"] == "news.headlines"
    assert b["window"]["since"] == "2026-05-26" and b["window"]["until"] == "2026-08-24"
    assert b["window"]["freshness"].startswith("volume thins")
    assert b["meta"]["plan"] == "free" and b["meta"]["quota"]["requests"]["used"] == 1
    for h in ("X-RateLimit-Limit", "X-RateLimit-Remaining", "X-Quota-Requests-Remaining",
              "X-Quota-Exports-Remaining", "X-Plan"):
        assert h in r.headers, h
    assert r.headers["X-Plan"] == "free" and r.headers["X-Quota-Requests-Remaining"] == "999"
    items = b["data"]["items"]
    assert b["data"]["returned"] == 2 and b["data"]["total_estimate"] == 2
    it = items[0]
    assert it["id"] == ROW[0] and it["headline"] == "Spirit could cease" and it["publisher"] == "cbsnews.com"
    assert it["sentiment"] == {"label": "very_neg", "score": 0.51, "group": "negative"}
    assert it["priority"] == 7 and it["classes"][0]["code"] == 0
    assert "themes" not in it and it["organizations"] == ["spirit airlines"]
    assert "body" not in it
    assert b["subject"]["filters"]["q"] == "spirit airlines"


def test_headlines_next_cursor_when_more_rows(client):
    r = client.get("/v1/headlines", params={"limit": 1}, headers=H(client))
    b = r.json()
    assert b["data"]["returned"] == 1 and b["data"]["next_cursor"]
    r2 = client.get("/v1/headlines", params={"limit": 1, "cursor": b["data"]["next_cursor"]}, headers=H(client))
    assert r2.status_code == 200
    assert any("(datetime, target_id) < (toDateTime('2026-08-20 10:00:00'" in s for s in client.fake.sql)


def test_headlines_post_body_same_names(client):
    r = client.post("/v1/headlines", json={"q": "spirit airlines", "sentiment": ["negative"], "limit": 2},
                    headers=H(client))
    assert r.status_code == 200 and r.json()["subject"]["filters"]["sentiment"][0] == "extreme_neg"


def test_q_too_short_400(client):
    r = client.get("/v1/headlines", params={"q": "a"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 400 and b["error"]["kind"] == "bad_request" and b["feature"] == "news.headlines"
    assert "X-Plan" in r.headers


def test_unknown_class_code_400_and_limit_clamped_note(client):
    r = client.get("/v1/headlines", params={"classes": "0,999999"}, headers=H(client))
    assert r.status_code == 400 and "999999" in r.json()["error"]["reason"]
    r = client.get("/v1/headlines", params={"limit": 5000}, headers=H(client))
    assert r.status_code == 200
    assert any("clamped" in n for n in r.json()["meta"]["notes"])
    assert r.json()["data"]["limit"] == 100


def test_validation_error_is_envelope_400(client):
    r = client.get("/v1/headlines", params={"priority_min": 12}, headers=H(client))
    b = _env(r)
    assert r.status_code == 400 and b["error"]["kind"] == "bad_request" and "priority_min" in b["error"]["reason"]


def test_no_data_404(client):
    client.fake.total = 0
    r = client.get("/v1/headlines", params={"q": "zzzz qqqq"}, headers=H(client))
    assert r.status_code == 404 and r.json()["error"]["kind"] == "no_data"


def test_coverage_gate_503_before_query(client, monkeypatch):
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 1, "expected": 255_586_690,
                                                             "pct": 0.0, "partial": True, "checked_at": 0})
    n = len(client.fake.sql)
    r = client.get("/v1/headlines", headers=H(client))
    assert r.status_code == 503 and r.json()["error"]["kind"] == "coverage_unavailable"
    assert len(client.fake.sql) == n                       # no query ran


def test_serve_partial_answers_with_a_lower_bound_note(client, monkeypatch):
    from prism_news_api import config
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 237_398_763, "expected": 255_586_690,
                                                             "pct": 92.88, "partial": True, "checked_at": 0})
    monkeypatch.setattr(config, "PARTIAL_CAPTURE", True)
    r = client.get("/v1/headlines", headers=H(client))
    b = r.json()
    assert r.status_code == 200 and b["ok"]
    assert b["meta"]["notes"][0].startswith("Part of the news index is temporarily offline; this answer uses about 93%")
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 255_586_690, "expected": 255_586_690,
                                                             "pct": 100.0, "partial": False, "checked_at": 0})
    b = client.get("/v1/headlines", headers=H(client)).json()
    assert not any("temporarily offline" in n for n in b["meta"].get("notes") or [])


def test_rate_limit_429_with_retry_after(client, principal):
    principal.plan_cfg["rate_per_minute"] = 2
    client.get("/v1/me", headers=H(client))
    client.get("/v1/me", headers=H(client))
    r = client.get("/v1/me", headers=H(client))
    b = _env(r)
    assert r.status_code == 429 and b["error"]["kind"] == "rate_limited"
    assert "Retry-After" in r.headers and r.headers["X-RateLimit-Remaining"] == "0"


def test_request_quota_402_with_upgrade_url(client, principal):
    principal.plan_cfg["requests_per_month"] = 1
    assert client.get("/v1/headlines", headers=H(client)).status_code == 200
    r = client.get("/v1/headlines", headers=H(client))
    b = _env(r)
    assert r.status_code == 402 and b["error"]["kind"] == "quota_exceeded"
    assert b["error"]["upgrade_url"] == "https://fliarbi.com/radar/dashboard?tab=radarapi"
    assert b["meta"]["quota"]["requests"]["used"] == 1 and r.headers["X-Quota-Requests-Remaining"] == "0"
    assert client.get("/v1/me", headers=H(client)).status_code == 200      # unmetered still works


def test_unmetered_paths_do_not_consume_requests(client, fake_redis):
    for p in ("/v1/me", "/v1/status", "/v1/vocabulary", "/v1/classes?q=finance", "/v1/classes/0"):
        assert client.get(p, headers=H(client)).status_code == 200, p
    assert fake_redis.keys("pna:req:*") == []
    assert len(fake_redis.keys("pna:rl:*")) == 1


def test_article_charges_one_export_and_refunds_on_miss(client, fake_redis):
    r = client.get("/v1/articles/69f881d343843dd771cf50f2", headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["data"]["article"]["body"].startswith("full body")
    assert b["data"]["charged_exports"] == 1 and r.headers["X-Quota-Exports-Remaining"] == "99"
    r = client.get("/v1/articles/000000000000000000000000", headers=H(client))
    assert r.status_code == 404
    m = quota.month_key()
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{m}") == "1"        # miss refunded
    r = client.get("/v1/articles/not-an-id", headers=H(client))
    assert r.status_code == 400


def principal_id():
    return "64f000000000000000000abc"


def test_export_json_ndjson_csv(client, fake_redis):
    r = client.post("/v1/export", json={"limit": 2, "format": "json"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["data"]["returned"] == 2 and b["data"]["charged_exports"] == 2
    assert b["data"]["items"][0]["body"] and b["data"]["items"][0]["body_chars"] == 500
    m = quota.month_key()
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{m}") == "2"

    r = client.post("/v1/export", json={"limit": 2, "format": "ndjson"}, headers=H(client))
    assert r.status_code == 200 and r.headers["content-type"].startswith("application/x-ndjson")
    lines = r.text.strip().split("\n")
    first = json.loads(lines[0])
    assert first["ok"] and first["data"]["stream"] is True and "items" not in first["data"]
    assert len(lines) == 3 and json.loads(lines[1])["id"] == ROW[0]

    r = client.post("/v1/export", json={"limit": 2, "format": "csv"}, headers=H(client))
    assert r.status_code == 200 and r.headers["content-type"].startswith("text/csv")
    head = r.text.split("\n")[0]
    assert head == "id,headline,url,publisher,published_at,sentiment,priority,classes,body"
    assert r.headers["X-Export-Delivered"] == "2"
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{m}") == "6"

    r = client.post("/v1/export", json={"format": "xml"}, headers=H(client))
    assert r.status_code == 400


def test_export_402_when_no_exports_left(client, principal, fake_redis):
    principal.plan_cfg["exports_per_month"] = 2
    assert client.post("/v1/export", json={"limit": 2}, headers=H(client)).status_code == 200
    r = client.post("/v1/export", json={"limit": 2}, headers=H(client))
    assert r.status_code == 402 and r.json()["error"]["kind"] == "quota_exceeded"


def test_export_refunds_undelivered(client, monkeypatch, fake_redis):
    monkeypatch.setattr(articles, "resolve", lambda ids, full=False: ({ids[0]: REC[ids[0]]}, []))
    r = client.post("/v1/export", json={"limit": 2}, headers=H(client))
    b = r.json()
    assert b["data"]["returned"] == 1 and b["data"]["unresolved"] == 1 and b["data"]["charged_exports"] == 1
    m = quota.month_key()
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{m}") == "1"


def test_themes_lift_and_previous_period(client):
    r = client.get("/v1/themes", params={"q": "spirit airlines"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200
    it = b["data"]["items"]
    assert it[0]["theme"].startswith("bankruptcy") and it[0]["count"] == 40 and it[0]["previous_period_count"] == 20
    assert it[0]["delta_pct"] == 100.0 and it[0]["lift"] is not None and it[0]["lift"] > 1
    assert all(x["count"] >= 5 for x in it) and len(it) == 1          # 'tiny' (3 articles) dropped
    assert b["data"]["baseline"]["days"] == 30 and b["data"]["previous_period"]["until"] == "2026-05-25"


def test_sentiment_priority_trends(client):
    r = client.get("/v1/sentiment", params={"granularity": "weekly"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and len(b["data"]["labels"]) == 9 and len(b["data"]["groups"]) == 3
    assert b["data"]["groups"][0]["group"] == "negative" and b["data"]["timeline"]
    assert b["window"]["granularity"] == "weekly"
    r = client.get("/v1/sentiment", params={"granularity": "hourly"}, headers=H(client))
    assert r.status_code == 400
    r = client.get("/v1/priority", headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["data"]["critical"]["count"] == 5 and b["data"]["critical"]["share"] == 50.0
    assert len(b["data"]["bands"]) == 9
    r = client.get("/v1/trends", params={"granularity": "weekly"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["data"]["total"] == 10
    assert sum(1 for p in b["data"]["points"] if p["articles"] == 0) > 5   # zero-filled
    r = client.post("/v1/trends", json={"granularity": "monthly", "q": "spirit airlines"}, headers=H(client))
    assert r.status_code == 200 and r.json()["data"]["granularity"] == "monthly"


def test_classes_endpoints(client):
    r = client.get("/v1/classes", params={"q": "venture"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and any(i["code"] == 55 for i in b["data"]["items"])
    r = client.get("/v1/classes/0", headers=H(client))
    b = _env(r)
    assert b["data"]["path"] == "/News/Business News/Company News" and b["data"]["articles_30d"] == 1234
    assert "top_themes_30d" not in b["data"]
    r = client.get("/v1/classes/999999", headers=H(client))
    assert r.status_code == 400 and r.json()["error"]["kind"] == "bad_request"
    r = client.get("/v1/classes/0/headlines", headers=H(client))
    assert r.status_code == 200 and r.json()["feature"] == "news.class_headlines"
    assert r.json()["subject"]["filters"]["classes"] == [0]
    r = client.get("/v1/classes", params={"prefix": "/Nope"}, headers=H(client))
    assert r.status_code == 400


def test_theme_headlines_alias(client):
    r = client.get("/v1/themes/Bankruptcy Filings and Restructuring Proceedings/headlines", headers=H(client))
    assert r.status_code == 200 and r.json()["feature"] == "news.theme_headlines"
    assert r.json()["subject"]["filters"]["themes"] == ["bankruptcy filings and restructuring proceedings"]


def test_me_status_vocabulary(client):
    b = _env(client.get("/v1/me", headers=H(client)))
    assert b["feature"] == "api.me" and b["data"]["plan"]["name"] == "free" and "usage" in b["data"]
    b = _env(client.get("/v1/status", headers=H(client)))
    assert b["data"]["data_through"] == "2026-08-24" and b["data"]["healthy"] is True
    b = _env(client.get("/v1/vocabulary", headers=H(client)))
    assert len(b["data"]["sentiments"]) == 9 and "plans" in b["data"]


def test_unknown_route_and_method_are_envelopes(client):
    r = client.get("/v1/nothing", headers=H(client))
    b = _env(r)
    assert r.status_code == 404 and b["error"]["kind"] == "no_data"
    r = client.delete("/v1/headlines", headers=H(client))
    assert r.status_code == 405 and r.json()["error"]["kind"] == "bad_request"


def test_internal_error_never_leaks_traceback(client, monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("secret detail " + "x" * 500)
    monkeypatch.setattr(ch, "rows", boom)
    r = client.get("/v1/headlines", headers=H(client))
    b = _env(r)
    assert r.status_code == 500 and b["error"]["kind"] == "internal"
    assert "Traceback" not in r.text and len(b["error"]["reason"]) < 260


def test_healthz_and_openapi_need_no_key(client):
    assert client.get("/healthz").status_code == 200 and client.get("/healthz").json()["ok"] is True
    s = client.get("/v1/openapi.json").json()
    assert "/v1/headlines" in s["paths"] and "ApiKeyAuth" in s["components"]["securitySchemes"]
    assert client.get("/docs").status_code == 200


@pytest.mark.parametrize("params", [{}, {"q": " "}, {"q": "**"}, {"q": "??"}, {"q": "abc", "limit": 6}, {"q": "abc", "cursor": "anything"}])
def test_theme_discovery_requires_query_and_is_bounded(client, params):
    before = len(client.fake.sql)
    for method in ("get", "post"):
        r = (client.get("/v1/themes", params=params, headers=H(client)) if method == "get"
             else client.post("/v1/themes", json=params, headers=H(client)))
        assert r.status_code == 400
    assert len(client.fake.sql) == before


def test_theme_discovery_never_returns_more_than_five_or_directory_size(client, monkeypatch):
    original = client.fake.rows
    def many(sql, timeout=None):
        if "GROUP BY label HAVING" in sql:
            return [[f"theme {i}", 30 + i, 2] for i in range(12)]
        return original(sql, timeout)
    monkeypatch.setattr(ch, "rows", many)
    for method in ("get", "post"):
        r = (client.get("/v1/themes", params={"q": "spirit"}, headers=H(client)) if method == "get"
             else client.post("/v1/themes", json={"q": "spirit"}, headers=H(client)))
        b = r.json()
        assert r.status_code == 200
        assert len(b["data"]["items"]) == b["data"]["returned"] == 5
        assert b["data"]["next_cursor"] is None and b["data"]["total_estimate"] is None
        assert "subcats" not in r.text


def test_classes_do_not_offer_an_unrestricted_catalog_or_themes(client):
    assert client.get("/v1/classes", headers=H(client)).status_code == 400
    assert client.get("/v1/classes", params={"prefix": "/"}, headers=H(client)).status_code == 400
    b = client.get("/v1/classes", params={"q": "news"}, headers=H(client)).json()
    assert len(b["data"]["items"]) <= 5
    assert b["data"]["next_cursor"] is None
    b = client.get("/v1/classes/0", headers=H(client)).json()
    assert "top_themes_30d" not in b["data"] and len(b["data"]["children"]) <= 5


def test_public_failures_do_not_reveal_infrastructure(client, monkeypatch):
    def broken(*a, **k):
        raise RuntimeError("ClickHouse at 10.0.0.5:8123 SELECT subcats FROM " + ch.TABLE + " /home/user/secret")
    monkeypatch.setattr(ch, "rows", broken)
    r = client.get("/v1/headlines", headers=H(client))
    assert r.status_code == 500
    assert r.json()["error"]["reason"] == "The request could not be completed. Please try again later."
    for token in ("10.0.0.5", "ClickHouse", "subcats", "/home/", ch.TABLE):
        assert token not in r.text


def test_public_diagnostics_and_news_text_are_separate(client, monkeypatch):
    from prism_news_api.public import response
    payload = {"ok": True, "data": {"items": [{"body": "Redis and ClickHouse news"}],
                                      "table": {"table": "private.name"}},
               "meta": {"coverage": {"rows": 255586690, "expected": 255586690, "partial": False},
                        "notes": ["node 31 at 10.0.0.5 failed"], "sql": "select secret"}}
    out = response(payload)
    assert out["data"]["items"][0]["body"] == "Redis and ClickHouse news"
    assert "table" not in out["data"] and "sql" not in out["meta"]
    assert out["meta"]["coverage"] == {"available": True}
    assert "10.0.0.5" not in json.dumps(out)
    b = client.get("/v1/status", headers=H(client)).json()
    assert b["data"]["archive"]["article_count_display"] == "450M+"
    assert "corpus" not in b["data"] and "article_store" not in b["data"]
    assert set(client.get("/healthz").json()) == {"ok", "service", "version"}


def test_openapi_has_customer_language_and_required_theme_query(client):
    b = client.get("/v1/openapi.json").json()
    values = []
    def walk(v):
        if isinstance(v, dict):
            for key, item in v.items():
                if key in {"description", "summary"} and isinstance(item, str):
                    values.append(item.lower())
                walk(item)
        elif isinstance(v, list):
            for item in v: walk(item)
    walk(b)
    text = " ".join(values)
    for token in ("subcats", " tags", "clickhouse", "redis", "mongo", "country_pri", "cluster", "/home/"):
        assert token not in text, token
    params = {p["name"]: p for p in b["paths"]["/v1/themes"]["get"]["parameters"]}
    assert params["q"]["required"] and params["limit"]["schema"]["maximum"] == 5


def test_single_article_query_respects_plan_history(client):
    response = client.get("/v1/articles/" + ROW[0], headers=H(client))
    assert response.status_code == 200
    queries = [s for s in client.fake.sql if "target_id =" in s]
    assert queries and "datetime >= '2025-08-24'" in queries[-1]
    assert "datetime < '2026-08-25'" in queries[-1]


def test_theme_previous_period_does_not_read_beyond_plan_history(client):
    response = client.get("/v1/themes", params={"q": "spirit airlines", "since": "2025-08-24", "until": "2025-09-24"}, headers=H(client))
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["previous_period"] is None
    assert all(i["previous_period_count"] is None and i["delta_pct"] is None for i in data["items"])
    assert not any("2025-07-" in sql for sql in client.fake.sql)


def test_strict_gate_unless_partial_serving_is_switched_on(monkeypatch):
    from prism_news_api import ch, config
    from prism_news_api.envelope import ApiError
    assert ch._params(None)["skip_unavailable_shards"] == "0"
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"partial": True, "rows": 90, "expected": 100})
    import pytest as _pytest
    with _pytest.raises(ApiError):
        ch.require_coverage()
    monkeypatch.setattr(config, "PARTIAL_CAPTURE", True)
    assert ch._params(None)["skip_unavailable_shards"] == "1"
    assert ch.require_coverage()["rows"] == 90


def test_export_delivers_republished_copies_once(client, monkeypatch, fake_redis):
    ids = list(REC)[:2]
    copy = {**REC[ids[0]], "url": REC[ids[0]]["url"] + "-176/"}
    monkeypatch.setattr(articles, "resolve", lambda req, full=False: ({req[0]: REC[ids[0]], req[1]: copy}, []))
    b = client.post("/v1/export", json={"limit": 2}, headers=H(client)).json()
    assert b["data"]["returned"] == 1 and b["data"]["duplicates_dropped"] == 1 and b["data"]["charged_exports"] == 1
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{quota.month_key()}") == "1"


# ── pay-as-you-go: prepaid credits after the plan allowance ──────────────────
@pytest.fixture
def credits(monkeypatch):
    """A stand-in for the gateway's credit endpoints: records reserve/settle calls."""
    from prism_news_api import payg
    calls = {"reserve": [], "settle": [], "refuse": False}

    def post(path, body):
        if path.endswith("/reserve"):
            calls["reserve"].append(body)
            if calls["refuse"]:
                return 402, {"ok": False, "error": {"kind": "credits_required"}}
            return 200, {"ok": True, "data": {"request_id": f"r{len(calls['reserve'])}"}}
        calls["settle"].append(body)
        return 200, {"ok": True, "data": {"settled": True}}

    monkeypatch.setattr(payg, "enabled", lambda: True)
    monkeypatch.setattr(payg, "_post", post)
    return calls


def test_requests_past_the_plan_use_one_prepaid_credit(client, principal, credits):
    principal.plan_cfg["requests_per_month"] = 1
    assert client.get("/v1/headlines", headers=H(client)).status_code == 200
    assert credits["reserve"] == []
    r = client.get("/v1/headlines", headers=H(client))
    b = r.json()
    assert r.status_code == 200 and credits["reserve"][0]["units"] == 1
    assert credits["reserve"][0]["feature"] == "news:/v1/headlines"
    assert credits["settle"] == [{"request_id": "r1", "actual": 1}]
    assert any("1 prepaid credit" in n for n in b["meta"]["notes"])


def test_failed_paid_request_is_refunded_and_refusal_explains_pay_as_you_go(client, principal, credits, monkeypatch):
    principal.plan_cfg["requests_per_month"] = 0
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 1, "expected": 255_586_690,
                                                             "pct": 0.0, "partial": True, "checked_at": 0})
    assert client.get("/v1/headlines", headers=H(client)).status_code == 503
    assert credits["settle"] == [{"request_id": "r1", "actual": 0}]
    credits["refuse"] = True
    r = client.get("/v1/headlines", headers=H(client))
    assert r.status_code == 402 and "pay-as-you-go" in r.json()["error"]["reason"]


def test_export_beyond_plan_charges_credits_only_for_delivered_articles(client, principal, credits, fake_redis):
    principal.plan_cfg["exports_per_month"] = 1
    b = client.post("/v1/export", json={"limit": 2}, headers=H(client)).json()
    assert b["data"]["returned"] == 2 and b["data"]["charged_exports"] == 1 and b["data"]["charged_credits"] == 1
    assert credits["reserve"][-1]["units"] == 1 and credits["settle"][-1] == {"request_id": "r1", "actual": 1}
    assert fake_redis.get(f"pna:exp:u:{principal_id()}:{quota.month_key()}") == "1"
