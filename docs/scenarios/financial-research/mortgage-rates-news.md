# Mortgage Rates News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mortgage rates news” · 50/month India · 12,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [mortgage-rates-news.json](../../examples/scenarios/mortgage-rates-news.json).

**Question.** What did the news say about mortgage rates between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="mortgage rates"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,402 |
| Negative · neutral · positive | 62% · 1.4% · 36% |
| Critical (priority 7–9) | 67% (2,266 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (1,100 articles) |
| Most-reported country | United States (34% of matches) |
| Strongest theme by lift | business lending and financing news |

## Twelve months of coverage

Monthly matching articles for `mortgage rates` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 683 | 60% | 436 | 237 | ████████████ |
| Jun 2025 | 434 | 69% | 289 | 127 | ████████ |
| Jul 2025 | 773 | 57% | 535 | 233 | ██████████████ |
| Aug 2025 | 684 | 64% | 395 | 287 | ████████████ |
| Sep 2025 | 1,100 | 80% | 697 | 372 | ████████████████████ |
| Oct 2025 | 726 | 60% | 417 | 286 | █████████████ |
| Nov 2025 | 588 | 57% | 321 | 264 | ███████████ |
| Dec 2025 | 1,013 | 42% | 541 | 298 | ██████████████████ |
| Jan 2026 | 628 | 67% | 390 | 232 | ███████████ |
| Feb 2026 | 742 | 62% | 463 | 267 | █████████████ |
| Mar 2026 | 1,027 | 66% | 600 | 418 | ███████████████████ |
| Apr 2026 | 1,005 | 71% | 656 | 321 | ██████████████████ |

The last four complete months averaged 850 articles a month against 644 in the first four (+32%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,150 | 34% |
| Iran | 223 | 6.5% |
| United Kingdom | 180 | 5.3% |
| Iceland | 44 | 1.3% |
| Canada | 34 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| business lending and financing news | 448 | 19% | -20% |
| fixed-rate vs adjustable-rate mortgages | 686 | 30% | -22% |
| economy news: housing market trends | 424 | 18% | +19% |
| economic policy impact on businesses | 418 | 18% | +58% |
| mortgage refinancing guidelines | 717 | 31% | -40% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Mar 2026 | [Tamara Keith and Amy Walter on GOP midterm concerns](https://www.pbssocal.org/shows/newshour/clip/tamara-keith-and-amy-walter-on-gop-midterm-concerns-1661813389) | pbssocal.org | 9 | negative |
| 30 Apr 2026 | [Will Mortgage Rates Go Down In May? \| Bankrate](https://www.bankrate.com/mortgages/mortgage-interest-rates-forecast/) | bankrate.com | 8 | positive |
| 30 Apr 2026 | [Home sellers cut prices less even as U.S. listing prices fall again](https://www.stocktitan.net/news/NWS/spring-housing-market-holds-its-ground-despite-economic-headwinds-9bya0s1zamqe.html) | stocktitan.net | 8 | negative |
| 30 Apr 2026 | [US Mortgage Rates Surge to 6.5 Percent Amid Middle East Tensions](https://www.asatunews.co.id/en/mortgage-rates-surge-iran-tension) | asatunews.co.id | 8 | positive |
| 28 Apr 2026 | [Home price growth is slowing down — and even turning negative — in more of the country](https://malaysia.news.yahoo.com/home-price-growth-is-slowing-down--and-even-turning-negative--in-more-of-the-country-141505810.html) | malaysia.news.yahoo.com | 8 | negative |
| 27 Apr 2026 | [What's the mortgage interest rate forecast for May 2026? Here's what some experts expect.](https://cbsnews.com/news/mortgage-interest-rate-forecast-may-2026-experts/) | cbsnews.com | 8 | negative |
| 27 Apr 2026 | [Current Mortgage Rates: Navigating the Landscape as of April 27, 2026](https://www.theedadvocate.org/current-mortgage-rates-navigating-the-landscape-as-of-april-27-2026/) | theedadvocate.org | 8 | positive |
| 27 Apr 2026 | [Will mortgage rates rise again if interest rates go up this week?](https://www.thisismoney.co.uk/money/mortgageshome/article-15768203/Will-mortgage-rates-rise-rates-week-borrowers-do.html) | thisismoney.co.uk | 8 | negative |
| 27 Apr 2026 | [ATTOM's US home sales report shows declining profit margin](https://globalbusinessoutlook.com/real-estate/attoms-us-home-sales-report-shows-declining-profit-margin/) | globalbusinessoutlook.com | 8 | positive |
| 24 Apr 2026 | [These are the types of homebuyers who should buy this spring, according to experts](https://cbsnews.com/news/homebuyers-who-should-buy-spring-2026-experts-say/) | cbsnews.com | 8 | negative |
| 21 Apr 2026 | [US homebuilders set for another ‘lost’ earnings season](https://www.businesstimes.com.sg/property/us-homebuilders-set-another-lost-earnings-season) | businesstimes.com.sg | 8 | negative |
| 20 Apr 2026 | [Pending home sales see sharpest decline in three months as market headwinds mount - WestsideToday](https://westsidetoday.com/2026/04/20/pending-home-sales-see-sharpest-decline-in-three-months-as-market-headwinds-mount/) | westsidetoday.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "mortgage rates" --since 2026-01-01 --until 2026-04-30
prism-news trends "mortgage rates" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "mortgage rates" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "mortgage rates", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "mortgage rates", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Nifty News](nifty-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Silver Price News](silver-price-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
