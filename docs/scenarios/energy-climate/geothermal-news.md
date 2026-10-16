# Geothermal News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “geothermal news” · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [geothermal-news.json](../../examples/scenarios/geothermal-news.json).

**Question.** How did geothermal coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="geothermal"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,288 |
| Negative · neutral · positive | 9.9% · 3.6% · 86% |
| Critical (priority 7–9) | 57% (732 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (413 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | geothermal energy extraction & utilization |

## Twelve months of coverage

Monthly matching articles for `geothermal` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 161 | 61% | 8 | 150 | ████████ |
| Jun 2025 | 270 | 64% | 25 | 237 | █████████████ |
| Jul 2025 | 211 | 54% | 35 | 168 | ██████████ |
| Aug 2025 | 206 | 63% | 25 | 178 | ██████████ |
| Sep 2025 | 356 | 64% | 32 | 316 | █████████████████ |
| Oct 2025 | 167 | 69% | 16 | 145 | ████████ |
| Nov 2025 | 193 | 59% | 27 | 159 | █████████ |
| Dec 2025 | 244 | 57% | 19 | 215 | ████████████ |
| Jan 2026 | 222 | 52% | 16 | 204 | ███████████ |
| Feb 2026 | 305 | 60% | 29 | 267 | ███████████████ |
| Mar 2026 | 348 | 54% | 39 | 301 | █████████████████ |
| Apr 2026 | 413 | 60% | 44 | 342 | ████████████████████ |

The last four complete months averaged 322 articles a month against 212 in the first four (+52%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 59% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 373 | 29% |
| Philippines | 36 | 2.8% |
| Germany | 31 | 2.4% |
| Kenya | 28 | 2.2% |
| United Kingdom | 27 | 2.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| geothermal energy extraction & utilization | 497 | 59% | +44% |
| geothermal heat pump applications | 484 | 57% | +44% |
| offshore drilling operations | 54 | 6.4% | +238% |
| renewable energy policy & regulation | 25 | 3.0% | +127% |
| oil field automation systems | 24 | 2.9% | +243% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 26 Jan 2026 | [Equinix Commits $7 Million to Advance Singapore’s Low Carbon Energy Options](https://esgnews.com/equinix-commits-7-million-to-advance-singapores-low-carbon-energy-options/) | esgnews.com | 8 | positive |
| 28 Apr 2026 | [Constellation Energy Corporation Declares Dividend](https://www.constellationenergy.com/news/2026/04/constellation-energy-corporation-declares-dividend-q3-2025.html) | constellationenergy.com | 7 | positive |
| 27 Apr 2026 | [Central and eastern europe’s next energy alliance is taking shape, and it runs on geothermal](https://ceenergynews.com/voices/central-eastern-europe-geothermal/) | ceenergynews.com | 7 | negative |
| 22 Apr 2026 | [Geothermal the key to Türkiye’s energy independence](https://www.thinkgeoenergy.com/geothermal-the-key-to-turkiyes-energy-independence/) | thinkgeoenergy.com | 7 | positive |
| 21 Apr 2026 | [Geothermal Could Cover 64% of AI Data Center Energy Demand by 2030 - ChinaTechNews.com](https://www.chinatechnews.com/2026/04/22/120289-geothermal-could-cover-64-of-ai-data-center-energy-demand-by-2030) | chinatechnews.com | 7 | positive |
| 20 Apr 2026 | [Vulcan Energy Aktie: Siemens-Pakt besiegelt!](https://www.boerse-express.com/news/articles/vulcan-energy-aktie-siemens-pakt-besiegelt-894649) | boerse-express.com | 7 | positive |
| 16 Apr 2026 | [Zanskar lands novel USD-40m development facility to finance geothermal](https://renewablesnow.com/news/zanskar-lands-novel-usd-40m-development-facility-to-finance-geothermal-1293197/) | renewablesnow.com | 7 | positive |
| 15 Apr 2026 | [EIG holds initial closing of fund focused on geothermal power projects](https://www.energyglobal.com/other-renewables/15042026/eig-holds-initial-closing-of-fund-focused-on-geothermal-power-projects/) | energyglobal.com | 7 | positive |
| 6 Apr 2026 | [Sustainable: Age of geothermal has arrived in Minnesota](https://finance-commerce.com/2026/04/minnesota-geothermal-aquifer-heating-cooling/) | finance-commerce.com | 7 | positive |
| 19 Mar 2026 | [Enhanced geothermal deployment could be compressed to under 3 years: report](https://www.utilitydive.com/news/enhanced-geothermal-deployment-could-be-compressed-under-three-years-repor/815227/) | utilitydive.com | 7 | positive |
| 27 Feb 2026 | [Gradient Geothermal signs partnership to power AI factories with geothermal](https://www.thinkgeoenergy.com/gradient-geothermal-signs-partnership-to-power-ai-factories-with-geothermal/) | thinkgeoenergy.com | 7 | positive |
| 9 Feb 2026 | [The Architect and the Inheritance: How Dr. James Bose’s Vision Made the Geothermal Boom Possible](https://www.phcppros.com/articles/22621-the-architect-and-the-inheritance-how-dr-james-boses-vision-made-the-geothermal-boom-possible) | phcppros.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "geothermal" --since 2026-01-01 --until 2026-04-30
prism-news trends "geothermal" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "geothermal" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "geothermal", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "geothermal", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Glacier News](glacier-news.md)
- [Circular Economy News](circular-economy-news.md)
- [Energy Efficiency Industry](energy-efficiency-industry.md)
