# Rupee News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rupee news” · 2,400/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rupee-news.json](../../examples/scenarios/rupee-news.json).

**Question.** What did the news say about rupee between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="rupee"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,820 |
| Negative · neutral · positive | 70% · 0.9% · 29% |
| Critical (priority 7–9) | 63% (4,261 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,838 articles) |
| Most-reported country | India (30% of matches) |
| Strongest theme by lift | emerging markets economic updates |

## Twelve months of coverage

Monthly matching articles for `rupee` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 594 | 59% | 304 | 285 | ████ |
| Jun 2025 | 563 | 51% | 335 | 224 | ████ |
| Jul 2025 | 744 | 50% | 465 | 270 | █████ |
| Aug 2025 | 1,251 | 55% | 758 | 464 | █████████ |
| Sep 2025 | 1,170 | 62% | 726 | 425 | ████████ |
| Oct 2025 | 711 | 56% | 350 | 353 | █████ |
| Nov 2025 | 761 | 52% | 479 | 277 | █████ |
| Dec 2025 | 1,804 | 65% | 1,227 | 539 | █████████████ |
| Jan 2026 | 1,076 | 67% | 727 | 338 | ████████ |
| Feb 2026 | 961 | 56% | 411 | 536 | ███████ |
| Mar 2026 | 1,945 | 74% | 1,492 | 435 | ██████████████ |
| Apr 2026 | 2,838 | 55% | 2,129 | 681 | ████████████████████ |

The last four complete months averaged 1,705 articles a month against 788 in the first four (+116%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 59% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 2,074 | 30% |
| United States | 1,131 | 17% |
| Iran | 305 | 4.5% |
| China | 64 | 0.9% |
| Singapore | 50 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| emerging markets economic updates | 1,756 | 34% | +18% |
| foreign exchange (forex) rate fluctuations | 2,206 | 42% | +22% |
| asian financial market developments | 1,328 | 25% | +18% |
| forex spot market trading | 659 | 13% | +51% |
| forex market volatility analysis | 491 | 9.4% | +69% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Rupee Sinks to Record Low 95.23: Oil Price Spike and Fed Stance Crush INR - Business League](https://www.businessleague.in/rupee-sinks-to-record-low-95-23-oil-price-spike-and-fed-stance-crush-inr/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Rupee hits record low: Currency slips to 95.34 against US dollar as crude oil prices tops $120 per barrel -…](https://timesofindia.indiatimes.com/business/india-business/rupee-hits-record-low-of-95-20-against-us-dollar-slides-32-paise-in-early-trade/articleshow/130623920.cms) | timesofindia.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee closes at new low of 94.85 as West Asia peace talks stall - The Times of India](https://timesofindia.indiatimes.com/business/india-business/rupee-closes-at-new-low-of-94-85-as-west-asia-peace-talks-stall/articleshow/130620522.cms) | timesofindia.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee closes at new low of 94.85 as West Asia peace talks stall - Times of India](https://timesofindia.indiatimes.com/articleshowprint/130620522.cms) | timesofindia.indiatimes.com | 8 | negative |
| 29 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.deccanherald.com/business/markets/rupee-settles-at-all-time-closing-low-of-9486-against-us-dollar-3985079) | deccanherald.com | 8 | negative |
| 29 Apr 2026 | [Why rupee is falling in April 2026, more volatility ahead? - BusinessToday](https://www.businesstoday.in/markets/market-commentary/story/why-rupee-is-falling-in-april-2026-more-volatility-ahead-528027-2026-04-29) | businesstoday.in | 8 | negative |
| 28 Apr 2026 | [New Low for Rupee: Why the Indian Currency is Falling Against USD as Global Oil Crisis Deepens](https://www.republicworld.com/business/indian-rupee-hits-all-time-low-vs-usd-april-2026-oil-prices) | republicworld.com | 8 | negative |
| 27 Apr 2026 | [Rupee falls for fifth straight session as oil trades over $100 – Iran conflict weighs on currency](https://www.financialexpress.com/market/rupee-falls-for-fifth-straight-session-as-oil-trades-over-100-iran-conflict-weighs-on-currency-4219372/) | financialexpress.com | 8 | negative |
| 27 Apr 2026 | [Dollar demand, rising oil prices drag Rupee lower to 94.27 - Connected to India News I Singapore l UAE l UK…](https://www.connectedtoindia.com/dollar-demand-rising-oil-prices-drag-rupee-lower-to-94-27/) | connectedtoindia.com | 8 | negative |
| 25 Apr 2026 | [Rupee vs dollar: India faces currency dilemma amid weak manufacturing](https://www.deccanherald.com/opinion/the-rupees-dilemma-pride-vs-practicality-3981138) | deccanherald.com | 8 | negative |
| 24 Apr 2026 | [INDIA RUPEE-Rupee tracks Asian peers lower but state-run banks' dollar sales cushion](https://bfsi.economictimes.indiatimes.com/news/industry/india-rupee-rupee-tracks-asian-peers-lower-but-state-run-banks-dollar-sales-cushion/130485421) | bfsi.economictimes.indiatimes.com | 8 | negative |
| 24 Apr 2026 | [USD/INR: 5-day Gains Beckon on Escalating Geopolitical Tensions](https://www.investingcube.com/forex/usd-inr-5-day-gains-beckon-on-escalating-geopolitical-tensions/) | investingcube.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "rupee" --since 2026-01-01 --until 2026-04-30
prism-news trends "rupee" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "rupee" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "rupee", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "rupee", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Repo Rate News](repo-rate-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
- [ECB News Today](ecb-news-today.md)
- [Stablecoin News](stablecoin-news.md)
