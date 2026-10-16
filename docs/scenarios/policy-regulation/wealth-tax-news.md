# Wealth Tax News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wealth tax news” · 10/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wealth-tax-news.json](../../examples/scenarios/wealth-tax-news.json).

**Question.** How did coverage of wealth tax develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="wealth tax"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 387 |
| Negative · neutral · positive | 76% · 5.7% · 18% |
| Critical (priority 7–9) | 76% (295 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (112 articles) |
| Most-reported country | United States (44% of matches) |
| Strongest theme by lift | estate and gift tax planning techniques |

## Twelve months of coverage

Monthly matching articles for `wealth tax` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18 | 44% | 14 | 2 | ███ |
| Jun 2025 | 21 | 33% | 11 | 5 | ████ |
| Jul 2025 | 51 | 51% | 39 | 10 | █████████ |
| Aug 2025 | 37 | 38% | 22 | 14 | ███████ |
| Sep 2025 | 40 | 55% | 31 | 7 | ███████ |
| Oct 2025 | 33 | 73% | 28 | 3 | ██████ |
| Nov 2025 | 60 | 58% | 41 | 16 | ███████████ |
| Dec 2025 | 45 | 67% | 34 | 8 | ████████ |
| Jan 2026 | 111 | 85% | 86 | 17 | ████████████████████ |
| Feb 2026 | 112 | 62% | 80 | 22 | ████████████████████ |
| Mar 2026 | 98 | 78% | 77 | 17 | ██████████████████ |
| Apr 2026 | 66 | 83% | 49 | 13 | ████████████ |

The last four complete months averaged 97 articles a month against 32 in the first four (+205%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 172 | 44% |
| India | 8 | 2.1% |
| Australia | 4 | 1.0% |
| Brazil | 3 | 0.8% |
| China | 3 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| estate and gift tax planning techniques | 48 | 22% | +118% |
| political fundraising mechanisms | 44 | 20% | +529% |
| economy news: tax reform implications | 6 | 2.8% | — |
| real estate investment tax strategies | 14 | 6.4% | +1300% |
| capital gains tax minimization strategies | 8 | 3.7% | +60% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 17 Apr 2026 | [Mamdani Braggs “Highest Taxes Ever”, Then NYC Implodes (Video) \| Politics \| Before It's News](https://beforeitsnews.com/politics/2026/04/mamdani-braggs-highest-taxes-ever-then-nyc-implodes-video-3359371.html) | beforeitsnews.com | 7 | negative |
| 1 Jan 2026 | [Valuation of Unquoted Shares and the Primacy of Profit-Earning Capacity: Foundations of Share Valuation…](https://www.linkedin.com/pulse/valuation-unquoted-shares-primacy-profit-earning-capacity-ojha-qf5rc) | linkedin.com | 7 | neutral |
| 23 Apr 2026 | [List of Countries That Implement Wealth Tax \| Pusat Data Ekonomi dan Bisnis Indonesia \| Databoks](https://databoks.katadata.co.id/en/economics-macro/statistics/69e9f73c6b521/list-of-countries-that-implement-wealth-tax) | databoks.katadata.co.id | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "wealth tax" --since 2026-01-01 --until 2026-04-30
prism-news trends "wealth tax" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "wealth tax" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "wealth tax", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "wealth tax", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Social Media Regulation News](social-media-regulation-news.md)
- [Disaster Management News](disaster-management-news.md)
