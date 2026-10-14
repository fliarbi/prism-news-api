"""config — environment, defaults and the plan catalog.

Everything that points at infrastructure comes from `PRISM_*` environment
variables. A `.env` file at the repo root (or at `PRISM_ENV_FILE`) is read
first; real environment variables win. The defaults are local placeholders, so
the deployment's addresses, credentials and table names live only in `.env`
(see `.env.example`). Nothing here opens a connection — the modules that own a
store do that lazily.
"""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_DIR = Path(__file__).resolve().parent

PRODUCT = "prism_api"
KEY_PREFIX = "pna_"
KEY_LENGTH = 44                      # "pna_" + 40 hex
UPGRADE_URL = "https://fliarbi.com/radar/dashboard?tab=apikeys"


def load_env_file(path: Path | str) -> None:
    """KEY=VALUE lines into os.environ without overriding what is already set."""
    try:
        lines = Path(path).read_text().splitlines()
    except OSError:
        return
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip().removeprefix("export ").strip(), v.strip().strip("'\""))


load_env_file(os.environ.get("PRISM_ENV_FILE") or REPO_ROOT / ".env")


def _env(name: str, default):
    v = os.environ.get(name)
    return v if v not in (None, "") else default


# ── ClickHouse ───────────────────────────────────────────────────────────────
CH_HOST = _env("PRISM_CH_HOST", "http://localhost:8123").rstrip("/")
CH_USER = _env("PRISM_CH_USER", "default")
CH_PASSWORD = _env("PRISM_CH_PASSWORD", "")
CH_MAX_EXECUTION_TIME = int(_env("PRISM_CH_MAX_EXECUTION_TIME", "60"))
CH_MAX_THREADS = int(_env("PRISM_CH_MAX_THREADS", "12"))
CH_PRIORITY = int(_env("PRISM_CH_PRIORITY", "10"))
NEWS_TABLE = _env("PRISM_NEWS_TABLE", "news.articles")
# Strict row count on 2026-09-13. A shard outage returns SMALLER numbers, not
# an error, so the coverage gate compares against this floor (re-measured hourly).
EXPECTED_ROWS = 255_586_690

# ── MongoDB (identity) ───────────────────────────────────────────────────────
MONGO_URI = _env("PRISM_MONGO_URI", "mongodb://localhost:27017/")
AUTH_DB = _env("PRISM_AUTH_DB", "prism_auth")

# ── Redis (counters, baselines) ──────────────────────────────────────────────
REDIS_HOST = _env("PRISM_REDIS_HOST", "localhost")
REDIS_PORT = int(_env("PRISM_REDIS_PORT", "6379"))
REDIS_DB = int(_env("PRISM_REDIS_DB", "6"))
REDIS_PREFIX = "pna:"

# ── article store ring ───────────────────────────────────────────────────────
NEWS_COMMON = _env("PRISM_NEWS_COMMON", "")
NEWS_COMMON_FALLBACK = _env("PRISM_NEWS_COMMON_FALLBACK", "")

# ── catalog + data files ─────────────────────────────────────────────────────
_DEFAULT_PLANS = REPO_ROOT / "plans.json"
if not _DEFAULT_PLANS.is_file():
    _DEFAULT_PLANS = PACKAGE_DIR / "data" / "plans.json"
PLANS_PATH = Path(_env("PRISM_PLANS_PATH", str(_DEFAULT_PLANS)))
GCP_CLASSES_PATH = PACKAGE_DIR / "data" / "gcp_classes.json"
LOG_DIR = Path(_env("PRISM_LOG_DIR", str(REPO_ROOT / "logs")))

# ── product constants (measured 2026-09-13) ──────────────────────────────────
DEFAULT_WINDOW_DAYS = 90
DEFAULT_LIMIT = 100
CLASS_THRESHOLD = 0.39               # the pipeline's own GCP score threshold
CRITICAL_PRIORITY = 7
THEMES_DEFAULT_LIMIT = 5
THEMES_MAX_LIMIT = 5
ARCHIVE_SIZE_DISPLAY = "450M+"
THEMES_MIN_ARTICLES = 5
BASELINE_DAYS = 30
BASELINE_TTL = 86_400                # 24 h
COVERAGE_TTL = 3_600                 # re-measure count() hourly
COVERAGE_FAILURE_TTL = 30            # retry a failed measurement soon
DATA_THROUGH_TTL = 3_600
LASTUSED_TTL = 300                   # api_keys.last_used_at written at most per 5 min
AUTH_CACHE_TTL = 15                  # seconds a resolved key is held in-process
QUOTA_KEY_TTL = 45 * 86_400
RATE_KEY_TTL = 120
FRESHNESS_NOTE = "volume thins after 2026-05; the last months are partial"
COUNTRY_NOTE = ("Location coverage is incomplete and can be less complete for recent articles. "
                "A lower geographic count does not necessarily mean less news activity.")
GRANULARITIES = ("daily", "weekly", "monthly")
DEFAULT_GRANULARITY = "weekly"
EXPORT_FORMATS = ("json", "ndjson", "csv")

PUBLIC_PLAN_FIELDS = ("label", "requests_per_month", "exports_per_month",
                      "max_results", "max_export_batch", "rate_per_minute",
                      "history_days", "max_keys", "business_api",
                      "price_monthly_inr", "price_monthly_usd", "contact_sales")


def test_request_limit() -> int | None:
    """`PRISM_TEST_REQUEST_LIMIT` — honoured ONLY when set; overrides the plan's
    requests_per_month so the 402 path can be exercised without a real plan.
    Read per call so a test can set it after import."""
    v = os.environ.get("PRISM_TEST_REQUEST_LIMIT")
    return int(v) if v and v.isdigit() else None


# ── plan catalog: hot-reloaded on mtime ──────────────────────────────────────
_PLANS_LOCK = threading.Lock()
_PLANS_CACHE: dict | None = None
_PLANS_MTIME: float = -1.0


def plans(path: Path | None = None) -> dict:
    """The plan catalog (`plans.json` at the repo root), re-read when its mtime
    changes. The `_meta` block is stripped."""
    global _PLANS_CACHE, _PLANS_MTIME
    p = Path(path) if path else PLANS_PATH
    with _PLANS_LOCK:
        try:
            mtime = os.path.getmtime(p)
        except OSError:
            mtime = 0.0
        if _PLANS_CACHE is None or mtime != _PLANS_MTIME or path is not None:
            with open(p) as f:
                raw = json.load(f)
            cat = {k: v for k, v in raw.items() if not k.startswith("_")}
            if path is not None:
                return cat
            _PLANS_CACHE, _PLANS_MTIME = cat, mtime
        return _PLANS_CACHE


def plan_cfg(name: str | None, catalog: dict | None = None) -> dict:
    cat = catalog if catalog is not None else plans()
    return dict(cat.get(name or "free") or cat.get("free") or {})


def public_plan(cfg: dict) -> dict:
    return {k: cfg.get(k) for k in PUBLIC_PLAN_FIELDS if k in cfg}
