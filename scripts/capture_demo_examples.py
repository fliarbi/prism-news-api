#!/usr/bin/env python3
"""Capture the API responses behind the animated use-case demos.

Runs real requests against a running News API and saves each response under
docs/examples/demo/, replacing the illustrative fixture of the same name.
Requests that fail (for example `coverage_unavailable` while the archive is
partly offline) are reported and leave the existing file untouched, so a demo
stays labelled illustrative until a real capture succeeds. Account details
(plan, quota, key) are removed before saving.

    PRISM_API_BASE=http://127.0.0.1:8800 PRISM_API_KEY=pna_... \\
        python3 scripts/capture_demo_examples.py [--only NAME]

Then rebuild: build_use_case_demos.py, render_use_case_demos.mjs, check_use_case_demos.py.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "docs/examples/demo"
WINDOW = {"since": "2026-03-02", "until": "2026-04-26"}

# name -> (method, path, body or query, extra). Bodies may reference an earlier
# capture with {"$from": name, "$theme": index} to reuse a discovered theme.
CAPTURES: dict[str, tuple[str, str, dict]] = {
    "ev-themes": ("POST", "/v1/themes", {"q": "electric vehicle", **WINDOW, "limit": 5}),
    "ev-theme-headlines": ("POST", "/v1/headlines", {"q": "electric vehicle", **WINDOW, "limit": 6,
                                                      "themes": {"$from": "ev-themes", "$theme": 0}}),
    "tariff-sentiment": ("POST", "/v1/sentiment", {"q": "tariffs", **WINDOW, "granularity": "weekly"}),
    "tariff-negative-headlines": ("POST", "/v1/headlines", {"q": "tariffs", **WINDOW, "sentiment": ["negative"],
                                                            "priority_min": 6, "limit": 20}),
    "ai-compare": ("POST", "/v1/compare", {"queries": [
        {"name": "AI regulation", "filters": {"q": "AI regulation", **WINDOW}},
        {"name": "AI investment", "filters": {"q": "AI investment", **WINDOW}}]}),
    "ai-regulation-trends": ("POST", "/v1/trends", {"q": "AI regulation", **WINDOW, "granularity": "weekly"}),
    "ai-investment-trends": ("POST", "/v1/trends", {"q": "AI investment", **WINDOW, "granularity": "weekly"}),
    "semiconductor-priority": ("POST", "/v1/priority", {"q": "semiconductor", **WINDOW}),
    "semiconductor-critical": ("POST", "/v1/headlines", {"q": "semiconductor", **WINDOW, "priority_min": 7,
                                                         "limit": 20}),
    "class-map-vehicle": ("GET", "/v1/classes", {"q": "vehicle", "limit": 5}),
    "class-map-banking": ("GET", "/v1/classes", {"q": "banking", "limit": 5}),
    "battery-export": ("POST", "/v1/export", {"q": "battery storage", **WINDOW, "limit": 15, "format": "json"}),
}

PRIVATE_META = ("plan", "quota", "key", "account")


def call(base: str, key: str, method: str, path: str, body: dict) -> tuple[int, dict]:
    url, data = base + path, None
    if method == "GET":
        url += "?" + urllib.parse.urlencode(body)
    else:
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"X-API-Key": key, "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(int(e.headers.get("Retry-After") or 20))
                continue
            return e.code, json.loads(e.read() or b"{}")
    return 429, {"ok": False, "error": {"kind": "rate_limited"}}


def resolve(body: dict) -> dict:
    out = {}
    for k, v in body.items():
        if isinstance(v, dict) and "$from" in v:
            src = json.loads((DEST / f"{v['$from']}.json").read_text())
            if src.get("kind") != "captured":
                raise LookupError(f"needs a captured {v['$from']} first")
            v = [src["response"]["data"]["items"][v["$theme"]]["theme"]]
        out[k] = v
    return out


def capture(base: str, key: str, name: str) -> str:
    method, path, body = CAPTURES[name]
    try:
        body = resolve(body)
    except (LookupError, OSError) as e:
        return f"skipped ({e})"
    status, payload = call(base, key, method, path, body)
    if status != 200 or not payload.get("ok"):
        return f"not captured: HTTP {status} {(payload.get('error') or {}).get('kind')}"
    payload["meta"] = {k: v for k, v in (payload.get("meta") or {}).items() if k not in PRIVATE_META}
    record = {"name": name, "kind": "captured",
              # set with PRISM_PARTIAL_CAPTURE runs, e.g. "93% of archive rows (1 of 14 shards offline)"
              **({"coverage_note": os.environ["PRISM_CAPTURE_COVERAGE"]} if os.environ.get("PRISM_CAPTURE_COVERAGE") else {}),
              "captured_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "request": {"method": method, "path": path, "body": body}, "response": payload}
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / f"{name}.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    return "captured"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=sorted(CAPTURES))
    args = ap.parse_args()
    base = os.environ.get("PRISM_API_BASE", "http://127.0.0.1:8800").rstrip("/")
    key = os.environ.get("PRISM_API_KEY") or sys.exit("set PRISM_API_KEY")
    for name in [args.only] if args.only else CAPTURES:
        print(f"{name}: {capture(base, key, name)}")


if __name__ == "__main__":
    main()
