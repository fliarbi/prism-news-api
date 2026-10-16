# Climate Change News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “climate change news” · 590/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [climate-change-news.json](../../examples/scenarios/climate-change-news.json).

**Question.** How did climate change coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="climate change"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 117,428 |
| Negative · neutral · positive | 49% · 3.8% · 47% |
| Critical (priority 7–9) | 64% (75,653 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (37,144 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | sustainable construction materials and practices |

## Twelve months of coverage

Monthly matching articles for `climate change` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 23,983 | 65% | 11,196 | 11,562 | █████████████ |
| Jun 2025 | 20,201 | 66% | 9,125 | 10,317 | ███████████ |
| Jul 2025 | 26,509 | 64% | 13,220 | 12,392 | ██████████████ |
| Aug 2025 | 25,015 | 64% | 13,018 | 10,864 | █████████████ |
| Sep 2025 | 23,188 | 70% | 10,046 | 12,266 | ████████████ |
| Oct 2025 | 22,766 | 70% | 10,010 | 11,916 | ████████████ |
| Nov 2025 | 26,801 | 69% | 12,334 | 13,342 | ██████████████ |
| Dec 2025 | 22,801 | 69% | 10,923 | 11,050 | ████████████ |
| Jan 2026 | 24,493 | 67% | 12,363 | 11,261 | █████████████ |
| Feb 2026 | 27,806 | 66% | 13,791 | 12,991 | ███████████████ |
| Mar 2026 | 27,985 | 64% | 13,331 | 13,458 | ███████████████ |
| Apr 2026 | 37,144 | 62% | 17,738 | 17,813 | ████████████████████ |

The last four complete months averaged 29,357 articles a month against 23,927 in the first four (+23%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 40% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 18,979 | 16% |
| India | 6,882 | 5.9% |
| United Kingdom | 2,739 | 2.3% |
| Canada | 1,866 | 1.6% |
| Australia | 1,658 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| sustainable construction materials and practices | 2,407 | 3.0% | +266% |
| winter weather preparedness | 3,707 | 4.5% | +93% |
| green building certifications and standards | 2,332 | 2.9% | +283% |
| energy-efficient home solutions | 2,074 | 2.5% | +69% |
| indoor air quality management in buildings | 2,061 | 2.5% | +431% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Europe is the world’s fastest-warming continent](https://intellinews.com/europe-is-the-world-s-fastest-warming-continent-440388/) | intellinews.com | 9 | negative |
| 30 Apr 2026 | [Warming warnings as Europe reviews climate laws](https://www.prmoment.com/esg/warming-warnings-as-europe-reviews-climate-laws) | prmoment.com | 9 | negative |
| 29 Apr 2026 | [Europe is the world’s fastest-warming continent, twice as fast as global average says UN-backed study \|…](https://www.livemint.com/news/world/europe-is-the-world-s-fastest-warming-continent-twice-as-fast-as-global-average-wmo-copernicus-study-11777462103343.html) | livemint.com | 9 | negative |
| 29 Apr 2026 | [Europa: Rekordjahr 2025! Klimawandel bringt Dürren, Hitze, Waldbrände](https://www.rtl.de/news/europa-rekordjahr-2025-klimawandel-bringt-duerren-hitze-waldbraende-id30767095.html) | rtl.de | 9 | negative |
| 29 Apr 2026 | [Nearly all of Europe had above-average heat last year, as climate records toppled - BusinessWorld Online](https://bworldonline.com/world/2026/04/29/746376/nearly-all-of-europe-had-above-average-heat-last-year-as-climate-records-toppled/) | bworldonline.com | 9 | negative |
| 29 Apr 2026 | [Europe named fastest-warming continent in latest climate change report - IndiaVision India News & Information](https://www.indiavision.com/international/europe-named-fastest-warming-continent-in-latest-climate-change-report/602107/) | indiavision.com | 9 | negative |
| 29 Apr 2026 | [Klimabericht: Fast ganz Europa erlebte 2025 Extremwetter](https://www.moneycab.com/klima-umwelt/klimabericht-fast-ganz-europa-erlebte-2025-extremwetter/) | moneycab.com | 9 | negative |
| 29 Apr 2026 | [Hitze, Eisschmelze, Meereserwärmung: 2025 war ein Jahr der Extreme in Europa](https://www.abendblatt.de/panorama/article411848880/hitze-eisschmelze-meereserwaermung-2025-war-ein-jahr-der-extreme-in-europa.html) | abendblatt.de | 9 | negative |
| 29 Apr 2026 | [Nearly all of Europe had above-average heat last year, as climate records toppled](https://rnz.co.nz/news/world/593723/nearly-all-of-europe-had-above-average-heat-last-year-as-climate-records-toppled) | rnz.co.nz | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "climate change" --since 2026-01-01 --until 2026-04-30
prism-news trends "climate change" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "climate change" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "climate change", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "climate change", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cyclone News](cyclone-news.md)
- [Monsoon News](monsoon-news.md)
- [Gas Prices News](gas-prices-news.md)
- [Floods News](floods-news.md)
