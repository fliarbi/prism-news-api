# Floods News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “floods news” · 3,600/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [floods-news.json](../../examples/scenarios/floods-news.json).

**Question.** How did floods coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="floods"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,637 |
| Negative · neutral · positive | 71% · 2.5% · 27% |
| Critical (priority 7–9) | 81% (5,352 articles) |
| Busiest month, May 2025 – Apr 2026 | Jul 2025 (4,616 articles) |
| Most-reported country | United States (6.3% of matches) |
| Strongest theme by lift | hurricane/cyclone impact studies and preparedness |

## Twelve months of coverage

Monthly matching articles for `floods` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,582 | 81% | 1,189 | 349 | ███████ |
| Jun 2025 | 1,452 | 83% | 1,110 | 308 | ██████ |
| Jul 2025 | 4,616 | 83% | 3,815 | 739 | ████████████████████ |
| Aug 2025 | 4,119 | 87% | 3,306 | 744 | ██████████████████ |
| Sep 2025 | 3,845 | 91% | 2,729 | 1,035 | █████████████████ |
| Oct 2025 | 2,075 | 84% | 1,495 | 511 | █████████ |
| Nov 2025 | 1,741 | 88% | 1,335 | 371 | ████████ |
| Dec 2025 | 1,858 | 92% | 1,411 | 410 | ████████ |
| Jan 2026 | 1,078 | 83% | 756 | 300 | █████ |
| Feb 2026 | 2,306 | 80% | 1,685 | 543 | ██████████ |
| Mar 2026 | 1,384 | 80% | 952 | 402 | ██████ |
| Apr 2026 | 1,869 | 81% | 1,286 | 511 | ████████ |

The last four complete months averaged 1,659 articles a month against 2,942 in the first four (-44%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 28% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 416 | 6.3% |
| Indonesia | 204 | 3.1% |
| India | 183 | 2.8% |
| New Zealand | 93 | 1.4% |
| Australia | 75 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| hurricane/cyclone impact studies and preparedness | 1,271 | 28% | -24% |
| flood mitigation strategies and case studies | 2,301 | 50% | -39% |
| weather-related travel disruptions | 171 | 3.7% | +47% |
| extreme weather events | 373 | 8.1% | -26% |
| flood risk assessments | 759 | 16% | -13% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 19 Apr 2026 | [State of emergency declared in Whanganui district](https://www.nzherald.co.nz/whanganui-chronicle/news/state-of-emergency-declared-in-whanganui-district-with-flooding-forecast-residents-asked-to-prepare-for-evacuation/F2N7XTJPARGNBHFJU3VVDBCUZY/) | nzherald.co.nz | 9 | negative |
| 14 Apr 2026 | [Mozambique - Proposal for a Grant of USD 1,000,000.00 Emergency Relief Assistance Project in Response to the…](https://www.afdb.org/ar/documents/mozambique-proposal-grant-usd-100000000-emergency-relief-assistance-project-response-2026-floods-maputo-gaza-provinces-special-relief-fund-srf) | afdb.org | 9 | negative |
| 7 Apr 2026 | [Pakistan et Afghanistan \| Des intempéries font 188 morts](https://www.lapresse.ca/international/asie-et-oceanie/2026-04-07/pakistan-et-afghanistan/des-intemperies-font-188-morts.php) | lapresse.ca | 9 | negative |
| 6 Apr 2026 | [Nearly 100 Dead In Afghanistan In Storms And Earthquakes](https://independent.ng/nearly-100-dead-in-afghanistan-in-storms-and-earthquakes/) | independent.ng | 9 | negative |
| 4 Apr 2026 | [Floods, landslides triggered by heavy rain in Afghanistan leave 77 dead in 10 days, authorities say](https://www.ajc.com/news/2026/04/floods-landslides-triggered-by-heavy-rain-in-afghanistan-leave-77-dead-in-10-days-authorities-say/) | ajc.com | 9 | negative |
| 24 Mar 2026 | ['Inherent resilience': Hawaii governor praises community as state recovers from historic floods](https://us.headtopics.com/news/inherent-resilience-hawaii-governor-praises-community-as-81408233) | us.headtopics.com | 9 | negative |
| 23 Mar 2026 | [Mass evacuations in Canaries Storm Therese brings MORE misery to isles](https://www.the-sun.com/news/16125403/canaries-floods-landslides-storm-therese-misery-isles-set/) | the-sun.com | 9 | negative |
| 23 Mar 2026 | [Wildfires, Storms, Floods Account for Record 92% of Global Insured Losses: Swiss Re](https://www.insurancejournal.com/news/national/2026/03/23/863087.htm) | insurancejournal.com | 9 | negative |
| 14 Mar 2026 | [Ethiopia declares national mourning as flood death toll rises to 80](https://gulfnews.com/world/africa/ethiopia-declares-national-mourning-as-flood-death-toll-rises-to-80-1.500474045) | gulfnews.com | 9 | negative |
| 9 Mar 2026 | [Unsichtbare Gefahr im Wasser: Behörden in Australien sprechen Warnung aus](https://www.t-online.de/nachrichten/panorama/naturgewalten/id_101160998/australien-warnung-vor-krokodilen-nach-schweren-ueberflutungen.html) | t-online.de | 9 | negative |
| 8 Mar 2026 | [United Nations concerned over devastating floods in Kenya, sends condolence to families who lost love ones -…](https://www.ghanamma.com/2026/03/08/united-nations-concerned-over-devastating-floods-in-kenya-sends-condolence-to-families-who-lost-love-ones/) | ghanamma.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "floods" --since 2026-01-01 --until 2026-04-30
prism-news trends "floods" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "floods" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "floods", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "floods", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Climate Change News](climate-change-news.md)
- [Gas Prices News](gas-prices-news.md)
- [Renewable Energy News](renewable-energy-news.md)
- [Electric Vehicles News](electric-vehicles-news.md)
