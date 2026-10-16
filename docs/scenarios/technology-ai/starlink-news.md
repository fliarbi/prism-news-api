# Starlink News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “starlink news” · 320/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [starlink-news.json](../../examples/scenarios/starlink-news.json).

**Question.** How much starlink coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="starlink"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,519 |
| Negative · neutral · positive | 37% · 1.9% · 61% |
| Critical (priority 7–9) | 76% (7,978 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (2,933 articles) |
| Most-reported country | United States (31% of matches) |
| Strongest theme by lift | satellite communication technologies |

## Twelve months of coverage

Monthly matching articles for `starlink` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,151 | 76% | 903 | 1,224 | ███████████████ |
| Jun 2025 | 2,060 | 78% | 898 | 1,126 | ██████████████ |
| Jul 2025 | 1,987 | 67% | 754 | 1,213 | ██████████████ |
| Aug 2025 | 2,370 | 75% | 755 | 1,574 | ████████████████ |
| Sep 2025 | 1,571 | 71% | 344 | 1,203 | ███████████ |
| Oct 2025 | 1,769 | 72% | 400 | 1,353 | ████████████ |
| Nov 2025 | 1,450 | 67% | 284 | 1,155 | ██████████ |
| Dec 2025 | 1,990 | 76% | 498 | 1,474 | ██████████████ |
| Jan 2026 | 2,933 | 77% | 1,439 | 1,440 | ████████████████████ |
| Feb 2026 | 2,638 | 80% | 983 | 1,604 | ██████████████████ |
| Mar 2026 | 2,054 | 71% | 652 | 1,367 | ██████████████ |
| Apr 2026 | 2,894 | 74% | 815 | 2,018 | ████████████████████ |

The last four complete months averaged 2,630 articles a month against 2,142 in the first four (+23%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 3,269 | 31% |
| Iran | 318 | 3.0% |
| China | 162 | 1.5% |
| India | 158 | 1.5% |
| Ukraine | 158 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| satellite communication technologies | 1,125 | 17% | +59% |
| in-flight wi-fi connectivity | 414 | 6.3% | +70% |
| satellite communication systems | 498 | 7.6% | +44% |
| space launch infrastructure development | 483 | 7.3% | -7% |
| in-flight entertainment options | 391 | 6.0% | +56% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Street battles and withdrawal of Russian mercenaries: Inside the 48-hour fall of Mali’s Kidal](https://www.france24.com/en/africa/20260427-street-battles-withdrawal-russian-mercenaries-inside-48-hour-fall-mali-kidal) ⚠ | france24.com | 9 | negative |
| 23 Apr 2026 | [Dramatic moment Ukraine blows up a DOZEN Russian officers in suicide drone blitz](https://www.thescottishsun.co.uk/news/16187334/ukraine-drone-blitz-kills-russian-officers/) ⚠ | thescottishsun.co.uk | 9 | negative |
| 20 Apr 2026 | [‘Dread of what regime could do next quickly erased joy of ceasefire’ – Iranians tell of fears and hopes for…](https://www.independent.ie/world-news/middle-east/dread-of-what-regime-could-do-next-quickly-erased-joy-of-ceasefire-iranians-tell-of-fears-and-hopes-for-future/a196027094.html) ⚠ | independent.ie | 9 | negative |
| 18 Apr 2026 | [Voices in Iran: Residents break internet blackout to describe life during ceasefire](https://www.independent.co.uk/news/world/middle-east/iran-trump-ceasefire-internet-blackout-b2958065.html) ⚠ | independent.co.uk | 9 | negative |
| 16 Apr 2026 | [Russia Marks 'Missile Zones' Near NATO](https://www.ibtimes.sg/russia-declares-missile-impact-zones-near-nato-waters-rocket-launch-85398) ⚠ | ibtimes.sg | 9 | negative |
| 15 Apr 2026 | [Vladimir Putin 'plans to put nukes into space' as he plots global mayhem](https://www.thesun.co.uk/news/38829906/putin-plans-space-nukes-chilling-uk-threat/) ⚠ | thesun.co.uk | 9 | negative |
| 11 Apr 2026 | [Easter truce between Russia and Ukraine begins](https://gulfnews.com/world/europe/easter-truce-between-russia-and-ukraine-begins-2-1.500503864) ⚠ | gulfnews.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine trade drone strikes ahead of Easter truce](https://www.manilatimes.net/2026/04/11/news/russia-and-ukraine-trade-drone-strikes-ahead-of-easter-truce/2318393) ⚠ | manilatimes.net | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce](https://myrepublica.nagariknetwork.com/news/russia-and-ukraine-set-to-begin-easter-truce-24-89.html) ⚠ | myrepublica.nagariknetwork.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce \| Today News](https://www.livemint.com/news/world/russia-and-ukraine-set-to-begin-easter-truce-11775885911120.html) ⚠ | livemint.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce - World News](http://www.hurriyetdailynews.com/russia-and-ukraine-set-to-begin-easter-truce-220893) ⚠ | hurriyetdailynews.com | 9 | negative |
| 10 Apr 2026 | [Ukraine and Russia will cease fire for Orthodox Easter](https://www.bangkokpost.com/world/3234510/ukraine-and-russia-will-cease-fire-for-orthodox-easter) ⚠ | bangkokpost.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "starlink" --since 2026-01-01 --until 2026-04-30
prism-news trends "starlink" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "starlink" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "starlink", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "starlink", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Quantum Computing News](quantum-computing-news.md)
- [Robotics News](robotics-news.md)
- [Drones News](drones-news.md)
- [Youtube News](youtube-news.md)
