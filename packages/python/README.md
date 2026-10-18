# prism-news

[![PyPI](https://img.shields.io/pypi/v/prism-news.svg)](https://pypi.org/project/prism-news/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/fliarbi/prism-news-api/blob/main/packages/python/LICENSE)

Python client, command-line tool and **60 open news-topic datasets** for the
[Prism News API](https://github.com/fliarbi/prism-news-api) by Fliar: 450M+ historical and
real-time news articles with sentiment, priority, themes, geography and content classes.

Standard library only. Python 3.8+. pandas is optional.

```bash
pip install prism-news
# with DataFrame support
pip install "prism-news[pandas]"
```

## Open datasets (no API key)

Each topic dataset covers January 2019 to July 2026 and is published at
`https://huggingface.co/datasets/fliarbi/<slug>-news-2019-2026` (data licence CC BY-NC 4.0).
Topics include floods, hurricanes, covid, mental health, climate change, inflation, cybercrime,
electric vehicles, air pollution, data centers and 50 more.

```python
from prism_news import datasets

datasets.list_topics()[:2]
# [{'slug': 'snowfall', 'topic': 'snowfall', 'cluster': 'weather',
#   'repo': 'fliarbi/snowfall-news-2019-2026', 'url': 'https://huggingface.co/datasets/...'}, ...]

datasets.list_topics(cluster="health")      # filter by cluster
datasets.list_topics(online=True)           # only the repos live right now

t = datasets.load("floods")                 # {"sample": ..., "monthly": ..., "countries": ...}
t["monthly"].head()                         # DataFrame when pandas is installed
#      month  articles  all_news_articles  per_10k_news ...

rows = datasets.load_table("floods", "themes", as_frame=False)   # list of dicts
path = datasets.download("floods", "countries")                    # local CSV path
```

Tables: `sample` (headline sample), `monthly`, `countries`, `cities`, `continents`,
`country_tone`, `country_trend`, `organisations`, `themes`, `tone_by_year`, `states_india`,
`states_us`, `research_by_year`, `top_papers`, `patents_by_year`, `patent_offices`, `patent_cpc`.
Files are cached in `~/.cache/prism-news` (set `PRISM_NEWS_CACHE` to move it).

## API client

Create a key in the Fliar dashboard (free tier included; one key works on the Radar API and
both News APIs) and export it:

```bash
export PRISM_API_KEY=rdr_...
```

```python
from prism_news import Client, PrismAPIError

client = Client()                     # base URL https://radar-api.fliarbi.com/news

client.status()                       # free: index coverage
hl = client.headlines("electric vehicle", since="2026-01-01", until="2026-04-30", limit=20)
for item in hl["data"]["items"]:
    print(item["published_at"], item["headline"])

client.trends("tariffs", granularity="monthly")
client.sentiment("heatwave", since="2026-04-01")
client.themes("data centers", limit=5)
client.compare(["electric vehicle", "battery storage"], since="2026-01-01", until="2026-04-30")

# Business News API (same key)
client.business("funding", sector="fintech", sort="amount", limit=10)
client.company_news("tesla.com", since="2026-01-01")

try:
    client.me()
except PrismAPIError as e:
    print(e.status, e.kind)
```

Every method returns the JSON envelope `{"ok": ..., "data": ..., "meta": ...}`. Keyword
arguments become request fields; `None` values are dropped. `client.request(method, path, body)`
calls any endpoint directly.

## Command line

```bash
prism-news login                                  # saves base URL and key, owner-only file
prism-news status
prism-news headlines "electric vehicle" --since 2026-01-01 --limit 20 --table
prism-news trends "tariffs" --granularity monthly --table
prism-news export "floods" --since 2026-01-01 -o floods.csv
prism-business-news funding --sector fintech --sort amount --limit 10 --table

prism-news datasets list                          # open topic datasets, no key
prism-news datasets download floods monthly countries
```

Any `--name value` becomes a request field (`--priority-min 7` sends `priority_min=7`); repeat an
option for a list. Environment overrides: `PRISM_API_KEY`, `PRISM_API_BASE`,
`PRISM_BUSINESS_API_BASE`.

## Links

- API docs and 300 worked examples: https://github.com/fliarbi/prism-news-api
- JavaScript / TypeScript client: `npm install prism-news-api`
- Contact: b2b@fliarbi.com

## Licence

Code: MIT. Datasets: CC BY-NC 4.0.
