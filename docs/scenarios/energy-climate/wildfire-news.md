# Wildfire News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wildfire news” · 480/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wildfire-news.json](../../examples/scenarios/wildfire-news.json).

**Question.** How did wildfire coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="wildfire"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,364 |
| Negative · neutral · positive | 69% · 0.9% · 30% |
| Critical (priority 7–9) | 78% (4,160 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (2,734 articles) |
| Most-reported country | United States (38% of matches) |
| Strongest theme by lift | extreme weather event preparedness guides |

## Twelve months of coverage

Monthly matching articles for `wildfire` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,259 | 80% | 878 | 358 | █████████ |
| Jun 2025 | 951 | 80% | 685 | 261 | ███████ |
| Jul 2025 | 2,036 | 72% | 1,637 | 386 | ███████████████ |
| Aug 2025 | 2,734 | 80% | 2,247 | 470 | ████████████████████ |
| Sep 2025 | 1,108 | 76% | 807 | 298 | ████████ |
| Oct 2025 | 655 | 76% | 417 | 229 | █████ |
| Nov 2025 | 508 | 78% | 318 | 186 | ████ |
| Dec 2025 | 703 | 79% | 440 | 256 | █████ |
| Jan 2026 | 630 | 78% | 404 | 218 | █████ |
| Feb 2026 | 1,129 | 78% | 772 | 340 | ████████ |
| Mar 2026 | 1,259 | 78% | 839 | 403 | █████████ |
| Apr 2026 | 2,346 | 77% | 1,680 | 639 | █████████████████ |

The last four complete months averaged 1,341 articles a month against 1,745 in the first four (-23%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,046 | 38% |
| Canada | 306 | 5.7% |
| United Kingdom | 67 | 1.2% |
| India | 43 | 0.8% |
| South Korea | 26 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| extreme weather event preparedness guides | 814 | 20% | +196% |
| wildfire containment and aftermath analysis | 2,149 | 52% | +110% |
| natural disaster response and recovery efforts | 740 | 18% | +261% |
| wildfire prevention and management strategies | 62 | 1.5% | -38% |
| severe weather advisories and impact reports | 365 | 8.8% | +564% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Extreme weather and green energy on the rise in Europe](https://www.dw.com/en/extreme-weather-and-green-energy-on-the-rise-in-europe/a-76962870) | dw.com | 9 | negative |
| 28 Apr 2026 | [Rain Brings Relief As Georgia Wildfire Grows, Boosts Containment Efforts](http://religionunplugged.com/news/2026/4/28/rain-brings-relief-as-georgia-wildfire-grows-boosts-containment-efforts) | religionunplugged.com | 9 | negative |
| 28 Apr 2026 | [Rain brings some relief, but massive South Georgia wildfire still grows](https://www.yahoo.com/news/articles/rain-brings-relief-massive-south-025949982.html) | yahoo.com | 9 | negative |
| 27 Apr 2026 | [Japan’s Northeast Battles Fires Amid Climate Strain](https://stratnewsglobal.com/indo-pacific/japan/japans-northeast-battles-fires-amid-climate-strain/) | stratnewsglobal.com | 9 | negative |
| 25 Apr 2026 | [Wildfire continues to burn north of Lexington](https://northplattebulletin.com/crews-battle-wildfire-north-of-lexington/) | northplattebulletin.com | 9 | negative |
| 24 Apr 2026 | [Growing wildfires blamed for death of Florida firefighter, destruction of 120 Georgia homes](https://triblive.com/news/world/growing-wildfires-blamed-for-death-of-florida-firefighter-destruction-of-120-georgia-homes/) | triblive.com | 9 | negative |
| 23 Apr 2026 | [Wildfires continue to spread across South Georgia - Moultrie Observer](https://moultrieobserver.com/2026/04/23/wildfires-continue-to-spread-across-south-georgia/) | moultrieobserver.com | 9 | negative |
| 23 Apr 2026 | [Seeing or smelling smoke in Pender County? Here's why](https://www.starnewsonline.com/story/news/local/2026/04/23/wildfire-burning-in-pender-county-nc-near-whitehall-plantation/89751177007/) | starnewsonline.com | 9 | positive |
| 23 Apr 2026 | ['Doesn't feel real': Evacuees lean on community as fire forces families from Brantley County homes](https://www.yahoo.com/news/articles/doesnt-feel-real-evacuees-lean-035158399.html) | yahoo.com | 9 | negative |
| 23 Apr 2026 | [‘It’s horrible': Brantley County families lose homes as wildfire sweeps through area](https://www.yahoo.com/news/articles/horrible-brantley-county-families-lose-002840806.html) | yahoo.com | 9 | negative |
| 23 Apr 2026 | [Wildfire in Brantley County burns on, leaving some residents without homes](https://www.gpb.org/news/2026/04/23/wildfire-in-brantley-county-burns-on-leaving-some-residents-without-homes) | gpb.org | 9 | negative |
| 22 Apr 2026 | [Wildfire forecast: Here's when California could see increased risk this year](https://abc7.com/post/wildfire-forecast-shows-when-california-could-see-increased-risk-year/18945497/) | abc7.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "wildfire" --since 2026-01-01 --until 2026-04-30
prism-news trends "wildfire" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "wildfire" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "wildfire", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "wildfire", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Renewable Energy News](renewable-energy-news.md)
- [Electric Vehicles News](electric-vehicles-news.md)
- [OPEC News](opec-news.md)
- [Recycling Industry](recycling-industry.md)
