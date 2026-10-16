# Heat Pumps News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “heat pumps news” · 20/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [heat-pumps-news.json](../../examples/scenarios/heat-pumps-news.json).

**Question.** How did heat pumps coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="heat pumps"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,626 |
| Negative · neutral · positive | 43% · 1.4% · 56% |
| Critical (priority 7–9) | 34% (559 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (588 articles) |
| Most-reported country | United States (10% of matches) |
| Strongest theme by lift | energy-efficient home solutions |

## Twelve months of coverage

Monthly matching articles for `heat pumps` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 179 | 44% | 25 | 150 | ██████ |
| Jun 2025 | 146 | 48% | 32 | 111 | █████ |
| Jul 2025 | 184 | 48% | 39 | 144 | ██████ |
| Aug 2025 | 190 | 43% | 29 | 158 | ██████ |
| Sep 2025 | 239 | 42% | 43 | 192 | ████████ |
| Oct 2025 | 169 | 40% | 26 | 141 | ██████ |
| Nov 2025 | 218 | 48% | 32 | 183 | ███████ |
| Dec 2025 | 171 | 45% | 41 | 128 | ██████ |
| Jan 2026 | 238 | 50% | 52 | 183 | ████████ |
| Feb 2026 | 588 | 23% | 350 | 230 | ████████████████████ |
| Mar 2026 | 465 | 34% | 243 | 217 | ████████████████ |
| Apr 2026 | 335 | 43% | 55 | 272 | ███████████ |

The last four complete months averaged 406 articles a month against 175 in the first four (+133%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 31% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 169 | 10% |
| United Kingdom | 163 | 10% |
| Germany | 33 | 2.0% |
| China | 21 | 1.3% |
| France | 14 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| energy-efficient home solutions | 66 | 11% | +74% |
| geothermal heat pump applications | 48 | 8.0% | +4% |
| geothermal energy extraction & utilization | 48 | 8.0% | +23% |
| renewable energy policy & regulation | 38 | 6.4% | +375% |
| solar photovoltaic (pv) energy systems | 109 | 18% | +541% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [Attention: UK Bans Fuel Gas in New Building from 2028 - SPRSUN](https://sprsunheatpump.com/attention-uk-bans-fuel-gas-in-new-building-from-2028.html) | sprsunheatpump.com | 8 | positive |
| 6 Apr 2026 | [European Energy Crisis Accelerates Renewable Adoption as Fossil Fuel Prices Soar](https://advos.io/en/european-energy-crisis-accelerates-renewable-adoption-as-fossil-/202630560) | advos.io | 8 | negative |
| 31 Mar 2026 | [New residential heat pumps save Germany 1.3 billion euros on LNG imports over three years, according to new…](https://www.renewableenergymagazine.com/miscellaneous/new-residential-heat-pumps-save-germany-1-20260331) | renewableenergymagazine.com | 8 | negative |
| 30 Mar 2026 | [Heat pumps facing a ‘wave of disinformation’: Do they work in cold weather and old buildings?](https://au.news.yahoo.com/heat-pumps-facing-wave-disinformation-110408489.html) | au.news.yahoo.com | 8 | negative |
| 30 Mar 2026 | [From cold countries to old buildings: How well do heat pumps work?](http://www.euronews.com/2026/03/30/heat-pumps-facing-a-wave-of-disinformation-do-they-work-in-cold-weather-and-old-buildings) | euronews.com | 8 | negative |
| 27 Mar 2026 | [Energy Shock From Iran War Pushes More Consumers Towards EVs, Solar, and Heat Pumps](https://www.ibtimes.com/energy-shock-iran-war-pushes-more-consumers-towards-evs-solar-heat-pumps-3800393) | ibtimes.com | 8 | negative |
| 24 Mar 2026 | [Lower – or even zero – bills in newbuild homes as clean tech takes off](https://www.somersetcountygazette.co.uk/news/national/25964488.lower---even-zero---bills-newbuild-homes-clean-tech-takes-off/) | somersetcountygazette.co.uk | 8 | positive |
| 1 Mar 2026 | [California wants millions of heat pumps. High power bills might get in the way](https://www.latimes.com/california/story/2026-03-01/california-wants-millions-of-heat-pumps-high-power-bills-might-get-in-way) | latimes.com | 8 | negative |
| 25 Feb 2026 | [Scotland's Heat Pump Installation Plan Criticized as Too Slow](https://world.infonasional.com/scotland-heat-pump-plan-too-slow) | world.infonasional.com | 8 | positive |
| 12 Feb 2026 | [Solid-state electrocaloric materials heat up cooling performance - The American Ceramic Society](https://ceramics.org/ceramic-tech-today/solid-state-electrocaloric-materials-heat-up-cooling-performance/) | ceramics.org | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "heat pumps" --since 2026-01-01 --until 2026-04-30
prism-news trends "heat pumps" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "heat pumps" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "heat pumps", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "heat pumps", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Air Quality News](air-quality-news.md)
- [Pipeline News](pipeline-news.md)
- [Wind Turbines Industry](wind-turbines-industry.md)
- [Ethanol Blending News](ethanol-blending-news.md)
