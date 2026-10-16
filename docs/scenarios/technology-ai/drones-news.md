# Drones News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drones news” · 880/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [drones-news.json](../../examples/scenarios/drones-news.json).

**Question.** How much drones coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="drones"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 30,448 |
| Negative · neutral · positive | 68% · 6.1% · 26% |
| Critical (priority 7–9) | 83% (25,215 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (13,294 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | war journalism and media coverage |

## Twelve months of coverage

Monthly matching articles for `drones` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5,803 | 81% | 4,122 | 1,497 | █████████ |
| Jun 2025 | 4,798 | 83% | 3,397 | 1,255 | ███████ |
| Jul 2025 | 4,592 | 74% | 3,049 | 1,405 | ███████ |
| Aug 2025 | 4,238 | 74% | 2,418 | 1,710 | ██████ |
| Sep 2025 | 8,629 | 82% | 6,412 | 1,848 | █████████████ |
| Oct 2025 | 4,596 | 79% | 3,007 | 1,432 | ███████ |
| Nov 2025 | 3,596 | 79% | 2,127 | 1,340 | █████ |
| Dec 2025 | 3,397 | 81% | 2,023 | 1,263 | █████ |
| Jan 2026 | 3,200 | 80% | 1,808 | 1,284 | █████ |
| Feb 2026 | 4,901 | 78% | 2,929 | 1,776 | ███████ |
| Mar 2026 | 13,294 | 89% | 10,479 | 2,372 | ████████████████████ |
| Apr 2026 | 9,053 | 77% | 5,569 | 2,360 | ██████████████ |

The last four complete months averaged 7,612 articles a month against 4,858 in the first four (+57%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,590 | 15% |
| Ukraine | 1,424 | 4.7% |
| Iran | 1,337 | 4.4% |
| United Arab Emirates | 1,139 | 3.7% |
| Russia | 969 | 3.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| war journalism and media coverage | 1,786 | 7.7% | +299% |
| naval and aerial combat operations | 7,651 | 33% | +82% |
| military technology advancements | 8,939 | 38% | +64% |
| space warfare and militarization of space | 4,630 | 20% | +36% |
| cybersecurity and cyber warfare | 7,220 | 31% | +54% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Ukrainian Drones Strike Perm Oil Refinery as Putin Proposes Truce](https://world.infonasional.com/ukraine-drones-perm-oil-ceasefire) | world.infonasional.com | 9 | negative |
| 29 Apr 2026 | [As Tuapse oil refinery fire spreads, Russian tour operators downplay risks to summer tourists](https://www.yahoo.com/news/articles/people-once-envied-us-tuapse-180224935.html) | yahoo.com | 9 | negative |
| 29 Apr 2026 | [Ukraine Strikes Russian Oil Pumping Station](https://marinelink.com/news/ukraine-strikes-russian-oil-pumping-538607) | marinelink.com | 9 | negative |
| 29 Apr 2026 | [Ukraine says it hits Russian oil pumping station 1,500 km away](https://www.detroitnews.com/story/news/world/2026/04/29/ukraine-hits-russian-oil-pumping-station-1500-km-away/89852773007/) | detroitnews.com | 9 | negative |
| 29 Apr 2026 | [Ukraine Extends Range of Strikes on Russia, Hits Oil Targets](http://globalbankingandfinance.com/zelenskiy-ukraine-continue-extending-range-strikes-russia/) | globalbankingandfinance.com | 9 | negative |
| 29 Apr 2026 | [Ukraine says it shot down 33,000 Russian drones in March, a monthly record](https://www.ajc.com/news/2026/04/ukraine-says-it-shot-down-33000-russian-drones-in-march-a-monthly-record/) | ajc.com | 9 | negative |
| 28 Apr 2026 | [Wladimir Putin News: Putin beklagt Angriffe Kiews auf zivile Infrastruktur in Russland](https://www.news.de/politik/859565860/putin-beklagt-angriffe-kiews-auf-zivile-infrastruktur-in-russland-wladimir-putin-news-der-dpa-aktuell-zu-krieg-und-konflikte/1/) | news.de | 9 | negative |
| 28 Apr 2026 | [Third Ukrainian strike hits Russian oil refinery and prompts evacuations](https://www.nation.com.pk/29-Apr-2026/third-ukrainian-strike-hits-russian-oil-refinery-prompts-evacuations) | nation.com.pk | 9 | negative |
| 28 Apr 2026 | [Russian Iskander missile storage facility in occupied Crimea hit, Ukraine's Special Forces release video](https://www.yahoo.com/news/articles/russian-iskander-missile-storage-facility-172958134.html) | yahoo.com | 9 | negative |
| 28 Apr 2026 | [Hezbollah Drone Strikes and Israeli Air Raids Strain Lebanon Ceasefire](https://www.asatunews.co.id/en/hezbollah-drone-strikes-israeli-air-raids-lebanon-ceasefire) | asatunews.co.id | 9 | negative |
| 28 Apr 2026 | [Desperate Russian troops ‘shooting down OWN drones to claim battle bonuses’](https://www.thescottishsun.co.uk/news/16202145/russian-troops-shoot-drones-claim-bonuses-cannibal-horror/) | thescottishsun.co.uk | 9 | negative |
| 28 Apr 2026 | [At least 2 killed, 20 injured in Russian attacks on Ukraine over past day](https://www.yahoo.com/news/articles/least-2-killed-20-injured-085818626.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "drones" --since 2026-01-01 --until 2026-04-30
prism-news trends "drones" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "drones" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "drones", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "drones", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Robotics News](robotics-news.md)
- [Starlink News](starlink-news.md)
- [Youtube News](youtube-news.md)
- [Streaming News](streaming-news.md)
