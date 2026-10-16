# Candida Auris Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “candida auris outbreak” · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [candida-auris-outbreak.json](../../examples/scenarios/candida-auris-outbreak.json).

**Question.** How much candida auris coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="candida auris"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 140 |
| Negative · neutral · positive | 28% · 3.6% · 69% |
| Critical (priority 7–9) | 98% (137 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (57 articles) |
| Most-reported country | United States (11% of matches) |
| Strongest theme by lift | latent infections |

## Twelve months of coverage

Monthly matching articles for `candida auris` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 49 | 98% | 26 | 19 | █████████████████ |
| Jun 2025 | 14 | 93% | 2 | 11 | █████ |
| Jul 2025 | 23 | 100% | 1 | 21 | ████████ |
| Aug 2025 | 40 | 95% | 22 | 16 | ██████████████ |
| Sep 2025 | 34 | 79% | 23 | 10 | ████████████ |
| Oct 2025 | 19 | 84% | 4 | 13 | ███████ |
| Nov 2025 | 19 | 95% | 7 | 10 | ███████ |
| Dec 2025 | 26 | 100% | 10 | 15 | █████████ |
| Jan 2026 | 57 | 100% | 20 | 35 | ████████████████████ |
| Feb 2026 | 29 | 93% | 1 | 27 | ██████████ |
| Mar 2026 | 32 | 100% | 10 | 21 | ███████████ |
| Apr 2026 | 22 | 96% | 8 | 13 | ████████ |

The last four complete months averaged 35 articles a month against 32 in the first four (+11%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 19% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 16 | 11% |
| Norway | 4 | 2.9% |
| India | 2 | 1.4% |
| France | 1 | 0.7% |
| Italy | 1 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| latent infections | 27 | 23% | +8% |
| antimicrobial stewardship programs | 27 | 23% | +170% |
| opportunistic infections in immunocompromised patients | 68 | 59% | +42% |
| diagnosis of atypical pathogens | 24 | 21% | +85% |
| endotoxin-mediated septic shock | 57 | 49% | +24% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Mar 2026 | [Understanding the epidemiology of Candidozyma auris: a case-control study at an acute hospital in London, UK.](https://pubmed.ncbi.nlm.nih.gov/41831616/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 25 Mar 2026 | [Mortality of Candidozyma auris Candidemia Compared with Non-C. auris Candidemia.](https://pubmed.ncbi.nlm.nih.gov/42042329/) | pubmed.ncbi.nlm.nih.gov | 7 | negative |
| 1 Mar 2026 | [Successful Management of Candida auris Bloodstream Infection in an Elderly Patient: A Case Report.](https://pubmed.ncbi.nlm.nih.gov/41743364/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 4 Jan 2026 | [Síntomas y cómo se contagia el hongo mortal que se propaga de California a Carolina del Norte: lo que dicen…](https://www.lanacion.com.ar/estados-unidos/sintomas-y-como-se-contagia-el-hongo-mortal-que-se-propaga-de-california-a-carolina-del-norte-lo-que-nid04012026/) | lanacion.com.ar | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "candida auris" --since 2026-01-01 --until 2026-04-30
prism-news trends "candida auris" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "candida auris" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "candida auris", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "candida auris", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Sepsis News](sepsis-news.md)
- [Dengue News](dengue-news.md)
- [Lung Cancer News](lung-cancer-news.md)
- [Epidemic Outbreak](epidemic-outbreak.md)
