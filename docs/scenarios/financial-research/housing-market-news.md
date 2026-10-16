# Housing Market News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “housing market news” · 40/month India · 18,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [housing-market-news.json](../../examples/scenarios/housing-market-news.json).

**Question.** What did the news say about housing market between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="housing market"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,918 |
| Negative · neutral · positive | 54% · 1.8% · 44% |
| Critical (priority 7–9) | 57% (3,913 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,098 articles) |
| Most-reported country | United States (23% of matches) |
| Strongest theme by lift | economy news: housing market trends |

## Twelve months of coverage

Monthly matching articles for `housing market` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,017 | 55% | 573 | 435 | ██████████ |
| Jun 2025 | 944 | 59% | 507 | 433 | █████████ |
| Jul 2025 | 1,508 | 49% | 828 | 664 | ██████████████ |
| Aug 2025 | 1,581 | 50% | 847 | 714 | ███████████████ |
| Sep 2025 | 1,395 | 59% | 782 | 604 | █████████████ |
| Oct 2025 | 1,226 | 61% | 600 | 601 | ████████████ |
| Nov 2025 | 1,420 | 58% | 834 | 577 | ██████████████ |
| Dec 2025 | 1,268 | 57% | 598 | 654 | ████████████ |
| Jan 2026 | 1,510 | 58% | 846 | 650 | ██████████████ |
| Feb 2026 | 1,597 | 56% | 841 | 746 | ███████████████ |
| Mar 2026 | 1,713 | 57% | 842 | 801 | ████████████████ |
| Apr 2026 | 2,098 | 56% | 1,199 | 857 | ████████████████████ |

The last four complete months averaged 1,730 articles a month against 1,262 in the first four (+37%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,621 | 23% |
| United Kingdom | 409 | 5.9% |
| India | 231 | 3.3% |
| Australia | 228 | 3.3% |
| Canada | 133 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: housing market trends | 651 | 19% | +55% |
| economic policy impact on businesses | 553 | 16% | +73% |
| business lending and financing news | 362 | 11% | +7% |
| real estate market forecasting tools | 522 | 15% | +106% |
| regulatory compliance and legal business issues | 180 | 5.2% | +40% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | ['Five homes affordable': Rental market at breaking point for young South Aussies - News \| InDaily, Inside…](https://www.indailysa.com.au/news/just-in/2026/04/30/five-homes-affordable-rental-market-at-breaking-point-for-young-south-aussies) | indailysa.com.au | 8 | negative |
| 29 Apr 2026 | [How a plan to fix the housing market may be making it worse - realestate.com.au](https://www.dailytelegraph.com.au/real-estate/national/how-a-plan-to-fix-the-housing-market-may-be-making-it-worse/news-story/bb0c724ab7531d67115aa7e8365a23e9) | dailytelegraph.com.au | 8 | negative |
| 29 Apr 2026 | [March existing home sales hit slowest pace since 2009. Here's why.](https://www.bangordailynews.com/2026/04/29/business/business-housing/march-existing-home-sales/) | bangordailynews.com | 8 | negative |
| 29 Apr 2026 | [Lloyds takes £151m hit from Iran war as it forecasts rise in UK unemployment](https://www.theguardian.com/business/2026/apr/29/lloyds-iran-war-forecasts-rise-in-uk-unemployment) | theguardian.com | 8 | negative |
| 28 Apr 2026 | [Canada’s deflating housing bubble stymies wealth effect of booming stock market](https://www.theglobeandmail.com/investing/article-canadas-deflating-housing-bubble-stymies-wealth-effect-of-booming/) | theglobeandmail.com | 8 | negative |
| 27 Apr 2026 | [Florida's Middle Class Is Being Priced Out—And the Math Is Getting Worse - Zillow Group (NASDAQ:Z)](https://www.benzinga.com/real-estate/26/04/52056782/floridas-middle-class-is-being-priced-out-and-the-math-is-getting-worse) | benzinga.com | 8 | positive |
| 23 Apr 2026 | [Perth’s most expensive places to rent as prices hit a record](https://www.perthnow.com.au/news/business/property/domain-data-shows-perth-rents-at-new-record-prices-as-housing-market-vacancies-tighten-c-22172876) | perthnow.com.au | 8 | negative |
| 20 Apr 2026 | [Pending home sales see sharpest decline in three months as market headwinds mount - WestsideToday](https://westsidetoday.com/2026/04/20/pending-home-sales-see-sharpest-decline-in-three-months-as-market-headwinds-mount/) | westsidetoday.com | 8 | negative |
| 20 Apr 2026 | [While higher mortgage rates and increased competition among sellers has dampened typical spring growth, the…](https://bebeez.eu/2026/04/20/rightmove-market-surprisingly-resilient-despite-mortgage-rate-rises/) | bebeez.eu | 8 | positive |
| 19 Apr 2026 | [Housing market resilient despite Iran uncertainty and rate rises – Rightmove - Introducer Today](https://www.introducertoday.co.uk/breaking-news/2026/04/housing-market-resilient-despite-iran-uncertainty-and-rate-rises-rightmove/) | introducertoday.co.uk | 8 | positive |
| 18 Apr 2026 | [Priced out of Lisbon: When a full-time job isn’t enough](https://www.dw.com/en/priced-out-of-lisbon-when-a-full-time-job-isnt-enough/video-76841904) | dw.com | 8 | negative |
| 16 Apr 2026 | [US mortgage rates drop for second week to 6.3%, Freddie Mac says](https://www.businesstimes.com.sg/property/us-mortgage-rates-drop-second-week-6-3-freddie-mac-says) | businesstimes.com.sg | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "housing market" --since 2026-01-01 --until 2026-04-30
prism-news trends "housing market" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "housing market" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "housing market", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "housing market", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [GST News](gst-news.md)
- [Gold Price News](gold-price-news.md)
- [IPO News](ipo-news.md)
- [RBI News](rbi-news.md)
