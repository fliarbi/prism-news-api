# Epidemic Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “epidemic outbreak” · 50/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [epidemic-outbreak.json](../../examples/scenarios/epidemic-outbreak.json).

**Question.** How much epidemic coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="epidemic"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,834 |
| Negative · neutral · positive | 59% · 4.2% · 37% |
| Critical (priority 7–9) | 80% (2,267 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (1,390 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | global health challenges |

## Twelve months of coverage

Monthly matching articles for `epidemic` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,299 | 78% | 929 | 317 | ███████████████████ |
| Jun 2025 | 610 | 77% | 353 | 232 | █████████ |
| Jul 2025 | 848 | 70% | 597 | 228 | ████████████ |
| Aug 2025 | 1,390 | 77% | 1,035 | 333 | ████████████████████ |
| Sep 2025 | 614 | 77% | 367 | 225 | █████████ |
| Oct 2025 | 650 | 83% | 411 | 225 | █████████ |
| Nov 2025 | 689 | 76% | 421 | 249 | ██████████ |
| Dec 2025 | 896 | 75% | 526 | 328 | █████████████ |
| Jan 2026 | 783 | 80% | 412 | 337 | ███████████ |
| Feb 2026 | 660 | 79% | 386 | 240 | █████████ |
| Mar 2026 | 622 | 82% | 379 | 215 | █████████ |
| Apr 2026 | 769 | 79% | 483 | 257 | ███████████ |

The last four complete months averaged 708 articles a month against 1,037 in the first four (-32%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 29% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 406 | 14% |
| India | 84 | 3.0% |
| United Kingdom | 55 | 1.9% |
| Nigeria | 22 | 0.8% |
| Mexico | 17 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| global health challenges | 120 | 6.9% | +48% |
| infectious disease control strategies | 78 | 4.5% | +28% |
| covid-19 public health policies and lockdown measures | 78 | 4.5% | +8% |
| immunization strategies for rare diseases | 63 | 3.6% | +3% |
| public health emergency preparedness | 182 | 11% | +36% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Mar 2026 | [Israel says antisemitism raging in Netherlands after Jewish school blast](https://www.thehindu.com/news/international/israel-says-antisemitism-raging-in-netherlands-after-jewish-school-blast/article70744242.ece) | thehindu.com | 9 | negative |
| 21 Jan 2026 | [États-Unis : L’épidémie de rougeole s’intensifie et menace le statut sanitaire du pays](https://burkina24.com/2026/01/21/etats-unis-lepidemie-de-rougeole-sintensifie-et-menace-le-statut-sanitaire-du-pays/) | burkina24.com | 9 | negative |
| 20 Jan 2026 | [Odisha’s growth story is dying of kidney disease](https://sambadenglish.com/columns-and-analysis/odishas-growth-story-is-dying-of-kidney-disease-11015417) | sambadenglish.com | 9 | negative |
| 13 Jan 2026 | [Time for decisive action on substance-use disorder treatment](https://www.ama-assn.org/public-health/behavioral-health/time-decisive-action-substance-use-disorder-treatment) | ama-assn.org | 9 | negative |
| 7 Jan 2026 | [Flu Epidemic 2024: US Hospitalizations & Deaths Surge - TIme News](https://time.news/flu-epidemic-2024-us-hospitalizations-deaths-surge/) | time.news | 9 | negative |
| 1 Jan 2026 | [Transmitted by Rats and Rodents: Warnings of a Potential Leptospirosis Outbreak in Gaza - Jordan News \|…](https://www.jordannews.jo/Section-20/Middle-East/Transmitted-by-Rats-and-Rodents-Warnings-of-a-Potential-Leptospirosis-Outbreak-in-Gaza-47779) | jordannews.jo | 9 | negative |
| 23 Apr 2026 | [Prix du carburant : « Une nouvelle mobilisation des gilets jaunes n’est pas à redouter »](https://www.la-croix.com/a-vif/prix-du-carburant-une-nouvelle-mobilisation-des-gilets-jaunes-n-est-pas-a-redouter-20260423) | la-croix.com | 8 | negative |
| 23 Apr 2026 | [How Delaware can prevent gun violence before it happens \| Opinion](https://www.delawareonline.com/story/opinion/2026/04/23/delaware-gun-regulations/89735314007/) | delawareonline.com | 8 | negative |
| 17 Apr 2026 | [Targeting the virus-host interface for the development of therapeutics against filoviruses.](https://pubmed.ncbi.nlm.nih.gov/42001552/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 14 Apr 2026 | [Niël Terblanché In a pressing announcement, the Ministry of Health and Social Services (MoHSS) of Namibia…](https://www.observer24.com.na/malaria-epidemic-alert-registered-in-namibia/) | observer24.com.na | 8 | negative |
| 9 Apr 2026 | [Tuberculose Au Mali \| Un Défi De Santé Publique Persistant Malgré Des Efforts Accrus](https://maliactu.net/tuberculose-au-mali-un-defi-de-sante-publique-persistant-malgre-des-efforts-accrus/) | maliactu.net | 8 | negative |
| 4 Apr 2026 | [Application of TE Series Ultrasound against COVID-19 - Mindray](https://www.mindray.com/en/covid-19-response/application-of-te-series-ultrasound-against-covid-19) | mindray.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "epidemic" --since 2026-01-01 --until 2026-04-30
prism-news trends "epidemic" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "epidemic" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "epidemic", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "epidemic", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Candida Auris Outbreak](candida-auris-outbreak.md)
- [Lung Cancer News](lung-cancer-news.md)
- [Stroke News](stroke-news.md)
- [Antimicrobial Resistance News](antimicrobial-resistance-news.md)
