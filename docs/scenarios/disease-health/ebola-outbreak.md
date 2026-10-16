# Ebola Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ebola outbreak” · 14,800/month India · 110,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ebola-outbreak.json](../../examples/scenarios/ebola-outbreak.json).

**Question.** How much ebola coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="ebola"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,314 |
| Negative · neutral · positive | 70% · 1.0% · 29% |
| Critical (priority 7–9) | 89% (1,166 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (459 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | viral hemorrhagic fevers |

## Twelve months of coverage

Monthly matching articles for `ebola` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 297 | 86% | 190 | 98 | █████████████ |
| Jun 2025 | 118 | 80% | 50 | 67 | █████ |
| Jul 2025 | 234 | 73% | 157 | 76 | ██████████ |
| Aug 2025 | 250 | 80% | 164 | 83 | ███████████ |
| Sep 2025 | 459 | 95% | 368 | 89 | ████████████████████ |
| Oct 2025 | 196 | 90% | 104 | 84 | █████████ |
| Nov 2025 | 157 | 94% | 98 | 59 | ███████ |
| Dec 2025 | 163 | 90% | 72 | 84 | ███████ |
| Jan 2026 | 214 | 94% | 151 | 59 | █████████ |
| Feb 2026 | 305 | 88% | 201 | 101 | █████████████ |
| Mar 2026 | 404 | 87% | 289 | 110 | ██████████████████ |
| Apr 2026 | 391 | 88% | 279 | 109 | █████████████████ |

The last four complete months averaged 328 articles a month against 225 in the first four (+46%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 27% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 176 | 13% |
| Germany | 25 | 1.9% |
| Nigeria | 24 | 1.8% |
| United Kingdom | 14 | 1.1% |
| Democratic Republic of the Congo | 11 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| viral hemorrhagic fevers | 129 | 15% | -16% |
| emerging viral diseases | 234 | 27% | -16% |
| pandemic preparedness and response | 61 | 7.1% | +13% |
| public health emergency preparedness | 165 | 19% | -20% |
| global health emerging threats | 51 | 5.9% | +122% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Seattle police search for suspect after stabbing in North Seattle](https://www.yahoo.com/news/articles/seattle-police-search-suspect-stabbing-161709043.html) | yahoo.com | 9 | negative |
| 12 Apr 2026 | [9 hurt after crash in east Charlotte, Medic confirms](https://www.yahoo.com/news/articles/9-hurt-crash-east-charlotte-004545179.html) | yahoo.com | 9 | negative |
| 23 Mar 2026 | [Fire breaks out at Lexington County business Sunday afternoon; no injuries reported](https://www.yahoo.com/news/articles/fire-breaks-lexington-county-business-010247907.html) | yahoo.com | 9 | negative |
| 20 Mar 2026 | [Dispute leads to shooting incident in parking lot in Audubon, Pa.](https://www.yahoo.com/news/articles/dispute-leads-shooting-incident-parking-114906621.html) | yahoo.com | 9 | negative |
| 18 Mar 2026 | [Quitman ISD releases students early due to broken water main line](https://www.yahoo.com/news/articles/quitman-isd-releases-students-early-164416414.html) | yahoo.com | 9 | negative |
| 12 Mar 2026 | [What will shape Poroshenko and Putin's upcoming meeting?](https://www.pbssocal.org/shows/newshour/clip/what-will-shape-poroshenko-and-putin-s-upcoming-meeting-1416005236) | pbssocal.org | 9 | negative |
| 5 Mar 2026 | [Crash involving a rolled-over truck occurs along Eastbound Loop 202 Red Mountain in Tempe](https://www.yahoo.com/news/articles/crash-involving-rolled-over-semi-131102628.html) | yahoo.com | 9 | negative |
| 27 Feb 2026 | [Man struck by train, killed in Hall County, deputies say](https://www.yahoo.com/news/articles/man-struck-train-killed-hall-025604523.html) | yahoo.com | 9 | negative |
| 4 Feb 2026 | [Deputies in Osceola County to give briefing regarding a 2024 murder case](https://www.yahoo.com/news/articles/deputies-osceola-county-briefing-regarding-181839696.html) | yahoo.com | 9 | negative |
| 27 Jan 2026 | [Ethiopia declares end of Marburg outbreak that killed nine](https://health.economictimes.indiatimes.com/news/industry/ethiopia-declares-end-of-marburg-outbreak-that-killed-nine/127587629) | health.economictimes.indiatimes.com | 9 | negative |
| 30 Apr 2026 | [DOJ sues NJ over attempt to regulate federal law enforcement](https://www.yahoo.com/news/articles/doj-sues-nj-over-attempt-110940370.html) | yahoo.com | 8 | negative |
| 30 Apr 2026 | [Iran supreme leader issues statement saying only place Americans belong in Persian Gulf is 'at the bottom of…](https://www.yahoo.com/news/articles/iran-supreme-leader-issues-statement-104053387.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ebola" --since 2026-01-01 --until 2026-04-30
prism-news trends "ebola" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ebola" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ebola", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ebola", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through 24 Aug 2026; intake thins after May 2026.
- `q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- zero-count periods are included; partial_period marks buckets the window only partly covers
- Country shares use all matching articles. Location information is incomplete and varies by period.
- Theme shares use articles with identified themes; articles may have more than one theme.

## Related demonstrations

- [Measles Outbreak](measles-outbreak.md)
- [Influenza Outbreak](influenza-outbreak.md)
- [COVID News](covid-news.md)
