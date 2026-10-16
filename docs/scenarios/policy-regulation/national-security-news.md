# National Security News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “national security news” · 20/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [national-security-news.json](../../examples/scenarios/national-security-news.json).

**Question.** How did coverage of national security develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="national security"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 32,463 |
| Negative · neutral · positive | 71% · 3.9% · 25% |
| Critical (priority 7–9) | 86% (27,895 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (10,611 articles) |
| Most-reported country | United States (32% of matches) |
| Strongest theme by lift | mobile phone storage solutions |

## Twelve months of coverage

Monthly matching articles for `national security` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8,943 | 71% | 5,381 | 2,077 | █████████████████ |
| Jun 2025 | 5,067 | 82% | 3,536 | 1,294 | ██████████ |
| Jul 2025 | 6,885 | 68% | 4,912 | 1,548 | █████████████ |
| Aug 2025 | 10,611 | 59% | 5,344 | 2,402 | ████████████████████ |
| Sep 2025 | 5,681 | 81% | 3,672 | 1,578 | ███████████ |
| Oct 2025 | 5,622 | 83% | 3,664 | 1,648 | ███████████ |
| Nov 2025 | 4,783 | 84% | 3,085 | 1,400 | █████████ |
| Dec 2025 | 8,201 | 69% | 4,465 | 1,947 | ███████████████ |
| Jan 2026 | 6,924 | 78% | 4,653 | 1,814 | █████████████ |
| Feb 2026 | 7,314 | 86% | 4,844 | 2,177 | ██████████████ |
| Mar 2026 | 8,355 | 89% | 6,169 | 1,925 | ████████████████ |
| Apr 2026 | 9,870 | 89% | 7,473 | 2,121 | ███████████████████ |

The last four complete months averaged 8,116 articles a month against 7,876 in the first four (+3%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 10,512 | 32% |
| India | 1,700 | 5.2% |
| China | 749 | 2.3% |
| Iran | 685 | 2.1% |
| Nigeria | 608 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone storage solutions | 406 | 1.9% | -73% |
| cybersecurity protocols for defense infrastructure | 378 | 1.8% | +200% |
| mobile phone camera technology | 511 | 2.4% | -73% |
| mobile phone hardware components | 247 | 1.2% | -77% |
| mobile phone battery performance | 238 | 1.1% | -76% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [Evening Brief: A Green Beret’s $400K Bet on the Maduro Raid Blows Up](https://sofrep.com/news/evening-brief-a-green-berets-400k-bet-on-maduro-raid-blows-up/) | sofrep.com | 9 | negative |
| 20 Apr 2026 | [FBI urged to hunt for 'sinister' truth behind 11 vanished nuclear boffins](https://www.dailystar.co.uk/news/us-news/fbi-urged-hunt-sinister-truth-37044395) | dailystar.co.uk | 9 | negative |
| 20 Apr 2026 | [Donald Trump’s Threat to Iran Is Not ‘War Crime’, Says Mike Waltz](https://www.yahoo.com/news/articles/donald-trump-threat-iran-not-081101811.html) | yahoo.com | 9 | negative |
| 13 Apr 2026 | ['We will need to brace ourselves for a bumpy ride': Shanmugam explains consequences of the Middle East…](https://www.asiaone.com/singapore/we-will-need-brace-ourselves-bumpy-ride-shanmugam-explains-consequences-middle-east) | asiaone.com | 9 | negative |
| 10 Apr 2026 | [China supercomputer breach exposes massive defence data, sparks security concerns](https://economictimes.indiatimes.com/magazines/panache/china-supercomputer-breach-exposes-massive-defence-data-sparks-security-concerns/articleshow/130164411.cms) | economictimes.indiatimes.com | 9 | negative |
| 9 Apr 2026 | [Florida AG to probe OpenAI, alleging possible connection to FSU shooting \| TechCrunch](https://techcrunch.com/2026/04/09/florida-ag-to-probe-openai-alleging-possible-connection-to-fsu-shooting/) | techcrunch.com | 9 | negative |
| 8 Apr 2026 | [Iran Parliament calls to halt Strait of Hormuz shipping amid Lebanon conflict - Business Upturn](https://www.businessupturn.com/world/iran-parliament-calls-to-halt-strait-of-hormuz-shipping-amid-lebanon-conflict/) | businessupturn.com | 9 | negative |
| 7 Apr 2026 | [Trump F-15 Leak Row: US President Threatens Media Crackdown, Says ‘Give It Up Or Go To Jail’](https://news.abplive.com/news/world/trump-to-find-f-15-leak-iran-israel-war-us-president-threatens-media-crackdown-says-give-it-up-or-go-to-jail-1834994) | news.abplive.com | 9 | negative |
| 6 Apr 2026 | [Trump and top officials share new details of rescue of U.S. airmen from Iran](https://www.cbsnews.com/texas/news/trump-news-conference-iran/) | cbsnews.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "national security" --since 2026-01-01 --until 2026-04-30
prism-news trends "national security" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "national security" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "national security", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "national security", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [WTO News](wto-news.md)
- [Labour Law News](labour-law-news.md)
- [Climate Policy News](climate-policy-news.md)
- [Make in India News](make-in-india-news.md)
