# Cocoa Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cocoa industry” · 260/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cocoa-industry.json](../../examples/scenarios/cocoa-industry.json).

**Question.** How much news did the cocoa industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="cocoa industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 63 |
| Negative · neutral · positive | 25% · 3.2% · 71% |
| Critical (priority 7–9) | 76% (48 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (39 articles) |
| Most-reported country | Ghana (35% of matches) |
| Strongest theme by lift | agricultural export and international trade |

## Twelve months of coverage

Monthly matching articles for `cocoa industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 89% | 2 | 7 | █████ |
| Jun 2025 | 13 | 85% | 1 | 12 | ███████ |
| Jul 2025 | 16 | 62% | 5 | 11 | ████████ |
| Aug 2025 | 19 | 90% | 7 | 12 | ██████████ |
| Sep 2025 | 12 | 67% | 2 | 10 | ██████ |
| Oct 2025 | 26 | 92% | 4 | 22 | █████████████ |
| Nov 2025 | 13 | 85% | 2 | 11 | ███████ |
| Dec 2025 | 3 | 33% | 1 | 2 | ██ |
| Jan 2026 | 6 | 100% | 1 | 5 | ███ |
| Feb 2026 | 39 | 82% | 15 | 24 | ████████████████████ |
| Mar 2026 | 9 | 56% | 0 | 8 | █████ |
| Apr 2026 | 9 | 56% | 0 | 8 | █████ |

The last four complete months averaged 16 articles a month against 14 in the first four (+11%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 71% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| Ghana | 22 | 35% |
| United States | 10 | 16% |
| Ivory Coast | 7 | 11% |
| Ireland | 1 | 1.6% |
| Japan | 1 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agricultural export and international trade | 6 | 20% | +50% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 2 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Mar 2026 | [Côte d’Ivoire-AIP/ Le Conseil du café-cacao met en garde les acteurs de la filière de Sassandra contre les…](https://www.aip.ci/340544/cote-divoire-aip-le-conseil-du-cafe-cacao-met-en-garde-les-acteurs-de-la-filiere-de-sassandra-contre-les-pratiques-illicites/) | aip.ci | 6 | neutral |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cocoa industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "cocoa industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cocoa industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cocoa industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cocoa industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Electronics Industry](electronics-industry.md)
- [Wine Industry](wine-industry.md)
- [Glass Industry](glass-industry.md)
- [Medical Device Industry News](medical-device-industry-news.md)
