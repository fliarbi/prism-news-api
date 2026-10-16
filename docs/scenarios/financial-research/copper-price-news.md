# Copper Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “copper price news” · 590/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [copper-price-news.json](../../examples/scenarios/copper-price-news.json).

**Question.** What did the news say about copper price between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="copper price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 66 |
| Negative · neutral · positive | 36% · 0.0% · 64% |
| Critical (priority 7–9) | 36% (24 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (21 articles) |
| Most-reported country | United States (12% of matches) |
| Strongest theme by lift | industrial metal market analysis |

## Twelve months of coverage

Monthly matching articles for `copper price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 42% | 2 | 10 | ███████████ |
| Jun 2025 | 8 | 25% | 3 | 5 | ████████ |
| Jul 2025 | 12 | 33% | 1 | 11 | ███████████ |
| Aug 2025 | 8 | 62% | 3 | 5 | ████████ |
| Sep 2025 | 16 | 38% | 6 | 10 | ███████████████ |
| Oct 2025 | 10 | 30% | 5 | 5 | ██████████ |
| Nov 2025 | 2 | 100% | 2 | 0 | ██ |
| Dec 2025 | 16 | 25% | 2 | 14 | ███████████████ |
| Jan 2026 | 12 | 17% | 5 | 7 | ███████████ |
| Feb 2026 | 19 | 42% | 6 | 13 | ██████████████████ |
| Mar 2026 | 14 | 43% | 5 | 9 | █████████████ |
| Apr 2026 | 21 | 38% | 8 | 13 | ████████████████████ |

The last four complete months averaged 16 articles a month against 10 in the first four (+65%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 24% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 8 | 12% |
| Canada | 2 | 3.0% |
| Australia | 1 | 1.5% |
| China | 1 | 1.5% |
| Democratic Republic of the Congo | 1 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| industrial metal market analysis | 10 | 23% | +67% |
| metal commodity trading trends | 6 | 14% | +0% |
| derivatives trading (futures, options) | 8 | 19% | +100% |
| market sentiment and investor behavior | 6 | 14% | +500% |
| commodity trading and price changes | 17 | 40% | +112% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 1 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Mar 2026 | [Copper Price Crash: 2 महीने में ₹400 सस्ता हुआ कॉपर, अब आई तेजी; खरीदें या नहीं, टारगेट क्या? 6 सवालों में…](https://www.jagran.com/business/commodity-copper-price-today-expert-analysis-targets-investment-40189123.html) | jagran.com | 6 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "copper price" --since 2026-01-01 --until 2026-04-30
prism-news trends "copper price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "copper price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "copper price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "copper price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Hedge Fund News](hedge-fund-news.md)
- [Dividend News](dividend-news.md)
- [Unemployment News](unemployment-news.md)
- [Retirement News](retirement-news.md)
