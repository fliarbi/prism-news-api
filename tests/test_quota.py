"""quota math against an in-memory Redis stub: rate buckets, monthly request
counter with rollback, export reserve/refund, snapshot + headers."""
from __future__ import annotations

import pytest

from prism_news_api import quota
from prism_news_api.envelope import ApiError

U, K = "64f000000000000000000abc", "000000000000000000000001"


def test_rate_limit_increments_then_429_with_retry_after(fake_redis):
    for i in range(3):
        out = quota.check_rate(U, 3)
        assert out["remaining"] == 2 - i
    with pytest.raises(ApiError) as e:
        quota.check_rate(U, 3)
    assert e.value.kind == "rate_limited" and e.value.status == 429
    assert 1 <= int(e.value.headers["Retry-After"]) <= 60
    key = [k for k in fake_redis.keys("pna:rl:u:*")][0]
    assert fake_redis.ttl[key] == 120


def test_request_quota_counts_user_and_key_and_rolls_back_at_limit(fake_redis):
    m = quota.month_key()
    for _ in range(3):
        quota.check_requests(U, K, 3)
    assert fake_redis.get(f"pna:req:u:{U}:{m}") == "3"
    assert fake_redis.get(f"pna:req:k:{K}:{m}") == "3"
    with pytest.raises(ApiError) as e:
        quota.check_requests(U, K, 3)
    assert e.value.kind == "quota_exceeded" and e.value.status == 402
    assert e.value.fields["upgrade_url"].startswith("https://fliarbi.com")
    assert e.value.meta["quota"]["requests"]["used"] == 3
    assert fake_redis.get(f"pna:req:u:{U}:{m}") == "3"          # the failed call was rolled back
    assert fake_redis.ttl[f"pna:req:u:{U}:{m}"] == 45 * 86400


def test_reserve_then_refund(fake_redis):
    m = quota.month_key()
    granted = quota.reserve_exports(U, K, 10, 100)
    assert granted == 10 and fake_redis.get(f"pna:exp:u:{U}:{m}") == "10"
    assert fake_redis.get(f"pna:exp:k:{K}:{m}") == "10"
    quota.refund_exports(U, K, 4)                                   # 6 delivered
    assert fake_redis.get(f"pna:exp:u:{U}:{m}") == "6"
    assert fake_redis.get(f"pna:exp:k:{K}:{m}") == "6"
    assert quota.exports_remaining(U, K, 100) == 94


def test_reserve_clamps_to_remaining_and_402_when_none_left(fake_redis):
    m = quota.month_key()
    assert quota.reserve_exports(U, K, 8, 10) == 8
    assert quota.reserve_exports(U, K, 5, 10) == 2                  # only 2 left
    assert fake_redis.get(f"pna:exp:u:{U}:{m}") == "10"             # never over the limit
    with pytest.raises(ApiError) as e:
        quota.reserve_exports(U, K, 1, 10)
    assert e.value.kind == "quota_exceeded"
    assert fake_redis.get(f"pna:exp:u:{U}:{m}") == "10"             # rollback left it at the limit
    assert quota.reserve_exports(U, K, 0, 10) == 0


def test_refund_never_raises_and_ignores_nonpositive(fake_redis):
    quota.refund_exports(U, K, 0)
    quota.refund_exports(U, K, -3)
    assert fake_redis.keys("pna:exp:*") == []


def test_usage_snapshot_and_headers(fake_redis):
    quota.check_requests(U, K, 1000)
    quota.reserve_exports(U, K, 7, 100)
    snap = quota.usage(U, K, {"requests_per_month": 1000, "exports_per_month": 100, "rate_per_minute": 30},
                       rate={"limit": 30, "remaining": 29, "window": "minute"})
    assert snap["requests"] == {"used": 1, "limit": 1000, "remaining": 999}
    assert snap["exports"] == {"used": 7, "limit": 100, "remaining": 93}
    assert snap["this_key"] == {"requests": 1, "exports": 7}
    h = quota.headers_for(snap, "free")
    assert h == {"X-Plan": "free", "X-RateLimit-Limit": "30", "X-RateLimit-Remaining": "29",
                 "X-Quota-Requests-Remaining": "999", "X-Quota-Exports-Remaining": "93"}
    assert quota.headers_for(None, "pro") == {"X-Plan": "pro"}


def test_redis_down_is_fail_closed(monkeypatch):
    class Boom:
        def __getattr__(self, n):
            raise ConnectionError("down")
    monkeypatch.setattr(quota, "redis_client", lambda: Boom())
    with pytest.raises(ApiError) as e:
        quota.check_rate(U, 30)
    assert e.value.kind == "upstream" and e.value.status == 502


def test_cache_helpers(fake_redis):
    quota.cache_put("baseline:test", {"a": 1}, 60)
    assert quota.cache_get("baseline:test") == {"a": 1}
    assert fake_redis.ttl["pna:baseline:test"] == 60
    assert quota.cache_get("nope") is None
