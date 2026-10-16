# Rabies Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rabies outbreak” · 40/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rabies-outbreak.json](../../examples/scenarios/rabies-outbreak.json).

**Question.** How much rabies coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="rabies"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,232 |
| Negative · neutral · positive | 62% · 2.4% · 35% |
| Critical (priority 7–9) | 73% (898 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (610 articles) |
| Most-reported country | India (12% of matches) |
| Strongest theme by lift | dog vaccination schedules and preventive care |

## Twelve months of coverage

Monthly matching articles for `rabies` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 281 | 62% | 151 | 119 | █████████ |
| Jun 2025 | 189 | 69% | 136 | 45 | ██████ |
| Jul 2025 | 318 | 73% | 211 | 95 | ██████████ |
| Aug 2025 | 610 | 81% | 416 | 176 | ████████████████████ |
| Sep 2025 | 308 | 74% | 149 | 151 | ██████████ |
| Oct 2025 | 190 | 69% | 84 | 100 | ██████ |
| Nov 2025 | 194 | 77% | 90 | 101 | ██████ |
| Dec 2025 | 263 | 79% | 152 | 105 | █████████ |
| Jan 2026 | 243 | 80% | 142 | 92 | ████████ |
| Feb 2026 | 259 | 68% | 142 | 111 | ████████ |
| Mar 2026 | 331 | 71% | 213 | 112 | ███████████ |
| Apr 2026 | 399 | 73% | 269 | 117 | █████████████ |

The last four complete months averaged 308 articles a month against 350 in the first four (-12%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 33% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 152 | 12% |
| United States | 145 | 12% |
| United Kingdom | 18 | 1.5% |
| Malaysia | 10 | 0.8% |
| China | 8 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| dog vaccination schedules and preventive care | 106 | 13% | -33% |
| stray population management strategies | 95 | 12% | +19% |
| dog health issues and veterinary care | 79 | 9.6% | +36% |
| veterinary vaccines and zoonotic disease prevention | 75 | 9.1% | +92% |
| veterinary care for stray animals | 66 | 8.0% | +78% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Bat with rabies found in Camden County residence](https://www.courierpostonline.com/story/news/health/2026/04/27/camden-county-health-department-haddonfield-rabies-vaccine-rabies-exposure-cdc-bat-in-attic/89816613007/) | courierpostonline.com | 8 | negative |
| 20 Apr 2026 | ['Stop Rabies' initiative seeks to achieve rabies-free Philippines](https://www.philstar.com/lifestyle/health-and-family/2026/04/20/2522018/stop-rabies-initiative-seeks-achieve-rabies-free-philippines) | philstar.com | 8 | negative |
| 17 Apr 2026 | [March 2026 Excellence in Action: Dharamsala Animal Rescue, India](https://www.rabiesalliance.org/news/march-2026-excellence-action-dharamsala-animal-rescue-india) | rabiesalliance.org | 8 | positive |
| 15 Apr 2026 | [Testimony begins in trial of former animal control tech accused of cruelty](https://www.yahoo.com/news/articles/testimony-begins-trial-former-animal-035900720.html) | yahoo.com | 8 | negative |
| 2 Apr 2026 | [CDC pauses lab testing of rabies, monkeypox and other infectious diseases](https://www.nbcphiladelphia.com/news/national-international/cdc-pauses-testing-rabies-monkeypox/4379036/) | nbcphiladelphia.com | 8 | negative |
| 2 Apr 2026 | [CDC pauses testing for rabies and other serious infectious diseases](https://www.nbcnews.com/health/health-news/cdc-pauses-testing-rabies-monkeypox-epstein-barr-viruses-rcna266377) | nbcnews.com | 8 | negative |
| 2 Apr 2026 | [CDC pauses lab testing for dozens of diseases](http://www.healio.com/news/infectious-disease/20260402/cdc-pauses-lab-testing-for-dozens-of-diseases) | healio.com | 8 | negative |
| 1 Apr 2026 | [Rabies confirmed after mass dog bite incident in Assam town](https://www.thehindu.com/news/national/assam/rabies-confirmed-after-mass-dog-bite-incident-in-assam-town/article70810470.ece) | thehindu.com | 8 | negative |
| 31 Mar 2026 | [Rabies outbreak in Enugu triggers public health alert](https://thesun.ng/rabies-outbreak-in-enugu-triggers-public-health-alert/) | thesun.ng | 8 | negative |
| 26 Mar 2026 | [166 Dog Bite Cases Daily in Vasai-Virar Spark Health Risk](https://dogexpress.in/166-daily-dog-bite-cases-in-vasai-virar-spark-concern-after-child-rabies-death/) | dogexpress.in | 8 | negative |
| 25 Mar 2026 | [9 Year-Old Dies 6 Months After Skipping Rabies Vaccine: Why Not Getting Jabbed After A Dog Bite Can Be Fatal](https://www.ndtv.com/health/9-year-old-dies-6-months-after-skipping-rabies-vaccine-why-not-getting-jabbed-after-a-dog-bite-can-be-fatal-11263162) | ndtv.com | 8 | negative |
| 23 Mar 2026 | [Social activist calls for urgent, coordinated action against rabies in Sarawak \| Borneo Post Online](https://www.theborneopost.com/2026/03/23/social-activist-calls-for-urgent-coordinated-action-against-rabies-in-sarawak/) | theborneopost.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "rabies" --since 2026-01-01 --until 2026-04-30
prism-news trends "rabies" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "rabies" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "rabies", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "rabies", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Polio Outbreak](polio-outbreak.md)
- [Nipah Outbreak](nipah-outbreak.md)
- [Mpox Outbreak](mpox-outbreak.md)
- [CRISPR News](crispr-news.md)
