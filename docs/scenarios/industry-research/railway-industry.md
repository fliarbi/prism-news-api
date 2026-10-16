# Railway Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “railway industry” · 260/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [railway-industry.json](../../examples/scenarios/railway-industry.json).

**Question.** How much news did the railway industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="railway industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 291 |
| Negative · neutral · positive | 23% · 3.4% · 74% |
| Critical (priority 7–9) | 44% (129 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (85 articles) |
| Most-reported country | India (7.2% of matches) |
| Strongest theme by lift | rail freight technology innovations (e.g., iot, gps) |

## Twelve months of coverage

Monthly matching articles for `railway industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 53 | 53% | 11 | 40 | ████████████ |
| Jun 2025 | 66 | 50% | 10 | 56 | ████████████████ |
| Jul 2025 | 80 | 48% | 29 | 50 | ███████████████████ |
| Aug 2025 | 73 | 67% | 34 | 38 | █████████████████ |
| Sep 2025 | 49 | 41% | 6 | 40 | ████████████ |
| Oct 2025 | 58 | 64% | 11 | 44 | ██████████████ |
| Nov 2025 | 68 | 41% | 15 | 51 | ████████████████ |
| Dec 2025 | 52 | 58% | 17 | 31 | ████████████ |
| Jan 2026 | 54 | 52% | 15 | 36 | █████████████ |
| Feb 2026 | 73 | 51% | 22 | 49 | █████████████████ |
| Mar 2026 | 79 | 37% | 15 | 59 | ███████████████████ |
| Apr 2026 | 85 | 41% | 15 | 70 | ████████████████████ |

The last four complete months averaged 73 articles a month against 68 in the first four (+7%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 27% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 21 | 7.2% |
| United States | 19 | 6.5% |
| United Kingdom | 15 | 5.2% |
| Germany | 5 | 1.7% |
| Canada | 3 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| rail freight technology innovations (e.g., iot, gps) | 37 | 22% | +37% |
| rail freight environmental impact reduction | 22 | 13% | +267% |
| rail freight labor and workforce management | 21 | 12% | +320% |
| high-speed train operations and amenities | 20 | 12% | +82% |
| historical evolution of rail networks | 11 | 6.5% | +267% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 1 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 3 Apr 2026 | [Alstom takes over Cummins' fuel cell division for trains](https://www.hydronews.it/en/alstom-takes-over-cummins-fuel-cell-division-for-trains/) | hydronews.it | 7 | positive |
| 13 Mar 2026 | [Mirroring reality: how digital twining impacts the rail industry](https://www.globalrailwayreview.com/article/235179/mirroring-reality-how-digital-twining-impacts-the-rail-industry/) | globalrailwayreview.com | 7 | positive |
| 20 Feb 2026 | [Ministry proposes restructuring Vietnam Railways Corp into national railway group to spearhead North–South…](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/02/20/ministry-proposes-restructuring-vietnam-railways-corp-into-national-railway-group-to-spearhead-north-south-mega-project) | thestar.com.my | 7 | positive |
| 6 Feb 2026 | [Union Pacific moderniza locomotivas - ITJ \| International Transport Journal](https://transportjournal.com/pt-pt/2026/02/06/union-pacific-moderniza-locomotivas/) | transportjournal.com | 7 | positive |
| 6 Feb 2026 | [Union Pacific moderniza locomotoras - ITJ \| International Transport Journal](https://transportjournal.com/es/2026/02/06/union-pacific-moderniza-locomotoras/) | transportjournal.com | 7 | positive |
| 6 Feb 2026 | [Union Pacific modernise des locomotives - ITJ \| International Transport Journal](https://transportjournal.com/fr/2026/02/06/union-pacific-modernise-des-locomotives/) | transportjournal.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "railway industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "railway industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "railway industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "railway industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "railway industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Glass Industry](glass-industry.md)
- [Medical Device Industry News](medical-device-industry-news.md)
