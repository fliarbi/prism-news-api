# Energy Storage News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “energy storage news” · 50/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [energy-storage-news.json](../../examples/scenarios/energy-storage-news.json).

**Question.** How did energy storage coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="energy storage"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,648 |
| Negative · neutral · positive | 12% · 0.6% · 88% |
| Critical (priority 7–9) | 76% (10,375 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,665 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | smart grid integration for renewables |

## Twelve months of coverage

Monthly matching articles for `energy storage` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,893 | 78% | 103 | 1,772 | ██████████ |
| Jun 2025 | 1,826 | 80% | 99 | 1,711 | ██████████ |
| Jul 2025 | 2,056 | 82% | 123 | 1,923 | ███████████ |
| Aug 2025 | 1,841 | 79% | 116 | 1,706 | ██████████ |
| Sep 2025 | 2,202 | 80% | 80 | 2,107 | ████████████ |
| Oct 2025 | 2,366 | 82% | 117 | 2,232 | █████████████ |
| Nov 2025 | 2,234 | 82% | 159 | 2,064 | ████████████ |
| Dec 2025 | 2,413 | 80% | 115 | 2,278 | █████████████ |
| Jan 2026 | 3,018 | 84% | 179 | 2,827 | ████████████████ |
| Feb 2026 | 3,618 | 71% | 553 | 3,045 | ████████████████████ |
| Mar 2026 | 3,347 | 73% | 476 | 2,845 | ██████████████████ |
| Apr 2026 | 3,665 | 77% | 376 | 3,265 | ████████████████████ |

The last four complete months averaged 3,412 articles a month against 1,904 in the first four (+79%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,284 | 17% |
| India | 994 | 7.3% |
| China | 646 | 4.7% |
| United Kingdom | 342 | 2.5% |
| Australia | 340 | 2.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| smart grid integration for renewables | 1,029 | 12% | +82% |
| battery charging systems | 947 | 11% | +36% |
| renewable energy storage solutions (battery, thermal) | 2,683 | 30% | +48% |
| battery backup systems for electronics | 842 | 9.4% | +43% |
| electricity storage solutions & battery technologies | 401 | 4.5% | +73% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [China's Largest BTM Storage Project by Great Power and Zhongfu was Put into Operation! - Shanghai Metals…](https://news.metal.com/en/newscontent/103881704-Chinas-Largest-BTM-Storage-Project-by-Great-Power-and-Zhongfu-was-Put-into-Operation-) | news.metal.com | 8 | positive |
| 29 Apr 2026 | [Iron Flow Battery Achieves Record Lifespan - Electronics For You – Official Site ElectronicsForU.com](https://www.electronicsforu.com/news/iron-flow-battery-achieves-record-lifespan) | electronicsforu.com | 8 | positive |
| 29 Apr 2026 | [China's Biggest BTM Storage Project by Great Power and Zhongfu was Put into Operation! - Shanghai Metals…](https://news.metal.com/en/newscontent/103881704-Chinas-Biggest-BTM-Storage-Project-by-Great-Power-and-Zhongfu-was-Put-into-Operation-) | news.metal.com | 8 | positive |
| 28 Apr 2026 | [CATL and HyperStrong sign 60GWh sodium-ion storage deal - Best Magazine](https://www.bestmag.co.uk/catl-hyperstrong-60gwh-sodium-ion-storage/) | bestmag.co.uk | 8 | positive |
| 28 Apr 2026 | [Today's headlines: Two more offshore wind-killing deals, Republicans…](https://www.canarymedia.com/newsletters/todays-headlines-two-more-offshore-wind-killing-deals-republicans-want-to-revive-tax-credits-and-more) | canarymedia.com | 8 | positive |
| 28 Apr 2026 | [CATL says sodium batteries are mainstream-ready, signs massive 60 GWh deal](https://electrek.co/2026/04/27/catl-sodium-ion-battery-60gwh-energy-storage-deal) | electrek.co | 8 | positive |
| 28 Apr 2026 | [Multifunctional Strategies in Lithium-Sulfur Batteries: From Fundamentals to Future Technologies.](https://pubmed.ncbi.nlm.nih.gov/42053108/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 28 Apr 2026 | [Taming the Temperature Extremes: An Entropy-Regulated Electrolyte for Wide-Temperature Lithium-Ion Batteries.](https://pubmed.ncbi.nlm.nih.gov/42048653/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 27 Apr 2026 | [Meta Boosts AI Power with Space Solar & Energy Storage](https://www.newkerala.com/news/a/meta-announces-two-partnerships-boost-reliable-power-its-846.htm) | newkerala.com | 8 | positive |
| 27 Apr 2026 | [Multilateral Development Banks’ Clean Electricity Finance](http://www.nrdc.org/resources/multilateral-development-banks-clean-electricity-finance) | nrdc.org | 8 | positive |
| 27 Apr 2026 | [Middle East Construction News](https://meconstructionnews.com/67265/saudi-invites-bids-for-12000mwh-battery-energy-storage-system) | meconstructionnews.com | 8 | positive |
| 27 Apr 2026 | [China’s solar giant Sungrow revives Hong Kong IPO plan amid clean energy boom](https://www.scmp.com/business/china-business/article/3351515/chinas-solar-giant-sungrow-revives-hong-kong-ipo-plan-amid-rising-demand-clean-energy) | scmp.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "energy storage" --since 2026-01-01 --until 2026-04-30
prism-news trends "energy storage" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "energy storage" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "energy storage", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "energy storage", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Lithium News](lithium-news.md)
- [Refinery News](refinery-news.md)
- [Emissions Industry](emissions-industry.md)
- [Power Outage News](power-outage-news.md)
