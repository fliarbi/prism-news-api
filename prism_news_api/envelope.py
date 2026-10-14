"""envelope — one response shape for every path, including failures.

Identical to prism-mcp's envelope so the two surfaces interoperate:

    {
      "ok": true,
      "feature": "news.headlines",
      "subject": {"filters": {...}},
      "data": {...},
      "window": {"since": ..., "until": ..., "data_through": ..., "freshness": ...},
      "meta": {"seconds": 0.4, "coverage": {...}, "quota": {...}, "plan": "free", "notes": []},
      "error": {"kind": "...", "reason": "..."}      # only when ok is false
    }

`error.kind` is a closed set and maps to the HTTP status. The body is ALWAYS
the envelope — a client never parses two shapes.
"""
from __future__ import annotations

# kind -> HTTP status
KINDS: dict[str, int] = {
    "bad_request": 400,
    "unauthenticated": 401,
    "invalid_key": 401,
    "quota_exceeded": 402,
    "rate_limited": 429,
    "no_data": 404,
    "upstream": 502,
    "coverage_unavailable": 503,
    "internal": 500,
}


def ok(feature: str, data, subject=None, window=None, meta=None) -> dict:
    return {"ok": True, "feature": feature, "subject": subject or {},
            "data": data, "window": window or {}, "meta": meta or {}}


def fail(feature: str, reason: str, kind: str = "internal", subject=None,
         window=None, meta=None, **error_fields) -> dict:
    kind = kind if kind in KINDS else "internal"
    err = {"kind": kind, "reason": reason}
    err.update({k: v for k, v in error_fields.items() if v is not None})
    return {"ok": False, "feature": feature, "subject": subject or {},
            "data": None, "window": window or {}, "meta": meta or {},
            "error": err}


def status_of(env: dict) -> int:
    if env.get("ok"):
        return 200
    return KINDS.get(((env.get("error") or {}).get("kind")), 500)


def list_data(items: list, total_estimate=None, next_cursor=None, **extra) -> dict:
    """The list payload shape: data.items, data.returned, data.total_estimate,
    data.next_cursor (+ anything feature-specific)."""
    d = {"items": items, "returned": len(items),
         "total_estimate": total_estimate, "next_cursor": next_cursor}
    d.update(extra)
    return d


class ApiError(Exception):
    """Raised anywhere in the request path; the router renders it as an
    envelope with the kind's HTTP status. `fields` land inside `error`
    (e.g. upgrade_url), `headers` on the response (e.g. Retry-After)."""

    def __init__(self, kind: str, reason: str, *, fields: dict | None = None,
                 headers: dict | None = None, meta: dict | None = None):
        super().__init__(reason)
        self.kind = kind if kind in KINDS else "internal"
        self.reason = reason
        self.fields = fields or {}
        self.headers = headers or {}
        self.meta = meta or {}

    @property
    def status(self) -> int:
        return KINDS[self.kind]

    def envelope(self, feature: str, subject=None, window=None, meta=None) -> dict:
        m = dict(self.meta)
        m.update(meta or {})
        return fail(feature, self.reason, kind=self.kind, subject=subject,
                    window=window, meta=m, **self.fields)
