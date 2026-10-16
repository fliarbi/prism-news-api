# Rent Control News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rent control news” · 10/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rent-control-news.json](../../examples/scenarios/rent-control-news.json).

**Question.** How did coverage of rent control develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="rent control"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 170 |
| Negative · neutral · positive | 83% · 1.8% · 15% |
| Critical (priority 7–9) | 76% (129 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (66 articles) |
| Most-reported country | United States (32% of matches) |
| Strongest theme by lift | regulatory compliance and legal business issues |

## Twelve months of coverage

Monthly matching articles for `rent control` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 31 | 74% | 26 | 5 | █████████ |
| Jun 2025 | 31 | 84% | 23 | 8 | █████████ |
| Jul 2025 | 37 | 60% | 32 | 4 | ███████████ |
| Aug 2025 | 63 | 73% | 55 | 8 | ███████████████████ |
| Sep 2025 | 51 | 76% | 36 | 14 | ███████████████ |
| Oct 2025 | 49 | 80% | 40 | 9 | ███████████████ |
| Nov 2025 | 65 | 63% | 50 | 11 | ████████████████████ |
| Dec 2025 | 50 | 84% | 40 | 7 | ███████████████ |
| Jan 2026 | 32 | 72% | 23 | 9 | ██████████ |
| Feb 2026 | 38 | 82% | 28 | 8 | ████████████ |
| Mar 2026 | 34 | 85% | 30 | 4 | ██████████ |
| Apr 2026 | 66 | 70% | 60 | 5 | ████████████████████ |

The last four complete months averaged 42 articles a month against 40 in the first four (+5%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 58% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 55 | 32% |
| United Kingdom | 23 | 14% |
| Canada | 5 | 2.9% |
| India | 4 | 2.4% |
| Ghana | 2 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| regulatory compliance and legal business issues | 10 | 9.1% | +67% |
| rent control and stabilization regulations | 9 | 8.2% | -73% |
| landlord-tenant eviction proceedings | 8 | 7.3% | -60% |
| rent control policies | 6 | 5.5% | -50% |
| tenant rights advocacy | 6 | 5.5% | -33% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [Tenants under pressure, JFR report favours rent control](https://www.landlordzone.co.uk/news/tenants-under-pressure-jfr-report-favours-rent-control) | landlordzone.co.uk | 8 | negative |
| 22 Apr 2026 | [Rent Control, the idea that never dies.](https://www.landlordzone.co.uk/news/rent-control-the-idea-that-never-dies) | landlordzone.co.uk | 7 | negative |
| 14 Apr 2026 | [Put Rent Control on the Ballot](https://www.independent.com/2026/04/14/put-rent-control-on-the-ballot/) | independent.com | 7 | negative |
| 14 Apr 2026 | [Randy Rowse: Put Rent Control on the Ballot Before It Reshapes Santa Barbara](https://www.noozhawk.com/randy-rowse-put-rent-control-on-the-ballot-before-it-reshapes-santa-barbara/) | noozhawk.com | 7 | negative |
| 6 Apr 2026 | [AIM: Rent Control Will Stifle Needed Housing Development](https://aimnet.org/aim-rent-control-will-stifle-needed-housing-development/) | aimnet.org | 7 | negative |
| 23 Mar 2026 | [Real estate-backed study warns that rent control could tank Massachusetts property values - The Boston Globe](http://www.bostonglobe.com/2026/03/12/business/rent-control-property-values-massachusetts/) | bostonglobe.com | 7 | negative |
| 12 Mar 2026 | [Manitoba government proposes new grocery rules, rent control, some hydro hikes](https://canadiangrocer.com/manitoba-government-proposes-new-grocery-rules-rent-control-some-hydro-hikes) | canadiangrocer.com | 7 | negative |
| 12 Mar 2026 | [STUDY: Rent Control Could Cost Massachusetts $300B In Lost Property Values](https://www.bisnow.com/boston/news/multifamily/rent-control-could-cost-massachusetts-300b-property-values-study-133627) | bisnow.com | 7 | negative |
| 11 Mar 2026 | [I didn’t know their struggles; I apologise to Rent Control staff for name-calling – Acting Commissioner -…](https://www.adomonline.com/i-didnt-know-their-struggles-i-apologise-to-rent-control-staff-for-name-calling-acting-commissioner/) | adomonline.com | 7 | negative |
| 21 Feb 2026 | [Fewer than half of Providence apartments would be rent-controlled under current proposal, city estimates -…](https://www.bostonglobe.com/2026/02/20/metro/rent-control-providence-city-council-stabilization/) | bostonglobe.com | 7 | negative |
| 11 Feb 2026 | [Boston Mayor Wu says she would support rent control ballot question](https://www.yahoo.com/news/articles/boston-mayor-wu-says-she-161126291.html) | yahoo.com | 7 | negative |
| 6 Feb 2026 | [**California Rent Control Bill Stalls in Committee** A bill proposed in the California Assembly to expand…](https://cremarketbeat.com/california-rent-control-legislation-fails-to-advance-in-committee/) | cremarketbeat.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "rent control" --since 2026-01-01 --until 2026-04-30
prism-news trends "rent control" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "rent control" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "rent control", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "rent control", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Chips Act News](chips-act-news.md)
- [Content Moderation News](content-moderation-news.md)
- [Digital Markets Act News](digital-markets-act-news.md)
- [Railway Budget News](railway-budget-news.md)
