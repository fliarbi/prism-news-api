# Chemical Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “chemical industry” · 5,400/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [chemical-industry.json](../../examples/scenarios/chemical-industry.json).

**Question.** How much news did the chemical industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="chemical industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,399 |
| Negative · neutral · positive | 40% · 3.2% · 57% |
| Critical (priority 7–9) | 47% (1,128 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (918 articles) |
| Most-reported country | United States (12% of matches) |
| Strongest theme by lift | mergers and acquisitions in the chemical sector |

## Twelve months of coverage

Monthly matching articles for `chemical industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 365 | 54% | 90 | 266 | ████████ |
| Jun 2025 | 241 | 51% | 40 | 198 | █████ |
| Jul 2025 | 321 | 64% | 93 | 215 | ███████ |
| Aug 2025 | 311 | 64% | 106 | 189 | ███████ |
| Sep 2025 | 441 | 46% | 76 | 358 | ██████████ |
| Oct 2025 | 387 | 62% | 85 | 297 | ████████ |
| Nov 2025 | 339 | 56% | 76 | 254 | ███████ |
| Dec 2025 | 300 | 57% | 84 | 207 | ███████ |
| Jan 2026 | 379 | 60% | 102 | 263 | ████████ |
| Feb 2026 | 918 | 34% | 503 | 387 | ████████████████████ |
| Mar 2026 | 542 | 54% | 175 | 348 | ████████████ |
| Apr 2026 | 560 | 52% | 177 | 365 | ████████████ |

The last four complete months averaged 600 articles a month against 310 in the first four (+94%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 29% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 284 | 12% |
| India | 92 | 3.8% |
| China | 65 | 2.7% |
| Germany | 57 | 2.4% |
| United Kingdom | 46 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mergers and acquisitions in the chemical sector | 170 | 13% | +188% |
| specialty chemicals manufacturing processes | 149 | 11% | +314% |
| global chemical market trends and analysis | 185 | 14% | +68% |
| agrochemicals development and distribution | 112 | 8.4% | +20% |
| polymers and plastics production | 112 | 8.4% | +348% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Macclesfield site in line for share of Â£300m boost as AstraZeneca about turns on investment pause -…](https://www.prolificnorth.co.uk/news/macclesfield-site-in-line-for-share-of-300m-boost-as-astrazeneca-about-turns-on-investment-pause/) ⚠ | prolificnorth.co.uk | 8 | positive |
| 28 Apr 2026 | [Who's Responsible When a Contractor Gets Killed?](https://www.chemicalprocessing.com/show-coverage/echemexpo/article/55371757/whos-responsible-when-a-contractor-gets-killed) | chemicalprocessing.com | 8 | negative |
| 27 Apr 2026 | [Supreme Court grapples with multibillion-dollar wave of lawsuits over Roundup cancer claims](https://abcnews.com/US/wireStory/supreme-court-grapples-multibillion-dollar-wave-lawsuits-roundup-132430137) ⚠ | abcnews.com | 8 | negative |
| 27 Apr 2026 | [Chemoinformatics Market to Witness Significant Growth, Reaching USD 16,730 Million by 2033](https://www.openpr.com/news/4491037/chemoinformatics-market-to-witness-significant-growth) | openpr.com | 8 | positive |
| 21 Apr 2026 | [India Eyes $12B Tariff Windfall - South Asian Herald](https://southasianherald.com/india-eyes-12b-tariff-windfall/) ⚠ | southasianherald.com | 8 | negative |
| 21 Apr 2026 | [Community pharmacists hail FG ban on importation of locally-produced drugs](https://www.vanguardngr.com/2026/04/community-pharmacists-hail-fg-ban-on-importation-of-locally-produced-drugs/) ⚠ | vanguardngr.com | 8 | negative |
| 18 Apr 2026 | [Why Gujarat High Court called Bharuch Collector "illiterate"](https://www.barandbench.com/news/litigation/why-gujarat-high-court-called-bharuch-collector-illiterate) ⚠ | barandbench.com | 8 | negative |
| 17 Apr 2026 | [China’s air pollution control enters ‘deep water’ phase](http://www.eco-business.com/news/chinas-air-pollution-control-enters-deep-water-phase/) ⚠ | eco-business.com | 8 | negative |
| 16 Apr 2026 | [A Strong America Starts by Standing Up to Unfair Trade — and Standing with American Chemistry](https://www.breitbart.com/politics/2026/04/16/a-strong-america-starts-by-standing-up-to-unfair-trade-and-standing-with-american-chemistry/) ⚠ | breitbart.com | 8 | negative |
| 16 Apr 2026 | [MORNING GLORY: If you care about the Constitution, read Sarah Isgur's new book - FOX 24 WTAT](https://www.foxcharleston.com/morning-glory-if-you-care-about-the-constitution-read-sarah-isgurs-new-book/) | foxcharleston.com | 8 | negative |
| 16 Apr 2026 | [Europe’s chemical industry is in free fall — America's could be next](https://www.foxnews.com/opinion/europes-chemical-industry-free-fall-americas-could-next) | foxnews.com | 8 | negative |
| 15 Apr 2026 | [UK moves closer to major battery plant for electric cars,Auto news \| Autocar Professional](https://www.autocarpro.in/news-international/uk-moves-closer-to-major-battery-plant-for-electric-cars-42855) | autocarpro.in | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "chemical industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "chemical industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "chemical industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "chemical industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "chemical industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [FMCG Industry](fmcg-industry.md)
- [Steel Industry](steel-industry.md)
- [Music Industry](music-industry.md)
- [Aerospace Industry](aerospace-industry.md)
