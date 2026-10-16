# ETF News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “etf news” · 140/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [etf-news.json](../../examples/scenarios/etf-news.json).

**Question.** What did the news say about etf between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="ETF"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 121,283 |
| Negative · neutral · positive | 20% · 1.3% · 78% |
| Critical (priority 7–9) | 25% (29,797 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (40,224 articles) |
| Most-reported country | United States (44% of matches) |
| Strongest theme by lift | exchange-traded funds (etfs) for currency exposure |

## Twelve months of coverage

Monthly matching articles for `ETF` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19,657 | 29% | 3,761 | 15,564 | ██████████ |
| Jun 2025 | 16,985 | 26% | 2,773 | 13,996 | ████████ |
| Jul 2025 | 20,894 | 24% | 3,972 | 16,741 | ██████████ |
| Aug 2025 | 26,084 | 24% | 5,476 | 20,371 | █████████████ |
| Sep 2025 | 26,281 | 24% | 4,068 | 21,772 | █████████████ |
| Oct 2025 | 22,131 | 31% | 4,844 | 17,046 | ███████████ |
| Nov 2025 | 23,139 | 32% | 5,032 | 17,902 | ████████████ |
| Dec 2025 | 25,601 | 34% | 5,998 | 19,374 | █████████████ |
| Jan 2026 | 24,075 | 22% | 4,208 | 19,486 | ████████████ |
| Feb 2026 | 27,512 | 35% | 6,911 | 20,292 | ██████████████ |
| Mar 2026 | 29,472 | 22% | 6,114 | 22,962 | ███████████████ |
| Apr 2026 | 40,224 | 21% | 7,277 | 32,272 | ████████████████████ |

The last four complete months averaged 30,321 articles a month against 20,905 in the first four (+45%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 66% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 53,817 | 44% |
| United Kingdom | 5,779 | 4.8% |
| India | 3,968 | 3.3% |
| Ireland | 1,972 | 1.6% |
| South Korea | 1,390 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| exchange-traded funds (etfs) for currency exposure | 3,702 | 4.7% | -28% |
| market liquidity and capital flow analysis | 4,709 | 6.0% | +234% |
| exchange-traded funds (etfs) | 15,134 | 19% | +165% |
| exchange-traded funds (etfs) and mutual fund trends | 9,294 | 12% | +172% |
| environmental, social, governance (esg) investing | 1,197 | 1.5% | -21% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Mar 2026 | [Bitcoin Plunges 3% And ETFs Bleed $171M After Ukraine Destroys Russian Oil Ports](https://www.benzinga.com/crypto/cryptocurrency/26/03/51510607/bitcoin-plunges-3-and-etfs-bleed-171m-after-ukraine-destroys-russian-oil-ports) | benzinga.com | 9 | negative |
| 30 Apr 2026 | [Eric Trump Reiterates $1 Million Bitcoin Forecast At](https://www.tronweekly.com/eric-trump-reiterates-1-million-bitcoin/) | tronweekly.com | 8 | positive |
| 30 Apr 2026 | [Alphabet Soars, Meta Sinks As Big Tech Splits — ETFs Let You Pick The Right Side - Alphabet (NASDAQ:GOOGL](https://www.benzinga.com/etfs/sector-etfs/26/04/52178697/alphabet-soars-meta-sinks-as-big-tech-splits-etfs-let-you-pick-the-right-side) | benzinga.com | 8 | positive |
| 30 Apr 2026 | [ARK Invest Buys $39M Robinhood, Trims Spot Bitcoin ETF](https://beincrypto.com/ark-invest-robinhood-arkb-bitcoin-etf/) | beincrypto.com | 8 | negative |
| 30 Apr 2026 | [Chainlink Price Prediction Gains Weight as LINK ETF Inflows Top $111M and Pepeto Targets 100x](https://coinpedia.org/press-release/chainlink-price-prediction-gains-weight-pepeto-targets-100x/) | coinpedia.org | 8 | positive |
| 30 Apr 2026 | [Crypto ETFs Bleed $222M As Bitcoin And Ethereum Funds Flash Red](https://cryptoadventure.com/crypto-etfs-bleed-222m-as-bitcoin-and-ethereum-funds-flash-red/) | cryptoadventure.com | 8 | positive |
| 30 Apr 2026 | [Bitwise CIO Ties Bitcoin's 20% Rebound To Strategy's $7.2B STRC Buying \| Yellow.com](https://yellow.com/news/bitwise-strc-bitcoin-20-percent-rally) | yellow.com | 8 | negative |
| 30 Apr 2026 | [XRP price holds near $1.40 as ETF inflows hit $82.4 million](https://en.cryptonomist.ch/2026/04/30/xrp-price-outlook-etf-rakuten/) | en.cryptonomist.ch | 8 | positive |
| 30 Apr 2026 | [Bitcoin’s Institutional Absorption Cycle Deepens as Fed Hold Tests Market Momentum](https://www.unlock-bc.com/en/bitcoin-slips-after-fed-hold-as-institutional-demand-builds) | unlock-bc.com | 8 | positive |
| 29 Apr 2026 | [Eric Trump, John Koudounis Call Bitcoin A Global Reserve Asset, Float $1M Price Target](https://bitcoinmagazine.com/news/eric-trump-john-koudounis-bitcoin-asset) | bitcoinmagazine.com | 8 | positive |
| 29 Apr 2026 | [BlackRock’s IBIT Leads Bitcoin ETF Outflows in Latest $89.7M Pullback - Crypto Economy](https://crypto-economy.com/blackrock-ibit-leads-bitcoin-etf-outflows-89m/) | crypto-economy.com | 8 | negative |
| 29 Apr 2026 | [Bitcoin Spot ETFs Saw $89.7M in Net Outflows on April 28](https://coincu.com/bitcoin-spot-etfs-89-7m-net-outflows-april-28-blackrock-ibit-112m/) | coincu.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ETF" --since 2026-01-01 --until 2026-04-30
prism-news trends "ETF" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ETF" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ETF", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ETF", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [ECB News Today](ecb-news-today.md)
- [Stablecoin News](stablecoin-news.md)
- [GDP News](gdp-news.md)
- [Credit Card News](credit-card-news.md)
