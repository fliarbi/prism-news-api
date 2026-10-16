# Zika Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “zika outbreak” · 40/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [zika-outbreak.json](../../examples/scenarios/zika-outbreak.json).

**Question.** How much zika coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="zika"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 466 |
| Negative · neutral · positive | 31% · 5.0% · 64% |
| Critical (priority 7–9) | 78% (362 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (923 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | vector-borne disease epidemiology |

## Twelve months of coverage

Monthly matching articles for `zika` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 923 | 72% | 525 | 342 | ████████████████████ |
| Jun 2025 | 151 | 80% | 78 | 66 | ███ |
| Jul 2025 | 155 | 74% | 76 | 76 | ███ |
| Aug 2025 | 215 | 73% | 133 | 76 | █████ |
| Sep 2025 | 106 | 87% | 34 | 68 | ██ |
| Oct 2025 | 123 | 72% | 35 | 85 | ███ |
| Nov 2025 | 113 | 69% | 34 | 74 | ██ |
| Dec 2025 | 121 | 87% | 38 | 80 | ███ |
| Jan 2026 | 138 | 80% | 49 | 79 | ███ |
| Feb 2026 | 115 | 84% | 25 | 85 | ██ |
| Mar 2026 | 118 | 73% | 35 | 79 | ███ |
| Apr 2026 | 95 | 73% | 36 | 54 | ██ |

The last four complete months averaged 116 articles a month against 361 in the first four (-68%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 23% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 66 | 14% |
| Italy | 5 | 1.1% |
| Nigeria | 5 | 1.1% |
| Brazil | 4 | 0.9% |
| Canada | 3 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| vector-borne disease epidemiology | 147 | 41% | +30% |
| travel-related infectious disease risks | 78 | 22% | +26% |
| global health emerging threats | 42 | 12% | -12% |
| vector-borne disease mitigation | 31 | 8.6% | +41% |
| global health challenges | 27 | 7.5% | +50% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 7 Apr 2026 | [Belize Issues Urgent Health Alert as Mosquito-Borne Diseases Surge, Prompting Crucial Travel Warnings for…](https://www.travelandtourworld.com/news/article/belize-issues-urgent-health-alert-as-mosquito-borne-diseases-surge-prompting-crucial-travel-warnings-for-u-s-tourists-ahead-of-2026-peak-season/) | travelandtourworld.com | 8 | negative |
| 29 Mar 2026 | [Mosquito Bites: New Gut Mechanism Could Reduce Feeding & Reproduction - Time News](https://time.news/mosquito-bites-new-gut-mechanism-could-reduce-feeding-reproduction/) | time.news | 8 | positive |
| 2 Feb 2026 | [Fighting an epidemic \| Texas Children's](https://www.texaschildrens.org/content/media/fighting-epidemic) | texaschildrens.org | 8 | negative |
| 21 Jan 2026 | [Opportunities and Challenges of mRNA and VLP Technologies for Pan-Flavivirus Vaccine Development: Focus on…](https://pubmed.ncbi.nlm.nih.gov/41596723/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 1 Jan 2026 | [Arbovirus-Host Epigenetic Interplay: Unraveling the Neurological Mechanisms and Therapeutic Opportunities.](https://pubmed.ncbi.nlm.nih.gov/41351464/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Agent-Based Modeling Approach for Population Dynamics of the Biological Vector Aedes Aegypti.](https://pubmed.ncbi.nlm.nih.gov/42013888/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 15 Apr 2026 | [¿Cuánto gasta Guatemala en combatir el zancudo que transmite el dengue y chinkungunya?](https://www.prensalibre.com/guatemala/comunitario/salud-destina-q189-8-millones-para-combatir-dengue-chikungunya-y-zika-guatemala/) | prensalibre.com | 7 | negative |
| 14 Apr 2026 | [Com alta de casos e mortes, MPMS reforÃ§a fiscalizaÃ§Ã£o contra dengue e chikungunya em Dourados - RCN67](https://www.rcn67.com.br/dourados/com-alta-de-casos-e-mortes-mpms-reforca-fiscalizacao-contra-dengue-e-chikungunya-em-dourados/) | rcn67.com.br | 7 | positive |
| 11 Apr 2026 | [How Mosquitoes Find Humans: New AI Model Decodes Flight Patterns - Time News](https://time.news/how-mosquitoes-find-humans-new-ai-model-decodes-flight-patterns/) | time.news | 7 | positive |
| 10 Apr 2026 | [Retiraron 40 toneladas de chatarra \| La Municipalidad de Salta realizó un nuevo operativo de descacharrado](https://flipr.com.ar/salta/cuatro/retiraron-40-toneladas-de-chatarra-la-municipalidad-de-salta-realizo-un-nuevo-operativo-de-descacharrado/) | flipr.com.ar | 7 | positive |
| 9 Apr 2026 | [So real ist die Dengue-Gefahr in Deutschland](https://www.gmx.net/magazine/gesundheit/gross-dengue-bedrohung-deutschland-42093548) | gmx.net | 7 | negative |
| 7 Apr 2026 | [Operational strategies among infectious disease clinical trial sites during pandemics: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/41943131/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "zika" --since 2026-01-01 --until 2026-04-30
prism-news trends "zika" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "zika" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "zika", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "zika", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [ADHD News](adhd-news.md)
- [Gene Therapy News](gene-therapy-news.md)
- [Prostate Cancer News](prostate-cancer-news.md)
- [Hepatitis Outbreak](hepatitis-outbreak.md)
