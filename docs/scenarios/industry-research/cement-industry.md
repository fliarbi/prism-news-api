# Cement Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cement industry” · 2,900/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cement-industry.json](../../examples/scenarios/cement-industry.json).

**Question.** How much news did the cement industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="cement industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 661 |
| Negative · neutral · positive | 25% · 2.6% · 73% |
| Critical (priority 7–9) | 64% (426 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (206 articles) |
| Most-reported country | India (15% of matches) |
| Strongest theme by lift | cement additives and aggregates |

## Twelve months of coverage

Monthly matching articles for `cement industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 132 | 70% | 16 | 115 | █████████████ |
| Jun 2025 | 103 | 72% | 14 | 89 | ██████████ |
| Jul 2025 | 142 | 69% | 25 | 115 | ██████████████ |
| Aug 2025 | 160 | 71% | 24 | 134 | ████████████████ |
| Sep 2025 | 142 | 64% | 35 | 105 | ██████████████ |
| Oct 2025 | 164 | 73% | 27 | 134 | ████████████████ |
| Nov 2025 | 177 | 66% | 23 | 151 | █████████████████ |
| Dec 2025 | 194 | 77% | 33 | 159 | ███████████████████ |
| Jan 2026 | 118 | 75% | 17 | 97 | ███████████ |
| Feb 2026 | 178 | 58% | 35 | 136 | █████████████████ |
| Mar 2026 | 159 | 68% | 47 | 110 | ███████████████ |
| Apr 2026 | 206 | 61% | 64 | 138 | ████████████████████ |

The last four complete months averaged 165 articles a month against 134 in the first four (+23%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 43% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 101 | 15% |
| United States | 37 | 5.6% |
| China | 13 | 2.0% |
| United Kingdom | 13 | 2.0% |
| Nigeria | 12 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| cement additives and aggregates | 82 | 18% | -9% |
| concrete and cement materials | 95 | 21% | -14% |
| carbon footprint reduction techniques | 42 | 9.2% | -2% |
| company expansions and new market entries | 36 | 7.9% | +80% |
| green building materials (eco-friendly) | 11 | 2.4% | +10% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Irish cement industry is convinced fossil fuel usage can be cut by 90% over next 15 years](http://www.irishtimes.com/business/2026/04/20/cement-industry-believes-it-can-cut-fossil-fuel-usage-by-90-over-next-15-years/) | irishtimes.com | 8 | negative |
| 18 Apr 2026 | [Cement demand to be healthy in Q1FY27E; Likely to hit profitability despite price hikes: Nuvama](https://www.aninews.in/news/business/cement-demand-to-be-healthy-in-q1fy27e-likely-to-hit-profitability-despite-price-hikes-nuvama20260418080113) | aninews.in | 8 | positive |
| 30 Apr 2026 | [Driving cement decarbonisation at CalPortland](https://www.cemnet.com/Articles/story/181233/driving-cement-decarbonisation-at-calportland.html) | cemnet.com | 7 | positive |
| 29 Apr 2026 | [ABB and Alcemy collaborate to bring AI-driven quality control to cement production](https://www.worldcement.com/europe-cis/29042026/abb-and-alcemy-collaborate-to-bring-ai-driven-quality-control-to-cement-production/) | worldcement.com | 7 | positive |
| 22 Apr 2026 | [CarbonCure Appoints Yuliya Kravtsov As CEO To Scale Global Concrete Decarbonization](https://esgnews.com/carboncure-appoints-yuliya-kravtsov-as-ceo-to-scale-global-concrete-decarbonization/) | esgnews.com | 7 | positive |
| 21 Apr 2026 | [Indonesia Outlines Cement Industry Decarbonization Strategy](https://en.tempo.co/read/2099448/indonesia-outlines-cement-industry-decarbonization-strategy) | en.tempo.co | 7 | positive |
| 18 Apr 2026 | [Cement demand to be healthy in Q1FY27E, likely to hit profitability despite price hikes: Nuvama](https://infra.economictimes.indiatimes.com/news/construction/cement-demand-to-be-healthy-in-q1fy27e-likely-to-hit-profitability-despite-price-hikes-nuvama/130350048) | infra.economictimes.indiatimes.com | 7 | positive |
| 16 Apr 2026 | [Kadyrov honoured for expanding Chechen cement production](https://www.cemnet.com/News/story/181165/kadyrov-honoured-for-expanding-chechen-cement-production.html) | cemnet.com | 7 | positive |
| 15 Apr 2026 | [Indonesia rolls out five-pillar cement decarbonization strategy](https://en.antaranews.com/news/412408/indonesia-rolls-out-five-pillar-cement-decarbonization-strategy) | en.antaranews.com | 7 | positive |
| 10 Apr 2026 | [Work resumes on INR 15bn Suryatara Cement project](https://www.cemnet.com/News/story/181133/work-resumes-on-inr-15bn-suryatara-cement-project.html) | cemnet.com | 7 | positive |
| 7 Apr 2026 | [Breedon warns UK cement industry at risk without CBAM overhaul \| TheBusinessDesk.com](https://www.thebusinessdesk.com/eastmidlands/news/2109190-breedon-warns-uk-cement-industry-at-risk-without-cbam-overhaul) | thebusinessdesk.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cement industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "cement industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cement industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cement industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cement industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through 24 Aug 2026; intake thins after May 2026.
- `q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- zero-count periods are included; partial_period marks buckets the window only partly covers
- Country shares use all matching articles. Location information is incomplete and varies by period.
- Theme shares use articles with identified themes; articles may have more than one theme.

## Related demonstrations

- [Agriculture Industry](agriculture-industry.md)
- [Construction Industry](construction-industry.md)
- [Fashion Industry](fashion-industry.md)
- [Diamond Industry](diamond-industry.md)
