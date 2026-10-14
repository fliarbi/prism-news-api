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
