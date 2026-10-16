# Shipbuilding Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “shipbuilding industry” · 4,400/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [shipbuilding-industry.json](../../examples/scenarios/shipbuilding-industry.json).

**Question.** How much news did the shipbuilding industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="shipbuilding industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 189 |
| Negative · neutral · positive | 26% · 4.2% · 69% |
| Critical (priority 7–9) | 71% (135 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (59 articles) |
| Most-reported country | United States (22% of matches) |
| Strongest theme by lift | shipbuilding and dry dock maintenance |

## Twelve months of coverage

Monthly matching articles for `shipbuilding industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 40 | 68% | 7 | 30 | ██████████████ |
| Jun 2025 | 34 | 62% | 9 | 25 | ████████████ |
| Jul 2025 | 42 | 83% | 7 | 33 | ██████████████ |
| Aug 2025 | 59 | 83% | 9 | 47 | ████████████████████ |
| Sep 2025 | 59 | 81% | 12 | 46 | ████████████████████ |
| Oct 2025 | 49 | 69% | 15 | 34 | █████████████████ |
| Nov 2025 | 52 | 62% | 12 | 39 | ██████████████████ |
| Dec 2025 | 31 | 71% | 4 | 27 | ███████████ |
| Jan 2026 | 41 | 68% | 6 | 35 | ██████████████ |
| Feb 2026 | 56 | 77% | 16 | 38 | ███████████████████ |
| Mar 2026 | 37 | 68% | 12 | 24 | █████████████ |
| Apr 2026 | 55 | 71% | 16 | 34 | ███████████████████ |

The last four complete months averaged 47 articles a month against 44 in the first four (+8%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 41 | 22% |
| China | 32 | 17% |
| Singapore | 6 | 3.2% |
| South Korea | 6 | 3.2% |
| India | 5 | 2.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| shipbuilding and dry dock maintenance | 52 | 36% | +40% |
| maritime economic impact studies | 14 | 9.7% | +100% |
| lng (liquefied natural gas) carrier technology | 20 | 14% | +186% |
| maritime fuel efficiency and emission reduction | 8 | 5.6% | +33% |
| green shipping initiatives and sustainability | 8 | 5.6% | +0% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Feb 2026 | [Expectations are growing in the global shipbuilding industry for a “second Qatar boom.” Qatar, which has…](https://www.hellenicshippingnews.com/second-qatar-lng-boom-spurs-korea-china-shipbuilding-showdown-2/) | hellenicshippingnews.com | 8 | positive |
| 7 Apr 2026 | [Jones Act Parts Dataset: Where Ships Really Come From: News Article - Independent Institute](https://www.independent.org/article/2026/04/07/jones-act-parts-dataset-where-ships-really-come-from/) | independent.org | 7 | negative |
| 19 Mar 2026 | [South Korea’s Justice Ministry said Wednesday it plans to revise visa policies to attract more skilled…](https://www.hellenicshippingnews.com/seoul-looks-to-skilled-migrant-labor-to-ease-shipyard-labor-shortages/) | hellenicshippingnews.com | 7 | negative |
| 13 Mar 2026 | [Samsung Heavy Industries opens San Diego research center to support U.S.-Korea MASGA initiative](https://koreajoongangdaily.joins.com/news/2026-03-13/business/industry/Samsung-Heavy-Industries-opens-San-Diego-research-center-to-support-USKorea-MASGA-initiative/2544155) | koreajoongangdaily.joins.com | 7 | positive |
| 2 Mar 2026 | [Rheinmetall Aktie: Überwasserschiffbau-Ära beginnt](https://www.boerse-express.com/news/articles/rheinmetall-aktie-ueberwasserschiffbau-aera-beginnt-871514) | boerse-express.com | 7 | positive |
| 24 Feb 2026 | [SDHI Revives and Nears Completion of Five Offshore Support Vessels - India Seatrade News](https://indiaseatradenews.com/sdhi-revives-and-nears-completion-of-five-offshore-support-vessels/) | indiaseatradenews.com | 7 | positive |
| 19 Feb 2026 | [Krakatau Steel anticipates double-digit growth on shipbuilding demand - Companies - The Jakarta Post](http://www.thejakartapost.com/business/2026/02/19/krakatau-steel-anticipates-double-digit-growth-on-shipbuilding-demand.html) | thejakartapost.com | 7 | positive |
| 16 Feb 2026 | [Revitalization of Shipbuilding Industry: Counter Chinese, S. Korean Competitors through Technological…](https://japannews.yomiuri.co.jp/editorial/yomiuri-editorial/20260216-311699/) | japannews.yomiuri.co.jp | 7 | positive |
| 1 Feb 2026 | [China Holds 66.8 % of Global Orderbook as Shipping Demand Soars - India Seatrade News](https://indiaseatradenews.com/china-holds-66-8-of-global-orderbook-as-shipping-demand-soars/) | indiaseatradenews.com | 7 | positive |
| 29 Jan 2026 | [Shipbuilders put 3D printed parts on a US aircraft carrier and submarine. The Navy liked the results.](https://www.yahoo.com/news/articles/shipbuilders-put-3d-printed-parts-101301134.html) | yahoo.com | 7 | positive |
| 22 Jan 2026 | [- Cyprus Shipping News](https://cyprusshippingnews.com/2026/01/22/korea-and-japan-race-to-lead-liquefied-hydrogen-carriers/) | cyprusshippingnews.com | 7 | positive |
| 20 Jan 2026 | [The US Navy Has Ambitious Plans. Shipbuilders Must Catch Up.](https://www.bcg.com/publications/2026/the-us-navy-has-big-plans-shipbuilders-much-catch-up) | bcg.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "shipbuilding industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "shipbuilding industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "shipbuilding industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "shipbuilding industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "shipbuilding industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Restaurant Industry](restaurant-industry.md)
- [Semiconductor Industry News](semiconductor-industry-news.md)
- [Hospitality Industry](hospitality-industry.md)
- [Film Industry](film-industry.md)
