# Antimicrobial Resistance News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “antimicrobial resistance news” · 90/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [antimicrobial-resistance-news.json](../../examples/scenarios/antimicrobial-resistance-news.json).

**Question.** How much antimicrobial resistance coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="antimicrobial resistance"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,088 |
| Negative · neutral · positive | 26% · 3.6% · 70% |
| Critical (priority 7–9) | 93% (2,876 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,095 articles) |
| Most-reported country | United States (3.7% of matches) |
| Strongest theme by lift | antimicrobial stewardship programs |

## Twelve months of coverage

Monthly matching articles for `antimicrobial resistance` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 500 | 89% | 123 | 350 | █████████ |
| Jun 2025 | 546 | 88% | 160 | 362 | ██████████ |
| Jul 2025 | 529 | 93% | 138 | 365 | ██████████ |
| Aug 2025 | 554 | 93% | 159 | 364 | ██████████ |
| Sep 2025 | 654 | 93% | 203 | 433 | ████████████ |
| Oct 2025 | 676 | 92% | 207 | 440 | ████████████ |
| Nov 2025 | 834 | 94% | 265 | 537 | ███████████████ |
| Dec 2025 | 874 | 94% | 238 | 593 | ████████████████ |
| Jan 2026 | 1,095 | 94% | 293 | 756 | ████████████████████ |
| Feb 2026 | 663 | 94% | 170 | 466 | ████████████ |
| Mar 2026 | 604 | 94% | 161 | 418 | ███████████ |
| Apr 2026 | 726 | 91% | 176 | 524 | █████████████ |

The last four complete months averaged 772 articles a month against 532 in the first four (+45%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 15% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 114 | 3.7% |
| India | 79 | 2.6% |
| United Kingdom | 57 | 1.9% |
| Nigeria | 17 | 0.6% |
| Australia | 14 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| antimicrobial stewardship programs | 1,223 | 48% | +3% |
| treatment of multidrug-resistant organisms | 1,124 | 44% | +4% |
| antimicrobial-resistant pathogens | 1,317 | 51% | +4% |
| antibiotic resistance and novel treatments | 334 | 13% | +16% |
| antibiotic resistance research | 251 | 9.8% | -10% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 1 Jan 2026 | [Antimicrobial Resistance in Somalia: A Silent Public Health Crisis Demanding Immediate Action.](https://pubmed.ncbi.nlm.nih.gov/41777727/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 28 Apr 2026 | [Antimicrobial pharmacodynamics: defining regimens of antibiotics that are safe, effective and prevent the…](https://pubmed.ncbi.nlm.nih.gov/42057718/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Antimicrobial Efficacy and Mechanistic Insights of 0D, 1D, 2D, and 3D Nanoparticles: A Review.](https://pubmed.ncbi.nlm.nih.gov/42083404/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Revisiting Fluoroquinolone Prophylaxis in Hematological Malignancies and Hematopoietic Cell Transplantation:…](https://pubmed.ncbi.nlm.nih.gov/42055352/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Antibacterial Activity of Quantum-Confined One-Dimensional Titanate Nanofilaments.](https://pubmed.ncbi.nlm.nih.gov/42041112/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 22 Apr 2026 | [Molecular epidemiology and genomic plasticity of ESBL-producing and carbapenem-non-susceptible Klebsiella…](https://pubmed.ncbi.nlm.nih.gov/42031126/) | pubmed.ncbi.nlm.nih.gov | 8 | neutral |
| 22 Apr 2026 | [Assessing N. gonorrhoeae prevalence and testing capacity for new treatment rollout: a scoping review for…](https://pubmed.ncbi.nlm.nih.gov/42021210/) | pubmed.ncbi.nlm.nih.gov | 8 | negative |
| 21 Apr 2026 | [Redefining the Fight Against AMR: Anti-Virulence Strategies and Phage Therapy Lead the Way](https://indiamedtoday.com/redefining-the-fight-against-amr-anti-virulence-strategies-and-phage-therapy-lead-the-way/) | indiamedtoday.com | 8 | negative |
| 20 Apr 2026 | [Injectable natural hydrogel-loaded Ta4C3 quantum dots self-assembled with Phillyrin-mediated NIR-II…](https://pubmed.ncbi.nlm.nih.gov/42009968/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 19 Apr 2026 | [ICU infections show alarming antibiotic resistance in Pune hospital study](https://www.hindustantimes.com/cities/pune-news/icu-infections-show-alarming-antibiotic-resistance-in-pune-hospital-study-101776623261742.html) | hindustantimes.com | 8 | negative |
| 18 Apr 2026 | [Resistência antimicrobiana avança no mundo e ameaça tornar infecções comuns novamente potencialmente fatais](https://www.em.com.br/emgiro/2026/04/7401131-resistencia-antimicrobiana-avanca-no-mundo-e-ameaca-tornar-infeccoes-comuns-novamente-potencialmente-fatais.html) | em.com.br | 8 | negative |
| 16 Apr 2026 | [Why birds, foxes could provide warning signs of antibiotic resistance](https://euronews.com/health/2026/04/16/why-birds-and-foxes-could-act-as-early-warning-systems-of-antibiotic-resistance-across-eco) | euronews.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "antimicrobial resistance" --since 2026-01-01 --until 2026-04-30
prism-news trends "antimicrobial resistance" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "antimicrobial resistance" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "antimicrobial resistance", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "antimicrobial resistance", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Epidemic Outbreak](epidemic-outbreak.md)
- [Stroke News](stroke-news.md)
- [RSV News](rsv-news.md)
- [Typhoid Outbreak](typhoid-outbreak.md)
