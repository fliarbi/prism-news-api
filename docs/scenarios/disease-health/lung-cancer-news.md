# Lung Cancer News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lung cancer news” · 30/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [lung-cancer-news.json](../../examples/scenarios/lung-cancer-news.json).

**Question.** How much lung cancer coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="lung cancer"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,826 |
| Negative · neutral · positive | 18% · 2.3% · 79% |
| Critical (priority 7–9) | 92% (6,298 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (2,232 articles) |
| Most-reported country | United States (11% of matches) |
| Strongest theme by lift | lung cancer early detection methods |

## Twelve months of coverage

Monthly matching articles for `lung cancer` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,369 | 90% | 231 | 1,095 | ████████████ |
| Jun 2025 | 1,216 | 95% | 158 | 1,034 | ███████████ |
| Jul 2025 | 1,445 | 90% | 257 | 1,147 | █████████████ |
| Aug 2025 | 1,536 | 90% | 305 | 1,197 | ██████████████ |
| Sep 2025 | 1,463 | 93% | 190 | 1,241 | █████████████ |
| Oct 2025 | 1,569 | 94% | 210 | 1,330 | ██████████████ |
| Nov 2025 | 1,637 | 93% | 290 | 1,315 | ███████████████ |
| Dec 2025 | 2,073 | 94% | 222 | 1,806 | ███████████████████ |
| Jan 2026 | 2,232 | 94% | 266 | 1,906 | ████████████████████ |
| Feb 2026 | 1,411 | 92% | 283 | 1,094 | █████████████ |
| Mar 2026 | 1,504 | 90% | 285 | 1,190 | █████████████ |
| Apr 2026 | 1,679 | 92% | 417 | 1,218 | ███████████████ |

The last four complete months averaged 1,706 articles a month against 1,392 in the first four (+23%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 18% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 721 | 11% |
| United Kingdom | 114 | 1.7% |
| India | 83 | 1.2% |
| China | 61 | 0.9% |
| Canada | 27 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| lung cancer early detection methods | 3,050 | 55% | +6% |
| oncology and targeted therapy advancements | 562 | 10% | +1% |
| liquid biopsy for early detection | 473 | 8.6% | +14% |
| radiation-induced tissue damage mitigation | 346 | 6.3% | -6% |
| tumor marker blood tests | 249 | 4.5% | +3% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Lorraine Kelly admits 'I burst into tears' as she addresses 'false' diagnosis](https://www.mirror.co.uk/3am/celebrity-news/lorraine-kelly-admits-i-burst-37074394) | mirror.co.uk | 9 | negative |
| 4 Apr 2026 | [The Young and the Restless star Dee Freeman dies aged 66 from lung cancer](https://metro.co.uk/2026/04/04/the-young-and-the-restless-star-dee-freeman-dies-aged-66-from-lung-cancer-27849473/) | metro.co.uk | 9 | negative |
| 30 Apr 2026 | [The Truth Behind 7 Common Lung Cancer Myths](https://www.visionmonday.com/eyecare/health-watch/article/the-truth-behind-7-common-lung-cancer-myths/) | visionmonday.com | 8 | negative |
| 30 Apr 2026 | [Optimizing Lung Cancer Therapy With OSA Management \| www.PhysiciansWeekly.com](https://www.physiciansweekly.com/post/optimizing-lung-cancer-therapy-efficacy-through-osa-management) | physiciansweekly.com | 8 | positive |
| 29 Apr 2026 | [If you're in the medical field, keep reading](https://www.newsbytesapp.com/news/science/ai-tools-boosting-healthcare-diagnosis-accuracy/story) | newsbytesapp.com | 8 | positive |
| 29 Apr 2026 | [Alex Cole-Hamilton pledges lung cancer test expansion after Edinburgh pilot success](https://www.heraldscotland.com/news/26060627.lib-dems-pledge-lung-cancer-screening-expansion-edinburgh-pilot/) | heraldscotland.com | 8 | negative |
| 28 Apr 2026 | [Cascade Cell-Assisted Enhanced Fluorescence Strategy for Highly Sensitive Detection of Lung Adenocarcinoma…](https://pubmed.ncbi.nlm.nih.gov/42059301/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Lung cancer brain metastases management at the dawn of personalized medicine: are we ready to break the…](https://pubmed.ncbi.nlm.nih.gov/42061818/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Early detection of bowel Cancer in the UK represents success of screening program - Pharmaceutical Technology](https://www.pharmaceutical-technology.com/analyst-comment/early-detection-of-bowel-cancer-in-the-uk-represents-success-of-screening-program/) | pharmaceutical-technology.com | 8 | negative |
| 27 Apr 2026 | [Cambio de paradigma en el diagnóstico del cáncer en Europa: más detección, pero menos mortalidad](https://www.consalud.es/pacientes/cambio-de-paradigma-en-el-diagnostico-del-cancer-en-europa-mas-diagnosticos-pero-menos-mortalidad.html) | consalud.es | 8 | negative |
| 26 Apr 2026 | [Platycodon D promotes immunogenic cell death in lung cancer cells by targeting NFS1 to induce PANoptosis.](https://pubmed.ncbi.nlm.nih.gov/42068882/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 25 Apr 2026 | [Barry Manilow Makes First Public Appearance After Lung Cancer Surgery](https://www.yahoo.com/entertainment/celebrity/articles/barry-manilow-makes-first-public-020907819.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "lung cancer" --since 2026-01-01 --until 2026-04-30
prism-news trends "lung cancer" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "lung cancer" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "lung cancer", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "lung cancer", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Dengue News](dengue-news.md)
- [Candida Auris Outbreak](candida-auris-outbreak.md)
- [Epidemic Outbreak](epidemic-outbreak.md)
- [Stroke News](stroke-news.md)
