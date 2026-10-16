# Drug Pricing News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drug pricing news” · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [drug-pricing-news.json](../../examples/scenarios/drug-pricing-news.json).

**Question.** How did coverage of drug pricing develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="drug pricing"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 503 |
| Negative · neutral · positive | 47% · 1.4% · 51% |
| Critical (priority 7–9) | 85% (429 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (163 articles) |
| Most-reported country | United States (45% of matches) |
| Strongest theme by lift | drug pricing and reimbursement strategies |

## Twelve months of coverage

Monthly matching articles for `drug pricing` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 86 | 88% | 65 | 21 | ███████████ |
| Jun 2025 | 44 | 89% | 18 | 26 | █████ |
| Jul 2025 | 48 | 62% | 26 | 22 | ██████ |
| Aug 2025 | 59 | 97% | 41 | 17 | ███████ |
| Sep 2025 | 100 | 90% | 60 | 39 | ████████████ |
| Oct 2025 | 119 | 87% | 56 | 59 | ███████████████ |
| Nov 2025 | 87 | 70% | 30 | 57 | ███████████ |
| Dec 2025 | 109 | 86% | 48 | 60 | █████████████ |
| Jan 2026 | 131 | 79% | 60 | 71 | ████████████████ |
| Feb 2026 | 163 | 92% | 63 | 97 | ████████████████████ |
| Mar 2026 | 71 | 83% | 33 | 37 | █████████ |
| Apr 2026 | 138 | 85% | 81 | 54 | █████████████████ |

The last four complete months averaged 126 articles a month against 59 in the first four (+112%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 224 | 45% |
| United Kingdom | 8 | 1.6% |
| China | 6 | 1.2% |
| Venezuela | 3 | 0.6% |
| Central African Republic | 2 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| drug pricing and reimbursement strategies | 118 | 39% | -30% |
| pharmaceutical marketing and sales strategies | 107 | 35% | -34% |
| healthcare economics and market access | 76 | 25% | -30% |
| pharmaceutical regulation and drug policies | 62 | 20% | -8% |
| generic drug development and market trends | 56 | 18% | -18% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Astrazeneca ploughs £300m into UK in surprise U-turn](https://www.cityam.com/astrazeneca-to-plough-300m-into-uk-operations/) | cityam.com | 8 | positive |
| 23 Apr 2026 | [Regeneron and Trump Strike a Deal: What It Means for Drug Prices In US](https://www.timesnownews.com/world/us/us-news/regeneron-trump-strike-a-deal-what-it-means-for-drug-prices-in-us-and-regeneron-drugs-article-154152159) | timesnownews.com | 8 | positive |
| 23 Apr 2026 | [Trump touts drug pricing pact with Regeneron aimed at lowering costs](https://www.courierpostonline.com/story/news/politics/2026/04/23/trump-administration-drug-pricing-deal-regeneron/89751901007/) | courierpostonline.com | 8 | positive |
| 16 Apr 2026 | [US FDA's accelerated approval for drugs needs more transparency, says research firm](https://www.yahoo.com/news/articles/us-fdas-accelerated-approval-drugs-120437787.html) | yahoo.com | 8 | negative |
| 10 Apr 2026 | [Medicaid Drug Rebate Program, Healthcare Reform, Department of Health and Human Services (HHS) \| JD Supra](https://www.jdsupra.com/topics/medicaid-drug-rebate-program/healthcare-reform/department-of-health-and-human-services-hhs/) | jdsupra.com | 8 | negative |
| 1 Apr 2026 | [Trump puts Australia’s drugs scheme, digital rules in firing line](https://www.afr.com/world/north-america/trump-puts-australia-s-drugs-scheme-digital-rules-in-firing-line-20260401-p5zkj8) | afr.com | 8 | negative |
| 13 Mar 2026 | [Sebelius: GOP health bill reduces coverage, increases costs](https://www.pbssocal.org/shows/newshour/clip/sebelius-gop-health-bill-reduces-coverage-increases-costs-1498174470) | pbssocal.org | 8 | negative |
| 27 Feb 2026 | [Hospital use of drug discount program needs accountability - HeraldNet.com](https://www.heraldnet.com/2026/02/27/hospital-use-of-drug-discount-program-needs-accountability/) | heraldnet.com | 8 | negative |
| 25 Feb 2026 | [Trump Calls on Congress To Codify Most Favored Nation Drug Pricing in SOTU](https://www.biospace.com/policy/trump-calls-on-congress-to-codify-most-favored-nation-drug-pricing-in-sotu) | biospace.com | 8 | negative |
| 12 Feb 2026 | [Centers for Medicare & Medicaid Services (CMS), Department of Health and Human Services (HHS),…](https://www.jdsupra.com/topics/centers-for-medicare-medicaid-services-cms/department-of-health-and-human-services-hhs/pharmaceutical-industry/) | jdsupra.com | 8 | negative |
| 10 Feb 2026 | [AstraZenec­a CEO hails NHS drug price deal but keeps pause on £200m UK investment](https://www.pressreader.com/australia/the-guardian-australia/20260211/282222312203343) | pressreader.com | 8 | positive |
| 8 Feb 2026 | [Finding the Right Mix for 2018 Bio/Pharma Success \| Pharmaceutical Technology](https://www.pharmtech.com/view/finding-right-mix-2018-biopharma-success) | pharmtech.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "drug pricing" --since 2026-01-01 --until 2026-04-30
prism-news trends "drug pricing" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "drug pricing" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "drug pricing", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "drug pricing", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Immigration Policy News](immigration-policy-news.md)
- [Right to Repair News](right-to-repair-news.md)
- [Export Controls News](export-controls-news.md)
- [NEP News](nep-news.md)
