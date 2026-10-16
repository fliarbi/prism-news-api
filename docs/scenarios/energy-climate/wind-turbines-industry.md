# Wind Turbines Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wind turbines industry” · 110/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wind-turbines-industry.json](../../examples/scenarios/wind-turbines-industry.json).

**Question.** How did wind turbines coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="wind turbines"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,317 |
| Negative · neutral · positive | 27% · 3.4% · 69% |
| Critical (priority 7–9) | 64% (1,472 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (734 articles) |
| Most-reported country | United States (11% of matches) |
| Strongest theme by lift | wind turbine technology & onshore wind farms |

## Twelve months of coverage

Monthly matching articles for `wind turbines` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 346 | 62% | 79 | 248 | █████████ |
| Jun 2025 | 321 | 55% | 77 | 223 | █████████ |
| Jul 2025 | 481 | 63% | 149 | 317 | █████████████ |
| Aug 2025 | 443 | 63% | 168 | 259 | ████████████ |
| Sep 2025 | 448 | 68% | 110 | 329 | ████████████ |
| Oct 2025 | 398 | 64% | 73 | 303 | ███████████ |
| Nov 2025 | 395 | 67% | 94 | 287 | ███████████ |
| Dec 2025 | 462 | 67% | 136 | 300 | █████████████ |
| Jan 2026 | 447 | 66% | 117 | 318 | ████████████ |
| Feb 2026 | 510 | 61% | 129 | 359 | ██████████████ |
| Mar 2026 | 626 | 63% | 143 | 459 | █████████████████ |
| Apr 2026 | 734 | 64% | 239 | 474 | ████████████████████ |

The last four complete months averaged 579 articles a month against 398 in the first four (+46%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 34% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 245 | 11% |
| United Kingdom | 105 | 4.5% |
| Germany | 77 | 3.3% |
| China | 45 | 1.9% |
| India | 43 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| wind turbine technology & onshore wind farms | 1,139 | 63% | +50% |
| offshore floating wind turbine technology | 296 | 16% | +64% |
| offshore wind energy development | 713 | 39% | +68% |
| renewable energy policy & regulation | 59 | 3.2% | +136% |
| wind energy conversion & electricity production | 39 | 2.1% | +95% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [India’s Dependence on Mineral Imports Threatens Clean Energy Security: IEEFA Report - India Seatrade News](https://indiaseatradenews.com/indias-dependence-on-mineral-imports-threatens-clean-energy-security-ieefa-report/) | indiaseatradenews.com | 8 | positive |
| 30 Apr 2026 | [What's behind the loud booms rattling neighbors? Wind turbines coming down near Mart.](https://www.kxxv.com/news/local-news/in-your-neighborhood/whats-behind-the-loud-booms-rattling-neighbors-wind-turbines-coming-down-near-mart) | kxxv.com | 8 | negative |
| 27 Apr 2026 | [Offshore wind farms rise along Rhode Island's coast, even as Trump tries to stop them](https://www.latimes.com/environment/story/2026-04-27/offshore-wind-farms-rise-along-rhode-islands-coast-even-as-trump-tries-to-stop-them) | latimes.com | 8 | positive |
| 24 Apr 2026 | [Offshore wind farms take shape along Rhode Island's coast, even as Trump wants to stop them](http://gulfnews.com/business/energy/ap-us-climate-offshore-wind-1.500517333) | gulfnews.com | 8 | positive |
| 23 Apr 2026 | [Offshore wind farms take shape along Rhode Island’s coast, even as Trump wants to stop them](https://www.sandiegouniontribune.com/2026/04/23/climate-offshore-wind/) | sandiegouniontribune.com | 8 | positive |
| 23 Apr 2026 | [The Plant That Could End America's Reliance on Foreign Rare-Earth Metals](https://indiandefencereview.com/the-plant-that-could-end-rare-earth-metals/) | indiandefencereview.com | 8 | positive |
| 14 Apr 2026 | [Weekend Long Read: Why Offshore Wind Farms Can Be Deadly to Migratory Birds](https://www.caixinglobal.com/2025-03-01/weekend-long-read-why-offshore-wind-farms-can-be-deadly-to-migratory-birds-102293242.html) | caixinglobal.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "wind turbines" --since 2026-01-01 --until 2026-04-30
prism-news trends "wind turbines" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "wind turbines" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "wind turbines", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "wind turbines", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Pipeline News](pipeline-news.md)
- [Heat Pumps News](heat-pumps-news.md)
- [Ethanol Blending News](ethanol-blending-news.md)
- [Carbon Capture News](carbon-capture-news.md)
