"""routers — the HTTP surface. One dependency chain on every authenticated path:

    auth (key -> principal)  ->  rate limit  ->  request quota  ->  handler

Rate and quota are checked BEFORE the handler touches ClickHouse. Unmetered
paths (/v1/me, /v1/status, /v1/classes*, /v1/vocabulary) skip the request
quota but still pass the rate limit. The body is ALWAYS the envelope — on
success, on every ApiError, on validation failures, on unknown routes and on
unhandled exceptions (which are logged with a traceback and rendered as
`internal` with a short reason, never leaked).

Every authenticated response carries X-RateLimit-Limit, X-RateLimit-Remaining,
X-Quota-Requests-Remaining, X-Quota-Exports-Remaining and X-Plan.
"""
from __future__ import annotations

import json
import logging
import time
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, Query, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import Field
from starlette.exceptions import HTTPException as StarletteHTTPException

from . import auth, ch, config, envelope, quota, public
from .auth import Principal
from .ch import CHError
from .envelope import ApiError
from .features import articles_ep, classes, export, headlines, me, priority
from .features import sentiment, status, themes, trends, vocabulary
from .filters import Filters

log = logging.getLogger("prism_news_api.http")
router = APIRouter(prefix="/v1")

UNMETERED_PREFIXES = ("/v1/me", "/v1/status", "/v1/classes", "/v1/vocabulary")


# ── response plumbing ────────────────────────────────────────────────────────
class EnvelopeJSON(JSONResponse):
    """default=str: one datetime from the article store must never turn a
    working feature into a 500."""

    def render(self, content) -> bytes:
        return json.dumps(content, ensure_ascii=False, allow_nan=False,
                          default=str).encode("utf-8")


def _state(request: Request, name: str, default=None):
    return getattr(request.state, name, default)


def _headers(request: Request, extra: dict | None = None) -> dict:
    p: Principal | None = _state(request, "principal")
    h = {}
    if p is not None:
        h.update(quota.headers_for(_state(request, "quota"), p.plan))
    h.update(extra or {})
    return h


def _decorate(request: Request, env: dict) -> dict:
    p: Principal | None = _state(request, "principal")
    meta = env.setdefault("meta", {})
    if p is not None:
        meta["plan"] = p.plan
        snap = _state(request, "quota")
        if snap is not None:
            meta["quota"] = snap
        if p.notes:
            meta["notes"] = list(dict.fromkeys(list(meta.get("notes") or []) + list(p.notes)))
    meta.setdefault("request_seconds", round(time.time() - _state(request, "t0", time.time()), 3))
    return public.response(env)


def _maybe_refresh_quota(request: Request) -> None:
    """Export-charging handlers change the counters AFTER the dependency chain
    took its snapshot; re-read so headers and meta.quota reflect the charge."""
    p: Principal | None = _state(request, "principal")
    if p is None or not _state(request, "refresh_quota"):
        return
    try:
        request.state.quota = quota.usage(p.user_id, p.key_id, p.plan_cfg, _state(request, "rate"))
    except Exception as e:                      # headers are a courtesy, not the answer
        log.debug("quota refresh skipped: %s", e)
    request.state.refresh_quota = False


def respond(request: Request, env: dict, status: int | None = None,
            headers: dict | None = None) -> Response:
    _maybe_refresh_quota(request)
    env = _decorate(request, env)
    return EnvelopeJSON(env, status_code=status or envelope.status_of(env),
                        headers=_headers(request, headers))


def respond_error(request: Request, feature: str, e: ApiError) -> Response:
    snap = (e.meta or {}).get("quota") or _state(request, "quota")
    rate = _state(request, "rate")
    if snap is not None and rate and "rate" not in snap:
        snap = {**snap, "rate": rate}
    if snap is not None:
        request.state.quota = snap
    env = e.envelope(feature, meta={k: v for k, v in (e.meta or {}).items() if k != "quota"})
    return respond(request, env, status=e.status, headers=e.headers)


def guard(request: Request, feature: str, fn) -> Response:
    """Run a feature; whatever happens, the client gets the envelope."""
    try:
        out = fn()
        return out if isinstance(out, Response) else respond(request, out)
    except ApiError as e:
        return respond_error(request, feature, e)
    except CHError as e:
        return respond_error(request, feature, ch.as_api_error(e))
    except Exception as e:                      # never leak; never 500 without a body
        log.exception("unhandled in %s", feature)
        return respond_error(request, feature,
                             ApiError("internal", "The request could not be completed. Please try again later."))


def feature(fid: str):
    """Tag a route function so app-level handlers know which feature failed."""
    def deco(fn):
        fn.feature = fid
        return fn
    return deco


def _feature_of(request: Request) -> str:
    ep = request.scope.get("endpoint")
    return getattr(ep, "feature", None) or "api"


def _route_path(request: Request) -> str:
    route = request.scope.get("route")
    return getattr(route, "path", None) or request.url.path


# ── dependency chain ─────────────────────────────────────────────────────────
def principal_dep(request: Request) -> Principal:
    request.state.t0 = time.time()
    p = auth.authenticate(request.headers)
    request.state.principal = p
    return p


def _rate(request: Request, p: Principal) -> dict:
    rate = quota.check_rate(p.user_id, int(p.plan_cfg.get("rate_per_minute") or 30))
    request.state.rate = rate
    return rate


def metered(request: Request, p: Principal = Depends(principal_dep)) -> Principal:
    rate = _rate(request, p)
    quota.check_requests(p.user_id, p.key_id, int(p.plan_cfg.get("requests_per_month") or 0))
    request.state.quota = quota.usage(p.user_id, p.key_id, p.plan_cfg, rate)
    quota.record_daily(p.user_id, p.key_id, _route_path(request))
    return p


def unmetered(request: Request, p: Principal = Depends(principal_dep)) -> Principal:
    rate = _rate(request, p)
    request.state.quota = quota.usage(p.user_id, p.key_id, p.plan_cfg, rate)
    return p


# ── parameter models ─────────────────────────────────────────────────────────
FiltersQ = Annotated[Filters, Query()]


class FiltersWithGranularity(Filters):
    granularity: Optional[str] = Field(None, description="daily | weekly | monthly (default weekly)")


# FastAPI 0.116 does NOT expand a query-parameter model when another standalone
# Query() parameter sits beside it in the signature (the model becomes a
# required scalar named `f`), so `granularity` lives inside the model.
FiltersGranQ = Annotated[FiltersWithGranularity, Query()]


class ThemeFilters(Filters):
    """Discover up to five themes related to a specific search phrase."""
    q: str = Field(..., min_length=2, max_length=120, description="A specific topic to explore")
    limit: int = Field(5, ge=1, le=5, description="Number of suggestions, at most five")


ThemeFiltersQ = Annotated[ThemeFilters, Query()]


# ── headlines ────────────────────────────────────────────────────────────────
@router.get("/headlines", tags=["headlines"], summary="Headlines for a filter set")
@feature("news.headlines")
def headlines_get(request: Request, f: FiltersQ, p: Principal = Depends(metered)):
    return guard(request, "news.headlines", lambda: headlines.headlines(p, f))


@router.post("/headlines", tags=["headlines"], summary="Headlines for a filter set (JSON body)")
@feature("news.headlines")
def headlines_post(request: Request, f: Filters, p: Principal = Depends(metered)):
    return guard(request, "news.headlines", lambda: headlines.headlines(p, f))


# ── articles / export ────────────────────────────────────────────────────────
@router.get("/articles/{article_id}", tags=["articles"], summary="One full article (1 export)")
@feature("news.article")
def article_get(request: Request, article_id: str = Path(..., min_length=1, max_length=64),
                p: Principal = Depends(metered)):
    request.state.refresh_quota = True
    return guard(request, "news.article",
                 lambda: articles_ep.article(p, article_id, _route_path(request)))


@router.post("/export", tags=["articles"], summary="Full article bodies for a filter set (json | ndjson | csv)")
@feature("news.export")
def export_post(request: Request, req: export.ExportRequest, p: Principal = Depends(metered)):
    request.state.refresh_quota = True

    def run():
        res = export.run(p, req, _route_path(request))
        _maybe_refresh_quota(request)
        env = _decorate(request, res["envelope"])
        fmt = res["format"]
        if fmt == "json":
            return EnvelopeJSON(env, status_code=200, headers=_headers(request))
        res["envelope"] = env
        res["items"] = env["data"]["items"]
        if fmt == "ndjson":
            return Response(export.to_ndjson(res), media_type="application/x-ndjson",
                            headers=_headers(request, {"X-Export-Delivered": str(len(res["items"]))}))
        return Response(export.to_csv(res), media_type="text/csv; charset=utf-8",
                        headers=_headers(request, {
                            "X-Export-Delivered": str(len(res["items"])),
                            "Content-Disposition": "attachment; filename=prism-export.csv"}))
    return guard(request, "news.export", run)


# ── themes ───────────────────────────────────────────────────────────────────
@router.get("/themes", tags=["themes"], summary="Themes ranked by lift inside a filter set")
@feature("news.themes")
def themes_get(request: Request, f: ThemeFiltersQ, p: Principal = Depends(metered)):
    return guard(request, "news.themes", lambda: themes.themes(p, f))


@router.post("/themes", tags=["themes"], summary="Themes ranked by lift (JSON body)")
@feature("news.themes")
def themes_post(request: Request, f: ThemeFilters, p: Principal = Depends(metered)):
    return guard(request, "news.themes", lambda: themes.themes(p, f))


@router.get("/themes/{name}/headlines", tags=["themes"], summary="Headlines carrying one theme")
@feature("news.theme_headlines")
def theme_headlines_get(request: Request, f: FiltersQ, name: str = Path(..., min_length=1, max_length=200),
                        p: Principal = Depends(metered)):
    return guard(request, "news.theme_headlines",
                 lambda: headlines.headlines(p, f, feature="news.theme_headlines", extra_themes=[name]))


# ── distributions ────────────────────────────────────────────────────────────
@router.get("/sentiment", tags=["distributions"], summary="Sentiment distribution and timeline")
@feature("news.sentiment")
def sentiment_get(request: Request, f: FiltersGranQ, p: Principal = Depends(metered)):
    return guard(request, "news.sentiment", lambda: sentiment.sentiment(p, f, f.granularity))


@router.post("/sentiment", tags=["distributions"], summary="Sentiment distribution (JSON body)")
@feature("news.sentiment")
def sentiment_post(request: Request, f: FiltersWithGranularity, p: Principal = Depends(metered)):
    return guard(request, "news.sentiment", lambda: sentiment.sentiment(p, f, f.granularity))


@router.get("/priority", tags=["distributions"], summary="Priority band distribution vs the corpus baseline")
@feature("news.priority")
def priority_get(request: Request, f: FiltersQ, p: Principal = Depends(metered)):
    return guard(request, "news.priority", lambda: priority.priority(p, f))


@router.post("/priority", tags=["distributions"], summary="Priority distribution (JSON body)")
@feature("news.priority")
def priority_post(request: Request, f: Filters, p: Principal = Depends(metered)):
    return guard(request, "news.priority", lambda: priority.priority(p, f))


@router.get("/trends", tags=["distributions"], summary="Article volume over time")
@feature("news.trends")
def trends_get(request: Request, f: FiltersGranQ, p: Principal = Depends(metered)):
    return guard(request, "news.trends", lambda: trends.trends(p, f, f.granularity))


@router.post("/trends", tags=["distributions"], summary="Article volume over time (JSON body)")
@feature("news.trends")
def trends_post(request: Request, f: FiltersWithGranularity, p: Principal = Depends(metered)):
    return guard(request, "news.trends", lambda: trends.trends(p, f, f.granularity))


# ── classes (unmetered) ──────────────────────────────────────────────────────
@router.get("/classes", tags=["classes"], summary="Find up to five GCP content class codes")
@feature("news.classes")
def classes_get(request: Request, q: Optional[str] = Query(None, max_length=120),
                prefix: Optional[str] = Query(None, max_length=200),
                limit: int = Query(5, ge=1, le=5),
                p: Principal = Depends(unmetered)):
    return guard(request, "news.classes", lambda: classes.list_classes(p, q, prefix, limit))


@router.get("/classes/{code}", tags=["classes"], summary="A GCP content class and its recent coverage")
@feature("news.class")
def class_get(request: Request, code: int = Path(..., ge=0), p: Principal = Depends(unmetered)):
    return guard(request, "news.class", lambda: classes.one_class(p, code))


@router.get("/classes/{code}/headlines", tags=["classes"], summary="Headlines under one class (metered)")
@feature("news.class_headlines")
def class_headlines_get(request: Request, f: FiltersQ, code: int = Path(..., ge=0),
                        p: Principal = Depends(metered)):
    return guard(request, "news.class_headlines", lambda: classes.class_headlines(p, code, f))


# ── metadata (unmetered) ─────────────────────────────────────────────────────
@router.get("/vocabulary", tags=["meta"], summary="Sentiments, groups, priority bands, sort options, plans")
@feature("news.vocabulary")
def vocabulary_get(request: Request, p: Principal = Depends(unmetered)):
    return guard(request, "news.vocabulary", lambda: vocabulary.vocabulary(p))


@router.get("/me", tags=["meta"], summary="Your key, plan, limits and this month's usage")
@feature("api.me")
def me_get(request: Request, p: Principal = Depends(unmetered)):
    return guard(request, "api.me", lambda: me.me(p, _state(request, "rate")))


@router.get("/status", tags=["meta"], summary="Service readiness and available data dates")
@feature("api.status")
def status_get(request: Request, p: Principal = Depends(unmetered)):
    return guard(request, "api.status", lambda: status.status(p))


# ── app-level handlers (dependency-stage failures, validation, unknown routes) ─
def install_handlers(app) -> None:
    @app.exception_handler(ApiError)
    async def _api_error(request: Request, e: ApiError):
        return respond_error(request, _feature_of(request), e)

    @app.exception_handler(CHError)
    async def _ch_error(request: Request, e: CHError):
        return respond_error(request, _feature_of(request), ch.as_api_error(e))

    @app.exception_handler(RequestValidationError)
    async def _validation(request: Request, e: RequestValidationError):
        errs = []
        for err in e.errors():
            if err.get("type") == "extra_forbidden":
                errs.append("Unsupported parameter; see /docs for accepted filters")
                continue
            loc = ".".join(str(x) for x in err.get("loc", []) if x not in ("query", "body", "path"))
            errs.append(f"{loc}: {err.get('msg')}")
        api = ApiError("bad_request", "; ".join(errs)[:600] or "invalid parameters",
                       meta={"validation": [{k: v for k, v in err.items() if k != "ctx"}
                                            for err in e.errors() if err.get("type") != "extra_forbidden"][:5]})
        return respond_error(request, _feature_of(request), api)

    @app.exception_handler(StarletteHTTPException)
    async def _http(request: Request, e: StarletteHTTPException):
        if e.status_code == 404:
            api = ApiError("no_data", "No such endpoint. See /docs for supported endpoints.")
        elif e.status_code == 405:
            api = ApiError("bad_request", "This method is not supported by the endpoint.")
        elif e.status_code == 401:
            api = ApiError("unauthenticated", str(e.detail))
        elif 400 <= e.status_code < 500:
            api = ApiError("bad_request", str(e.detail))
        else:
            api = ApiError("internal", str(e.detail))
        resp = respond_error(request, _feature_of(request), api)
        resp.status_code = e.status_code if e.status_code in (404, 405, 401, 400) else resp.status_code
        return resp

    @app.exception_handler(Exception)
    async def _any(request: Request, e: Exception):
        log.exception("unhandled exception on %s %s", request.method, request.url.path)
        return respond_error(request, _feature_of(request),
                             ApiError("internal", "The request could not be completed. Please try again later."))


__all__ = ["router", "install_handlers", "metered", "unmetered", "principal_dep",
           "guard", "respond", "respond_error", "feature", "EnvelopeJSON",
           "FiltersQ", "FiltersGranQ", "FiltersWithGranularity", "UNMETERED_PREFIXES"]
