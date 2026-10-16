# Streaming News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “streaming news” · 40/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [streaming-news.json](../../examples/scenarios/streaming-news.json).

**Question.** How much streaming coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="streaming"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 57,757 |
| Negative · neutral · positive | 13% · 1.9% · 85% |
| Critical (priority 7–9) | 13% (7,307 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (22,877 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | video monetization models (subscription, ads, etc.) |

## Twelve months of coverage

Monthly matching articles for `streaming` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9,186 | 13% | 1,203 | 7,708 | ████████ |
| Jun 2025 | 6,797 | 13% | 851 | 5,821 | ██████ |
| Jul 2025 | 8,799 | 14% | 1,355 | 7,331 | ████████ |
| Aug 2025 | 10,288 | 16% | 1,608 | 8,527 | █████████ |
| Sep 2025 | 9,371 | 14% | 1,416 | 7,776 | ████████ |
| Oct 2025 | 8,478 | 16% | 1,461 | 6,896 | ███████ |
| Nov 2025 | 8,627 | 14% | 1,275 | 7,213 | ████████ |
| Dec 2025 | 10,340 | 21% | 1,528 | 8,642 | █████████ |
| Jan 2026 | 9,552 | 14% | 1,273 | 8,089 | ████████ |
| Feb 2026 | 11,738 | 18% | 1,863 | 9,658 | ██████████ |
| Mar 2026 | 13,590 | 14% | 1,990 | 11,256 | ████████████ |
| Apr 2026 | 22,877 | 8.9% | 2,545 | 19,859 | ████████████████████ |

The last four complete months averaged 14,439 articles a month against 8,768 in the first four (+65%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 15,380 | 27% |
| India | 2,004 | 3.5% |
| United Kingdom | 1,885 | 3.3% |
| Japan | 480 | 0.8% |
| Australia | 468 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| video monetization models (subscription, ads, etc.) | 1,348 | 4.5% | +60% |
| xxx-rated media and content | 1,178 | 3.9% | +9717% |
| adult entertainment industry | 1,031 | 3.4% | +25675% |
| ott (over-the-top) media services | 2,047 | 6.8% | +94% |
| video-on-demand (vod) platforms | 866 | 2.9% | +125% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 4 Apr 2026 | [Xxtenations 2018 Death Killer 2026 Digital Library Update #819](https://zephyrpeacock.com/insidersecretsbuzz126/xxtenations-2018-death-killer/) | zephyrpeacock.com | 9 | negative |
| 4 Apr 2026 | [R Kelly Sexual Tape Newest Upload Hub 2026 #930](https://zephyrpeacock.com/insidersecretsbuzz1366/r-kelly-sexual-tape/) | zephyrpeacock.com | 9 | negative |
| 28 Apr 2026 | [JioHotstar OTT growth delivers stunning win in OTT battle](https://punemirror.com/entertainment/jiohotstar-ott-growth-fy26-market-shift/) | punemirror.com | 8 | positive |
| 24 Apr 2026 | [The Peacock Streaming Service Has Lost A Staggering Amount Of Money - SlashFilm](https://www.slashfilm.com/2156508/peacock-streaming-service-lost-money/) | slashfilm.com | 8 | positive |
| 24 Apr 2026 | [Inside the huge sum Tyson Fury got for his Morecambe house](https://www.mirror.co.uk/tv/tv-news/inside-huge-amount-tyson-fury-37065232) | mirror.co.uk | 8 | positive |
| 24 Apr 2026 | [Twitch star ExtraEmily goes on indefinite break after viewbot controversy](https://www.hindustantimes.com/world-news/us-news/twitch-star-extraemily-goes-on-indefinite-break-after-viewbot-controversy-101776970163514.html) | hindustantimes.com | 8 | negative |
| 23 Apr 2026 | [Taylor Swift Crowned Most-Streamed Artist in Spotify History With Over 120 Billion Streams](https://www.ibtimes.com.au/taylor-swift-crowned-most-streamed-artist-spotify-history-over-120-billion-streams-1867380) | ibtimes.com.au | 8 | positive |
| 19 Apr 2026 | [Netflix co-founder Reed Hastings exits as chairman, company shares slump](https://www.malaymail.com/news/showbiz/2026/04/19/netflix-co-founder-reed-hastings-exits-as-chairman-company-shares-slump/216900) | malaymail.com | 8 | positive |
| 16 Apr 2026 | [Netflix Shares Fall 8% on Q2 Miss Despite Q1 Beat and Hastings Board Exit - Time News](https://time.news/netflix-shares-fall-8-on-q2-miss-despite-q1-beat-and-hastings-board-exit/) | time.news | 8 | positive |
| 15 Apr 2026 | [Justin Bieber's Coachella Headline Ignites Massive Streaming Surge for Publishers and Songwriters - Radio…](https://radiofacts.com/justin-biebers-coachella-headline-ignites-massive-streaming-surge-for-publishers-and-songwriters/) | radiofacts.com | 8 | positive |
| 15 Apr 2026 | [Netflix Q1 2026 earnings ad growth and content spending in focus](https://indiantelevision.com/mam/netflix-q1-2026-earnings-ad-growth-and-content-spending-in-focus/) | indiantelevision.com | 8 | positive |
| 14 Apr 2026 | [Why Streaming Costs More Than Cable: 3 Ways Hollywood Killed Cord Cutting](https://techaeris.com/2026/04/14/why-streaming-costs-more-than-cable-2026/) | techaeris.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "streaming" --since 2026-01-01 --until 2026-04-30
prism-news trends "streaming" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "streaming" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "streaming", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "streaming", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Drones News](drones-news.md)
- [Youtube News](youtube-news.md)
- [AI Agents News](ai-agents-news.md)
- [Virtual Reality News](virtual-reality-news.md)
