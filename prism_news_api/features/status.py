"""Service readiness and data dates for API consumers."""
from __future__ import annotations
import time
from .. import __version__, articles, ch, config, envelope, public
from ..auth import Principal


def status(p: Principal | None = None) -> dict:
    t0 = time.time()
    try:
        cov = ch.coverage()
        dt = ch.data_through()
        ready = bool(not cov.get("partial", True) and articles.health().get("available") and dt)
    except Exception:
        dt, ready = None, False
    data = {"service": "Prism News API", "version": __version__, "healthy": ready,
            "data_through": dt, "archive": public.archive(),
            "default_window_days": config.DEFAULT_WINDOW_DAYS,
            "freshness": config.FRESHNESS_NOTE, "location_coverage_note": config.COUNTRY_NOTE}
    return envelope.ok("api.status", data, window={"data_through": dt, "freshness": config.FRESHNESS_NOTE},
                       meta={"seconds": round(time.time() - t0, 3), "coverage": {"available": ready}})
