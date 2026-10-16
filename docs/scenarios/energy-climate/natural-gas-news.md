# Natural Gas News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “natural gas news” · 60,500/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [natural-gas-news.json](../../examples/scenarios/natural-gas-news.json).

**Question.** How did natural gas coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="natural gas"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 23,125 |
| Negative · neutral · positive | 51% · 2.7% · 46% |
| Critical (priority 7–9) | 74% (17,156 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (9,501 articles) |
| Most-reported country | United States (22% of matches) |
| Strongest theme by lift | natural gas liquefaction processes |

## Twelve months of coverage

Monthly matching articles for `natural gas` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,643 | 62% | 899 | 1,619 | ██████ |
| Jun 2025 | 2,216 | 68% | 783 | 1,396 | █████ |
| Jul 2025 | 2,499 | 65% | 845 | 1,606 | █████ |
| Aug 2025 | 3,300 | 68% | 1,146 | 2,087 | ███████ |
| Sep 2025 | 3,104 | 75% | 1,204 | 1,821 | ███████ |
| Oct 2025 | 2,795 | 74% | 926 | 1,807 | ██████ |
| Nov 2025 | 2,530 | 71% | 690 | 1,787 | █████ |
| Dec 2025 | 2,923 | 67% | 735 | 2,131 | ██████ |
| Jan 2026 | 3,032 | 68% | 917 | 2,035 | ██████ |
| Feb 2026 | 3,388 | 68% | 1,041 | 2,233 | ███████ |
| Mar 2026 | 9,501 | 81% | 6,285 | 2,977 | ████████████████████ |
| Apr 2026 | 7,204 | 71% | 3,631 | 3,368 | ███████████████ |

The last four complete months averaged 5,781 articles a month against 2,664 in the first four (+117%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,131 | 22% |
| India | 2,612 | 11% |
| Iran | 551 | 2.4% |
| Canada | 395 | 1.7% |
| China | 297 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| natural gas liquefaction processes | 4,772 | 28% | +141% |
| gas flaring reduction techniques | 2,077 | 12% | +151% |
| liquefied natural gas (lng) storage | 4,609 | 27% | +146% |
| pipeline infrastructure development | 2,551 | 15% | +269% |
| natural gas extraction processes | 3,796 | 22% | +145% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [European natural gas prices ticked higher on Friday, as investors gauged the ongoing blockage of the Strait…](https://www.hellenicshippingnews.com/european-natural-gas-prices-rise-as-mideast-tensions-weigh-on-supplies/) | hellenicshippingnews.com | 9 | negative |
| 24 Apr 2026 | [IEA says Iran war will keep the global natural gas market tight for two years](https://www.cbsnews.com/news/iran-war-lng-supply-iea-report-gas-markets-impact/) | cbsnews.com | 9 | negative |
| 24 Apr 2026 | [The Islamic Republic of Iran’s Underground Missile Cities \| Opinion - Conservative \| Before It's News](https://beforeitsnews.com/opinion-conservative/2026/04/the-islamic-republic-of-irans-underground-missile-cities-3738934.html) | beforeitsnews.com | 9 | negative |
| 22 Apr 2026 | [Iran war conflict could create systemic gas demand destruction, says top sector official](https://www.straitstimes.com/asia/iran-war-conflict-could-create-systemic-gas-demand-destruction-says-top-sector-official) | straitstimes.com | 9 | negative |
| 22 Apr 2026 | [Iran war conflict could create systemic gas demand destruction, says top sector official \| BOE Report](https://boereport.com/2026/04/22/iran-war-conflict-could-create-systemic-gas-demand-destruction-says-top-sector-official/) | boereport.com | 9 | negative |
| 22 Apr 2026 | [Dual House Explosions Hospitalize Five People in San Antonio](https://world.infonasional.com/san-antonio-house-explosions-injuries) | world.infonasional.com | 9 | negative |
| 16 Apr 2026 | [West Reading chocolate factory explosion: PA legislation addresses natural gas safety concerns](https://www.mcall.com/2026/04/16/west-reading-chocolate-factory-explosion-pa-legislation-addresses-natural-gas-safety-concerns/) | mcall.com | 9 | negative |
| 16 Apr 2026 | [Energy analysts have warned of surging energy prices beyond already elevated levels, as the last vessels…](https://www.hellenicshippingnews.com/energy-prices-set-to-rise-as-last-gulf-tankers-reach-europe-analysts-say/) | hellenicshippingnews.com | 9 | negative |
| 14 Apr 2026 | [TurkStream: The Strategic Pillar of Europe's Energy Security - Time News](https://time.news/turkstream-the-strategic-pillar-of-europes-energy-security/) | time.news | 9 | negative |
| 8 Apr 2026 | [European gas prices plunge on hopes for restored LNG flows following US-Iran ceasefire](https://www.bairdmaritime.com/shipping/tankers/gas/european-gas-prices-plunge-on-hopes-for-restored-lng-flows-following-us-iran-ceasefire) | bairdmaritime.com | 9 | negative |
| 7 Apr 2026 | [Deadly South Jordan house explosion report stresses importance of natural gas alarms](https://www.fox13now.com/news/local-news/salt-lake-county/deadly-south-jordan-house-explosion-report-stresses-importance-of-natural-gas-alarms) | fox13now.com | 9 | negative |
| 7 Apr 2026 | [Investing in America: 1937 New London Explosion](https://www.yahoo.com/news/articles/investing-america-1937-london-explosion-015726970.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "natural gas" --since 2026-01-01 --until 2026-04-30
prism-news trends "natural gas" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "natural gas" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "natural gas", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "natural gas", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Petrol Price News](petrol-price-news.md)
- [Coal Industry](coal-industry.md)
