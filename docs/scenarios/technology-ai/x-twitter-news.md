# X Twitter News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “x twitter news” · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [x-twitter-news.json](../../examples/scenarios/x-twitter-news.json).

**Question.** How much x twitter coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="Twitter"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 125,100 |
| Negative · neutral · positive | 42% · 2.0% · 56% |
| Critical (priority 7–9) | 40% (50,532 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (137,916 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | cryptocurrency impact on forex markets |

## Twelve months of coverage

Monthly matching articles for `Twitter` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 28,573 | 42% | 12,893 | 14,708 | ████ |
| Jun 2025 | 21,194 | 39% | 8,586 | 12,044 | ███ |
| Jul 2025 | 47,631 | 34% | 22,862 | 23,932 | ███████ |
| Aug 2025 | 137,916 | 44% | 73,769 | 61,869 | ████████████████████ |
| Sep 2025 | 29,691 | 39% | 11,357 | 17,111 | ████ |
| Oct 2025 | 24,359 | 39% | 9,387 | 14,409 | ████ |
| Nov 2025 | 22,039 | 40% | 8,490 | 13,020 | ███ |
| Dec 2025 | 21,430 | 38% | 7,878 | 12,967 | ███ |
| Jan 2026 | 22,140 | 42% | 9,286 | 12,411 | ███ |
| Feb 2026 | 30,691 | 43% | 12,610 | 17,478 | ████ |
| Mar 2026 | 31,828 | 44% | 14,561 | 16,529 | █████ |
| Apr 2026 | 40,441 | 35% | 16,158 | 23,357 | ██████ |

The last four complete months averaged 31,275 articles a month against 58,828 in the first four (-47%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 26,493 | 21% |
| South Africa | 5,957 | 4.8% |
| India | 2,905 | 2.3% |
| United Kingdom | 2,672 | 2.1% |
| Malaysia | 1,191 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| cryptocurrency impact on forex markets | 5,585 | 7.6% | +205% |
| entertainment industry awards shows | 1,174 | 1.6% | +138% |
| corporate governance and board decisions | 238 | 0.3% | +34% |
| winter weather preparedness | 349 | 0.5% | +301% |
| political satire and news comedy | 309 | 0.4% | -23% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Michael Jackson’s Nephew Slams Media Ahead of ‘Michael’ Biopic Release: ‘Can’t Wait ‘Till Some Critics Have…](https://www.yahoo.com/entertainment/movies/articles/michael-jackson-nephew-slams-media-203846645.html) | yahoo.com | 9 | negative |
| 14 Apr 2026 | [Dick Vitale health update: College hoops analyst confirms cancer back](https://www.freep.com/story/sports/nba/pistons/2026/04/13/dick-vitale-health-update-college-hoops-analyst-confirms-cancer-back/89599466007/) | freep.com | 9 | positive |
| 13 Apr 2026 | [Dick Vitale health update: College basketball analyst confirms melanoma diagnosis](https://www.cincinnati.com/story/sports/2026/04/13/dick-vitale-health-update-melanoma-diagnosis-cancer/89597325007/) | cincinnati.com | 9 | positive |
| 13 Apr 2026 | [It's not really the kind of message you expect to get from a friend or a colleague - or indeed from anyone…](https://www.bbc.co.uk/blogs/thereporters/rorycellanjones/2010/02/embarrassment_on_twitter.html) | bbc.co.uk | 9 | negative |
| 10 Apr 2026 | [President shares video alleging Israeli soldiers abused Palestinian child, compares situation to massacre of…](https://koreatimes.co.kr/foreignaffairs/20260410/president-shares-video-alleging-israeli-soldiers-abused-palestinian-child-compares-situation-to-massacre-of-jewish-people) | koreatimes.co.kr | 9 | negative |
| 8 Apr 2026 | ['Trump Bows To Iranian Civilisation': Iran Mission Dig At US President Hours After Ceasefire](https://www.timesnownews.com/world/us/us-news/donald-trump-bows-to-iranian-civilisation-iran-mission-dig-at-us-president-hours-after-ceasefire-article-154028862) | timesnownews.com | 9 | negative |
| 8 Apr 2026 | [Iran claims victory in war with US after ceasefire but has a warning](https://www.ibtimes.co.in/iran-claims-victory-war-us-after-ceasefire-has-warning-900730) | ibtimes.co.in | 9 | negative |
| 5 Apr 2026 | [ATAQUE al CORAZÓN ENERGÉTICO de IRÁN: 5 MUERTOS y 170 HERIDOS](https://flipr.com.ar/nacionales/streaming/c5n/ataque-al-corazon-energetico-de-iran-5-muertos-y-170-heridos/) | flipr.com.ar | 9 | — |
| 16 Mar 2026 | [News Wrap: North Korea warns against U.S. aggression with th](https://www.pbssocal.org/shows/newshour/clip/news-wrap-north-korea-warns-against-u-s-aggression-with-threat-to-strike-1492027089) | pbssocal.org | 9 | negative |
| 1 Mar 2026 | [Agencia internacional desmiente a Grok tras afirmar que video de ataque a IrÃ¡n corresponde a 2021](https://www.biobiochile.cl/noticias/internacional/mediooriente/2026/03/01/agencia-internacional-desmiente-a-grok-tras-afirmar-que-video-de-ataque-a-iran-corresponde-a-2021.shtml) | biobiochile.cl | 9 | negative |
| 28 Feb 2026 | [Trump Exposed as Hypocrite by His Own Iran War Doomsday Warnings](https://www.thedailybeast.com/donald-trump-warned-us-how-desperate-it-would-be-to-attack-iran/) | thedailybeast.com | 9 | negative |
| 28 Jan 2026 | [X permite publicaÃ§Ãµes de vÃ­deos que simulam estupros apesar de polÃ­ticas internas de seguranÃ§a](https://www1.folha.uol.com.br/tec/2026/01/x-permite-publicacoes-de-videos-que-simulam-estupros-apesar-de-politicas-internas-de-seguranca.shtml) | folha.uol.com.br | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "Twitter" --since 2026-01-01 --until 2026-04-30
prism-news trends "Twitter" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "Twitter" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "Twitter", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "Twitter", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Wearables News](wearables-news.md)
- [Smartphones News](smartphones-news.md)
- [AI Startups News](ai-startups-news.md)
- [Web3 News](web3-news.md)
