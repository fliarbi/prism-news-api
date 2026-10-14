#!/usr/bin/env python3
"""mint_test_key — DEV ONLY. Create (or revoke) an API key for a user by email.

Production keys are issued by the dashboard blueprint (radar :5100
/api_keys/create). This script exists so the API can be smoke-tested before
that ships. It writes exactly the document shape in docs/DESIGN.md §2 and
prints the key ONCE; only its SHA-256 is stored.

    python3 scripts/mint_test_key.py you@example.com --name "smoke test"
    python3 scripts/mint_test_key.py --revoke <key_id>
    python3 scripts/mint_test_key.py --list you@example.com

Also ensures the indexes from the design (api_keys.key_hash unique,
api_keys (user_id, status), api_usage_daily (user_id, day)) exist — idempotent.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import secrets
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pymongo  # noqa: E402
from bson import ObjectId  # noqa: E402

from prism_news_api import config  # noqa: E402


def db():
    return pymongo.MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)[config.AUTH_DB]


def ensure_indexes(d) -> None:
    d.api_keys.create_index("key_hash", unique=True, name="key_hash_unique")
    d.api_keys.create_index([("user_id", 1), ("status", 1)], name="user_status")
    d.api_usage_daily.create_index([("user_id", 1), ("day", 1)], name="user_day")


def mint(d, email: str, name: str) -> dict:
    user = d.users.find_one({"email": email.strip().lower()}, {"_id": 1, "email": 1})
    if not user:
        user = d.users.find_one({"email": email.strip()}, {"_id": 1, "email": 1})
    if not user:
        raise SystemExit(f"no users doc with email {email!r}")
    key = config.KEY_PREFIX + secrets.token_hex(20)
    assert len(key) == config.KEY_LENGTH
    now = dt.datetime.utcnow()
    doc = {"user_id": user["_id"], "product": config.PRODUCT, "name": name[:60],
           "key_hash": hashlib.sha256(key.encode()).hexdigest(),
           "prefix": key[:12], "last4": key[-4:], "status": "active",
           "created_at": now, "created_ip": None, "last_used_at": None,
           "revoked_at": None, "created_by": "scripts/mint_test_key.py"}
    res = d.api_keys.insert_one(doc)
    return {"key": key, "id": str(res.inserted_id), "prefix": doc["prefix"],
            "last4": doc["last4"], "user_id": str(user["_id"]), "email": user["email"]}


def revoke(d, key_id: str) -> bool:
    r = d.api_keys.update_one({"_id": ObjectId(key_id), "status": "active"},
                              {"$set": {"status": "revoked", "revoked_at": dt.datetime.utcnow()}})
    return r.modified_count == 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("email", nargs="?", help="users email to mint a key for")
    ap.add_argument("--name", default="dev key", help="key name (1..60 chars)")
    ap.add_argument("--revoke", metavar="KEY_ID", help="mark this api_keys _id revoked")
    ap.add_argument("--list", metavar="EMAIL", help="list keys for an email")
    a = ap.parse_args()
    d = db()
    ensure_indexes(d)
    if a.revoke:
        ok = revoke(d, a.revoke)
        print("revoked" if ok else "not found or already revoked")
        return 0 if ok else 1
    if a.list:
        u = d.users.find_one({"email": a.list}, {"_id": 1})
        if not u:
            print("no such user")
            return 1
        for k in d.api_keys.find({"user_id": u["_id"]}).sort("created_at", -1):
            print(f"{k['_id']}  {k['status']:8s}  {k['prefix']}…{k['last4']}  {k['name']!r}  "
                  f"created {k['created_at']:%Y-%m-%d %H:%M}  last_used {k.get('last_used_at')}")
        return 0
    if not a.email:
        ap.error("email is required (or --revoke / --list)")
    out = mint(d, a.email, a.name)
    print("API key (shown ONCE, not stored):", out["key"])
    print(f"id={out['id']} prefix={out['prefix']} last4={out['last4']} user={out['email']} ({out['user_id']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
