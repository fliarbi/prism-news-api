# Solar Energy News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “solar energy news” · 260/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [solar-energy-news.json](../../examples/scenarios/solar-energy-news.json).

**Question.** How did solar energy coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="solar energy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,185 |
| Negative · neutral · positive | 12% · 1.0% · 87% |
| Critical (priority 7–9) | 76% (10,082 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,072 articles) |
| Most-reported country | United States (20% of matches) |
| Strongest theme by lift | solar photovoltaic (pv) energy systems |

## Twelve months of coverage

Monthly matching articles for `solar energy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,585 | 72% | 382 | 2,158 | █████████████ |
| Jun 2025 | 2,375 | 76% | 288 | 2,065 | ████████████ |
| Jul 2025 | 2,561 | 73% | 436 | 2,096 | █████████████ |
| Aug 2025 | 2,819 | 68% | 521 | 2,265 | ██████████████ |
| Sep 2025 | 2,465 | 74% | 320 | 2,124 | ████████████ |
| Oct 2025 | 2,540 | 76% | 312 | 2,201 | ████████████ |
| Nov 2025 | 2,340 | 79% | 264 | 2,061 | ███████████ |
| Dec 2025 | 2,463 | 79% | 249 | 2,191 | ████████████ |
| Jan 2026 | 2,498 | 78% | 247 | 2,231 | ████████████ |
| Feb 2026 | 3,487 | 78% | 405 | 3,040 | █████████████████ |
| Mar 2026 | 3,128 | 75% | 422 | 2,666 | ███████████████ |
| Apr 2026 | 4,072 | 76% | 562 | 3,471 | ████████████████████ |

The last four complete months averaged 3,296 articles a month against 2,585 in the first four (+28%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,581 | 20% |
| India | 1,311 | 9.9% |
| United Kingdom | 285 | 2.2% |
| China | 271 | 2.1% |
| Australia | 244 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| solar photovoltaic (pv) energy systems | 4,305 | 45% | +45% |
| renewable energy policy & regulation | 752 | 7.9% | +93% |
| smart grid integration for renewables | 653 | 6.9% | +75% |
| solar panel recycling & waste management | 600 | 6.3% | +55% |
| community solar & shared renewable projects | 1,242 | 13% | +45% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 26 Mar 2026 | [State of Climate Report: What’s Driving Earth’s Energy Imbalance?](https://impakter.com/state-of-global-climate-report-whats-driving-earths-energy-imbalance/) | impakter.com | 9 | negative |
| 23 Mar 2026 | ['Flashing red': climate imbalance reaches all-time high](https://www.perthnow.com.au/news/technology/flashing-red-climate-imbalance-reaches-all-time-high-c-22034142) | perthnow.com.au | 9 | negative |
| 30 Apr 2026 | [India Rises to World’s No. 2 Solar Market as Clean Energy Push Gains Pace \| SportsZ News](https://sportsz.news/news/india-rises-to-worlds-no-2-solar-market-as-clean-energy-push-gains-pace/) | sportsz.news | 8 | positive |
| 29 Apr 2026 | [Global Solar Adoption Surges Amid Fossil Fuel Crisis](https://www.newkerala.com/news/a/more-countries-turning-solar-amid-high-fossil-fuel-167.htm) | newkerala.com | 8 | positive |
| 29 Apr 2026 | [Copernicus-Bericht 2025: Klimawandel macht Europa weiterhin zu schaffen](https://tagesschau.de/wissen/klima/klima-copernicus-bericht-100.html) | tagesschau.de | 8 | negative |
| 28 Apr 2026 | [Meta looks to solar power for AI data centres \| TahawulTech.com](https://www.tahawultech.com/news/meta-looks-to-solar-power-for-ai-data-centres/) | tahawultech.com | 8 | positive |
| 28 Apr 2026 | [Paradox Of Green Progress: Solar Expansion And Limits Of Environmental Law In Rajasthan](https://www.livelaw.in/articles/solar-expansion-environmental-law-limits-rajasthan-531890) | livelaw.in | 8 | positive |
| 27 Apr 2026 | [Meta Boosts AI Power with Space Solar & Energy Storage](https://www.newkerala.com/news/a/meta-announces-two-partnerships-boost-reliable-power-its-846.htm) | newkerala.com | 8 | positive |
| 27 Apr 2026 | [Meta seeks to power data centers with energy beamed from space](https://www.latimes.com/business/story/2026-04-27/meta-seeks-to-power-data-centers-with-energy-beamed-from-space) | latimes.com | 8 | positive |
| 27 Apr 2026 | [Egypt: Madbouly urges solar transition, lifts early closing hours for shops](https://www.zawya.com/en/economy/north-africa/egypt-madbouly-urges-solar-transition-lifts-early-closing-hours-for-shops-h5stprlh) | zawya.com | 8 | negative |
| 26 Apr 2026 | [Solar Energy: Solar infra helps India meet record 256GW power demand \| India News - The Times of India](https://timesofindia.indiatimes.com/india/solar-infra-helps-india-meet-record-256gw-power-demand/articleshow/130539197.cms) | timesofindia.indiatimes.com | 8 | positive |
| 25 Apr 2026 | [Harvesting the sun: How solar energy is powering the future of rural farming economies](https://www.thehindubusinessline.com/economy/agri-business/harvesting-the-sun-how-solar-energy-is-powering-the-future-of-rural-farming-economies/article70902734.ece) | thehindubusinessline.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "solar energy" --since 2026-01-01 --until 2026-04-30
prism-news trends "solar energy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "solar energy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "solar energy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "solar energy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Solar Panels Industry](solar-panels-industry.md)
- [Fusion Energy News](fusion-energy-news.md)
- [Air Pollution Industry](air-pollution-industry.md)
- [Lithium News](lithium-news.md)
