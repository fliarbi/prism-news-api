# Electric Vehicles News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “electric vehicles news” · 260/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [electric-vehicles-news.json](../../examples/scenarios/electric-vehicles-news.json).

**Question.** How did electric vehicles coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="electric vehicles"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 49,613 |
| Negative · neutral · positive | 19% · 9.9% · 71% |
| Critical (priority 7–9) | 45% (22,254 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (16,804 articles) |
| Most-reported country | India (21% of matches) |
| Strongest theme by lift | government incentives for alternative fuel vehicles |

## Twelve months of coverage

Monthly matching articles for `electric vehicles` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7,725 | 55% | 1,847 | 5,763 | █████████ |
| Jun 2025 | 7,086 | 52% | 1,866 | 5,149 | ████████ |
| Jul 2025 | 10,699 | 42% | 2,405 | 8,175 | █████████████ |
| Aug 2025 | 7,564 | 53% | 1,614 | 5,862 | █████████ |
| Sep 2025 | 9,172 | 53% | 1,847 | 7,208 | ███████████ |
| Oct 2025 | 8,516 | 54% | 1,944 | 6,461 | ██████████ |
| Nov 2025 | 7,107 | 54% | 1,297 | 5,677 | ████████ |
| Dec 2025 | 8,353 | 50% | 1,728 | 6,541 | ██████████ |
| Jan 2026 | 9,288 | 51% | 2,151 | 7,008 | ███████████ |
| Feb 2026 | 16,804 | 34% | 2,322 | 9,990 | ████████████████████ |
| Mar 2026 | 10,575 | 47% | 2,584 | 7,863 | █████████████ |
| Apr 2026 | 12,946 | 52% | 2,585 | 10,199 | ███████████████ |

The last four complete months averaged 12,403 articles a month against 8,268 in the first four (+50%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 51% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 10,262 | 21% |
| United States | 6,634 | 13% |
| China | 1,991 | 4.0% |
| United Kingdom | 1,375 | 2.8% |
| Australia | 534 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| government incentives for alternative fuel vehicles | 2,393 | 8.1% | +40% |
| electric vehicle (ev) technology | 3,488 | 12% | +19% |
| electric vehicle charging infrastructure | 2,788 | 9.4% | +22% |
| lithium-ion battery advancements for evs | 1,400 | 4.7% | +84% |
| alternative fuel vehicle market trends | 1,260 | 4.2% | +147% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Mar 2026 | [A reminder as oil prices spike: EVs are the #1 route to energy independence](https://electrek.co/2026/03/10/a-reminder-as-oil-prices-spike-evs-are-the-1-route-to-energy-independence/) | electrek.co | 9 | negative |
| 29 Apr 2026 | [Govt mulls partial credit guarantee, interest subvention support for pvt sector electric bus, truck adoption…](https://www.livemint.com/economy/india-government-plans-finance-electric-private-buses-trucks-clean-mobility-11777473638619.html) | livemint.com | 8 | positive |
| 29 Apr 2026 | [China commerce minister says reached 'soft landing' with EU over EV tariffs](https://www.auto.economictimes.indiatimes.com/news/industry/china-commerce-minister-says-reached-soft-landing-with-eu-over-ev-tariffs/130599949) | auto.economictimes.indiatimes.com | 8 | positive |
| 29 Apr 2026 | [Two million electric vehicles registered in the UK](https://transportandenergy.com/2026/04/29/two-million-electric-vehicles-registered-in-the-uk/) | transportandenergy.com | 8 | positive |
| 24 Apr 2026 | [China's auto industry races to embed AI in just about everything](https://www.detroitnews.com/story/business/autos/2026/04/24/chinas-auto-industry-races-to-embed-ai-in-just-about-everything/89770948007/) | detroitnews.com | 8 | positive |
| 24 Apr 2026 | [After call from Beijing, China’s auto industry races to embed AI in just about everything](https://www.straitstimes.com/asia/east-asia/after-call-from-beijing-chinas-auto-industry-races-to-embed-ai-in-just-about-everything) | straitstimes.com | 8 | positive |
| 24 Apr 2026 | [China's auto industry races to embed AI in line with Beijing mandate](https://www.asiaone.com/money/chinas-auto-industry-races-embed-ai-line-beijing-mandate) | asiaone.com | 8 | positive |
| 24 Apr 2026 | [Tariff waiver raises fresh concerns for automotive policy, stability](https://guardian.ng/business-services/tariff-waiver-raises-fresh-concerns-for-automotive-policy-stability-2/) | guardian.ng | 8 | negative |
| 23 Apr 2026 | [The Plant That Could End America's Reliance on Foreign Rare-Earth Metals](https://indiandefencereview.com/the-plant-that-could-end-rare-earth-metals/) | indiandefencereview.com | 8 | positive |
| 23 Apr 2026 | [Solar, battery, EV exports from China hit record USD 21.9B in March, surge 70%](https://powerphilippines.com/solar-battery-ev-exports-from-china-hit-record-usd-21-9b-in-march-surge-70/) | powerphilippines.com | 8 | positive |
| 22 Apr 2026 | [IEA: 2025 Global Electricity Demand to Rise 3%, EVs and Data Centers Become Core Engines](https://autonews.gasgoo.com/articles/news/iea-2025-global-electricity-demand-to-rise-3-evs-and-data-centers-become-core-engines-2046958701091487745) | autonews.gasgoo.com | 8 | positive |
| 22 Apr 2026 | [Govt Speeds Up EV Shift After Missing Production, Charging Stations Targets](https://www.techjuice.pk/govt-speeds-up-ev-shift-after-missing-production-charging-stations-targets/) | techjuice.pk | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "electric vehicles" --since 2026-01-01 --until 2026-04-30
prism-news trends "electric vehicles" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "electric vehicles" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "electric vehicles", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "electric vehicles", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Floods News](floods-news.md)
- [Renewable Energy News](renewable-energy-news.md)
- [Wildfire News](wildfire-news.md)
- [OPEC News](opec-news.md)
