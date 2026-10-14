#!/usr/bin/env python3
"""Regenerate prism_news_api/data/gcp_classes.json from the pipeline's own
code map in Redis (PRISM_CLASSES_REDIS_HOST/PORT, db 3, keys classification_to_int_code:*).

    key   = "classification_to_int_code:___News___Business News___Company News"
    value = "0"
    label = "/" + key.split(":", 1)[1].replace("___", "/").lstrip("/")
          = "/News/Business News/Company News"

Read-only against Redis; writes only the JSON file in this repo. Prints a
diff summary against the current file and exits 0 when nothing changed.
"""
from __future__ import annotations

import os
import argparse
import json
import sys
from pathlib import Path

import redis

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "prism_news_api" / "data" / "gcp_classes.json"


def fetch(host: str, port: int, db: int) -> dict[int, str]:
    r = redis.Redis(host=host, port=port, db=db, socket_timeout=10, decode_responses=True)
    out: dict[int, str] = {}
    for key in r.scan_iter("classification_to_int_code:*", count=500):
        label = "/" + key.split(":", 1)[1].replace("___", "/").lstrip("/")
        code = int(r.get(key))
        if code in out and out[code] != label:
            print(f"WARNING: code {code} maps to both {out[code]!r} and {label!r}", file=sys.stderr)
        out[code] = label
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default=os.environ.get("PRISM_CLASSES_REDIS_HOST", "localhost"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("PRISM_CLASSES_REDIS_PORT", "6379")))
    ap.add_argument("--db", type=int, default=3)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--check", action="store_true", help="only report differences; do not write")
    a = ap.parse_args()

    fresh = fetch(a.host, a.port, a.db)
    if not fresh:
        print("no classification_to_int_code:* keys found — refusing to write an empty map", file=sys.stderr)
        return 2
    out = Path(a.out)
    old: dict[int, str] = {}
    if out.exists():
        old = {int(k): v for k, v in json.loads(out.read_text()).items()}
    added = sorted(set(fresh) - set(old))
    removed = sorted(set(old) - set(fresh))
    changed = sorted(k for k in set(fresh) & set(old) if fresh[k] != old[k])
    print(f"redis: {len(fresh)} classes; file: {len(old)}; added {len(added)}, removed {len(removed)}, relabelled {len(changed)}")
    for k in added[:10]:
        print(f"  + {k}: {fresh[k]}")
    for k in removed[:10]:
        print(f"  - {k}: {old[k]}")
    for k in changed[:10]:
        print(f"  ~ {k}: {old[k]!r} -> {fresh[k]!r}")
    if not (added or removed or changed):
        print("no change")
        return 0
    if a.check:
        return 1
    out.write_text(json.dumps({str(k): fresh[k] for k in sorted(fresh)}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
