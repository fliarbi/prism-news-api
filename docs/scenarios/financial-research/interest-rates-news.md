# Interest Rates News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “interest rates news” · 260/month India · 12,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [interest-rates-news.json](../../examples/scenarios/interest-rates-news.json).

**Question.** What did the news say about interest rates between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="interest rates"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 28,548 |
| Negative · neutral · positive | 55% · 6.3% · 39% |
| Critical (priority 7–9) | 61% (17,440 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (8,848 articles) |
| Most-reported country | United States (24% of matches) |
| Strongest theme by lift | economy news: central bank interest rate decisions |

## Twelve months of coverage

Monthly matching articles for `interest rates` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6,235 | 60% | 3,433 | 2,504 | ██████████████ |
| Jun 2025 | 5,006 | 62% | 2,715 | 2,004 | ███████████ |
| Jul 2025 | 7,329 | 55% | 4,290 | 2,749 | █████████████████ |
| Aug 2025 | 6,895 | 65% | 3,849 | 2,704 | ████████████████ |
| Sep 2025 | 8,373 | 67% | 4,525 | 3,394 | ███████████████████ |
| Oct 2025 | 5,313 | 65% | 2,726 | 2,367 | ████████████ |
| Nov 2025 | 5,420 | 62% | 2,875 | 2,321 | ████████████ |
| Dec 2025 | 7,858 | 58% | 3,640 | 3,638 | ██████████████████ |
| Jan 2026 | 6,208 | 67% | 3,218 | 2,631 | ██████████████ |
| Feb 2026 | 6,157 | 58% | 3,076 | 2,724 | ██████████████ |
| Mar 2026 | 7,335 | 62% | 4,560 | 2,352 | █████████████████ |
| Apr 2026 | 8,848 | 58% | 4,879 | 3,297 | ████████████████████ |

The last four complete months averaged 7,137 articles a month against 6,366 in the first four (+12%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 45% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 6,747 | 24% |
| Iran | 1,066 | 3.7% |
| India | 964 | 3.4% |
| United Kingdom | 797 | 2.8% |
| Australia | 539 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: central bank interest rate decisions | 3,135 | 17% | -1% |
| economy news: monetary policy changes | 3,129 | 17% | -0% |
| market sentiment and investor behavior | 1,416 | 7.5% | +52% |
| economy news: inflation rate analysis | 3,284 | 17% | +32% |
| central bank monetary policy announcements | 2,389 | 13% | -37% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 8 Apr 2026 | [Police link two late-night assaults in Christchurch, including park stabbing](https://www.nzherald.co.nz/nz/crime/christchurch-assaults-police-link-colombo-st-attack-and-bradford-park-stabbing/2Y3EBTKDDBAT5AMDAQPC6D4AIY/) | nzherald.co.nz | 9 | negative |
| 30 Apr 2026 | [FxWirePro: EUR/AUD dips after ECB rate decision , eyes 1.6150 level - EconoTimes](https://econotimes.com/FxWirePro-EUR-AUD-dips-after-ECB-rate-decision-eyes-16150-level-1740555) | econotimes.com | 8 | negative |
| 30 Apr 2026 | [‘Progress’: ANZ profits surge 9 per cent](https://www.goldcoastbulletin.com.au/business/work/leaders-companies/anz-halfyear-profits-surge-9-per-cent-to-365bn/news-story/79f487943b70c46a4b0b0d6e15d59338) | goldcoastbulletin.com.au | 8 | negative |
| 30 Apr 2026 | [Colombia Holds Interest Rates Steady in May and June](https://colombiaone.com/2026/04/30/colombia-holds-interest-rates-steady-in-may-and-june/) | colombiaone.com | 8 | positive |
| 30 Apr 2026 | [FxWirePro: GBP/USD jump after BoE rate hold - EconoTimes](https://econotimes.com/FxWirePro-GBP-USD-jump-after-BoE-rate-hold-1740517) | econotimes.com | 8 | negative |
| 30 Apr 2026 | [World Liberty Financial (WLFI) Plunges to New ATL: Has Trump's Family Ruined Crypto?](https://cryptopotato.com/world-liberty-financial-wlfi-plunges-to-new-atl-has-trumps-family-ruined-crypto/) | cryptopotato.com | 8 | negative |
| 30 Apr 2026 | [Bank of England warns ‘higher inflation unavoidable’ after holding interest rates](https://www.theguardian.com/business/2026/apr/30/bank-of-england-leaves-interest-rates-on-hold) | theguardian.com | 8 | negative |
| 30 Apr 2026 | [ECB holds rates at 2% as inflation rises and eurozone growth slows](https://au.finance.yahoo.com/news/ecb-holds-rates-2-inflation-122126422.html) | au.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [Bank of England may restart rate cuts in fourth quarter](https://www.share-talk.com/bank-of-england-may-restart-rate-cuts-in-fourth-quarter/) | share-talk.com | 8 | negative |
| 30 Apr 2026 | [Fed's favored inflation gauge shows rising prices as war heated up](https://malaysia.news.yahoo.com/feds-favored-inflation-gauge-shows-rising-prices-as-war-heated-up-131007113.html) | malaysia.news.yahoo.com | 8 | negative |
| 30 Apr 2026 | [ECB Holds the Line: Rates Stay Steady as Geopolitical Energy Risks Loom - EconoTimes](https://econotimes.com/ECB-Holds-the-Line-Rates-Stay-Steady-as-Geopolitical-Energy-Risks-Loom-1740495) | econotimes.com | 8 | positive |
| 30 Apr 2026 | [ECB Maintains Interest Rates Amid Rising Iran Conflict Risks](https://world.infonasional.com/ecb-holds-rates-iran-conflict) | world.infonasional.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "interest rates" --since 2026-01-01 --until 2026-04-30
prism-news trends "interest rates" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "interest rates" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "interest rates", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "interest rates", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Silver Price News](silver-price-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
- [S&P 500 News Today](s-p-500-news-today.md)
- [UPI News](upi-news.md)
