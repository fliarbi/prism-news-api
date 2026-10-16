# Power Outage News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “power outage news” · 30/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [power-outage-news.json](../../examples/scenarios/power-outage-news.json).

**Question.** How did power outage coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="power outage"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,046 |
| Negative · neutral · positive | 81% · 1.3% · 18% |
| Critical (priority 7–9) | 73% (1,491 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (660 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | electricity grid resilience & disaster recovery |

## Twelve months of coverage

Monthly matching articles for `power outage` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 660 | 76% | 570 | 80 | ████████████████████ |
| Jun 2025 | 376 | 82% | 329 | 47 | ███████████ |
| Jul 2025 | 431 | 68% | 335 | 91 | █████████████ |
| Aug 2025 | 382 | 68% | 306 | 74 | ████████████ |
| Sep 2025 | 245 | 68% | 175 | 66 | ███████ |
| Oct 2025 | 270 | 71% | 202 | 67 | ████████ |
| Nov 2025 | 174 | 73% | 133 | 39 | █████ |
| Dec 2025 | 343 | 84% | 288 | 48 | ██████████ |
| Jan 2026 | 521 | 74% | 413 | 103 | ████████████████ |
| Feb 2026 | 423 | 70% | 330 | 84 | █████████████ |
| Mar 2026 | 555 | 75% | 470 | 75 | █████████████████ |
| Apr 2026 | 547 | 72% | 443 | 97 | █████████████████ |

The last four complete months averaged 512 articles a month against 462 in the first four (+11%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 374 | 18% |
| India | 58 | 2.8% |
| Canada | 49 | 2.4% |
| Ghana | 37 | 1.8% |
| Nigeria | 27 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| electricity grid resilience & disaster recovery | 328 | 24% | +73% |
| electricity distribution networks & management | 354 | 26% | +108% |
| electricity transmission infrastructure & grid systems | 101 | 7.3% | +140% |
| weather-related travel disruptions | 59 | 4.3% | +638% |
| power quality analysis & harmonic filtering technologies | 78 | 5.6% | +62% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Feb 2026 | [Chief says more funding needed to repair homes after power outage, flooding](https://www.winnipegfreepress.com/breakingnews/2026/02/28/chief-says-more-funding-needed-to-repair-homes-after-power-outage-flooding) | winnipegfreepress.com | 9 | negative |
| 22 Feb 2026 | [Ukraine Faces Scheduled Power Outages on February 23 After Drone Attacks](https://mezha.net/eng/bukvy/ukraine-faces-scheduled-power-outages-on-february-23-after-drone-attacks/) | mezha.net | 9 | negative |
| 12 Feb 2026 | [Odesa Faces Power Outage After Russian Drone Strikes](https://world.infonasional.com/odesa-power-outage-russian-strikes) | world.infonasional.com | 9 | negative |
| 14 Jan 2026 | [Energy crisis in Kyiv unprecedented, Mayor says \| Ukraine News](https://kyivindependent.com/explosions-in-kyiv-energy-infrastructure-air-defense/) | kyivindependent.com | 9 | negative |
| 27 Apr 2026 | [One year on: Spain’s 2025 blackout still haunts millions](https://euroweeklynews.com/2026/04/27/apagon-power-outage-one-year-on-spains-2025-blackout-still-haunts-millions-as-claims-deadline-expires/) | euroweeklynews.com | 8 | negative |
| 24 Apr 2026 | [Power outage hits Orange Beach](https://www.yahoo.com/news/articles/power-outage-hits-orange-beach-212842633.html) | yahoo.com | 8 | negative |
| 23 Apr 2026 | [5 Advocates Trapped Between Floors in Court Lift After Power Cut](https://www.awamkasach.com/5-advocates-trapped-between-floors-in-court-lift-after-power-cut/) | awamkasach.com | 8 | negative |
| 23 Apr 2026 | [Expert report identifies causes of Iberian blackout](https://www.pveurope.eu/grid-connection/expert-report-identifies-causes-iberian-blackout) | pveurope.eu | 8 | negative |
| 22 Apr 2026 | [Thousands wake to no power after blackout in Perth Hills](https://www.thewest.com.au/news/perth/power-outage-leaves-1600-customers-in-roleystone-and-martin-without-power-for-at-least-seven-hours-c-22179930) | thewest.com.au | 8 | negative |
| 20 Apr 2026 | [Residents of Lagos community protest 18 months without electricity](https://www.premiumtimesng.com/regional/ssouth-west/873388-residents-of-lagos-community-protest-18-months-without-electricity.html) | premiumtimesng.com | 8 | negative |
| 16 Apr 2026 | [Outage knocks out power to hundreds in SLO County. When will it be back on?](https://www.yahoo.com/news/articles/outage-knocks-power-hundreds-slo-195512265.html) | yahoo.com | 8 | negative |
| 15 Apr 2026 | [Dozens of homes without heat after days-long power outage in Nunavut hamlet](https://halifax.citynews.ca/2026/04/15/dozens-of-homes-without-heat-after-days-long-power-outage-in-nunavut-hamlet/) | halifax.citynews.ca | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "power outage" --since 2026-01-01 --until 2026-04-30
prism-news trends "power outage" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "power outage" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "power outage", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "power outage", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Energy Storage News](energy-storage-news.md)
- [Emissions Industry](emissions-industry.md)
- [Wind Energy News](wind-energy-news.md)
- [Heatwave News](heatwave-news.md)
