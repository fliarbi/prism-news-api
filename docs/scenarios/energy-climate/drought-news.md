# Drought News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drought news” · 70/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [drought-news.json](../../examples/scenarios/drought-news.json).

**Question.** How did drought coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="drought"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,359 |
| Negative · neutral · positive | 56% · 2.9% · 42% |
| Critical (priority 7–9) | 71% (7,379 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,480 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | agricultural weather impacts |

## Twelve months of coverage

Monthly matching articles for `drought` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,384 | 69% | 1,378 | 913 | ███████████ |
| Jun 2025 | 1,658 | 68% | 880 | 731 | ███████ |
| Jul 2025 | 2,301 | 73% | 1,442 | 785 | ██████████ |
| Aug 2025 | 2,921 | 67% | 1,775 | 1,080 | █████████████ |
| Sep 2025 | 2,252 | 63% | 1,296 | 863 | ██████████ |
| Oct 2025 | 1,522 | 67% | 735 | 717 | ███████ |
| Nov 2025 | 1,267 | 73% | 620 | 606 | ██████ |
| Dec 2025 | 1,326 | 75% | 665 | 622 | ██████ |
| Jan 2026 | 1,486 | 75% | 707 | 719 | ███████ |
| Feb 2026 | 2,081 | 73% | 1,122 | 894 | █████████ |
| Mar 2026 | 2,312 | 70% | 1,246 | 990 | ██████████ |
| Apr 2026 | 4,480 | 70% | 2,655 | 1,694 | ████████████████████ |

The last four complete months averaged 2,590 articles a month against 2,316 in the first four (+12%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,670 | 26% |
| India | 377 | 3.6% |
| United Kingdom | 119 | 1.1% |
| Australia | 115 | 1.1% |
| Canada | 102 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agricultural weather impacts | 741 | 10% | +211% |
| drought conditions monitoring | 806 | 11% | +197% |
| climate-resilient crop development | 239 | 3.2% | +96% |
| seasonal weather trends | 222 | 3.0% | +534% |
| historical weather comparisons | 401 | 5.5% | +435% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Wildfires, start of multiple agriculture plantings hindered by drought](https://www.yahoo.com/news/articles/wildfires-start-multiple-agriculture-plantings-183600436.html) | yahoo.com | 9 | negative |
| 28 Apr 2026 | [Large, Drought-Driven Wildfires Forecast For Southern California's Summer](https://patch.com/california/longbeach-ca/large-drought-driven-wildfires-forecast-southern-californias-summer) | patch.com | 9 | negative |
| 28 Apr 2026 | [Late April weather forecast calls for a big shift](https://usatoday.com/story/news/weather/2026/04/28/wildfire-rain-cold-us-forecast/89833014007/) | usatoday.com | 9 | negative |
| 27 Apr 2026 | [Why the Southeast is burning. Extreme drought is only part of the reason.](https://www.ajc.com/opinion/2026/04/why-the-southeast-is-burning-extreme-drought-is-only-part-of-the-reason/) | ajc.com | 9 | negative |
| 27 Apr 2026 | [Much-needed rain targets the South, yet worst drought zones will miss out](https://www.aol.com/news/much-needed-rain-targets-south-104144695.html) | aol.com | 9 | negative |
| 24 Apr 2026 | [Somalia Drought Displaces 62,000 in 2025](https://www.newkerala.com/news/a/62000-displaced-somalia-due-drought-iom-644.htm) | newkerala.com | 9 | negative |
| 24 Apr 2026 | [Hot, dry and hurricane-scarred: How climate change fueled wildfires in Georgia and Florida](https://www.yahoo.com/news/articles/hot-dry-hurricane-scarred-climate-180041725.html) | yahoo.com | 9 | negative |
| 24 Apr 2026 | [Wildfires rage in Georgia, Florida; homes burn, evacuations ordered](https://www.usatoday.com/story/news/nation/2026/04/24/wildfires-georgia-florida-south-evacuations-updates/89771147007/) | usatoday.com | 9 | negative |
| 24 Apr 2026 | [Wildfires Destroy 50 Georgia Homes Amid Severe Drought](https://world.infonasional.com/georgia-wildfires-destroy-homes-drought) | world.infonasional.com | 9 | negative |
| 23 Apr 2026 | [Wildfires rage across Georgia and northern Florida amid severe drought](https://www.yahoo.com/news/articles/wildfires-rage-across-georgia-northern-183756353.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "drought" --since 2026-01-01 --until 2026-04-30
prism-news trends "drought" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "drought" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "drought", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "drought", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Carbon Capture News](carbon-capture-news.md)
- [Deforestation News](deforestation-news.md)
- [Glacier News](glacier-news.md)
- [Circular Economy News](circular-economy-news.md)
