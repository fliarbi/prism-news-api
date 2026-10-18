"""prism-news: Python client, CLI and open datasets for the Prism News API by Fliar.

    from prism_news import Client, datasets

    client = Client()                      # key from PRISM_API_KEY
    client.headlines("electric vehicle", since="2026-01-01", limit=10)

    datasets.list_topics()                 # 60 open topic datasets, 2019-2026
    tables = datasets.load("floods")       # sample, monthly, countries
"""
__version__ = "0.1.0"

from .client import Client, PrismAPIError  # noqa: E402
from . import datasets  # noqa: E402

__all__ = ["Client", "PrismAPIError", "datasets", "__version__"]
