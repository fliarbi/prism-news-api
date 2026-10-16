# E Coli Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “e coli outbreak” · 2,400/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [e-coli-outbreak.json](../../examples/scenarios/e-coli-outbreak.json).

**Question.** How much e coli coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="E. coli"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,616 |
| Negative · neutral · positive | 48% · 3.5% · 49% |
| Critical (priority 7–9) | 88% (1,417 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (506 articles) |
| Most-reported country | United States (22% of matches) |
| Strongest theme by lift | antimicrobial stewardship programs |

## Twelve months of coverage

Monthly matching articles for `E. coli` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 295 | 81% | 111 | 170 | ████████████ |
| Jun 2025 | 329 | 84% | 140 | 170 | █████████████ |
| Jul 2025 | 320 | 74% | 126 | 179 | █████████████ |
| Aug 2025 | 506 | 83% | 283 | 210 | ████████████████████ |
| Sep 2025 | 311 | 82% | 107 | 187 | ████████████ |
| Oct 2025 | 291 | 88% | 128 | 151 | ████████████ |
| Nov 2025 | 268 | 86% | 84 | 166 | ███████████ |
| Dec 2025 | 335 | 88% | 126 | 194 | █████████████ |
| Jan 2026 | 346 | 84% | 87 | 238 | ██████████████ |
| Feb 2026 | 335 | 88% | 143 | 179 | █████████████ |
| Mar 2026 | 452 | 92% | 252 | 187 | ██████████████████ |
| Apr 2026 | 483 | 86% | 285 | 186 | ███████████████████ |

The last four complete months averaged 404 articles a month against 362 in the first four (+11%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 30% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 354 | 22% |
| United Kingdom | 25 | 1.6% |
| India | 21 | 1.3% |
| Canada | 15 | 0.9% |
| Australia | 9 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| antimicrobial stewardship programs | 135 | 12% | +2% |
| proteomic profiling and protein interactions | 58 | 5.0% | -2% |
| treatment of multidrug-resistant organisms | 115 | 10.0% | +2% |
| bioremediation techniques for ecosystems | 48 | 4.2% | -8% |
| biotechnology innovations in medicine | 39 | 3.4% | +15% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Un motocycliste perd la vie après avoir percuté un arbre dans la province d'Anvers](http://www.dhnet.be/actu/faits/2026/04/25/un-motocycliste-perd-la-vie-apres-avoir-percute-un-arbre-dans-la-province-danvers-SED2U7QY4FCHDE5BCOG7OHGIAU/) | dhnet.be | 9 | negative |
| 27 Mar 2026 | [FDA Reports More Severe E. Coli Illnesses Linked to Raw Cheese From a California Farm](https://www.today.com/health/recall/fda-reports-severe-e-coli-illnesses-linked-raw-cheese-california-farm-rcna265405) | today.com | 9 | negative |
| 27 Mar 2026 | [Outbreak linked to raw cheese grows; 9 cases total, one with kidney failure](https://arstechnica.com/health/2026/03/kidney-failure-case-reported-in-raw-cheese-outbreak-maker-still-denies-link/) | arstechnica.com | 9 | negative |
| 27 Mar 2026 | [E. coli illnesses, kidney damage, linked to raw cheese from a California dairy farm](https://www.nbcnews.com/health/health-news/e-coli-kidney-raw-milk-cheese-california-dairy-farm-fda-rcna265460) | nbcnews.com | 9 | negative |
| 27 Mar 2026 | [9 sickened in E. coli outbreak tied to a California company's raw milk and cheese - WWAYTV3](https://www.wwaytv3.com/9-sickened-in-e-coli-outbreak-tied-to-a-california-companys-raw-milk-and-cheese/) | wwaytv3.com | 9 | negative |
| 27 Mar 2026 | [9 sickened in E. coli outbreak tied to a California company’s raw milk and cheese](https://www.sandiegouniontribune.com/2026/03/26/raw-milk-cheese-e-coli-raw-farm/) | sandiegouniontribune.com | 9 | negative |
| 27 Mar 2026 | [9 sickened in E. coli outbreak tied to a California company's raw milk and cheese](https://www.yahoo.com/news/articles/9-sickened-e-coli-outbreak-000249890.html) | yahoo.com | 9 | negative |
| 9 Feb 2026 | [E. coli Outbreak Linked to McDonald's Quarter Pounders - CDC News - News Directory 3](https://www.newsdirectory3.com/e-coli-outbreak-linked-to-mcdonalds-quarter-pounders-cdc-news/) | newsdirectory3.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "E. coli" --since 2026-01-01 --until 2026-04-30
prism-news trends "E. coli" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "E. coli" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "E. coli", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "E. coli", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Bird Flu News](bird-flu-news.md)
- [HIV News](hiv-news.md)
- [Salmonella Outbreak](salmonella-outbreak.md)
- [Norovirus Outbreak](norovirus-outbreak.md)
