# Clinical Trial News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “clinical trial news” · 70/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [clinical-trial-news.json](../../examples/scenarios/clinical-trial-news.json).

**Question.** How much clinical trial coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="clinical trial"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,198 |
| Negative · neutral · positive | 10% · 2.5% · 87% |
| Critical (priority 7–9) | 88% (10,719 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (3,620 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | oncology and targeted therapy advancements |

## Twelve months of coverage

Monthly matching articles for `clinical trial` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,539 | 88% | 255 | 2,203 | ██████████████ |
| Jun 2025 | 2,183 | 87% | 200 | 1,915 | ████████████ |
| Jul 2025 | 2,302 | 87% | 273 | 1,955 | █████████████ |
| Aug 2025 | 2,345 | 88% | 250 | 2,043 | █████████████ |
| Sep 2025 | 2,497 | 88% | 265 | 2,162 | ██████████████ |
| Oct 2025 | 2,631 | 90% | 235 | 2,301 | ███████████████ |
| Nov 2025 | 2,782 | 92% | 274 | 2,420 | ███████████████ |
| Dec 2025 | 3,329 | 91% | 342 | 2,878 | ██████████████████ |
| Jan 2026 | 3,620 | 89% | 295 | 3,190 | ████████████████████ |
| Feb 2026 | 2,598 | 84% | 318 | 2,228 | ██████████████ |
| Mar 2026 | 2,788 | 88% | 293 | 2,423 | ███████████████ |
| Apr 2026 | 3,192 | 90% | 343 | 2,774 | ██████████████████ |

The last four complete months averaged 3,050 articles a month against 2,342 in the first four (+30%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 22% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,543 | 13% |
| United Kingdom | 206 | 1.7% |
| China | 182 | 1.5% |
| India | 93 | 0.8% |
| Canada | 87 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| oncology and targeted therapy advancements | 921 | 12% | +18% |
| clinical trials and regulatory approvals | 730 | 9.3% | +38% |
| clinical trial methodologies | 595 | 7.6% | +27% |
| rare disease therapies and orphan drugs | 557 | 7.1% | +14% |
| gene therapy and crispr technologies | 466 | 6.0% | +32% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Eliminating animal products reshapes metabolic health and environmental impact](https://news-medical.net/news/20260430/Eliminating-animal-products-reshapes-metabolic-health-and-environmental-impact.aspx) | news-medical.net | 8 | positive |
| 30 Apr 2026 | [EnGeneIC Announces First Patient Dosed in Recurrent Glioblastoma Clinical Trial](https://www.nationaltribune.com.au/engeneic-announces-first-patient-dosed-in-recurrent-glioblastoma-clinical-trial/) | nationaltribune.com.au | 8 | positive |
| 30 Apr 2026 | [Sydney Towle Celebrates Successful Tumor Removal with Wand and Tiara in Her Hospital Bed](https://www.yahoo.com/entertainment/celebrity/articles/sydney-towle-celebrates-successful-tumor-141731192.html) | yahoo.com | 8 | positive |
| 30 Apr 2026 | [First patients enrolled in HistoSonics WOLVERINE clinical trial - Interventional News](https://interventionalnews.com/first-patients-enrolled-in-histosonics-wolverine-clinical-trial/) | interventionalnews.com | 8 | positive |
| 29 Apr 2026 | [Precision BioSciences Activates First Clinical Trial Site and Begins Patient Enrollment in Phase 1/2…](https://www.biospace.com/press-releases/precision-biosciences-activates-first-clinical-trial-site-and-begins-patient-enrollment-in-phase-1-2-function-dmd-study) | biospace.com | 8 | positive |
| 29 Apr 2026 | [Rein Therapeutics Provides Clinical Trial Update for Phase 2 RENEW Study of LTI-03 in Idiopathic Pulmonary…](https://www.biospace.com/press-releases/rein-therapeutics-provides-clinical-trial-update-for-phase-2-renew-study-of-lti-03-in-idiopathic-pulmonary-fibrosis) | biospace.com | 8 | positive |
| 29 Apr 2026 | [Argo Biopharma begins dosing for Phase I BW-50218 trial](https://www.clinicaltrialsarena.com/news/argo-biopharma-begins-dosing-bw50218-trial/) | clinicaltrialsarena.com | 8 | positive |
| 29 Apr 2026 | [DURHAM, N.C. — Precision BioSciences, Inc. (Nasdaq: DTIL), a clinical stage gene editing company utilizing…](https://checkorphan.org/news/precision-biosciences-launches-first-clinical-trial-site-and-patient-enrollment-for-pbgene-dmd-gene-editing-therapy-in-duchenne-muscular-dystrophy/) | checkorphan.org | 8 | positive |
| 28 Apr 2026 | [AI Model Boosts Pulmonary Nodule Diagnosis](https://www.emjreviews.com/respiratory/news/ai-model-boosts-pulmonary-nodule-diagnosis/) | emjreviews.com | 8 | positive |
| 28 Apr 2026 | [Updated: FDA claims trial 'manipulation' tainted approval of ChemoCentryx drug now owned by Amgen](https://endpoints.news/fda-claims-trial-manipulation-tainted-approval-of-chemocentryx-drug/) | endpoints.news | 8 | negative |
| 28 Apr 2026 | [FDA starts review of new lung cancer drug, decision due Feb. 2027](https://www.stocktitan.net/news/CGEM/u-s-food-and-drug-administration-accepts-new-drug-application-for-o7dz8md64r08.html) | stocktitan.net | 8 | positive |
| 28 Apr 2026 | [AI Skin Cancer Apps: Do They Work?](https://www.visionmonday.com/eyecare/health-watch/article/ai-skin-cancer-apps-do-they-work/) | visionmonday.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "clinical trial" --since 2026-01-01 --until 2026-04-30
prism-news trends "clinical trial" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "clinical trial" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "clinical trial", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "clinical trial", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Hepatitis Outbreak](hepatitis-outbreak.md)
- [Malaria Outbreak](malaria-outbreak.md)
- [Depression News](depression-news.md)
- [Sepsis News](sepsis-news.md)
