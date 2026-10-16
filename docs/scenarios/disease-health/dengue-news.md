# Dengue News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “dengue news” · 320/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [dengue-news.json](../../examples/scenarios/dengue-news.json).

**Question.** How much dengue coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="dengue"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,890 |
| Negative · neutral · positive | 43% · 2.5% · 55% |
| Critical (priority 7–9) | 68% (1,288 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (1,171 articles) |
| Most-reported country | India (4.9% of matches) |
| Strongest theme by lift | vector-borne disease mitigation |

## Twelve months of coverage

Monthly matching articles for `dengue` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,171 | 66% | 682 | 448 | ████████████████████ |
| Jun 2025 | 469 | 69% | 270 | 185 | ████████ |
| Jul 2025 | 705 | 68% | 420 | 267 | ████████████ |
| Aug 2025 | 984 | 70% | 677 | 284 | █████████████████ |
| Sep 2025 | 864 | 78% | 588 | 261 | ███████████████ |
| Oct 2025 | 475 | 79% | 299 | 164 | ████████ |
| Nov 2025 | 580 | 78% | 334 | 232 | ██████████ |
| Dec 2025 | 434 | 81% | 208 | 213 | ███████ |
| Jan 2026 | 432 | 81% | 199 | 217 | ███████ |
| Feb 2026 | 356 | 81% | 156 | 191 | ██████ |
| Mar 2026 | 404 | 72% | 199 | 195 | ███████ |
| Apr 2026 | 698 | 51% | 254 | 431 | ████████████ |

The last four complete months averaged 472 articles a month against 832 in the first four (-43%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 18% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 92 | 4.9% |
| United States | 56 | 3.0% |
| Bangladesh | 24 | 1.3% |
| Cook Islands | 23 | 1.2% |
| Brazil | 14 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| vector-borne disease mitigation | 290 | 24% | -20% |
| vector-borne disease epidemiology | 586 | 48% | -29% |
| global health challenges | 177 | 14% | +16% |
| travel-related infectious disease risks | 257 | 21% | +15% |
| zoonotic disease prevention measures | 255 | 21% | -22% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Measles surge accompanied by rising dengue prevalence](http://www.dhakatribune.com/bangladesh/health/408829/measles-surge-accompanied-by-rising-dengue) | dhakatribune.com | 9 | negative |
| 29 Apr 2026 | [Envu India Backs National Conclave Uniting India's Public Health Leaders To Advance Urban Vector-Borne…](https://www.outlookindia.com/xhub/featured-insights/envu-india-backs-national-conclave-uniting-indias-public-health-leaders-to-advance-urban-vector-borne-disease-control) | outlookindia.com | 8 | positive |
| 28 Apr 2026 | [Envu India supports national conclave uniting India's public health leadership to advance urban vector-borne…](https://www.expresshealthcare.in/news/envu-india-supports-national-conclave-uniting-indias-public-health-leadership-to-advance-urban-vector-borne-disease-control/453499/) | expresshealthcare.in | 8 | positive |
| 26 Apr 2026 | [28 dengue cases detected overnight](http://www.dhakatribune.com/bangladesh/health/408705/28-dengue-cases-detected-overnight) | dhakatribune.com | 8 | negative |
| 24 Apr 2026 | [Experts Call For Urgent Action To Bridge Dengue Treatment Gaps In India And South-East Asia](https://businessnewsthisweek.com/health/experts-call-for-urgent-action-to-bridge-dengue-treatment-gaps-in-india-and-south-east-asia/) | businessnewsthisweek.com | 8 | positive |
| 23 Apr 2026 | [Experts Urge Action on Dengue Treatment Gaps in India](https://www.newkerala.com/news/a/experts-meet-india-call-urgent-action-dengue-treatment-443.htm) | newkerala.com | 8 | negative |
| 23 Apr 2026 | [Experts convene in India to push for urgent action on dengue treatment gaps](https://www.indianpharmapost.com/public-health/experts-convene-in-india-to-push-for-urgent-action-on-dengue-treatment-gaps-19893) | indianpharmapost.com | 8 | positive |
| 22 Apr 2026 | [Dengue cases from January to March fall nearly 30% from previous quarter](https://www.asiaone.com/singapore/dengue-cases-january-march-fall-nearly-30-previous-quarter) | asiaone.com | 8 | negative |
| 21 Apr 2026 | [India braces for monsoon dengue surge with new mosquito trap, first vaccine cleared](https://khaleejtimes.com/world/asia/india-braces-for-monsoon-dengue-surge-with-new-mosquito-trap-first-vaccine-cleared) | khaleejtimes.com | 8 | negative |
| 19 Apr 2026 | [Vector-Borne Infections: Current Happenings 2026 formulated By Dr.T.V.Rao MD](https://www.linkedin.com/pulse/vector-borne-infections-current-happenings-2026-formulated-dr-t-v-rao-rb5xc) | linkedin.com | 8 | negative |
| 18 Apr 2026 | [40-bed dengue ward ready at Civil Hospital - The Tribune](https://www.tribuneindia.com/news/ludhiana/40-bed-dengue-ward-ready-at-civil-hospital/) | tribuneindia.com | 8 | negative |
| 18 Apr 2026 | [India approves its first dengue vaccine. How it could protect you against dengue - The Times of India](https://timesofindia.indiatimes.com/toi-plus/health/india-approves-its-first-dengue-vaccine-how-it-could-protect-you-against-dengue/articleshow/130347476.cms) | timesofindia.indiatimes.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "dengue" --since 2026-01-01 --until 2026-04-30
prism-news trends "dengue" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "dengue" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "dengue", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "dengue", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Depression News](depression-news.md)
- [Sepsis News](sepsis-news.md)
- [Candida Auris Outbreak](candida-auris-outbreak.md)
- [Lung Cancer News](lung-cancer-news.md)
