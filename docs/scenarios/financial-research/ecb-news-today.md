# ECB News Today: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ecb news today” · 20/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ecb-news-today.json](../../examples/scenarios/ecb-news-today.json).

**Question.** What did the news say about ecb between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="ECB"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,746 |
| Negative · neutral · positive | 55% · 12% · 33% |
| Critical (priority 7–9) | 62% (4,195 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (2,076 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | economy news: monetary policy changes |

## Twelve months of coverage

Monthly matching articles for `ECB` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 959 | 68% | 586 | 309 | █████████ |
| Jun 2025 | 1,403 | 67% | 757 | 524 | ██████████████ |
| Jul 2025 | 1,214 | 58% | 544 | 587 | ████████████ |
| Aug 2025 | 917 | 59% | 495 | 367 | █████████ |
| Sep 2025 | 1,154 | 65% | 570 | 490 | ███████████ |
| Oct 2025 | 963 | 64% | 462 | 450 | █████████ |
| Nov 2025 | 992 | 67% | 513 | 397 | ██████████ |
| Dec 2025 | 1,227 | 64% | 616 | 491 | ████████████ |
| Jan 2026 | 1,013 | 57% | 468 | 400 | ██████████ |
| Feb 2026 | 1,969 | 61% | 932 | 693 | ███████████████████ |
| Mar 2026 | 2,076 | 66% | 1,320 | 597 | ████████████████████ |
| Apr 2026 | 1,688 | 62% | 1,022 | 522 | ████████████████ |

The last four complete months averaged 1,686 articles a month against 1,123 in the first four (+50%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,010 | 15% |
| United Kingdom | 350 | 5.2% |
| Germany | 218 | 3.2% |
| Iran | 140 | 2.1% |
| France | 123 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: monetary policy changes | 731 | 16% | +59% |
| economy news: central bank interest rate decisions | 725 | 16% | +50% |
| foreign exchange (forex) rate fluctuations | 343 | 7.7% | +61% |
| economy news: inflation rate analysis | 790 | 18% | +90% |
| forex spot market trading | 175 | 3.9% | +207% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [ECB and BOE edge toward rate hikes as energy turmoil deepens- Moneycontrol.com](https://www.moneycontrol.com/news/business/economy/ecb-and-boe-edge-toward-rate-hikes-as-energy-turmoil-deepens-13905013.html) | moneycontrol.com | 8 | negative |
| 30 Apr 2026 | [ECB holds rates at 2% as inflation rises and eurozone growth slows](https://au.finance.yahoo.com/news/ecb-holds-rates-2-inflation-122126422.html) | au.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [ECB Holds the Line: Rates Stay Steady as Geopolitical Energy Risks Loom - EconoTimes](https://econotimes.com/ECB-Holds-the-Line-Rates-Stay-Steady-as-Geopolitical-Energy-Risks-Loom-1740495) | econotimes.com | 8 | positive |
| 30 Apr 2026 | [US growth falls short in Q1 2026; EU, UK hold rates as oil prices rise - Türkiye Today](https://www.turkiyetoday.com/business/us-growth-falls-short-in-q1-2026-eu-uk-hold-rates-as-oil-prices-rise-3219134) | turkiyetoday.com | 8 | negative |
| 30 Apr 2026 | [ECB holds interest rates unchanged at 2pc](https://www.independent.ie/business/irish/ecb-holds-interest-rates-unchanged-at-2pc/a2056425365.html) | independent.ie | 8 | negative |
| 30 Apr 2026 | [EZB-Zinsentscheidung: Leitzinsen im Euroraum bleiben konstant](https://kurier.at/wirtschaft/ezb-zinsentscheidung-leitzinsen-euroraum-konstant/403155581) | kurier.at | 8 | negative |
| 30 Apr 2026 | [The ECB avoids making a move but warns of "growing risks" of inflation due to the war](https://en.ara.cat/economy/the-ecb-avoids-making-move-despite-the-war-and-inflation_1_5723611.html) | en.ara.cat | 8 | negative |
| 30 Apr 2026 | [ECB Interest Rate Standoff: Geopolitical Fog Clouds the Path to Easing - EconoTimes](https://econotimes.com/ECB-Interest-Rate-Standoff-Geopolitical-Fog-Clouds-the-Path-to-Easing-1740469) | econotimes.com | 8 | negative |
| 30 Apr 2026 | [ECB, Bank of England Set to Hold Rates Unchanged Today](https://www.fxempire.com/news/article/ecb-bank-of-england-set-to-hold-rates-unchanged-today-1594864) | fxempire.com | 8 | negative |
| 30 Apr 2026 | [Euro Zone Inflation Surges Past ECB Target Amid Soaring Oil Prices](https://www.globalbankingandfinance.com/euro-zone-inflation-soars-ecb-target-oil-prices/) | globalbankingandfinance.com | 8 | negative |
| 30 Apr 2026 | [USD / CAD - Canadian Dollar trading aimlessly](https://www.baystreet.ca/forex_trader/3737/USD-CAD--Canadian-Dollar-trading-aimlessly) | baystreet.ca | 8 | negative |
| 29 Apr 2026 | [ECB to Hold Rates Steady, Signals Possible Hike Amid Inflation Fears](https://www.globalbankingandfinance.com/ecb-hold-rates-steady-keep-hikes-firmly-table/) | globalbankingandfinance.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ECB" --since 2026-01-01 --until 2026-04-30
prism-news trends "ECB" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ECB" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ECB", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ECB", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Commercial Real Estate News](commercial-real-estate-news.md)
- [Rupee News](rupee-news.md)
- [Stablecoin News](stablecoin-news.md)
- [ETF News](etf-news.md)
