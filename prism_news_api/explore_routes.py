"""Public exploration routes.

GET/POST /v1/overview and /v1/coverage: ExplorationFilters.
GET/POST /v1/geography: GeographyFilters (q required, default/max five countries).
POST /v1/compare: CompareRequest with 2–5 named filter sets.
GET /v1/articles/{article_id}/related: DiscoveryFilters, 100 headlines by
default, bounded by the plan. All paths use the shared metered guard chain.
"""
from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from .auth import Principal
from .features import explore
from .routers import feature, guard, metered


router = APIRouter(prefix="/v1")
FiltersQ = Annotated[explore.ExplorationFilters, Query()]
DiscoveryQ = Annotated[explore.DiscoveryFilters, Query()]
GeographyQ = Annotated[explore.GeographyFilters, Query()]


@router.get("/overview", summary="Article counts, tone and critical share")
@feature("news.overview")
def overview_get(request: Request, f: FiltersQ, p: Principal = Depends(metered)):
    return guard(request, "news.overview", lambda: explore.overview(p, f))


@router.post("/overview", summary="Article counts, tone and critical share")
@feature("news.overview")
def overview_post(request: Request, f: explore.ExplorationFilters, p: Principal = Depends(metered)):
    return guard(request, "news.overview", lambda: explore.overview(p, f))


@router.post("/compare", summary="Compare 2–5 named filter sets using an exact union count")
@feature("news.compare")
def compare_post(request: Request, req: explore.CompareRequest, p: Principal = Depends(metered)):
    return guard(request, "news.compare", lambda: explore.compare(p, req))


@router.get("/geography", summary="Top five countries for a required phrase")
@feature("news.geography")
def geography_get(request: Request, f: GeographyQ, p: Principal = Depends(metered)):
    return guard(request, "news.geography", lambda: explore.geography(p, f))


@router.post("/geography", summary="Top five countries for a required phrase")
@feature("news.geography")
def geography_post(request: Request, f: explore.GeographyFilters, p: Principal = Depends(metered)):
    return guard(request, "news.geography", lambda: explore.geography(p, f))


@router.get("/coverage", summary="Sentiment, theme and location availability within filters")
@feature("news.coverage")
def coverage_get(request: Request, f: FiltersQ, p: Principal = Depends(metered)):
    return guard(request, "news.coverage", lambda: explore.coverage(p, f))


@router.post("/coverage", summary="Sentiment, theme and location availability within filters")
@feature("news.coverage")
def coverage_post(request: Request, f: explore.ExplorationFilters, p: Principal = Depends(metered)):
    return guard(request, "news.coverage", lambda: explore.coverage(p, f))


@router.get("/articles/{article_id}/related", summary="Related headlines within your phrase and filters")
@feature("news.related")
def related_get(request: Request, article_id: str, f: DiscoveryQ, p: Principal = Depends(metered)):
    return guard(request, "news.related", lambda: explore.related(p, article_id, f))
