# Crypto News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “crypto news” · 49,500/month India · 165,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [crypto-news.json](../../examples/scenarios/crypto-news.json).

**Question.** What did the news say about crypto between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="crypto"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 66,190 |
| Negative · neutral · positive | 33% · 1.2% · 65% |
| Critical (priority 7–9) | 59% (39,201 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (20,318 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | cryptocurrency impact on forex markets |

## Twelve months of coverage

Monthly matching articles for `crypto` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18,293 | 61% | 4,419 | 13,670 | ██████████████████ |
| Jun 2025 | 15,508 | 60% | 3,681 | 11,677 | ███████████████ |
| Jul 2025 | 12,394 | 56% | 2,571 | 9,649 | ████████████ |
| Aug 2025 | 11,962 | 58% | 2,754 | 9,070 | ████████████ |
| Sep 2025 | 15,303 | 59% | 2,888 | 12,255 | ███████████████ |
| Oct 2025 | 17,159 | 64% | 4,192 | 12,824 | █████████████████ |
| Nov 2025 | 16,747 | 64% | 5,018 | 11,558 | ████████████████ |
| Dec 2025 | 15,496 | 62% | 4,204 | 11,141 | ███████████████ |
| Jan 2026 | 12,000 | 59% | 3,120 | 8,706 | ████████████ |
| Feb 2026 | 18,934 | 53% | 7,909 | 10,820 | ███████████████████ |
| Mar 2026 | 14,938 | 60% | 4,659 | 10,087 | ███████████████ |
| Apr 2026 | 20,318 | 64% | 6,349 | 13,702 | ████████████████████ |

The last four complete months averaged 16,548 articles a month against 14,539 in the first four (+14%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 18,249 | 28% |
| Iran | 1,219 | 1.8% |
| United Kingdom | 1,013 | 1.5% |
| China | 884 | 1.3% |
| India | 854 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| cryptocurrency impact on forex markets | 34,125 | 68% | -9% |
| technical analysis for currency markets | 2,093 | 4.2% | +42% |
| exchange-traded funds (etfs) for currency exposure | 1,975 | 4.0% | -25% |
| regulatory compliance in foreign exchange trading | 7,052 | 14% | +26% |
| forex trading risk management frameworks | 1,760 | 3.5% | +76% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 11 Apr 2026 | [Iran Conflict: Diplomacy and International Mediation Efforts - Time News](https://time.news/iran-conflict-diplomacy-and-international-mediation-efforts/) ⚠ | time.news | 9 | negative |
| 22 Mar 2026 | [US-Iran Tensions Spike as Trump Sets 48-Hour Deadline on Strait of Hormuz Blockade](https://coingape.com/us-iran-tensions-spike-as-trump-sets-48-hour-deadline-on-strait-of-hormuz-blockade/) | coingape.com | 9 | negative |
| 3 Mar 2026 | [Iran sends chilling WW3 warning - 'The Gates of Hell will open'](https://www.express.co.uk/news/world/2177617/iran-war-us-israel-ww3-warning) ⚠ | express.co.uk | 9 | negative |
| 30 Apr 2026 | [US Cracks Down on Iran’s Crypto Network With Crypto Seizures](https://coinlaw.io/us-iran-crypto-seizure-sanctions-crackdown/) | coinlaw.io | 8 | negative |
| 30 Apr 2026 | [Could Pepeto Be the Next Crypto to Explode as Strategy Loads 818,334 BTC While SOL and BNB Stall](https://www.openpr.com/news/4497376/could-pepeto-be-the-next-crypto-to-explode-as-strategy-loads) | openpr.com | 8 | negative |
| 30 Apr 2026 | [Justin Sun And Trump-Linked WLFI Move From Crypto Alliance To Court Fight](https://cryptoadventure.com/justin-sun-and-trump-linked-wlfi-move-from-crypto-alliance-to-court-fight/) | cryptoadventure.com | 8 | negative |
| 29 Apr 2026 | [Here's Why XRP (Ripple) Could Drop Below $1 and Stay There \| The Motley Fool](https://www.fool.com/investing/2026/04/29/heres-why-xrp-ripple-could-drop-below-1-and-stay-t/) ⚠ | fool.com | 8 | negative |
| 29 Apr 2026 | [Is Crypto Becoming Part of Everyday Life, or Is Mass Adoption Still Far Away? - Crypto Economy](https://crypto-economy.com/is-crypto-becoming-part-of-everyday-life-or-is-mass-adoption-still-far-away/) | crypto-economy.com | 8 | negative |
| 29 Apr 2026 | [Bitcoin Drops $75,000 As Ethereum, XRP Trade Lose 3%](https://www.benzinga.com/crypto/cryptocurrency/26/04/52145880/bitcoin-drops-75000-as-ethereum-xrp-trade-lose-3) | benzinga.com | 8 | positive |
| 29 Apr 2026 | [Nigel Farage faces standards probe over $6.7 million gift from Tether billionaire Christopher Harborne](https://www.coindesk.com/policy/2026/04/29/u-k-s-farage-faces-standards-probe-over-usd6-7-million-gift-from-tether-billionaire-christopher-harborne) | coindesk.com | 8 | negative |
| 29 Apr 2026 | [MEXC and Sumsub Partner to Strengthen Global Compliance and Combat Emerging Identity Fraud Risks](https://mediabulletins.com/business/mexc-and-sumsub-partner-to-strengthen-global-compliance-and-combat-emerging-identity-fraud-risks/) | mediabulletins.com | 8 | positive |
| 29 Apr 2026 | [FOMC Meeting Today: Powell Speech and Fed Interest Rate Decision Could Move BTC, ETH, XRP and Altcoins](https://coinpedia.org/news/fed-rate-cut-news-how-powells-words-could-move-btc-eth-and-altcoins/) | coinpedia.org | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "crypto" --since 2026-01-01 --until 2026-04-30
prism-news trends "crypto" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "crypto" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "crypto", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "crypto", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Stock Market News](stock-market-news.md)
- [GST News](gst-news.md)
- [Gold Price News](gold-price-news.md)
