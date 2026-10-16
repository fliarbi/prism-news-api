# GDP News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gdp news” · 1,000/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gdp-news.json](../../examples/scenarios/gdp-news.json).

**Question.** What did the news say about gdp between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="GDP"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,655 |
| Negative · neutral · positive | 40% · 2.8% · 57% |
| Critical (priority 7–9) | 71% (9,030 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,291 articles) |
| Most-reported country | China (10% of matches) |
| Strongest theme by lift | economy news: gdp growth reports |

## Twelve months of coverage

Monthly matching articles for `GDP` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,653 | 67% | 1,954 | 1,545 | █████████████████ |
| Jun 2025 | 2,927 | 69% | 1,541 | 1,218 | ██████████████ |
| Jul 2025 | 2,626 | 71% | 1,242 | 1,302 | ████████████ |
| Aug 2025 | 2,644 | 77% | 1,137 | 1,406 | ████████████ |
| Sep 2025 | 2,707 | 75% | 1,073 | 1,559 | █████████████ |
| Oct 2025 | 2,176 | 76% | 980 | 1,136 | ██████████ |
| Nov 2025 | 2,103 | 78% | 819 | 1,224 | ██████████ |
| Dec 2025 | 2,740 | 73% | 1,034 | 1,596 | █████████████ |
| Jan 2026 | 2,605 | 78% | 908 | 1,632 | ████████████ |
| Feb 2026 | 3,317 | 80% | 1,323 | 1,905 | ███████████████ |
| Mar 2026 | 2,442 | 76% | 1,192 | 1,152 | ███████████ |
| Apr 2026 | 4,291 | 58% | 1,639 | 2,544 | ████████████████████ |

The last four complete months averaged 3,164 articles a month against 2,962 in the first four (+7%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| China | 1,321 | 10% |
| India | 1,285 | 10% |
| United States | 1,253 | 9.9% |
| United Kingdom | 216 | 1.7% |
| Nigeria | 190 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: gdp growth reports | 2,243 | 29% | +26% |
| economy news: economic forecast revisions | 649 | 8.3% | +45% |
| economy news: productivity and efficiency trends | 308 | 3.9% | +34% |
| economy news: government debt levels | 740 | 9.4% | +34% |
| economy news: fiscal policy updates | 820 | 10% | +29% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Growing GDP, thank GPT](https://www.marketplace.org/episode/2026/04/30/growing-gdp-thank-gpt) | marketplace.org | 8 | positive |
| 30 Apr 2026 | [US Public Debt Surpasses National Economic Output](https://world.infonasional.com/us-debt-exceeds-gdp-milestone) | world.infonasional.com | 8 | negative |
| 30 Apr 2026 | [America’s Debt Just Hit Grim Milestone After Decades Of Politicians Spending Like Drunken Sailors \| U. S.…](https://beforeitsnews.com/u-s-politics/2026/04/americas-debt-just-hit-grim-milestone-after-decades-of-politicians-spending-like-drunken-sailors-2628486.html) | beforeitsnews.com | 8 | negative |
| 28 Apr 2026 | [WTTC says Middle East travel growth beats global average as Saudi Arabia leads expansion](https://travel.economictimes.indiatimes.com/news/research-and-statistics/research/saudi-arabia-leads-middle-east-travel-growth-surpassing-global-average/130575600) | travel.economictimes.indiatimes.com | 8 | positive |
| 28 Apr 2026 | [L’Inde : un marché prometteur pour nos exportateurs](http://www.edc.ca/fr/article/affaires-inde-conseils-importateurs-exportateurs.html) | edc.ca | 8 | positive |
| 28 Apr 2026 | [Nepal’s growth holds steady at 3.85 percent despite shocks](https://kathmandupost.com/money/2026/04/28/nepal-s-growth-holds-steady-at-3-85-percent-despite-shocks) | kathmandupost.com | 8 | negative |
| 25 Apr 2026 | [UEMOA \| L'endettement Galopant, Une Bombe à Retardement Pour La](https://maliactu.net/uemoa-l-endettement-galopant-une-bombe-a-retardement-pour-la-souverainete-africaine/) | maliactu.net | 8 | negative |
| 24 Apr 2026 | [Russland droht andauernde Wirtschaftsflaute](https://de.finance.yahoo.com/nachrichten/russland-droht-andauernde-wirtschaftsflaute-030021304.html) | de.finance.yahoo.com | 8 | negative |
| 24 Apr 2026 | [Russlands Wirtschaft extrem unter Druck](https://www.gmx.net/magazine/politik/russland-krieg-ukraine/russlands-wirtschaft-extrem-druck-42188172) | gmx.net | 8 | negative |
| 23 Apr 2026 | [Germany halves 2026 growth forecast as Mideast tensions hit economy](https://www.thestar.com.my/news/world/2026/04/23/germany-halves-2026-growth-forecast-as-mideast-tensions-hit-economy) | thestar.com.my | 8 | negative |
| 23 Apr 2026 | [Jordan to access USD 200 million as it reaches agreement with IMF](https://internationalfinance.com/macroeconomy/jordan-access-usd-million-reaches-agreement-with-imf/) | internationalfinance.com | 8 | positive |
| 22 Apr 2026 | [IMF projects Ghana’s debt-to-GDP to rise to 53% by 2026 despite recent gains - Adomonline.com](https://www.adomonline.com/imf-projects-ghanas-debt-to-gdp-to-rise-to-53-by-2026-despite-recent-gains/) | adomonline.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "GDP" --since 2026-01-01 --until 2026-04-30
prism-news trends "GDP" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "GDP" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "GDP", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "GDP", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Stablecoin News](stablecoin-news.md)
- [ETF News](etf-news.md)
- [Credit Card News](credit-card-news.md)
- [Hedge Fund News](hedge-fund-news.md)
