"""Pay-as-you-go: once an account's monthly plan allowance is used, requests and
full-text articles draw prepaid credits from the Fliar API wallet that the Radar API
gateway keeps (one wallet for the Radar API and Prism News, one credit each).

Credits are reserved before the work and settled after it; anything not settled is
refunded by the gateway after ten minutes. The gateway's private credit endpoints
are reached the same way as its key check (local address + shared secret).
"""
from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request

from . import config
from .envelope import ApiError

log = logging.getLogger("prism_news_api.payg")


def enabled() -> bool:
    return bool(config.RADAR_KEYS_URL and config.RADAR_KEYS_SECRET)


def _post(path: str, body: dict) -> tuple[int, dict]:
    headers = {"Content-Type": "application/json", "X-Introspect-Secret": config.RADAR_KEYS_SECRET}
    if config.RADAR_KEYS_HOST:
        headers["Host"] = config.RADAR_KEYS_HOST
    req = urllib.request.Request(config.RADAR_KEYS_URL + path, method="POST",
                                 data=json.dumps(body).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b"{}")
        except ValueError:
            return e.code, {}
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        log.error("credit service unavailable: %s", type(e).__name__)
        return 599, {}


def reserve(user_id: str, feature: str, units: int, refused: ApiError) -> str:
    """Reserve `units` prepaid credits or raise `refused` (the plan's quota error),
    extended with how to continue on pay-as-you-go."""
    if not enabled():
        raise refused
    status, body = _post("/internal/credits/reserve", {"account_id": user_id, "feature": feature[:80],
                                                       "units": int(units)})
    rid = (body.get("data") or {}).get("request_id") if status == 200 and body.get("ok") else None
    if rid:
        return rid
    if status == 599:
        raise ApiError("upstream", "the credit service did not answer; try again shortly")
    refused.reason = (refused.reason.rstrip(".") + f". To continue pay-as-you-go, add prepaid credits and a "
                      f"monthly spending limit at {config.KEYS_URL} (1 credit per request or full-text article).")
    raise refused


def settle(request_id: str | None, actual: int) -> None:
    """Charge `actual` of the reserved credits and refund the rest. Best-effort:
    an unsettled reservation is refunded by the gateway."""
    if not request_id:
        return
    status, _ = _post("/internal/credits/settle", {"request_id": request_id, "actual": max(0, int(actual))})
    if status != 200:
        log.error("credit settlement %s failed (HTTP %s)", request_id, status)
