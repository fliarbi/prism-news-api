# Restaurant Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “restaurant industry” · 260/month India · 12,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [restaurant-industry.json](../../examples/scenarios/restaurant-industry.json).

**Question.** How much news did the restaurant industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="restaurant industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,870 |
| Negative · neutral · positive | 31% · 1.0% · 67% |
| Critical (priority 7–9) | 35% (647 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (546 articles) |
| Most-reported country | United States (33% of matches) |
| Strongest theme by lift | ghost kitchens and virtual restaurants |

## Twelve months of coverage

Monthly matching articles for `restaurant industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 329 | 30% | 86 | 239 | ████████████ |
| Jun 2025 | 326 | 23% | 105 | 220 | ████████████ |
| Jul 2025 | 377 | 29% | 146 | 225 | ██████████████ |
| Aug 2025 | 546 | 30% | 181 | 362 | ████████████████████ |
| Sep 2025 | 368 | 21% | 80 | 286 | █████████████ |
| Oct 2025 | 309 | 35% | 93 | 213 | ███████████ |
| Nov 2025 | 386 | 37% | 123 | 262 | ██████████████ |
| Dec 2025 | 387 | 39% | 92 | 290 | ██████████████ |
| Jan 2026 | 372 | 24% | 77 | 291 | ██████████████ |
| Feb 2026 | 474 | 36% | 135 | 334 | █████████████████ |
| Mar 2026 | 527 | 37% | 212 | 312 | ███████████████████ |
| Apr 2026 | 497 | 38% | 164 | 323 | ██████████████████ |

The last four complete months averaged 468 articles a month against 394 in the first four (+19%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 610 | 33% |
| India | 117 | 6.3% |
| United Kingdom | 46 | 2.5% |
| Canada | 29 | 1.6% |
| China | 12 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| ghost kitchens and virtual restaurants | 114 | 12% | +54% |
| airport and transit terminal restaurants | 53 | 5.5% | +51% |
| food trucks and mobile eateries | 52 | 5.4% | +148% |
| robot-staffed or automated service restaurants | 75 | 7.8% | +127% |
| corporate governance and board decisions | 24 | 2.5% | +118% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 19 Apr 2026 | [Hotel and restaurant workers have started their strike - In this country](https://medianews.az/en/otel-ve-restoran-iscileri-tetile-baslayiblar-bu-olkede) | medianews.az | 8 | negative |
| 17 Apr 2026 | [Chicago mayor links restaurant industry to ‘slavery’ as tipped wage fight intensifies](https://www.foxnews.com/politics/chicago-mayor-links-restaurant-industry-slavery-tipped-wage-fight-intensifies) | foxnews.com | 8 | negative |
| 16 Apr 2026 | [Indian restaurants' 'slowdown' is ringing up a ₹79,000 cr bill as Iran war chokes LPG supply](https://economictimes.indiatimes.com/industry/services/hotels-/-restaurants/west-asia-lpg-shortage-india-restaurants-79000-crore-monthly-loss-iran-war-impact/articleshow/130303754.cms) | economictimes.indiatimes.com | 8 | negative |
| 8 Apr 2026 | [UK fast food chain savages Labour after entering administration - 'killing us'](https://www.express.co.uk/news/uk/2191672/uk-fast-food-chain-leon-administration) | express.co.uk | 8 | negative |
| 7 Apr 2026 | [Leon founder: Labour ‘killing’ restaurant industry](https://www.cityam.com/leon-founder-labour-killing-restaurant-industry/) | cityam.com | 8 | negative |
| 27 Mar 2026 | [Gas price spike is eating up fast food sales: Chart](https://finance.yahoo.com/news/gas-price-spike-is-eating-up-fast-food-sales-chart-131624351.html) | finance.yahoo.com | 8 | negative |
| 11 Mar 2026 | [Rising gas prices could disrupt restaurant sales recovery](https://www.nrn.com/restaurant-finance/rising-gas-prices-could-disrupt-restaurant-sales-recovery) | nrn.com | 8 | negative |
| 11 Mar 2026 | [Former Employees And Coworkers Describe Volatile Kitchen Culture At San Diego’s Only Three-Michelin-Star…](https://www.sandiegoville.com/2026/03/former-employees-describe-volatile.html) | sandiegoville.com | 8 | negative |
| 9 Mar 2026 | [Middle East crisis: Hospitality industry seeks urgent government action over commercial LPG supply…](https://timesofindia.indiatimes.com/india/middle-east-crisis-hospitality-industry-seeks-urgent-government-action-over-commercial-lpg-supply-disruption/articleshow/129348886.cms) | timesofindia.indiatimes.com | 8 | negative |
| 28 Feb 2026 | ['Bar Rescue' host Jon Taffer sounds the alarm as weight-loss drugs threaten America's restaurants](https://www.foxnews.com/entertainment/bar-rescue-host-jon-taffer-sounds-alarm-weight-loss-drugs-threaten-americas-restaurants.print) | foxnews.com | 8 | negative |
| 21 Feb 2026 | [Biryani to Billions: How a Hyderabad Tax Probe May Uncover a ₹70,000 Crore Digital Evasion Scandal](https://goachronicle.com/biryani-to-billions-how-a-hyderabad-tax-probe-may-uncover-a-%e2%82%b970000-crore-digital-evasion-scandal/) | goachronicle.com | 8 | negative |
| 23 Jan 2026 | [Singapore Eateries Appeal for Increased Subsidies and Rent Control Amid Skyrocketing Business Closures](https://www.retailnews.asia/singapore-eateries-appeal-for-increased-subsidies-and-rent-control-amid-skyrocketing-business-closures/) | retailnews.asia | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "restaurant industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "restaurant industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "restaurant industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "restaurant industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "restaurant industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Food Processing Industry](food-processing-industry.md)
- [Pharmaceutical Industry](pharmaceutical-industry.md)
- [Semiconductor Industry News](semiconductor-industry-news.md)
- [Shipbuilding Industry](shipbuilding-industry.md)
