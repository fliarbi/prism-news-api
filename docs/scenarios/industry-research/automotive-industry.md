# Automotive Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “automotive industry” · 22,200/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [automotive-industry.json](../../examples/scenarios/automotive-industry.json).

**Question.** How much news did the automotive industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="auto industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,378 |
| Negative · neutral · positive | 43% · 0.8% · 56% |
| Critical (priority 7–9) | 61% (836 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (421 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | automotive industry market trends |

## Twelve months of coverage

Monthly matching articles for `auto industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 294 | 60% | 165 | 128 | ██████████████ |
| Jun 2025 | 276 | 71% | 173 | 100 | █████████████ |
| Jul 2025 | 401 | 54% | 210 | 187 | ███████████████████ |
| Aug 2025 | 417 | 56% | 231 | 185 | ████████████████████ |
| Sep 2025 | 343 | 57% | 141 | 201 | ████████████████ |
| Oct 2025 | 296 | 69% | 120 | 163 | ██████████████ |
| Nov 2025 | 181 | 65% | 86 | 92 | █████████ |
| Dec 2025 | 255 | 73% | 132 | 121 | ████████████ |
| Jan 2026 | 307 | 72% | 155 | 147 | ███████████████ |
| Feb 2026 | 421 | 59% | 157 | 263 | ████████████████████ |
| Mar 2026 | 250 | 56% | 108 | 138 | ████████████ |
| Apr 2026 | 400 | 57% | 172 | 227 | ███████████████████ |

The last four complete months averaged 344 articles a month against 347 in the first four (-1%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 58% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 377 | 27% |
| India | 165 | 12% |
| China | 93 | 6.8% |
| Japan | 33 | 2.4% |
| Canada | 25 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| automotive industry market trends | 158 | 20% | +88% |
| electric vehicle (ev) technology | 148 | 19% | +38% |
| automotive industry sustainability initiatives | 74 | 9.5% | +57% |
| electric vehicle charging infrastructure | 92 | 12% | +24% |
| automotive industry mergers and acquisitions | 41 | 5.3% | +64% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 19 Apr 2026 | [SAIC Motor in EL PAÍS English](https://english.elpais.com/news/shanghai-automotive-industry-corporation/) | english.elpais.com | 8 | negative |
| 26 Mar 2026 | [Jeep devises new batch of bold concepts for Moab adventures](https://www.autonews.com/stellantis/an-easter-jeep-safari-0326/) | autonews.com | 8 | negative |
| 14 Mar 2026 | [Another Biggie Pulls to the Side as EV Startups Forge Ahead](http://brandequity.economictimes.indiatimes.com/news/business-of-brands/another-biggie-pulls-to-the-side-as-ev-startups-forge-ahead/129572241) | brandequity.economictimes.indiatimes.com | 8 | negative |
| 30 Jan 2026 | [After Letting China In, Canada Hopes Korea Comes Too \| Carscoops](https://www.carscoops.com/2026/01/after-letting-china-in-canada-hopes-korea-comes-too/) | carscoops.com | 8 | positive |
| 27 Jan 2026 | [Hyundai shares take a hit after Trump threatens further hike in tariffs on S Korean auto, pharma industries…](https://www.cnbctv18.com/market/hyundai-shares-take-a-hit-after-trump-threatens-further-hike-in-tariffs-on-s-korean-auto-pharma-industries-19833535.htm) | cnbctv18.com | 8 | negative |
| 13 Jan 2026 | [Back in Michigan, President Trump Celebrates Auto Industry, Economic Revival](https://www.whitehouse.gov/releases/2026/01/back-in-michigan-president-trump-celebrates-auto-industry-economic-revival/) | whitehouse.gov | 8 | negative |
| 29 Apr 2026 | [NXP Rallies After Stronger Auto Market Bolsters Forecast (2)](https://news.bloomberglaw.com/international-trade/nxp-rallies-after-stronger-automotive-market-bolsters-forecast) | news.bloomberglaw.com | 7 | positive |
| 28 Apr 2026 | [Kia CEO signals price cuts in Europe to counter Chinese competition](https://www.sowetanlive.co.za/motoring/2026-04-28-kia-ceo-signals-price-cuts-in-europe-to-counter-chinese-competition/) | sowetanlive.co.za | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "auto industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "auto industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "auto industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "auto industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "auto industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Textile Industry](textile-industry.md)
- [Food Processing Industry](food-processing-industry.md)
