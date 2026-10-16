# Antibiotics News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “antibiotics news” · 30/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [antibiotics-news.json](../../examples/scenarios/antibiotics-news.json).

**Question.** How much antibiotics coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="antibiotics"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,985 |
| Negative · neutral · positive | 31% · 4.5% · 65% |
| Critical (priority 7–9) | 85% (4,254 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,480 articles) |
| Most-reported country | United States (7.6% of matches) |
| Strongest theme by lift | antimicrobial stewardship programs |

## Twelve months of coverage

Monthly matching articles for `antibiotics` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 973 | 81% | 260 | 666 | █████████████ |
| Jun 2025 | 925 | 80% | 205 | 669 | ████████████ |
| Jul 2025 | 1,012 | 80% | 262 | 684 | ██████████████ |
| Aug 2025 | 1,114 | 81% | 352 | 700 | ███████████████ |
| Sep 2025 | 1,197 | 82% | 370 | 752 | ████████████████ |
| Oct 2025 | 1,055 | 86% | 260 | 744 | ██████████████ |
| Nov 2025 | 1,113 | 83% | 309 | 743 | ███████████████ |
| Dec 2025 | 1,238 | 83% | 290 | 883 | █████████████████ |
| Jan 2026 | 1,480 | 88% | 318 | 1,076 | ████████████████████ |
| Feb 2026 | 1,119 | 86% | 348 | 718 | ███████████████ |
| Mar 2026 | 1,210 | 85% | 495 | 672 | ████████████████ |
| Apr 2026 | 1,176 | 82% | 375 | 749 | ████████████████ |

The last four complete months averaged 1,246 articles a month against 1,006 in the first four (+24%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 19% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 378 | 7.6% |
| United Kingdom | 161 | 3.2% |
| India | 129 | 2.6% |
| Australia | 21 | 0.4% |
| China | 21 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| antimicrobial stewardship programs | 999 | 28% | -2% |
| antibiotic resistance research | 517 | 14% | -4% |
| treatment of multidrug-resistant organisms | 1,019 | 28% | +0% |
| antibiotic resistance and novel treatments | 421 | 12% | +16% |
| antimicrobial-resistant pathogens | 1,081 | 30% | -1% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Wenn Antibiotika ihre Kraft verlieren](https://www.wort.lu/panorama/gesundesleben/wenn-antibiotika-ihre-kraft-verlieren/145657118.html) | wort.lu | 9 | negative |
| 23 Mar 2026 | [Doctor on likelihood of national lockdown following Kent meningitis cases](http://www.express.co.uk/life-style/health/2185351/kent-meningitis-outbreak-national-lockdown) | express.co.uk | 9 | negative |
| 16 Mar 2026 | [Terrified students queue for meninigitis medicine as parents take them home](https://www.mirror.co.uk/news/uk-news/terrified-students-queue-meninigitis-drugs-36877022) | mirror.co.uk | 9 | negative |
| 30 Apr 2026 | [CDC warns of drug-resistant salmonella infections linked to backyard poultry](https://www.latimes.com/science/story/2026-04-30/cdc-warns-of-drug-resistant-salmonella-infections-linked-to-backyard-poultry) | latimes.com | 8 | negative |
| 29 Apr 2026 | [Antibiotics API Supply Chains Are Fracturing And Most Pharma Companies Aren't Ready](https://www.openpr.com/news/4494194/antibiotics-api-supply-chains-are-fracturing-and-most-pharma) | openpr.com | 8 | negative |
| 28 Apr 2026 | [Antimicrobial pharmacodynamics: defining regimens of antibiotics that are safe, effective and prevent the…](https://pubmed.ncbi.nlm.nih.gov/42057718/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "antibiotics" --since 2026-01-01 --until 2026-04-30
prism-news trends "antibiotics" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "antibiotics" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "antibiotics", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "antibiotics", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Telemedicine News](telemedicine-news.md)
- [Asthma News](asthma-news.md)
- [Kidney Disease News](kidney-disease-news.md)
- [Leprosy News](leprosy-news.md)
