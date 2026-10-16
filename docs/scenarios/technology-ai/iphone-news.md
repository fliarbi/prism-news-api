# Iphone News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “iphone news” · 1,600/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [iphone-news.json](../../examples/scenarios/iphone-news.json).

**Question.** How much iphone coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="iPhone"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 28,141 |
| Negative · neutral · positive | 17% · 2.8% · 80% |
| Critical (priority 7–9) | 26% (7,220 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (13,317 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | mobile operating systems |

## Twelve months of coverage

Monthly matching articles for `iPhone` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6,923 | 36% | 1,921 | 4,639 | ██████████ |
| Jun 2025 | 5,391 | 20% | 802 | 4,423 | ████████ |
| Jul 2025 | 6,984 | 20% | 1,514 | 5,169 | ██████████ |
| Aug 2025 | 12,205 | 27% | 2,900 | 8,407 | ██████████████████ |
| Sep 2025 | 13,317 | 13% | 1,483 | 11,190 | ████████████████████ |
| Oct 2025 | 6,120 | 28% | 1,103 | 4,724 | █████████ |
| Nov 2025 | 5,817 | 20% | 817 | 4,760 | █████████ |
| Dec 2025 | 5,086 | 22% | 854 | 3,822 | ████████ |
| Jan 2026 | 5,648 | 25% | 878 | 4,557 | ████████ |
| Feb 2026 | 6,310 | 23% | 1,137 | 5,035 | █████████ |
| Mar 2026 | 7,027 | 21% | 1,190 | 5,610 | ███████████ |
| Apr 2026 | 9,156 | 32% | 1,544 | 7,379 | ██████████████ |

The last four complete months averaged 7,035 articles a month against 7,876 in the first four (-11%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,796 | 17% |
| South Korea | 1,257 | 4.5% |
| India | 1,201 | 4.3% |
| China | 648 | 2.3% |
| United Kingdom | 510 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile operating systems | 4,616 | 25% | -45% |
| latest gadgets and consumer electronics | 2,811 | 15% | -4% |
| mobile phone hardware components | 1,442 | 7.7% | -0% |
| mobile phone operating systems | 810 | 4.3% | +13% |
| mobile phone display technologies | 1,278 | 6.8% | -14% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Singer D4vd’s iPhone had ‘significant amount’ of child porn, prosecutor says](https://www.pressenterprise.com/2026/04/23/singer-d4vds-iphone-had-significant-amount-of-child-porn-prosecutor-says/) | pressenterprise.com | 9 | negative |
| 23 Apr 2026 | [Driver killed after car hits tree, catches fire in Kent Co.](https://www.yahoo.com/news/articles/driver-killed-car-hits-tree-121715646.html) | yahoo.com | 9 | negative |
| 22 Jan 2026 | [Marine Veteran Sent Heartbreaking Text to Loved Ones After Being Fatally Shot at Facebook Marketplace Meetup](https://www.yahoo.com/news/articles/marine-veteran-sent-heartbreaking-text-212926555.html) | yahoo.com | 9 | negative |
| 14 Jan 2026 | [Urgent Warning for iPhone Users as Security Experts Push Immediate iOS Update](https://startupnews.fyi/cyber-security/urgent-warning-for-iphone-users-as-security-experts-push-immediate-ios-update) | startupnews.fyi | 9 | negative |
| 30 Apr 2026 | [Apple earning beat forecasts on iPhone 17 demand](https://gulfnews.com/technology/apple-earnings-beat-forecasts-on-iphone-17-demand-1.500525225) | gulfnews.com | 8 | positive |
| 30 Apr 2026 | [Apple sales forecast beats Wall Street expectations, shares rise](https://www.rnz.co.nz/news/world/593973/apple-sales-forecast-beats-wall-street-expectations-shares-rise) | rnz.co.nz | 8 | positive |
| 30 Apr 2026 | [Still performing like a young lad at 50, Apple releases fantastic earnings and the stock soars $10](https://www.phonearena.com/news/apple-releases-a-fantastic-earnings-report_id180080) | phonearena.com | 8 | positive |
| 30 Apr 2026 | [Apple earnings recap: Tim Cook delivers a beat across the board, talks rising memory costs](https://www.businessinsider.com/apple-q2-earnings-tim-cook-john-ternus-iphone-mac-mini-2026-4) | businessinsider.com | 8 | positive |
| 30 Apr 2026 | [Apple Stock Slips After Earnings Beat as iPhone Supply Snag Clouds $100 Billion Buyback](https://ts2.tech/en/apple-stock-slips-after-earnings-beat-as-iphone-supply-snag-clouds-100-billion-buyback/) | ts2.tech | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "iPhone" --since 2026-01-01 --until 2026-04-30
prism-news trends "iPhone" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "iPhone" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "iPhone", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "iPhone", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Chatgpt News](chatgpt-news.md)
- [Whatsapp News](whatsapp-news.md)
- [Data Center News](data-center-news.md)
- [ISRO News](isro-news.md)
