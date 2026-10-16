"""auth: header extraction, key format, plan resolution (missing → free,
expired → free, kill-switch → free with account_flag, test override)."""
from __future__ import annotations

import datetime as dt

import pytest

from prism_news_api import auth, config
from prism_news_api.envelope import ApiError

NOW = dt.datetime(2026, 9, 13, 12, 0, 0)
KEY = "pna_" + "ab" * 20


def test_extract_key_header_forms():
    assert auth.extract_key({"x-api-key": KEY}) == KEY
    assert auth.extract_key({"authorization": f"Bearer {KEY}"}) == KEY
    assert auth.extract_key({"authorization": "Basic xyz"}) is None
    assert auth.extract_key({}) is None


def test_hash_is_sha256_hex():
    assert auth.hash_key(KEY) == __import__("hashlib").sha256(KEY.encode()).hexdigest()


def test_missing_key_is_unauthenticated_and_malformed_is_invalid():
    with pytest.raises(ApiError) as e:
        auth.authenticate({})
    assert e.value.kind == "unauthenticated" and e.value.status == 401
    with pytest.raises(ApiError) as e:
        auth.authenticate({"x-api-key": "sk_live_nope"})
    assert e.value.kind == "invalid_key" and e.value.status == 401
    with pytest.raises(ApiError):
        auth.authenticate({"x-api-key": "pna_" + "zz" * 20})   # not hex


def test_plan_missing_is_free(plans):
    ctx = auth.plan_context({"email": "x"}, plans, NOW)
    assert ctx["plan"] == "free" and ctx["source"] == "free" and not ctx["expired"]
    assert ctx["plan_cfg"]["requests_per_month"] == plans["free"]["requests_per_month"]


def test_paid_plan_active(plans):
    u = {"entitlements": {"prism_api": {"plan": "pro", "expires": NOW + dt.timedelta(days=10),
                                        "source": "dedicated"}}}
    ctx = auth.plan_context(u, plans, NOW)
    assert ctx["plan"] == "pro" and ctx["plan_cfg"]["history_days"] is None
    assert ctx["expires"].startswith("2026-09-23")


def test_expired_plan_falls_back_to_free(plans):
    u = {"entitlements": {"prism_api": {"plan": "pro", "expires": NOW - dt.timedelta(seconds=1)}}}
    ctx = auth.plan_context(u, plans, NOW)
    assert ctx["plan"] == "free" and ctx["expired"] is True
    assert any("expired" in n for n in ctx["notes"])


def test_no_cross_grant_from_radar_plan(plans):
    u = {"plan": "pro", "entitlements": {"radar": {"plan": "pro", "expires": NOW + dt.timedelta(days=30),
                                                   "source": "dedicated"}}}
    assert auth.plan_context(u, plans, NOW)["plan"] == "free"


@pytest.mark.parametrize("flag,field", [("banned", {"banned": True}), ("disabled", {"disabled": True}),
                                        ("email_unverified", {"email_verified": False})])
def test_kill_switch_forces_free_with_account_flag(plans, flag, field):
    u = {"entitlements": {"prism_api": {"plan": "business", "expires": NOW + dt.timedelta(days=30)}}, **field}
    ctx = auth.plan_context(u, plans, NOW)
    assert ctx["plan"] == "free" and ctx["account_flag"] == flag


def test_unknown_plan_name_is_free(plans):
    u = {"entitlements": {"prism_api": {"plan": "platinum", "expires": None}}}
    ctx = auth.plan_context(u, plans, NOW)
    assert ctx["plan"] == "free" and any("catalog" in n for n in ctx["notes"])


def test_test_request_limit_override_only_when_set(plans, monkeypatch):
    monkeypatch.delenv("PRISM_TEST_REQUEST_LIMIT", raising=False)
    assert auth.plan_context({}, plans, NOW)["plan_cfg"]["requests_per_month"] == plans["free"]["requests_per_month"]
    monkeypatch.setenv("PRISM_TEST_REQUEST_LIMIT", "3")
    ctx = auth.plan_context({}, plans, NOW)
    assert ctx["plan_cfg"]["requests_per_month"] == 3 and any("override" in n for n in ctx["notes"])


def test_plans_catalog_shape(plans):
    assert set(plans) >= {"free", "pro", "business", "enterprise"}
    for name, cfg in plans.items():
        for k in ("requests_per_month", "exports_per_month", "max_results", "max_export_batch",
                  "rate_per_minute", "max_keys"):
            assert isinstance(cfg[k], int), (name, k)
    assert plans["free"]["history_days"] == 365
    assert config.public_plan(plans["free"])["label"] == "Free"


# ── rdr_ keys: one key for Radar API and Prism News ──────────────────────────
RDR = "rdr_" + "cd" * 32
USER_ID = "64b7f0c2a1b2c3d4e5f60718"


@pytest.fixture
def gateway(monkeypatch):
    """A stand-in for the Radar API gateway's private key check."""
    import json
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    seen = {}
    reply = {"ok": True, "data": {"active": True, "account_id": USER_ID, "key_id": "k1", "name": "My app",
                                  "last4": "cdcd", "scopes": ["*"], "expires_at": 0}}

    class H(BaseHTTPRequestHandler):
        def do_POST(self):
            seen["path"], seen["secret"], seen["host"] = self.path, self.headers.get("X-Introspect-Secret"), self.headers.get("Host")
            seen["body"] = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            out = json.dumps(reply).encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(out)))
            self.end_headers()
            self.wfile.write(out)

        def log_message(self, *a):
            pass

    srv = HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    monkeypatch.setattr(config, "RADAR_KEYS_URL", f"http://127.0.0.1:{srv.server_port}")
    monkeypatch.setattr(config, "RADAR_KEYS_SECRET", "x" * 40)
    monkeypatch.setattr(config, "RADAR_KEYS_HOST", "radar-api.example")

    from bson import ObjectId

    class Users:
        def find_one(self, q, proj=None):
            return {"_id": q["_id"], "email": "a@example.com", "email_verified": True} if q["_id"] == ObjectId(USER_ID) else None

    class DB:
        users = Users()

    monkeypatch.setattr(auth, "mongo_db", lambda: DB())
    monkeypatch.setattr(auth, "touch_last_used", lambda key_id: None)
    auth.clear_cache()
    yield seen, reply
    srv.shutdown()
    auth.clear_cache()


def test_radar_key_resolves_to_the_same_account_and_news_plan(gateway):
    seen, _ = gateway
    p = auth.authenticate({"x-api-key": RDR})
    assert p.user_id == USER_ID and p.plan == "free" and p.key_prefix == "rdr_…cdcd" and p.key_id == "rdr:k1"
    assert seen["path"] == "/internal/keys/introspect" and seen["secret"] == "x" * 40
    assert seen["host"] == "radar-api.example" and seen["body"] == {"api_key": RDR}


@pytest.mark.parametrize("data,reason", [({"active": False, "reason": "unauthorized"}, "revoked"),
                                         ({"active": True, "account_id": USER_ID, "scopes": ["companies"]}, "news access"),
                                         ({"active": True, "account_id": "64b7f0c2a1b2c3d4e5f60719", "scopes": ["news"]}, "no account")])
def test_radar_key_rejected_when_inactive_unscoped_or_unknown(gateway, data, reason):
    _, reply = gateway
    reply["data"] = data
    with pytest.raises(ApiError) as e:
        auth.authenticate({"x-api-key": RDR})
    assert e.value.kind == "invalid_key" and reason in e.value.reason


def test_radar_keys_refused_when_not_configured(monkeypatch):
    monkeypatch.setattr(config, "RADAR_KEYS_URL", "")
    auth.clear_cache()
    with pytest.raises(ApiError) as e:
        auth.authenticate({"x-api-key": RDR})
    assert e.value.kind == "invalid_key"


def test_radar_key_service_down_is_upstream_not_invalid(monkeypatch):
    monkeypatch.setattr(config, "RADAR_KEYS_URL", "http://127.0.0.1:9")
    monkeypatch.setattr(config, "RADAR_KEYS_SECRET", "x" * 40)
    auth.clear_cache()
    with pytest.raises(ApiError) as e:
        auth.authenticate({"x-api-key": RDR})
    assert e.value.kind == "upstream"
