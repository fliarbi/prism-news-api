# 3d Printing Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “3d printing industry” · 590/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [3d-printing-industry.json](../../examples/scenarios/3d-printing-industry.json).

**Question.** How much news did 3d printing receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="3d printing"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,828 |
| Negative · neutral · positive | 6.3% · 0.8% · 93% |
| Critical (priority 7–9) | 52% (2,527 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,326 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | 3d printers and additive manufacturing devices |

## Twelve months of coverage

Monthly matching articles for `3d printing` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 966 | 52% | 37 | 921 | ███████████████ |
| Jun 2025 | 915 | 56% | 27 | 883 | ██████████████ |
| Jul 2025 | 1,082 | 53% | 42 | 1,032 | ████████████████ |
| Aug 2025 | 1,036 | 53% | 29 | 1,002 | ████████████████ |
| Sep 2025 | 994 | 59% | 35 | 953 | ███████████████ |
| Oct 2025 | 1,031 | 58% | 59 | 963 | ████████████████ |
| Nov 2025 | 1,119 | 52% | 36 | 1,070 | █████████████████ |
| Dec 2025 | 1,002 | 59% | 41 | 958 | ███████████████ |
| Jan 2026 | 1,049 | 56% | 56 | 980 | ████████████████ |
| Feb 2026 | 1,226 | 56% | 89 | 1,125 | ██████████████████ |
| Mar 2026 | 1,227 | 49% | 98 | 1,123 | ███████████████████ |
| Apr 2026 | 1,326 | 49% | 61 | 1,254 | ████████████████████ |

The last four complete months averaged 1,207 articles a month against 1,000 in the first four (+21%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 33% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 798 | 17% |
| United Kingdom | 114 | 2.4% |
| China | 113 | 2.3% |
| India | 86 | 1.8% |
| Japan | 50 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| 3d printers and additive manufacturing devices | 1,782 | 51% | +29% |
| additive manufacturing technologies | 309 | 8.8% | -8% |
| industrial 3d printing applications | 289 | 8.2% | -9% |
| prototyping and rapid manufacturing | 190 | 5.4% | -17% |
| nanotechnology in drug delivery systems | 63 | 1.8% | +10% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Artificial Intelligence Enabled Precise 3D Printing of Polyvinylidene Fluoride (PVDF) Microfibers for…](https://pubmed.ncbi.nlm.nih.gov/41974611/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [3D printed photo-sensitized microfiltration membranes for simultaneous water filtration and pathogen…](https://pubmed.ncbi.nlm.nih.gov/41734203/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 21 Apr 2026 | [Printed neurons communicate with living brain cells: A computer efficiency boost?](https://www.digitaljournal.com/tech-science/printed-neurons-communicate-with-living-brain-cells-a-computer-efficiency-boost/article) | digitaljournal.com | 8 | positive |
| 20 Apr 2026 | [Supercapacitor-Powered Electric Wind-Up Plane](https://www.circuitdigest.com/news/supercapacitor-powered-electric-wind-up-plane) | circuitdigest.com | 8 | positive |
| 14 Apr 2026 | [Scientists Used AI to Design a Steel That's 30% Stronger, Never Rusts, and Was Built for 3D Printing From…](https://indiandefencereview.com/scientists-used-ai-design-steel-30-stronger-never-rusts-built-for-3d-printing/) | indiandefencereview.com | 8 | positive |
| 10 Apr 2026 | [L&rsquo;apprentissage automatique conçoit un acier économique et inoxydable pour l&rsquo;impression 3D](https://www.enerzine.com/lapprentissage-automatique-concoit-un-acier-economique-et-inoxydable-pour-limpression-3d/185293-2026-04) | enerzine.com | 8 | positive |
| 7 Apr 2026 | [DTU 3D Prints New Fuel Cell Design With 5x Power Boost - 3DPrint.com \| Additive Manufacturing Business](https://3dprint.com/325013/dtu-3d-prints-new-fuel-cell-design-with-5x-power-boost/) | 3dprint.com | 8 | positive |
| 3 Apr 2026 | [The Industrial Science Report: 3D printing drives programmable industrial materials and new levels of…](https://www.plantservices.com/industrial-science-report/article/55368527/atownshend@endeavorb2b.com) | plantservices.com | 8 | positive |
| 31 Mar 2026 | [Lucknow News: केजीएमयू ने 10 रुपये की लागत से बनी कृत्रिम आंख बनाई](https://www.amarujala.com/lucknow/kgmu-develops-artificial-eye-costing-rs-10-lucknow-news-c-13-knp1002-1670436-2026-04-01) | amarujala.com | 8 | positive |
| 25 Mar 2026 | [Volumetric Printing with Light - ASME](https://www.asme.org/topics-resources/content/volumetric-printing-with-light) | asme.org | 8 | positive |
| 20 Mar 2026 | [3D Bioprinting of Elastic Ear Cartilage - 3Dnatives](https://www.3dnatives.com/en/3d-bioprinting-of-elastic-ear-cartilage-20032026/) | 3dnatives.com | 8 | positive |
| 18 Mar 2026 | [3D printed ears made from human cells stay flexible for weeks in animal tests](https://mhealthspot.com/2026/03/3d-printed-ears-made-from-human-cells-stay-flexible-for-weeks-in-animal-tests/) | mhealthspot.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "3d printing" --since 2026-01-01 --until 2026-04-30
prism-news trends "3d printing" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "3d printing" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "3d printing", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "3d printing", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Aerospace Industry](aerospace-industry.md)
- [Sugar Industry](sugar-industry.md)
- [Agriculture Industry](agriculture-industry.md)
- [Construction Industry](construction-industry.md)
