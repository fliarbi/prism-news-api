# Malaria Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “malaria outbreak” · 30/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [malaria-outbreak.json](../../examples/scenarios/malaria-outbreak.json).

**Question.** How much malaria coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="malaria"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,782 |
| Negative · neutral · positive | 27% · 2.5% · 70% |
| Critical (priority 7–9) | 76% (2,102 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,195 articles) |
| Most-reported country | United States (7.2% of matches) |
| Strongest theme by lift | neglected tropical diseases |

## Twelve months of coverage

Monthly matching articles for `malaria` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 713 | 80% | 256 | 439 | ████████████ |
| Jun 2025 | 542 | 79% | 160 | 368 | █████████ |
| Jul 2025 | 852 | 73% | 286 | 550 | ██████████████ |
| Aug 2025 | 858 | 72% | 387 | 447 | ██████████████ |
| Sep 2025 | 898 | 79% | 396 | 482 | ███████████████ |
| Oct 2025 | 610 | 87% | 183 | 405 | ██████████ |
| Nov 2025 | 660 | 86% | 188 | 460 | ███████████ |
| Dec 2025 | 645 | 84% | 199 | 424 | ███████████ |
| Jan 2026 | 572 | 88% | 116 | 437 | ██████████ |
| Feb 2026 | 516 | 87% | 188 | 313 | █████████ |
| Mar 2026 | 499 | 81% | 162 | 321 | ████████ |
| Apr 2026 | 1,195 | 62% | 293 | 873 | ████████████████████ |

The last four complete months averaged 696 articles a month against 741 in the first four (-6%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 28% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 199 | 7.2% |
| India | 129 | 4.6% |
| Nigeria | 94 | 3.4% |
| Kenya | 33 | 1.2% |
| United Kingdom | 29 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| neglected tropical diseases | 562 | 32% | +6% |
| vector-borne disease epidemiology | 599 | 34% | -1% |
| vector-borne disease mitigation | 156 | 8.9% | +8% |
| parasitic infections in humans | 538 | 31% | +6% |
| community health initiatives | 81 | 4.6% | +138% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Malaria Cases Spike In Gauteng 2026 \| Symptoms And Warning](https://www.joburgetc.com/news/malaria-cases-gauteng-2026-warning/) | joburgetc.com | 9 | negative |
| 30 Apr 2026 | [Gold Fields Foundation supports Tarkwa Nsuaem Health Directorate to mark World Malaria Day - MyJoyOnline](https://www.myjoyonline.com/gold-fields-foundation-supports-tarkwa-nsuaem-health-directorate-to-mark-world-malaria-day/) | myjoyonline.com | 8 | positive |
| 30 Apr 2026 | [Creating proteins to fight malaria](https://www.path.org/our-impact/articles/creating-proteins-to-fight-malaria/) | path.org | 8 | positive |
| 29 Apr 2026 | [...Nigeria bears 27% global disease burden –WHO](https://thesun.ng/nigeria-bears-27-global-disease-burden-who/) | thesun.ng | 8 | negative |
| 29 Apr 2026 | [WHO Clears First Malaria Drug for Newborns - Current Affairs Usthadian Academy](https://www.usthadian.com/who-clears-first-malaria-drug-for-newborns/) | usthadian.com | 8 | positive |
| 29 Apr 2026 | [Serum Institute of India, University of Oxford Sign Licensing Pact for Multi-Stage Malaria Vaccine R78C](https://medicaldialogues.in/news/industry/pharma/serum-institute-of-india-university-of-oxford-sign-licensing-pact-for-multi-stage-malaria-vaccine-r78c-169621) | medicaldialogues.in | 8 | positive |
| 29 Apr 2026 | [Oxford University strikes new malaria vaccine pact with Serum Institute of India](https://www.dailyexcelsior.com/oxford-university-strikes-new-malaria-vaccine-pact-with-serum-institute-of-india-2/) | dailyexcelsior.com | 8 | positive |
| 29 Apr 2026 | [Envu India Backs National Conclave on Urban Vector Control, Charts Path to Eliminate Dengue-Malaria in Cities](https://indiamedtoday.com/envu-india-backs-national-conclave-on-urban-vector-control-charts-path-to-eliminate-dengue-malaria-in-cities/) | indiamedtoday.com | 8 | positive |
| 28 Apr 2026 | [FG Targets 50% Reduction Of Malaria Burden By 2030](https://sciencenigeria.com/fg-targets-50-reduction-of-malaria-burden-by-2030/) | sciencenigeria.com | 8 | positive |
| 28 Apr 2026 | [Oxford & Serum Institute Team Up for Next-Gen Malaria Vaccine](https://www.easterneye.biz/oxford-serum-institute-multi-stage-malaria-vaccine-deal/) | easterneye.biz | 8 | positive |
| 28 Apr 2026 | [22 राज्यों के मुख्य सचिवों को एनएचआरसी का नोटिस,बढ़ते लू पर जताई चिंता](https://www.tarunmitra.in/national/nhrc-notice-to-chief-secretaries-of-22-states-expressed-concern/article-139623) | tarunmitra.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "malaria" --since 2026-01-01 --until 2026-04-30
prism-news trends "malaria" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "malaria" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "malaria", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "malaria", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Prostate Cancer News](prostate-cancer-news.md)
- [Hepatitis Outbreak](hepatitis-outbreak.md)
- [Clinical Trial News](clinical-trial-news.md)
- [Depression News](depression-news.md)
