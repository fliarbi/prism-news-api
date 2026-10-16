# Uranium News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “uranium news” · 140/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [uranium-news.json](../../examples/scenarios/uranium-news.json).

**Question.** How did uranium coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="uranium"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,342 |
| Negative · neutral · positive | 60% · 3.5% · 37% |
| Critical (priority 7–9) | 79% (5,037 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,738 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | mineral exploration drilling techniques |

## Twelve months of coverage

Monthly matching articles for `uranium` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 835 | 74% | 424 | 373 | ██████ |
| Jun 2025 | 2,065 | 82% | 1,559 | 462 | ███████████████ |
| Jul 2025 | 966 | 70% | 540 | 399 | ███████ |
| Aug 2025 | 762 | 76% | 328 | 398 | ██████ |
| Sep 2025 | 814 | 72% | 266 | 529 | ██████ |
| Oct 2025 | 539 | 66% | 127 | 393 | ████ |
| Nov 2025 | 563 | 72% | 196 | 351 | ████ |
| Dec 2025 | 593 | 60% | 96 | 459 | ████ |
| Jan 2026 | 693 | 60% | 139 | 517 | █████ |
| Feb 2026 | 1,353 | 73% | 687 | 619 | ██████████ |
| Mar 2026 | 1,558 | 84% | 983 | 522 | ███████████ |
| Apr 2026 | 2,738 | 85% | 1,972 | 674 | ████████████████████ |

The last four complete months averaged 1,586 articles a month against 1,157 in the first four (+37%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,814 | 29% |
| Iran | 336 | 5.3% |
| Canada | 297 | 4.7% |
| India | 134 | 2.1% |
| Australia | 58 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mineral exploration drilling techniques | 302 | 6.3% | +11% |
| geological surveying technologies | 154 | 3.2% | +24% |
| disarmament and arms control agreements | 791 | 16% | +533% |
| weapons of mass destruction (wmds) | 816 | 17% | +538% |
| economic sanctions and wartime trade | 802 | 17% | +547% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Trump says recovering Iran uranium 'will be a long and difficult process'](https://myrepublica.nagariknetwork.com/news/trump-says-recovering-iran-uranium-will-be-a-long-and-difficult-process-56-26.html) | myrepublica.nagariknetwork.com | 9 | negative |
| 18 Apr 2026 | ['We're Going to Take It Back Home to the US': Trump Reiterates to Take Enriched Uranium Despite Iran's Denial](https://www.republicworld.com/world-news/we-re-going-to-take-it-back-home-to-the-us-trump-reiterates-to-take-enriched-uranium-despite-iran-s-denial) | republicworld.com | 9 | negative |
| 17 Apr 2026 | [Trump: Iran Has Agreed to Hand Over Its Nuclear Dust](https://www.abhs.in/blog/trump-iran-agreed-no-nuclear-weapon-hand-over-nuclear-dust-april-2026) | abhs.in | 9 | negative |
| 16 Apr 2026 | [Trump says Iran agrees to hand over its enriched uranium](http://www.radionz.co.nz/news/world/592647/trump-says-iran-agrees-to-hand-over-its-enriched-uranium) | radionz.co.nz | 9 | negative |
| 9 Apr 2026 | [Israel-Lebanon Op Threatens Iran-US Ceasefire, Peace Talks](https://www.newkerala.com/news/a/stalemate-over-israel-op-lebanon-threatens-west-asia-530.htm) | newkerala.com | 9 | negative |
| 8 Apr 2026 | [Netanyahu: ceasefire fragile, Israel ready for war again](https://www.thehindubusinessline.com/news/world/netanyahu-says-israel-will-achieve-goals-by-agreement-or-resuming-fighting-warns-iran-with-finger-on-trigger/article70840212.ece) | thehindubusinessline.com | 9 | negative |
| 7 Apr 2026 | [Rescue or ruse: Iran accuses US of using operation to retrieve airman as cover to 'steal' uranium](https://www.indiatvnews.com/news/world/rescue-or-ruse-iran-accuses-us-of-using-operation-to-retrieve-airman-as-cover-to-steal-its-uranium-2026-04-07-1036541) | indiatvnews.com | 9 | negative |
| 6 Apr 2026 | [Cover ‘to steal enriched uranium’: Iran on US motives behind ‘daring’ operation for rescue of F-15E aviator](https://www.hindustantimes.com/world-news/cover-to-steal-enriched-uranium-iran-on-us-motives-behind-daring-operation-for-rescue-of-f-15e-aviator-101775511442839.html) | hindustantimes.com | 9 | negative |
| 6 Apr 2026 | [US Could Use Rescue of Pilots as Cover to Steal Iranian Uranium - Iranian Foreign Ministry](https://sputnikglobe.com/20260406/us-could-use-rescue-of-pilots-as-cover-to-steal-iranian-uranium---iranian-foreign-ministry-1123953193.html) | sputnikglobe.com | 9 | negative |
| 6 Apr 2026 | [West Asia War Escalates: Iran Rejects Proposed 45-Day Ceasefire, Says 'No Concessions On Hormuz, Uranium'](https://www.freepressjournal.in/world/west-asia-war-escalates-iran-rejects-proposed-45-day-ceasefire-says-no-concessions-on-hormuz-uranium) | freepressjournal.in | 9 | negative |
| 2 Apr 2026 | [US Military Plans for Iran: Trump Requests Options to Seize Nuclear Material & Middle East Buildup - Time News](https://time.news/us-military-plans-for-iran-trump-requests-options-to-seize-nuclear-material-middle-east-buildup/) | time.news | 9 | negative |
| 31 Mar 2026 | [President Trump Posts Video Showing Fiery Bunker Buster Bomb Attack in Iran](https://www.tmz.com/2026/03/31/president-trump-posts-video-of-iranian-bomb-strike/) | tmz.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "uranium" --since 2026-01-01 --until 2026-04-30
prism-news trends "uranium" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "uranium" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "uranium", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "uranium", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [EV Charging News](ev-charging-news.md)
- [Power Grid News](power-grid-news.md)
- [Solar Panels Industry](solar-panels-industry.md)
- [Fusion Energy News](fusion-energy-news.md)
