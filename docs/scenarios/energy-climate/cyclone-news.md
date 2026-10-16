# Cyclone News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cyclone news” · 8,100/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cyclone-news.json](../../examples/scenarios/cyclone-news.json).

**Question.** How did cyclone coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="cyclone"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,976 |
| Negative · neutral · positive | 58% · 6.0% · 36% |
| Critical (priority 7–9) | 72% (2,848 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (1,917 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | weather-related travel disruptions |

## Twelve months of coverage

Monthly matching articles for `cyclone` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 562 | 56% | 331 | 188 | ██████ |
| Jun 2025 | 438 | 57% | 227 | 175 | █████ |
| Jul 2025 | 507 | 51% | 268 | 214 | █████ |
| Aug 2025 | 848 | 46% | 406 | 395 | █████████ |
| Sep 2025 | 594 | 68% | 388 | 145 | ██████ |
| Oct 2025 | 1,917 | 80% | 1,481 | 364 | ████████████████████ |
| Nov 2025 | 1,481 | 84% | 1,145 | 267 | ███████████████ |
| Dec 2025 | 1,376 | 82% | 927 | 405 | ██████████████ |
| Jan 2026 | 622 | 72% | 351 | 227 | ██████ |
| Feb 2026 | 776 | 75% | 485 | 243 | ████████ |
| Mar 2026 | 1,126 | 69% | 637 | 425 | ████████████ |
| Apr 2026 | 1,452 | 71% | 836 | 523 | ███████████████ |

The last four complete months averaged 994 articles a month against 589 in the first four (+69%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 631 | 16% |
| Australia | 571 | 14% |
| New Zealand | 387 | 9.7% |
| Sri Lanka | 119 | 3.0% |
| India | 111 | 2.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| weather-related travel disruptions | 352 | 11% | +136% |
| extreme weather events | 631 | 20% | -20% |
| hurricane and typhoon tracking | 759 | 25% | -44% |
| tornado and cyclone reports | 438 | 14% | -22% |
| hurricane/cyclone impact studies and preparedness | 814 | 26% | -30% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 11 Apr 2026 | [New Zealand braces for Cyclone Vaianu, North Island evacuations ordered](https://www.thestar.com.my/news/world/2026/04/11/new-zealand-braces-for-cyclone-vaianu-north-island-evacuations-ordered) | thestar.com.my | 9 | negative |
| 11 Apr 2026 | [New Zealand’s North Island braces for Cyclone Vaianu with thousands ordered to evacuate](https://www.theguardian.com/world/2026/apr/11/new-zealands-north-island-braces-for-cyclone-vaianu-with-thousands-ordered-to-evacuate) | theguardian.com | 9 | negative |
| 7 Apr 2026 | [Cyclone Vaianu moves away from Fiji, but heavy rain warning remains in force](http://www.radionz.co.nz/international/pacific-news/591750/cyclone-vaianu-moves-away-from-fiji-but-heavy-rain-warning-remains-in-force) | radionz.co.nz | 9 | negative |
| 19 Mar 2026 | [Qld and NT brace for Tropical Cyclone Narelle - ABC listen](https://www.abc.net.au/listen/programs/pm/qld-and-nt-brace-for-tropical-cyclone-narelle-/106475298) | abc.net.au | 9 | negative |
| 26 Feb 2026 | [Cyclone Gabrielle inquest: Wives of volunteer firefighters proud of their work](https://www.radionz.co.nz/news/national/588049/cyclone-gabrielle-inquest-wives-of-volunteer-firefighters-proud-of-their-work) | radionz.co.nz | 9 | negative |
| 14 Feb 2026 | [Dozens killed and thousands displaced as powerful cyclone rips through nation: 'It looks like a catastrophic…](https://www.yahoo.com/news/articles/dozens-killed-thousands-displaced-powerful-010000421.html) | yahoo.com | 9 | negative |
| 12 Jan 2026 | [Flood warning as ex-cyclone wreaks havoc on far north](http://www.sbs.com.au/nitv/article/flood-warning-as-ex-cyclone-wreaks-havoc-on-far-north/5zviu7wda) | sbs.com.au | 9 | negative |
| 29 Apr 2026 | [Calls for Early NPF Withdrawals Following Cyclone Damage - Solomon Star News](https://www.solomonstarnews.com/calls-for-early-npf-withdrawals-following-cyclone-damage/) | solomonstarnews.com | 8 | positive |
| 16 Apr 2026 | [Man dead in Logan County motorcycle crash - WV MetroNews](https://wvmetronews.com/2026/04/16/one-dead-in-logan-county-motorcycle-crash/) | wvmetronews.com | 8 | negative |
| 16 Apr 2026 | [A safer home: Two cyclone-smashed marae given $27m to rebuild in new location](https://www.nzherald.co.nz/nz/tangoio-and-petane-marae-to-be-rebuilt-on-safer-hawkes-bay-sites-with-government-funding/Q5GHCNEN4BEH5OY3IQB3RZREGU/) | nzherald.co.nz | 8 | positive |
| 12 Apr 2026 | ['Most dangerous period': Conditions deteriorate as Cyclone Vaianu makes landfall](https://www.nzherald.co.nz/nz/cyclone-vaianu-live-updates-rare-red-wind-warnings-in-force-with-cyclone-set-to-make-landfall-today/HXNDWMWBNND57CV476XROHB5JI/) | nzherald.co.nz | 8 | positive |
| 11 Apr 2026 | [Neuseeland bereitet sich mit Evakuierungen auf Zyklon "Vaianu" vor](https://www.tagesschau.de/ausland/ozeanien/neuseeland-zyklon-102.html) | tagesschau.de | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cyclone" --since 2026-01-01 --until 2026-04-30
prism-news trends "cyclone" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cyclone" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cyclone", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cyclone", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Petrol Price News](petrol-price-news.md)
- [Coal Industry](coal-industry.md)
- [Monsoon News](monsoon-news.md)
- [Climate Change News](climate-change-news.md)
