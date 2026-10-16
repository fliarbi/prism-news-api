# Nickel News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nickel news” · 320/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nickel-news.json](../../examples/scenarios/nickel-news.json).

**Question.** How did nickel coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="nickel"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,117 |
| Negative · neutral · positive | 21% · 1.9% · 77% |
| Critical (priority 7–9) | 43% (2,182 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,607 articles) |
| Most-reported country | United States (38% of matches) |
| Strongest theme by lift | mineral exploration drilling techniques |

## Twelve months of coverage

Monthly matching articles for `nickel` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 980 | 36% | 222 | 729 | ████████████ |
| Jun 2025 | 838 | 36% | 165 | 650 | ██████████ |
| Jul 2025 | 1,204 | 36% | 322 | 865 | ███████████████ |
| Aug 2025 | 1,563 | 29% | 417 | 1,109 | ███████████████████ |
| Sep 2025 | 1,018 | 40% | 168 | 815 | █████████████ |
| Oct 2025 | 1,029 | 36% | 172 | 818 | █████████████ |
| Nov 2025 | 1,090 | 37% | 207 | 853 | ██████████████ |
| Dec 2025 | 1,150 | 36% | 230 | 890 | ██████████████ |
| Jan 2026 | 1,045 | 42% | 209 | 814 | █████████████ |
| Feb 2026 | 1,370 | 45% | 316 | 1,023 | █████████████████ |
| Mar 2026 | 1,095 | 40% | 204 | 869 | ██████████████ |
| Apr 2026 | 1,607 | 43% | 366 | 1,213 | ████████████████████ |

The last four complete months averaged 1,279 articles a month against 1,146 in the first four (+12%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 61% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,944 | 38% |
| Canada | 301 | 5.9% |
| United Kingdom | 132 | 2.6% |
| Indonesia | 115 | 2.2% |
| China | 93 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mineral exploration drilling techniques | 166 | 5.4% | +35% |
| metal commodity trading trends | 89 | 2.9% | +345% |
| battery charging systems | 89 | 2.9% | +31% |
| industrial metal market analysis | 122 | 4.0% | +230% |
| battery backup systems for electronics | 67 | 2.2% | +31% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Nickel Mines shooter's widow plans to remarry](https://lancasteronline.com/news/nickel-mines-shooters-widow-plans-to-remarry/article_26f70c69-1eec-54ca-ac5b-3fc0ce590e69.html) | lancasteronline.com | 9 | negative |
| 16 Apr 2026 | [NASA's Perseverance Detects That 3-Billion-Year-Old Mars Rocks Contain Something Never Seen Before at This…](https://dailygalaxy.com/2026/04/rover-found-mars-rocks-contain-something/) | dailygalaxy.com | 8 | positive |
| 12 Apr 2026 | [Hyundai Motor Group partners Korea Zinc on nickel value chain for EV business \| Autocar Professional](https://www.autocarpro.in/news-international/hyundai-motor-group-partners-korea-zinc-on-nickel-value-chain-for-ev-business-116571) | autocarpro.in | 8 | positive |
| 5 Apr 2026 | [Indonesia’s Electric Vehicle Vision Boosted by South Korea’s Strategic Partnership: A Key to Tourism and…](https://www.travelandtourworld.com/news/article/indonesias-electric-vehicle-vision-boosted-by-south-koreas-strategic-partnership-a-key-to-tourism-and-economic-growth/) | travelandtourworld.com | 8 | positive |
| 1 Apr 2026 | [Nickel: Regulator action is driving increased digital asset investment](https://www.financialinvestigator.nl/nl/nieuws-detailpagina/2026/04/01/nickel-regulator-action-is-driving-increased-digital-asset-investment) | financialinvestigator.nl | 8 | positive |
| 27 Mar 2026 | [【SMM Analysis】Windfall or Export Levy? Inside Indonesia's Upcoming Commodities’ Tax - Shanghai Metals Market…](https://news.metal.com/en/newscontent/103829040-SMM-AnalysisWindfall-or-Export-Levy-Inside-Indonesias-Upcoming-Commodities%E2%80%99-Tax) | news.metal.com | 8 | negative |
| 27 Feb 2026 | [Global Alloy Price Shock and Its Impact on the Mold Steel Market: A Structural Analysis](https://www.linkedin.com/pulse/global-alloy-price-shock-its-impact-mold-steel-market-structural-ryi2c) | linkedin.com | 8 | negative |
| 24 Feb 2026 | [Inside India’s battery recycling push: securing materials for the next phase of EV manufacturing -…](https://www.manufacturingtodayindia.com/inside-indias-battery-recycling-push-securing-materials-for-the-next-phase-of-ev-manufacturing) | manufacturingtodayindia.com | 8 | positive |
| 23 Feb 2026 | [China set to seek new nickel sources amid US agreement](https://www.pressreader.com/china/south-china-morning-post-6150/20260224/281951729289783) | pressreader.com | 8 | positive |
| 11 Feb 2026 | [Nickel jumps as top Indonesia mine gets lower output quota](https://www.zawya.com/en/business/commodities/nickel-jumps-as-top-indonesia-mine-gets-lower-output-quota-ukxxca5r) | zawya.com | 8 | positive |
| 6 Feb 2026 | [China investors flood metals markets amid economic slowdown](https://bitcoinethereumnews.com/finance/china-investors-flood-metals-markets-amid-economic-slowdown/) | bitcoinethereumnews.com | 8 | negative |
| 6 Feb 2026 | [China investors flood metals markets amid economic slowdown - Cryptopolitan](https://www.cryptopolitan.com/china-investors-flood-metals-markets/) | cryptopolitan.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "nickel" --since 2026-01-01 --until 2026-04-30
prism-news trends "nickel" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "nickel" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "nickel", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "nickel", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Biofuels News](biofuels-news.md)
- [Green Hydrogen News](green-hydrogen-news.md)
- [Air Quality News](air-quality-news.md)
- [Pipeline News](pipeline-news.md)
