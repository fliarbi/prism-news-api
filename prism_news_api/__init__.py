"""prism_news_api — the Prism News Exploration API.

A FastAPI service over Prism's 255.6M-article news corpus. The business API
(`prism-business-news-api`) imports this package rather than copying it:

    from prism_news_api import auth, quota, ch, envelope, filters, articles, export

`export` is re-exported from `prism_news_api.features.export`.
"""
from __future__ import annotations

__version__ = "0.2.0"

from . import articles, auth, ch, config, envelope, filters, quota, taxonomy  # noqa: E402,F401
from .features import export  # noqa: E402,F401

__all__ = ["__version__", "articles", "auth", "ch", "config", "envelope",
           "filters", "quota", "taxonomy", "export"]
