# Climate Policy News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “climate policy news” · 10/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [climate-policy-news.json](../../examples/scenarios/climate-policy-news.json).

**Question.** How did coverage of climate policy develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="climate policy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,403 |
| Negative · neutral · positive | 59% · 1.8% · 39% |
| Critical (priority 7–9) | 79% (1,898 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (937 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | carbon footprint reduction techniques |

## Twelve months of coverage

Monthly matching articles for `climate policy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 428 | 70% | 218 | 179 | █████████ |
| Jun 2025 | 330 | 75% | 169 | 152 | ███████ |
| Jul 2025 | 669 | 71% | 365 | 278 | ██████████████ |
| Aug 2025 | 334 | 74% | 180 | 144 | ███████ |
| Sep 2025 | 539 | 80% | 340 | 185 | ████████████ |
| Oct 2025 | 503 | 79% | 253 | 236 | ███████████ |
| Nov 2025 | 937 | 78% | 493 | 419 | ████████████████████ |
| Dec 2025 | 437 | 86% | 224 | 202 | █████████ |
| Jan 2026 | 448 | 83% | 258 | 181 | ██████████ |
| Feb 2026 | 794 | 82% | 501 | 277 | █████████████████ |
| Mar 2026 | 551 | 76% | 304 | 237 | ████████████ |
| Apr 2026 | 610 | 75% | 351 | 250 | █████████████ |

The last four complete months averaged 601 articles a month against 440 in the first four (+36%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 466 | 19% |
| Canada | 54 | 2.2% |
| China | 47 | 2.0% |
| United Kingdom | 40 | 1.7% |
| Germany | 38 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| carbon footprint reduction techniques | 329 | 18% | +34% |
| climate change mitigation strategies | 638 | 34% | +5% |
| renewable energy policy & regulation | 80 | 4.3% | +110% |
| renewable energy sources and technologies | 261 | 14% | +7% |
| energy-efficient home solutions | 76 | 4.0% | +192% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 7 Apr 2026 | [Studie: Menschgemachte Treibhausgase verstärken gleichzeitige Hitzewellen und Dürren](http://www.n-tv.de/ticker/Studie-Menschgemachte-Treibhausgase-verstaerken-gleichzeitige-Hitzewellen-und-Duerren-id30689037.html) | n-tv.de | 9 | negative |
| 29 Apr 2026 | [US pressure puts World Bank’s climate plan at risk - Climate and Capital Media](https://www.climateandcapitalmedia.com/us-pressure-puts-world-banks-climate-plan-at-risk/) | climateandcapitalmedia.com | 8 | positive |
| 28 Apr 2026 | [Protesters halt NatWest shareholder meeting as boss defends climate policy](https://www.irishnews.com/news/uk/protesters-halt-natwest-shareholder-meeting-as-boss-defends-climate-policy-XEH6XQYZ6RIJDC26G652YWAA2A/) | irishnews.com | 8 | negative |
| 20 Apr 2026 | [Geopolitics and climate cooperation for a world in flux](https://www.e3g.org/news/geopolitics-and-climate-cooperation-for-a-world-in-flux/) | e3g.org | 8 | negative |
| 16 Apr 2026 | [US pressure puts World Bank's climate plan at risk](https://www.climatechangenews.com/2026/04/16/us-pressure-puts-world-banks-climate-plan-at-risk/) | climatechangenews.com | 8 | positive |
| 15 Apr 2026 | [CCC releases detailed plan to reach UK net zero target](https://www.thechemicalengineer.com/news/ccc-releases-detailed-plan-to-reach-uk-net-zero-target/) | thechemicalengineer.com | 8 | positive |
| 13 Apr 2026 | [With a very ambitious climate policy, the transport sector can be transformed in the long term from the…](https://www.cleanenergywire.org/news/car-toll-higher-co2-price-better-public-transport-help-reach-sectors-climate-targets-report) | cleanenergywire.org | 8 | negative |
| 13 Apr 2026 | [The pressure on Germany's grand coalition government to come up with effective energy and climate policy is…](http://www.cleanenergywire.org/news/german-government-enters-crunch-time-climate-challenge) | cleanenergywire.org | 8 | negative |
| 11 Apr 2026 | [India Moves to End New HFC Production Clearances - Current Affairs Usthadian Academy](https://www.usthadian.com/india-moves-to-end-new-hfc-production-clearances/) | usthadian.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "climate policy" --since 2026-01-01 --until 2026-04-30
prism-news trends "climate policy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "climate policy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "climate policy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "climate policy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Labour Law News](labour-law-news.md)
- [National Security News](national-security-news.md)
- [Make in India News](make-in-india-news.md)
- [Sanctions News](sanctions-news.md)
