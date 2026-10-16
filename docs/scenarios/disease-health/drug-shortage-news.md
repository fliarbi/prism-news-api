# Drug Shortage News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drug shortage news” · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [drug-shortage-news.json](../../examples/scenarios/drug-shortage-news.json).

**Question.** How much drug shortage coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="drug shortage"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 89 |
| Negative · neutral · positive | 60% · 2.2% · 38% |
| Critical (priority 7–9) | 87% (77 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (34 articles) |
| Most-reported country | United States (33% of matches) |
| Strongest theme by lift | pharmaceutical manufacturing techniques |

## Twelve months of coverage

Monthly matching articles for `drug shortage` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 28 | 86% | 15 | 13 | ████████████████ |
| Jun 2025 | 20 | 95% | 13 | 7 | ████████████ |
| Jul 2025 | 24 | 88% | 13 | 11 | ██████████████ |
| Aug 2025 | 20 | 90% | 16 | 4 | ████████████ |
| Sep 2025 | 14 | 86% | 10 | 3 | ████████ |
| Oct 2025 | 13 | 69% | 7 | 5 | ████████ |
| Nov 2025 | 6 | 83% | 1 | 3 | ████ |
| Dec 2025 | 11 | 91% | 6 | 5 | ██████ |
| Jan 2026 | 22 | 91% | 13 | 9 | █████████████ |
| Feb 2026 | 34 | 82% | 14 | 20 | ████████████████████ |
| Mar 2026 | 11 | 82% | 9 | 2 | ██████ |
| Apr 2026 | 22 | 91% | 17 | 3 | █████████████ |

The last four complete months averaged 22 articles a month against 23 in the first four (-3%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 29 | 33% |
| India | 4 | 4.5% |
| Canada | 3 | 3.4% |
| Japan | 2 | 2.2% |
| Botswana | 1 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| pharmaceutical manufacturing techniques | 5 | 12% | — |
| drug manufacturing quality control | 5 | 12% | +67% |
| pharmaceutical supply chain management | 8 | 19% | +100% |
| drug pricing and reimbursement strategies | 11 | 26% | +267% |
| prescription drug guidelines | 5 | 12% | +150% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Medicines, one in three citizens complain of shortages and on generic medicines comes the risk of stock-outs](https://en.ilsole24ore.com/art/medicines-citizen-three-complains-of-shortages-and-generic-medicines-come-stock-risk-AIgz9FmC) | en.ilsole24ore.com | 8 | negative |
| 7 Apr 2026 | [Aux avant-postes - Pénurie de médicaments : la pharmacie mondiale en panne ?](https://www.france24.com/fr/%C3%A9missions/aux-avant-postes/20260407-p%C3%A9nurie-de-m%C3%A9dicaments-la-pharmacie-mondiale-en-panne) | france24.com | 7 | negative |
| 28 Jan 2026 | [Development of an Advanced Manufacturing Technology for Continuous Drug Substance Production.](https://pubmed.ncbi.nlm.nih.gov/41624704/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 23 Jan 2026 | [Advanced manufacturing study automated production of critical API](https://www.europeanpharmaceuticalreview.com/news/270630/advanced-manufacturing-automated-production-api/) | europeanpharmaceuticalreview.com | 7 | positive |
| 1 Jan 2026 | [How AI Can Help Solve Drug Shortage Issues \| Pharmaceutical Commerce](https://www.pharmaceuticalcommerce.com/view/how-ai-can-help-solve-drug-shortage-issues) | pharmaceuticalcommerce.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "drug shortage" --since 2026-01-01 --until 2026-04-30
prism-news trends "drug shortage" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "drug shortage" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "drug shortage", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "drug shortage", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Kidney Disease News](kidney-disease-news.md)
- [Leprosy News](leprosy-news.md)
- [Thalassemia News](thalassemia-news.md)
- [Diabetes Outbreak](diabetes-outbreak.md)
