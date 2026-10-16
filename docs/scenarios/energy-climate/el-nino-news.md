# El Nino News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “el nino news” · 1,000/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [el-nino-news.json](../../examples/scenarios/el-nino-news.json).

**Question.** How did el nino coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="El Nino"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,697 |
| Negative · neutral · positive | 78% · 2.6% · 19% |
| Critical (priority 7–9) | 91% (1,548 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (798 articles) |
| Most-reported country | India (14% of matches) |
| Strongest theme by lift | climate feedback loops and tipping points |

## Twelve months of coverage

Monthly matching articles for `El Nino` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 215 | 91% | 171 | 43 | █████ |
| Jun 2025 | 132 | 93% | 122 | 10 | ███ |
| Jul 2025 | 177 | 70% | 147 | 30 | ████ |
| Aug 2025 | 263 | 82% | 212 | 44 | ███████ |
| Sep 2025 | 151 | 90% | 124 | 27 | ████ |
| Oct 2025 | 171 | 92% | 156 | 12 | ████ |
| Nov 2025 | 178 | 99% | 170 | 7 | ████ |
| Dec 2025 | 232 | 97% | 218 | 10 | ██████ |
| Jan 2026 | 246 | 95% | 234 | 10 | ██████ |
| Feb 2026 | 245 | 93% | 212 | 26 | ██████ |
| Mar 2026 | 408 | 93% | 330 | 66 | ██████████ |
| Apr 2026 | 798 | 89% | 548 | 224 | ████████████████████ |

The last four complete months averaged 424 articles a month against 197 in the first four (+116%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 236 | 14% |
| United States | 210 | 12% |
| Indonesia | 28 | 1.6% |
| Australia | 25 | 1.5% |
| Malaysia | 22 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| climate feedback loops and tipping points | 52 | 4.5% | +1633% |
| cold war-era proxy conflicts | 179 | 15% | +0% |
| el niño and la niña effects | 247 | 21% | +426% |
| climate change impacts on weather | 312 | 27% | +564% |
| war reparations and post-conflict reconstruction | 180 | 16% | +1% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 13 Apr 2026 | [Super El Nino could bring record heat to Türkiye, experts say - Türkiye Today](https://www.turkiyetoday.com/lifestyle/super-el-nino-could-bring-record-heat-to-turkiye-experts-say-3218001) | turkiyetoday.com | 9 | negative |
| 30 Mar 2026 | [Haze looms as forest fires rage](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/03/30/haze-looms-as-forest-fires-rage) | thestar.com.my | 9 | negative |
| 29 Mar 2026 | [Haze threat looms as Indonesia battles early forest fires ahead of El Nino](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/03/29/haze-threat-looms-as-indonesia-battles-early-forest-fires-ahead-of-el-nino) | thestar.com.my | 9 | negative |
| 27 Mar 2026 | [Malaysia’s rice bowl is thirsting for water as heat bakes in—and El Nino isn’t even here yet](https://asianews.network/malaysias-rice-bowl-is-thirsting-for-water-as-heat-bakes-in-and-el-nino-isnt-even-here-yet/') | asianews.network | 9 | negative |
| 25 Feb 2026 | [Peru declares a state of emergency for hundreds of districts after severe rains and flooding](https://www.yahoo.com/news/articles/peru-declares-state-emergency-hundreds-184421363.html) | yahoo.com | 9 | negative |
| 30 Apr 2026 | [From surplus to strain: World rice supply threatened by Iran war, El Nino](https://www.thehindubusinessline.com/economy/agri-business/from-surplus-to-strain-world-rice-supply-threatened-by-iran-war-el-nino/article70923908.ece) | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [Crossing the Threshold Into El Nino: Historic Values Forecast This Summer, Fall](https://www.dtnpf.com/agriculture/web/AG/blogs/ag-weather-forum/blog-post/2026/04/30/crossing-threshold-el-nino-historic) | dtnpf.com | 8 | negative |
| 30 Apr 2026 | [Padi farmers concerned by heatwave](https://www.thestar.com.my/news/nation/2026/04/30/padi-farmers-concerned-by-heatwave) | thestar.com.my | 8 | positive |
| 29 Apr 2026 | [Global tensions present opportunity for India amid inflationary risks: Finance Ministry](https://www.thehindubusinessline.com/economy/global-tensions-present-opportunity-for-india-amid-inflationary-risks-finance-ministry/article70921018.ece) | thehindubusinessline.com | 8 | positive |
| 28 Apr 2026 | [Why heatwaves are becoming India’s new normal: A deep dive into what’s behind the scorching temperatures -…](https://economictimes.indiatimes.com/news/india/why-heatwaves-are-becoming-indias-new-normal-a-deep-dive-into-whats-behind-the-scorching-temperatures/printarticle/130589745.cms) | economictimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [Why heatwaves are becoming India’s new normal: A deep dive into what’s behind the scorching temperatures](https://economictimes.indiatimes.com/news/india/why-heatwaves-are-becoming-indias-new-normal-a-deep-dive-into-whats-behind-the-scorching-temperatures/articleshow/130589745.cms) | economictimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [Telangana braces for heat, uneven rain as El Nino takes hold](https://www.newindianexpress.com/states/telangana/2026/Apr/28/telangana-braces-for-heat-uneven-rain-as-el-nino-takes-hold) | newindianexpress.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "El Nino" --since 2026-01-01 --until 2026-04-30
prism-news trends "El Nino" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "El Nino" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "El Nino", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "El Nino", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Rare Earths News](rare-earths-news.md)
- [Diesel Price News](diesel-price-news.md)
- [EV Charging News](ev-charging-news.md)
- [Power Grid News](power-grid-news.md)
