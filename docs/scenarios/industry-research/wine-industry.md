# Wine Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wine industry” · 90/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wine-industry.json](../../examples/scenarios/wine-industry.json).

**Question.** How much news did the wine industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="wine industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,551 |
| Negative · neutral · positive | 23% · 1.9% · 75% |
| Critical (priority 7–9) | 25% (385 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (461 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | champagne region vineyards |

## Twelve months of coverage

Monthly matching articles for `wine industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 330 | 18% | 37 | 288 | ██████████████ |
| Jun 2025 | 245 | 22% | 35 | 207 | ███████████ |
| Jul 2025 | 293 | 26% | 63 | 227 | █████████████ |
| Aug 2025 | 348 | 23% | 77 | 266 | ███████████████ |
| Sep 2025 | 416 | 38% | 132 | 280 | ██████████████████ |
| Oct 2025 | 282 | 21% | 42 | 239 | ████████████ |
| Nov 2025 | 358 | 23% | 59 | 296 | ████████████████ |
| Dec 2025 | 282 | 29% | 48 | 229 | ████████████ |
| Jan 2026 | 279 | 24% | 61 | 204 | ████████████ |
| Feb 2026 | 402 | 23% | 106 | 289 | █████████████████ |
| Mar 2026 | 409 | 30% | 101 | 302 | ██████████████████ |
| Apr 2026 | 461 | 23% | 87 | 370 | ████████████████████ |

The last four complete months averaged 388 articles a month against 304 in the first four (+28%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 406 | 26% |
| Australia | 58 | 3.7% |
| United Kingdom | 48 | 3.1% |
| France | 42 | 2.7% |
| New Zealand | 41 | 2.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| champagne region vineyards | 519 | 45% | +27% |
| grape varietals in winemaking | 777 | 68% | +10% |
| international wine awards | 773 | 68% | +17% |
| vintage wine collecting | 562 | 49% | +26% |
| wine fermentation processes | 659 | 58% | +10% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 18 Mar 2026 | [Warning for wine: Climate change is coming for the elixir of life](https://www.indiatoday.in/science/story/climate-change-is-hitting-wine-rose-chauvgnon-elixir-of-life-warming-planet-vineyards-sula-wine-india-vineyards-2883211-2026-03-18) | indiatoday.in | 8 | positive |
| 17 Feb 2026 | [The wine industry headache](https://www.radionz.co.nz/news/thedetail/587135/the-wine-industry-headache) | radionz.co.nz | 8 | negative |
| 30 Apr 2026 | [Wine code of conduct details emerge as industry continues to shrink](http://www.abc.net.au/news/rural/2026-04-30/wine-industry-code-of-conduct-details/106614568) | abc.net.au | 7 | positive |
| 22 Apr 2026 | [AI hype or reality? Wine sector weighs its next move](https://www.thedrinksbusiness.com/2026/04/ai-hype-or-reality-wine-sector-weighs-its-next-move/) | thedrinksbusiness.com | 7 | positive |
| 20 Apr 2026 | [Gold mine, wine industry can co-exist: Santana](https://www.odt.co.nz/regions/central-otago/gold-mine-wine-industry-can-co-exist-santana) | odt.co.nz | 7 | positive |
| 14 Apr 2026 | [Napa Valley wine boss demands controversial Trump policy is expanded to save California vineyards](https://nypost.com/2026/04/14/us-news/napa-valley-wine-boss-demands-controversial-trump-policy-is-expanded-to-save-california-vineyards/) | nypost.com | 7 | negative |
| 14 Apr 2026 | [Why WA vintners oppose wine bottle deposit plan](https://thewest.com.au/business/retail/at-a-serious-disadvantage-wa-wine-industry-calls-for-pause-on-bottle-refunds-c-22134872) | thewest.com.au | 7 | negative |
| 2 Apr 2026 | [Weekend wine guide: Marlborough winery responds to market conditions with low-alcohol wines](https://www.nzherald.co.nz/the-listener/life/weekend-wine-guide-marlborough-winery-responds-to-market-conditions-with-low-alcohol-wines/premium/L2A3RHWITZDEBLGKBAKETQMC74/) | nzherald.co.nz | 7 | positive |
| 1 Apr 2026 | [Pennsylvania Department of Agriculture's Agricultural Innovation Grant Program](https://www.morningagclips.com/pennsylvania-department-of-agricultures-agricultural-innovation-grant-program/) | morningagclips.com | 7 | positive |
| 1 Apr 2026 | [4 436 hectares concernés dans l’Aude en 2026 : une "erreur fondamentale" pointée par les acteurs viticoles…](https://www.lindependant.fr/2026/04/01/4-436-hectares-concernes-dans-laude-en-2026-une-erreur-fondamentale-pointee-par-les-acteurs-viticoles-sur-les-modalites-de-larrachage-13300006.php) | lindependant.fr | 7 | positive |
| 30 Mar 2026 | [Tasmanian wine workforce discussion paper released - The Shout](https://theshout.com.au/tasmanian-wine-workforce-discussion-paper-released/) | theshout.com.au | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "wine industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "wine industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "wine industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "wine industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "wine industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Banking Industry](banking-industry.md)
- [Electronics Industry](electronics-industry.md)
- [Cocoa Industry](cocoa-industry.md)
- [Glass Industry](glass-industry.md)
