# Pipeline News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pipeline news” · 50/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [pipeline-news.json](../../examples/scenarios/pipeline-news.json).

**Question.** How did pipeline coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="pipeline"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 17,933 |
| Negative · neutral · positive | 34% · 2.1% · 64% |
| Critical (priority 7–9) | 69% (12,314 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (5,720 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | pipeline infrastructure development |

## Twelve months of coverage

Monthly matching articles for `pipeline` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,148 | 68% | 686 | 1,412 | ████████ |
| Jun 2025 | 1,878 | 61% | 522 | 1,326 | ███████ |
| Jul 2025 | 2,747 | 68% | 951 | 1,745 | ██████████ |
| Aug 2025 | 3,155 | 66% | 1,202 | 1,889 | ███████████ |
| Sep 2025 | 3,185 | 72% | 911 | 2,206 | ███████████ |
| Oct 2025 | 2,412 | 69% | 620 | 1,751 | ████████ |
| Nov 2025 | 2,742 | 72% | 841 | 1,869 | ██████████ |
| Dec 2025 | 2,708 | 73% | 861 | 1,790 | █████████ |
| Jan 2026 | 3,051 | 69% | 810 | 2,182 | ███████████ |
| Feb 2026 | 4,414 | 66% | 1,215 | 3,091 | ███████████████ |
| Mar 2026 | 4,748 | 70% | 1,791 | 2,849 | █████████████████ |
| Apr 2026 | 5,720 | 69% | 2,300 | 3,307 | ████████████████████ |

The last four complete months averaged 4,483 articles a month against 2,482 in the first four (+81%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 45% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 3,366 | 19% |
| India | 905 | 5.0% |
| United Kingdom | 458 | 2.5% |
| Canada | 344 | 1.9% |
| Nigeria | 291 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| pipeline infrastructure development | 2,735 | 23% | +100% |
| pipeline corrosion prevention methods | 1,184 | 10% | +90% |
| oil and gas supply chain management | 531 | 4.5% | +264% |
| gas flaring reduction techniques | 774 | 6.6% | +100% |
| oncology and targeted therapy advancements | 454 | 3.9% | +78% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 19 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 6 Apr 2026 | [Ucrania lanza ataque contra oleoducto ruso en el Báltico](https://www.eleconomista.com.mx/internacionales/ucrania-lanza-ataque-oleoducto-ruso-baltico-20260405-807349.html) | eleconomista.com.mx | 9 | negative |
| 31 Mar 2026 | [Balochistan Burns Again: Viral Video Shows 18-Inch Gas Pipeline Blown Up In Quetta, Supply Disrupted](https://www.freepressjournal.in/world/balochistan-burns-again-viral-video-shows-18-inch-gas-pipeline-blown-up-in-quetta-supply-disrupted) | freepressjournal.in | 9 | negative |
| 24 Mar 2026 | [Iran media says energy infrastructure attacked after Trump postpones strike](https://khaleejtimes.com/world/iran-media-says-energy-infrastructure-attacked-after-trump-postpones-strike) | khaleejtimes.com | 9 | negative |
| 11 Mar 2026 | [Nairobi’s flood survivors recount trauma as mental health crisis deepens](https://www.nation.africa/kenya/health/nairobi-s-flood-survivors-recount-trauma-as-mental-health-crisis-deepens-5387342) | nation.africa | 9 | negative |
| 23 Apr 2026 | [EU approves a $106B loan package to help Ukraine after Hungary lifts its veto](https://www.pbs.org/newshour/world/eu-approves-a-106b-loan-package-to-help-ukraine-after-hungary-lifts-its-veto) | pbs.org | 8 | negative |
| 23 Apr 2026 | [EU approves a $106 billion loan package to help Ukraine after Hungary lifts its veto](https://www.orlandosentinel.com/2026/04/23/eu-approves-ukraine-loan-package/) | orlandosentinel.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "pipeline" --since 2026-01-01 --until 2026-04-30
prism-news trends "pipeline" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "pipeline" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "pipeline", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "pipeline", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Nickel News](nickel-news.md)
- [Air Quality News](air-quality-news.md)
- [Heat Pumps News](heat-pumps-news.md)
- [Wind Turbines Industry](wind-turbines-industry.md)
