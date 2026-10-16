# EV Batteries News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ev batteries news” · 110/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ev-batteries-news.json](../../examples/scenarios/ev-batteries-news.json).

**Question.** How much ev batteries coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="ev batteries"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 294 |
| Negative · neutral · positive | 11% · 0.3% · 89% |
| Critical (priority 7–9) | 81% (238 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (459 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | lithium-ion battery advancements for evs |

## Twelve months of coverage

Monthly matching articles for `ev batteries` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 50 | 82% | 5 | 45 | ██ |
| Jun 2025 | 51 | 71% | 5 | 44 | ██ |
| Jul 2025 | 74 | 80% | 8 | 66 | ███ |
| Aug 2025 | 459 | 12% | 13 | 446 | ████████████████████ |
| Sep 2025 | 97 | 87% | 33 | 64 | ████ |
| Oct 2025 | 72 | 82% | 9 | 63 | ███ |
| Nov 2025 | 37 | 78% | 5 | 30 | ██ |
| Dec 2025 | 40 | 88% | 9 | 31 | ██ |
| Jan 2026 | 76 | 79% | 1 | 75 | ███ |
| Feb 2026 | 76 | 83% | 9 | 67 | ███ |
| Mar 2026 | 56 | 82% | 11 | 44 | ██ |
| Apr 2026 | 86 | 80% | 10 | 76 | ████ |

The last four complete months averaged 74 articles a month against 158 in the first four (-54%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 38 | 13% |
| China | 22 | 7.5% |
| United Kingdom | 22 | 7.5% |
| India | 16 | 5.4% |
| Switzerland | 8 | 2.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| lithium-ion battery advancements for evs | 78 | 35% | +34% |
| ev battery recycling and sustainability | 73 | 33% | +46% |
| solid-state battery breakthroughs | 35 | 16% | +59% |
| battery charging systems | 28 | 13% | +154% |
| hybrid & electric vehicle components | 17 | 7.7% | +54% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Apr 2026 | [Hyundai Motor Group partners Korea Zinc on nickel value chain for EV business \| Autocar Professional](https://www.autocarpro.in/news-international/hyundai-motor-group-partners-korea-zinc-on-nickel-value-chain-for-ev-business-116571) | autocarpro.in | 8 | positive |
| 10 Feb 2026 | [FAW installs 'industry first' semi-solid-state battery in an EV, promising 1,000+ km range](https://electrek.co/2026/02/10/faw-installs-first-semi-solid-state-ev-battery-with-1000-km-range/) | electrek.co | 8 | positive |
| 20 Jan 2026 | [EV battery sector in China expands by 40% - BatteryIndustry.net](https://batteryindustry.net/ev-battery-sector-in-china-expands-by-40/) | batteryindustry.net | 8 | positive |
| 15 Jan 2026 | [News, 15 January 2026](https://telematicswire.net/catl-locks-in-massive-17-2b-lfp-supply-deal-with-ronbay-to-secure-future-battery-materials/) | telematicswire.net | 8 | positive |
| 22 Apr 2026 | [Axens' MACARON cathode plant earns France's strategic project label and 25% tax credit](https://chargedevs.com/newswire/axens-macaron-cathode-plant-earns-frances-strategic-project-label-and-25-tax-credit/) | chargedevs.com | 7 | positive |
| 15 Apr 2026 | [UK-built cars could miss out on EU grants thanks to new 'Made in Europe' legislation \| Auto Express](https://www.autoexpress.co.uk/news/369384/uk-built-cars-could-miss-out-eu-grants-thanks-new-made-europe-legislation) | autoexpress.co.uk | 7 | negative |
| 3 Apr 2026 | [EV-focused Neuron Energy forays into BESS with 5-GWh factory in India](https://renewablesnow.com/news/ev-focused-neuron-energy-forays-into-bess-with-5-gwh-factory-in-india-1292568) | renewablesnow.com | 7 | positive |
| 21 Mar 2026 | [Asia's EVolution: Indonesia’s nickel powers global electric vehicle boom but at what cost to the country? -…](https://www.chinatechnews.com/2026/03/22/117794-asias-evolution-indonesias-nickel-powers-global-electric-vehicle-boom-but-at-what-cost-to-the-country) | chinatechnews.com | 7 | positive |
| 8 Mar 2026 | [Ranked: U.S. Import Reliance for 37 Critical Minerals](https://aheadoftheherd.com/ranked-u-s-import-reliance-for-37-critical-minerals/) | aheadoftheherd.com | 7 | positive |
| 22 Feb 2026 | [OMC Power enters EV battery repurposing business in partnership with Honda Motors Japan](https://economictimes.indiatimes.com/industry/renewables/omc-power-enters-ev-battery-repurposing-business-in-partnership-with-honda-motors-japan/articleshow/128666647.cms) | economictimes.indiatimes.com | 7 | positive |
| 18 Feb 2026 | [Most EV batteries outlast their cars, real-world data shows](https://electrek.co/2026/02/18/most-ev-batteries-outlast-their-cars-real-world-data-shows/) | electrek.co | 7 | positive |
| 18 Feb 2026 | [Average used EV battery health stands at 95.15%, real-world data shows](https://fleetworld.co.uk/average-used-ev-battery-health-stands-at-95-15-real-world-data-shows/) | fleetworld.co.uk | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ev batteries" --since 2026-01-01 --until 2026-04-30
prism-news trends "ev batteries" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ev batteries" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ev batteries", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ev batteries", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Blockchain News](blockchain-news.md)
- [Autonomous Vehicles News](autonomous-vehicles-news.md)
- [Smart Home News](smart-home-news.md)
- [AI in Education News](ai-in-education-news.md)
