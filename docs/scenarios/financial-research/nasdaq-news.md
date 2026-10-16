# Nasdaq News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nasdaq news” · 1,600/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nasdaq-news.json](../../examples/scenarios/nasdaq-news.json).

**Question.** What did the news say about nasdaq between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="nasdaq"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 158,036 |
| Negative · neutral · positive | 18% · 2.6% · 79% |
| Critical (priority 7–9) | 33% (52,308 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (56,082 articles) |
| Most-reported country | United States (39% of matches) |
| Strongest theme by lift | options trading for stocks |

## Twelve months of coverage

Monthly matching articles for `nasdaq` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18,282 | 45% | 3,794 | 14,207 | ███████ |
| Jun 2025 | 19,345 | 33% | 3,043 | 16,074 | ███████ |
| Jul 2025 | 12,174 | 56% | 2,839 | 9,072 | ████ |
| Aug 2025 | 18,250 | 47% | 3,388 | 14,602 | ███████ |
| Sep 2025 | 25,653 | 43% | 3,883 | 21,350 | █████████ |
| Oct 2025 | 22,072 | 52% | 4,485 | 16,136 | ████████ |
| Nov 2025 | 22,495 | 55% | 5,389 | 16,460 | ████████ |
| Dec 2025 | 21,119 | 50% | 4,543 | 15,563 | ████████ |
| Jan 2026 | 31,990 | 31% | 4,648 | 26,576 | ███████████ |
| Feb 2026 | 36,886 | 35% | 6,115 | 29,919 | █████████████ |
| Mar 2026 | 33,078 | 41% | 7,737 | 24,450 | ████████████ |
| Apr 2026 | 56,082 | 28% | 10,725 | 43,764 | ████████████████████ |

The last four complete months averaged 39,509 articles a month against 17,013 in the first four (+132%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 61,352 | 39% |
| China | 2,963 | 1.9% |
| Canada | 1,201 | 0.8% |
| United Kingdom | 1,186 | 0.8% |
| Iran | 940 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| options trading for stocks | 4,260 | 3.9% | +85% |
| corporate governance and board decisions | 2,514 | 2.3% | +140% |
| market volatility indicators | 3,921 | 3.5% | +14% |
| stock splits and reverse splits | 2,373 | 2.1% | +202% |
| initial public offerings (ipos) | 4,121 | 3.7% | +69% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 13 Apr 2026 | [Elon Musk Questions COVID-19 Vaccine Dosage As He Recounts Near-Hospitalization Ordeal: 'Felt Like I Was](https://www.benzinga.com/news/health-care/26/04/51773724/elon-musk-questions-covid-19-vaccine-dosage-says-it-was-obviously-too-high) | benzinga.com | 9 | negative |
| 8 Apr 2026 | [Oil falls below $100, Dow futures soar 1,000 points on Iran ceasefire deal](https://qz.com/trump-iran-war-ceasefire-deal-oil-prices-stocks-markets) ⚠ | qz.com | 9 | negative |
| 31 Mar 2026 | [Trump reportedly willing to end Iran war without reopening the Strait of Hormuz](https://sherwood.news/markets/trump-reportedly-willing-end-iran-war-without-reopening-strait-of-hormuz/) | sherwood.news | 9 | negative |
| 30 Apr 2026 | [Evernorth XRP names OpenAI CFO to its board](https://crypto.news/evernorth-xrp-names-openai-cfo-to-its-board/) | crypto.news | 8 | positive |
| 30 Apr 2026 | [Apple Stock Pops On Strong Q3 Guidance: Details - Apple (NASDAQ:AAPL)](https://www.benzinga.com/trading-ideas/movers/26/04/52201788/apple-stock-pops-on-strong-q3-guidance-details) | benzinga.com | 8 | positive |
| 30 Apr 2026 | [XMax puts AWS-hosted AI platform online, opens new investor site](https://www.stocktitan.net/news/XWIN/x-max-inc-launches-ai-inference-platform-and-new-ai-and-corporate-c91bdl3n0r2r.html) | stocktitan.net | 8 | positive |
| 30 Apr 2026 | [Apple (AAPL) Q2 FY26 sales, earnings beat estimates amid strong iPhone sales](https://news.alphastreet.com/apple-aapl-q2-fy26-sales-earnings-beat-estimates-amid-strong-iphone-sales/) | news.alphastreet.com | 8 | positive |
| 30 Apr 2026 | [US stocks today: US market ends higher, S&P 500, Nasdaq notch biggest monthly gains in years](https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-market-ends-higher-sp-500-nasdaq-notch-biggest-monthly-gains-in-years/articleshow/130651806.cms) | economictimes.indiatimes.com | 8 | positive |
| 30 Apr 2026 | [Meta Seeks $25 Billion Bond Sale As AI Spending Soars](https://finance.yahoo.com/markets/stocks/articles/meta-seeks-25-billion-bond-190420800.html) | finance.yahoo.com | 8 | positive |
| 30 Apr 2026 | [Why Is Opendoor Technologies Stock Sliding On Thursday? - Opendoor Technologies (NASDAQ:OPEN)](https://www.benzinga.com/trading-ideas/movers/26/04/52186563/why-is-opendoor-technologies-stock-sliding-on-thursday) | benzinga.com | 8 | negative |
| 30 Apr 2026 | [Alphabet Soars, Meta Sinks As Big Tech Splits — ETFs Let You Pick The Right Side - Alphabet (NASDAQ:GOOGL](https://www.benzinga.com/etfs/sector-etfs/26/04/52178697/alphabet-soars-meta-sinks-as-big-tech-splits-etfs-let-you-pick-the-right-side) | benzinga.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "nasdaq" --since 2026-01-01 --until 2026-04-30
prism-news trends "nasdaq" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "nasdaq" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "nasdaq", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "nasdaq", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Inflation News](inflation-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
- [Recession News](recession-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
