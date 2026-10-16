# Defence Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “defence industry news” · 590/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [defence-industry-news.json](../../examples/scenarios/defence-industry-news.json).

**Question.** How much news did the defence industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="defence industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,131 |
| Negative · neutral · positive | 17% · 3.1% · 80% |
| Critical (priority 7–9) | 74% (1,572 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (714 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | national defense policy impacts on aerospace |

## Twelve months of coverage

Monthly matching articles for `defence industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 206 | 66% | 31 | 171 | ██████ |
| Jun 2025 | 188 | 69% | 45 | 136 | █████ |
| Jul 2025 | 241 | 66% | 39 | 190 | ███████ |
| Aug 2025 | 236 | 78% | 42 | 187 | ███████ |
| Sep 2025 | 355 | 74% | 53 | 293 | ██████████ |
| Oct 2025 | 373 | 77% | 32 | 333 | ██████████ |
| Nov 2025 | 327 | 79% | 47 | 274 | █████████ |
| Dec 2025 | 342 | 76% | 42 | 292 | ██████████ |
| Jan 2026 | 346 | 73% | 50 | 286 | ██████████ |
| Feb 2026 | 548 | 76% | 119 | 414 | ███████████████ |
| Mar 2026 | 523 | 73% | 81 | 429 | ███████████████ |
| Apr 2026 | 714 | 73% | 108 | 574 | ████████████████████ |

The last four complete months averaged 533 articles a month against 218 in the first four (+145%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 449 | 21% |
| United Kingdom | 104 | 4.9% |
| Germany | 93 | 4.4% |
| Australia | 86 | 4.0% |
| Canada | 68 | 3.2% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| national defense policy impacts on aerospace | 171 | 13% | +68% |
| defense systems integration techniques | 94 | 7.1% | +54% |
| international aerospace export compliance standards | 144 | 11% | +76% |
| defense contract bidding procedures | 171 | 13% | +32% |
| electronic warfare systems in modern defense | 72 | 5.4% | +47% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Europe’s rearmament needs Ukrainian innovation and European scale - Friends of Europe](https://www.friendsofeurope.org/insights/critical-thinking-europes-rearmament-needs-ukrainian-innovation-and-european-scale/) | friendsofeurope.org | 8 | positive |
| 21 Apr 2026 | [Pentagon details $1.5 trillion FY2027 budget request](https://defence-industry.eu/pentagon-details-1-5-trillion-fy2027-budget-request/) | defence-industry.eu | 8 | positive |
| 15 Apr 2026 | [UK announces record drone package for Ukraine](https://defence-industry.eu/uk-announces-record-drone-package-for-ukraine/) | defence-industry.eu | 8 | positive |
| 14 Apr 2026 | [Chinese media question U.S. Air Force F-47 fighter program](https://defence-industry.eu/chinese-media-question-u-s-air-force-f-47-fighter-program/) | defence-industry.eu | 8 | negative |
| 6 Apr 2026 | [Israel to accelerate Arrow interceptor production](https://defence-industry.eu/israel-ministry-of-defense-approves-acceleration-of-arrow-interceptor-production-to-strengthen-missile-defense-capabilities/) | defence-industry.eu | 8 | positive |
| 31 Mar 2026 | [Chairman of the Joint Chiefs of Staff highlights role of defense industrial workforce in U.S. military…](https://defence-industry.eu/chairman-of-the-joint-chiefs-of-staff-highlights-role-of-defense-industrial-workforce-in-u-s-military-operations/) | defence-industry.eu | 8 | positive |
| 30 Mar 2026 | [EU approves defence programme to develop European and Ukrainian industries](https://www.yahoo.com/news/articles/eu-approves-defence-programme-develop-105400695.html) | yahoo.com | 8 | positive |
| 29 Mar 2026 | [UK receives 48th Lockheed Martin F-35B Lightning II fighter](https://defence-industry.eu/uk-receives-48th-lockheed-martin-f-35b-lightning-ii-fighter/) | defence-industry.eu | 8 | negative |
| 17 Mar 2026 | [Khorramshahr missile illustrates Iran’s progress in long-range ballistic missile development](https://defence-industry.eu/khorramshahr-missile-illustrates-irans-progress-in-long-range-ballistic-missile-development/) | defence-industry.eu | 8 | negative |
| 12 Mar 2026 | [Prime Minister calls for greater self-reliance in developing defence industry](https://en.nhandan.vn/prime-minister-calls-for-greater-self-reliance-in-developing-defence-industry-post159913.html) | en.nhandan.vn | 8 | positive |
| 27 Feb 2026 | [IFS 2025 Batch Calls on Rajnath Singh; Raksha Mantri Highlights Push for Indigenous Defence & Diplomacy -…](https://indiaseatradenews.com/ifs-2025-batch-calls-on-rajnath-singh-raksha-mantri-highlights-push-for-indigenous-defence-diplomacy/) | indiaseatradenews.com | 8 | positive |
| 26 Feb 2026 | [Ukrspecsystems opens £200 million Suffolk drone factory to support Ukraine and create 500 UK jobs](https://defence-industry.eu/ukrspecsystems-opens-200-million-suffolk-drone-factory-to-support-ukraine-and-create-500-uk-jobs/) | defence-industry.eu | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "defence industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "defence industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "defence industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "defence industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "defence industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through 24 Aug 2026; intake thins after May 2026.
- `q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- zero-count periods are included; partial_period marks buckets the window only partly covers
- Country shares use all matching articles. Location information is incomplete and varies by period.
- Theme shares use articles with identified themes; articles may have more than one theme.

## Related demonstrations

- [Sports Industry](sports-industry.md)
- [Insurance Industry](insurance-industry.md)
- [Dairy Industry](dairy-industry.md)
- [Beverage Industry](beverage-industry.md)
