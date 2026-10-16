# Renewable Energy News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “renewable energy news” · 1,000/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [renewable-energy-news.json](../../examples/scenarios/renewable-energy-news.json).

**Question.** How did renewable energy coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="renewable energy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 66,413 |
| Negative · neutral · positive | 18% · 1.4% · 80% |
| Critical (priority 7–9) | 73% (48,640 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (20,371 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | renewable energy policy & regulation |

## Twelve months of coverage

Monthly matching articles for `renewable energy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 11,733 | 69% | 2,338 | 9,163 | ████████████ |
| Jun 2025 | 10,086 | 71% | 1,560 | 8,392 | ██████████ |
| Jul 2025 | 11,610 | 69% | 2,156 | 9,273 | ███████████ |
| Aug 2025 | 11,191 | 68% | 2,085 | 8,967 | ███████████ |
| Sep 2025 | 12,960 | 74% | 1,980 | 10,822 | █████████████ |
| Oct 2025 | 12,755 | 75% | 1,801 | 10,800 | █████████████ |
| Nov 2025 | 12,751 | 76% | 2,001 | 10,621 | █████████████ |
| Dec 2025 | 12,508 | 75% | 1,733 | 10,632 | ████████████ |
| Jan 2026 | 12,514 | 74% | 1,801 | 10,545 | ████████████ |
| Feb 2026 | 17,138 | 74% | 2,855 | 13,994 | █████████████████ |
| Mar 2026 | 16,390 | 72% | 3,315 | 12,824 | ████████████████ |
| Apr 2026 | 20,371 | 73% | 4,192 | 15,875 | ████████████████████ |

The last four complete months averaged 16,603 articles a month against 11,155 in the first four (+49%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 10,036 | 15% |
| India | 6,398 | 9.6% |
| United Kingdom | 2,696 | 4.1% |
| China | 1,642 | 2.5% |
| Australia | 1,386 | 2.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| renewable energy policy & regulation | 3,186 | 7.2% | +82% |
| solar photovoltaic (pv) energy systems | 7,088 | 16% | +51% |
| smart grid integration for renewables | 2,284 | 5.2% | +82% |
| energy-efficient home solutions | 1,429 | 3.2% | +34% |
| renewable energy investment & financing models | 1,272 | 2.9% | +109% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Europe’s climate crisis worsens as warming outpaces global trends](https://www.openaccessgovernment.org/europes-climate-crisis-worsens-as-warming-outpaces-global-trends/208889/) ⚠ | openaccessgovernment.org | 9 | negative |
| 25 Apr 2026 | [Did Trump’s Economic War Backfire as Xi Turns Crisis into Strategic Gain](https://www.timesnownews.com/world/us/us-news/did-trumps-economic-war-backfire-as-xi-turns-crisis-into-strategic-gain-article-154169240) ⚠ | timesnownews.com | 9 | negative |
| 23 Apr 2026 | [IEA: World Faces Biggest Energy Security Threat in History](https://www.newkerala.com/news/a/world-facing-biggest-energy-security-threat-history-iea-813.htm) | newkerala.com | 9 | negative |
| 22 Apr 2026 | [The Debate - World's worst energy crisis? Iran war sparks scramble for alternatives to Gulf oil](https://www.france24.com/en/tv-shows/the-debate/20260422-world-s-worst-energy-crisis-iran-war-sparks-scramble-for-alternatives-to-gulf-oil) | france24.com | 9 | negative |
| 21 Apr 2026 | [Singapore’s resilience and ‘unnatural resourcefulness’ amid global shocks](https://www.businesstimes.com.sg/opinion-features/singapores-resilience-and-unnatural-resourcefulness-amid-global-shocks) | businesstimes.com.sg | 9 | negative |
| 21 Apr 2026 | [As global crude oil crisis deepens, the only cure may be a demand shock](https://www.indiatoday.in/business/commodities/story/global-oil-crisis-resolution-cure-use-less-demand-destruction-explaned-2899291-2026-04-21) | indiatoday.in | 9 | negative |
| 20 Apr 2026 | [Climate Change and Its Comprehensive Impact on Planet Earth - Jordan News \| Latest News from Jordan, MENA](https://www.jordannews.jo/Section-29/Analysis/Climate-Change-and-Its-Comprehensive-Impact-on-Planet-Earth-50721) ⚠ | jordannews.jo | 9 | negative |
| 17 Apr 2026 | [Iran War: Strait of Hormuz Open Amid Israel-Lebanon Truce](https://en.tempo.co/read/2098896/iran-war-strait-of-hormuz-open-amid-israel-lebanon-truce) ⚠ | en.tempo.co | 9 | negative |
| 14 Apr 2026 | [As I write these lines… \| FairPlanet](https://www.fairplanet.org/dossier/climate-change/as-i-write-these-lines/) ⚠ | fairplanet.org | 9 | negative |
| 9 Apr 2026 | [Trump says Iran doing "very poor job" of letting oil through Hormuz Strait](https://www.newsweek.com/trump-iran-poor-job-oil-hormuz-strait-11808527) ⚠ | newsweek.com | 9 | negative |
| 9 Apr 2026 | [What does Trump have to do with taco Tuesday? Social jabs explained](https://www.dailycommercial.com/story/news/trump/2026/04/09/donald-trump-taco-tariffs-iran/89517075007/) ⚠ | dailycommercial.com | 9 | negative |
| 9 Apr 2026 | [Global Energy Crisis: Iran War Analysis and Regulatory Hurdles - Time News](https://time.news/global-energy-crisis-iran-war-analysis-and-regulatory-hurdles/) | time.news | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "renewable energy" --since 2026-01-01 --until 2026-04-30
prism-news trends "renewable energy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "renewable energy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "renewable energy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "renewable energy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Gas Prices News](gas-prices-news.md)
- [Floods News](floods-news.md)
- [Electric Vehicles News](electric-vehicles-news.md)
- [Wildfire News](wildfire-news.md)
