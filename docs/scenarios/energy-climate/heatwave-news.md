# Heatwave News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “heatwave news” · 480/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [heatwave-news.json](../../examples/scenarios/heatwave-news.json).

**Question.** How did heatwave coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="heatwave"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,902 |
| Negative · neutral · positive | 71% · 5.2% · 23% |
| Critical (priority 7–9) | 60% (1,747 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,834 articles) |
| Most-reported country | India (41% of matches) |
| Strongest theme by lift | extreme weather events |

## Twelve months of coverage

Monthly matching articles for `heatwave` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 554 | 56% | 363 | 170 | ██████ |
| Jun 2025 | 1,696 | 50% | 1,080 | 536 | ██████████████████ |
| Jul 2025 | 1,470 | 52% | 918 | 497 | ████████████████ |
| Aug 2025 | 1,175 | 57% | 754 | 371 | █████████████ |
| Sep 2025 | 141 | 74% | 103 | 36 | ██ |
| Oct 2025 | 89 | 66% | 50 | 33 | █ |
| Nov 2025 | 91 | 75% | 56 | 30 | █ |
| Dec 2025 | 100 | 68% | 72 | 26 | █ |
| Jan 2026 | 353 | 77% | 248 | 99 | ████ |
| Feb 2026 | 131 | 62% | 100 | 23 | █ |
| Mar 2026 | 584 | 65% | 437 | 119 | ██████ |
| Apr 2026 | 1,834 | 55% | 1,282 | 437 | ████████████████████ |

The last four complete months averaged 726 articles a month against 1,224 in the first four (-41%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 65% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 1,193 | 41% |
| Australia | 249 | 8.6% |
| United States | 215 | 7.4% |
| Malaysia | 62 | 2.1% |
| United Kingdom | 28 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| extreme weather events | 469 | 21% | +2506% |
| heatwave advisories | 1,370 | 62% | +2110% |
| seasonal weather trends | 103 | 4.7% | +1960% |
| daily temperature reports | 311 | 14% | +5083% |
| regional weather patterns | 114 | 5.2% | +3700% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [South-east Asia office workers swelter in energy-saving drive, heatwave](http://www.straitstimes.com/asia/se-asia/south-east-asia-office-workers-swelter-in-energy-saving-drive-heatwave) | straitstimes.com | 9 | negative |
| 24 Apr 2026 | [Bangladesh sweats as Middle East fuel shortages force power cuts](http://www.straitstimes.com/asia/south-asia/bangladesh-sweats-as-middle-east-fuel-shortages-force-power-cuts) | straitstimes.com | 9 | negative |
| 22 Apr 2026 | [Almost 30% of Us Face 5x More Heat-Drought Extremes by End of Century](https://www.sciencealert.com/almost-30-of-us-face-5x-more-heat-drought-extremes-by-end-of-century) | sciencealert.com | 9 | negative |
| 14 Apr 2026 | [Australia-Heatwave.](https://www.farminguk.com/news/australia-heatwave-_10888.html) | farminguk.com | 9 | negative |
| 5 Apr 2026 | [Thailand Weather Forecast: Extreme Heat in Bangkok, Light Rain in North and Northeast - Time News](https://time.news/thailand-weather-forecast-extreme-heat-in-bangkok-light-rain-in-north-and-northeast/) | time.news | 9 | negative |
| 31 Mar 2026 | [USA's record-breaking heatwave set to get worse as experts warn climate change threat is 'here'](https://uniladtech.com/news/usa-record-breaking-heatwave-to-get-worse-959497-20260331) | uniladtech.com | 9 | negative |
| 23 Mar 2026 | [Health minister warns of 40°C danger as heatwave scorches Malaysia, claiming life of child left in car](https://www.malaymail.com/news/malaysia/2026/03/23/health-minister-warns-of-40c-danger-as-heatwave-scorches-malaysia-claiming-life-of-child-left-in-car/213549) | malaymail.com | 9 | negative |
| 23 Mar 2026 | [15 heat-related cases this year, including one child death, says Dzulkefly](https://www.thestar.com.my/news/nation/2026/03/23/15-heat-related-cases-this-year-including-one-child-death-says-dzulkefly) ⚠ | thestar.com.my | 9 | negative |
| 23 Mar 2026 | [Dzulkefly: 15-heat-related cases this year, including one child death \| Borneo Post Online](https://www.theborneopost.com/2026/03/23/dzulkefly-15-heat-related-cases-this-year-including-one-child-death/) ⚠ | theborneopost.com | 9 | negative |
| 21 Mar 2026 | [What is a snow drought? Why California’s 'warm snow drought' matters](https://www.usatoday.com/story/news/nation/california/2026/03/21/snow-drought-explained-what-californias-warm-winter-means/89244124007/) | usatoday.com | 9 | negative |
| 17 Mar 2026 | [Historic heat wave in the United States: States that will see record temperatures according to the NWS](https://en.as.com/latest_news/historic-heat-wave-in-the-united-states-states-that-will-see-record-temperatures-according-to-the-nws-f202603-n/) ⚠ | en.as.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "heatwave" --since 2026-01-01 --until 2026-04-30
prism-news trends "heatwave" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "heatwave" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "heatwave", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "heatwave", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Power Outage News](power-outage-news.md)
- [Wind Energy News](wind-energy-news.md)
- [Offshore Wind News](offshore-wind-news.md)
- [Fuel Prices News](fuel-prices-news.md)
