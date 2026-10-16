# Carbon Capture News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “carbon capture news” · 10/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [carbon-capture-news.json](../../examples/scenarios/carbon-capture-news.json).

**Question.** How did carbon capture coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="carbon capture"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,569 |
| Negative · neutral · positive | 12% · 0.8% · 88% |
| Critical (priority 7–9) | 86% (1,355 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (524 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | carbon footprint reduction techniques |

## Twelve months of coverage

Monthly matching articles for `carbon capture` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 373 | 85% | 67 | 304 | ██████████████ |
| Jun 2025 | 380 | 84% | 74 | 300 | ███████████████ |
| Jul 2025 | 331 | 82% | 57 | 273 | █████████████ |
| Aug 2025 | 345 | 83% | 56 | 287 | █████████████ |
| Sep 2025 | 376 | 83% | 33 | 337 | ██████████████ |
| Oct 2025 | 451 | 84% | 38 | 405 | █████████████████ |
| Nov 2025 | 392 | 84% | 55 | 332 | ███████████████ |
| Dec 2025 | 343 | 84% | 36 | 303 | █████████████ |
| Jan 2026 | 310 | 83% | 47 | 259 | ████████████ |
| Feb 2026 | 524 | 89% | 52 | 468 | ████████████████████ |
| Mar 2026 | 358 | 85% | 33 | 323 | ██████████████ |
| Apr 2026 | 377 | 87% | 49 | 324 | ██████████████ |

The last four complete months averaged 392 articles a month against 357 in the first four (+10%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 57% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 264 | 17% |
| India | 161 | 10% |
| United Kingdom | 98 | 6.2% |
| Canada | 62 | 4.0% |
| Japan | 32 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| carbon footprint reduction techniques | 300 | 28% | -6% |
| carbon credit systems & renewable incentives | 76 | 7.0% | -12% |
| climate change mitigation strategies | 333 | 31% | -1% |
| green hydrogen production methods | 60 | 5.5% | +11% |
| waste-to-energy conversion technologies | 57 | 5.2% | -22% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Carbon capture platform launched in Nigeria](https://www.gasworld.com/story/carbon-capture-platform-launched-in-nigeria/2247159.article/) | gasworld.com | 8 | positive |
| 17 Apr 2026 | [Pacific declaration urges end to age of fossil fuels](https://thewest.com.au/news/environment/pacific-declaration-urges-end-to-age-of-fossil-fuels-c-22155591) | thewest.com.au | 8 | negative |
| 1 Apr 2026 | [Integrated Electrochemical CO2 Capture with Energy Storage for Renewable Energy Compatibility.](https://pubmed.ncbi.nlm.nih.gov/41860024/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 30 Mar 2026 | [Woodside promises Browse CCS still live amid climate worries](https://thewest.com.au/business/energy/browse-lng-woodside-pledges-carbon-capture-and-storage-still-on-agenda-after-withdrawing-environmental-plans-c-22068815) | thewest.com.au | 8 | positive |
| 21 Mar 2026 | [This Government of urbanites is putting Britain’s food security at risk](https://www.pressreader.com/uk/the-daily-telegraph-saturday/20260321/282016153851579) | pressreader.com | 8 | negative |
| 17 Mar 2026 | [New Era Cleantech to Build Coal Gasification Complex](https://chemindigest.com/new-era-cleantech-to-develop-coal-gasification-complex-in-bhadrawati-maharashtra/) | chemindigest.com | 8 | positive |
| 28 Feb 2026 | [Carbon capture risks leading Indian steel down a technological dead end](https://energy.economictimes.indiatimes.com/news/renewable/carbon-capture-risks-leading-indian-steel-down-a-technological-dead-end/128869052) | energy.economictimes.indiatimes.com | 8 | positive |
| 25 Feb 2026 | [Government hits back after Labour says we know better](https://www.liverpoolecho.co.uk/news/liverpool-news/government-hits-back-after-labour-33491230) | liverpoolecho.co.uk | 8 | negative |
| 19 Feb 2026 | [INEOS awarded €300 million grant by French Government to rejuvenate and decarbonise Lavera site and cut CO2…](https://renewable-carbon.eu/news/ineos-awarded-e300-million-grant-by-french-government-to-rejuvenate-and-decarbonise-lavera-site-and-cut-co2-emissions-by-331000-tonnes-per-annum/) | renewable-carbon.eu | 8 | positive |
| 11 Feb 2026 | [PM Modi highlights how carbon capture can power India's next steel revolution](https://businessnewsthisweek.com/business/pm-modi-highlights-how-carbon-capture-can-power-indias-next-steel-revolution/) | businessnewsthisweek.com | 8 | positive |
| 6 Feb 2026 | [Rs 20,000-crore CCUS push aims to future-proof India’s heavy industry in low-carbon era](https://www.financialexpress.com/business/news/rs-20000-crore-ccus-push-aims-to-future-proof-indias-heavy-industry-in-low-carbon-era/4132683/) | financialexpress.com | 8 | positive |
| 5 Feb 2026 | [Carbon Capture Technology Faces a Difficult Few Years, Finds IDTechEx Research · EMSNow](https://www.emsnow.com/carbon-capture-technology-faces-a-difficult-few-years-finds-idtechex-research/) | emsnow.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "carbon capture" --since 2026-01-01 --until 2026-04-30
prism-news trends "carbon capture" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "carbon capture" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "carbon capture", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "carbon capture", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Wind Turbines Industry](wind-turbines-industry.md)
- [Ethanol Blending News](ethanol-blending-news.md)
- [Deforestation News](deforestation-news.md)
- [Drought News](drought-news.md)
