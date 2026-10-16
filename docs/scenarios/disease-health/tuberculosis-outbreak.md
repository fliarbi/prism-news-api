# Tuberculosis Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tuberculosis outbreak” · 40/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [tuberculosis-outbreak.json](../../examples/scenarios/tuberculosis-outbreak.json).

**Question.** How much tuberculosis coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="tuberculosis"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,497 |
| Negative · neutral · positive | 35% · 6.5% · 58% |
| Critical (priority 7–9) | 87% (3,900 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (1,235 articles) |
| Most-reported country | United States (7.0% of matches) |
| Strongest theme by lift | latent infections |

## Twelve months of coverage

Monthly matching articles for `tuberculosis` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 858 | 83% | 301 | 492 | ██████████████ |
| Jun 2025 | 653 | 85% | 181 | 407 | ███████████ |
| Jul 2025 | 757 | 85% | 236 | 468 | ████████████ |
| Aug 2025 | 758 | 84% | 230 | 469 | ████████████ |
| Sep 2025 | 818 | 90% | 251 | 505 | █████████████ |
| Oct 2025 | 789 | 87% | 192 | 523 | █████████████ |
| Nov 2025 | 926 | 90% | 298 | 567 | ███████████████ |
| Dec 2025 | 924 | 90% | 273 | 584 | ███████████████ |
| Jan 2026 | 1,164 | 86% | 325 | 712 | ███████████████████ |
| Feb 2026 | 948 | 90% | 419 | 482 | ███████████████ |
| Mar 2026 | 1,235 | 85% | 412 | 761 | ████████████████████ |
| Apr 2026 | 1,150 | 86% | 432 | 649 | ███████████████████ |

The last four complete months averaged 1,124 articles a month against 756 in the first four (+49%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 29% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 314 | 7.0% |
| India | 277 | 6.2% |
| Canada | 142 | 3.2% |
| Italy | 87 | 1.9% |
| Nigeria | 65 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| latent infections | 635 | 22% | +53% |
| infectious disease complications in chronic illnesses | 538 | 19% | +71% |
| diagnosis of atypical pathogens | 262 | 9.1% | +49% |
| community-acquired infections | 242 | 8.4% | +122% |
| opportunistic infections in immunocompromised patients | 575 | 20% | +41% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Apr 2026 | [Old disease, new battle: Central Texas health experts working to fight Tuberculosis cases in Texas](https://www.kxxv.com/news/local-news/in-your-neighborhood/brazos-county/old-disease-new-battle-central-texas-health-experts-working-to-fight-tuberculosis-cases-in-texas) | kxxv.com | 9 | negative |
| 10 Apr 2026 | [Pakistan TB Crisis: 1,800 Daily Cases, 140 Deaths](https://www.newkerala.com/news/a/pakistans-current-response-tb-insufficient-as-cases-continue-153.htm) | newkerala.com | 9 | negative |
| 26 Mar 2026 | ['White Plague': One Of Humanity's Deadliest Killers Resurging In US](https://www.ndtv.com/feature/white-plague-one-of-humanitys-deadliest-killers-resurging-in-us-11270554) | ndtv.com | 9 | negative |
| 24 Mar 2026 | [Cambodia achieves significant results in fight against tuberculosis: PM Manet](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/03/24/cambodia-achieves-significant-results-in-fight-against-tuberculosis-pm-manet) | thestar.com.my | 9 | negative |
| 24 Mar 2026 | [Tuberkulose wird für Europa zunehmend zur tödlichen Gefahr](https://www.n-tv.de/wissen/Tuberkulose-wird-fuer-Europa-zunehmend-zur-toedlichen-Gefahr-id30504456.html) | n-tv.de | 9 | negative |
| 23 Mar 2026 | [To stop TB we must act now â together](https://www.dailymaverick.co.za/opinionista/2026-03-23-to-stop-tb-we-must-act-now-together/) | dailymaverick.co.za | 9 | negative |
| 20 Mar 2026 | [Alerta por tuberculosis: España registra un repunte del 8% y se aleja de los objetivos de la OMS](https://www.consalud.es/pacientes/alerta-por-tuberculosis-espana-registra-un-repunte-del-8-y-se-aleja-de-los-objetivos-de-la-oms.html) | consalud.es | 9 | negative |
| 1 Mar 2026 | [Disseminated Tuberculosis With Granulomatous Pericarditis: The Essential Role of Forensic Histopathology in…](https://pubmed.ncbi.nlm.nih.gov/42046626/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 2 Feb 2026 | [Savannah Guthrie's Mother Missing in Arizona \| KTLA - TIme News](https://time.news/savannah-guthries-mother-missing-in-arizona-ktla/) | time.news | 9 | negative |
| 30 Apr 2026 | [No sputum needed: Easy-to-use TB test shows accuracy in 7-country analysis](http://www.cidrap.umn.edu/tuberculosis/no-sputum-needed-easy-use-tb-test-shows-accuracy-7-country-analysis) | cidrap.umn.edu | 8 | positive |
| 30 Apr 2026 | [Portable Tuberculosis Test Matches Laboratory Accuracy in Minutes, Study Finds](https://clpmag.com/diagnostic-technologies/molecular-diagnostics/portable-tuberculosis-test-matches-lab-accuracy/) | clpmag.com | 8 | positive |
| 30 Apr 2026 | [Two Gates grants back Evotec push for shorter, safer TB treatment](https://www.stocktitan.net/news/EVO/evotec-receives-grants-to-advance-tuberculosis-co6h8tom6xry.html) | stocktitan.net | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "tuberculosis" --since 2026-01-01 --until 2026-04-30
prism-news trends "tuberculosis" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "tuberculosis" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "tuberculosis", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "tuberculosis", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Salmonella Outbreak](salmonella-outbreak.md)
- [Norovirus Outbreak](norovirus-outbreak.md)
- [Cholera Outbreak](cholera-outbreak.md)
- [Vaccine News](vaccine-news.md)
