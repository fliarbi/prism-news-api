# Air Quality News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “air quality news” · 70/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [air-quality-news.json](../../examples/scenarios/air-quality-news.json).

**Question.** How did air quality coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="air quality"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,308 |
| Negative · neutral · positive | 61% · 2.3% · 37% |
| Critical (priority 7–9) | 69% (4,364 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (3,324 articles) |
| Most-reported country | India (27% of matches) |
| Strongest theme by lift | air quality and pollution levels |

## Twelve months of coverage

Monthly matching articles for `air quality` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,130 | 51% | 625 | 479 | ███████ |
| Jun 2025 | 1,129 | 60% | 609 | 483 | ███████ |
| Jul 2025 | 1,199 | 59% | 662 | 500 | ███████ |
| Aug 2025 | 1,505 | 65% | 980 | 495 | █████████ |
| Sep 2025 | 998 | 58% | 465 | 496 | ██████ |
| Oct 2025 | 2,114 | 74% | 1,411 | 668 | █████████████ |
| Nov 2025 | 3,324 | 68% | 2,040 | 1,240 | ████████████████████ |
| Dec 2025 | 2,846 | 79% | 2,017 | 777 | █████████████████ |
| Jan 2026 | 1,653 | 74% | 1,103 | 512 | ██████████ |
| Feb 2026 | 1,598 | 68% | 913 | 649 | ██████████ |
| Mar 2026 | 1,356 | 68% | 805 | 513 | ████████ |
| Apr 2026 | 1,701 | 66% | 1,001 | 646 | ██████████ |

The last four complete months averaged 1,577 articles a month against 1,241 in the first four (+27%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 1,731 | 27% |
| United States | 838 | 13% |
| United Kingdom | 85 | 1.4% |
| China | 62 | 1.0% |
| Thailand | 44 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| air quality and pollution levels | 667 | 15% | -56% |
| air quality improvement initiatives | 2,225 | 50% | -46% |
| environmental policy and legislation | 864 | 19% | -7% |
| eco-friendly transportation alternatives | 134 | 3.0% | -5% |
| climate change and public health | 111 | 2.5% | -60% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | ['A nightmare' — Russians in Tuapse in disbelief after Ukrainian drones bring the war home](https://www.yahoo.com/news/articles/nightmare-russians-tuapse-disbelief-ukrainian-132704016.html) | yahoo.com | 9 | negative |
| 22 Apr 2026 | [Report Finds 33 Million US Children Exposed to Harmful Air Pollution Across the Country](https://newsable.asianetnews.com/international/climate-change/report-finds-33-million-us-children-exposed-to-harmful-air-pollution-across-the-country-articleshow-dvpq9ay) | newsable.asianetnews.com | 9 | negative |
| 19 Apr 2026 | [Toxic haze in the North triggers lung risks: expert](https://www.bangkokpost.com/thailand/general/3239455/toxic-haze-in-the-north-triggers-lung-risks-expert) | bangkokpost.com | 9 | negative |
| 1 Apr 2026 | [Northern Thailand chokes on hazardous haze as Pattaya breathes easier for now - Pattaya Mail](https://www.pattayamail.com/news/northern-thailand-chokes-on-hazardous-haze-as-pattaya-breathes-easier-for-now-541504) | pattayamail.com | 9 | negative |
| 1 Apr 2026 | [Mortality impacts of long-term PM2.5 and NO2 exposure in Great Britain under national and international air…](https://pubmed.ncbi.nlm.nih.gov/41960439/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 31 Mar 2026 | [Chiang Mai under a blanket of toxic air as warning signs reach Pattaya - Pattaya Mail](https://www.pattayamail.com/news/chiang-mai-under-a-blanket-of-toxic-air-as-warning-signs-reach-pattaya-541465) | pattayamail.com | 9 | negative |
| 29 Mar 2026 | [Breathing danger: WHO identifies world’s most polluted countries and cleanest nations](https://euroweeklynews.com/2026/03/29/breathing-danger-who-identifies-worlds-most-polluted-countries-and-cleanest-nations/) | euroweeklynews.com | 9 | negative |
| 25 Mar 2026 | [Finland Has Europe’s Cleanest Air, But Pollution Still a Concern \| 2025 Report - Time News](https://time.news/finland-has-europes-cleanest-air-but-pollution-still-a-concern-2025-report/) | time.news | 9 | negative |
| 24 Mar 2026 | [Global air quality worsened in 2025 - Taipei Times](https://www.taipeitimes.com/News/world/archives/2026/03/25/2003854448) | taipeitimes.com | 9 | negative |
| 24 Mar 2026 | [Pakistan Air Pollution: World’s Highest PM2.5 Levels in 2025 - Time News](https://time.news/pakistan-air-pollution-worlds-highest-pm2-5-levels-in-2025/) | time.news | 9 | negative |
| 24 Mar 2026 | [Pakistan ranked world's most polluted country in 2025: IQAir report](https://www.aninews.in/news/world/asia/pakistan-ranked-worlds-most-polluted-country-in-2025-iqair-report20260324141232) | aninews.in | 9 | negative |
| 24 Mar 2026 | [Global air quality worsened in 2025 and poses threat to growth](https://www.businesstimes.com.sg/esg/global-air-quality-worsened-2025-and-poses-threat-growth) | businesstimes.com.sg | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "air quality" --since 2026-01-01 --until 2026-04-30
prism-news trends "air quality" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "air quality" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "air quality", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "air quality", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Green Hydrogen News](green-hydrogen-news.md)
- [Nickel News](nickel-news.md)
- [Pipeline News](pipeline-news.md)
- [Heat Pumps News](heat-pumps-news.md)
