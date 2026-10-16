# Leprosy News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “leprosy news” · 10/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [leprosy-news.json](../../examples/scenarios/leprosy-news.json).

**Question.** How much leprosy coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="leprosy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 479 |
| Negative · neutral · positive | 37% · 4.4% · 58% |
| Critical (priority 7–9) | 63% (302 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (188 articles) |
| Most-reported country | India (15% of matches) |
| Strongest theme by lift | neglected tropical diseases |

## Twelve months of coverage

Monthly matching articles for `leprosy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 102 | 51% | 42 | 48 | ███████████ |
| Jun 2025 | 58 | 62% | 18 | 34 | ██████ |
| Jul 2025 | 75 | 49% | 24 | 46 | ████████ |
| Aug 2025 | 82 | 66% | 34 | 45 | █████████ |
| Sep 2025 | 84 | 63% | 31 | 46 | █████████ |
| Oct 2025 | 59 | 64% | 20 | 38 | ██████ |
| Nov 2025 | 64 | 69% | 16 | 44 | ███████ |
| Dec 2025 | 76 | 74% | 27 | 44 | ████████ |
| Jan 2026 | 188 | 69% | 77 | 100 | ████████████████████ |
| Feb 2026 | 85 | 62% | 32 | 50 | █████████ |
| Mar 2026 | 93 | 69% | 35 | 56 | ██████████ |
| Apr 2026 | 113 | 50% | 34 | 73 | ████████████ |

The last four complete months averaged 120 articles a month against 79 in the first four (+51%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 31% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 71 | 15% |
| United States | 18 | 3.8% |
| Nigeria | 12 | 2.5% |
| Indonesia | 8 | 1.7% |
| Brazil | 4 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| neglected tropical diseases | 68 | 33% | +51% |
| infectious disease complications in chronic illnesses | 24 | 12% | +118% |
| latent infections | 15 | 7.3% | +67% |
| diagnosis of atypical pathogens | 15 | 7.3% | +275% |
| rare bacterial infections | 53 | 26% | +0% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Telangana Reports Over 2,500 Leprosy Cases Annually](https://www.telugu360.com/telangana-reports-over-2500-leprosy-cases-annually/) | telugu360.com | 8 | negative |
| 28 Apr 2026 | [Temporal Trends and Projections of Leprosy in Brazil: Application of Machine Learning Techniques for…](https://pubmed.ncbi.nlm.nih.gov/42066748/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 24 Apr 2026 | [NLR India marks 27 years of service with call for stronger last-mile action against leprosy](https://www.aninews.in/news/world/asia/nlr-india-marks-27-years-of-service-with-call-for-stronger-last-mile-action-against-leprosy20260425030632) | aninews.in | 8 | negative |
| 9 Apr 2026 | [Un análisis de sangre combinado con inteligencia artificial abre el camino al diagnóstico precoz de la lepra](https://www.consalud.es/pacientes/un-analisis-de-sangre-combinado-con-inteligencia-artificial-abre-el-camino-al-diagnostico-precoz-de-la-lepra.html) | consalud.es | 8 | positive |
| 30 Mar 2026 | [ईरान के मिसाइल हमले से इजरायल के केमिकल प्लांट में लगी भीषण आग... जहरीली गैस के रिसाव का खतरा](https://www.agniban.com/missile-attack-causes-massive-fire-at-israeli-chemical-plant-risk-of-toxic-gas-leak/) | agniban.com | 8 | negative |
| 13 Mar 2026 | [PAHO Director highlights regional commitment to eliminating leprosy at conference in Rio de Janeiro](https://www.paho.org/en/news/13-3-2026-paho-director-highlights-regional-commitment-eliminating-leprosy-conference-rio) | paho.org | 8 | negative |
| 11 Mar 2026 | [Health Minister calls for accelerated leprosy screening, surveillance](https://en.antaranews.com/news/407995/health-minister-calls-for-accelerated-leprosy-screening-surveillance) | en.antaranews.com | 8 | positive |
| 8 Mar 2026 | [Chile Eliminates Leprosy: First in Americas, Second Globally \| WHO & PAHO Report - News Directory 3](https://www.newsdirectory3.com/chile-eliminates-leprosy-first-in-americas-second-globally-who-paho-report/) | newsdirectory3.com | 8 | negative |
| 6 Mar 2026 | [Chile es el primer país de América libre de lepra](https://www.dw.com/es/chile-es-el-primer-país-de-américa-oficialmente-libre-de-lepra/a-76244196) | dw.com | 8 | negative |
| 4 Mar 2026 | [Chile Eliminates Leprosy, Sets Regional Benchmark](https://mexicobusiness.news/health/news/chile-eliminates-leprosy-sets-regional-benchmark) | mexicobusiness.news | 8 | negative |
| 4 Mar 2026 | [Chile becomes the first country in the Americas to be verified by WHO for the elimination of leprosy](https://www.nationaltribune.com.au/chile-becomes-the-first-country-in-the-americas-to-be-verified-by-who-for-the-elimination-of-leprosy/) | nationaltribune.com.au | 8 | negative |
| 1 Mar 2026 | [US-Israel Attacks Iran LIVE: इजरायल-अमेरिका नहीं... इन तीन देशों पर ईरान ने किया एक साथ हमला](https://www.aajtak.in/world/story/israel-vs-iran-live-updates-tehran-bombed-attack-middle-east-tensions-us-trump-on-nuclear-talks-ntc-ntyv-2484044-2026-03-02) | aajtak.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "leprosy" --since 2026-01-01 --until 2026-04-30
prism-news trends "leprosy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "leprosy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "leprosy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "leprosy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Antibiotics News](antibiotics-news.md)
- [Kidney Disease News](kidney-disease-news.md)
- [Drug Shortage News](drug-shortage-news.md)
- [Thalassemia News](thalassemia-news.md)
