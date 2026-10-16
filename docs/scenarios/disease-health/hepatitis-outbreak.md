# Hepatitis Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hepatitis outbreak” · 40/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [hepatitis-outbreak.json](../../examples/scenarios/hepatitis-outbreak.json).

**Question.** How much hepatitis coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="hepatitis"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,362 |
| Negative · neutral · positive | 24% · 6.4% · 69% |
| Critical (priority 7–9) | 88% (2,079 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (1,196 articles) |
| Most-reported country | United States (8.1% of matches) |
| Strongest theme by lift | liver cancer and hepatitis connections |

## Twelve months of coverage

Monthly matching articles for `hepatitis` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 569 | 81% | 163 | 363 | ██████████ |
| Jun 2025 | 469 | 82% | 105 | 330 | ████████ |
| Jul 2025 | 757 | 72% | 203 | 500 | █████████████ |
| Aug 2025 | 700 | 84% | 264 | 376 | ████████████ |
| Sep 2025 | 713 | 90% | 268 | 397 | ████████████ |
| Oct 2025 | 594 | 89% | 136 | 408 | ██████████ |
| Nov 2025 | 517 | 88% | 116 | 364 | █████████ |
| Dec 2025 | 1,196 | 92% | 441 | 661 | ████████████████████ |
| Jan 2026 | 817 | 91% | 163 | 590 | ██████████████ |
| Feb 2026 | 452 | 86% | 109 | 314 | ████████ |
| Mar 2026 | 542 | 87% | 164 | 347 | █████████ |
| Apr 2026 | 551 | 86% | 133 | 384 | █████████ |

The last four complete months averaged 590 articles a month against 624 in the first four (-5%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 17% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 192 | 8.1% |
| India | 54 | 2.3% |
| China | 26 | 1.1% |
| United Kingdom | 23 | 1.0% |
| Australia | 10 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| liver cancer and hepatitis connections | 175 | 12% | -5% |
| infectious disease research and prevention | 162 | 11% | -4% |
| vaccination and immunization research | 116 | 7.8% | -1% |
| gene therapy and crispr technologies | 69 | 4.6% | +17% |
| biotechnology innovations in medicine | 64 | 4.3% | +23% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Global hepatitis infections fall, but pace lags behind 2030 targets: WHO - Türkiye Today](https://www.turkiyetoday.com/lifestyle/global-hepatitis-infections-fall-but-pace-still-lags-behind-2030-targets-who-warns-3219058) | turkiyetoday.com | 8 | negative |
| 16 Apr 2026 | [Over 30 Gandhi Medical College Hyderabad students fall ill after water Contamination, 1 contracts hepatitis:…](https://medicaldialogues.in/news/education/medical-colleges/over-30-gandhi-medical-college-hyderabad-students-fall-ill-after-water-contamination-1-contracts-hepatitis-report-168759) | medicaldialogues.in | 8 | negative |
| 22 Mar 2026 | ['They Tried to Cover It Up' — Father's Fury After Son Faces Six Months of HIV Tests Following Royal Gwent…](https://www.ibtimes.co.uk/whistleblower-exposes-nhs-sterilisation-failure-1787320) | ibtimes.co.uk | 8 | negative |
| 22 Mar 2026 | [21 People Treated with Unsterilized Surgical Tools at Hospital. Patients Were Not Told for Weeks, Despite…](https://www.yahoo.com/news/articles/21-people-treated-unsterilized-surgical-193606031.html) | yahoo.com | 8 | negative |
| 17 Mar 2026 | [Judge blocks vaccine rollback: Northeast Ohio health leaders warn of risks to children](https://www.yahoo.com/news/articles/judge-blocks-vaccine-rollback-northeast-213629252.html) | yahoo.com | 8 | negative |
| 15 Mar 2026 | [How blood product rules are changing \| Mint Ahmedabad - newspaper - Lee esta historia en Magzter.com](https://www.magzter.com/es/stories/newspaper/Mint-Ahmedabad/HOW-BLOOD-PRODUCT-RULES-ARE-CHANGING) | magzter.com | 8 | positive |
| 15 Mar 2026 | [How blood product rules are changing \| Mint Ahmedabad - newspaper - Bu hikayeyi Magzter.com'da okuyun](https://www.magzter.com/tr/stories/newspaper/Mint-Ahmedabad/HOW-BLOOD-PRODUCT-RULES-ARE-CHANGING) | magzter.com | 8 | positive |
| 1 Mar 2026 | [Optimal Corticosteroid Therapy Based on Liver Biopsy for Severe Immune-Mediated Hepatitis During…](https://pubmed.ncbi.nlm.nih.gov/41808699/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 17 Feb 2026 | [We don’t know what’s killing us: Inside Haryana's fever-hit village](https://www.indiatoday.in/india/story/chayasa-palwal-haryana-mysterious-illness-seven-deaths-liver-failure-probe-2869909-2026-02-17) | indiatoday.in | 8 | negative |
| 27 Jan 2026 | [Liver Transplant in Children with Anaemia](https://www.emjreviews.com/en-us/amj/hematology/news/stem-cell-transplant-after-liver-transplant-in-children/) | emjreviews.com | 8 | positive |
| 1 Jan 2026 | [Current Therapeutic Targets for Alcohol-Associated Liver Disease.](https://pubmed.ncbi.nlm.nih.gov/40683560/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 1 Jan 2026 | [Investigation into the Pancreatic Pathogenesis of SFTSV across Multiple Levels.](https://pubmed.ncbi.nlm.nih.gov/41090515/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "hepatitis" --since 2026-01-01 --until 2026-04-30
prism-news trends "hepatitis" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "hepatitis" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "hepatitis", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "hepatitis", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Zika Outbreak](zika-outbreak.md)
- [Prostate Cancer News](prostate-cancer-news.md)
- [Malaria Outbreak](malaria-outbreak.md)
- [Clinical Trial News](clinical-trial-news.md)
