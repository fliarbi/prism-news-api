# Education Policy News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “education policy news” · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [education-policy-news.json](../../examples/scenarios/education-policy-news.json).

**Question.** How did coverage of education policy develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="education policy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,885 |
| Negative · neutral · positive | 40% · 2.1% · 58% |
| Critical (priority 7–9) | 71% (1,331 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (656 articles) |
| Most-reported country | India (20% of matches) |
| Strongest theme by lift | elementary school curriculum development |

## Twelve months of coverage

Monthly matching articles for `education policy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 410 | 66% | 163 | 229 | ████████████ |
| Jun 2025 | 404 | 69% | 149 | 247 | ████████████ |
| Jul 2025 | 605 | 59% | 221 | 369 | ██████████████████ |
| Aug 2025 | 605 | 67% | 256 | 336 | ██████████████████ |
| Sep 2025 | 434 | 71% | 165 | 262 | █████████████ |
| Oct 2025 | 386 | 80% | 191 | 182 | ████████████ |
| Nov 2025 | 311 | 73% | 103 | 206 | █████████ |
| Dec 2025 | 360 | 70% | 132 | 221 | ███████████ |
| Jan 2026 | 353 | 69% | 120 | 223 | ███████████ |
| Feb 2026 | 430 | 70% | 167 | 254 | █████████████ |
| Mar 2026 | 446 | 67% | 168 | 269 | ██████████████ |
| Apr 2026 | 656 | 75% | 290 | 354 | ████████████████████ |

The last four complete months averaged 471 articles a month against 506 in the first four (-7%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 377 | 20% |
| United States | 330 | 18% |
| United Kingdom | 44 | 2.3% |
| Nigeria | 24 | 1.3% |
| Ghana | 18 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| elementary school curriculum development | 59 | 4.8% | +195% |
| bilingual and esl education strategies | 75 | 6.1% | +97% |
| education law and policy compliance | 85 | 7.0% | +286% |
| university rankings and reputation metrics | 36 | 3.0% | +50% |
| history and social studies curriculum development | 84 | 6.9% | +147% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [How Manipur University Stands Out in NEP 2020: 80 Percent ABC and 70 Percent FYUP Adoption](https://www.indiatodayne.in/opinion/story/how-manipur-university-stands-out-in-nep-2020-80-percent-abc-and-70-percent-fyup-adoption-1382545-2026-04-28) | indiatodayne.in | 8 | positive |
| 24 Apr 2026 | [NEWS: Shortage of Educational Psychologists Risks Undermining SEND Reforms \| Edexec](https://edexec.co.uk/news-shortage-of-educational-psychologists-risks-undermining-send-reforms/) | edexec.co.uk | 8 | negative |
| 18 Apr 2026 | [Class I admission age 6 years, says CBSE](https://www.newindianexpress.com/states/kerala/2026/Apr/18/class-i-admission-age-6-years-says-cbse-3) | newindianexpress.com | 8 | negative |
| 16 Apr 2026 | [Socioeconomic status a key factor in understanding Alaska test data, lawmakers hear](https://www.yahoo.com/news/articles/socioeconomic-status-key-factor-understanding-235623622.html) | yahoo.com | 8 | negative |
| 16 Apr 2026 | [Schools across UK short of 1,400 of educational psychologists, experts warn](https://www.yahoo.com/news/articles/schools-across-uk-short-1-173635615.html) | yahoo.com | 8 | negative |
| 16 Apr 2026 | [RTE hurt school learning outcomes, affecting both reading & math proficiency—NITI Aayog working paper](https://theprint.in/india/education/rte-hurt-school-learning-outcomes-affecting-both-reading-math-proficiency-niti-aayog-working-paper/2905898/) | theprint.in | 8 | negative |
| 6 Apr 2026 | [“NEP 2020 is a Manifesto for Linguistic Liberation, Not Imposition”: Union Education Minister - PNI](https://www.pninews.com/nep-2020-is-a-manifesto-for-linguistic-liberation-not-imposition-union-education-minister/) | pninews.com | 8 | negative |
| 5 Apr 2026 | [1k contract basis teachers deployed in schools for NEP implementation \| Goa News - The Times of India](https://timesofindia.indiatimes.com/city/goa/1k-contract-basis-teachers-deployed-in-schools-for-nep-implementation/articleshow/130045718.cms) | timesofindia.indiatimes.com | 8 | positive |
| 4 Apr 2026 | [2026 TN elections \| Stalin slams CBSE’s ‘covert’ push to impose Hindi in south states](https://www.dtnext.in/news/politics/2026-tn-elections-stalin-slams-cbses-covert-push-to-impose-hindi-in-south-states) | dtnext.in | 8 | negative |
| 1 Apr 2026 | [Early Memphis schools audit findings ‘consistent with waste or abuse’](https://www.yahoo.com/news/articles/early-memphis-schools-audit-findings-183815139.html) | yahoo.com | 8 | negative |
| 19 Mar 2026 | [Increase education spending to 6% of GDP: Parliamentary panel to Cent](https://www.hindustantimes.com/india-news/increase-education-spending-to-6-of-gdp-parliamentary-panel-to-cent-101773862077046.html) | hindustantimes.com | 8 | positive |
| 16 Mar 2026 | [The Evolution of the U.S. Department of Education Under Trump: A Closer Look](https://www.theedadvocate.org/the-evolution-of-the-u-s-department-of-education-under-trump-a-closer-look/) | theedadvocate.org | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "education policy" --since 2026-01-01 --until 2026-04-30
prism-news trends "education policy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "education policy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "education policy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "education policy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Uniform Civil Code News](uniform-civil-code-news.md)
- [Stablecoin Regulation News](stablecoin-regulation-news.md)
- [Student Visa News](student-visa-news.md)
- [WTO News](wto-news.md)
