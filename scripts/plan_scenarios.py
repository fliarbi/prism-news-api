#!/usr/bin/env python3
"""Turn the keyword research into docs/scenarios/plan.json: per segment, candidate
scenarios in search-demand order, each with the exact (validated) API calls behind
its page. capture_scenarios.py then keeps the first `target` populated ones."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import scenario_common as sc  # noqa: E402
from prism_news_api.features.explore import ExplorationFilters, GeographyFilters  # noqa: E402
from prism_news_api.filters import Filters  # noqa: E402
from prism_news_api.routers import FiltersWithGranularity, ThemeFilters  # noqa: E402

RESEARCH_FILE = sc.RESEARCH / "keyword-research-2026-10-16.json"
TARGET = 50
WINDOW = {"since": "2026-01-01", "until": "2026-04-30"}
YEAR = {"since": "2025-05-01", "until": "2026-04-30"}
MODELS = {"/v1/overview": ExplorationFilters, "/v1/trends": FiltersWithGranularity,
          "/v1/geography": GeographyFilters, "/v1/themes": ThemeFilters, "/v1/headlines": Filters}


def calls(q: str) -> list[dict]:
    out = [
        {"name": "overview", "method": "POST", "path": "/v1/overview", "body": {"q": q, **WINDOW}},
        {"name": "trends", "method": "POST", "path": "/v1/trends", "body": {"q": q, **YEAR, "granularity": "monthly"}},
        {"name": "geography", "method": "POST", "path": "/v1/geography", "body": {"q": q, **WINDOW}},
        {"name": "themes", "method": "POST", "path": "/v1/themes", "body": {"q": q, **WINDOW}},
        {"name": "headlines", "method": "POST", "path": "/v1/headlines",
         "body": {"q": q, **WINDOW, "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}},
    ]
    for c in out:
        MODELS[c["path"]].model_validate(c["body"])
    return out


def main() -> None:
    research = json.loads(RESEARCH_FILE.read_text())
    segments = []
    for seg in research["segments"]:
        scen = []
        for t in seg["topics"]:
            if t.get("excluded"):
                continue
            scen.append({"slug": sc.slugify(t["target"]["phrase"]), "segment": seg["id"], "topic": t["topic"],
                         "q": t["q"], "keyword": t["target"], "score": t["score"], "calls": calls(t["q"]),
                         "primary": {"call": "overview", "field": "matched", "min": 60}})
        segments.append({"id": seg["id"], "title": seg["title"], "target": TARGET, "scenarios": scen})
    sc.SCEN.mkdir(parents=True, exist_ok=True)
    sc.PLAN.write_text(json.dumps({"window": WINDOW, "year": YEAR, "research": RESEARCH_FILE.name,
                                   "segments": segments}, indent=1, ensure_ascii=False) + "\n")
    print({s["id"]: len(s["scenarios"]) for s in segments})


if __name__ == "__main__":
    main()
