# Student Visa News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “student visa news” · 90/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [student-visa-news.json](../../examples/scenarios/student-visa-news.json).

**Question.** How did coverage of student visa develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="student visa"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 474 |
| Negative · neutral · positive | 76% · 1.7% · 22% |
| Critical (priority 7–9) | 77% (365 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (681 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | student visa eligibility and documentation |

## Twelve months of coverage

Monthly matching articles for `student visa` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 681 | 81% | 608 | 60 | ████████████████████ |
| Jun 2025 | 519 | 78% | 448 | 59 | ███████████████ |
| Jul 2025 | 393 | 54% | 317 | 72 | ████████████ |
| Aug 2025 | 336 | 74% | 238 | 85 | ██████████ |
| Sep 2025 | 175 | 77% | 142 | 30 | █████ |
| Oct 2025 | 119 | 82% | 98 | 19 | ███ |
| Nov 2025 | 152 | 78% | 102 | 48 | ████ |
| Dec 2025 | 116 | 85% | 86 | 29 | ███ |
| Jan 2026 | 115 | 76% | 88 | 27 | ███ |
| Feb 2026 | 131 | 82% | 106 | 23 | ████ |
| Mar 2026 | 109 | 80% | 87 | 19 | ███ |
| Apr 2026 | 119 | 71% | 79 | 37 | ███ |

The last four complete months averaged 118 articles a month against 482 in the first four (-75%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 58% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 139 | 29% |
| India | 28 | 5.9% |
| United Kingdom | 28 | 5.9% |
| Australia | 19 | 4.0% |
| Canada | 10 | 2.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| student visa eligibility and documentation | 101 | 29% | -36% |
| visa extension and adjustment of status | 62 | 18% | -24% |
| visa overstay consequences and penalties | 39 | 11% | +70% |
| non-immigrant visa classifications (e.g., b-1, f-1) | 73 | 21% | -26% |
| work visa categories (e.g., h-1b, l-1, tier 2) | 30 | 8.7% | -41% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 3 Apr 2026 | [Australia Tightens Student Visa Norms for India; Check Revised Guidelines](https://www.timesnownews.com/education/australia-tightens-student-visa-norms-for-india-check-revised-guidelines-article-153989523) | timesnownews.com | 8 | negative |
| 23 Mar 2026 | [Immigration department not keeping up with demand for student visa probes: auditor](https://www.winnipegfreepress.com/canada/2026/03/23/newsalert-international-student-program-needs-to-boost-integrity-auditor) | winnipegfreepress.com | 8 | negative |
| 17 Mar 2026 | [Over a year later, pro-Palestinian protester is released from ICE custody](https://www.yahoo.com/news/articles/over-later-pro-palestinian-protester-002605997.html) | yahoo.com | 8 | negative |
| 10 Mar 2026 | [New Student Visas Dropped 35.6% Last Summer](http://www.insidehighered.com/news/global/international-students-us/2026/03/10/new-student-visas-dropped-356-last-summer) | insidehighered.com | 8 | negative |
| 7 Mar 2026 | [Tighter scrutiny, same fundamentals: Why India will remain central to global education - The Economic Times](https://economictimes.indiatimes.com/nri/study/tighter-scrutiny-same-fundamentals-why-india-will-remain-central-to-global-education/articleshow/129199689.cms) | economictimes.indiatimes.com | 8 | negative |
| 5 Mar 2026 | [UK Embassy in Yangon announces student visa applications will no longer be accepted from March 26](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/03/05/uk-embassy-in-yangon-announces-student-visa-applications-will-no-longer-be-accepted-from-march-26) | thestar.com.my | 8 | negative |
| 5 Mar 2026 | [Shabana Mahmood has undermined the last immigration myth](https://www.yahoo.com/news/articles/shabana-mahmood-undermined-last-immigration-093000609.html) | yahoo.com | 8 | negative |
| 4 Mar 2026 | [Student visa restrictions for four countries](https://wonkhe.com/wonk-corner/student-visa-restrictions-for-four-countries/) | wonkhe.com | 8 | negative |
| 19 Feb 2026 | [Feds: Former MN corrections officer was in U.S. illegally, a ‘serial fraudster’](https://www.yahoo.com/news/articles/feds-former-mn-corrections-officer-014400437.html) | yahoo.com | 8 | negative |
| 13 Feb 2026 | [Students miss January intakes amid visa delays ahead of new rules](https://www.timeshighereducation.com/news/students-miss-january-intakes-amid-visa-delays-ahead-new-rules) | timeshighereducation.com | 8 | negative |
| 7 Feb 2026 | [Trump administration won't let student deported to Honduras return](https://www.straitstimes.com/world/trump-administration-wont-let-student-deported-to-honduras-return) | straitstimes.com | 8 | negative |
| 5 Feb 2026 | [Pradhan meets delegation of 24 Canadian universities to boost India-Canada higher education ties](https://indianexpress.com/article/education/pradhan-meets-delegation-of-24-canadian-universities-to-boost-india-canada-higher-education-ties-10514893/) | indianexpress.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "student visa" --since 2026-01-01 --until 2026-04-30
prism-news trends "student visa" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "student visa" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "student visa", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "student visa", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Stablecoin Regulation News](stablecoin-regulation-news.md)
- [Education Policy News](education-policy-news.md)
- [WTO News](wto-news.md)
- [Labour Law News](labour-law-news.md)
