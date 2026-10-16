# UPI News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “upi news” · 2,400/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [upi-news.json](../../examples/scenarios/upi-news.json).

**Question.** What did the news say about upi between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="UPI"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 17,050 |
| Negative · neutral · positive | 34% · 1.9% · 64% |
| Critical (priority 7–9) | 55% (9,370 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,938 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | garage rock revival |

## Twelve months of coverage

Monthly matching articles for `UPI` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,273 | 54% | 877 | 1,321 | █████████ |
| Jun 2025 | 1,917 | 60% | 606 | 1,263 | ████████ |
| Jul 2025 | 2,610 | 54% | 767 | 1,774 | ███████████ |
| Aug 2025 | 4,373 | 40% | 932 | 3,355 | ██████████████████ |
| Sep 2025 | 3,064 | 61% | 941 | 2,062 | ████████████ |
| Oct 2025 | 3,093 | 63% | 947 | 2,083 | █████████████ |
| Nov 2025 | 2,998 | 51% | 890 | 2,055 | ████████████ |
| Dec 2025 | 2,941 | 56% | 1,062 | 1,827 | ████████████ |
| Jan 2026 | 3,445 | 50% | 1,101 | 2,294 | ██████████████ |
| Feb 2026 | 4,664 | 55% | 1,256 | 3,348 | ███████████████████ |
| Mar 2026 | 4,003 | 56% | 1,580 | 2,321 | ████████████████ |
| Apr 2026 | 4,938 | 58% | 1,800 | 2,996 | ████████████████████ |

The last four complete months averaged 4,262 articles a month against 2,793 in the first four (+53%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,301 | 25% |
| India | 3,416 | 20% |
| Denmark | 360 | 2.1% |
| South Korea | 317 | 1.9% |
| United Kingdom | 212 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| garage rock revival | 388 | 3.8% | +130% |
| mobile banking app innovations | 286 | 2.8% | +82% |
| payment systems and real-time transaction technologies | 263 | 2.5% | +32% |
| glam rock aesthetics | 389 | 3.8% | +121% |
| online payment gateway integration services | 451 | 4.4% | +19% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [U.S. kills three in latest suspected drug boat attack in Pacific](https://www.yahoo.com/news/articles/u-kills-three-latest-suspected-055821043.html) | yahoo.com | 9 | negative |
| 23 Apr 2026 | [Renewed Israel-Hezbollah war raises human, material toll on Lebanon - UPI.com](https://www.upi.com/Top_News/World-News/2026/04/23/lebanon-israeli-bombing-destruction-displaced/6861776972813/) | upi.com | 9 | negative |
| 20 Apr 2026 | [U.S. kills three in latest military strike on a suspected drug boat](https://www.yahoo.com/news/articles/u-kills-three-latest-military-040549061.html) | yahoo.com | 9 | negative |
| 20 Apr 2026 | [U.S. kills three in latest military strike on a suspected drug boat - UPI.com](https://www.upi.com/Top_News/World-News/2026/04/20/latam-us-strike-drug-boat/2311776653521/) | upi.com | 9 | negative |
| 15 Apr 2026 | [U.S. kills four in fourth anti-drug boat strike since Saturday - UPI.com](https://www.upi.com/Top_News/World-News/2026/04/15/drug-boat-attack/7051776225028/) | upi.com | 9 | negative |
| 14 Apr 2026 | [U.S. kills two in Pacific strike of alleged drug-trafficking boat - UPI.com](https://www.upi.com/Top_News/US/2026/04/13/SOUTHCOM-boat-attack/6431776130576/) | upi.com | 9 | negative |
| 13 Apr 2026 | [U.S. kills five in two strikes on alleged drug boats in Pacific](https://www.yahoo.com/news/articles/u-kills-five-two-strikes-080810178.html) | yahoo.com | 9 | negative |
| 13 Apr 2026 | [U.S. kills five in two strikes on alleged drug boats in Pacific - UPI.com](https://www.upi.com/Top_News/World-News/2026/04/13/SOUTHCOM-drug-boat/5061776064668/) | upi.com | 9 | negative |
| 12 Apr 2026 | [Trump says U.S. Navy will block Strait of Hormuz after peace talks fail](https://www.yahoo.com/news/articles/trump-says-u-navy-block-165358457.html) | yahoo.com | 9 | negative |
| 12 Apr 2026 | [Trump says U.S. Navy will block Strait of Hormuz after peace talks fail - UPI.com](https://www.upi.com/Top_News/World-News/2026/04/12/trump-block-strait-hormuz-iran-deal/2001776011033/) | upi.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "UPI" --since 2026-01-01 --until 2026-04-30
prism-news trends "UPI" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "UPI" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "UPI", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "UPI", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Interest Rates News](interest-rates-news.md)
- [S&P 500 News Today](s-p-500-news-today.md)
- [Budget News](budget-news.md)
- [SEBI News](sebi-news.md)
