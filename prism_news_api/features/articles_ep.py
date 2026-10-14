"""articles_ep — GET /v1/articles/{id}: one full article, charged as 1 export.

Reserve 1 -> fetch the signal row (ClickHouse, by target_id) and the record
(article store) in parallel -> deliver -> refund if nothing was delivered.
`target_id` is not in the table's sort key, so the CH lookup is a scan
(~0.4 s measured); acceptable for a single-article fetch."""
from __future__ import annotations

import re
import time
from concurrent.futures import ThreadPoolExecutor

from .. import articles, ch, envelope, quota
from datetime import date, timedelta
from ..auth import Principal
from ..envelope import ApiError
from . import _common as c

FEATURE = "news.article"
_ID_RE = re.compile(r"^[0-9a-fA-F]{24}$")


def article(p: Principal, article_id: str, endpoint: str = "/v1/articles/{id}") -> dict:
    t0 = time.time()
    aid = (article_id or "").strip()
    if not _ID_RE.match(aid):
        raise ApiError("bad_request", "article id must be a 24-character hex id (the `id` of a headline)")
    ch.require_coverage()
    dt = ch.data_through()
    limit = int(p.plan_cfg.get("exports_per_month") or 0)
    granted = quota.reserve_exports(p.user_id, p.key_id, 1, limit)
    try:
        until_x = (date.fromisoformat(dt) + timedelta(days=1)).isoformat()
        permitted = f"datetime < {ch.sql_str(until_x)}"
        history_days = p.plan_cfg.get("history_days")
        if history_days is not None:
            since = (date.fromisoformat(dt) - timedelta(days=int(history_days))).isoformat()
            permitted += f" AND datetime >= {ch.sql_str(since)}"
        sql = f"SELECT {c.HEADLINE_COLS} FROM {ch.TABLE} WHERE target_id = {ch.sql_str(aid)} AND {permitted} LIMIT 1"
        with ThreadPoolExecutor(max_workers=2) as pool:
            f_row = pool.submit(lambda: c.run_ch(lambda: ch.one(sql)))
            f_rec = pool.submit(articles.resolve, [aid], True)
            row = f_row.result()
            recs, store_errors = f_rec.result()
        rec = recs.get(aid)
        if not row:
            raise ApiError("no_data", "no article with that id in the corpus",
                           meta={"notes": c.store_notes(store_errors)})
        if not rec or not rec.get("url"):
            raise ApiError("no_data", "The full article is currently unavailable", meta={"notes": c.store_notes(store_errors)})
        item = c.item_of(row, rec, full=True)
    except BaseException:
        quota.refund_exports(p.user_id, p.key_id, granted)
        raise
    quota.record_daily(p.user_id, p.key_id, endpoint, requests=0, exports=1)
    window = {"published_at": item["published_at"], "data_through": dt,
              "freshness": ch.freshness_note()}
    return envelope.ok(FEATURE, {"article": item, "charged_exports": 1},
                       subject={"id": aid}, window=window,
                       meta=c.meta(t0, c.store_notes(store_errors)))
