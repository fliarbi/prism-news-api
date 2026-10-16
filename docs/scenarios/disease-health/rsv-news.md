# RSV News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rsv news” · 20/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rsv-news.json](../../examples/scenarios/rsv-news.json).

**Question.** How much rsv coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="RSV"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,889 |
| Negative · neutral · positive | 34% · 1.8% · 64% |
| Critical (priority 7–9) | 54% (3,201 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,176 articles) |
| Most-reported country | United States (40% of matches) |
| Strongest theme by lift | maternal and neonatal immunization strategies |

## Twelve months of coverage

Monthly matching articles for `RSV` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,064 | 48% | 281 | 769 | ██████████ |
| Jun 2025 | 1,077 | 66% | 474 | 582 | ██████████ |
| Jul 2025 | 975 | 52% | 321 | 632 | █████████ |
| Aug 2025 | 1,644 | 54% | 755 | 862 | ███████████████ |
| Sep 2025 | 1,228 | 59% | 430 | 766 | ███████████ |
| Oct 2025 | 1,027 | 52% | 278 | 730 | █████████ |
| Nov 2025 | 914 | 50% | 201 | 698 | ████████ |
| Dec 2025 | 1,221 | 57% | 420 | 783 | ███████████ |
| Jan 2026 | 1,341 | 71% | 553 | 762 | ████████████ |
| Feb 2026 | 1,202 | 57% | 383 | 798 | ███████████ |
| Mar 2026 | 1,170 | 51% | 390 | 752 | ███████████ |
| Apr 2026 | 2,176 | 44% | 689 | 1,445 | ████████████████████ |

The last four complete months averaged 1,472 articles a month against 1,190 in the first four (+24%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 58% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,358 | 40% |
| Ireland | 217 | 3.7% |
| United Kingdom | 181 | 3.1% |
| China | 66 | 1.1% |
| Australia | 61 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| maternal and neonatal immunization strategies | 153 | 4.3% | +25% |
| vaccine mandates and policy debates | 150 | 4.3% | +39% |
| covid-19 epidemiology and transmission modeling | 139 | 4.0% | +34% |
| community-acquired infections | 139 | 4.0% | +45% |
| covid-19 variants (alpha, delta, omicron) and mutations | 133 | 3.8% | +37% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [RSV infant jab reduces serious illness but long-term scheme not cost-effective, says health watchdog](https://www.independent.ie/irish-news/health/rsv-infant-jab-reduces-serious-illness-but-long-term-scheme-not-cost-effective-says-health-watchdog/a635754712.html) | independent.ie | 8 | positive |
| 28 Apr 2026 | [Impact and cost-effectiveness of two interventions to prevent paediatric respiratory syncytial virus disease…](https://pubmed.ncbi.nlm.nih.gov/42060341/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [RSV ready? Exploring feasibility and acceptability of RSV immunization options in low- and middle-income…](https://pubmed.ncbi.nlm.nih.gov/41946217/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [RSV hospitalizations in infants doubled after pandemic lull in Canada, surveillance shows](http://www.cidrap.umn.edu/respiratory-syncytial-virus-rsv/rsv-hospitalizations-infants-doubled-after-pandemic-lull-canada) | cidrap.umn.edu | 8 | positive |
| 23 Apr 2026 | [ESCMID Global 2026: Zelicapavir demonstrates benefits for high-risk adults with RSV](https://www.yahoo.com/news/articles/escmid-global-2026-zelicapavir-demonstrates-221830330.html) | yahoo.com | 8 | positive |
| 23 Apr 2026 | [ESCMID Global 2026: Zelicapavir demonstrates benefits for high-risk adults with RSV - Pharmaceutical…](https://www.pharmaceutical-technology.com/analyst-comment/escmid-global-2026-zelicapavir-demonstrates-benefits-for-high-risk-adults-with-rsv/) | pharmaceutical-technology.com | 8 | positive |
| 23 Apr 2026 | [Free RSV Vaccines for Older Australians: Protection Against Flu and RSV This Winter - Memesita](https://www.memesita.com/free-rsv-vaccines-for-older-australians-protection-against-flu-and-rsv-this-winter/) | memesita.com | 8 | positive |
| 22 Apr 2026 | [ESCMID Global 2026: real-world evidence of nirsevimab resistance](https://www.yahoo.com/news/articles/escmid-global-2026-real-world-102007099.html) | yahoo.com | 8 | positive |
| 21 Apr 2026 | [Why early action matters for cardiovascular health](https://www.politico.eu/sponsored-content/why-early-action-matters-for-cardiovascular-health/) | politico.eu | 8 | positive |
| 21 Apr 2026 | [Study: Early maternal RSV vaccination leads to stronger protection for babies](https://www.healio.com/news/pediatrics/20260421/study-early-maternal-rsv-vaccination-leads-to-stronger-protection-for-babies) | healio.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "RSV" --since 2026-01-01 --until 2026-04-30
prism-news trends "RSV" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "RSV" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "RSV", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "RSV", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Stroke News](stroke-news.md)
- [Antimicrobial Resistance News](antimicrobial-resistance-news.md)
- [Typhoid Outbreak](typhoid-outbreak.md)
- [Lupus News](lupus-news.md)
