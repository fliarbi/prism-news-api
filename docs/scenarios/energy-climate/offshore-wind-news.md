# Offshore Wind News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “offshore wind news” · 10/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [offshore-wind-news.json](../../examples/scenarios/offshore-wind-news.json).

**Question.** How did offshore wind coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="offshore wind"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,841 |
| Negative · neutral · positive | 32% · 1.1% · 67% |
| Critical (priority 7–9) | 87% (3,358 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,059 articles) |
| Most-reported country | United States (22% of matches) |
| Strongest theme by lift | offshore floating wind turbine technology |

## Twelve months of coverage

Monthly matching articles for `offshore wind` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 728 | 86% | 257 | 457 | ██████████████ |
| Jun 2025 | 477 | 81% | 79 | 385 | █████████ |
| Jul 2025 | 743 | 79% | 181 | 547 | ██████████████ |
| Aug 2025 | 1,001 | 84% | 456 | 529 | ███████████████████ |
| Sep 2025 | 999 | 89% | 428 | 560 | ███████████████████ |
| Oct 2025 | 719 | 84% | 182 | 532 | ██████████████ |
| Nov 2025 | 680 | 81% | 107 | 557 | █████████████ |
| Dec 2025 | 805 | 85% | 326 | 468 | ███████████████ |
| Jan 2026 | 1,059 | 88% | 418 | 624 | ████████████████████ |
| Feb 2026 | 841 | 86% | 203 | 627 | ████████████████ |
| Mar 2026 | 984 | 89% | 314 | 661 | ███████████████████ |
| Apr 2026 | 957 | 87% | 282 | 667 | ██████████████████ |

The last four complete months averaged 960 articles a month against 737 in the first four (+30%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 55% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 846 | 22% |
| United Kingdom | 424 | 11% |
| Germany | 161 | 4.2% |
| Taiwan | 73 | 1.9% |
| Denmark | 67 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| offshore floating wind turbine technology | 1,650 | 54% | +22% |
| offshore wind energy development | 2,222 | 73% | +30% |
| wind turbine technology & onshore wind farms | 1,352 | 44% | +46% |
| offshore supply vessel operations | 128 | 4.2% | +94% |
| offshore oil rig safety protocols | 95 | 3.1% | +53% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Democrats investigate as Trump OKs almost $2 billion in taxpayer money to end offshore wind projects](https://ca.finance.yahoo.com/news/democrats-investigate-trump-oks-almost-154315717.html) | ca.finance.yahoo.com | 8 | negative |
| 29 Apr 2026 | [Gavin Newsom Accuses the Trump Administration of Paying Offshore Wind Developers Nearly $900 Million To Walk…](https://www.inkl.com/news/gavin-newsom-accuses-the-trump-administration-of-paying-offshore-wind-developers-nearly-900-million-to-walk-away-from-projects) | inkl.com | 8 | negative |
| 27 Apr 2026 | [US Government Scraps Two Offshore Wind Leases for Fossil Fuel Investment Pledge](https://www.oedigital.com/news/538511-us-government-scraps-two-offshore-wind-leases-for-fossil-fuel-investment-pledge) | oedigital.com | 8 | negative |
| 27 Apr 2026 | [Offshore wind farms rise along Rhode Island's coast, even as Trump tries to stop them](https://www.latimes.com/environment/story/2026-04-27/offshore-wind-farms-rise-along-rhode-islands-coast-even-as-trump-tries-to-stop-them) | latimes.com | 8 | positive |
| 24 Apr 2026 | [Complexity the 'real killer' for European offshore wind – Vestas CEO](http://www.windpowermonthly.com/article/1955816/complexity-real-killer-european-offshore-wind-–-vestas-ceo) | windpowermonthly.com | 8 | negative |
| 24 Apr 2026 | [Offshore wind farms take shape along Rhode Island's coast, even as Trump wants to stop them](http://gulfnews.com/business/energy/ap-us-climate-offshore-wind-1.500517333) | gulfnews.com | 8 | positive |
| 23 Apr 2026 | [Offshore wind farms take shape along Rhode Island’s coast, even as Trump wants to stop them](https://www.sandiegouniontribune.com/2026/04/23/climate-offshore-wind/) | sandiegouniontribune.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "offshore wind" --since 2026-01-01 --until 2026-04-30
prism-news trends "offshore wind" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "offshore wind" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "offshore wind", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "offshore wind", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through 24 Aug 2026; intake thins after May 2026.
- `q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- zero-count periods are included; partial_period marks buckets the window only partly covers
- Country shares use all matching articles. Location information is incomplete and varies by period.
- Theme shares use articles with identified themes; articles may have more than one theme.

## Related demonstrations

- [Wind Energy News](wind-energy-news.md)
- [Heatwave News](heatwave-news.md)
- [Fuel Prices News](fuel-prices-news.md)
- [Battery Storage News](battery-storage-news.md)
