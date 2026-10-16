# Deforestation News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “deforestation news” · 260/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [deforestation-news.json](../../examples/scenarios/deforestation-news.json).

**Question.** How did deforestation coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="deforestation"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,863 |
| Negative · neutral · positive | 51% · 2.0% · 47% |
| Critical (priority 7–9) | 82% (1,529 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (918 articles) |
| Most-reported country | United States (8.3% of matches) |
| Strongest theme by lift | biodiversity conservation efforts |

## Twelve months of coverage

Monthly matching articles for `deforestation` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 821 | 75% | 479 | 285 | ██████████████████ |
| Jun 2025 | 414 | 83% | 241 | 167 | █████████ |
| Jul 2025 | 564 | 73% | 302 | 248 | ████████████ |
| Aug 2025 | 515 | 81% | 282 | 210 | ███████████ |
| Sep 2025 | 572 | 85% | 294 | 265 | ████████████ |
| Oct 2025 | 600 | 83% | 373 | 216 | █████████████ |
| Nov 2025 | 918 | 86% | 509 | 369 | ████████████████████ |
| Dec 2025 | 610 | 88% | 376 | 220 | █████████████ |
| Jan 2026 | 403 | 86% | 227 | 166 | █████████ |
| Feb 2026 | 424 | 82% | 192 | 224 | █████████ |
| Mar 2026 | 433 | 84% | 231 | 192 | █████████ |
| Apr 2026 | 603 | 77% | 293 | 292 | █████████████ |

The last four complete months averaged 466 articles a month against 578 in the first four (-19%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 155 | 8.3% |
| Brazil | 84 | 4.5% |
| Indonesia | 79 | 4.2% |
| India | 78 | 4.2% |
| Afghanistan | 48 | 2.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| biodiversity conservation efforts | 617 | 43% | -35% |
| deforestation prevention campaigns | 608 | 43% | -34% |
| environmental policy and legislation | 151 | 11% | -8% |
| forest carbon sequestration and climate change mitigation | 40 | 2.8% | -47% |
| sustainable urban planning initiatives | 38 | 2.7% | +138% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Global forest loss slows but El NiÃ±o fires could threaten progress](https://www.bbc.co.uk/news/articles/c78q5pygn66o) | bbc.co.uk | 9 | negative |
| 29 Apr 2026 | [Tropical forest loss eases after record year: researchers](https://phys.org/news/2026-04-tropical-forest-loss-eases-year.html) | phys.org | 9 | negative |
| 29 Apr 2026 | [‘Encouraging’: Global rainforest loss slows in 2025 after record year](http://www.aljazeera.com/news/2026/4/29/tropical-forest-loss-slows-in-2025-after-record-year-report) | aljazeera.com | 9 | negative |
| 12 Apr 2026 | [El futuro de los bosques de todo el mundo se juega en Europa: así es su papel clave para frenar la…](https://www.elespanol.com/enclave-ods/historias/20260413/futuro-bosques-mundo-juega-europa-papel-clave-frenar-deforestacion/1003744202499_0.html) | elespanol.com | 9 | negative |
| 18 Feb 2026 | [Brasil encontrou rumo no combate ao desmatamento](https://oglobo.globo.com/opiniao/editorial/coluna/2026/02/brasil-encontrou-rumo-no-combate-ao-desmatamento.ghtml) | oglobo.globo.com | 9 | negative |
| 29 Jan 2026 | [Flood losses set to soar 1,000% in South-east Asia: insurance firm study](https://www.businesstimes.com.sg/esg/flood-losses-set-soar-1000-south-east-asia-insurance-firm-study) | businesstimes.com.sg | 9 | negative |
| 20 Jan 2026 | [The Amazon Loses the Equivalent of Six Football Fields Per Minute, WWF Warns](https://colombiaone.com/2026/01/20/amazon-loses-six-football-fields-wwf/) | colombiaone.com | 9 | negative |
| 30 Apr 2026 | [Forest bump: Fewer trees being felled](http://www.csmonitor.com/Editorials/the-monitors-view/2026/0430/Forest-bump-Fewer-trees-being-felled) | csmonitor.com | 8 | negative |
| 29 Apr 2026 | [Regenwald: Zerstörung ging 2025 um mehr als ein Drittel zurück](https://www.faz.net/aktuell/wirtschaft/mehr-wirtschaft/regenwald-zerstoerung-ging-2025-um-mehr-als-ein-drittel-zurueck-accg-200776585.html) | faz.net | 8 | negative |
| 27 Apr 2026 | [Une école pour les enfants qui souffrent en Haïti avec l'association Main dans la Main](http://www.lindependant.fr/2026/04/27/une-ecole-pour-les-enfants-qui-souffrent-en-haiti-avec-lassociation-main-dans-la-main-13345552.php) | lindependant.fr | 8 | negative |
| 27 Apr 2026 | [US lawmakers urge EU not to water down deforestation law in review](http://www.euronews.com/my-europe/2026/04/27/us-lawmakers-urge-eu-not-to-water-down-deforestation-law-ahead-of-review) | euronews.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "deforestation" --since 2026-01-01 --until 2026-04-30
prism-news trends "deforestation" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "deforestation" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "deforestation", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "deforestation", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Ethanol Blending News](ethanol-blending-news.md)
- [Carbon Capture News](carbon-capture-news.md)
- [Drought News](drought-news.md)
- [Glacier News](glacier-news.md)
