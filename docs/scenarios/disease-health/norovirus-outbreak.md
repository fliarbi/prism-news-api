# Norovirus Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “norovirus outbreak” · 390/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [norovirus-outbreak.json](../../examples/scenarios/norovirus-outbreak.json).

**Question.** How much norovirus coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="norovirus"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 729 |
| Negative · neutral · positive | 79% · 2.5% · 19% |
| Critical (priority 7–9) | 74% (541 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (275 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | community-acquired infections |

## Twelve months of coverage

Monthly matching articles for `norovirus` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 99 | 75% | 65 | 30 | ███████ |
| Jun 2025 | 59 | 63% | 23 | 34 | ████ |
| Jul 2025 | 99 | 61% | 78 | 17 | ███████ |
| Aug 2025 | 105 | 66% | 67 | 35 | ████████ |
| Sep 2025 | 40 | 75% | 23 | 15 | ███ |
| Oct 2025 | 98 | 74% | 73 | 23 | ███████ |
| Nov 2025 | 83 | 77% | 60 | 21 | ██████ |
| Dec 2025 | 256 | 62% | 209 | 38 | ███████████████████ |
| Jan 2026 | 156 | 78% | 124 | 27 | ███████████ |
| Feb 2026 | 275 | 68% | 225 | 44 | ████████████████████ |
| Mar 2026 | 201 | 79% | 161 | 33 | ███████████████ |
| Apr 2026 | 97 | 75% | 61 | 34 | ███████ |

The last four complete months averaged 182 articles a month against 90 in the first four (+101%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 123 | 17% |
| United Kingdom | 38 | 5.2% |
| Canada | 17 | 2.3% |
| Italy | 17 | 2.3% |
| Ireland | 12 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| community-acquired infections | 63 | 12% | +174% |
| covid-19 public health policies and lockdown measures | 43 | 8.0% | +258% |
| sanitation and hygiene initiatives | 85 | 16% | -10% |
| infectious disease control strategies | 38 | 7.1% | +171% |
| covid-19 epidemiology and transmission modeling | 33 | 6.2% | +38% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 4 Apr 2026 | [Hospital Steps Down Norovirus Incident but Warns of High Case Numbers - Time News](https://time.news/hospital-steps-down-norovirus-incident-but-warns-of-high-case-numbers/) | time.news | 8 | negative |
| 30 Mar 2026 | [Hospital Declares Critical Incident Due to Norovirus & Emergency Department Demand - Time News](https://time.news/hospital-declares-critical-incident-due-to-norovirus-emergency-department-demand/) | time.news | 8 | negative |
| 30 Mar 2026 | [UK hospital declares critical incident with visiting restrictions in place](https://www.express.co.uk/news/uk/2188351/surrey-hospital-critical-incident-norovirus-outbreak) | express.co.uk | 8 | negative |
| 26 Mar 2026 | [Osaka School Food Poisoning Affects Over 600](https://www.newkerala.com/news/a/food-poisoning-hits-multiple-schools-japans-osaka-affecting-965.htm) | newkerala.com | 8 | negative |
| 24 Mar 2026 | [HSE warns people not to go to work if they have these 2 symptoms](https://www.rsvplive.ie/news/irish-news/hse-warns-people-not-go-36913270) | rsvplive.ie | 8 | negative |
| 16 Mar 2026 | [153 People on Princess Cruise Ship in the Caribbean Infected With Norovirus](https://www.today.com/health/news/princess-cruise-ship-norovirus-oubtreak-2026-rcna263655) | today.com | 8 | negative |
| 13 Mar 2026 | [Sickness Sweeps Through Guests and Crew on Newest Princess Cruises Ship](https://www.cruisehive.com/sickness-sweeps-through-guests-and-crew-on-newest-princess-cruises-ship/201947) | cruisehive.com | 8 | negative |
| 11 Mar 2026 | [Recalled oysters, clams likely contaminated by human waste](https://healio.com/news/infectious-disease/20260311/recalled-oysters-clams-likely-contaminated-by-human-waste) | healio.com | 8 | negative |
| 10 Mar 2026 | [Raw Oysters, Clams Recalled Across 9 States for Potential Norovirus Contamination](https://www.yahoo.com/news/articles/raw-oysters-clams-recalled-across-164047166.html) | yahoo.com | 8 | negative |
| 10 Mar 2026 | [Oysters and clams in 9 states could be contaminated with norovirus, FDA warns](https://www.yahoo.com/news/articles/oysters-clams-9-states-could-145508365.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "norovirus" --since 2026-01-01 --until 2026-04-30
prism-news trends "norovirus" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "norovirus" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "norovirus", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "norovirus", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [E Coli Outbreak](e-coli-outbreak.md)
- [Salmonella Outbreak](salmonella-outbreak.md)
- [Tuberculosis Outbreak](tuberculosis-outbreak.md)
- [Cholera Outbreak](cholera-outbreak.md)
