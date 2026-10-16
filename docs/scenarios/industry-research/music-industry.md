# Music Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “music industry” · 720/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [music-industry.json](../../examples/scenarios/music-industry.json).

**Question.** How much news did the music industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="music industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 18,683 |
| Negative · neutral · positive | 22% · 0.4% · 78% |
| Critical (priority 7–9) | 21% (3,912 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (5,627 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | garage rock revival |

## Twelve months of coverage

Monthly matching articles for `music industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,311 | 22% | 681 | 2,586 | ████████████ |
| Jun 2025 | 2,279 | 21% | 496 | 1,755 | ████████ |
| Jul 2025 | 3,078 | 20% | 778 | 2,279 | ███████████ |
| Aug 2025 | 2,728 | 17% | 561 | 2,152 | ██████████ |
| Sep 2025 | 2,698 | 22% | 585 | 2,086 | ██████████ |
| Oct 2025 | 3,353 | 30% | 771 | 2,563 | ████████████ |
| Nov 2025 | 3,806 | 25% | 587 | 3,200 | ██████████████ |
| Dec 2025 | 3,191 | 23% | 543 | 2,627 | ███████████ |
| Jan 2026 | 4,191 | 16% | 1,075 | 3,095 | ███████████████ |
| Feb 2026 | 4,455 | 20% | 968 | 3,448 | ████████████████ |
| Mar 2026 | 4,410 | 21% | 836 | 3,552 | ████████████████ |
| Apr 2026 | 5,627 | 25% | 1,214 | 4,376 | ████████████████████ |

The last four complete months averaged 4,671 articles a month against 2,849 in the first four (+64%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 51% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,406 | 29% |
| United Kingdom | 1,069 | 5.7% |
| India | 498 | 2.7% |
| Nigeria | 228 | 1.2% |
| Canada | 194 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| garage rock revival | 540 | 5.6% | +163% |
| punk rock rebellion | 688 | 7.1% | +883% |
| glam rock aesthetics | 568 | 5.9% | +172% |
| pop music chart-topping albums | 261 | 2.7% | -34% |
| outdoor summer music festival guides | 223 | 2.3% | +190% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [D4vd Charged: Dismemberment in Teenager's Death - Memesita](https://www.memesita.com/d4vd-charged-dismemberment-in-teenagers-death/) | memesita.com | 8 | negative |
| 22 Apr 2026 | [Sonu Nigam Claims Asha Bhosle's Death Should Not Be 'Mourned', Says, 'Is This A Life To Cry..'](https://www.bollywoodshaadis.com/articles/sonu-nigam-asha-bhosle-death-78075) | bollywoodshaadis.com | 8 | negative |
| 22 Apr 2026 | [Inside the industry's streaming fraud response as Deezer now logs 75,000 AI-based tracks per day](http://www.musicweek.com/digital/read/inside-the-industry-s-streaming-fraud-response-as-deezer-now-logs-75-000-ai-based-tracks-per-day/093982) | musicweek.com | 8 | negative |
| 21 Apr 2026 | [‘After music, kabaddi, Bishnoi gang seizing control of cricket in Canada’](https://www.newindianexpress.com/india/2026/Apr/21/after-music-kabaddi-bishnoi-gang-seizing-control-of-cricket-in-canada) | newindianexpress.com | 8 | negative |
| 17 Apr 2026 | [Singer D4vd Arrested in Connection with 16-Year-Old's Death - Memesita](https://www.memesita.com/singer-d4vd-arrested-in-connection-with-16-year-olds-death/) | memesita.com | 8 | negative |
| 16 Apr 2026 | [Everything to Know About Nicki Minaj's Parents — After Rapper's Dad is Killed In a Hit-and-Run Accident](https://radaronline.com/p/nicki-minaj-parents-meet-robert-carol-maraj-dead-father/) | radaronline.com | 8 | negative |
| 15 Apr 2026 | [US jury finds Live Nation guilty of monopoly](https://en.ilsole24ore.com/art/usa-jury-finds-live-nation-guilty-of-monopoly-AISwosWC) | en.ilsole24ore.com | 8 | negative |
| 13 Apr 2026 | [Asha Bhosle Death: Pakistan Regulator Sends Notice, Restricts Channel From Coverage On Singer's Demise](https://www.timesnownews.com/entertainment-news/bollywood/asha-bhosle-death-pakistan-regulator-sends-notice-restricts-channel-from-coverage-on-singers-demise-article-154068813) ⚠ | timesnownews.com | 8 | negative |
| 13 Apr 2026 | [Asha Bhosle Funeral Live Update & Videos: Legendary Singer To Be Cremated At Shivaji Park With State Honours…](https://in.mashable.com/entertainment/108406/asha-bhosle-funeral-live-update-videos-legendary-singer-to-be-cremated-at-shivaji-park-with-state-ho) | in.mashable.com | 8 | negative |
| 12 Apr 2026 | [Asha Bhosle Passes Away At 92, Helen Finds The Singer's Death 'Shocking', Says, 'She Was So Healthy'](https://www.bollywoodshaadis.com/articles/asha-bhosle-passes-away-at-92-helen-finds-the-singer-death-shocking-77604) | bollywoodshaadis.com | 8 | negative |
| 12 Apr 2026 | ['Heartbreaking': Maha Guv Varma, CM Fadnavis express distress over passing of Asha Bhosle - Social News XYZ](https://www.socialnews.xyz/2026/04/12/heartbreaking-maha-guv-varma-cm-fadnavis-express-distress-over-passing-of-asha-bhosle/) | socialnews.xyz | 8 | negative |
| 12 Apr 2026 | ['Deeply concerned': PM Modi wishes Asha Bhosle speedy recovery](https://www.newsbytesapp.com/news/entertainment/pm-narendra-modi-prays-for-asha-bhosle-s-recovery/story) | newsbytesapp.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "music industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "music industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "music industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "music industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "music industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Steel Industry](steel-industry.md)
- [Chemical Industry](chemical-industry.md)
- [Aerospace Industry](aerospace-industry.md)
- [Sugar Industry](sugar-industry.md)
