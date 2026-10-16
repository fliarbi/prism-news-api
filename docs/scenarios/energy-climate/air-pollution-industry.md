# Air Pollution Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “air pollution industry” · 480/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [air-pollution-industry.json](../../examples/scenarios/air-pollution-industry.json).

**Question.** How did air pollution coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="air pollution"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,888 |
| Negative · neutral · positive | 65% · 2.2% · 33% |
| Critical (priority 7–9) | 86% (3,359 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (1,816 articles) |
| Most-reported country | India (21% of matches) |
| Strongest theme by lift | air quality improvement initiatives |

## Twelve months of coverage

Monthly matching articles for `air pollution` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 637 | 82% | 354 | 266 | ███████ |
| Jun 2025 | 707 | 82% | 427 | 261 | ████████ |
| Jul 2025 | 780 | 76% | 505 | 252 | █████████ |
| Aug 2025 | 754 | 77% | 478 | 258 | ████████ |
| Sep 2025 | 691 | 84% | 365 | 304 | ████████ |
| Oct 2025 | 1,242 | 83% | 804 | 416 | ██████████████ |
| Nov 2025 | 1,590 | 86% | 1,136 | 428 | ██████████████████ |
| Dec 2025 | 1,816 | 87% | 1,303 | 468 | ████████████████████ |
| Jan 2026 | 1,165 | 88% | 770 | 360 | █████████████ |
| Feb 2026 | 948 | 85% | 558 | 371 | ██████████ |
| Mar 2026 | 852 | 85% | 575 | 252 | █████████ |
| Apr 2026 | 923 | 87% | 609 | 300 | ██████████ |

The last four complete months averaged 972 articles a month against 720 in the first four (+35%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 831 | 21% |
| United States | 484 | 12% |
| China | 67 | 1.7% |
| United Kingdom | 45 | 1.2% |
| Thailand | 30 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| air quality improvement initiatives | 1,758 | 61% | -32% |
| environmental policy and legislation | 723 | 25% | +14% |
| eco-friendly transportation alternatives | 151 | 5.2% | +8% |
| air quality and pollution levels | 108 | 3.7% | -63% |
| climate change and public health | 76 | 2.6% | -50% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Pollution de l'air : 46 % des enfants américains menacés - Nouvelles Du Monde](https://www.nouvelles-du-monde.com/pollution-de-lair-46-des-enfants-americains-menaces/) | nouvelles-du-monde.com | 9 | negative |
| 22 Apr 2026 | [2026 State of the Air report: 46% of pediatric population breathe polluted, unhealthy air](https://healio.com/news/pulmonology/20260422/2026-state-of-the-air-report-46-of-pediatric-population-breathe-polluted-unhealthy-air) | healio.com | 9 | negative |
| 18 Apr 2026 | [Smogkrise in Chiang Mai verschärft sich: Waldbrände treiben Luftverschmutzung auf gefährliche Werte –…](https://www.pattayamail.com/pattayablatt/smogkrise-in-chiang-mai-verscharft-sich-waldbrande-treiben-luftverschmutzung-auf-gefahrliche-werte-pattaya-bleibt-unter-klarem-himmel-544582) | pattayamail.com | 9 | negative |
| 31 Mar 2026 | [Blazes cloak northern Thailand in hazardous air pollution](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/03/31/blazes-cloak-northern-thailand-in-hazardous-air-pollution) | thestar.com.my | 9 | negative |
| 29 Mar 2026 | [Is India's Air And Water Pollution Out of Control? Here's What Recent Reports Imply](https://www.etvbharat.com/en/opinion/is-india-air-and-water-pollution-out-of-control-what-do-recent-reports-imply-enn26032903699) | etvbharat.com | 9 | negative |
| 29 Mar 2026 | [Nur 13 Länder haben sichere Luft – die Schweiz nicht](https://www.20min.ch/story/iqair-bericht-nur-13-laender-weltweit-mit-sicherer-luftqualitaet-103536027) | 20min.ch | 9 | negative |
| 27 Mar 2026 | [Chiang Mai tops global pollution rankings as smog from forest fires pushes PM2.5 to hazardous levels -…](https://www.pattayamail.com/thailandnews/chiang-mai-tops-global-pollution-rankings-as-smog-from-forest-fires-pushes-pm2-5-to-hazardous-levels-540861) | pattayamail.com | 9 | negative |
| 27 Mar 2026 | [Chiang Mai tops PM2.5 list](https://www.bangkokpost.com/thailand/general/3225749/chiang-mai-tops-pm25-list) | bangkokpost.com | 9 | negative |
| 26 Mar 2026 | [Top 10 most and least polluted countries in the world 2025-26: Where does India stand?](https://indianexpress.com/article/trending/top-10-listing/iqair-most-and-least-polluted-countries-in-the-world-2026-10602213/) | indianexpress.com | 9 | negative |
| 24 Mar 2026 | [Top-10 Polluted Countries in the World as of Now, Check the List](https://currentaffairs.adda247.com/top-10-polluted-countries-in-the-world-as-of-now/) | currentaffairs.adda247.com | 9 | negative |
| 23 Mar 2026 | [When it's hot and polluted, suicide numbers climb, University of Utah study finds](http://www.ksl.com/article/51467868/when-its-hot-and-polluted-suicide-numbers-climb-university-of-utah-study-finds) | ksl.com | 9 | negative |
| 19 Mar 2026 | [Why Europe's poorer regions are hit hardest by air pollution](https://www.euronews.com/health/2026/03/19/air-pollution-linked-to-greater-health-risks-in-poorer-european-regions-study-finds) | euronews.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "air pollution" --since 2026-01-01 --until 2026-04-30
prism-news trends "air pollution" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "air pollution" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "air pollution", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "air pollution", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Fusion Energy News](fusion-energy-news.md)
- [Solar Energy News](solar-energy-news.md)
- [Lithium News](lithium-news.md)
- [Refinery News](refinery-news.md)
