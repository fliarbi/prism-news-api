"""Open news-topic datasets by Fliar (January 2019 - July 2026).

Each topic is a public Hugging Face dataset repo fliarbi/<slug>-news-2019-2026 with a
sample of headlines, a monthly volume and tone series, a country table and more.
Licence of the data: CC BY-NC 4.0.

    from prism_news import datasets
    datasets.list_topics()                     # [{"slug": "floods", "topic": "floods", ...}, ...]
    t = datasets.load("floods")                # {"sample": ..., "monthly": ..., "countries": ...}
    monthly = datasets.load_table("floods", "monthly")

Tables are pandas DataFrames when pandas is installed (or as_frame=True), otherwise
lists of dicts. Downloads are cached in ~/.cache/prism-news (PRISM_NEWS_CACHE overrides).
"""
from __future__ import annotations

import csv
import io
import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from . import __version__

HF_ORG = "fliarbi"
SUFFIX = "-news-2019-2026"
HF_BASE = "https://huggingface.co"
DEFAULT_TABLES = ("sample", "monthly", "countries")
TABLES = ("sample", "monthly", "countries", "cities", "continents", "country_tone", "country_trend",
          "organisations", "themes", "tone_by_year", "states_india", "states_us", "research_by_year",
          "top_papers", "patents_by_year", "patent_offices", "patent_cpc")

# slug, topic, cluster
_TOPICS = [
    ('snowfall', 'snowfall', 'weather'),
    ('hurricanes', 'hurricanes', 'disasters'),
    ('covid', 'covid', 'health'),
    ('floods', 'floods', 'disasters'),
    ('waste-management', 'waste management', 'urban'),
    ('mental-health', 'mental health', 'health'),
    ('earthquakes', 'earthquakes', 'disasters'),
    ('weather', 'weather', 'weather'),
    ('climate-change', 'climate change', 'environment'),
    ('lung-cancer', 'lung cancer', 'health'),
    ('tornadoes', 'tornadoes', 'disasters'),
    ('cybercrime', 'cybercrime', 'crime'),
    ('pfas', 'pfas', 'water'),
    ('gun-violence', 'gun violence', 'crime'),
    ('measles', 'measles', 'health'),
    ('airports', 'airports', 'urban'),
    ('breast-cancer', 'breast cancer', 'health'),
    ('homelessness', 'homelessness', 'society'),
    ('electric-vehicles', 'electric vehicles', 'energy'),
    ('alzheimers', "alzheimer's", 'health'),
    ('malaria', 'malaria', 'health'),
    ('inflation', 'inflation', 'economy'),
    ('volcano', 'volcano', 'disasters'),
    ('data-breach', 'data breach', 'crime'),
    ('monsoon', 'monsoon', 'weather'),
    ('unemployment', 'unemployment', 'economy'),
    ('migration', 'migration', 'society'),
    ('tsunami', 'tsunami', 'disasters'),
    ('suicide', 'suicide', 'health'),
    ('natural-disasters', 'natural disasters', 'disasters'),
    ('housing', 'housing', 'urban'),
    ('air-pollution', 'air pollution', 'environment'),
    ('cybersecurity', 'cybersecurity', 'tech'),
    ('kidney-disease', 'kidney disease', 'health'),
    ('drowning', 'drowning', 'safety'),
    ('domestic-violence', 'domestic violence', 'crime'),
    ('hepatitis', 'hepatitis', 'health'),
    ('population', 'population', 'society'),
    ('poverty', 'poverty', 'economy'),
    ('smartphones', 'smartphones', 'tech'),
    ('drones', 'drones', 'tech'),
    ('protests', 'protests', 'society'),
    ('road-accidents', 'road accidents', 'safety'),
    ('drought', 'drought', 'environment'),
    ('plane-crash', 'plane crash', 'safety'),
    ('obesity', 'obesity', 'health'),
    ('oil-prices', 'oil prices', 'energy'),
    ('opioid-crisis', 'opioid crisis', 'health'),
    ('antimicrobial-resistance', 'antimicrobial resistance', 'health'),
    ('vaccine', 'vaccine', 'health'),
    ('robotics', 'robotics', 'tech'),
    ('biodiversity-loss', 'biodiversity loss', 'environment'),
    ('food-safety', 'food safety', 'food'),
    ('ransomware', 'ransomware', 'crime'),
    ('data-centers', 'data centers', 'tech'),
    ('heart-attack', 'heart attack', 'health'),
    ('carbon-emissions', 'carbon emissions', 'environment'),
    ('water-pollution', 'water pollution', 'environment'),
    ('crimes-against-women', 'crimes against women', 'crime'),
    ('5g', '5g', 'tech')
]


def _cache_dir() -> Path:
    d = Path(os.environ.get("PRISM_NEWS_CACHE") or Path.home() / ".cache" / "prism-news")
    d.mkdir(parents=True, exist_ok=True)
    return d


def _get(url: str, timeout: float = 120.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": f"prism-news-python/{__version__}"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def repo_id(slug: str) -> str:
    """Hugging Face repo id for a topic slug, e.g. 'floods' -> 'fliarbi/floods-news-2019-2026'."""
    return f"{HF_ORG}/{slug}{SUFFIX}"


def url(slug: str) -> str:
    """Dataset page URL."""
    return f"{HF_BASE}/datasets/{repo_id(slug)}"


def list_topics(online: bool = False, cluster: Optional[str] = None) -> List[Dict[str, str]]:
    """The topic datasets: [{"slug", "topic", "cluster", "repo", "url"}].

    online=True asks the Hugging Face API which repos are live right now and returns only those
    (topics published after this release appear too).
    """
    known = {s: (t, c) for s, t, c in _TOPICS}
    slugs = [s for s, _, _ in _TOPICS]
    if online:
        raw = json.loads(_get(f"{HF_BASE}/api/datasets?author={HF_ORG}&limit=1000"))
        live = [d["id"].split("/", 1)[1][: -len(SUFFIX)] for d in raw if d.get("id", "").endswith(SUFFIX)]
        slugs = [s for s in slugs if s in live] + sorted(s for s in live if s not in known)
    out = []
    for s in slugs:
        topic, clus = known.get(s, (s.replace("-", " "), ""))
        if cluster and clus != cluster:
            continue
        out.append({"slug": s, "topic": topic, "cluster": clus, "repo": repo_id(s), "url": url(s)})
    return out


def _file_for(slug: str, table: str) -> str:
    return f"data/{slug}-news-sample.csv" if table == "sample" else f"data/{table}.csv"


def download(slug: str, table: str = "sample", refresh: bool = False) -> Path:
    """Download one CSV (cached) and return its local path."""
    if table not in TABLES:
        raise ValueError(f"unknown table {table!r}; choose one of {', '.join(TABLES)}")
    target = _cache_dir() / slug / f"{table}.csv"
    if target.exists() and not refresh:
        return target
    src = f"{HF_BASE}/datasets/{repo_id(slug)}/resolve/main/{_file_for(slug, table)}"
    try:
        data = _get(src)
    except urllib.error.HTTPError as e:
        if e.code in (401, 404):
            raise LookupError(f"{repo_id(slug)} has no {table!r} table (HTTP {e.code}); "
                              f"see datasets.list_topics()") from None
        raise
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".part")
    tmp.write_bytes(data)
    tmp.replace(target)
    return target


def _pandas():
    try:
        import pandas  # noqa: F401
        return pandas
    except ImportError:
        return None


def load_table(slug: str, table: str = "sample", as_frame: Optional[bool] = None, refresh: bool = False):
    """One table as a pandas DataFrame (if pandas is installed) or a list of dicts."""
    path = download(slug, table, refresh=refresh)
    pd = _pandas()
    if as_frame is None:
        as_frame = pd is not None
    if as_frame:
        if pd is None:
            raise ImportError("as_frame=True needs pandas: pip install pandas")
        return pd.read_csv(path)
    with io.open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load(slug: str, tables: Iterable[str] = DEFAULT_TABLES, as_frame: Optional[bool] = None,
         refresh: bool = False) -> Dict[str, object]:
    """Load several tables of one topic: {"sample": ..., "monthly": ..., "countries": ...}."""
    if isinstance(tables, str):
        tables = (tables,)
    return {t: load_table(slug, t, as_frame=as_frame, refresh=refresh) for t in tables}
