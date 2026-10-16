"""Shared fixtures. No network anywhere in tests: Redis, Mongo, ClickHouse and
the article-store ring are replaced by in-memory stubs."""
from __future__ import annotations

import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prism_news_api import auth, config  # noqa: E402


class FakePipeline:
    def __init__(self, r):
        self.r, self.ops = r, []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.ops.append((name, a, k))
            return self
        return rec

    def execute(self):
        return [getattr(self.r, n)(*a, **k) for n, a, k in self.ops]


class FakeRedis:
    """Enough of redis-py for quota.py: strings, INCR/INCRBY/DECR/DECRBY,
    SET NX EX, EXPIRE, GET, DEL, KEYS, pipeline()."""

    def __init__(self):
        self.d: dict = {}
        self.ttl: dict = {}

    def get(self, k):
        return self.d.get(k)

    def set(self, k, v, nx=False, ex=None):
        if nx and k in self.d:
            return None
        self.d[k] = str(v)
        if ex:
            self.ttl[k] = ex
        return True

    def incr(self, k):
        return self.incrby(k, 1)

    def incrby(self, k, n):
        self.d[k] = str(int(self.d.get(k) or 0) + int(n))
        return int(self.d[k])

    def decr(self, k):
        return self.incrby(k, -1)

    def decrby(self, k, n):
        return self.incrby(k, -int(n))

    def expire(self, k, s):
        self.ttl[k] = s
        return True

    def delete(self, *ks):
        n = 0
        for k in ks:
            n += 1 if self.d.pop(k, None) is not None else 0
        return n

    def keys(self, pattern="*"):
        import fnmatch
        return [k for k in self.d if fnmatch.fnmatch(k, pattern)]

    def ping(self):
        return True

    def pipeline(self):
        return FakePipeline(self)


@pytest.fixture
def fake_redis(monkeypatch):
    from prism_news_api import quota
    r = FakeRedis()
    monkeypatch.setattr(quota, "redis_client", lambda: r)
    return r


@pytest.fixture
def plans():
    return config.plans()


@pytest.fixture
def free_cfg(plans):
    return dict(plans["free"])


@pytest.fixture
def principal(free_cfg):
    return auth.Principal(user_id="64f000000000000000000abc", key_id="000000000000000000000001",
                          key_prefix="pna_test0000", key_name="t", email="t@example.com",
                          plan="free", plan_cfg=free_cfg, source="free", expired=False,
                          expires=None, account_flag=None, notes=[])


DATA_THROUGH = "2026-08-24"


@pytest.fixture
def data_through():
    return DATA_THROUGH


@pytest.fixture(autouse=True)
def _strict_coverage_by_default(monkeypatch):
    """Tests assume the strict coverage gate whatever the deployment's .env sets
    (PRISM_SERVE_PARTIAL); partial-serving tests switch it on explicitly."""
    from prism_news_api import config as _config
    monkeypatch.setattr(_config, "PARTIAL_CAPTURE", False)
