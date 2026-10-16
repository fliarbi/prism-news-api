# Mpox Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mpox outbreak” · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [mpox-outbreak.json](../../examples/scenarios/mpox-outbreak.json).

**Question.** How much mpox coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="mpox"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 661 |
| Negative · neutral · positive | 50% · 2.9% · 48% |
| Critical (priority 7–9) | 92% (606 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (222 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | viral hemorrhagic fevers |

## Twelve months of coverage

Monthly matching articles for `mpox` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 194 | 82% | 77 | 109 | █████████████████ |
| Jun 2025 | 154 | 87% | 78 | 70 | ██████████████ |
| Jul 2025 | 215 | 80% | 116 | 99 | ███████████████████ |
| Aug 2025 | 177 | 94% | 90 | 79 | ████████████████ |
| Sep 2025 | 222 | 93% | 113 | 108 | ████████████████████ |
| Oct 2025 | 187 | 96% | 100 | 81 | █████████████████ |
| Nov 2025 | 128 | 88% | 37 | 89 | ████████████ |
| Dec 2025 | 215 | 92% | 66 | 140 | ███████████████████ |
| Jan 2026 | 179 | 93% | 82 | 94 | ████████████████ |
| Feb 2026 | 150 | 88% | 63 | 79 | ██████████████ |
| Mar 2026 | 153 | 90% | 79 | 68 | ██████████████ |
| Apr 2026 | 179 | 95% | 103 | 72 | ████████████████ |

The last four complete months averaged 165 articles a month against 185 in the first four (-11%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 33% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 93 | 14% |
| United Kingdom | 16 | 2.4% |
| Democratic Republic of the Congo | 11 | 1.7% |
| Ghana | 11 | 1.7% |
| Nigeria | 11 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| viral hemorrhagic fevers | 43 | 10% | +16% |
| global health challenges | 40 | 9.5% | +43% |
| emerging viral diseases | 94 | 22% | -4% |
| global health emerging threats | 32 | 7.6% | +10% |
| travel-related infectious disease risks | 42 | 10% | +0% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 3 Apr 2026 | [DR Congo lifts national mpox emergency after two years](https://tunisianstar.com/dr-congo-lifts-national-mpox-emergency-two-years/) | tunisianstar.com | 9 | negative |
| 3 Apr 2026 | [Congo declares end of two-year mpox outbreak that killed over 2,000 \| Africanews](https://www.africanews.com/2026/04/03/congo-declares-end-of-two-year-mpox-outbreak-that-killed-over-2000/) | africanews.com | 9 | negative |
| 2 Apr 2026 | [Congo says its mpox outbreak is over after 2 years and more than 2,200 suspected deaths](https://us.headtopics.com/news/congo-says-its-mpox-outbreak-is-over-after-2-years-and-more-81772269) | us.headtopics.com | 9 | negative |
| 27 Mar 2026 | [La OMS alerta del riesgo de transmisión sostenida de mpox si no se frenan los brotes](https://www.consalud.es/pacientes/la-oms-alerta-del-riesgo-de-transmision-sostenida-de-mpox-si-no-se-frenan-los-brotes.html) | consalud.es | 9 | negative |
| 9 Mar 2026 | [Ghana records eight deaths, over 1,000 mpox cases since May 2025 – Health Minister - MyJoyOnline](https://www.myjoyonline.com/ghana-records-eight-deaths-over-1000-mpox-cases-since-may-2025-health-minister/) | myjoyonline.com | 9 | negative |
| 1 Mar 2026 | [Mpox Outbreak in the East Africa Region: Current Status, Containment Measures, Challenges, and Future…](https://pubmed.ncbi.nlm.nih.gov/41675254/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 18 Feb 2026 | [Madagascar Mpox Cases Rise: Awareness & Growing Concerns - News Directory 3](https://www.newsdirectory3.com/madagascar-mpox-cases-rise-awareness-growing-concerns/) | newsdirectory3.com | 9 | negative |
| 30 Apr 2026 | [In Madagascar, stigma is undermining the fight against mpox](https://www.gavi.org/vaccineswork/madagascar-stigma-undermining-fight-against-mpox) | gavi.org | 8 | negative |
| 28 Apr 2026 | [High-throughput multiplex immunoassay for the detection of mpox and MVA-BN vaccination up to 2 years after…](https://pubmed.ncbi.nlm.nih.gov/42068991/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 24 Apr 2026 | [Africa CDC Aware Of Reported COVID-19 Cases In Nigeria](https://sciencenigeria.com/africa-cdc-aware-of-reported-covid-19-cases-in-nigeria/) | sciencenigeria.com | 8 | positive |
| 21 Apr 2026 | [Mpox Cases Soar In CA As Rare Strain Detected For First Time In San Francisco](https://patch.com/california/san-francisco/mpox-cases-soar-ca-rare-strain-detected-first-time-san-francisco) | patch.com | 8 | positive |
| 20 Apr 2026 | [Vaccinations urged as dangerous strain of mpox virus emerges in Northern California](https://www.pottsmerc.com/2026/04/20/dangerous-mpox-clade-california-vaccinations-urged/) | pottsmerc.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "mpox" --since 2026-01-01 --until 2026-04-30
prism-news trends "mpox" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "mpox" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "mpox", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "mpox", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Nipah Outbreak](nipah-outbreak.md)
- [Rabies Outbreak](rabies-outbreak.md)
- [CRISPR News](crispr-news.md)
- [Whooping Cough Outbreak](whooping-cough-outbreak.md)
