# Rare Earths News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rare earths news” · 170/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rare-earths-news.json](../../examples/scenarios/rare-earths-news.json).

**Question.** How did rare earths coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="rare earths"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,219 |
| Negative · neutral · positive | 28% · 2.3% · 69% |
| Critical (priority 7–9) | 67% (1,485 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (1,464 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | rare earth metals extraction processes |

## Twelve months of coverage

Monthly matching articles for `rare earths` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 264 | 60% | 103 | 158 | ████ |
| Jun 2025 | 578 | 72% | 342 | 225 | ████████ |
| Jul 2025 | 429 | 66% | 187 | 233 | ██████ |
| Aug 2025 | 388 | 69% | 171 | 210 | █████ |
| Sep 2025 | 292 | 75% | 90 | 195 | ████ |
| Oct 2025 | 1,464 | 82% | 833 | 593 | ████████████████████ |
| Nov 2025 | 471 | 72% | 207 | 253 | ██████ |
| Dec 2025 | 379 | 70% | 131 | 237 | █████ |
| Jan 2026 | 513 | 69% | 196 | 300 | ███████ |
| Feb 2026 | 696 | 70% | 184 | 499 | ██████████ |
| Mar 2026 | 460 | 69% | 110 | 340 | ██████ |
| Apr 2026 | 550 | 58% | 139 | 399 | ████████ |

The last four complete months averaged 555 articles a month against 415 in the first four (+34%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 472 | 21% |
| China | 140 | 6.3% |
| India | 80 | 3.6% |
| Australia | 67 | 3.0% |
| Brazil | 62 | 2.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| rare earth metals extraction processes | 574 | 42% | +5% |
| mineral exploration drilling techniques | 159 | 12% | +46% |
| global metal supply chain logistics | 221 | 16% | -1% |
| mining project financing and investment | 89 | 6.5% | +98% |
| industrial mineral exploration methods | 73 | 5.3% | +170% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Xi’s rare earth card gives China $1.2 trillion leverage before Trump summit](https://www.chinapulse.com/data-news/2026/04/29/xis-rare-earth-card-gives-china-1-2-trillion-leverage-before-trump-summit/) | chinapulse.com | 8 | negative |
| 13 Apr 2026 | [To compete with China, US needs to rebuild rare earth talent from the ground up](https://www.scmp.com/news/china/diplomacy/article/3349894/compete-china-us-needs-rebuild-rare-earth-talent-ground) | scmp.com | 8 | negative |
| 8 Apr 2026 | [Trump-Xi Meeting to Focus on Trade Stability](https://stratnewsglobal.com/world-news/trump-xi-meeting-to-focus-on-trade-stability/) | stratnewsglobal.com | 8 | negative |
| 7 Apr 2026 | [Trump will pursue stability with China’s Xi in May meeting, USTR Greer says](http://www.straitstimes.com/world/united-states/ustr-greer-says-economic-relationship-with-china-is-stable) | straitstimes.com | 8 | negative |
| 1 Apr 2026 | [Japan, France mull rare earths deal to cut China reliance, Nikkei reports](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/04/01/japan-france-mull-rare-earths-deal-to-cut-china-reliance-nikkei-reports) | thestar.com.my | 8 | positive |
| 24 Mar 2026 | [China continues to dominate rare earths as diversification efforts gain momentum](https://www.mining-technology.com/analyst-comment/china-dominate-rare-earths/) | mining-technology.com | 8 | negative |
| 19 Mar 2026 | [Washington Signs Rare Earths Pact With Goiás State, Not Lula](https://www.riotimesonline.com/brazil-rare-earths-us-goias-critical-minerals/) | riotimesonline.com | 8 | negative |
| 21 Feb 2026 | [Brazil, India eye critical minerals deal as leaders meet](http://www.dhakatribune.com/world/south-asia/403827/brazil-india-eye-critical-minerals-deal-as) | dhakatribune.com | 8 | positive |
| 21 Feb 2026 | [PM Modi to meet Brazilian President Lula da Silva today in Delhi to boost cooperation: Key details \| Today…](https://www.livemint.com/news/india/narendra-modi-lula-da-silva-meeting-key-agenda-india-brazil-ties-bilateral-trade-11771640436607.html) | livemint.com | 8 | positive |
| 9 Feb 2026 | [Get digital access to India Today Hindi - February 18, 2026 issue \| Magzter.com](https://www.magzter.com/IN/India-Today-Group/India-Today-Hindi/News/2329970) | magzter.com | 8 | positive |
| 4 Feb 2026 | [What are 'rare earths' for?](https://economictimes.indiatimes.com/news/international/world-news/what-are-rare-earths-for/articleshow/127902930.cms) | economictimes.indiatimes.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "rare earths" --since 2026-01-01 --until 2026-04-30
prism-news trends "rare earths" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "rare earths" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "rare earths", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "rare earths", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Nuclear Power News](nuclear-power-news.md)
- [LNG News](lng-news.md)
- [Diesel Price News](diesel-price-news.md)
- [El Nino News](el-nino-news.md)
