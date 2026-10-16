# Prostate Cancer News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “prostate cancer news” · 30/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [prostate-cancer-news.json](../../examples/scenarios/prostate-cancer-news.json).

**Question.** How much prostate cancer coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="prostate cancer"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,397 |
| Negative · neutral · positive | 25% · 3.4% · 72% |
| Critical (priority 7–9) | 91% (4,021 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (2,306 articles) |
| Most-reported country | United States (12% of matches) |
| Strongest theme by lift | prostate cancer risk factors |

## Twelve months of coverage

Monthly matching articles for `prostate cancer` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,306 | 87% | 1,352 | 899 | ████████████████████ |
| Jun 2025 | 904 | 88% | 159 | 701 | ████████ |
| Jul 2025 | 904 | 87% | 184 | 688 | ████████ |
| Aug 2025 | 790 | 90% | 166 | 594 | ███████ |
| Sep 2025 | 1,040 | 90% | 206 | 778 | █████████ |
| Oct 2025 | 1,163 | 91% | 310 | 813 | ██████████ |
| Nov 2025 | 1,165 | 88% | 222 | 901 | ██████████ |
| Dec 2025 | 1,103 | 93% | 154 | 914 | ██████████ |
| Jan 2026 | 1,249 | 92% | 215 | 972 | ███████████ |
| Feb 2026 | 921 | 87% | 184 | 693 | ████████ |
| Mar 2026 | 957 | 92% | 158 | 764 | ████████ |
| Apr 2026 | 1,270 | 94% | 537 | 706 | ███████████ |

The last four complete months averaged 1,099 articles a month against 1,226 in the first four (-10%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 23% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 519 | 12% |
| United Kingdom | 156 | 3.5% |
| Canada | 85 | 1.9% |
| Israel | 32 | 0.7% |
| Australia | 30 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| prostate cancer risk factors | 2,313 | 65% | +0% |
| radiation-induced tissue damage mitigation | 399 | 11% | +11% |
| oncology and targeted therapy advancements | 222 | 6.3% | +12% |
| hormone therapy for breast cancer | 130 | 3.7% | +38% |
| liquid biopsy for early detection | 115 | 3.2% | +8% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Mar 2026 | [Joe Biden Hidden Illness: Physician Claims Cancer Spread to Bone During Presidency](https://www.ibtimes.co.uk/joe-biden-hidden-illness-physician-claims-cancer-spread-bone-during-presidency-1787216) | ibtimes.co.uk | 9 | negative |
| 30 Jan 2026 | [Exclusive: Patriots DC Terrell Williams cancer-free after battle with prostate cancer](https://www.bostonherald.com/2026/01/30/exclusive-patriots-dc-terrell-williams-cancer-free-after-battle-with-prostate-cancer/) | bostonherald.com | 9 | — |
| 28 Apr 2026 | [JOE.ie - Prostate cancer symptoms as Chris Hoy issues new health update](https://www.joe.ie/news/prostate-cancer-symptoms-as-chris-hoy-issues-new-health-update-870332) | joe.ie | 8 | positive |
| 28 Apr 2026 | [The Equivalents Are Coming! Developing a Shared Nomenclature for Radiopharmaceutical Therapy of…](https://pubmed.ncbi.nlm.nih.gov/42061947/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [HF-125, a first-in-class computer-modeled novel inhibitor of Tribbles 2, for therapy of enzalutamide…](https://pubmed.ncbi.nlm.nih.gov/42094475/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Prostate Cancer, Part 2: PSMA and Beyond.](https://pubmed.ncbi.nlm.nih.gov/42049456/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Bracing for the Flood: How Should We Manage Prostate Cancer Care by 2050?](https://www.emjreviews.com/urology/article/bracing-for-the-flood-how-should-we-manage-prostate-cancer-care-by-2050-j18126/) | emjreviews.com | 8 | positive |
| 25 Apr 2026 | [Netanyahu confirma que fue diagnosticado con cáncer de próstata](https://www.excelsior.com.mx/internacional/netanyahu-confirma-que-fue-diagnosticado-con-cancer-prostata) | excelsior.com.mx | 8 | negative |
| 25 Apr 2026 | [Le dÃ©pistage du cancer de la prostate rate sa cible en Suisse](https://www.tdg.ch/cancer-de-la-prostate-le-depistage-rate-sa-cible-en-suisse-849307124777) | tdg.ch | 8 | negative |
| 25 Apr 2026 | [Israel PM Benjamin Netanyahu Treated For Early-Stage Prostate Cancer](https://www.oneindia.com/international/israel-pm-benjamin-netanyahu-treated-for-early-stage-prostate-cancer-011-8069089.html) | oneindia.com | 8 | negative |
| 25 Apr 2026 | [Israel's Benjamin Netanyahu says he was treated for prostate cancer and is now healthy](http://gulfnews.com/world/mena/israels-benjamin-netanyahu-says-he-was-treated-for-prostate-cancer-and-is-now-healthy-1.500518163) | gulfnews.com | 8 | negative |
| 25 Apr 2026 | [Netanyahu ocultó su tratamiento contra un cáncer de próstata](https://www.diariodeleon.es/internacional/260425/2082883/netanyahu-oculto-tratamiento-cancer-prostata.html) | diariodeleon.es | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "prostate cancer" --since 2026-01-01 --until 2026-04-30
prism-news trends "prostate cancer" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "prostate cancer" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "prostate cancer", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "prostate cancer", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Gene Therapy News](gene-therapy-news.md)
- [Zika Outbreak](zika-outbreak.md)
- [Hepatitis Outbreak](hepatitis-outbreak.md)
- [Malaria Outbreak](malaria-outbreak.md)
