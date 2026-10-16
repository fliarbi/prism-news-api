# IMF News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “imf news” · 320/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [imf-news.json](../../examples/scenarios/imf-news.json).

**Question.** What did the news say about imf between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="IMF"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,802 |
| Negative · neutral · positive | 60% · 3.8% · 36% |
| Critical (priority 7–9) | 82% (9,685 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (6,361 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | economy news: economic forecast revisions |

## Twelve months of coverage

Monthly matching articles for `IMF` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,643 | 76% | 2,052 | 1,496 | ███████████ |
| Jun 2025 | 1,502 | 76% | 811 | 651 | █████ |
| Jul 2025 | 2,210 | 71% | 1,177 | 990 | ███████ |
| Aug 2025 | 1,539 | 79% | 877 | 615 | █████ |
| Sep 2025 | 1,675 | 76% | 881 | 745 | █████ |
| Oct 2025 | 3,296 | 74% | 1,521 | 1,702 | ██████████ |
| Nov 2025 | 1,609 | 85% | 812 | 761 | █████ |
| Dec 2025 | 1,624 | 83% | 816 | 768 | █████ |
| Jan 2026 | 1,962 | 84% | 917 | 1,005 | ██████ |
| Feb 2026 | 1,876 | 83% | 965 | 853 | ██████ |
| Mar 2026 | 1,603 | 83% | 1,001 | 566 | █████ |
| Apr 2026 | 6,361 | 81% | 4,231 | 1,800 | ████████████████████ |

The last four complete months averaged 2,950 articles a month against 2,224 in the first four (+33%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,465 | 21% |
| India | 518 | 4.4% |
| Pakistan | 311 | 2.6% |
| China | 281 | 2.4% |
| United Kingdom | 229 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: economic forecast revisions | 352 | 4.5% | +132% |
| economy news: central bank quantitative easing policies | 756 | 9.6% | +76% |
| economy news: gdp growth reports | 814 | 10% | +80% |
| economy news: fiscal policy updates | 794 | 10% | +33% |
| economy news: government debt levels | 650 | 8.3% | +26% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [War-linked energy shock pushing inflation higher in Europe: IMF expert](https://www.fibre2fashion.com/news/economics/war-linked-energy-shock-pushing-inflation-higher-in-europe-imf-expert-309803-newsdetails.htm) | fibre2fashion.com | 9 | negative |
| 17 Apr 2026 | [Chancellor says ‘no issue’ with fuel supply after energy boss's six-week warning](https://travelweekly.co.uk/news/europe-has-maybe-six-weeks-of-jet-fuel-left-warns-energy-boss) | travelweekly.co.uk | 9 | negative |
| 16 Apr 2026 | [Día 48 de la guerra entre Estados Unidos, Israel e Irán: todo lo que hay que saber](https://www.lanacion.com.ar/el-mundo/dia-48-de-la-guerra-entre-estados-unidos-israel-e-iran-todo-lo-que-hay-que-saber-nid16042026/) | lanacion.com.ar | 9 | negative |
| 15 Apr 2026 | [Iran war escalation could push global economy to brink of recession, IMF warns - Türkiye Today](https://www.turkiyetoday.com/business/iran-war-escalation-could-push-global-economy-to-brink-of-recession-imf-warns-3218153) | turkiyetoday.com | 9 | negative |
| 14 Apr 2026 | [Petrol, energy bills and mortgages - how 'Trumpflation' will impact you](https://inews.co.uk/news/politics/three-ways-trumpflation-your-pocket-4354162) | inews.co.uk | 9 | negative |
| 14 Apr 2026 | [IMF slashes UK economic growth forecasts as Iran war risks global recession](https://www.thenational.scot/news/26020925.imf-slashes-uk-economic-growth-forecasts-iran-war-risks-global-recession/) | thenational.scot | 9 | negative |
| 14 Apr 2026 | [Iran war wreaks havoc on global economy and could spark recession, says IMF](https://www.middleeasteye.net/news/iran-war-wreaks-havoc-global-economy-and-could-spark-recession-says-imf) | middleeasteye.net | 9 | negative |
| 14 Apr 2026 | [IMF warns of inflation surge, growth slump if Strait of Hormuz remains shut](https://www.abc.net.au/news/2026-04-15/international-monetary-fund-world-economic-outlook-iran-war/106564598) | abc.net.au | 9 | negative |
| 14 Apr 2026 | [UK economic growth forecasts slashed as IMF says Iran war risks global recession](https://www.edp24.co.uk/news/national/26020326.uk-economic-growth-forecasts-slashed-imf-says-iran-war-risks-global-recession/) | edp24.co.uk | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "IMF" --since 2026-01-01 --until 2026-04-30
prism-news trends "IMF" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "IMF" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "IMF", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "IMF", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Market Crash News](market-crash-news.md)
- [Tax News Today](tax-news-today.md)
- [NBFC News](nbfc-news.md)
