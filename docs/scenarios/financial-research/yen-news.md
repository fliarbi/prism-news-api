# Yen News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “yen news” · 210/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [yen-news.json](../../examples/scenarios/yen-news.json).

**Question.** What did the news say about yen between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="yen"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,249 |
| Negative · neutral · positive | 39% · 2.0% · 59% |
| Critical (priority 7–9) | 50% (5,607 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (4,545 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | emerging markets economic updates |

## Twelve months of coverage

Monthly matching articles for `yen` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,482 | 53% | 1,098 | 1,307 | ███████████ |
| Jun 2025 | 1,685 | 43% | 622 | 1,012 | ███████ |
| Jul 2025 | 3,287 | 55% | 1,725 | 1,427 | ██████████████ |
| Aug 2025 | 4,545 | 35% | 1,449 | 3,010 | ████████████████████ |
| Sep 2025 | 2,232 | 61% | 1,067 | 1,101 | ██████████ |
| Oct 2025 | 1,989 | 54% | 730 | 1,223 | █████████ |
| Nov 2025 | 2,057 | 47% | 795 | 1,247 | █████████ |
| Dec 2025 | 2,157 | 52% | 920 | 1,177 | █████████ |
| Jan 2026 | 2,575 | 54% | 1,116 | 1,415 | ███████████ |
| Feb 2026 | 2,873 | 54% | 1,101 | 1,708 | █████████████ |
| Mar 2026 | 2,646 | 46% | 977 | 1,613 | ████████████ |
| Apr 2026 | 3,155 | 46% | 1,146 | 1,938 | ██████████████ |

The last four complete months averaged 2,812 articles a month against 3,000 in the first four (-6%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 72% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 3,165 | 28% |
| Japan | 901 | 8.0% |
| India | 863 | 7.7% |
| United Kingdom | 484 | 4.3% |
| China | 240 | 2.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| emerging markets economic updates | 545 | 7.6% | +51% |
| foreign exchange (forex) rate fluctuations | 748 | 10% | +37% |
| asian financial market developments | 383 | 5.3% | +94% |
| forex market volatility analysis | 202 | 2.8% | +226% |
| forex spot market trading | 189 | 2.6% | +125% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [USD/JPY Caves in On Aggressive BoJ Posture. But Will It Last?](https://www.investingcube.com/forex/usd-jpy-caves-in-on-aggressive-boj-posture-but-will-it-last/) | investingcube.com | 8 | negative |
| 30 Apr 2026 | [Dollar drops versus yen as Japanese officials signal possible intervention](https://www.zawya.com/en/economy/global/dollar-drops-versus-yen-as-japanese-officials-signal-possible-intervention-vfyga57j) | zawya.com | 8 | negative |
| 30 Apr 2026 | [Yen crosses key threshold, but don’t count on intervention just yet \| Mint](https://www.livemint.com/global/yen-crosses-key-threshold-but-don-t-count-on-intervention-just-yet-11777540086587.html) | livemint.com | 8 | negative |
| 30 Apr 2026 | [Privacy in the AI era is possible, says Proton's CEO, but one thing keeps him up at night](https://www.zdnet.com/article/proton-ceo-andy-yen-interview-ai-privacy-security-semafor/) | zdnet.com | 8 | positive |
| 28 Apr 2026 | [The BoJ will continue raising rates in Japan, but the pace is highly uncertain](https://www.oxfordeconomics.com/resource/the-boj-will-continue-raising-rates-in-japan-but-the-pace-is-highly-uncertain/) | oxfordeconomics.com | 8 | positive |
| 28 Apr 2026 | [USD/JPY: Yen rebound seen short-lived – MUFG](https://bitcoinethereumnews.com/finance/usd-jpy-yen-rebound-seen-short-lived-mufg/) | bitcoinethereumnews.com | 8 | negative |
| 28 Apr 2026 | [Dollar picks up, yen steady as central banks in focus after BOJ holds](https://www.zawya.com/en/business/currencies/dollar-picks-up-yen-steady-as-central-banks-in-focus-after-boj-holds-fyksfn71) | zawya.com | 8 | negative |
| 28 Apr 2026 | [Yen steady, dollar edges higher as central banks in focus after BOJ holds](https://www.zawya.com/en/economy/global/yen-steady-dollar-edges-higher-as-central-banks-in-focus-after-boj-holds-uknknsl7) | zawya.com | 8 | negative |
| 28 Apr 2026 | [Global Markets \| Nikkei closes off record high, JGBs wobble on BOJ's hawkish hold](https://economictimes.indiatimes.com/markets/us-stocks/news/updated-global-markets-nikkei-closes-off-record-high-jgbs-wobble-on-bojs-hawkish-hold/articleshow/130574835.cms) | economictimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [BTC remains under pressure after three Bank of Japan (BoJ) members call for a rate hike](https://www.coindesk.com/markets/2026/04/28/three-bank-of-japan-members-call-for-a-rate-hike-yen-rises-while-bitcoin-falls) | coindesk.com | 8 | negative |
| 28 Apr 2026 | [Yen steady as BOJ kicks off big week for central banks](https://www.zawya.com/en/business/currencies/yen-steady-as-boj-kicks-off-big-week-for-central-banks-y7t0v8qh) | zawya.com | 8 | negative |
| 23 Apr 2026 | [GBP/JPY Price Forecast: Yen gains on intervention fears, but uptrend remains intact](https://bitcoinethereumnews.com/finance/gbp-jpy-price-forecast-yen-gains-on-intervention-fears-but-uptrend-remains-intact/) | bitcoinethereumnews.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "yen" --since 2026-01-01 --until 2026-04-30
prism-news trends "yen" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "yen" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "yen", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "yen", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Retirement News](retirement-news.md)
- [Treasury Yields News](treasury-yields-news.md)
- [Market Crash News](market-crash-news.md)
- [Tax News Today](tax-news-today.md)
