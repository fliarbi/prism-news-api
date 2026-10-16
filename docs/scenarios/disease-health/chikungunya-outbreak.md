# Chikungunya Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “chikungunya outbreak” · 20/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [chikungunya-outbreak.json](../../examples/scenarios/chikungunya-outbreak.json).

**Question.** How much chikungunya coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="chikungunya"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 895 |
| Negative · neutral · positive | 58% · 2.9% · 39% |
| Critical (priority 7–9) | 79% (703 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (621 articles) |
| Most-reported country | United States (4.6% of matches) |
| Strongest theme by lift | vector-borne disease mitigation |

## Twelve months of coverage

Monthly matching articles for `chikungunya` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 508 | 68% | 295 | 183 | ████████████████ |
| Jun 2025 | 180 | 82% | 130 | 43 | ██████ |
| Jul 2025 | 310 | 82% | 212 | 84 | ██████████ |
| Aug 2025 | 621 | 88% | 505 | 110 | ████████████████████ |
| Sep 2025 | 283 | 82% | 191 | 89 | █████████ |
| Oct 2025 | 270 | 88% | 206 | 59 | █████████ |
| Nov 2025 | 180 | 68% | 111 | 63 | ██████ |
| Dec 2025 | 206 | 81% | 106 | 93 | ███████ |
| Jan 2026 | 165 | 84% | 91 | 69 | █████ |
| Feb 2026 | 245 | 75% | 155 | 85 | ████████ |
| Mar 2026 | 187 | 75% | 90 | 89 | ██████ |
| Apr 2026 | 298 | 81% | 181 | 109 | ██████████ |

The last four complete months averaged 224 articles a month against 405 in the first four (-45%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 20% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 41 | 4.6% |
| India | 38 | 4.2% |
| Brazil | 15 | 1.7% |
| United Kingdom | 13 | 1.4% |
| Cook Islands | 10 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| vector-borne disease mitigation | 129 | 21% | -32% |
| vector-borne disease epidemiology | 258 | 41% | -22% |
| global health challenges | 98 | 16% | -18% |
| zoonotic disease prevention measures | 139 | 22% | -38% |
| travel-related infectious disease risks | 113 | 18% | +11% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [COE confirma mais uma morte suspeita por Chikungunya em Dourados - RCN67](https://www.rcn67.com.br/dourados/coe-confirma-mais-uma-morte-suspeita-por-chikungunya-em-dourados-2/) | rcn67.com.br | 8 | negative |
| 26 Apr 2026 | [Seroprevalence of chikungunya virus infection and co-occurrence with malaria among patients with febrile…](https://pubmed.ncbi.nlm.nih.gov/42036962/) | pubmed.ncbi.nlm.nih.gov | 8 | negative |
| 22 Apr 2026 | [Dourados tem 6.411 notificaÃ§Ãµes e 2.204 casos confirmados de Chikungunya, segundo o Informe…](https://www.rcn67.com.br/dourados/dourados-tem-6-411-notificacoes-e-2-204-casos-confirmados-de-chikungunya/) | rcn67.com.br | 8 | negative |
| 19 Apr 2026 | [Vector-Borne Infections: Current Happenings 2026 formulated By Dr.T.V.Rao MD](https://www.linkedin.com/pulse/vector-borne-infections-current-happenings-2026-formulated-dr-t-v-rao-rb5xc) | linkedin.com | 8 | negative |
| 19 Apr 2026 | [Chikungunya therapy shows promise in first-in-human study](https://healio.com/news/infectious-disease/20260419/chikungunya-therapy-shows-promise-in-firstinhuman-study) | healio.com | 8 | positive |
| 18 Apr 2026 | [Dourados chega a 5 mil casos prováveis de chikungunya](https://midiamax.com.br/cotidiano/2026/dourados-chega-5-mil-casos-provaveis-chikungunya/) | midiamax.com.br | 8 | negative |
| 17 Apr 2026 | [Com 5,8 mil casos e 12 mortes, três cidades de MS decretam emergência por chikungunya](https://midiamax.com.br/cotidiano/2026/58-mil-casos-12-mortes-tres-cidades-ms-decretam-emergencia-chikungunya/) | midiamax.com.br | 8 | negative |
| 16 Apr 2026 | [Conselheiro de Saúde aciona MPF contra saída da Força Nacional do SUS de Dourados](https://midiamax.com.br/cotidiano/2026/conselheiro-saude-aciona-mpf-contra-saida-forca-nacional-sus-dourados/) | midiamax.com.br | 8 | negative |
| 16 Apr 2026 | [Epidemia: MS concentra 63% das mortes causadas por chikungunya no país](https://midiamax.com.br/cotidiano/2026/ms-confirma-12a-morte-chikungunya-concentra-63-obitos-pais/) | midiamax.com.br | 8 | negative |
| 16 Apr 2026 | [Bavarian Nordic Receives Swissmedic Approval for Chikungunya Vaccine](https://www.globenewswire.com/news-release/2026/04/16/3275022/0/en/Bavarian-Nordic-Receives-Swissmedic-Approval-for-Chikungunya-Vaccine.html) | globenewswire.com | 8 | positive |
| 14 Apr 2026 | [Chikungunya cases reported in Kerala: State govt steps up surveillance, issues advisory](https://www.indiatvnews.com/news/india/chikungunya-cases-reported-in-kerala-state-govt-steps-up-surveillance-issues-advisory-2026-04-14-1037527) | indiatvnews.com | 8 | negative |
| 11 Apr 2026 | [Casos de chikungunya aumentam na região urbana e Dourados chega a 1,5 mil infectados](https://midiamax.com.br/cotidiano/2026/casos-chikungunya-aumentam-regiao-urbana-dourados-chega-15-mil-infectados/) | midiamax.com.br | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "chikungunya" --since 2026-01-01 --until 2026-04-30
prism-news trends "chikungunya" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "chikungunya" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "chikungunya", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "chikungunya", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [CRISPR News](crispr-news.md)
- [Whooping Cough Outbreak](whooping-cough-outbreak.md)
- [Pandemic News](pandemic-news.md)
- [ADHD News](adhd-news.md)
