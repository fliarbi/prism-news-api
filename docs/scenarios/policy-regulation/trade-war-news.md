# Trade War News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “trade war news” · 720/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [trade-war-news.json](../../examples/scenarios/trade-war-news.json).

**Question.** How did coverage of trade war develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="trade war"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,195 |
| Negative · neutral · positive | 79% · 2.4% · 18% |
| Critical (priority 7–9) | 77% (1,687 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (5,606 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | political economy and resource allocation |

## Twelve months of coverage

Monthly matching articles for `trade war` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5,606 | 78% | 4,191 | 1,214 | ████████████████████ |
| Jun 2025 | 1,694 | 70% | 1,300 | 308 | ██████ |
| Jul 2025 | 2,787 | 65% | 2,180 | 529 | ██████████ |
| Aug 2025 | 1,430 | 77% | 1,111 | 264 | █████ |
| Sep 2025 | 943 | 71% | 621 | 280 | ███ |
| Oct 2025 | 2,228 | 82% | 1,644 | 502 | ████████ |
| Nov 2025 | 544 | 79% | 408 | 118 | ██ |
| Dec 2025 | 489 | 83% | 365 | 113 | ██ |
| Jan 2026 | 953 | 78% | 793 | 140 | ███ |
| Feb 2026 | 576 | 81% | 437 | 125 | ██ |
| Mar 2026 | 321 | 71% | 238 | 76 | █ |
| Apr 2026 | 345 | 70% | 268 | 64 | █ |

The last four complete months averaged 549 articles a month against 2,879 in the first four (-81%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 636 | 29% |
| China | 110 | 5.0% |
| Canada | 77 | 3.5% |
| Greenland | 37 | 1.7% |
| United Kingdom | 25 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| political economy and resource allocation | 54 | 3.6% | -8% |
| trade policies and agreements | 647 | 43% | -51% |
| trade agreements and free trade zones | 46 | 3.0% | +31% |
| economy news: trade deficit/surplus announcements | 38 | 2.5% | -30% |
| trade dispute resolution mechanisms | 36 | 2.4% | +24% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Abraham Newman, analista internacional: “El neomonarquismo de Trump nos ayuda a comprender por qué EE.UU.…](https://flipr.com.ar/nacionales/economia/lanacion/abraham-newman-analista-internacional-el-neomonarquismo-de-trump-nos-ayuda-a-comprender-por-que-ee-uu-esta-tan-cerca-de-la-argentina/) | flipr.com.ar | 8 | negative |
| 20 Apr 2026 | [Top five quotes from our 2026 Economic Outlook webinar](https://www.canadianmanufacturing.com/features/2026-economic-outlook-webinar-charts-a-path-for-canadas-mfg-industry/) | canadianmanufacturing.com | 8 | negative |
| 14 Apr 2026 | [U.S. Exporters Laud China Tariff Reprieve, but Scars Remain](https://www.caixinglobal.com/2025-11-07/us-exporters-laud-china-tariff-reprieve-but-scars-remain-102380133.html) | caixinglobal.com | 8 | negative |
| 6 Apr 2026 | [Trump to Meet Xi Jinping During First China Visit in Eight Years - Time News](https://time.news/trump-to-meet-xi-jinping-during-first-china-visit-in-eight-years/) | time.news | 8 | negative |
| 31 Mar 2026 | [Impacts of Trump's Liberation Day tariffs linger one year later](https://www.wtxl.com/politics/economy/impacts-of-trumps-liberation-day-tariffs-linger-one-year-later) | wtxl.com | 8 | negative |
| 30 Mar 2026 | [Iran could emerge stronger and more dangerous from this war](https://www.afr.com/world/middle-east/iran-could-emerge-stronger-and-more-dangerous-from-this-war-20260331-p5zk3d) | afr.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "trade war" --since 2026-01-01 --until 2026-04-30
prism-news trends "trade war" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "trade war" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "trade war", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "trade war", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Citizenship News](citizenship-news.md)
- [Obamacare News](obamacare-news.md)
- [MSP News](msp-news.md)
- [Data Privacy News](data-privacy-news.md)
