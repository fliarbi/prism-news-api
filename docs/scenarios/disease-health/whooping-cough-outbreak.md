# Whooping Cough Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “whooping cough outbreak” · 10/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [whooping-cough-outbreak.json](../../examples/scenarios/whooping-cough-outbreak.json).

**Question.** How much whooping cough coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="whooping cough"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 144 |
| Negative · neutral · positive | 72% · 2.1% · 26% |
| Critical (priority 7–9) | 81% (117 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (236 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | pediatric infectious disease case studies |

## Twelve months of coverage

Monthly matching articles for `whooping cough` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 73 | 80% | 58 | 15 | ██████ |
| Jun 2025 | 38 | 87% | 29 | 7 | ███ |
| Jul 2025 | 58 | 83% | 44 | 14 | █████ |
| Aug 2025 | 87 | 85% | 67 | 18 | ███████ |
| Sep 2025 | 87 | 94% | 70 | 16 | ███████ |
| Oct 2025 | 53 | 100% | 50 | 3 | ████ |
| Nov 2025 | 236 | 89% | 180 | 53 | ████████████████████ |
| Dec 2025 | 78 | 95% | 49 | 27 | ███████ |
| Jan 2026 | 29 | 97% | 15 | 14 | ██ |
| Feb 2026 | 42 | 81% | 30 | 8 | ████ |
| Mar 2026 | 34 | 65% | 27 | 7 | ███ |
| Apr 2026 | 39 | 85% | 30 | 8 | ███ |

The last four complete months averaged 36 articles a month against 64 in the first four (-44%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 22 | 15% |
| Australia | 11 | 7.6% |
| Italy | 7 | 4.9% |
| United Kingdom | 5 | 3.5% |
| Germany | 4 | 2.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| pediatric infectious disease case studies | 27 | 25% | -58% |
| community-acquired infections | 13 | 12% | -74% |
| vaccine myths and misinformation countermeasures | 12 | 11% | -50% |
| maternal and neonatal immunization strategies | 11 | 10% | +57% |
| pediatric vaccination requirements | 31 | 29% | -30% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 6 Feb 2026 | [Whooping cough cases are at their highest level in 35 years – so why the surge?](https://www.nationaltribune.com.au/whooping-cough-cases-are-at-their-highest-level-in-35-years-so-why-the-surge/) | nationaltribune.com.au | 9 | negative |
| 30 Apr 2026 | [Whooping cough outbreak: Pasadena health officials confirm 4 cases at school](https://abc7.com/post/whooping-cough-outbreak-pasadena-health-officials-confirm-4-cases-don-benito-fundamental-school/19005637/) | abc7.com | 8 | negative |
| 22 Apr 2026 | [2026 में लौट रही हैं ‘भूली-बिसरी’ जानलेवा बीमारियां! क्या बचपन में लगे टीके आज भी असरदार है? \| Global…](https://www.patrika.com/health-news/global-resurgence-measles-whooping-cough-2026-alert-hindi-20520898) | patrika.com | 8 | negative |
| 7 Apr 2026 | [Whatcom County monitoring cluster of whooping cough cases at Western Washington University](https://www.yahoo.com/news/articles/whatcom-county-monitoring-cluster-whooping-010432291.html) | yahoo.com | 8 | negative |
| 1 Apr 2026 | [Whooping Cough Rising in Netherlands After COVID-19 Measures Lifted - RIVM - Time News](https://time.news/whooping-cough-rising-in-netherlands-after-covid-19-measures-lifted-rivm/) | time.news | 8 | negative |
| 31 Mar 2026 | [Whooping Cough: How an Outbreak Impacted Blake's Life - Time News](https://time.news/whooping-cough-how-an-outbreak-impacted-blakes-life/) | time.news | 8 | negative |
| 24 Mar 2026 | ['I'm a doctor - when your two-week cough needs checking out'](https://www.express.co.uk/life-style/health/2185972/doctor-warning-whooping-cough) | express.co.uk | 8 | negative |
| 18 Mar 2026 | [Whooping cough case confirmed at Preston County middle school](https://www.yahoo.com/news/articles/whooping-cough-case-confirmed-preston-174034215.html) | yahoo.com | 8 | negative |
| 22 Feb 2026 | [Vanuatu's Health Ministry says whooping cough under control](https://www.radionz.co.nz/international/pacific-news/587609/vanuatu-s-health-ministry-says-whooping-cough-under-control) | radionz.co.nz | 8 | negative |
| 21 Feb 2026 | [Texas logged more than 4,000 cases of whooping cough last year, a 60-year high](https://www.yahoo.com/news/articles/texas-logged-more-4-000-215153210.html) | yahoo.com | 8 | negative |
| 16 Feb 2026 | [Deadly disease spikes as vaccine rates fall](https://www.thewest.com.au/news/whooping-cough-numbers-at-record-highs-as-vaccine-rates-fall-across-australia-c-21657460) | thewest.com.au | 8 | negative |
| 16 Feb 2026 | [Vanuatu whooping cough death toll rises to seven](https://www.rnz.co.nz/international/pacific-news/586995/vanuatu-whooping-cough-death-toll-rises-to-seven) | rnz.co.nz | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "whooping cough" --since 2026-01-01 --until 2026-04-30
prism-news trends "whooping cough" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "whooping cough" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "whooping cough", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "whooping cough", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Mpox Outbreak](mpox-outbreak.md)
- [CRISPR News](crispr-news.md)
- [Chikungunya Outbreak](chikungunya-outbreak.md)
- [Pandemic News](pandemic-news.md)
