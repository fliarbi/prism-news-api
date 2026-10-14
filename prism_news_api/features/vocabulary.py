"""vocabulary — GET /v1/vocabulary: the closed vocabularies a caller filters
with, plus the plan limits table. Static; unmetered."""
from __future__ import annotations

import time

from .. import config, envelope, taxonomy
from ..auth import Principal
from . import _common as c


def vocabulary(p: Principal) -> dict:
    t0 = time.time()
    data = taxonomy.vocabulary()
    data["filters"] = ["q", "match", "sentiment", "classes", "class_prefix", "themes", "priority_min",
                       "priority_max", "country", "since", "until", "limit", "sort", "cursor"]
    data["defaults"] = {"window_days": config.DEFAULT_WINDOW_DAYS, "limit": config.DEFAULT_LIMIT,
                        "themes_limit": config.THEMES_DEFAULT_LIMIT,
                        "granularity": config.DEFAULT_GRANULARITY, "export_format": "json"}
    data["plans"] = {name: config.public_plan(cfg) for name, cfg in config.plans().items()}
    data["your_plan"] = p.plan
    return envelope.ok("news.vocabulary", data, subject={}, window={"freshness": config.FRESHNESS_NOTE},
                       meta={"seconds": round(time.time() - t0, 3), "notes": []})
