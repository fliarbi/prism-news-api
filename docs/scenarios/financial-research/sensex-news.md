# Sensex News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sensex news” · 6,600/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [sensex-news.json](../../examples/scenarios/sensex-news.json).

**Question.** What did the news say about sensex between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="sensex"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,978 |
| Negative · neutral · positive | 47% · 0.8% · 52% |
| Critical (priority 7–9) | 41% (4,923 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,814 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | asian financial market developments |

## Twelve months of coverage

Monthly matching articles for `sensex` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,234 | 36% | 715 | 1,514 | ████████████ |
| Jun 2025 | 2,068 | 32% | 581 | 1,481 | ███████████ |
| Jul 2025 | 2,524 | 28% | 1,030 | 1,483 | █████████████ |
| Aug 2025 | 3,515 | 39% | 1,241 | 2,256 | ██████████████████ |
| Sep 2025 | 2,912 | 39% | 938 | 1,928 | ███████████████ |
| Oct 2025 | 1,906 | 27% | 402 | 1,496 | ██████████ |
| Nov 2025 | 1,924 | 28% | 604 | 1,316 | ██████████ |
| Dec 2025 | 1,982 | 30% | 800 | 1,170 | ██████████ |
| Jan 2026 | 2,059 | 43% | 1,017 | 1,029 | ███████████ |
| Feb 2026 | 3,073 | 30% | 1,015 | 2,006 | ████████████████ |
| Mar 2026 | 3,032 | 49% | 1,942 | 1,084 | ████████████████ |
| Apr 2026 | 3,814 | 42% | 1,625 | 2,161 | ████████████████████ |

The last four complete months averaged 2,994 articles a month against 2,585 in the first four (+16%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,172 | 18% |
| India | 1,960 | 16% |
| Iran | 667 | 5.6% |
| China | 393 | 3.3% |
| Japan | 219 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| asian financial market developments | 2,974 | 32% | +37% |
| market volatility indicators | 3,643 | 39% | +62% |
| emerging markets economic updates | 2,242 | 24% | +44% |
| stock market index composition | 3,411 | 37% | +50% |
| international/emerging markets stocks | 3,101 | 33% | +45% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Sensex, Nifty end 7 per cent higher in April](https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-end-7-per-cent-higher-in-april/article70926006.ece) | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty fall amid FII selling and surge in crude oil prices](https://www.newindianexpress.com/business/2026/Apr/30/sensex-nifty-fall-amid-fii-selling-and-surge-in-crude-oil-prices) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [Why is the stock market closed on May 1? See NSE BSE Holiday List 2026](https://www.theweek.in/news/biz-tech/2026/04/30/indian-stock-market-holiday-may-1-sensex-nifty.html) | theweek.in | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty end lower amid rising crude oil prices](https://www.ibtimes.co.in/sensex-nifty-end-lower-amid-rising-crude-oil-prices-901655) | ibtimes.co.in | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty Fall Nearly 1% Today: Oil Price Surge Weighs on Sentiment - Business League](https://www.businessleague.in/sensex-nifty-fall-nearly-1-today-oil-price-surge-weighs-on-sentiment/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Record High Oil, All-Time Low Rupee Batters Sensex, Nifty; IndiGo, Eternal Top Losers Chart](https://www.freepressjournal.in/business/record-high-oil-rupee-plunge-batter-sensex-nifty-indigo-eternal-top-losers-chart) | freepressjournal.in | 8 | negative |
| 30 Apr 2026 | [6 reasons why markets are falling today: Sensex nosedives 1,100 points, Crude spikes to $125](https://www.financialexpress.com/market/6-reasons-why-markets-are-falling-today-sensex-nosedives-1100-points-nifty-plunges-to-23900-4222994/) | financialexpress.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy: Nagaraj Shetti recommends Time Technoplast, Gujarat Ambuja Exports shares to buy \| Stock…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-nagaraj-shetti-recommends-time-technoplast-gujarat-ambuja-exports-shares-to-buy-11777528414947.html) | livemint.com | 8 | negative |
| 30 Apr 2026 | [Why Is Stock Market Down Today, April 30, 2026? \| LatestLY](https://www.latestly.com/business/why-is-stock-market-down-today-april-30-2026-7412906.html) | latestly.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy or sell: Osho Krishan of Angel One suggests buying Chennai Petroleum Corp, Bharti Airtel…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-or-sell-osho-krishan-of-angel-one-suggests-buying-chennai-petroleum-corp-bharti-airtel-shares-to-buy-11777522637744.html) | livemint.com | 8 | negative |
| 29 Apr 2026 | [Market outlook amid assembly election exit polls 2026 results; Sensex, Nifty levels to watch tomorrow -…](https://www.businesstoday.in/markets/stocks/story/market-outlook-amid-assembly-election-exit-polls-2026-results-sensex-nifty-levels-to-watch-tomorrow-528084-2026-04-29) | businesstoday.in | 8 | negative |
| 29 Apr 2026 | [Stock Market Today: Sensex, Nifty End Higher Amid Global Uncertainty \| 📰 LatestLY](https://www.latestly.com/india/news/stock-market-today-sensex-nifty-end-higher-amid-global-uncertainty-7412073.html) | latestly.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "sensex" --since 2026-01-01 --until 2026-04-30
prism-news trends "sensex" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "sensex" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "sensex", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "sensex", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [SEBI News](sebi-news.md)
- [Income Tax News](income-tax-news.md)
- [Inflation News](inflation-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
