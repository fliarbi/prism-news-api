# Nifty News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nifty news” · 14,800/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nifty-news.json](../../examples/scenarios/nifty-news.json).

**Question.** What did the news say about nifty between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="nifty"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 16,582 |
| Negative · neutral · positive | 37% · 1.1% · 62% |
| Critical (priority 7–9) | 34% (5,621 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (6,151 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | asian financial market developments |

## Twelve months of coverage

Monthly matching articles for `nifty` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,703 | 34% | 813 | 1,889 | █████████ |
| Jun 2025 | 2,628 | 33% | 719 | 1,903 | █████████ |
| Jul 2025 | 3,467 | 26% | 1,287 | 2,165 | ███████████ |
| Aug 2025 | 4,643 | 34% | 1,531 | 3,090 | ███████████████ |
| Sep 2025 | 3,928 | 31% | 961 | 2,921 | █████████████ |
| Oct 2025 | 2,327 | 26% | 422 | 1,889 | ████████ |
| Nov 2025 | 2,357 | 29% | 640 | 1,688 | ████████ |
| Dec 2025 | 2,349 | 31% | 787 | 1,544 | ████████ |
| Jan 2026 | 2,566 | 38% | 986 | 1,540 | ████████ |
| Feb 2026 | 6,151 | 22% | 1,595 | 4,427 | ████████████████████ |
| Mar 2026 | 3,675 | 46% | 2,026 | 1,635 | ████████████ |
| Apr 2026 | 4,190 | 39% | 1,579 | 2,588 | ██████████████ |

The last four complete months averaged 4,146 articles a month against 3,360 in the first four (+23%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,264 | 14% |
| India | 2,234 | 13% |
| Iran | 664 | 4.0% |
| China | 358 | 2.2% |
| Japan | 197 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| asian financial market developments | 3,056 | 24% | +44% |
| market volatility indicators | 3,683 | 28% | +55% |
| emerging markets economic updates | 2,209 | 17% | +61% |
| stock market index composition | 3,505 | 27% | +46% |
| international/emerging markets stocks | 3,477 | 27% | +53% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Sensex, Nifty end 7 per cent higher in April](https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-end-7-per-cent-higher-in-april/article70926006.ece) | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty fall amid FII selling and surge in crude oil prices](https://www.newindianexpress.com/business/2026/Apr/30/sensex-nifty-fall-amid-fii-selling-and-surge-in-crude-oil-prices) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty end lower amid rising crude oil prices](https://www.ibtimes.co.in/sensex-nifty-end-lower-amid-rising-crude-oil-prices-901655) | ibtimes.co.in | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty Fall Nearly 1% Today: Oil Price Surge Weighs on Sentiment - Business League](https://www.businessleague.in/sensex-nifty-fall-nearly-1-today-oil-price-surge-weighs-on-sentiment/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Nifty 50 Outlook April 30: Bullish Flag vs Strait of Hormuz Risks](https://www.republicworld.com/business/nifty-50-technical-analysis-bullish-flag-breakout-hormuz-oil-risk) | republicworld.com | 8 | negative |
| 30 Apr 2026 | [6 reasons why markets are falling today: Sensex nosedives 1,100 points, Crude spikes to $125](https://www.financialexpress.com/market/6-reasons-why-markets-are-falling-today-sensex-nosedives-1100-points-nifty-plunges-to-23900-4222994/) | financialexpress.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy: Nagaraj Shetti recommends Time Technoplast, Gujarat Ambuja Exports shares to buy \| Stock…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-nagaraj-shetti-recommends-time-technoplast-gujarat-ambuja-exports-shares-to-buy-11777528414947.html) | livemint.com | 8 | negative |
| 30 Apr 2026 | [Why Is Stock Market Down Today, April 30, 2026? \| LatestLY](https://www.latestly.com/business/why-is-stock-market-down-today-april-30-2026-7412906.html) | latestly.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy or sell: Osho Krishan of Angel One suggests buying Chennai Petroleum Corp, Bharti Airtel…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-or-sell-osho-krishan-of-angel-one-suggests-buying-chennai-petroleum-corp-bharti-airtel-shares-to-buy-11777522637744.html) | livemint.com | 8 | negative |
| 29 Apr 2026 | [Market outlook amid assembly election exit polls 2026 results; Sensex, Nifty levels to watch tomorrow -…](https://www.businesstoday.in/markets/stocks/story/market-outlook-amid-assembly-election-exit-polls-2026-results-sensex-nifty-levels-to-watch-tomorrow-528084-2026-04-29) | businesstoday.in | 8 | negative |
| 29 Apr 2026 | [Stock Market Today: Sensex, Nifty End Higher Amid Global Uncertainty \| 📰 LatestLY](https://www.latestly.com/india/news/stock-market-today-sensex-nifty-end-higher-amid-global-uncertainty-7412073.html) | latestly.com | 8 | positive |
| 29 Apr 2026 | [Sensex, Nifty end higher amid global uncertainty](https://www.ibtimes.co.in/sensex-nifty-end-higher-amid-global-uncertainty-901626) | ibtimes.co.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "nifty" --since 2026-01-01 --until 2026-04-30
prism-news trends "nifty" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "nifty" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "nifty", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "nifty", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [IPO News](ipo-news.md)
- [RBI News](rbi-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Mortgage Rates News](mortgage-rates-news.md)
