# Measles Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “measles outbreak” · 590/month India · 201,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [measles-outbreak.json](../../examples/scenarios/measles-outbreak.json).

**Question.** How much measles coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="measles"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,175 |
| Negative · neutral · positive | 79% · 5.0% · 16% |
| Critical (priority 7–9) | 89% (4,605 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (1,914 articles) |
| Most-reported country | United States (30% of matches) |
| Strongest theme by lift | immunization strategies for rare diseases |

## Twelve months of coverage

Monthly matching articles for `measles` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,214 | 82% | 965 | 227 | █████████████ |
| Jun 2025 | 633 | 82% | 495 | 128 | ███████ |
| Jul 2025 | 964 | 76% | 799 | 158 | ██████████ |
| Aug 2025 | 922 | 85% | 753 | 163 | ██████████ |
| Sep 2025 | 959 | 91% | 647 | 304 | ██████████ |
| Oct 2025 | 703 | 93% | 534 | 166 | ███████ |
| Nov 2025 | 540 | 88% | 437 | 97 | ██████ |
| Dec 2025 | 538 | 87% | 434 | 99 | ██████ |
| Jan 2026 | 777 | 91% | 593 | 170 | ████████ |
| Feb 2026 | 1,914 | 88% | 1,562 | 238 | ████████████████████ |
| Mar 2026 | 969 | 85% | 712 | 135 | ██████████ |
| Apr 2026 | 1,515 | 91% | 1,238 | 260 | ████████████████ |

The last four complete months averaged 1,294 articles a month against 933 in the first four (+39%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,552 | 30% |
| Bangladesh | 219 | 4.2% |
| United Kingdom | 131 | 2.5% |
| Canada | 130 | 2.5% |
| Australia | 56 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| immunization strategies for rare diseases | 1,353 | 34% | +188% |
| vaccine hesitancy research | 620 | 16% | +265% |
| global health challenges | 470 | 12% | +187% |
| community-acquired infections | 448 | 11% | +634% |
| pediatric infectious disease case studies | 692 | 18% | +289% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Calls for RFK Jr. to be fired as cases of deadly disease once eradicated surge](https://www.uniladtech.com/news/rfk-jr-vaccine-warning-measles-447887-20260428) | uniladtech.com | 9 | negative |
| 27 Apr 2026 | [South Carolina declares end to massive measles outbreak](https://www.dispatch.com/story/life/health-wellness/2026/04/27/measles-outbreak-south-carolina/89823667007/) | dispatch.com | 9 | negative |
| 27 Apr 2026 | [South Carolina’s measles outbreak is over after sickening nearly 1,000 people](https://www.dailydemocrat.com/2026/04/27/south-carolina-measles/) | dailydemocrat.com | 9 | negative |
| 27 Apr 2026 | [US measles outbreak declared over, with around 144 cases reported in Florida](https://www.yahoo.com/news/articles/us-measles-outbreak-declared-over-164620661.html) | yahoo.com | 9 | negative |
| 27 Apr 2026 | [Measles surge accompanied by rising dengue prevalence](http://www.dhakatribune.com/bangladesh/health/408829/measles-surge-accompanied-by-rising-dengue) | dhakatribune.com | 9 | negative |
| 26 Apr 2026 | [8 more children die of measles, measles-like symptoms in 24 hours](https://www.dhakatribune.com/bangladesh/health/408704/8-more-children-die-of-measles-measles-like) | dhakatribune.com | 9 | negative |
| 26 Apr 2026 | [Pakistan reports 71 measles deaths in 4 months, Sindh records highest toll](https://gulfnews.com/world/asia/pakistan/pakistan-reports-71-measles-deaths-in-4-months-sindh-records-highest-toll-1.500519646) | gulfnews.com | 9 | negative |
| 23 Apr 2026 | [New Jersey has its first confirmed measles case of 2026](https://www.courierpostonline.com/story/news/health/2026/04/23/new-jersey-department-of-health-new-jersey-measles-case-cdc-newark-liberty-airport/89754039007/) | courierpostonline.com | 9 | negative |
| 23 Apr 2026 | [Deadly meningitis spreads as Sudanese refugees pack Chad camps, MSF says](https://www.yahoo.com/news/articles/deadly-meningitis-spreads-sudanese-refugees-154314042.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "measles" --since 2026-01-01 --until 2026-04-30
prism-news trends "measles" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "measles" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "measles", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "measles", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Ebola Outbreak](ebola-outbreak.md)
- [Influenza Outbreak](influenza-outbreak.md)
