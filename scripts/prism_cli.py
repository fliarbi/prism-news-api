#!/usr/bin/env python3
"""prism-news / prism-business-news: command-line client for the Prism News APIs.

Identical in both API repositories; the command name picks the API. Standard
library only (Python 3.8+). One API key works on both APIs.

    prism-news login                       # save API base URL(s) and key (owner-only file)
    prism-news headlines "electric vehicle" --since 2026-01-01 --until 2026-04-30 --limit 20
    prism-news trends "tariffs" --granularity monthly --table
    prism-business-news funding --sector fintech --sort amount --limit 10 --table
    prism-business-news company tesla.com --since 2026-01-01
    prism-news call POST /v1/compare '{"queries": [...]}'

Any `--name value` becomes a request field (`--priority-min 7` -> priority_min=7);
repeat an option for a list (`--sentiment negative --sentiment neutral`).
Environment overrides: PRISM_API_KEY, PRISM_API_BASE, PRISM_BUSINESS_API_BASE.
"""
from __future__ import annotations

import getpass
import json
import os
import stat
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

VERSION = "1.0.0"
CONFIG = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "prism" / "config.json"
FREE = {"me", "status", "vocabulary"}

# command -> (method, path); "{arg}" takes the positional argument.
NEWS = {
    "overview": ("POST", "/v1/overview"), "headlines": ("POST", "/v1/headlines"), "themes": ("POST", "/v1/themes"),
    "theme-headlines": ("GET", "/v1/themes/{arg}/headlines"), "sentiment": ("POST", "/v1/sentiment"),
    "priority": ("POST", "/v1/priority"), "trends": ("POST", "/v1/trends"), "geography": ("POST", "/v1/geography"),
    "coverage": ("POST", "/v1/coverage"), "compare": ("POST", "/v1/compare"), "export": ("POST", "/v1/export"),
    "article": ("GET", "/v1/articles/{arg}"), "related": ("GET", "/v1/articles/{arg}/related"),
    "classes": ("GET", "/v1/classes"), "class": ("GET", "/v1/classes/{arg}"),
    "class-headlines": ("GET", "/v1/classes/{arg}/headlines"),
    "me": ("GET", "/v1/me"), "status": ("GET", "/v1/status"), "vocabulary": ("GET", "/v1/vocabulary"),
}
BUSINESS = {
    "overview": ("POST", "/v1/business/overview"), "headlines": ("POST", "/v1/business/headlines"),
    "themes": ("POST", "/v1/business/themes"), "sentiment": ("POST", "/v1/business/sentiment"),
    "trends": ("POST", "/v1/business/trends"), "events": ("POST", "/v1/business/events"),
    "event-trends": ("POST", "/v1/business/event-trends"), "funding": ("POST", "/v1/business/funding"),
    "funding-summary": ("POST", "/v1/business/funding/summary"),
    "company": ("GET", "/v1/business/companies/{arg}/news"), "export": ("POST", "/v1/export"),
    "article": ("GET", "/v1/articles/{arg}"), "classes": ("GET", "/v1/classes"),
    "me": ("GET", "/v1/me"), "status": ("GET", "/v1/status"), "vocabulary": ("GET", "/v1/vocabulary"),
}
PRODUCTS = {"prism-news": ("news", NEWS, "PRISM_API_BASE"),
            "prism-business-news": ("business", BUSINESS, "PRISM_BUSINESS_API_BASE")}


def die(msg: str, code: int = 1) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def load_config() -> dict:
    try:
        return json.loads(CONFIG.read_text())
    except (OSError, ValueError):
        return {}


def save_config(cfg: dict) -> None:
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    os.chmod(CONFIG.parent, stat.S_IRWXU)
    fd = os.open(CONFIG, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(cfg, f, indent=1)
    os.chmod(CONFIG, 0o600)


def settings(product: str, env_base: str) -> tuple[str, str]:
    cfg = load_config()
    base = os.environ.get(env_base) or cfg.get(f"{product}_base") or ""
    key = os.environ.get("PRISM_API_KEY") or cfg.get("key") or ""
    if not base or not key:
        die(f"Not configured. Run `{prog()} login`, or set {env_base} and PRISM_API_KEY.")
    return base.rstrip("/"), key


def prog() -> str:
    return os.environ.get("PRISM_CLI_PRODUCT") or Path(sys.argv[0]).name


def request(base: str, key: str, method: str, path: str, body: dict, raw: bool = False):
    url, data = base + path, None
    if method == "GET":
        if body:
            url += "?" + urllib.parse.urlencode({k: (",".join(map(str, v)) if isinstance(v, list) else v)
                                                 for k, v in body.items()})
    else:
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method, headers={
        "X-API-Key": key, "Content-Type": "application/json", "User-Agent": f"prism-cli/{VERSION}"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            payload = r.read()
            status = r.status
    except urllib.error.HTTPError as e:
        payload, status = e.read(), e.code
    except urllib.error.URLError as e:
        die(f"Cannot reach {base}: {e.reason}")
    if raw:
        return status, payload
    try:
        return status, json.loads(payload or b"{}")
    except ValueError:
        return status, {"ok": False, "error": {"kind": "not_json", "reason": payload[:200].decode(errors="replace")}}


def value(v: str):
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    for cast in (int, float):
        try:
            return cast(v)
        except ValueError:
            pass
    return v


def parse(argv: list[str]) -> tuple[list[str], dict, dict]:
    """Positional words, request fields and client flags (--table, -o FILE, --json BODY)."""
    pos, fields, flags = [], {}, {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--table", "--raw"):
            flags[a[2:]] = True
        elif a in ("-o", "--output", "--json"):
            if i + 1 >= len(argv):
                die(f"{a} needs a value", 2)
            flags["output" if a != "--json" else "json"] = argv[i + 1]
            i += 1
        elif a.startswith("--"):
            name, _, inline = a[2:].partition("=")
            if not inline:
                if i + 1 >= len(argv):
                    die(f"--{name} needs a value", 2)
                inline = argv[i + 1]
                i += 1
            name = name.replace("-", "_")
            v = value(inline)
            fields[name] = (fields[name] if isinstance(fields[name], list) else [fields[name]]) + [v] if name in fields else v
        else:
            pos.append(a)
        i += 1
    return pos, fields, flags


def table(payload: dict) -> str:
    data = payload.get("data") or {}
    items = (data.get("items") or data.get("points") or data.get("labels") or data.get("groups")
             or (data.get("headlines") or {}).get("items") or [])
    if not items:
        return json.dumps(payload, indent=1, ensure_ascii=False)
    keys = [k for k in items[0] if not isinstance(items[0][k], (list, dict))][:7]
    rows = [[str(it.get(k, ""))[:70] for k in keys] for it in items]
    width = [max(len(k), *(len(r[j]) for r in rows)) for j, k in enumerate(keys)]
    line = lambda cells: "  ".join(c.ljust(w) for c, w in zip(cells, width))  # noqa: E731
    out = [line(keys), line(["-" * w for w in width])] + [line(r) for r in rows]
    if data.get("next_cursor"):
        out.append(f"\nmore results: add --cursor {data['next_cursor']}")
    return "\n".join(out)


def login(product: str, env_base: str) -> None:
    cfg = load_config()
    print("Prism API login. The key is stored owner-only in", CONFIG)
    for name, label in (("news", "News API base URL"), ("business", "Business News API base URL")):
        current = cfg.get(f"{name}_base", "")
        entered = input(f"{label}{f' [{current}]' if current else ''}: ").strip()
        if entered:
            cfg[f"{name}_base"] = entered.rstrip("/")
    key = getpass.getpass("API key (input hidden; leave empty to keep the saved key): ").strip()
    if key:
        cfg["key"] = key
    if not cfg.get("key") or not cfg.get(f"{product}_base"):
        die("A key and the base URL for this API are required.")
    status, payload = request(cfg[f"{product}_base"], cfg["key"], "GET", "/v1/me", {})
    if status != 200:
        die(f"Check failed: HTTP {status} {(payload.get('error') or {}).get('kind')}. Nothing was saved.")
    save_config(cfg)
    plan = ((payload.get("data") or {}).get("plan") or {})
    print(f"Saved. Plan: {plan.get('label') or plan.get('name') or 'unknown'}. Try: {prog()} status")


def usage(commands: dict) -> str:
    names = ", ".join(sorted(commands))
    return (f"{prog()} {VERSION}\nusage: {prog()} COMMAND [QUERY|ID] [--field value ...] [--table] [-o FILE]\n"
            f"       {prog()} login | logout | call METHOD PATH [JSON]\ncommands: {names}\n"
            f"Example: {prog()} headlines \"electric vehicle\" --since 2026-01-01 --until 2026-04-30 --limit 20 --table")


def main(argv: list[str]) -> None:
    name = prog()
    product, commands, env_base = PRODUCTS.get(name, PRODUCTS["prism-news"])
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(usage(commands))
        return
    if argv[0] in ("-V", "--version"):
        print(VERSION)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "login":
        return login(product, env_base)
    if cmd == "logout":
        cfg = load_config()
        cfg.pop("key", None)
        save_config(cfg)
        print("Key removed from", CONFIG)
        return
    pos, fields, flags = parse(rest)
    if cmd == "call":
        if len(pos) < 2:
            die("usage: call METHOD PATH [JSON]", 2)
        method, path = pos[0].upper(), pos[1]
        body = {**(json.loads(pos[2]) if len(pos) > 2 else {}), **fields}
    elif cmd in commands:
        method, path = commands[cmd]
        if "{arg}" in path:
            if not pos:
                die(f"{cmd} needs an argument", 2)
            path = path.replace("{arg}", urllib.parse.quote(pos.pop(0), safe=""))
        body = {**(json.loads(flags["json"]) if "json" in flags else {}), **fields}
        if pos:
            body.setdefault("q", " ".join(pos))
        if cmd == "export" and flags.get("output"):
            body.setdefault("format", Path(flags["output"]).suffix.lstrip(".") if Path(flags["output"]).suffix in (".csv", ".ndjson", ".json") else "json")
    else:
        die(f"Unknown command {cmd!r}.\n" + usage(commands), 2)
    base, key = settings(product, env_base)
    if flags.get("output"):
        status, raw = request(base, key, method, path, body, raw=True)
        Path(flags["output"]).write_bytes(raw)
        print(f"HTTP {status}: wrote {len(raw):,} bytes to {flags['output']}", file=sys.stderr)
        sys.exit(0 if status == 200 else 1)
    status, payload = request(base, key, method, path, body)
    print(table(payload) if flags.get("table") and status == 200 else json.dumps(payload, indent=1, ensure_ascii=False))
    if status != 200 or not payload.get("ok", True):
        sys.exit(1)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(130)
