# Asthma News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “asthma news” · 20/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [asthma-news.json](../../examples/scenarios/asthma-news.json).

**Question.** How much asthma coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="asthma"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,691 |
| Negative · neutral · positive | 32% · 6.6% · 61% |
| Critical (priority 7–9) | 72% (2,668 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (1,075 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | clinical trial phases for new drugs |

## Twelve months of coverage

Monthly matching articles for `asthma` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,075 | 58% | 464 | 552 | ████████████████████ |
| Jun 2025 | 604 | 72% | 217 | 346 | ███████████ |
| Jul 2025 | 754 | 69% | 282 | 428 | ██████████████ |
| Aug 2025 | 962 | 69% | 425 | 494 | ██████████████████ |
| Sep 2025 | 794 | 72% | 234 | 515 | ███████████████ |
| Oct 2025 | 697 | 74% | 218 | 438 | █████████████ |
| Nov 2025 | 880 | 77% | 285 | 542 | ████████████████ |
| Dec 2025 | 857 | 76% | 293 | 504 | ████████████████ |
| Jan 2026 | 1,047 | 82% | 251 | 704 | ███████████████████ |
| Feb 2026 | 749 | 76% | 227 | 474 | ██████████████ |
| Mar 2026 | 903 | 65% | 297 | 553 | █████████████████ |
| Apr 2026 | 992 | 66% | 415 | 519 | ██████████████████ |

The last four complete months averaged 923 articles a month against 849 in the first four (+9%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 34% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 701 | 19% |
| India | 182 | 4.9% |
| United Kingdom | 76 | 2.1% |
| Australia | 29 | 0.8% |
| China | 21 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| clinical trial phases for new drugs | 116 | 6.6% | +25% |
| asthma symptoms and management | 71 | 4.0% | -55% |
| clinical trials and regulatory approvals | 62 | 3.5% | +44% |
| air quality and pollution levels | 52 | 3.0% | +40% |
| public health initiatives and programs | 45 | 2.6% | +25% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Mississippi Middle School Students Stop Bus From Crashing After Driver Blacks Out](https://www.insurancejournal.com/news/southeast/2026/04/30/867860.htm) | insurancejournal.com | 8 | negative |
| 30 Apr 2026 | [Montelukast use during first trimester not linked to congenital malformation odds](https://www.healio.com/news/allergy-asthma/20260429/montelukast-use-during-first-trimester-not-linked-to-congenital-malformation-odds) | healio.com | 8 | positive |
| 29 Apr 2026 | [Mississippi Students Stop Runaway School Bus After Driver Passes Out](https://www.wideopencountry.com/mississippi-students-stop-runaway-school-bus-after-driver-passes-out/) | wideopencountry.com | 8 | negative |
| 29 Apr 2026 | [Watch: Mississippi middle schoolers heroically stop school bus after driver passes out](https://fox2detroit.com/news/mississippi-school-bus-driver-passes-out) | fox2detroit.com | 8 | negative |
| 29 Apr 2026 | [Dramatic moment schoolkids stop bus from crashing after driver passed out](https://www.the-sun.com/news/16288671/kids-stop-bus-crashing-driver-passes-out-mississippi/) | the-sun.com | 8 | negative |
| 28 Apr 2026 | [Watch: US school kids stop bus from crashing after driver blacks out](https://www.1news.co.nz/2026/04/29/watch-us-school-kids-stop-bus-from-crashing-after-driver-blacks-out/) | 1news.co.nz | 8 | — |
| 21 Apr 2026 | [A 32-year-old newlywed had a persistent cough. It was stage 4 cancer.](https://www.aol.com/articles/she-never-smoked-cigarette-stage-100325576.html) | aol.com | 8 | negative |
| 21 Apr 2026 | [Very high prenatal PFAS exposure linked to elevated childhood asthma incidence](https://www.healio.com/news/allergy-asthma/20260421/very-high-prenatal-pfas-exposure-linked-to-elevated-childhood-asthma-incidence) | healio.com | 8 | negative |
| 18 Apr 2026 | [Subterranean salvation under siege](https://www.thestar.com.my/news/focus/2026/04/18/subterranean-salvation-under-siege) | thestar.com.my | 8 | positive |
| 17 Apr 2026 | [Lung function improvement greater with albuterol-budesonide regardless of asthma control](https://healio.com/news/pulmonology/20260417/lung-function-improvement-greater-with-albuterolbudesonide-regardless-of-asthma-control) | healio.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "asthma" --since 2026-01-01 --until 2026-04-30
prism-news trends "asthma" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "asthma" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "asthma", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "asthma", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cell Therapy News](cell-therapy-news.md)
- [Telemedicine News](telemedicine-news.md)
- [Antibiotics News](antibiotics-news.md)
- [Kidney Disease News](kidney-disease-news.md)
