"""me — GET /v1/me: the key, the plan, the limits, this month's usage. Unmetered."""
from __future__ import annotations

import time

from .. import config, envelope, quota
from ..auth import Principal


def me(p: Principal, rate: dict | None = None) -> dict:
    t0 = time.time()
    data = p.as_me()
    data["usage"] = quota.usage(p.user_id, p.key_id, p.plan_cfg, rate)
    data["upgrade_url"] = config.UPGRADE_URL
    data["metered_note"] = ("every authenticated call is metered except /v1/me, /v1/status, "
                            "/v1/classes*, /v1/vocabulary; exports are charged per article delivered")
    return envelope.ok("api.me", data, subject={"key": p.key_prefix},
                       meta={"seconds": round(time.time() - t0, 3), "notes": list(p.notes)})
