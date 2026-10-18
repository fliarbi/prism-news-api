"""A small, standard-library client for the Prism News API.

Every method returns the decoded JSON envelope ({"ok": true, "data": ..., "meta": ...}).
A non-2xx answer raises PrismAPIError with the HTTP status and the API's error kind.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional

from . import __version__

DEFAULT_BASE = "https://radar-api.fliarbi.com/news"
DEFAULT_BUSINESS_BASE = "https://radar-api.fliarbi.com/business-news"


class PrismAPIError(Exception):
    """Raised when the API answers with a non-2xx status."""

    def __init__(self, status: int, payload: Any):
        self.status = status
        self.payload = payload
        err = (payload or {}).get("error") if isinstance(payload, dict) else None
        self.kind = (err or {}).get("kind") if isinstance(err, dict) else None
        reason = (err or {}).get("reason") if isinstance(err, dict) else None
        super().__init__(f"HTTP {status}" + (f" {self.kind}" if self.kind else "") + (f": {reason}" if reason else ""))


class Client:
    """Prism News API client.

    Args:
        api_key: your key; defaults to the PRISM_API_KEY environment variable.
        base_url: defaults to PRISM_API_BASE or https://radar-api.fliarbi.com/news.
        business_base_url: defaults to PRISM_BUSINESS_API_BASE or .../business-news.
        timeout: seconds per request.
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None,
                 business_base_url: Optional[str] = None, timeout: float = 180.0):
        self.api_key = api_key if api_key is not None else os.environ.get("PRISM_API_KEY", "")
        self.base_url = (base_url or os.environ.get("PRISM_API_BASE") or DEFAULT_BASE).rstrip("/")
        self.business_base_url = (business_base_url or os.environ.get("PRISM_BUSINESS_API_BASE")
                                  or DEFAULT_BUSINESS_BASE).rstrip("/")
        self.timeout = timeout

    # -- transport -----------------------------------------------------------------
    def _url(self, path: str, business: bool) -> str:
        return (self.business_base_url if business else self.base_url) + path

    def request(self, method: str, path: str, body: Optional[Dict[str, Any]] = None,
                business: bool = False) -> Dict[str, Any]:
        """Send one request. GET bodies become query parameters."""
        if not self.api_key:
            raise PrismAPIError(401, {"error": {"kind": "no_key",
                                                "reason": "set PRISM_API_KEY or pass api_key="}})
        body = {k: v for k, v in (body or {}).items() if v is not None}
        url, data = self._url(path, business), None
        if method.upper() == "GET":
            if body:
                url += "?" + urllib.parse.urlencode(
                    {k: (",".join(map(str, v)) if isinstance(v, (list, tuple)) else v) for k, v in body.items()})
        else:
            data = json.dumps(body).encode()
        req = urllib.request.Request(url, data=data, method=method.upper(), headers={
            "X-API-Key": self.api_key, "Content-Type": "application/json",
            "User-Agent": f"prism-news-python/{__version__}"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                status, raw = r.status, r.read()
        except urllib.error.HTTPError as e:
            status, raw = e.code, e.read()
        try:
            payload = json.loads(raw or b"{}")
        except ValueError:
            payload = {"ok": False, "error": {"kind": "not_json", "reason": raw[:200].decode(errors="replace")}}
        if not 200 <= status < 300:
            raise PrismAPIError(status, payload)
        return payload

    def _post(self, path: str, q: Optional[str], fields: Dict[str, Any], business: bool = False):
        if q is not None:
            fields = {"q": q, **fields}
        return self.request("POST", path, fields, business)

    # -- free endpoints ------------------------------------------------------------
    def me(self):
        """Your plan, allowance and usage."""
        return self.request("GET", "/v1/me")

    def status(self):
        """Index coverage and shard availability."""
        return self.request("GET", "/v1/status")

    def vocabulary(self):
        """Accepted values for sentiment, priority and other fields."""
        return self.request("GET", "/v1/vocabulary")

    # -- news ------------------------------------------------------------------------
    def overview(self, q: str, **fields):
        return self._post("/v1/overview", q, fields)

    def headlines(self, q: str, **fields):
        """Headlines matching q. Common fields: since, until, limit, sentiment, priority_min, country, cursor."""
        return self._post("/v1/headlines", q, fields)

    def themes(self, q: str, **fields):
        return self._post("/v1/themes", q, fields)

    def theme_headlines(self, theme_id: str, **fields):
        return self.request("GET", f"/v1/themes/{urllib.parse.quote(str(theme_id), safe='')}/headlines", fields)

    def sentiment(self, q: str, **fields):
        return self._post("/v1/sentiment", q, fields)

    def priority(self, q: str, **fields):
        return self._post("/v1/priority", q, fields)

    def trends(self, q: str, **fields):
        """Time series of volume and tone. Field granularity: daily, weekly or monthly."""
        return self._post("/v1/trends", q, fields)

    def geography(self, q: str, **fields):
        return self._post("/v1/geography", q, fields)

    def coverage(self, q: str, **fields):
        return self._post("/v1/coverage", q, fields)

    def compare(self, queries, **filters):
        """Compare 2-5 queries on one scale.

        queries: strings (each becomes {"name": s, "filters": {"q": s}}) or {"name", "filters"} objects.
        Keyword filters (since, until, classes, sentiment, ...) are applied to every query.
        """
        common = {k: v for k, v in filters.items() if v is not None}
        items = []
        for q in queries:
            if isinstance(q, str):
                items.append({"name": q, "filters": {**common, "q": q}})
            else:
                items.append({"name": q["name"], "filters": {**common, **(q.get("filters") or {})}})
        return self.request("POST", "/v1/compare", {"queries": items})

    def export(self, q: str, **fields):
        return self._post("/v1/export", q, fields)

    def article(self, article_id: str):
        return self.request("GET", f"/v1/articles/{urllib.parse.quote(str(article_id), safe='')}")

    def related(self, article_id: str, **fields):
        return self.request("GET", f"/v1/articles/{urllib.parse.quote(str(article_id), safe='')}/related", fields)

    def classes(self):
        """GCP content-class codes."""
        return self.request("GET", "/v1/classes")

    def class_info(self, code: str):
        return self.request("GET", f"/v1/classes/{urllib.parse.quote(str(code), safe='')}")

    def class_headlines(self, code: str, **fields):
        return self.request("GET", f"/v1/classes/{urllib.parse.quote(str(code), safe='')}/headlines", fields)

    # -- business news -----------------------------------------------------------
    def business(self, endpoint: str, q: Optional[str] = None, **fields):
        """POST /v1/business/<endpoint> on the business API, e.g. business("funding", sector="fintech")."""
        return self._post(f"/v1/business/{endpoint.strip('/')}", q, fields, business=True)

    def company_news(self, domain: str, **fields):
        return self.request("GET", f"/v1/business/companies/{urllib.parse.quote(domain, safe='')}/news",
                            fields, business=True)
