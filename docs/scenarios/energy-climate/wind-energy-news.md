# Wind Energy News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wind energy news” · 170/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wind-energy-news.json](../../examples/scenarios/wind-energy-news.json).

**Question.** How did wind energy coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="wind energy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,930 |
| Negative · neutral · positive | 18% · 1.8% · 80% |
| Critical (priority 7–9) | 77% (3,028 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,250 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | wind turbine technology & onshore wind farms |

## Twelve months of coverage

Monthly matching articles for `wind energy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 870 | 76% | 237 | 621 | ██████████████ |
| Jun 2025 | 718 | 79% | 142 | 563 | ███████████ |
| Jul 2025 | 1,044 | 78% | 299 | 716 | █████████████████ |
| Aug 2025 | 846 | 74% | 280 | 551 | ██████████████ |
| Sep 2025 | 750 | 76% | 170 | 569 | ████████████ |
| Oct 2025 | 727 | 73% | 70 | 652 | ████████████ |
| Nov 2025 | 590 | 77% | 78 | 508 | █████████ |
| Dec 2025 | 829 | 81% | 189 | 631 | █████████████ |
| Jan 2026 | 850 | 78% | 143 | 689 | ██████████████ |
| Feb 2026 | 925 | 74% | 159 | 735 | ███████████████ |
| Mar 2026 | 905 | 77% | 177 | 714 | ██████████████ |
| Apr 2026 | 1,250 | 79% | 236 | 1,006 | ████████████████████ |

The last four complete months averaged 982 articles a month against 870 in the first four (+13%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 694 | 18% |
| India | 349 | 8.9% |
| United Kingdom | 97 | 2.5% |
| China | 94 | 2.4% |
| Australia | 74 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| wind turbine technology & onshore wind farms | 1,017 | 37% | +43% |
| renewable energy policy & regulation | 260 | 9.4% | +71% |
| offshore floating wind turbine technology | 222 | 8.0% | +24% |
| offshore wind energy development | 559 | 20% | +30% |
| renewable energy investment & financing models | 168 | 6.1% | +144% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Feb 2026 | [Don’t let climate fatalism become a self-fulfilling prophecy](https://www.popsci.com/environment/dont-let-climate-fatalism-become-a-self-fulfilling-prophecy/) ⚠ | popsci.com | 9 | negative |
| 30 Apr 2026 | [Intermittent renewables and rising demand: Why grid resilience is now critical](https://www.pv-magazine-india.com/2026/04/30/intermittent-renewables-and-rising-demand-why-grid-resilience-is-now-critical/) | pv-magazine-india.com | 8 | positive |
| 30 Apr 2026 | [Asia accelerates electrification as oil supply risks reshape energy strategy](https://www.domain-b.com/economy/world-economy/asia-electrification-energy-shift-2026) | domain-b.com | 8 | positive |
| 30 Apr 2026 | [Global wind installations up 40 percent during 2026, according to GWEC](https://www.heavyliftpfi.com/business/2026/04/30/global-wind-installations-up-40-percent-during-2026-according-to-gwec/) | heavyliftpfi.com | 8 | positive |
| 29 Apr 2026 | [India–Kenya trade surges to USD 4.31 bn, JTC meet deepens economic ties](https://www.uniindia.com/india-kenya-trade-surges-to-usd-4-31-bn-jtc-meet-deepens-economic-ties/business-economy/news/3826248.html) ⚠ | uniindia.com | 8 | positive |
| 28 Apr 2026 | [Trump administration blocks US wind energy projects in switch to oil and gas](https://www.theguardian.com/us-news/2026/apr/28/trump-administration-wind-projects) | theguardian.com | 8 | negative |
| 28 Apr 2026 | [Trump’s attempt to crush clean energy progress not going to plan, experts say](https://www.theguardian.com/us-news/2026/apr/28/trump-clean-energy-progress) | theguardian.com | 8 | negative |
| 28 Apr 2026 | [US wind installations to gain pace through 2028 - Wood Mackenzie](https://renewablesnow.com/news/us-wind-installations-to-gain-pace-through-2028-wood-mackenzie-1293787/) | renewablesnow.com | 8 | positive |
| 28 Apr 2026 | [Third Japanese Management Training Programme in May](http://island.lk/third-japanese-management-training-programme-in-may/) | island.lk | 8 | positive |
| 28 Apr 2026 | [ADB-backed grid upgrade tender signals next phase of Sri Lanka’s energy transition](http://island.lk/adb-backed-grid-upgrade-tender-signals-next-phase-of-sri-lankas-energy-transition/) | island.lk | 8 | positive |
| 27 Apr 2026 | [WindEurope raises alarm over misinformation risks to wind buildout](https://renewablesnow.com/news/windeurope-raises-alarm-over-misinformation-risks-to-wind-buildout-1293754/) | renewablesnow.com | 8 | negative |
| 27 Apr 2026 | [U.S. Energy Information Administration Projects 80 GW Surge In Solar, Wind And Storage By 2027](https://solarquarter.com/2026/04/27/u-s-energy-information-administration-projects-80-gw-surge-in-solar-wind-and-storage-by-2027/) | solarquarter.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "wind energy" --since 2026-01-01 --until 2026-04-30
prism-news trends "wind energy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "wind energy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "wind energy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "wind energy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Emissions Industry](emissions-industry.md)
- [Power Outage News](power-outage-news.md)
- [Heatwave News](heatwave-news.md)
- [Offshore Wind News](offshore-wind-news.md)
