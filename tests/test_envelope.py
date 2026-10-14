from __future__ import annotations

import pytest

from prism_news_api import envelope
from prism_news_api.envelope import ApiError


def test_kind_status_map_matches_design():
    assert envelope.KINDS == {"bad_request": 400, "unauthenticated": 401, "invalid_key": 401,
                              "quota_exceeded": 402, "rate_limited": 429, "no_data": 404,
                              "upstream": 502, "coverage_unavailable": 503, "internal": 500}


def test_ok_shape():
    e = envelope.ok("news.headlines", {"items": []}, subject={"filters": {}}, window={"since": "x"})
    assert set(e) == {"ok", "feature", "subject", "data", "window", "meta"}
    assert e["ok"] is True and envelope.status_of(e) == 200


def test_fail_shape_and_unknown_kind_becomes_internal():
    e = envelope.fail("news.x", "boom", kind="quota_exceeded", upgrade_url="https://u")
    assert e["ok"] is False and e["data"] is None
    assert e["error"] == {"kind": "quota_exceeded", "reason": "boom", "upgrade_url": "https://u"}
    assert envelope.status_of(e) == 402
    assert envelope.fail("f", "r", kind="weird")["error"]["kind"] == "internal"


@pytest.mark.parametrize("kind,status", list(envelope.KINDS.items()))
def test_api_error_status(kind, status):
    e = ApiError(kind, "why", headers={"Retry-After": "7"}, fields={"x": 1}, meta={"m": 2})
    assert e.status == status
    env = e.envelope("news.f", meta={"n": 3})
    assert env["error"]["kind"] == kind and env["error"]["x"] == 1
    assert env["meta"] == {"m": 2, "n": 3} and envelope.status_of(env) == status


def test_list_data():
    d = envelope.list_data([1, 2], total_estimate=9, next_cursor="c", unresolved=0)
    assert d == {"items": [1, 2], "returned": 2, "total_estimate": 9, "next_cursor": "c", "unresolved": 0}
