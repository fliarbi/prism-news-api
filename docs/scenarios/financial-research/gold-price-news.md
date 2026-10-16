# Gold Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gold price news” · 22,200/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gold-price-news.json](../../examples/scenarios/gold-price-news.json).

**Question.** What did the news say about gold price between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="gold price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,439 |
| Negative · neutral · positive | 39% · 2.0% · 59% |
| Critical (priority 7–9) | 14% (350 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (746 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | derivatives trading (futures, options) |

## Twelve months of coverage

Monthly matching articles for `gold price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 523 | 28% | 278 | 240 | ██████████████ |
| Jun 2025 | 375 | 23% | 174 | 199 | ██████████ |
| Jul 2025 | 331 | 22% | 111 | 217 | █████████ |
| Aug 2025 | 362 | 22% | 128 | 222 | ██████████ |
| Sep 2025 | 480 | 17% | 92 | 384 | █████████████ |
| Oct 2025 | 651 | 18% | 204 | 420 | █████████████████ |
| Nov 2025 | 341 | 21% | 114 | 216 | █████████ |
| Dec 2025 | 382 | 15% | 110 | 268 | ██████████ |
| Jan 2026 | 520 | 14% | 166 | 347 | ██████████████ |
| Feb 2026 | 569 | 14% | 185 | 376 | ███████████████ |
| Mar 2026 | 604 | 16% | 286 | 306 | ████████████████ |
| Apr 2026 | 746 | 13% | 316 | 407 | ████████████████████ |

The last four complete months averaged 610 articles a month against 398 in the first four (+53%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 391 | 16% |
| India | 334 | 14% |
| Iran | 97 | 4.0% |
| Pakistan | 41 | 1.7% |
| China | 30 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| derivatives trading (futures, options) | 736 | 37% | +55% |
| commodity trading and price changes | 1,251 | 63% | +29% |
| precious metal spot prices | 266 | 13% | -7% |
| market sentiment and investor behavior | 360 | 18% | +118% |
| precious metals trading trends (gold, silver, platinum) | 601 | 30% | -27% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [Gold Price Today 15 April 2026: Yellow Metal Retraces from One-Month High as US-Iran Peace Talks Loom -…](https://www.businessleague.in/gold-price-today-15-april-2026-yellow-metal-retraces-from-one-month-high-as-us-iran-peace-talks-loom/) | businessleague.in | 8 | negative |
| 13 Apr 2026 | [Gold Buyers Hold Back as US-Iran Deadlock and Hawkish Fed Outlook Strengthen Dollar](https://www.bizzbuzz.news/wealth/gold/gold-price-xauusd-us-iran-tensions-analysis-1388867) | bizzbuzz.news | 8 | negative |
| 7 Apr 2026 | [20-day EMA acts as key barrier ahead of Trump’s deadline to Iran](https://bitcoinethereumnews.com/finance/20-day-ema-acts-as-key-barrier-ahead-of-trumps-deadline-to-iran/) | bitcoinethereumnews.com | 8 | neutral |
| 21 Mar 2026 | [Gold Price Crash Accelerates as SPDR GLD ETF Outflows Jump: What Next?](https://www.banklesstimes.com/articles/2026/03/21/gold-price-crash-accelerates-as-spdr-gld-etf-outflows-jump-what-next/) | banklesstimes.com | 8 | negative |
| 22 Feb 2026 | [High-Grade Near-Surface Graphite Intersected at Millennium](https://investingnews.com/high-grade-near-surface-graphite-intersected-at-millennium/) | investingnews.com | 8 | negative |
| 10 Feb 2026 | [Canadian Bank Ups 2026 Gold Forecast to $6,000](https://www.linkedin.com/pulse/canadian-bank-ups-2026-gold-forecast-6000-money-metals-3rv7e) | linkedin.com | 8 | positive |
| 24 Jan 2026 | [Gold Price Forecast After Hitting $5K: Brace for a Short-Term Reversal \| BanklessTimes](https://www.banklesstimes.com/articles/2026/01/24/gold-price-forecast-after-hitting-5k-brace-for-a-short-term-reversal/) | banklesstimes.com | 8 | negative |
| 25 Apr 2026 | [Madhya Pradesh Gold Prices 18, 22 and 24 Carat Today: MP में सोने का बड़ा उलटफेर! कमाई का मौका या नुकसान का…](https://indianews.in/business/gold-price-today-25-april-2026-in-madhya-pradesh-bhopal-indore-gwalior-jabalpur-ujjain-sagar-satna-rewa-908531/) | indianews.in | 7 | negative |
| 20 Apr 2026 | [AXCAP VENTURES INC. (CVE:AXCP) \| Roxmore Resources dévoile des perspectives économiques positives pour le…](https://www.webdisclosure.com/article/roxmore-resources-devoile-des-perspectives-economiques-positives-pour-le-projet-aurifere-de-converse-eQPCNVb1Uka) | webdisclosure.com | 7 | positive |
| 19 Apr 2026 | [Barrick Mining Aktie: Neue Investitionsfelder identifiziert](https://www.boerse-express.com/news/articles/barrick-mining-aktie-neue-investitionsfelder-identifiziert-894258) | boerse-express.com | 7 | negative |
| 18 Apr 2026 | [Gold price increased in India today, check latest rates in top cities](https://kalingatv.com/business/gold-price-increased-in-india-today-check-latest-rates-in-top-cities-5/) | kalingatv.com | 7 | positive |
| 14 Apr 2026 | [Barrick Mining Aktie: Gute Nachrichten begeistern!](https://www.boerse-express.com/news/articles/barrick-mining-aktie-gute-nachrichten-begeistern-892002) | boerse-express.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "gold price" --since 2026-01-01 --until 2026-04-30
prism-news trends "gold price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "gold price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "gold price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "gold price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Crypto News](crypto-news.md)
- [GST News](gst-news.md)
- [Housing Market News](housing-market-news.md)
- [IPO News](ipo-news.md)
