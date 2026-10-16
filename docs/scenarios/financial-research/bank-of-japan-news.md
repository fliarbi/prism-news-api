# Bank of Japan News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bank of japan news” · 880/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [bank-of-japan-news.json](../../examples/scenarios/bank-of-japan-news.json).

**Question.** What did the news say about bank of japan between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="bank of japan"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,686 |
| Negative · neutral · positive | 71% · 4.5% · 24% |
| Critical (priority 7–9) | 77% (1,303 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (1,025 articles) |
| Most-reported country | Japan (29% of matches) |
| Strongest theme by lift | emerging markets economic updates |

## Twelve months of coverage

Monthly matching articles for `bank of japan` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 213 | 71% | 160 | 50 | ████ |
| Jun 2025 | 215 | 72% | 152 | 55 | ████ |
| Jul 2025 | 210 | 64% | 160 | 46 | ████ |
| Aug 2025 | 164 | 73% | 110 | 51 | ███ |
| Sep 2025 | 272 | 75% | 173 | 80 | █████ |
| Oct 2025 | 317 | 82% | 186 | 121 | ██████ |
| Nov 2025 | 258 | 81% | 195 | 62 | █████ |
| Dec 2025 | 1,025 | 74% | 711 | 301 | ████████████████████ |
| Jan 2026 | 270 | 76% | 195 | 70 | █████ |
| Feb 2026 | 345 | 78% | 231 | 107 | ███████ |
| Mar 2026 | 477 | 79% | 355 | 96 | █████████ |
| Apr 2026 | 594 | 76% | 424 | 133 | ████████████ |

The last four complete months averaged 422 articles a month against 200 in the first four (+110%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| Japan | 497 | 29% |
| United States | 309 | 18% |
| Iran | 56 | 3.3% |
| Singapore | 34 | 2.0% |
| China | 31 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| emerging markets economic updates | 308 | 22% | -1% |
| foreign exchange (forex) rate fluctuations | 463 | 34% | -6% |
| asian financial market developments | 196 | 14% | +10% |
| central bank monetary policy announcements | 413 | 30% | -24% |
| economy news: monetary policy changes | 351 | 25% | +5% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [The BoJ will continue raising rates in Japan, but the pace is highly uncertain](https://www.oxfordeconomics.com/resource/the-boj-will-continue-raising-rates-in-japan-but-the-pace-is-highly-uncertain/) | oxfordeconomics.com | 8 | positive |
| 28 Apr 2026 | [USD/JPY steadies after hawkish BoJ as Middle East tensions lift Dollar](https://bitcoinethereumnews.com/finance/usd-jpy-steadies-after-hawkish-boj-as-middle-east-tensions-lift-dollar/) | bitcoinethereumnews.com | 8 | negative |
| 28 Apr 2026 | [BOJ: Gradual tightening with higher inflation risks – UOB](https://bitcoinethereumnews.com/finance/boj-gradual-tightening-with-higher-inflation-risks-uob/) | bitcoinethereumnews.com | 8 | neutral |
| 28 Apr 2026 | [USD/JPY: BoJ split vote lifts normalization risks – BNY](https://bitcoinethereumnews.com/finance/usd-jpy-boj-split-vote-lifts-normalization-risks-bny/) | bitcoinethereumnews.com | 8 | negative |
| 28 Apr 2026 | [BOJ Governor Kazuo Ueda Hints at Rate Hike as Inflation Pressures Build - EconoTimes](https://econotimes.com/BOJ-Governor-Kazuo-Ueda-Hints-at-Rate-Hike-as-Inflation-Pressures-Build-1740205) | econotimes.com | 8 | negative |
| 28 Apr 2026 | [Gold Prices Drop Amid Iran War Concerns, Rising Oil Costs, and Hawkish Central Bank Signals - EconoTimes](https://econotimes.com/Gold-Prices-Drop-Amid-Iran-War-Concerns-Rising-Oil-Costs-and-Hawkish-Central-Bank-Signals-1740198) | econotimes.com | 8 | positive |
| 28 Apr 2026 | [BTC remains under pressure after three Bank of Japan (BoJ) members call for a rate hike](https://www.coindesk.com/markets/2026/04/28/three-bank-of-japan-members-call-for-a-rate-hike-yen-rises-while-bitcoin-falls) | coindesk.com | 8 | negative |
| 28 Apr 2026 | [Yen Strengthens as BOJ Signals Rate Hikes; Asian Currencies Slip Ahead of Fed Meeting - EconoTimes](https://econotimes.com/Yen-Strengthens-as-BOJ-Signals-Rate-Hikes-Asian-Currencies-Slip-Ahead-of-Fed-Meeting-1740180) | econotimes.com | 8 | negative |
| 28 Apr 2026 | [Asian Stocks Mixed as BOJ Holds Rates, Oil Prices and Fed Outlook Weigh on Markets - EconoTimes](https://econotimes.com/Asian-Stocks-Mixed-as-BOJ-Holds-Rates-Oil-Prices-and-Fed-Outlook-Weigh-on-Markets-1740179) | econotimes.com | 8 | positive |
| 28 Apr 2026 | [USD/JPY softens on hawkish BoJ hold \| FXCM Markets](https://www.fxcm.com/markets/insights/usd-jpy-softens-on-hawkish-boj-hold/) | fxcm.com | 8 | negative |
| 28 Apr 2026 | [Japan's central bank holds its key rate steady amid worries about the Iran war and energy prices](https://apnews.com/article/japan-boj-rates-iran-30c80da1e1f2e96b70fa368d7f58cc19) | apnews.com | 8 | negative |
| 28 Apr 2026 | [BOJ keeps rates steady but hawkish split points to June hike](https://www.businesstimes.com.sg/companies-markets/banking-finance/boj-keeps-rates-steady-3-board-members-dissent-call-hike) | businesstimes.com.sg | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "bank of japan" --since 2026-01-01 --until 2026-04-30
prism-news trends "bank of japan" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "bank of japan" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "bank of japan", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "bank of japan", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Nasdaq News](nasdaq-news.md)
- [Recession News](recession-news.md)
- [US Dollar News](us-dollar-news.md)
- [Crude Oil Price News](crude-oil-price-news.md)
