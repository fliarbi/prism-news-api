# Typhoid Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “typhoid outbreak” · 20/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [typhoid-outbreak.json](../../examples/scenarios/typhoid-outbreak.json).

**Question.** How much typhoid coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="typhoid"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 342 |
| Negative · neutral · positive | 58% · 2.0% · 39% |
| Critical (priority 7–9) | 74% (251 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (138 articles) |
| Most-reported country | India (26% of matches) |
| Strongest theme by lift | community-acquired infections |

## Twelve months of coverage

Monthly matching articles for `typhoid` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 64 | 67% | 36 | 28 | █████████ |
| Jun 2025 | 68 | 63% | 43 | 25 | ██████████ |
| Jul 2025 | 104 | 55% | 53 | 50 | ███████████████ |
| Aug 2025 | 138 | 62% | 77 | 55 | ████████████████████ |
| Sep 2025 | 129 | 78% | 78 | 47 | ███████████████████ |
| Oct 2025 | 95 | 78% | 46 | 47 | ██████████████ |
| Nov 2025 | 78 | 72% | 34 | 41 | ███████████ |
| Dec 2025 | 73 | 74% | 27 | 45 | ███████████ |
| Jan 2026 | 122 | 82% | 82 | 39 | ██████████████████ |
| Feb 2026 | 79 | 73% | 45 | 33 | ███████████ |
| Mar 2026 | 71 | 61% | 29 | 40 | ██████████ |
| Apr 2026 | 70 | 71% | 44 | 23 | ██████████ |

The last four complete months averaged 86 articles a month against 94 in the first four (-9%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 89 | 26% |
| United States | 26 | 7.6% |
| Tonga | 10 | 2.9% |
| Ghana | 8 | 2.3% |
| United Kingdom | 7 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| community-acquired infections | 27 | 13% | +200% |
| community health initiatives | 17 | 8.0% | +112% |
| antimicrobial stewardship programs | 17 | 8.0% | +31% |
| diagnosis of atypical pathogens | 13 | 6.1% | +86% |
| sanitation and hygiene initiatives | 26 | 12% | +86% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Essential Medicine Prices Soar in Pakistan, Insulin Costs Double](https://www.newkerala.com/news/a/essential-medicines-become-costlier-pakistan-doctors-warn-health-620.htm) | newkerala.com | 8 | negative |
| 1 Apr 2026 | [Drug-resistant typhoid drives 87% of India’s disease costs, children suffer most](https://www.theweek.in/news/health/2026/04/01/drug-resistant-typhoid-drives-87-of-indias-disease-costs-children-suffer-most.html) | theweek.in | 8 | negative |
| 31 Mar 2026 | [Thyrocare Technologies data shows one in three fever cases linked to infections in India - Express Healthcare](https://www.expresshealthcare.in/news/thyrocare-technologies-data-shows-one-in-three-fever-cases-linked-to-infections-in-india/453209/) | expresshealthcare.in | 8 | positive |
| 25 Mar 2026 | [Antibiotic resistance fuels 87% of India's typhoid economic burden: Study](https://health.economictimes.indiatimes.com/news/industry/antibiotic-resistance-fuels-87-per-cent-of-indias-typhoid-economic-burden-study/129796656) | health.economictimes.indiatimes.com | 8 | negative |
| 25 Mar 2026 | [Antibiotic resistance fuels 87 per cent of India's typhoid economic burden: Study](https://www.dailyexcelsior.com/antibiotic-resistance-fuels-87-per-cent-of-indias-typhoid-economic-burden-study/) | dailyexcelsior.com | 8 | negative |
| 10 Mar 2026 | [Florence Nightingale Never Visited India, but Changed How Millions Lived and Died Here](https://www.timesnownews.com/lifestyle/people/florence-nightingale-never-visited-india-but-changed-how-millions-lived-and-died-here-article-153791946) | timesnownews.com | 8 | negative |
| 26 Feb 2026 | [Typhoid is becoming more antibiotic-resistant and spreading across the world](https://www.yahoo.com/news/articles/typhoid-becoming-more-antibiotic-resistant-232641566.html) | yahoo.com | 8 | negative |
| 25 Feb 2026 | [Ancient Killer Is Rapidly Gaining Resistance to Antibiotics, Scientists Warn](https://www.yahoo.com/news/articles/ancient-killer-rapidly-gaining-resistance-201211059.html) | yahoo.com | 8 | negative |
| 11 Feb 2026 | [Water Contamination causes health issues in North India](https://solinas.in/of-rising-typhoid-diarrhoea-numbers-in-north-india-pipeline-health/) | solinas.in | 8 | negative |
| 29 Jan 2026 | [A 21st Century Take on Typhoid](http://www.sabin.org/resources/a-21st-century-take-on-typhoid/) | sabin.org | 8 | negative |
| 9 Jan 2026 | [7 Early Signs And Symptoms Of Typhoid](https://www.ndtv.com/health/7-early-signs-and-symptoms-of-typhoid-10564708) | ndtv.com | 8 | positive |
| 9 Jan 2026 | [Typhoid explained: How Salmonella Typhi spreads and why children are most vulnerable](https://www.theweek.in/news/health/2026/01/09/typhoid-explained-how-salmonella-typhi-spreads-and-why-children-are-most-vulnerable.html) | theweek.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "typhoid" --since 2026-01-01 --until 2026-04-30
prism-news trends "typhoid" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "typhoid" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "typhoid", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "typhoid", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Antimicrobial Resistance News](antimicrobial-resistance-news.md)
- [RSV News](rsv-news.md)
- [Lupus News](lupus-news.md)
- [Hypertension News](hypertension-news.md)
