# Aviation Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “aviation industry” · 2,400/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [aviation-industry.json](../../examples/scenarios/aviation-industry.json).

**Question.** How much news did the aviation industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="aviation industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,469 |
| Negative · neutral · positive | 27% · 3.0% · 70% |
| Critical (priority 7–9) | 54% (3,518 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,936 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | aviation industry aircraft manufacturing processes |

## Twelve months of coverage

Monthly matching articles for `aviation industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 895 | 51% | 204 | 660 | █████████ |
| Jun 2025 | 974 | 60% | 332 | 627 | ██████████ |
| Jul 2025 | 1,034 | 53% | 293 | 712 | ███████████ |
| Aug 2025 | 1,012 | 55% | 208 | 771 | ██████████ |
| Sep 2025 | 1,071 | 51% | 171 | 879 | ███████████ |
| Oct 2025 | 1,216 | 54% | 234 | 954 | █████████████ |
| Nov 2025 | 1,501 | 58% | 367 | 1,111 | ████████████████ |
| Dec 2025 | 1,157 | 57% | 274 | 858 | ████████████ |
| Jan 2026 | 1,256 | 51% | 218 | 1,002 | █████████████ |
| Feb 2026 | 1,702 | 57% | 478 | 1,183 | ██████████████████ |
| Mar 2026 | 1,575 | 57% | 483 | 1,043 | ████████████████ |
| Apr 2026 | 1,936 | 52% | 564 | 1,302 | ████████████████████ |

The last four complete months averaged 1,617 articles a month against 979 in the first four (+65%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,227 | 19% |
| India | 485 | 7.5% |
| United Kingdom | 160 | 2.5% |
| China | 140 | 2.2% |
| Nigeria | 136 | 2.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| aviation industry aircraft manufacturing processes | 448 | 10% | +44% |
| aviation industry airport infrastructure development | 221 | 5.0% | +14% |
| aviation fuel management | 201 | 4.6% | +183% |
| aviation industry aerospace defense contracting | 178 | 4.1% | +34% |
| aviation industry aircraft leasing and financing | 271 | 6.2% | +33% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Fuel price surge, West Asia conflict push Indian airlines towards bigger losses](https://english.mathrubhumi.com/news/money/indian-aviation-industry-outlook-fy2026-losses-t5lykfpr) | english.mathrubhumi.com | 8 | negative |
| 28 Apr 2026 | [Rising JetA1 cost plunges Nigeria aviation into turbulence](https://punchng.com/rising-jeta1-cost-plunges-nigeria-aviation-into-turbulence/) | punchng.com | 8 | negative |
| 28 Apr 2026 | ['On Verge Of Stopping Ops': Airlines' Mayday Call To Centre Amid High Fuel Prices As Iran Crisis Drags On](https://www.republicworld.com/business/on-verge-of-stopping-ops-airlines-mayday-call-to-centre-amid-high-fuel-prices-as-iran-crisis-drags-on) | republicworld.com | 8 | negative |
| 28 Apr 2026 | [Airlines Warn Of Operational Crisis Amid Rising ATF Prices, Seek Govt Relief](https://www.newsmobile.in/nation/airlines-warn-of-operational-crisis-amid-rising-atf-prices-seek-govt-relief/) | newsmobile.in | 8 | negative |
| 25 Apr 2026 | [Air India Hesitant To Shift Part Of Operations To New Greenfield Facility At Navi Mumbai – Outlook Business](https://business.outlookindia.com/corporate/air-india-hesitant-to-shift-part-of-operations-to-new-greenfield-facility-at-navi-mumbai) | business.outlookindia.com | 8 | positive |
| 22 Apr 2026 | [How Trump's Immigration Crackdown Is Affecting Aviation Worker Shortages](https://simpleflying.com/trump-immigration-crackdown-influencing-aviation-worker-shortages/) | simpleflying.com | 8 | negative |
| 21 Apr 2026 | [Jet fuel shortage likely hitting Asia by June](https://www.philstar.com/headlines/2026/04/22/2522712/jet-fuel-shortage-likely-hitting-asia-june) | philstar.com | 8 | negative |
| 21 Apr 2026 | [Global aviation faces turbulence as Iran crisis, costs reshape outlook](https://www.thecitizen.co.tz/tanzania/business/global-aviation-faces-turbulence-as-iran-crisis-costs-reshape-outlook-5430840) | thecitizen.co.tz | 8 | negative |
| 16 Apr 2026 | [West Asia conflict hits aviation, tourism, inbound travel dips 15-20%, industry faces ₹18,000 cr loss: PHDCCI](https://www.thehindubusinessline.com/economy/west-asia-conflict-hits-aviation-tourism-inbound-travel-dips-15-20-industry-faces-18000-cr-loss-phdcci/article70868694.ece) | thehindubusinessline.com | 8 | negative |
| 16 Apr 2026 | [Middle East aviation enters its toughest test yet as war, fuel costs and route disruption reshape 2026 outlook](https://gulfnews.com/business/aviation/middle-east-aviation-faces-turbulent-months-ahead-as-war-fuel-shocks-test-airlines-1.500508044) | gulfnews.com | 8 | negative |
| 6 Apr 2026 | [Low investor confidence threatens growth of Nigeria's aviation sector - Expert](https://guardian.ng/business-services/aviation-business/low-investor-confidence-threatens-growth-of-nigerias-aviation-sector-expert/) | guardian.ng | 8 | negative |
| 3 Apr 2026 | [Top airline boss issues horror warning about the future of holidays](http://www.express.co.uk/news/uk/2190215/top-airline-boss-warning-future-holidays) | express.co.uk | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "aviation industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "aviation industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "aviation industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "aviation industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "aviation industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Healthcare Industry](healthcare-industry.md)
- [Plastics Industry](plastics-industry.md)
- [Telecom Industry](telecom-industry.md)
- [Hotel Industry](hotel-industry.md)
