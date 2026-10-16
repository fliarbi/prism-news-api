"""main — create_app(); the ASGI entry point is `prism_news_api.main:app`.

    gunicorn -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8800 prism_news_api.main:app

Public API: CORS allow-all. /healthz needs no key; everything under /v1 does
(except the OpenAPI document and /docs).
"""
from __future__ import annotations

import logging
import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from . import __version__, ch, config, routers, explore_routes

DESCRIPTION = """
Explore 450M+ historical and real-time news articles by topic, sentiment, importance, GCP content class,
and combinations of filters. The article count is supplied by Fliar; query counts
reflect available matching coverage. Browse 100 headlines or export 100 full
articles by default. Discover up to five themes with a specific search phrase.

Get an API key from Fliar dashboard > Fliar Prism > API keys. Send X-API-Key
or Authorization: Bearer. One account quota works across both news APIs.
Read the [user guide](/guide) for examples, pagination and quota rules.
"""

EXPOSE_HEADERS = ["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-Quota-Requests-Remaining",
                  "X-Quota-Exports-Remaining", "X-Plan", "Retry-After", "X-Export-Delivered",
                  "Content-Disposition"]


def _logging() -> None:
    level = os.environ.get("PRISM_LOG_LEVEL", "INFO").upper()
    root = logging.getLogger()
    if not root.handlers:
        h = logging.StreamHandler(sys.stderr)
        h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        root.addHandler(h)
    root.setLevel(level)
    logging.getLogger("pymongo").setLevel(logging.WARNING)


def create_app() -> FastAPI:
    _logging()
    app = FastAPI(title="Prism News Exploration API", version=__version__,
                  description=DESCRIPTION.strip(), docs_url="/docs", redoc_url=None,
                  openapi_url="/v1/openapi.json",
                  # Public path prefix when served behind a proxy that strips it (e.g. /news),
                  # so /docs loads the schema from the right URL. Empty when served at the root.
                  root_path=os.environ.get("PRISM_ROOT_PATH", "").rstrip("/"),
                  contact={"name": "Fliar Business Intelligence", "url": "https://fliarbi.com"})
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False,
                       allow_methods=["*"], allow_headers=["*"], expose_headers=EXPOSE_HEADERS)
    app.include_router(routers.router)
    app.include_router(explore_routes.router)
    routers.install_handlers(app)

    @app.get("/healthz", tags=["meta"], summary="Liveness (no auth)")
    def healthz():
        return {"ok": True, "service": "prism-news-api", "version": __version__}

    @app.get("/guide", include_in_schema=False)
    def guide():
        from fastapi.responses import PlainTextResponse
        return PlainTextResponse((config.PACKAGE_DIR / "data" / "user_guide.md").read_text(),
                                 media_type="text/markdown")

    def openapi():
        if app.openapi_schema:
            return app.openapi_schema
        schema = get_openapi(title=app.title, version=app.version, description=app.description,
                             routes=app.routes, contact=app.contact)
        comps = schema.setdefault("components", {})
        comps["securitySchemes"] = {
            "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
            "BearerAuth": {"type": "http", "scheme": "bearer"}}
        comps.setdefault("schemas", {})["Envelope"] = {
            "type": "object",
            "properties": {"ok": {"type": "boolean"}, "feature": {"type": "string"},
                           "subject": {"type": "object"}, "data": {},
                           "window": {"type": "object"}, "meta": {"type": "object"},
                           "error": {"type": "object", "properties": {
                               "kind": {"type": "string", "enum": list(routers.envelope.KINDS)},
                               "reason": {"type": "string"}}}},
            "required": ["ok", "feature", "subject", "data", "window", "meta"]}
        for path, ops in schema.get("paths", {}).items():
            for op in ops.values():
                if not isinstance(op, dict) or not path.startswith("/v1/"):
                    continue
                op["security"] = [{"ApiKeyAuth": []}, {"BearerAuth": []}]
                responses = op.setdefault("responses", {})
                responses.pop("422", None)
                for code, description in (("400", "Invalid parameters"), ("401", "API key required or invalid"),
                    ("402", "Monthly quota reached"), ("404", "No matching data"),
                    ("429", "Rate limit reached; respect Retry-After"), ("500", "Request could not be completed"),
                    ("502", "Data temporarily unavailable"), ("503", "Reliable coverage temporarily unavailable")):
                    responses.setdefault(code, {"description": description})
                for resp in responses.values():
                    resp.setdefault("content", {}).setdefault("application/json", {})["schema"] = {
                        "$ref": "#/components/schemas/Envelope"}
                if path == "/v1/export":
                    content = responses["200"]["content"]
                    for media in ("text/csv", "application/x-ndjson"):
                        content[media] = {"schema": {"type": "string"}}
        app.openapi_schema = schema
        return schema

    app.openapi = openapi
    return app


app = create_app()
