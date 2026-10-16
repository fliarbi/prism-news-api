# US Dollar News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “us dollar news” · 1,900/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [us-dollar-news.json](../../examples/scenarios/us-dollar-news.json).

**Question.** What did the news say about us dollar between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="us dollar"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 14,024 |
| Negative · neutral · positive | 63% · 3.4% · 33% |
| Critical (priority 7–9) | 44% (6,120 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (5,767 articles) |
| Most-reported country | United States (38% of matches) |
| Strongest theme by lift | foreign exchange (forex) rate fluctuations |

## Twelve months of coverage

Monthly matching articles for `us dollar` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,577 | 58% | 1,618 | 907 | █████████ |
| Jun 2025 | 2,056 | 55% | 1,203 | 795 | ███████ |
| Jul 2025 | 1,995 | 52% | 1,155 | 772 | ███████ |
| Aug 2025 | 1,731 | 47% | 889 | 765 | ██████ |
| Sep 2025 | 1,931 | 48% | 913 | 947 | ███████ |
| Oct 2025 | 2,648 | 38% | 1,042 | 1,566 | █████████ |
| Nov 2025 | 2,006 | 49% | 1,097 | 857 | ███████ |
| Dec 2025 | 2,084 | 58% | 1,250 | 773 | ███████ |
| Jan 2026 | 2,147 | 58% | 1,295 | 788 | ███████ |
| Feb 2026 | 2,843 | 53% | 1,702 | 1,041 | ██████████ |
| Mar 2026 | 3,267 | 47% | 2,201 | 950 | ███████████ |
| Apr 2026 | 5,767 | 32% | 3,682 | 1,875 | ████████████████████ |

The last four complete months averaged 3,506 articles a month against 2,090 in the first four (+68%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 64% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,283 | 38% |
| India | 1,655 | 12% |
| Iran | 574 | 4.1% |
| China | 240 | 1.7% |
| Singapore | 197 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| foreign exchange (forex) rate fluctuations | 2,653 | 24% | +15% |
| emerging markets economic updates | 1,612 | 15% | +18% |
| forex spot market trading | 1,172 | 11% | +62% |
| asian financial market developments | 1,149 | 10% | +25% |
| forex market volatility analysis | 1,022 | 9.3% | +126% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [The sources, one government and another a market source, spoke on condition of anonymity as they were not…](https://www.yarrawongachronicle.com.au/aap-finance/japan-intervenes-to-counter-currency-weakness-sources/) | yarrawongachronicle.com.au | 8 | negative |
| 30 Apr 2026 | [Dollar mostly down after the Fed holds rates - FinanceFeeds](https://financefeeds.com/dollar-mostly-down-after-the-fed-holds-rates/) | financefeeds.com | 8 | negative |
| 30 Apr 2026 | [Trump tightens naval blockade as Iranian rial collapses to record low](https://www.euronews.com/2026/04/30/trump-tightens-us-naval-blockade-as-iranian-rial-collapses-to-record-low) | euronews.com | 8 | negative |
| 30 Apr 2026 | [Indian Rupee Plunges to a Historic Low Against US Dollar At ₹95.20 Sparks Economic Concerns - PUNE PULSE](https://www.mypunepulse.com/indian-rupee-plunges-to-a-historic-low-against-us-dollar-at-%e2%82%b995-20-sparks-economic-concerns/) | mypunepulse.com | 8 | negative |
| 30 Apr 2026 | [BT Explainer: Rupee hits new low: Could it touch 100? - BusinessToday](https://www.businesstoday.in/latest/economy/story/bt-explainer-rupee-hits-new-low-could-it-touch-100-528311-2026-04-30) | businesstoday.in | 8 | negative |
| 30 Apr 2026 | [Rupee Sinks to Record Low 95.23: Oil Price Spike and Fed Stance Crush INR - Business League](https://www.businessleague.in/rupee-sinks-to-record-low-95-23-oil-price-spike-and-fed-stance-crush-inr/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.dtnext.in/news/business/biz-rupee-close-27) | dtnext.in | 8 | negative |
| 30 Apr 2026 | [Rupee falls to record low of 95.3 against US dollars as oil prices surge](https://scroll.in/latest/1092497/rupee-falls-to-record-low-of-95-3-against-us-dollars-as-oil-prices-surge) | scroll.in | 8 | negative |
| 30 Apr 2026 | [Oil Surges to Wartime Highs as Supply Shock Deepens - Comments from Century Financial - Middle East News 247](https://menews247.com/oil-surges-to-wartime-highs-as-supply-shock-deepens-comments-from-century-financial/) | menews247.com | 8 | positive |
| 30 Apr 2026 | [Rupee Hits Record Low Of 95.20 Against US Dollar](https://www.newsmobile.in/trending-now/rupee-hits-record-low-of-95-20-against-us-dollar/) | newsmobile.in | 8 | negative |
| 30 Apr 2026 | [Rupee Falls 32 Paise To All-Time Low Of 95.20 Against US Dollar – Outlook Business](https://www.outlookbusiness.com/markets/rupee-falls-32-paise-to-all-time-low-of-9520-against-us-dollar) | outlookbusiness.com | 8 | negative |
| 30 Apr 2026 | [Rupee hits record low: Currency slips to 95.34 against US dollar as crude oil prices tops $120 per barrel -…](https://timesofindia.indiatimes.com/business/india-business/rupee-hits-record-low-of-95-20-against-us-dollar-slides-32-paise-in-early-trade/articleshow/130623920.cms) | timesofindia.indiatimes.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "us dollar" --since 2026-01-01 --until 2026-04-30
prism-news trends "us dollar" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "us dollar" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "us dollar", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "us dollar", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Recession News](recession-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
- [Crude Oil Price News](crude-oil-price-news.md)
- [Fintech News](fintech-news.md)
