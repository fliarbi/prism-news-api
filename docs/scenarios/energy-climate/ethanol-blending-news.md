# Ethanol Blending News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ethanol blending news” · 390/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ethanol-blending-news.json](../../examples/scenarios/ethanol-blending-news.json).

**Question.** How did ethanol blending coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="ethanol blending"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 306 |
| Negative · neutral · positive | 16% · 2.9% · 81% |
| Critical (priority 7–9) | 50% (152 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (143 articles) |
| Most-reported country | India (28% of matches) |
| Strongest theme by lift | biofuel production & algae-based energy |

## Twelve months of coverage

Monthly matching articles for `ethanol blending` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 83% | 1 | 11 | ██ |
| Jun 2025 | 11 | 82% | 3 | 8 | ██ |
| Jul 2025 | 31 | 68% | 7 | 24 | ████ |
| Aug 2025 | 83 | 51% | 15 | 67 | ████████████ |
| Sep 2025 | 64 | 75% | 31 | 33 | █████████ |
| Oct 2025 | 23 | 87% | 8 | 15 | ███ |
| Nov 2025 | 76 | 12% | 3 | 73 | ███████████ |
| Dec 2025 | 20 | 60% | 0 | 20 | ███ |
| Jan 2026 | 17 | 94% | 2 | 15 | ██ |
| Feb 2026 | 13 | 46% | 1 | 10 | ██ |
| Mar 2026 | 143 | 29% | 17 | 124 | ████████████████████ |
| Apr 2026 | 133 | 67% | 28 | 100 | ███████████████████ |

The last four complete months averaged 76 articles a month against 34 in the first four (+123%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 36% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 85 | 28% |
| United States | 8 | 2.6% |
| Brazil | 6 | 2.0% |
| Iran | 5 | 1.6% |
| Nepal | 2 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| biofuel production & algae-based energy | 37 | 22% | +164% |
| vehicle dimensions and cargo space specs | 18 | 11% | new |
| crude oil refining methods | 14 | 8.3% | +600% |
| emission control & catalytic converters | 14 | 8.3% | +100% |
| renewable energy in agriculture (biogas, solar irrigation) | 11 | 6.5% | +22% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Gadkari calls for 100% ethanol blending as West Asia crisis exposes supply vulnerabilities](https://www.auto.economictimes.indiatimes.com/news/industry/indias-push-for-100-ethanol-blending-amid-west-asia-energy-crisis/130416738) | auto.economictimes.indiatimes.com | 8 | positive |
| 13 Apr 2026 | [West Asia Conflict: Govt hints at 21% ethanol blending](https://www.thehindubusinessline.com/economy/west-asia-conflict-govt-hints-at-21-ethanol-blending/article70858219.ece) | thehindubusinessline.com | 8 | positive |
| 29 Mar 2026 | [Ethanol blending to cut fuel imports: PM's big E20 push amid Hormuz crisis](https://www.indiatoday.in/india/story/ethanol-blending-fuel-imports-pm-modi-e20-push-hormuz-iran-west-asia-middle-east-crisis-2888577-2026-03-29) | indiatoday.in | 8 | positive |
| 24 Mar 2026 | [India looks to accelerate ethanol push as oil price shock creates fresh urgency to cut import dependence](https://www.fortuneindia.com/business-news/india-looks-to-accelerate-ethanol-push-as-oil-price-shock-creates-fresh-urgency-to-cut-import-dependence/131539) | fortuneindia.com | 8 | negative |
| 23 Mar 2026 | [Crisis in West Asia created negative impact on world economy, people: PM Modi in Lok Sabha. \| Newsalert](https://www.devdiscourse.com/article/Newsalert/3847011-crisis-in-west-asia-created-negative-impact-on-world-economy-people-pm-modi-in-lok-sabha) | devdiscourse.com | 8 | neutral |
| 7 Mar 2026 | [From Fields to Fuel: The Agricultural Side of India’s Bioenergy Push](https://eng.ruralvoice.in/opinion/from-fields-to-fuel-the-agricultural-side-of-india’s-bioenergy-push.html) | eng.ruralvoice.in | 8 | positive |
| 28 Jan 2026 | [Ethanol Blending at Twenty Percent Cuts India’s Forex Outgo by $19.3 Billion \| Chemical Industry Digest](https://chemindigest.com/ethanol-blending-at-twenty-percent-cuts-indias-forex-outgo-by-19-3-billion/) | chemindigest.com | 8 | positive |
| 27 Jan 2026 | [India's $19.3B Forex Savings from 20% Ethanol Blending, 100 GW Nuclear Goal](https://www.newkerala.com/news/a/india-saved-usd-193-billion-forex-20-ethanol-445.htm) | newkerala.com | 8 | positive |
| 29 Apr 2026 | [Govt clears legal path for 100% ethanol-powered vehicles](https://www.thehindubusinessline.com/incoming/govt-clears-legal-path-for-100-ethanol-powered-vehicles/article70921054.ece) | thehindubusinessline.com | 7 | positive |
| 28 Apr 2026 | [Government could raise ethanol blending in petrol - Introduction \| Autocar India](https://www.autocarindia.com/industry/government-pushes-to-raise-ethanol-blending-439584) | autocarindia.com | 7 | positive |
| 26 Apr 2026 | [Ethanol Blending: Govt pushes ethanol blending beyond 20%; vehicle impact remains concern \| India News - The…](https://timesofindia.indiatimes.com/india/govt-pushes-ethanol-blending-beyond-20-vehicle-impact-remains-concern/articleshow/130538626.cms) | timesofindia.indiatimes.com | 7 | positive |
| 22 Apr 2026 | [Govt Clears Ethanol Blending In ATF, New Rules Aim To Boost SAF And Cut Oil Imports](https://www.freepressjournal.in/business/govt-clears-ethanol-blending-in-atf-new-rules-aim-to-boost-saf-and-cut-oil-imports) | freepressjournal.in | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ethanol blending" --since 2026-01-01 --until 2026-04-30
prism-news trends "ethanol blending" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ethanol blending" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ethanol blending", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ethanol blending", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Heat Pumps News](heat-pumps-news.md)
- [Wind Turbines Industry](wind-turbines-industry.md)
- [Carbon Capture News](carbon-capture-news.md)
- [Deforestation News](deforestation-news.md)
