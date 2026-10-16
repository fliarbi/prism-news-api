# Stock Market News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “stock market news” · 74,000/month India · 201,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [stock-market-news.json](../../examples/scenarios/stock-market-news.json).

**Question.** What did the news say about stock market between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="stock market"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 226,944 |
| Negative · neutral · positive | 26% · 2.7% · 72% |
| Critical (priority 7–9) | 29% (64,714 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (82,710 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | market volatility indicators |

## Twelve months of coverage

Monthly matching articles for `stock market` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 33,813 | 34% | 8,403 | 24,636 | ████████ |
| Jun 2025 | 36,236 | 22% | 6,065 | 29,479 | █████████ |
| Jul 2025 | 23,722 | 40% | 7,216 | 15,903 | ██████ |
| Aug 2025 | 28,040 | 37% | 7,205 | 20,225 | ███████ |
| Sep 2025 | 35,288 | 34% | 7,223 | 27,098 | █████████ |
| Oct 2025 | 30,992 | 42% | 8,301 | 21,102 | ███████ |
| Nov 2025 | 30,732 | 44% | 9,094 | 20,707 | ███████ |
| Dec 2025 | 29,963 | 40% | 8,149 | 20,552 | ███████ |
| Jan 2026 | 45,166 | 25% | 9,417 | 34,596 | ███████████ |
| Feb 2026 | 52,325 | 32% | 13,096 | 37,841 | █████████████ |
| Mar 2026 | 46,743 | 35% | 15,865 | 29,459 | ███████████ |
| Apr 2026 | 82,710 | 24% | 20,068 | 60,499 | ████████████████████ |

The last four complete months averaged 56,736 articles a month against 30,453 in the first four (+86%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 64,520 | 28% |
| India | 5,984 | 2.6% |
| United Kingdom | 4,255 | 1.9% |
| Canada | 3,704 | 1.6% |
| China | 3,366 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market volatility indicators | 8,287 | 5.5% | +47% |
| asian financial market developments | 4,632 | 3.1% | +58% |
| short selling strategies | 3,684 | 2.5% | +140% |
| stock market index composition | 5,809 | 3.9% | +66% |
| emerging markets economic updates | 3,353 | 2.2% | +61% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [US-Iran Ceasefire Deadline: क्या क्रैश होगा शेयर मार्केट? सीजफायर खत्म होने से पहले ट्रंप की ईरान को चेतावनी…](https://www.livemint.com/hindi/market/share-market-crash-countdow-us-iran-tensions-gift-nifty-slips-as-trump-rejects-ceasefire-extension-portfolio-safe-241776787480847.html) | livemint.com | 9 | negative |
| 8 Apr 2026 | [$1.5 trillion relief rally erupts on Wall Street after Trump hits pause on Iran strikes \| Fortune](https://www.fortune.com/2026/04/08/markets-sp-trump-truce-ceasefire-iran-war-rally-strait-of-hormuz/) | fortune.com | 9 | negative |
| 7 Apr 2026 | [Ibovespa zera perdas e fecha estável com pedido de trégua do Paquistão](https://exame.com/invest/mercados/ibovespa-hoje-07-04-2026fechamento/) | exame.com | 9 | negative |
| 30 Apr 2026 | [U.S. stocks rally to the finish of their best month since 2020, even as oil prices whipsaw](https://www.latimes.com/business/story/2026-04-30/u-s-stocks-rally-to-finish-of-their-best-month-since-2020) | latimes.com | 8 | negative |
| 30 Apr 2026 | [US stocks rally to the finish of their best month since 2020, even as oil prices whipsaw](https://ca.finance.yahoo.com/news/brent-crude-tops-125-barrel-044922386.html) | ca.finance.yahoo.com | 8 | positive |
| 30 Apr 2026 | [Senate Prohibits Members, Staff From Using Prediction Markets](https://www.yahoo.com/news/articles/senate-prohibits-members-staff-using-193346837.html) | yahoo.com | 8 | negative |
| 30 Apr 2026 | [Solana-based yield trading platform Exponent has raised $5 million in seed funding, led by Multicoin Capital.](https://www.panewslab.com/articles/019ddef8-244e-72b0-9a8b-813265ed54ec) | panewslab.com | 8 | positive |
| 30 Apr 2026 | [El petróleo frena su escalada y se aleja de los máximos de 2022 \| Diario Sur](https://www.diariosur.es/economia/mercados/petroleo-alcanza-maximos-2022-sacude-mercados-financieros-20260430102516-ntrc.html) | diariosur.es | 8 | negative |
| 30 Apr 2026 | [Record High Oil, All-Time Low Rupee Batters Sensex, Nifty; IndiGo, Eternal Top Losers Chart](https://www.freepressjournal.in/business/record-high-oil-rupee-plunge-batter-sensex-nifty-indigo-eternal-top-losers-chart) | freepressjournal.in | 8 | negative |
| 30 Apr 2026 | [Stocks to buy: Nagaraj Shetti recommends Time Technoplast, Gujarat Ambuja Exports shares to buy \| Stock…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-nagaraj-shetti-recommends-time-technoplast-gujarat-ambuja-exports-shares-to-buy-11777528414947.html) | livemint.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy or sell: Osho Krishan of Angel One suggests buying Chennai Petroleum Corp, Bharti Airtel…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-or-sell-osho-krishan-of-angel-one-suggests-buying-chennai-petroleum-corp-bharti-airtel-shares-to-buy-11777522637744.html) | livemint.com | 8 | negative |
| 30 Apr 2026 | [Stock market: BJP win in Bengal elections? What JM, others say on exit poll results 2026 - BusinessToday](https://www.businesstoday.in/markets/stocks/story/stock-market-bjp-win-in-bengal-elections-what-jm-others-say-on-exit-poll-results-2026-528144-2026-04-30) | businesstoday.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "stock market" --since 2026-01-01 --until 2026-04-30
prism-news trends "stock market" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "stock market" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "stock market", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "stock market", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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
