# Market Crash News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “market crash news” · 880/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [market-crash-news.json](../../examples/scenarios/market-crash-news.json).

**Question.** What did the news say about market crash between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="market crash"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 578 |
| Negative · neutral · positive | 76% · 0.2% · 24% |
| Critical (priority 7–9) | 72% (418 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (332 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | market volatility indicators |

## Twelve months of coverage

Monthly matching articles for `market crash` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 100 | 74% | 54 | 46 | ██████ |
| Jun 2025 | 135 | 56% | 51 | 82 | ████████ |
| Jul 2025 | 55 | 60% | 37 | 18 | ███ |
| Aug 2025 | 79 | 63% | 60 | 19 | █████ |
| Sep 2025 | 40 | 75% | 29 | 11 | ██ |
| Oct 2025 | 332 | 77% | 221 | 110 | ████████████████████ |
| Nov 2025 | 191 | 83% | 131 | 59 | ████████████ |
| Dec 2025 | 73 | 59% | 63 | 10 | ████ |
| Jan 2026 | 96 | 70% | 72 | 23 | ██████ |
| Feb 2026 | 211 | 74% | 149 | 62 | █████████████ |
| Mar 2026 | 175 | 70% | 146 | 29 | ███████████ |
| Apr 2026 | 96 | 75% | 70 | 26 | ██████ |

The last four complete months averaged 144 articles a month against 92 in the first four (+57%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 147 | 25% |
| Iran | 39 | 6.8% |
| India | 21 | 3.6% |
| China | 10 | 1.7% |
| Japan | 5 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market volatility indicators | 87 | 22% | +691% |
| stock market index composition | 68 | 17% | +1033% |
| market sentiment and investor behavior | 67 | 17% | +81% |
| market volatility and risk assessment | 72 | 18% | +53% |
| bull and bear market transitions | 82 | 20% | +26% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Feb 2026 | [Best Crypto to Invest In: South Korea Deploys AI Market Surveillance as Iran Strikes Crash ETH and SOL, but…](https://www.openpr.com/news/4408627/best-crypto-to-invest-in-south-korea-deploys-ai-market) | openpr.com | 8 | negative |
| 22 Feb 2026 | [Market Crash Impact for NSE:RELIANCE by GlobalWolfStreet](https://in.tradingview.com/chart/RELIANCE/5Zulp20m-Market-Crash-Impact/) | in.tradingview.com | 8 | negative |
| 20 Feb 2026 | [ZeroLend, Parsec Become Latest Victims in Post-October 10 Crypto Shakeout](https://bitcoinethereumnews.com/crypto/zerolend-parsec-become-latest-victims-in-post-october-10-crypto-shakeout/) | bitcoinethereumnews.com | 8 | negative |
| 8 Feb 2026 | [Bitcoin Cycle Killed by Grifters, Tesla Investor Gerber Says](https://bitcoinethereumnews.com/bitcoin/bitcoin-cycle-killed-by-grifters-tesla-investor-gerber-says/) | bitcoinethereumnews.com | 8 | negative |
| 8 Feb 2026 | [Bitcoin Cycle Killed by Grifters, Tesla Investor Gerber Says - U.Today](https://u.today/bitcoin-cycle-killed-by-grifters-tesla-investor-gerber-says) | u.today | 8 | negative |
| 5 Feb 2026 | [Apocalypse now? Top economist says crypto market looks bleak](https://bitcoinethereumnews.com/crypto/apocalypse-now-top-economist-says-crypto-market-looks-bleak/) | bitcoinethereumnews.com | 8 | negative |
| 31 Jan 2026 | [Dragonfly Partner: The market crash on October 11th was not solely caused by Binance and Ethena; multiple…](https://www.panewslab.com/en/articles/34be1d0e-c89c-406b-b5df-0a137c99b143) | panewslab.com | 8 | negative |
| 31 Jan 2026 | [OKX CEO Takes Aim Against Binance for October 10 Crypto Market Crash](https://www.cryptotimes.io/2026/01/31/okx-ceo-takes-aim-against-binance-for-october-10-crypto-market-crash/) | cryptotimes.io | 8 | negative |
| 30 Jan 2026 | [What crash? Binance’s CZ rejects claims platform caused $19b crypto crash](https://crypto.news/what-crash-binance-cz-rejects-19b-crash-claim/) | crypto.news | 8 | negative |
| 13 Apr 2026 | [Ola Electric shares slip 8%,overbought on charts; still a 'buy'? - BusinessToday](https://www.businesstoday.in/markets/stocks/story/ola-electric-shares-slip-overbought-on-charts-still-a-buy-525324-2026-04-13) | businesstoday.in | 7 | positive |
| 28 Mar 2026 | [Robert Kiyosaki Highlights Bitcoin Strategy as He Flags Incoming Market Crash Risk](https://news.bitcoin.com/robert-kiyosaki-highlights-bitcoin-strategy-as-he-flags-incoming-market-crash-risk) | news.bitcoin.com | 7 | positive |
| 23 Mar 2026 | [Stock Market Crash Reason: ये 5 कारण... जिनसे शेयर बाजार में भूचाल, 12 लाख करोड़ स्वाहा!](https://www.aajtak.in/business/news/story/stock-market-crash-five-big-reason-behind-bloodbath-investors-big-loss-tutc-dskc-2504539-2026-03-23) | aajtak.in | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "market crash" --since 2026-01-01 --until 2026-04-30
prism-news trends "market crash" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "market crash" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "market crash", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "market crash", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Treasury Yields News](treasury-yields-news.md)
- [Yen News](yen-news.md)
- [Tax News Today](tax-news-today.md)
- [IMF News](imf-news.md)
