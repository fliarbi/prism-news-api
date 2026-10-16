# Humanoid Robot News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “humanoid robot news” · 20/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [humanoid-robot-news.json](../../examples/scenarios/humanoid-robot-news.json).

**Question.** How much humanoid robot coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="humanoid robot"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,907 |
| Negative · neutral · positive | 6.8% · 0.8% · 92% |
| Critical (priority 7–9) | 58% (1,101 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (684 articles) |
| Most-reported country | China (19% of matches) |
| Strongest theme by lift | entertainment and companion robotics |

## Twelve months of coverage

Monthly matching articles for `humanoid robot` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 193 | 55% | 21 | 172 | ██████ |
| Jun 2025 | 167 | 61% | 27 | 139 | █████ |
| Jul 2025 | 209 | 53% | 13 | 195 | ██████ |
| Aug 2025 | 396 | 59% | 12 | 380 | ████████████ |
| Sep 2025 | 186 | 63% | 4 | 182 | █████ |
| Oct 2025 | 226 | 46% | 10 | 216 | ███████ |
| Nov 2025 | 293 | 62% | 31 | 259 | █████████ |
| Dec 2025 | 180 | 61% | 14 | 164 | █████ |
| Jan 2026 | 407 | 56% | 18 | 388 | ████████████ |
| Feb 2026 | 291 | 52% | 11 | 277 | █████████ |
| Mar 2026 | 525 | 61% | 68 | 455 | ███████████████ |
| Apr 2026 | 684 | 59% | 32 | 642 | ████████████████████ |

The last four complete months averaged 477 articles a month against 241 in the first four (+98%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| China | 353 | 19% |
| United States | 349 | 18% |
| India | 44 | 2.3% |
| Spain | 28 | 1.5% |
| Germany | 20 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| entertainment and companion robotics | 426 | 38% | +155% |
| human-robot interaction and collaborative robotics | 201 | 18% | +158% |
| domestic service robotics for household tasks | 415 | 37% | +133% |
| robotic actuators and mechanisms | 76 | 6.8% | +204% |
| artificial intelligence in robotic decision-making | 62 | 5.6% | +158% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Elon Musk Says Optimus V3 Unveil To Be Closer To Robot's Production As Rivals 'Copy' Everything Tesla Doe](https://benzinga.com/markets/tech/26/04/51989926/elon-musk-says-optimus-v3-unveil-to-be-closer-to-robots-production-as-rivals-copy-everything-tesla-does) | benzinga.com | 8 | positive |
| 20 Apr 2026 | [Robot named Lightning blows past human runners to set half-marathon record in Beijing](https://www.latimes.com/sports/story/2026-04-20/humanoid-robot-lightning-sets-half-marathon-record-in-beijing) | latimes.com | 8 | positive |
| 20 Apr 2026 | [China's humanoid robot smashes half marathon world record](https://www.indy100.com/science-tech/humanoid-robot-beijing-half-marathon-honor-china) | indy100.com | 8 | positive |
| 20 Apr 2026 | [A humanoid robot sprints to victory in Beijing, beating world record](https://www.thestar.com.my/tech/tech-news/2026/04/20/a-humanoid-robot-sprints-to-victory-in-beijing-beating-the-human-half-marathon-world-record) | thestar.com.my | 8 | positive |
| 20 Apr 2026 | [A humanoid robot sprints past the human half-marathon world record in Beijing race](https://lethbridgeherald.com/sports/national-sports/2026/04/19/a-humanoid-robot-sprints-past-the-human-half-marathon-world-record-in-beijing-race/) | lethbridgeherald.com | 8 | positive |
| 20 Apr 2026 | [Humanoid Robot Smashes Human Half Marathon Record in Beijing — Nearly 3x Faster Than Last Year! (VIDEO) \|…](https://www.thegatewaypundit.com/2026/04/humanoid-robot-smashes-human-half-marathon-record-beijing/) | thegatewaypundit.com | 8 | positive |
| 19 Apr 2026 | [Humanoid robot wins Beijing half-marathon, defeating the human world record](https://www.pbs.org/newshour/world/humanoid-robot-wins-beijing-half-marathon-defeating-the-human-world-record) | pbs.org | 8 | positive |
| 19 Apr 2026 | [Robot wins half-marathon in time faster than human world record](https://www.dailystar.co.uk/news/latest-news/robot-wins-half-marathon-time-37038020) | dailystar.co.uk | 8 | positive |
| 19 Apr 2026 | [A humanoid robot sprints to victory in Beijing, beating the human half-marathon world record - WTOP News](https://wtop.com/funny-weird-news/2026/04/a-humanoid-robot-sprints-to-victory-in-beijing-beating-the-human-half-marathon-world-record/) | wtop.com | 8 | positive |
| 19 Apr 2026 | [Humanoid robot wins half-marathon in China; beats world record](https://www.espn.co.uk/athletics/story/_/id/48529282/humanoid-robot-wins-half-marathon-china-beats-world-record) | espn.co.uk | 8 | positive |
| 19 Apr 2026 | [Siemens tests Nvidia AI-powered humanoid robot in German factory](https://euronews.com/2026/04/19/can-ai-robots-work-alongside-humans-siemens-and-nvidia-trial-a-humanoid-robot) | euronews.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "humanoid robot" --since 2026-01-01 --until 2026-04-30
prism-news trends "humanoid robot" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "humanoid robot" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "humanoid robot", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "humanoid robot", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI Safety News](ai-safety-news.md)
- [Augmented Reality News](augmented-reality-news.md)
- [Blockchain News](blockchain-news.md)
- [Autonomous Vehicles News](autonomous-vehicles-news.md)
