# Agriculture Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “agriculture industry” · 1,300/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [agriculture-industry.json](../../examples/scenarios/agriculture-industry.json).

**Question.** How much news did the agriculture industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="agriculture industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 822 |
| Negative · neutral · positive | 30% · 1.9% · 68% |
| Critical (priority 7–9) | 56% (459 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (289 articles) |
| Most-reported country | United States (31% of matches) |
| Strongest theme by lift | tractors and tractor attachments |

## Twelve months of coverage

Monthly matching articles for `agriculture industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 151 | 40% | 41 | 104 | ██████████ |
| Jun 2025 | 100 | 57% | 37 | 59 | ███████ |
| Jul 2025 | 132 | 48% | 46 | 83 | █████████ |
| Aug 2025 | 170 | 56% | 61 | 106 | ████████████ |
| Sep 2025 | 160 | 61% | 51 | 106 | ███████████ |
| Oct 2025 | 126 | 52% | 27 | 96 | █████████ |
| Nov 2025 | 132 | 48% | 35 | 96 | █████████ |
| Dec 2025 | 156 | 58% | 58 | 96 | ███████████ |
| Jan 2026 | 106 | 50% | 23 | 79 | ███████ |
| Feb 2026 | 289 | 67% | 90 | 195 | ████████████████████ |
| Mar 2026 | 214 | 44% | 60 | 150 | ███████████████ |
| Apr 2026 | 213 | 55% | 75 | 132 | ███████████████ |

The last four complete months averaged 206 articles a month against 138 in the first four (+49%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 253 | 31% |
| India | 73 | 8.9% |
| Canada | 13 | 1.6% |
| United Kingdom | 10 | 1.2% |
| China | 6 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| tractors and tractor attachments | 28 | 5.8% | +300% |
| agricultural technology and precision farming tools | 25 | 5.2% | +56% |
| agricultural policy and regulatory compliance | 23 | 4.8% | +475% |
| futures contracts specifications and expiration dates | 18 | 3.8% | new |
| farm labor management and safety protocols | 17 | 3.5% | +143% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 3 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 2 Apr 2026 | [Is America on the cusp of a farm crisis?](https://www.nbcnews.com/business/economy/trump-iran-war-farm-crisis-rcna266283) | nbcnews.com | 8 | negative |
| 27 Mar 2026 | [Trump highlights new relief for farmers battered by tariffs, Iran war](https://www.capecodtimes.com/story/news/politics/2026/03/27/donald-trump-farmers-agriculture-regulation-iran-tariffs/89343530007/) | capecodtimes.com | 8 | positive |
| 19 Feb 2026 | [Zach Lahn says Iowa must confront big ag as it fights rise in cancer](https://mmajunkie.usatoday.com/story/news/politics/elections/2026/02/19/zach-lahn-iowa-cancer-crisis-big-agriculture/88703534007/) | mmajunkie.usatoday.com | 8 | negative |
| 10 Feb 2026 | [Tennessee row crop farmers face changing global market after two years in the red](https://www.yahoo.com/news/articles/tennessee-row-crop-farmers-face-110049411.html) | yahoo.com | 8 | negative |
| 22 Apr 2026 | [Alltech survey: Global feed production hit 1.44 billion tons in 2025](https://www.feedandadditive.com/alltech-survey-global-feed-production-hit-1-44-billion-tons-in-2025/) | feedandadditive.com | 7 | positive |
| 11 Apr 2026 | [$950M water project on drafting table](https://www.montereyherald.com/2026/04/11/950m-water-project-on-drafting-table/) | montereyherald.com | 7 | negative |
| 18 Mar 2026 | [Ag Day at the Capitol brings focus to farmers and future farmers](https://www.yahoo.com/news/articles/ag-day-capitol-brings-focus-181144798.html) | yahoo.com | 7 | positive |
| 14 Mar 2026 | [पंतनगर में किसान मेले का सीएम धामी ने किया शुभारंभ, गिनाई सरकार की उपलब्धियां](https://www.etvbharat.com/hi/state/cm-dhami-inaugurates-kisan-mela-in-pantnagar-uttarakhand-news-uts26031403112) | etvbharat.com | 7 | positive |
| 20 Feb 2026 | [Apex Ag Solutions Launches Mental Health Resource for Farmers](https://armoneyandpolitics.com/apex-ag-mental-health-farmers/) | armoneyandpolitics.com | 7 | positive |
| 23 Feb 2026 | [Nutrien Stock in 2026: Buy, Hold, or Sell?](http://www.theglobeandmail.com/investing/markets/stocks/NTR-T/pressreleases/372922/nutrien-stock-in-2026-buy-hold-or-sell/) | theglobeandmail.com | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "agriculture industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "agriculture industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "agriculture industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "agriculture industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "agriculture industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Sugar Industry](sugar-industry.md)
- [3d Printing Industry](3d-printing-industry.md)
- [Construction Industry](construction-industry.md)
- [Cement Industry](cement-industry.md)
