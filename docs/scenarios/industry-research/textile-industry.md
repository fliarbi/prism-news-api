# Textile Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “textile industry” · 27,100/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [textile-industry.json](../../examples/scenarios/textile-industry.json).

**Question.** How much news did the textile industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="textile industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,982 |
| Negative · neutral · positive | 28% · 1.7% · 70% |
| Critical (priority 7–9) | 55% (1,083 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (642 articles) |
| Most-reported country | India (17% of matches) |
| Strongest theme by lift | textile manufacturing advancements |

## Twelve months of coverage

Monthly matching articles for `textile industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 386 | 45% | 77 | 300 | ████████████ |
| Jun 2025 | 285 | 35% | 42 | 238 | █████████ |
| Jul 2025 | 368 | 56% | 84 | 269 | ███████████ |
| Aug 2025 | 434 | 62% | 185 | 235 | ██████████████ |
| Sep 2025 | 466 | 46% | 87 | 365 | ███████████████ |
| Oct 2025 | 316 | 52% | 80 | 233 | ██████████ |
| Nov 2025 | 289 | 49% | 56 | 224 | █████████ |
| Dec 2025 | 278 | 50% | 60 | 210 | █████████ |
| Jan 2026 | 396 | 60% | 99 | 292 | ████████████ |
| Feb 2026 | 642 | 57% | 183 | 450 | ████████████████████ |
| Mar 2026 | 398 | 53% | 106 | 286 | ████████████ |
| Apr 2026 | 546 | 49% | 165 | 365 | █████████████████ |

The last four complete months averaged 496 articles a month against 368 in the first four (+35%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 330 | 17% |
| United States | 213 | 11% |
| China | 57 | 2.9% |
| United Kingdom | 37 | 1.9% |
| Bangladesh | 25 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| textile manufacturing advancements | 132 | 11% | +83% |
| textile market analysis and forecasts | 117 | 9.9% | +29% |
| global textile trade and import/export trends | 114 | 9.7% | +5% |
| textile manufacturing processes | 62 | 5.2% | +288% |
| textile industry supply chain management | 61 | 5.2% | +307% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Industry Alert: Heat Stress Threatens $65 Billion in Exports and Millions of Jobs](https://wwd.com/sourcing-journal/industry-news/heat-stress-threatens-65-billion-in-exports-1238930790/) | wwd.com | 8 | negative |
| 28 Apr 2026 | [Tamil Nadu: Tiruppur Exporters Association welcomes India-New Zealand FTA](https://www.aninews.in/news/national/general-news/tamil-nadu-tiruppur-exporters-association-welcomes-india-new-zealand-fta20260428170213) | aninews.in | 8 | positive |
| 27 Apr 2026 | [Nigeria’s Textile Industry Needs Deep Structural Reset To Compete, Economist Warns](https://naija247news.com/frontpage/analysis-cover-story/nigerias-textile-industry-needs-deep-structural-reset-to-compete-economist-warns/) | naija247news.com | 8 | negative |
| 16 Apr 2026 | [Op-Ed: Whistleblower Testimony Confirms Systematic Forced Labor in Xinjiang](https://wwd.com/sourcing-journal/industry-news/whistleblower-systematic-forced-labor-xinjiang-china-uyghur-1238864930/) | wwd.com | 8 | negative |
| 6 Apr 2026 | [Iran War To Hit Over 50 pc Of Textile Exports](https://www.deccanchronicle.com/business/iran-war-to-hit-over-50-pc-of-textile-exports-1948869) | deccanchronicle.com | 8 | negative |
| 3 Apr 2026 | [West Asia war impact: LPG crunch forces shutdowns across textile units, lakhs of workers in limbo](https://www.dtnext.in/news/national/west-asia-war-impact-lpg-crunch-forces-shutdowns-across-textile-units-lakhs-of-workers-in-limbo) | dtnext.in | 8 | negative |
| 1 Apr 2026 | [$174 billion on the brink: India's textile industry reels under West Asia war shock, braces for 'huge…](https://cfo.economictimes.indiatimes.com/news/news/174-billion-on-the-brink-indias-textile-industry-reels-under-west-asia-war-shock-braces-for-huge-crisis-in-april/129945837) | cfo.economictimes.indiatimes.com | 8 | negative |
| 23 Mar 2026 | [West Asia Conflict Triggers Industrial Strain in Gujarat as Textile Mills Cut Operations \| Manufacturing…](https://apparelresources.com/business-news/manufacturing/west-asia-conflict-triggers-industrial-strain-gujarat-textile-mills-cut-operations/) | apparelresources.com | 8 | negative |
| 18 Mar 2026 | [AI Meets Human Ingenuity At ITAMMA Awards - Textile Insights](https://textileinsights.in/ai-meets-human-ingenuity-at-itamma-awards/) | textileinsights.in | 8 | negative |
| 14 Mar 2026 | [Textile and Apparel Exports Set for Growth Under New Plan](https://www.indian-apparel.com/ministry-of-textiles-news/proposal-boost-textile-and-apparel-exports-india/) | indian-apparel.com | 8 | positive |
| 12 Mar 2026 | [West Asia Conflict Hits Bhilwara Textile Exports; US $86 Million–US $100 Million in Shipments Affected \|…](https://in.apparelresources.com/business-news/retail/west-asia-conflict-hits-bhilwara-textile-exports-us-86-million-us-100-million-shipments-affected/) | in.apparelresources.com | 8 | negative |
| 12 Mar 2026 | [West Asia conflict hits Bhilwara textile industry, Rs 1000 crore fabric exports impacted](https://economictimes.indiatimes.com/industry/cons-products/garments-/-textiles/west-asia-conflict-hits-bhilwara-textile-industry-rs-1000-crore-fabric-exports-impacted/articleshow/129495807.cms) | economictimes.indiatimes.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "textile industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "textile industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "textile industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "textile industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "textile industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Automotive Industry](automotive-industry.md)
- [Food Processing Industry](food-processing-industry.md)
- [Pharmaceutical Industry](pharmaceutical-industry.md)
