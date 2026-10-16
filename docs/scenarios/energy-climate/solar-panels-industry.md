# Solar Panels Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “solar panels industry” · 480/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [solar-panels-industry.json](../../examples/scenarios/solar-panels-industry.json).

**Question.** How did solar panels coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="solar panels"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,674 |
| Negative · neutral · positive | 22% · 0.9% · 77% |
| Critical (priority 7–9) | 60% (2,807 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,434 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | solar photovoltaic (pv) energy systems |

## Twelve months of coverage

Monthly matching articles for `solar panels` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 836 | 56% | 158 | 675 | ████████████ |
| Jun 2025 | 844 | 54% | 99 | 736 | ████████████ |
| Jul 2025 | 1,019 | 54% | 173 | 836 | ██████████████ |
| Aug 2025 | 1,189 | 53% | 245 | 937 | █████████████████ |
| Sep 2025 | 956 | 59% | 171 | 778 | █████████████ |
| Oct 2025 | 969 | 60% | 125 | 837 | ██████████████ |
| Nov 2025 | 840 | 59% | 132 | 704 | ████████████ |
| Dec 2025 | 820 | 56% | 129 | 685 | ███████████ |
| Jan 2026 | 916 | 63% | 147 | 762 | █████████████ |
| Feb 2026 | 1,061 | 61% | 225 | 828 | ███████████████ |
| Mar 2026 | 1,263 | 62% | 351 | 902 | ██████████████████ |
| Apr 2026 | 1,434 | 56% | 295 | 1,120 | ████████████████████ |

The last four complete months averaged 1,168 articles a month against 972 in the first four (+20%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 851 | 18% |
| United Kingdom | 316 | 6.8% |
| India | 201 | 4.3% |
| China | 158 | 3.4% |
| Australia | 95 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| solar photovoltaic (pv) energy systems | 1,616 | 49% | +37% |
| solar panel recycling & waste management | 342 | 10% | +28% |
| community solar & shared renewable projects | 515 | 16% | +60% |
| perovskite solar cell innovations | 174 | 5.3% | +44% |
| renewable energy policy & regulation | 156 | 4.8% | +129% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 5 Feb 2026 | [Polizeihund deckt Millionenverbrechen mit Solarpaneelen auf: Mutter in Haft](https://www.t-online.de/nachrichten/panorama/kriminalitaet/id_101116148/hoexter-polizeihund-deckt-millionenverbrechen-auf.html) | t-online.de | 9 | negative |
| 30 Apr 2026 | [India’s Dependence on Mineral Imports Threatens Clean Energy Security: IEEFA Report - India Seatrade News](https://indiaseatradenews.com/indias-dependence-on-mineral-imports-threatens-clean-energy-security-ieefa-report/) | indiaseatradenews.com | 8 | positive |
| 28 Apr 2026 | [Israeli soldiers smash solar panels with diggers in Christian village](https://www.yahoo.com/news/articles/israeli-soldiers-smash-solar-panels-130243064.html) | yahoo.com | 8 | negative |
| 27 Apr 2026 | [Israeli military destroys solar panels in south Lebanon village \| The National](https://www.thenational.ae/news/mena/2026/04/27/footage-shows-israeli-military-destroying-solar-panels-in-south-lebanon-village/) | thenational.ae | 8 | negative |
| 26 Apr 2026 | [Renewable energy will boost national security and protect UK from sabotage, minister says](https://www.inkl.com/news/renewable-energy-will-boost-national-security-and-protect-uk-from-sabotage-minister-says) | inkl.com | 8 | negative |
| 26 Apr 2026 | [IDF probes soldiers seen damaging solar panels in south Lebanon Christian village](https://www.timesofisrael.com/idf-probes-soldiers-seen-damaging-solar-panels-in-south-lebanon-christian-village/) | timesofisrael.com | 8 | negative |
| 26 Apr 2026 | [IDF probes video showing soldiers destroying solar panels in Christian-Lebanese village](https://www.yahoo.com/news/articles/idf-probes-video-showing-soldiers-004006667.html) | yahoo.com | 8 | negative |
| 25 Apr 2026 | [Miliband branded 'king of hypocrisy' for not having solar panels at £1.6m home](https://www.thesun.co.uk/news/38929437/hypocrisy-ed-miliband-no-solar-panels-house/) | thesun.co.uk | 8 | negative |
| 24 Apr 2026 | [Indonesia accelerates 100 GW solar program amid US tariffs](https://en.antaranews.com/news/413519/indonesia-accelerates-100-gw-solar-program-amid-us-tariffs) | en.antaranews.com | 8 | positive |
| 23 Apr 2026 | [Did Lagos Order All Solar Users to Obtain Permit? Here’s What Government Clarified - Tech \| Business \| Economy](https://techeconomy.ng/did-lagos-order-all-solar-users-to-obtain-permit-heres-what-government-clarified/) | techeconomy.ng | 8 | positive |
| 15 Apr 2026 | [Attention: UK Bans Fuel Gas in New Building from 2028 - SPRSUN](https://sprsunheatpump.com/attention-uk-bans-fuel-gas-in-new-building-from-2028.html) | sprsunheatpump.com | 8 | positive |
| 11 Apr 2026 | [PM Surya Ghar Yojna: Objectives, Eligibility, Apply Online, Benefits and Latest Update](https://www.jagranjosh.com/general-knowledge/pm-surya-ghar-muft-bijli-yojna-objectives-eligibility-apply-online-benefits-1820007753-1) | jagranjosh.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "solar panels" --since 2026-01-01 --until 2026-04-30
prism-news trends "solar panels" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "solar panels" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "solar panels", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "solar panels", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Power Grid News](power-grid-news.md)
- [Uranium News](uranium-news.md)
- [Fusion Energy News](fusion-energy-news.md)
- [Solar Energy News](solar-energy-news.md)
