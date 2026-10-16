# Mergers and Acquisitions News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mergers and acquisitions news” · 720/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [mergers-and-acquisitions-news.json](../../examples/scenarios/mergers-and-acquisitions-news.json).

**Question.** What did the news say about mergers and acquisitions between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="mergers and acquisitions"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 44,613 |
| Negative · neutral · positive | 24% · 4.8% · 71% |
| Critical (priority 7–9) | 48% (21,457 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (12,971 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | corporate governance and board decisions |

## Twelve months of coverage

Monthly matching articles for `mergers and acquisitions` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7,480 | 46% | 1,811 | 5,177 | ████████████ |
| Jun 2025 | 7,204 | 43% | 1,621 | 5,154 | ███████████ |
| Jul 2025 | 9,285 | 46% | 2,554 | 6,269 | ██████████████ |
| Aug 2025 | 7,953 | 42% | 1,922 | 5,652 | ████████████ |
| Sep 2025 | 8,927 | 43% | 1,901 | 6,585 | ██████████████ |
| Oct 2025 | 7,447 | 52% | 1,399 | 5,712 | ███████████ |
| Nov 2025 | 7,101 | 53% | 1,544 | 5,202 | ███████████ |
| Dec 2025 | 8,831 | 55% | 1,808 | 6,623 | ██████████████ |
| Jan 2026 | 9,209 | 49% | 1,959 | 6,829 | ██████████████ |
| Feb 2026 | 12,218 | 49% | 2,862 | 8,817 | ███████████████████ |
| Mar 2026 | 10,215 | 46% | 2,360 | 7,261 | ████████████████ |
| Apr 2026 | 12,971 | 48% | 3,402 | 8,949 | ████████████████████ |

The last four complete months averaged 11,153 articles a month against 7,980 in the first four (+40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 11,414 | 26% |
| India | 1,807 | 4.0% |
| United Kingdom | 1,563 | 3.5% |
| Canada | 581 | 1.3% |
| France | 432 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| corporate governance and board decisions | 1,860 | 7.0% | +80% |
| mergers and acquisitions activity updates | 5,304 | 20% | +49% |
| corporate restructuring and divestitures | 3,387 | 13% | +56% |
| initial public offerings (ipos) | 1,558 | 5.8% | +28% |
| company expansions and new market entries | 1,891 | 7.1% | +97% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [FCCPC Warns Firms Against Breaching Merger Notification Rules](https://thewillnews.com/fccpc-warns-firms-against-breaching-merger-notification-rules/) | thewillnews.com | 8 | positive |
| 21 Apr 2026 | [FCCPC toughens merger rules, signs Lagos consumer pact](https://punchng.com/fccpc-toughens-merger-rules-signs-lagos-consumer-pact/) | punchng.com | 8 | negative |
| 21 Apr 2026 | [FCCPC warns companies against mergers without prior approval](https://punchng.com/fccpc-warns-companies-against-mergers-without-prior-approval/) | punchng.com | 8 | positive |
| 15 Apr 2026 | [Bank of America first-quarter profit rises on strong trading, investment banking](http://www.theglobeandmail.com/business/international-business/us-business/article-bank-of-america-first-quarter-earnings-results-trading-investment/) | theglobeandmail.com | 8 | positive |
| 14 Apr 2026 | [India auto & EV deal activity at $745 mn in Q1; PE investments jump 86%: Grant Thornton Bharat](https://www.fortuneindia.com/auto/india-auto-ev-deal-activity-at-35-deals-745-million-in-q1-2026-pe-investments-jump-86-grant-thornton-bharat/132405) | fortuneindia.com | 8 | positive |
| 13 Apr 2026 | [Goldman Sachs posts best quarterly profit in five years with 18% jump](http://www.euronews.com/business/2026/04/13/goldman-sachs-posts-best-quarterly-profit-in-five-years-with-18-jump) | euronews.com | 8 | positive |
| 3 Apr 2026 | [2026: A Year of Transformation in Cryptocurrency M&A Trends](https://www.theedadvocate.org/2026-a-year-of-transformation-in-cryptocurrency-ma-trends/) | theedadvocate.org | 8 | positive |
| 2 Apr 2026 | [Tolling takes off in Europe - pv magazine Global](https://www.pv-magazine.com/2026/04/02/tolling-takes-off-in-europe/) | pv-magazine.com | 8 | positive |
| 1 Apr 2026 | [U.S. Firms Continue To Slash Jobs Amid Record AI Spending And Mega-Deals](http://ibtimes.com/us-firms-slash-jobs-amid-record-ai-spending-mega-deals-3800723) | ibtimes.com | 8 | negative |
| 23 Mar 2026 | [M&A activity to accelerate this year despite war disruption, Goldman Sachs says \| M&A Critique](https://mnacritique.mergersindia.com/news/ma-activity-to-accelerate-this-year-despite-war-disruption-goldman-sachs-says/) | mnacritique.mergersindia.com | 8 | positive |
| 20 Mar 2026 | [M&A activity to accelerate this year despite war disruption, Goldman Sachs says](https://economictimes.indiatimes.com/news/international/business/ma-activity-to-accelerate-this-year-despite-war-disruption-goldman-sachs-says/articleshow/129699736.cms) | economictimes.indiatimes.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "mergers and acquisitions" --since 2026-01-01 --until 2026-04-30
prism-news trends "mergers and acquisitions" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "mergers and acquisitions" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "mergers and acquisitions", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "mergers and acquisitions", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Fintech News](fintech-news.md)
- [Mutual Fund News](mutual-fund-news.md)
- [Private Equity News](private-equity-news.md)
- [Pension News](pension-news.md)
