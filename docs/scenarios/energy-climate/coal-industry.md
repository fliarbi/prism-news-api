# Coal Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “coal industry” · 480/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [coal-industry.json](../../examples/scenarios/coal-industry.json).

**Question.** How did coal coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="coal"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,463 |
| Negative · neutral · positive | 48% · 3.3% · 49% |
| Critical (priority 7–9) | 72% (9,654 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,191 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | mining safety and regulatory compliance |

## Twelve months of coverage

Monthly matching articles for `coal` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,188 | 69% | 957 | 1,143 | ██████████ |
| Jun 2025 | 1,798 | 70% | 822 | 929 | █████████ |
| Jul 2025 | 2,555 | 64% | 1,308 | 1,154 | ████████████ |
| Aug 2025 | 3,257 | 68% | 1,616 | 1,558 | ████████████████ |
| Sep 2025 | 2,421 | 74% | 975 | 1,376 | ████████████ |
| Oct 2025 | 1,976 | 74% | 746 | 1,183 | █████████ |
| Nov 2025 | 2,037 | 72% | 977 | 983 | ██████████ |
| Dec 2025 | 2,294 | 69% | 938 | 1,293 | ███████████ |
| Jan 2026 | 2,458 | 71% | 983 | 1,391 | ████████████ |
| Feb 2026 | 3,536 | 75% | 1,825 | 1,602 | █████████████████ |
| Mar 2026 | 3,278 | 73% | 1,606 | 1,564 | ████████████████ |
| Apr 2026 | 4,191 | 68% | 2,052 | 1,983 | ████████████████████ |

The last four complete months averaged 3,366 articles a month against 2,450 in the first four (+37%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,543 | 19% |
| India | 2,145 | 16% |
| China | 327 | 2.4% |
| Australia | 236 | 1.8% |
| United Kingdom | 190 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mining safety and regulatory compliance | 621 | 7.2% | +78% |
| mining law and policy frameworks | 719 | 8.4% | +87% |
| renewable energy policy & regulation | 245 | 2.9% | +78% |
| artisanal and small-scale mining challenges | 356 | 4.2% | +122% |
| electricity generation from fossil fuels | 213 | 2.5% | +61% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Feb 2026 | [2014 Grassroots Anti-Coal Movements To Watch](https://www.sierraclub.org/compass/2014/12/2014-grassroots-anti-coal-movements-watch) | sierraclub.org | 9 | negative |
| 5 Feb 2026 | [At least 18 killed and several trapped after blast tears through coal mine](https://www.thescottishsun.co.uk/news/15890189/workers-killed-trapped-india-coal-mine-blast/) | thescottishsun.co.uk | 9 | negative |
| 29 Apr 2026 | [Le Haut conseil pour le climat presse l’État d’accélérer la sortie des énergies fossiles – Entrevue](https://entrevue.fr/environnement/le-haut-conseil-pour-le-climat-presse-letat-daccelerer-la-sortie-des-energies-fossiles/) | entrevue.fr | 8 | negative |
| 29 Apr 2026 | [France unveils plan to ditch all fossil fuels by 2050](https://www.enca.com/opinion/france-unveils-plan-ditch-all-fossil-fuels-2050) | enca.com | 8 | positive |
| 29 Apr 2026 | [France unveils roadmap to ditch all fossil fuels by 2050](https://www.inkl.com/news/france-unveils-roadmap-to-ditch-all-fossil-fuels-by-2050) | inkl.com | 8 | negative |
| 29 Apr 2026 | [California’s state legislature may succeed in destroying its own oil industry, but it won’t change anything…](https://californiaglobe.com/fr/ringside-californias-self-destructive-war-on-oil/) | californiaglobe.com | 8 | negative |
| 28 Apr 2026 | [Renewable energy just broke a 100-year-old streak](https://vox.com/the-highlight/486845/climate-change-coal-solar-renewable-power) | vox.com | 8 | negative |
| 27 Apr 2026 | [India boosts coal and gas output as power demand hits record peak in heatwave - CNBC TV18](https://www.cnbctv18.com/energy/india-boosts-coal-and-gas-output-as-power-demand-hits-record-peak-in-heatwave-ws-l-19894198.htm) | cnbctv18.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "coal" --since 2026-01-01 --until 2026-04-30
prism-news trends "coal" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "coal" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "coal", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "coal", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Natural Gas News](natural-gas-news.md)
- [Petrol Price News](petrol-price-news.md)
- [Cyclone News](cyclone-news.md)
- [Monsoon News](monsoon-news.md)
