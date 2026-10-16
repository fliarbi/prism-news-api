# Dividend News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “dividend news” · 1,000/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [dividend-news.json](../../examples/scenarios/dividend-news.json).

**Question.** What did the news say about dividend between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="dividend"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 19,137 |
| Negative · neutral · positive | 11% · 5.3% · 84% |
| Critical (priority 7–9) | 24% (4,535 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (7,840 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | dividend announcements and shareholder payouts |

## Twelve months of coverage

Monthly matching articles for `dividend` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,158 | 30% | 293 | 2,723 | ████████ |
| Jun 2025 | 2,578 | 18% | 249 | 2,230 | ███████ |
| Jul 2025 | 1,825 | 34% | 221 | 1,514 | █████ |
| Aug 2025 | 2,447 | 32% | 290 | 2,058 | ██████ |
| Sep 2025 | 2,512 | 26% | 191 | 2,212 | ██████ |
| Oct 2025 | 1,774 | 33% | 162 | 1,551 | █████ |
| Nov 2025 | 2,690 | 44% | 492 | 2,107 | ███████ |
| Dec 2025 | 2,543 | 30% | 335 | 2,112 | ██████ |
| Jan 2026 | 2,438 | 22% | 259 | 2,081 | ██████ |
| Feb 2026 | 4,636 | 32% | 553 | 3,871 | ████████████ |
| Mar 2026 | 4,223 | 28% | 513 | 3,473 | ███████████ |
| Apr 2026 | 7,840 | 17% | 777 | 6,581 | ████████████████████ |

The last four complete months averaged 4,784 articles a month against 2,502 in the first four (+91%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 36% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,760 | 25% |
| Canada | 318 | 1.7% |
| India | 312 | 1.6% |
| United Kingdom | 220 | 1.1% |
| China | 161 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| dividend announcements and shareholder payouts | 7,090 | 45% | +90% |
| corporate governance and board decisions | 961 | 6.2% | +268% |
| dividend discount model (ddm) | 3,084 | 20% | +50% |
| dividend policy types | 3,621 | 23% | +48% |
| dividend investing strategies | 3,788 | 24% | +51% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Highest dividend payouts in FY26: UltraTech Cement, Maruti Suzuki HCL Tech lead](https://www.financialexpress.com/business/industry/highest-dividend-payouts-in-fy26-ultratech-cement-maruti-suzuki-hcl-tech-leadnbsp/4222472/) | financialexpress.com | 8 | positive |
| 28 Apr 2026 | [Maruti Suzuki announces Rs 140/share dividend, fixes record date. Check details](https://economictimes.indiatimes.com/markets/stocks/earnings/maruti-suzuki-announces-rs-140/share-dividend-fixes-record-date-check-details/articleshow/130575397.cms) | economictimes.indiatimes.com | 8 | positive |
| 26 Apr 2026 | [CSCS promises stronger dividends after N8.9 billion payout approval](https://nairametrics.com/2026/04/26/cscs-promises-stronger-dividends-after-n8-9-billion-payout-approval/) | nairametrics.com | 8 | positive |
| 24 Apr 2026 | [Infosys dividend history: How IT major has rewarded shareholders in last 5 years](https://economictimes.indiatimes.com/markets/stocks/news/infosys-dividend-history-how-it-major-has-rewarded-shareholders-in-last-5-years/articleshow/130486273.cms) | economictimes.indiatimes.com | 8 | positive |
| 23 Apr 2026 | [Dividend alert! Rs 36 per share by this IT stock Record date, payment date - BusinessToday](https://www.businesstoday.in/markets/stocks/story/dividend-alert-rs-36-per-share-by-this-it-stock-record-date-payment-date-527130-2026-04-23) | businesstoday.in | 8 | positive |
| 23 Apr 2026 | [Infosys dividend today: History, results timing, preview, stock returns, target prices - BusinessToday](https://www.businesstoday.in/markets/stocks/story/infosys-dividend-today-history-results-timing-preview-stock-returns-target-prices-527023-2026-04-23) | businesstoday.in | 8 | positive |
| 22 Apr 2026 | [Tech Mahindra declares highest-ever Rs 51 dividend; shares plunge 2%](https://www.financialexpress.com/business/industry/tech-mahindra-declares-highest-ever-rs-51-dividend-shares-plunge-2/4215072/) | financialexpress.com | 8 | positive |
| 22 Apr 2026 | [HCLTech Shares Drop Nearly 3% Before Q4 Results, Profit Up 4%](https://www.startuptalky.com/news/hcltech-shares-drop-ahead-q4-results/) | startuptalky.com | 8 | positive |
| 21 Apr 2026 | [Nestle India Hits 52-week High as Q4 Profit Jumps 27% – Outlook Business](https://www.outlookbusiness.com/markets/nestle-india-hits-52-week-high-as-q4-profit-jumps-27) | outlookbusiness.com | 8 | positive |
| 21 Apr 2026 | [NBP 350% Dividend: When Will Shareholders Actually Get Paid?](https://www.techjuice.pk/nbp-350-dividend-when-will-shareholders-actually-get-paid/) | techjuice.pk | 8 | positive |
| 17 Apr 2026 | [Dividend stock: Jio Financial Services declares ₹0.60 dividend alongside Q4 results - CNBC TV18](https://www.cnbctv18.com/market/jio-financial-services-share-price-declares-rs-0-60-dividend-alongside-q4-results-ws-l-19888849.htm) | cnbctv18.com | 8 | positive |
| 17 Apr 2026 | [Weibo Corporation: Weibo Announces Fourth Quarter and Fiscal Year 2025 Unaudited Financial Results and…](https://www.finanznachrichten.de/nachrichten-2026-03/67977296-weibo-corporation-weibo-announces-fourth-quarter-and-fiscal-year-2025-unaudited-financial-results-and-annual-dividend-008.htm) | finanznachrichten.de | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "dividend" --since 2026-01-01 --until 2026-04-30
prism-news trends "dividend" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "dividend" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "dividend", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "dividend", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Credit Card News](credit-card-news.md)
- [Hedge Fund News](hedge-fund-news.md)
- [Copper Price News](copper-price-news.md)
- [Unemployment News](unemployment-news.md)
