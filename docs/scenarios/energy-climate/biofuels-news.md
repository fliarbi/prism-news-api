# Biofuels News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “biofuels news” · 210/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [biofuels-news.json](../../examples/scenarios/biofuels-news.json).

**Question.** How did biofuels coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="biofuels"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,872 |
| Negative · neutral · positive | 27% · 4.8% · 69% |
| Critical (priority 7–9) | 65% (1,210 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (617 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | biofuel production & algae-based energy |

## Twelve months of coverage

Monthly matching articles for `biofuels` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 507 | 42% | 139 | 325 | ████████████████ |
| Jun 2025 | 270 | 64% | 49 | 213 | █████████ |
| Jul 2025 | 290 | 69% | 66 | 219 | █████████ |
| Aug 2025 | 367 | 65% | 81 | 279 | ████████████ |
| Sep 2025 | 425 | 72% | 75 | 344 | ██████████████ |
| Oct 2025 | 397 | 71% | 84 | 298 | █████████████ |
| Nov 2025 | 325 | 69% | 69 | 248 | ███████████ |
| Dec 2025 | 335 | 62% | 53 | 266 | ███████████ |
| Jan 2026 | 320 | 72% | 52 | 257 | ██████████ |
| Feb 2026 | 405 | 60% | 77 | 302 | █████████████ |
| Mar 2026 | 530 | 65% | 190 | 306 | █████████████████ |
| Apr 2026 | 617 | 64% | 179 | 415 | ████████████████████ |

The last four complete months averaged 468 articles a month against 358 in the first four (+31%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 35% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 300 | 16% |
| India | 115 | 6.1% |
| Brazil | 31 | 1.7% |
| United Kingdom | 23 | 1.2% |
| China | 19 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| biofuel production & algae-based energy | 349 | 28% | +14% |
| renewable energy in agriculture (biogas, solar irrigation) | 173 | 14% | +44% |
| biomass energy conversion processes | 137 | 11% | +14% |
| waste-to-energy conversion technologies | 47 | 3.7% | -8% |
| crude oil refining methods | 46 | 3.7% | +188% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [Mother of one of the girls killed in plant explosion files lawsuit against Horizon Biofuels](https://www.ketv.com/article/fremont-plant-explosion-mother-files-lawsuit/71114278) | ketv.com | 8 | negative |
| 16 Apr 2026 | [Advanced Biofuels Market: Share, Growth and Outlook Driven by Renewable Energy Solutions and Decarbonization…](https://www.openpr.com/news/4474475/advanced-biofuels-market-share-growth-and-outlook-driven) | openpr.com | 8 | positive |
| 15 Apr 2026 | [PM Narendra Modi bets big on hydrocarbons and biofuels \| Autocar Professional](http://www.autocarpro.in/news-national/pm-narendra-modi-bets-hydrocarbons-biofuels-22835) | autocarpro.in | 8 | positive |
| 14 Apr 2026 | [ExxonMobil, IIT Madras and IIT Bombay to research on biofuel \| Autocar Professional](https://www.autocarpro.in/news-national/exxonmobil-partners-iit-bombay-and-iit-madras-for-advanced-research-on-biofuels-44380) | autocarpro.in | 8 | positive |
| 9 Apr 2026 | [Chalmers declares renewables are answer to fuel crisis](https://thenightly.com.au/politics/treasurer-jim-chalmers-says-renewable-energy-is-answer-to-fuel-crisis-as-anthony-albanese-visits-singapore--c-22114601) | thenightly.com.au | 8 | negative |
| 3 Apr 2026 | [U.S. Biofuels Target Could Fuel Destruction of Tropical Rainforest](https://www.yahoo.com/news/articles/u-biofuels-target-could-fuel-070000801.html) | yahoo.com | 8 | negative |
| 2 Apr 2026 | ['Failed experiment’: Experts query the true sustainability of biofuels](http://euronews.com/2026/04/02/a-failed-experiment-biofuels-under-the-spotlight-as-eu-scrambles-for-alternative-energy) | euronews.com | 8 | negative |
| 28 Mar 2026 | [For last 15 years, rule of fear, corruption and appeasement politics going on in West Bengal: Amit Shah in…](https://www.devdiscourse.com/article/Newsalert/3853857-for-last-15-years-rule-of-fear-corruption-and-appeasement-politics-going-on-in-west-bengal-amit-shah-in-kolkata) | devdiscourse.com | 8 | negative |
| 27 Mar 2026 | [EPA Finalizes Historic New Renewable Fuel Standards to Strengthen American Energy Security, Support Rural…](https://www.epa.gov/newsreleases/epa-finalizes-historic-new-renewable-fuel-standards-strengthen-american-energy) | epa.gov | 8 | positive |
| 27 Mar 2026 | [A pennycress transparent testa 8 knockout mutant has drastic changes in seed coat anatomy and chemical…](https://pubmed.ncbi.nlm.nih.gov/41685867/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 26 Mar 2026 | [Brazil has a secret weapon against oil shocks](https://www.economist.com/the-americas/2026/03/26/brazil-has-a-secret-weapon-against-oil-shocks) | economist.com | 8 | negative |
| 24 Mar 2026 | [Verbio SE: Zweite Energiekrise in Folge als neuer Katalysator; Schätzungen und Kursziel angehoben; KAUFEN…](https://www.finanznachrichten.de/nachrichten-2026-03/68021446-verbio-se-zweite-energiekrise-in-folge-als-neuer-katalysator-schaetzungen-und-kursziel-angehoben-kaufen-beibehalten-098.htm) | finanznachrichten.de | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "biofuels" --since 2026-01-01 --until 2026-04-30
prism-news trends "biofuels" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "biofuels" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "biofuels", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "biofuels", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Fuel Prices News](fuel-prices-news.md)
- [Battery Storage News](battery-storage-news.md)
- [Green Hydrogen News](green-hydrogen-news.md)
- [Nickel News](nickel-news.md)
