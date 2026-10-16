# CRISPR News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “crispr news” · 50/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [crispr-news.json](../../examples/scenarios/crispr-news.json).

**Question.** How much crispr coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="CRISPR"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,530 |
| Negative · neutral · positive | 5.3% · 1.9% · 93% |
| Critical (priority 7–9) | 90% (3,167 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,078 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | gene therapy and crispr technologies |

## Twelve months of coverage

Monthly matching articles for `CRISPR` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 831 | 90% | 70 | 749 | ███████████████ |
| Jun 2025 | 643 | 93% | 45 | 591 | ████████████ |
| Jul 2025 | 720 | 88% | 35 | 672 | █████████████ |
| Aug 2025 | 726 | 91% | 42 | 675 | █████████████ |
| Sep 2025 | 822 | 86% | 47 | 748 | ███████████████ |
| Oct 2025 | 739 | 94% | 59 | 670 | ██████████████ |
| Nov 2025 | 898 | 93% | 60 | 821 | █████████████████ |
| Dec 2025 | 868 | 91% | 36 | 811 | ████████████████ |
| Jan 2026 | 1,078 | 92% | 45 | 1,020 | ████████████████████ |
| Feb 2026 | 832 | 90% | 56 | 769 | ███████████████ |
| Mar 2026 | 722 | 90% | 49 | 656 | █████████████ |
| Apr 2026 | 898 | 86% | 36 | 828 | █████████████████ |

The last four complete months averaged 882 articles a month against 730 in the first four (+21%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 30% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 620 | 18% |
| United Kingdom | 76 | 2.1% |
| India | 48 | 1.4% |
| China | 47 | 1.3% |
| Germany | 32 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| gene therapy and crispr technologies | 740 | 29% | +15% |
| biotechnology innovations in medicine | 572 | 22% | +20% |
| genetic and genomic research studies | 553 | 22% | +17% |
| stem cell research and applications | 489 | 19% | +9% |
| rare disease therapies and orphan drugs | 321 | 12% | +12% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [CRISPR speed patterns can identify multiple viruses and variants simultaneously](https://phys.org/news/2026-04-crispr-patterns-multiple-viruses-variants.html) | phys.org | 8 | positive |
| 29 Apr 2026 | [Florida citrus growers rejoice: EPA approved first CRISPR-edited HLB-resistant rootstock -…](https://www.freshfruitportal.com/news/2026/04/29/hlb-florida-citrus/) | freshfruitportal.com | 8 | positive |
| 28 Apr 2026 | [A Versatile tRNA-gRNA Array-Based CRISPR/Cas9 Platform Enabling Multiplex Genome Editing and Large-Fragment…](https://pubmed.ncbi.nlm.nih.gov/42052944/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Innovative CRISPR/Cas9-Based Strategy for Allele-Specific HLA Peptidome Analysis Using a Pan-HLA Antibody.](https://pubmed.ncbi.nlm.nih.gov/42069060/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [LISBON, Portugal – Nerai Bioscience, a biotechnology company spun out from the University of Zurich and ETH…](https://checkorphan.org/news/rare-disease-drug-development-with-ai-engineered-crispr-editors/) | checkorphan.org | 8 | positive |
| 28 Apr 2026 | [Catalytic hairpin assembly-assisted split-T7 promoter-regulated CRISPR/Cas12a system for the sensitive…](https://pubmed.ncbi.nlm.nih.gov/41960606/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Paired CRISPR screens identify mitochondrial metabolism and UBE2H as aneuploid-specific dependencies in…](https://pubmed.ncbi.nlm.nih.gov/42094535/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [A heterologous marker-free selection approach for CRISPR/Cas9-based gene editing in the malaria parasite…](https://pubmed.ncbi.nlm.nih.gov/41885428/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Acquisition of novel arrays via horizontal gene transfer rewire CRISPR-mediated defense in Pseudomonas…](https://pubmed.ncbi.nlm.nih.gov/42094579/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Gene Editing Candidate Lonvo-z Meets Endpoints in Phase 3 HAE Study](https://www.empr.com/news/gene-editing-candidate-lonvo-z-meets-endpoints-in-phase-3-hae-study/) | empr.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "CRISPR" --since 2026-01-01 --until 2026-04-30
prism-news trends "CRISPR" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "CRISPR" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "CRISPR", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "CRISPR", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Rabies Outbreak](rabies-outbreak.md)
- [Mpox Outbreak](mpox-outbreak.md)
- [Whooping Cough Outbreak](whooping-cough-outbreak.md)
- [Chikungunya Outbreak](chikungunya-outbreak.md)
