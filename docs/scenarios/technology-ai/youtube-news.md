# Youtube News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “youtube news” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [youtube-news.json](../../examples/scenarios/youtube-news.json).

**Question.** How much youtube coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="YouTube"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 149,454 |
| Negative · neutral · positive | 35% · 1.4% · 63% |
| Critical (priority 7–9) | 31% (45,834 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (45,543 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | sustainable construction materials and practices |

## Twelve months of coverage

Monthly matching articles for `YouTube` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 27,020 | 30% | 8,274 | 18,199 | ████████████ |
| Jun 2025 | 21,825 | 29% | 6,268 | 15,148 | ██████████ |
| Jul 2025 | 29,780 | 28% | 9,792 | 19,459 | █████████████ |
| Aug 2025 | 35,467 | 32% | 12,577 | 22,373 | ████████████████ |
| Sep 2025 | 32,802 | 35% | 11,460 | 20,519 | ██████████████ |
| Oct 2025 | 27,560 | 31% | 7,642 | 19,509 | ████████████ |
| Nov 2025 | 23,378 | 32% | 7,147 | 15,827 | ██████████ |
| Dec 2025 | 25,833 | 32% | 8,009 | 17,448 | ███████████ |
| Jan 2026 | 26,553 | 29% | 8,693 | 17,438 | ████████████ |
| Feb 2026 | 38,989 | 31% | 14,760 | 23,664 | █████████████████ |
| Mar 2026 | 38,369 | 32% | 14,537 | 23,189 | █████████████████ |
| Apr 2026 | 45,543 | 31% | 14,360 | 30,446 | ████████████████████ |

The last four complete months averaged 37,364 articles a month against 28,523 in the first four (+31%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 40,885 | 27% |
| India | 14,284 | 9.6% |
| United Kingdom | 4,295 | 2.9% |
| China | 1,153 | 0.8% |
| Australia | 1,134 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| sustainable construction materials and practices | 1,976 | 2.5% | +521% |
| building automation and smart systems | 1,975 | 2.5% | +523% |
| green building certifications and standards | 1,975 | 2.5% | +523% |
| indoor air quality management in buildings | 1,967 | 2.5% | +526% |
| mental health and support communities | 1,654 | 2.1% | +189% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Newton man charged with sexually abusing child](https://www.kcci.com/article/camden-beach-newton-iowa-charged-sexual-abuse-child/71106458) | kcci.com | 9 | negative |
| 22 Apr 2026 | [The Debate - World's worst energy crisis? Iran war sparks scramble for alternatives to Gulf oil](https://www.france24.com/en/tv-shows/the-debate/20260422-world-s-worst-energy-crisis-iran-war-sparks-scramble-for-alternatives-to-gulf-oil) | france24.com | 9 | negative |
| 21 Apr 2026 | [Trump 'tried to use nuclear codes but was stopped by military chief'](https://www.aol.com/entertainment/trump-tried-nuclear-codes-stopped-095509465.html) | aol.com | 9 | negative |
| 21 Apr 2026 | [Parlons-en, les invités - Enfant violé, enfance volée ? Parlons-en avec Romain Lemire et Frédéric Pommier](https://www.france24.com/fr/%C3%A9missions/parlons-en-les-invit%C3%A9s/20260421-enfant-viol%C3%A9-enfance-vol%C3%A9e-parlons-en-avec-romain-lemire-et-fr%C3%A9d%C3%A9ric-pommier) | france24.com | 9 | negative |
| 20 Apr 2026 | [Donald Trump 'blocked from using nuclear codes' during emergency meeting](https://www.dailystar.co.uk/news/latest-news/donald-trump-blocked-using-nuclear-37045547) | dailystar.co.uk | 9 | negative |
| 19 Apr 2026 | [Au cœur de l’info, l’invité - Andreï Kourkov : "On sort de l'hiver le plus dramatique pour l'Ukraine"](https://www.france24.com/fr/%C3%A9missions/au-c%C5%93ur-de-l-info-l-invit%C3%A9/20260419-andre%C3%AF-kourkov-on-sort-de-l-hiver-le-plus-dramatique-pour-l-ukraine) | france24.com | 9 | negative |
| 15 Apr 2026 | ['China's Nostradamus' Predicts US Will Lose Ground Invasion This Month, Ending the US Dollar Dominance](http://www.ibtimes.co.uk/chinas-nostradamus-predicts-us-will-lose-ground-invasion-this-month-ending-us-dollar-dominance-1791880) | ibtimes.co.uk | 9 | negative |
| 12 Apr 2026 | [The last thing the US wants: Trump will hang the defeat on Europe Ukraine and in Iran: EADaily](https://eadaily.com/en/news/2026/04/13/the-last-thing-the-us-wants-trump-will-hang-the-defeat-on-europe-ukraine-and-in-iran) | eadaily.com | 9 | negative |
| 12 Apr 2026 | [Chilling Iran propaganda video shows Trump being 'buried' in horror WW3 threat](http://www.express.co.uk/news/world/2193103/iran-propaganda-video-shows-trump) | express.co.uk | 9 | negative |
| 8 Apr 2026 | [The Debate - Can the ceasefire hold? Fragile US–Iran truce tested ahead of talks](https://www.france24.com/en/tv-shows/the-debate/20260408-can-ceasefire-hold-us-iran-truce-tested-before-talks-start) | france24.com | 9 | negative |
| 8 Apr 2026 | [US, Iran agree to ceasefire as Trump pulls back on threat to destroy Iranian 'civilisation'](https://www.france24.com/en/middle-east/20260408-us-iran-agree-two-week-ceasefire-trump-pulls-back-threats) | france24.com | 9 | negative |
| 7 Apr 2026 | [YouTube simulation shows result of US declaring nuclear war on Russia](https://www.ladbible.com/news/us-news/us-nuclear-war-russia-simulation-what-would-happen-972772-20260407) | ladbible.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "YouTube" --since 2026-01-01 --until 2026-04-30
prism-news trends "YouTube" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "YouTube" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "YouTube", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "YouTube", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Starlink News](starlink-news.md)
- [Drones News](drones-news.md)
- [Streaming News](streaming-news.md)
- [AI Agents News](ai-agents-news.md)
