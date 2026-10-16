# Cholera Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cholera outbreak” · 320/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cholera-outbreak.json](../../examples/scenarios/cholera-outbreak.json).

**Question.** How much cholera coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="cholera"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 355 |
| Negative · neutral · positive | 60% · 2.0% · 38% |
| Critical (priority 7–9) | 85% (303 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (243 articles) |
| Most-reported country | United States (10% of matches) |
| Strongest theme by lift | community health initiatives |

## Twelve months of coverage

Monthly matching articles for `cholera` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 151 | 82% | 108 | 39 | ████████████ |
| Jun 2025 | 112 | 82% | 86 | 26 | █████████ |
| Jul 2025 | 150 | 73% | 110 | 32 | ████████████ |
| Aug 2025 | 243 | 90% | 200 | 40 | ████████████████████ |
| Sep 2025 | 154 | 92% | 101 | 50 | █████████████ |
| Oct 2025 | 106 | 87% | 57 | 47 | █████████ |
| Nov 2025 | 141 | 94% | 77 | 61 | ████████████ |
| Dec 2025 | 77 | 87% | 49 | 23 | ██████ |
| Jan 2026 | 94 | 93% | 45 | 44 | ████████ |
| Feb 2026 | 76 | 87% | 50 | 24 | ██████ |
| Mar 2026 | 55 | 82% | 36 | 17 | █████ |
| Apr 2026 | 130 | 81% | 80 | 46 | ███████████ |

The last four complete months averaged 89 articles a month against 164 in the first four (-46%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 36 | 10% |
| India | 23 | 6.5% |
| Nigeria | 17 | 4.8% |
| Kenya | 9 | 2.5% |
| Mozambique | 7 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| community health initiatives | 37 | 16% | -36% |
| infectious disease control strategies | 16 | 7.0% | -20% |
| environmental health risk assessments | 24 | 10% | +33% |
| epidemiological surveillance systems | 15 | 6.5% | -17% |
| sanitation and hygiene initiatives | 29 | 13% | -40% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 2 Feb 2026 | [Cholera kills 12 in Mozambique within 24 hours, as cases spike in Malawi - Adomonline.com](https://www.adomonline.com/cholera-kills-12-in-mozambique-within-24-hours-as-cases-spike-in-malawi/) | adomonline.com | 9 | negative |
| 15 Jan 2026 | [Epidemiologic Characteristics and Predictors of Mortality in Somalia's 2024 Cholera Outbreak.](https://pubmed.ncbi.nlm.nih.gov/41538089/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 17 Apr 2026 | [Water access expanded amid rising cholera risk - Daily News](https://dailynews.co.tz/water-access-expanded-amid-rising-cholera-risk/) | dailynews.co.tz | 8 | negative |
| 15 Apr 2026 | [NCDC Alerts 10 States On Flood-Linked Cholera, Disease Outbreak Risks](https://sciencenigeria.com/ncdc-alerts-10-states-on-flood-linked-cholera-disease-outbreak-risks/) | sciencenigeria.com | 8 | negative |
| 12 Apr 2026 | [The numbers (of infected) will explode." That's Elizabeth Byrs from the United Nations talking about the…](https://www.bbc.co.uk/blogs/worldhaveyoursay/2010/11/on_air_your_questions_on_haiti.html) | bbc.co.uk | 8 | negative |
| 8 Apr 2026 | [Cholera can quickly become life-threatening, but the best defense might be sitting in your pantry. New…](https://www.foxnews.com/health/deadly-bacterial-disease-could-stopped-common-pantry-staple-study-suggests.print) | foxnews.com | 8 | positive |
| 27 Mar 2026 | [Cholera aid for African countries stalled by Iran conflict](https://www.yahoo.com/news/articles/cholera-aid-african-countries-stalled-114909191.html) | yahoo.com | 8 | negative |
| 2 Mar 2026 | [Co-administration of oral killed whole-cell recombinant cholera toxin B-subunit vaccine (WC-rCTB) and live…](https://pubmed.ncbi.nlm.nih.gov/41641963/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 20 Feb 2026 | [Japan boosts Lagos' cholera response with $1.7 million medical supplies](https://www.premiumtimesng.com/health/health-news/858291-japan-boosts-lagos-cholera-response-with-1-7-million-medical-supplies.html) | premiumtimesng.com | 8 | negative |
| 12 Feb 2026 | [Man dies from rare cholera-like disease in the UK](https://metro.co.uk/2026/02/12/man-dies-rare-cholera-like-disease-uk-26851205/) | metro.co.uk | 8 | negative |
| 11 Feb 2026 | [Cholera Death UK: 125 Years After Epidemic \| News - TIme News](https://time.news/cholera-death-uk-125-years-after-epidemic-news/) | time.news | 8 | negative |
| 10 Feb 2026 | [15 cholera cases in 3 days in Jamnagar, pipeline leakage suspected](https://www.hindustantimes.com/india-news/15-cholera-cases-in-3-days-in-jamnagar-pipeline-leakage-suspected-101770731793641.html) | hindustantimes.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cholera" --since 2026-01-01 --until 2026-04-30
prism-news trends "cholera" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cholera" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cholera", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cholera", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Norovirus Outbreak](norovirus-outbreak.md)
- [Tuberculosis Outbreak](tuberculosis-outbreak.md)
- [Vaccine News](vaccine-news.md)
- [Ozempic News](ozempic-news.md)
