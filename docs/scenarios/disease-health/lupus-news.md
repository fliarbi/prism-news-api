# Lupus News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lupus news” · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [lupus-news.json](../../examples/scenarios/lupus-news.json).

**Question.** How much lupus coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="lupus"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,525 |
| Negative · neutral · positive | 18% · 7.3% · 74% |
| Critical (priority 7–9) | 73% (1,106 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (493 articles) |
| Most-reported country | United States (10% of matches) |
| Strongest theme by lift | rare disease research publications |

## Twelve months of coverage

Monthly matching articles for `lupus` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 343 | 62% | 75 | 223 | ██████████████ |
| Jun 2025 | 301 | 67% | 40 | 222 | ████████████ |
| Jul 2025 | 340 | 63% | 72 | 205 | ██████████████ |
| Aug 2025 | 332 | 64% | 76 | 223 | █████████████ |
| Sep 2025 | 344 | 60% | 75 | 249 | ██████████████ |
| Oct 2025 | 439 | 74% | 46 | 371 | ██████████████████ |
| Nov 2025 | 468 | 77% | 134 | 306 | ███████████████████ |
| Dec 2025 | 382 | 72% | 64 | 278 | ███████████████ |
| Jan 2026 | 493 | 75% | 87 | 382 | ████████████████████ |
| Feb 2026 | 271 | 72% | 37 | 199 | ███████████ |
| Mar 2026 | 339 | 67% | 59 | 257 | ██████████████ |
| Apr 2026 | 422 | 74% | 96 | 296 | █████████████████ |

The last four complete months averaged 381 articles a month against 329 in the first four (+16%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 18% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 157 | 10% |
| United Kingdom | 24 | 1.6% |
| China | 13 | 0.8% |
| Central African Republic | 11 | 0.7% |
| India | 10 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| rare disease research publications | 211 | 23% | +7% |
| autoimmune disorders not otherwise specified | 111 | 12% | -37% |
| clinical trial phases for new drugs | 95 | 10% | +22% |
| rare disease therapies and orphan drugs | 77 | 8.4% | +48% |
| immune system dysregulation disorders | 65 | 7.1% | -50% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [New Research Funded by Lupus Foundation of America Uncovers Microbiome-Linked Pathway Associated with Lupus…](https://www.lupus.org/news/new-research-funded-by-lupus-foundation-of-america-uncovers-microbiomelinked-pathway) | lupus.org | 8 | positive |
| 15 Apr 2026 | [She Was Told She’d Never Have Children Because of Her Lupus. Then She Had a Healthy Pregnancy at Age 40](https://www.yahoo.com/lifestyle/articles/she-told-she-d-never-140000823.html) | yahoo.com | 8 | negative |
| 14 Apr 2026 | [Hinge Bio Announces First Subject Dosed in Phase 1 Trial of HB2198, a Novel B cell Depleting Agent, for…](https://www.biospace.com/press-releases/hinge-bio-announces-first-subject-dosed-in-phase-1-trial-of-hb2198-a-novel-b-cell-depleting-agent-for-treating-autoimmune-disease) | biospace.com | 8 | positive |
| 4 Mar 2026 | [J&J's nipocalimab gets FDA Fast Track designation for lupus - PMLiVE](https://pmlive.com/pharma_news/jjs-nipocalimab-gets-fda-fast-track-designation-for-lupus) | pmlive.com | 8 | positive |
| 1 Mar 2026 | [Clinical Response to Baricitinib in Monogenic Lupus: Real-World Evidence from a Case Series of Seven Patients.](https://pubmed.ncbi.nlm.nih.gov/42100058/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 23 Apr 2026 | [Wicklow woman with lupus and cancer confined to one room as family appeals for help to adapt home](https://www.independent.ie/irish-news/health/wicklow-woman-with-lupus-and-cancer-confined-to-one-room-as-family-appeals-for-help-to-adapt-home/a1843796496.html) | independent.ie | 7 | negative |
| 20 Apr 2026 | [Baseline characteristics of patients with SLE with and without lupus nephritis from the Latin American…](https://pubmed.ncbi.nlm.nih.gov/42009373/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 20 Apr 2026 | [Primary headaches in juvenile-onset systemic lupus erythematosus: A preliminary case control study using…](https://pubmed.ncbi.nlm.nih.gov/42008622/) | pubmed.ncbi.nlm.nih.gov | 7 | neutral |
| 15 Apr 2026 | [Men with Lupus Are 'Few and Far Between.' This Man Shares How He Deals with His Rare Diagnosis](https://www.yahoo.com/lifestyle/articles/men-lupus-few-far-between-130000064.html) | yahoo.com | 7 | negative |
| 15 Apr 2026 | [Autoimmune drug candidate cleared B and T cells in lupus models](https://www.stocktitan.net/news/ALLO/allogene-therapeutics-announces-nature-communications-publication-vf0gm9wilrd7.html) | stocktitan.net | 7 | positive |
| 15 Apr 2026 | [Beeline Medicines emerges as Bristol Myers' partner for shelved immunology drugs](https://endpoints.news/beeline-medicines-emerges-as-bristol-myers-partner-for-shelved-immunology-drugs/) | endpoints.news | 7 | positive |
| 13 Apr 2026 | [Judge says manager’s lawsuit against Wells Fargo can move forward](https://www.yahoo.com/news/articles/judge-says-manager-lawsuit-against-161046937.html) | yahoo.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "lupus" --since 2026-01-01 --until 2026-04-30
prism-news trends "lupus" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "lupus" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "lupus", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "lupus", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [RSV News](rsv-news.md)
- [Typhoid Outbreak](typhoid-outbreak.md)
- [Hypertension News](hypertension-news.md)
- [Anxiety News](anxiety-news.md)
