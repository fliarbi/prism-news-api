# Refinery News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “refinery news” · 140/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [refinery-news.json](../../examples/scenarios/refinery-news.json).

**Question.** How did refinery coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="refinery"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 7,480 |
| Negative · neutral · positive | 60% · 2.6% · 37% |
| Critical (priority 7–9) | 80% (5,982 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,000 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | crude oil refining methods |

## Twelve months of coverage

Monthly matching articles for `refinery` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 750 | 70% | 385 | 340 | █████ |
| Jun 2025 | 644 | 76% | 290 | 342 | ████ |
| Jul 2025 | 800 | 75% | 432 | 356 | █████ |
| Aug 2025 | 950 | 76% | 458 | 467 | ██████ |
| Sep 2025 | 1,339 | 81% | 796 | 508 | █████████ |
| Oct 2025 | 1,230 | 87% | 716 | 482 | ████████ |
| Nov 2025 | 956 | 80% | 494 | 441 | ██████ |
| Dec 2025 | 711 | 76% | 337 | 362 | █████ |
| Jan 2026 | 868 | 71% | 327 | 506 | ██████ |
| Feb 2026 | 959 | 76% | 401 | 521 | ██████ |
| Mar 2026 | 2,653 | 82% | 1,813 | 789 | ██████████████████ |
| Apr 2026 | 3,000 | 82% | 1,949 | 976 | ████████████████████ |

The last four complete months averaged 1,870 articles a month against 786 in the first four (+138%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,104 | 15% |
| India | 596 | 8.0% |
| Nigeria | 470 | 6.3% |
| Australia | 236 | 3.2% |
| Ireland | 137 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| crude oil refining methods | 1,026 | 18% | +88% |
| petroleum distillation processes | 621 | 11% | +90% |
| crude oil storage solutions | 459 | 8.2% | +194% |
| petrochemical manufacturing | 427 | 7.6% | +91% |
| chemical plant explosions and hazardous material leaks | 781 | 14% | +398% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Mar 2026 | [Ukraine's Bold Strike on Crucial Russian Oil Targets \| Law-Order](https://www.devdiscourse.com/article/law-order/3847177-ukraines-bold-strike-on-crucial-russian-oil-targets) | devdiscourse.com | 9 | negative |
| 29 Apr 2026 | [Do Global Refinery Fires Signal Something Much Darker?](https://stratnewsglobal.com/west-asia/do-global-refinery-fires-signal-something-much-darker/) | stratnewsglobal.com | 8 | negative |
| 24 Apr 2026 | [US sanctions China-based refinery_ 40 shippers over Iranian oil](https://article.wn.com/view/2026/04/25/US_sanctions_Chinabased_refinery_40_shippers_over_Iranian_oi/) | article.wn.com | 8 | negative |
| 22 Apr 2026 | [Pachpadra refinery blaze: Agencies examining CCTV footages to find out reasons of fire - Social News XYZ](https://www.socialnews.xyz/2026/04/22/pachpadra-refinery-blaze-agencies-examining-cctv-footages-to-find-out-reasons-of-fire/) | socialnews.xyz | 8 | negative |
| 20 Apr 2026 | [Fire at Pachpadra Refinery Postpones PM Modi's Rajasthan Visit](https://www.newkerala.com/news/a/rajasthan-pm-modis-visit-postponed-after-fire-pachpadra-280.htm) | newkerala.com | 8 | negative |
| 20 Apr 2026 | [Rajasthan CM orders high-level probe into Pachpadra refinery fire, calls it 'unfortunate' - Yes Punjab News](https://yespunjab.com/rajasthan-cm-orders-high-level-probe-into-pachpadra-refinery-fire-calls-it-unfortunate/) | yespunjab.com | 8 | negative |
| 20 Apr 2026 | [Rajasthan CM orders high-level probe into Pachpadra refinery fire, calls it 'unfortunate' - Social News XYZ](https://www.socialnews.xyz/2026/04/20/rajasthan-cm-orders-high-level-probe-into-pachpadra-refinery-fire-calls-it-unfortunate/) | socialnews.xyz | 8 | negative |
| 20 Apr 2026 | [Fire at Rajasthan Pachpadra Refinery a day before inauguration; situation brought under control](https://munsifdaily.com/fire-at-rajasthan-pachpadra-refinery-a-day/) | munsifdaily.com | 8 | negative |
| 17 Apr 2026 | ['Plenty of fuel': Tasmanian government says Geelong refinery fire won't be a problem](https://www.abc.net.au/news/2026-04-17/viva-geelong-refinery-fire-impact-on-tasmania-petrol-diesel/106574822) | abc.net.au | 8 | positive |
| 16 Apr 2026 | [Australien: Großbrand in Öl-Raffinerie verschärft Treibstoffkrise dramatisch](https://www.braunschweiger-zeitung.de/panorama/article411728210/grossbrand-in-oel-raffinerie-verschaerft-australiens-treibstoffkrise.html) | braunschweiger-zeitung.de | 8 | negative |
| 11 Apr 2026 | [Bangladesh eyes India route to refine Russian crude amid supply crunch - The Economic Times](http://economictimes.indiatimes.com/news/india/bangladesh-eyes-india-route-to-refine-russian-crude-amid-supply-crunch/printarticle/130196122.cms) ⚠ | economictimes.indiatimes.com | 8 | positive |
| 11 Apr 2026 | [Bangladesh eyes India route to refine Russian crude amid supply crunch](https://economictimes.indiatimes.com/news/india/bangladesh-eyes-india-route-to-refine-russian-crude-amid-supply-crunch/articleshow/130196122.cms) ⚠ | economictimes.indiatimes.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "refinery" --since 2026-01-01 --until 2026-04-30
prism-news trends "refinery" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "refinery" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "refinery", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "refinery", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Air Pollution Industry](air-pollution-industry.md)
- [Lithium News](lithium-news.md)
- [Energy Storage News](energy-storage-news.md)
- [Emissions Industry](emissions-industry.md)
