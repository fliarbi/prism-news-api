# Diabetes Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “diabetes outbreak” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [diabetes-outbreak.json](../../examples/scenarios/diabetes-outbreak.json).

**Question.** How much diabetes coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="diabetes"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 18,660 |
| Negative · neutral · positive | 27% · 4.8% · 69% |
| Critical (priority 7–9) | 84% (15,635 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (5,451 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | diabetes medication management |

## Twelve months of coverage

Monthly matching articles for `diabetes` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4,177 | 79% | 961 | 2,980 | ███████████████ |
| Jun 2025 | 3,621 | 79% | 769 | 2,636 | █████████████ |
| Jul 2025 | 4,140 | 74% | 980 | 2,920 | ███████████████ |
| Aug 2025 | 4,401 | 78% | 1,085 | 3,090 | ████████████████ |
| Sep 2025 | 4,400 | 82% | 1,071 | 3,128 | ████████████████ |
| Oct 2025 | 3,912 | 81% | 809 | 2,871 | ██████████████ |
| Nov 2025 | 4,548 | 83% | 1,071 | 3,233 | █████████████████ |
| Dec 2025 | 4,677 | 84% | 922 | 3,471 | █████████████████ |
| Jan 2026 | 5,451 | 88% | 1,067 | 3,987 | ████████████████████ |
| Feb 2026 | 3,776 | 80% | 790 | 2,815 | ██████████████ |
| Mar 2026 | 4,023 | 81% | 915 | 2,949 | ███████████████ |
| Apr 2026 | 5,410 | 84% | 2,195 | 3,025 | ████████████████████ |

The last four complete months averaged 4,665 articles a month against 4,085 in the first four (+14%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 26% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,834 | 15% |
| India | 759 | 4.1% |
| United Kingdom | 304 | 1.6% |
| China | 128 | 0.7% |
| Canada | 97 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| diabetes medication management | 1,548 | 15% | +16% |
| public health initiatives and programs | 860 | 8.1% | +13% |
| patient safety and quality improvement studies | 830 | 7.9% | +21% |
| health disparities and equity research | 1,405 | 13% | +14% |
| nutritional science and dietary health research | 1,257 | 12% | +2% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 13 Jan 2026 | ['The Thing' Actor T.K. Carter Had Recent Health Issues Before Death](https://www.tmz.com/2026/01/13/tk-carter-recent-health-issues-before-death/) | tmz.com | 9 | negative |
| 30 Apr 2026 | [Genprex Receives Patent Grant from The Israel Patent Office for the Combination of Reqorsa® Gene Therapy and…](https://www.biospace.com/press-releases/genprex-receives-patent-grant-from-the-israel-patent-office-for-the-combination-of-reqorsa-gene-therapy-and-pd-1-antibodies-to-treat-cancer) | biospace.com | 8 | positive |
| 29 Apr 2026 | [Damon Wayans reveals the scary symptom that led to his type 2 diabetes diagnosis](https://www.foxnews.com/health/damon-wayans-reveals-scary-symptom-led-type-2-diabetes-diagnosis) | foxnews.com | 8 | negative |
| 29 Apr 2026 | [Dr Reddy's gets Health Canada nod for generic semaglutide injection](https://economictimes.indiatimes.com/industry/healthcare/biotech/pharmaceuticals/dr-reddys-gets-health-canada-nod-for-generic-semaglutide-injection/articleshow/130596904.cms) | economictimes.indiatimes.com | 8 | positive |
| 28 Apr 2026 | [Man claiming he's proof 'Ozempic penis' exists makes x-rated confession about how it's impacted his life](https://uniladtech.com/news/ozempic-penis-x-rated-confession-943643-20260428) | uniladtech.com | 8 | positive |
| 28 Apr 2026 | [From strangers to family: Kidney transplant brings two Texans together](https://www.yahoo.com/lifestyle/articles/strangers-family-kidney-transplant-brings-020723936.html) | yahoo.com | 8 | positive |
| 28 Apr 2026 | [Protein-Encapsulated DNA Metal Nanocluster as a Fluorescent Nanoprobe for Detecting Insulin.](https://pubmed.ncbi.nlm.nih.gov/42047329/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Synthesis, characterization, and α-glucosidase inhibitory activity of methyl proline derivatives of…](https://pubmed.ncbi.nlm.nih.gov/42095105/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Considerations for the clinical use of teplizumab in stage 2 Type 1 diabetes: A Consensus Statement from the…](https://pubmed.ncbi.nlm.nih.gov/42051156/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [As heart, kidney and metabolic health worsen, cancer risk may rise, study finds](https://www.yahoo.com/news/articles/heart-kidney-metabolic-health-worsen-163217520.html) | yahoo.com | 8 | negative |
| 27 Apr 2026 | [Synthetic Semaglutide vs Ozempic: Comparable Efficacy in Type 2 Diabetes](https://www.clinicaladvisor.com/news/synthetic-semaglutide-vs-ozempic-type-2-diabetes/) | clinicaladvisor.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "diabetes" --since 2026-01-01 --until 2026-04-30
prism-news trends "diabetes" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "diabetes" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "diabetes", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "diabetes", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Drug Shortage News](drug-shortage-news.md)
- [Thalassemia News](thalassemia-news.md)
