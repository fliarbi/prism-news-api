#!/usr/bin/env python3
"""smoke_test — hit EVERY endpoint of a running prism-news-api with a real key.

    python3 smoke_test.py --key pna_…  [--base http://127.0.0.1:8800] [--samples] [--hammer]

Asserts, per call: the HTTP status is the expected one, the body is the
envelope (ok/feature/subject/data/window/meta[/error]), `ok` agrees with the
status, and every authenticated response carries the five quota headers.
Prints a table and exits non-zero on any failure. `--samples` prints trimmed
payloads for the headline queries and the export; `--hammer` fires /v1/me
until a 429 appears and prints that envelope.

A 429 met during the run (the free tier allows 30 calls/minute and this
script makes ~35) is handled the way a client should: sleep Retry-After and
retry once. It is reported in the table, not counted as a failure.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# must match prism_news_api/features/export.py CSV_COLUMNS
CSV_COLUMNS = ("id", "headline", "url", "publisher", "published_at", "sentiment",
               "priority", "classes", "body")

ENVELOPE_KEYS = {"ok", "feature", "subject", "data", "window", "meta"}
QUOTA_HEADERS = ("x-ratelimit-limit", "x-ratelimit-remaining", "x-quota-requests-remaining",
                 "x-quota-exports-remaining", "x-plan")


class Result:
    def __init__(self, status, headers, text, ms):
        # uvicorn emits lowercase header names; compare case-insensitively
        self.status, self.text, self.ms = status, text, ms
        self.headers = {k.lower(): v for k, v in dict(headers).items()}
        try:
            self.json = json.loads(text) if text and text.lstrip().startswith("{") else None
        except Exception:
            self.json = None


def call(base, method, path, params=None, body=None, headers=None, timeout=90) -> Result:
    url = base.rstrip("/") + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    if data is not None:
        req.add_header("Content-Type", "application/json")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return Result(r.status, dict(r.headers), r.read().decode("utf-8", "replace"), (time.time() - t0) * 1000)
    except urllib.error.HTTPError as e:
        return Result(e.code, dict(e.headers), e.read().decode("utf-8", "replace"), (time.time() - t0) * 1000)


def trim(o, depth=0):
    """Shorten long strings/lists for printing."""
    if isinstance(o, dict):
        return {k: trim(v, depth + 1) for k, v in list(o.items())[:40]}
    if isinstance(o, list):
        return [trim(x, depth + 1) for x in o[:3]] + ([f"… +{len(o) - 3} more"] if len(o) > 3 else [])
    if isinstance(o, str) and len(o) > 140:
        return o[:140] + f"… ({len(o)} chars)"
    return o


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=os.environ.get("PRISM_API_BASE", "http://127.0.0.1:8800"))
    ap.add_argument("--key", default=os.environ.get("PRISM_API_KEY"))
    ap.add_argument("--samples", action="store_true", help="print trimmed sample payloads")
    ap.add_argument("--hammer", action="store_true", help="hit /v1/me until a 429 and print it")
    ap.add_argument("--q", default="electric vehicle")
    a = ap.parse_args()
    if not a.key:
        print("need --key or PRISM_API_KEY", file=sys.stderr)
        return 2
    H = {"X-API-Key": a.key}
    B = {"Authorization": f"Bearer {a.key}"}
    rows, samples, failures = [], {}, 0
    ctx: dict = {}

    def run(name, method, path, params=None, body=None, headers=None, expect=(200,),
            kind=None, check=None, authed=True, sample=False, envelope=True):
        nonlocal failures
        r = call(a.base, method, path, params, body, headers)
        note = ""
        if r.status == 429 and 429 not in expect:
            wait = int(r.headers.get("retry-after", "5"))
            note = f"429 met, slept {wait}s; "
            time.sleep(wait + 0.5)
            r = call(a.base, method, path, params, body, headers)
        ok = r.status in expect
        is_json = r.json is not None
        if is_json and envelope:
            if not ENVELOPE_KEYS <= set(r.json):
                ok, note = False, note + "not an envelope; "
            elif r.json["ok"] != (200 <= r.status < 300):
                ok, note = False, note + "ok/status disagree; "
            if kind and (r.json.get("error") or {}).get("kind") != kind:
                ok, note = False, note + f"kind={((r.json.get('error') or {}).get('kind'))}; "
        elif not is_json and r.status < 400 and "text/csv" not in r.headers.get("content-type", "") \
                and "ndjson" not in r.headers.get("content-type", ""):
            ok, note = False, note + "non-JSON body; "
        if authed and r.status not in (401,):
            missing = [h for h in QUOTA_HEADERS if h not in r.headers]
            if missing:
                ok, note = False, note + f"missing headers {missing}; "
        if ok and check:
            try:
                msg = check(r)
                if msg:
                    note += msg
            except AssertionError as e:
                ok, note = False, note + f"check failed: {e}; "
            except Exception as e:
                ok, note = False, note + f"check error: {type(e).__name__}: {e}; "
        if not ok:
            failures += 1
        rows.append((name, f"{method} {path}", r.status, "/".join(map(str, expect)), f"{r.ms:.0f}",
                     "PASS" if ok else "FAIL", note.strip()))
        if sample and r.json:
            samples[name] = r.json
        return r

    # ── no key / bad key ─────────────────────────────────────────────────────
    run("healthz", "GET", "/healthz", authed=False, envelope=False,
        check=lambda r: f"data_through={r.json.get('data_through')}" if r.json else None)
    run("openapi", "GET", "/v1/openapi.json", authed=False, envelope=False,
        check=lambda r: (lambda s: f"{len(s['paths'])} paths")(json.loads(r.text)))
    run("no key → 401", "GET", "/v1/headlines", expect=(401,), kind="unauthenticated", authed=False)
    run("bad key → 401", "GET", "/v1/headlines", headers={"X-API-Key": "pna_" + "0" * 40},
        expect=(401,), kind="invalid_key", authed=False)
    run("revoked-format key → 401", "GET", "/v1/me", headers={"X-API-Key": "nope"},
        expect=(401,), kind="invalid_key", authed=False)

    # ── unmetered ────────────────────────────────────────────────────────────
    run("me (Bearer)", "GET", "/v1/me", headers=B,
        check=lambda r: f"plan={r.json['data']['plan']['name']} used={r.json['data']['usage']['requests']['used']}")
    run("status", "GET", "/v1/status", headers=H,
        check=lambda r: f"healthy={r.json['data']['healthy']} archive={r.json['data']['archive']['article_count_display']}")
    run("vocabulary", "GET", "/v1/vocabulary", headers=H,
        check=lambda r: f"{len(r.json['data']['sentiments'])} sentiments, {r.json['data']['class_count']} classes")
    run("classes?q=venture", "GET", "/v1/classes", {"q": "venture"}, headers=H,
        check=lambda r: f"{r.json['data']['returned']} hits; code 55 present={any(i['code'] == 55 for i in r.json['data']['items'])}")
    run("classes/0", "GET", "/v1/classes/0", headers=H,
        check=lambda r: f"articles_30d={r.json['data']['articles_30d']}")
    run("classes/55", "GET", "/v1/classes/55", headers=H,
        check=lambda r: r.json["data"]["path"])
    run("classes/999999 → 400", "GET", "/v1/classes/999999", headers=H, expect=(400,), kind="bad_request")

    # ── headlines ────────────────────────────────────────────────────────────
    def hl_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "no items"
        it = d["items"][0]
        for k in ("id", "headline", "url", "publisher", "published_at", "lede", "sentiment", "priority",
                  "classes", "country", "organizations", "people"):
            assert k in it, f"item lacks {k}"
        ctx.setdefault("ids", []).extend(i["id"] for i in d["items"])
        ctx["cursor"] = d.get("next_cursor")
        ctx["lede_len"] = len(it["lede"] or "")
        return f"{d['returned']} items / {d['total_estimate']:,} total; cursor={'yes' if d.get('next_cursor') else 'no'}"

    run("headlines q", "GET", "/v1/headlines", {"q": a.q, "limit": 5}, headers=H, check=hl_check, sample=True)
    run("headlines page 2 (cursor)", "GET", "/v1/headlines", {"q": a.q, "limit": 5, "cursor": ctx.get("cursor")},
        headers=H, check=lambda r: (lambda ids: (
            f"{len(ids)} items, disjoint={not (set(ids) & set(ctx['ids'][:5]))}"
        ))([i["id"] for i in r.json["data"]["items"]]))
    run("headlines classes=0 neg p>=7", "GET", "/v1/headlines",
        {"classes": 0, "sentiment": "negative", "priority_min": 7, "limit": 5}, headers=H,
        check=lambda r: (hl_check(r) + "; all p>=7 & neg=" + str(all(
            i["priority"] >= 7 and i["sentiment"]["group"] == "negative" for i in r.json["data"]["items"]))),
        sample=True)
    run("headlines POST body", "POST", "/v1/headlines", body={"q": a.q, "sentiment": ["positive"], "limit": 3},
        headers=H, check=lambda r: f"{r.json['data']['returned']} items; sentiment={r.json['subject']['filters'].get('sentiment')}")
    run("headlines sort=priority", "GET", "/v1/headlines", {"q": a.q, "sort": "priority", "limit": 3}, headers=H,
        check=lambda r: "priorities=" + str([i["priority"] for i in r.json["data"]["items"]]))
    run("headlines q too short → 400", "GET", "/v1/headlines", {"q": "a"}, headers=H, expect=(400,), kind="bad_request")
    run("headlines unknown class → 400", "GET", "/v1/headlines", {"classes": "0,999999"}, headers=H,
        expect=(400,), kind="bad_request")
    run("headlines limit=5000 → clamped", "GET", "/v1/headlines", {"q": a.q, "limit": 5000}, headers=H,
        check=lambda r: f"limit={r.json['data']['limit']}; note={'clamped' in ' '.join(r.json['meta']['notes'])}")
    run("headlines since=2020 → clamped", "GET", "/v1/headlines", {"q": a.q, "since": "2020-01-01", "limit": 2},
        headers=H, check=lambda r: f"since={r.json['window']['since']}; note={'history_days' in ' '.join(r.json['meta']['notes'])}")
    run("headlines nonsense q → 404", "GET", "/v1/headlines", {"q": "zzqqxxjjkkvv"}, headers=H,
        expect=(404,), kind="no_data")

    # ── themes → pick a real one ─────────────────────────────────────────────
    def themes_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "no themes"
        it = d["items"][0]
        for k in ("theme", "count", "share", "lift", "previous_period_count", "delta_pct"):
            assert k in it, f"theme row lacks {k}"
        ctx["theme"] = it["theme"]
        return f"top={it['theme']!r} n={it['count']} lift={it['lift']} prev={it['previous_period_count']}"
    run("themes class_prefix=/Finance", "GET", "/v1/themes", {"q": "investment", "class_prefix": "/Finance", "limit": 5},
        headers=H, check=themes_check, sample=True)
    theme = ctx.get("theme") or "quarterly and annual financial results"
    run("headlines /Finance + theme", "GET", "/v1/headlines",
        {"class_prefix": "/Finance", "themes": theme, "limit": 5}, headers=H, check=hl_check, sample=True)
    run("themes/{name}/headlines", "GET", f"/v1/themes/{urllib.parse.quote(theme)}/headlines", {"limit": 3},
        headers=H, check=lambda r: f"{r.json['data']['returned']} items; feature={r.json['feature']}")
    run("classes/0/headlines", "GET", "/v1/classes/0/headlines", {"limit": 3}, headers=H,
        check=lambda r: f"{r.json['data']['returned']} items; feature={r.json['feature']}")

    # ── distributions ────────────────────────────────────────────────────────
    run("sentiment weekly", "GET", "/v1/sentiment", {"q": a.q, "granularity": "weekly"}, headers=H,
        check=lambda r: f"carrying={r.json['data']['carrying']} ratio={r.json['data']['negative_to_positive_ratio']} "
                        f"vs_base={r.json['data']['vs_baseline_ratio']} pts={len(r.json['data']['timeline'])}", sample=True)
    run("priority", "GET", "/v1/priority", {"q": a.q}, headers=H,
        check=lambda r: f"critical={r.json['data']['critical']['share']}% vs_base={r.json['data']['vs_baseline_critical']}", sample=True)
    run("trends weekly", "GET", "/v1/trends", {"q": a.q, "granularity": "weekly"}, headers=H,
        check=lambda r: f"total={r.json['data']['total']} pts={len(r.json['data']['points'])} peak={r.json['data']['peak']}", sample=True)
    run("trends hourly → 400", "GET", "/v1/trends", {"granularity": "hourly"}, headers=H, expect=(400,), kind="bad_request")

    # ── article + export ─────────────────────────────────────────────────────
    aid = (ctx.get("ids") or ["000000000000000000000000"])[0]

    def art_check(r):
        art = r.json["data"]["article"]
        assert art.get("body"), "no body"
        assert art["body_chars"] > ctx.get("lede_len", 0), f"body {art['body_chars']} not longer than lede"
        return f"body_chars={art['body_chars']} > lede {ctx.get('lede_len')}; authors={len(art['authors'])}; exports_remaining={r.headers.get('x-quota-exports-remaining')}"
    run("articles/{id}", "GET", f"/v1/articles/{aid}", headers=H, check=art_check, sample=True)
    run("articles/bad → 400", "GET", "/v1/articles/not-an-id", headers=H, expect=(400,), kind="bad_request")
    run("articles/unknown → 404", "GET", "/v1/articles/000000000000000000000000", headers=H, expect=(404,), kind="no_data")

    def exp_json_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "nothing exported"
        short = [i["id"] for i in d["items"] if (i.get("body_chars") or 0) <= len(i.get("lede") or "")]
        assert not short, f"bodies not longer than lede for {short}"
        return f"{d['returned']} delivered, charged={d['charged_exports']}, min body={min(i['body_chars'] for i in d['items'])} chars"
    run("export json x5", "POST", "/v1/export", body={"q": a.q, "limit": 5, "format": "json"}, headers=H,
        check=exp_json_check, sample=True)

    def exp_csv_check(r):
        rows_ = list(csv.reader(io.StringIO(r.text)))
        assert rows_[0] == list(CSV_COLUMNS), f"header {rows_[0]}"
        assert len(rows_) - 1 >= 1, "no rows"
        body = CSV_COLUMNS.index("body")
        assert all(len(x[body]) > 300 for x in rows_[1:]), "a body is short"
        samples["export csv x5"] = {"header": rows_[0], "rows": len(rows_) - 1,
                                    "first_row_trimmed": [c[:60] for c in rows_[1]]}
        return f"{len(rows_) - 1} rows; delivered header={r.headers.get('x-export-delivered')}"
    run("export csv x5", "POST", "/v1/export", body={"q": a.q, "limit": 5, "format": "csv"}, headers=H, check=exp_csv_check)

    def exp_nd_check(r):
        lines = [l for l in r.text.split("\n") if l]
        first = json.loads(lines[0])
        assert first["ok"] and first["data"]["stream"] is True, "first line not a stream envelope"
        assert len(lines) - 1 == first["data"]["returned"], "line count != returned"
        return f"{len(lines) - 1} article lines"
    run("export ndjson x2", "POST", "/v1/export", body={"q": a.q, "limit": 2, "format": "ndjson"}, headers=H, check=exp_nd_check)
    run("export xml → 400", "POST", "/v1/export", body={"format": "xml"}, headers=H, expect=(400,), kind="bad_request")
    # An unknown path resolves no principal, so the 404 envelope carries no
    # quota headers by design (DESIGN.md §8); authed=False skips that check.
    run("unknown route → 404", "GET", "/v1/nothing", headers=H, expect=(404,), kind="no_data", authed=False)

    # ── table ────────────────────────────────────────────────────────────────
    w = [max(len(str(r[i])) for r in rows + [("case", "call", "status", "expect", "ms", "result", "note")]) for i in range(7)]
    fmt = "  ".join("{:<%d}" % x for x in w)
    print(fmt.format("case", "call", "status", "expect", "ms", "result", "note"))
    print("-" * (sum(w) + 12))
    for r in rows:
        print(fmt.format(*[str(x) for x in r]))
    print(f"\n{len(rows) - failures}/{len(rows)} passed")

    if a.samples:
        print("\n=== samples (trimmed) ===")
        for k, v in samples.items():
            print(f"\n--- {k}")
            print(json.dumps(trim(v), indent=1, ensure_ascii=False, default=str))

    if a.hammer:
        print("\n=== hammering /v1/me until 429 ===")
        for i in range(200):
            r = call(a.base, "GET", "/v1/me", headers=H)
            if r.status == 429:
                print(f"429 after {i + 1} calls; Retry-After={r.headers.get('retry-after')} "
                      f"X-RateLimit-Remaining={r.headers.get('x-ratelimit-remaining')}")
                print(json.dumps(r.json, indent=1))
                break
        else:
            print("no 429 in 200 calls")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
