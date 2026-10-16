# Stroke News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “stroke news” · 10/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [stroke-news.json](../../examples/scenarios/stroke-news.json).

**Question.** How much stroke coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="stroke"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,761 |
| Negative · neutral · positive | 28% · 3.1% · 69% |
| Critical (priority 7–9) | 76% (8,166 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (3,104 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | clinical trial methodologies |

## Twelve months of coverage

Monthly matching articles for `stroke` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,477 | 72% | 744 | 1,640 | ████████████████ |
| Jun 2025 | 1,853 | 78% | 479 | 1,280 | ████████████ |
| Jul 2025 | 2,255 | 72% | 690 | 1,502 | ███████████████ |
| Aug 2025 | 2,641 | 68% | 866 | 1,695 | █████████████████ |
| Sep 2025 | 2,315 | 77% | 638 | 1,601 | ███████████████ |
| Oct 2025 | 2,382 | 81% | 598 | 1,700 | ███████████████ |
| Nov 2025 | 2,258 | 84% | 597 | 1,571 | ███████████████ |
| Dec 2025 | 2,335 | 81% | 506 | 1,731 | ███████████████ |
| Jan 2026 | 3,104 | 87% | 595 | 2,385 | ████████████████████ |
| Feb 2026 | 2,304 | 76% | 654 | 1,579 | ███████████████ |
| Mar 2026 | 2,303 | 73% | 680 | 1,551 | ███████████████ |
| Apr 2026 | 3,050 | 67% | 1,051 | 1,917 | ████████████████████ |

The last four complete months averaged 2,690 articles a month against 2,306 in the first four (+17%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 24% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,424 | 13% |
| United Kingdom | 255 | 2.4% |
| India | 248 | 2.3% |
| Australia | 85 | 0.8% |
| China | 78 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| clinical trial methodologies | 399 | 6.4% | +26% |
| medical imaging technique handbooks | 339 | 5.5% | +10% |
| public health initiatives and programs | 331 | 5.3% | +18% |
| medical journal publications and research papers | 420 | 6.8% | +19% |
| epidemiology and disease control studies | 763 | 12% | +9% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Combination therapy pill could reduce stroke risk by 40% - Drug Discovery World (DDW)](https://www.ddw-online.com/combination-therapy-pill-could-reduce-stroke-risk-by-40-41445-202604/) | ddw-online.com | 8 | positive |
| 29 Apr 2026 | [‘Back in six weeks’: Kamikamica sets footy return date after terrifying stroke](https://www.watoday.com.au/sport/nrl/back-in-six-weeks-kamikamica-sets-footy-return-date-after-terrifying-stroke-20260429-p5zs6g.html) | watoday.com.au | 8 | positive |
| 29 Apr 2026 | [India faces growing stroke threat](https://www.thehansindia.com/life-style/health/india-faces-growing-stroke-threat-1070270) | thehansindia.com | 8 | positive |
| 28 Apr 2026 | [Fifth Grader Saves Mom After She Has a Stroke During a 10K: 'I've Never Been Called a Hero'](https://www.yahoo.com/lifestyle/articles/fifth-grader-saves-mom-she-183048103.html) | yahoo.com | 8 | negative |
| 28 Apr 2026 | [1 in 7 Stroke Patients in India Are Under 44, Says ICMR: Why It’s Rising](https://www.timesnownews.com/health/1-in-7-stroke-patients-in-india-are-under-44-says-icmr-why-its-rising-article-154188522) | timesnownews.com | 8 | positive |
| 28 Apr 2026 | [1 In 7 stroke patients in India are between ages 18-44: Here’s what happens if you reach hospital after 24…](https://indianexpress.com/article/lifestyle/health/1-in-7-stroke-patients-in-india-are-between-ages-18-44-heres-what-happens-if-you-reach-hospital-after-24-hours-of-symptom-onset-10659926/) | indianexpress.com | 8 | negative |
| 28 Apr 2026 | [Systematic review and meta-analysis of stroke blood biomarker data highlights need for more translational…](https://pubmed.ncbi.nlm.nih.gov/42062243/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [RHOBH star nearly suffers a STROKE after diagnosis with 'silent killer' disease](https://www.the-sun.com/tv/16281389/rhobh-crystal-kung-minkoff-stroke-blood-pressure-diagnosis-killer/) | the-sun.com | 8 | negative |
| 27 Apr 2026 | [How Can I Lower My Stroke Risk? \| Members Only](http://www.aarp.org/health/healthy-living/ask-dr-adam-how-to-reduce-stroke-risk/) | aarp.org | 8 | negative |
| 27 Apr 2026 | [“RHOBH”'s Crystal Kung Minkoff Says She Nearly Had a Stroke in Recent Health Scare: ‘The Silent Killer’](https://www.yahoo.com/entertainment/celebrity/articles/rhobh-crystal-kung-minkoff-says-154356082.html) | yahoo.com | 8 | negative |
| 27 Apr 2026 | [Stroke: The Silent Global Emergency We Can No Longer Ignore](https://odishabytes.com/brain-stroke-the-silent-global-emergency-we-can-no-longer-ignore/) | odishabytes.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "stroke" --since 2026-01-01 --until 2026-04-30
prism-news trends "stroke" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "stroke" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "stroke", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "stroke", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Lung Cancer News](lung-cancer-news.md)
- [Epidemic Outbreak](epidemic-outbreak.md)
- [Antimicrobial Resistance News](antimicrobial-resistance-news.md)
- [RSV News](rsv-news.md)
