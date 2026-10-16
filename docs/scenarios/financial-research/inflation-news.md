# Inflation News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “inflation news” · 590/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [inflation-news.json](../../examples/scenarios/inflation-news.json).

**Question.** What did the news say about inflation between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="inflation"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 88,963 |
| Negative · neutral · positive | 67% · 4.1% · 29% |
| Critical (priority 7–9) | 68% (60,876 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (30,591 articles) |
| Most-reported country | United States (20% of matches) |
| Strongest theme by lift | economy news: inflation rate analysis |

## Twelve months of coverage

Monthly matching articles for `inflation` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 16,010 | 60% | 9,776 | 5,400 | ██████████ |
| Jun 2025 | 10,990 | 66% | 6,484 | 3,963 | ███████ |
| Jul 2025 | 14,725 | 57% | 9,380 | 4,805 | ██████████ |
| Aug 2025 | 14,801 | 64% | 8,989 | 5,179 | ██████████ |
| Sep 2025 | 15,673 | 65% | 8,812 | 6,166 | ██████████ |
| Oct 2025 | 13,409 | 68% | 7,759 | 5,187 | █████████ |
| Nov 2025 | 12,431 | 68% | 7,229 | 4,710 | ████████ |
| Dec 2025 | 15,147 | 65% | 8,486 | 5,979 | ██████████ |
| Jan 2026 | 13,877 | 68% | 7,875 | 5,455 | █████████ |
| Feb 2026 | 17,562 | 67% | 10,580 | 6,146 | ███████████ |
| Mar 2026 | 26,933 | 72% | 20,098 | 5,827 | ██████████████████ |
| Apr 2026 | 30,591 | 67% | 21,087 | 8,163 | ████████████████████ |

The last four complete months averaged 22,241 articles a month against 14,132 in the first four (+57%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 45% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 17,993 | 20% |
| India | 4,478 | 5.0% |
| Iran | 3,432 | 3.9% |
| United Kingdom | 2,202 | 2.5% |
| Australia | 1,022 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: inflation rate analysis | 12,978 | 21% | +59% |
| market sentiment and investor behavior | 3,991 | 6.6% | +223% |
| economy news: central bank interest rate decisions | 6,952 | 11% | +21% |
| economy news: monetary policy changes | 6,905 | 11% | +22% |
| foreign exchange (forex) rate fluctuations | 3,455 | 5.7% | +124% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Portion of road to close for 1 week in Moraine](https://www.yahoo.com/news/articles/portion-road-close-1-week-072959599.html) | yahoo.com | 9 | negative |
| 22 Apr 2026 | [War-linked energy shock pushing inflation higher in Europe: IMF expert](https://www.fibre2fashion.com/news/economics/war-linked-energy-shock-pushing-inflation-higher-in-europe-imf-expert-309803-newsdetails.htm) | fibre2fashion.com | 9 | negative |
| 21 Apr 2026 | [Government predicts €1.2bn budget deficit and says inflation could reach 6.7% in 2026](http://www.irishexaminer.com/news/politics/arid-41831243.html) | irishexaminer.com | 9 | negative |
| 20 Apr 2026 | [Iranians Fear No Relief After War Ends](https://www.ibtimes.sg/calm-streets-cafes-reopen-rising-fears-repression-grip-even-after-war-iran-85527) | ibtimes.sg | 9 | negative |
| 16 Apr 2026 | [Mit dem Unglück leben – die einfachen Russen und ihre ganz normale Misere](https://www.nzz.ch/feuilleton/zunehmender-frust-die-einfachen-russen-beginnen-zu-ahnen-dass-ihre-misere-auch-mit-dem-krieg-zusammenhaengt-ld.1932570) | nzz.ch | 9 | negative |
| 11 Apr 2026 | [Opinião de Jorge Noutel: A injustiça, a ganância, o louco e a catástrofe - Jornal o Interior](https://www.ointerior.pt/opiniao/opiniao-de-jorge-noutel-a-injustica-a-ganancia-o-louco-e-a-catastrofe/) | ointerior.pt | 9 | negative |
| 10 Apr 2026 | [IMF Warns Iran War Will Leave Lasting Scars on Global Economy \| OilPrice.com](https://oilprice.com/Energy/Energy-General/IMF-Warns-Iran-War-Will-Leave-Lasting-Scars-on-Global-Economy.html) | oilprice.com | 9 | negative |
| 9 Apr 2026 | [Fuel shortages and inflation: IMF warns of ‘scarring’ harm from war](https://www.cityam.com/fuel-shortages-hunger-inflation-spiral-imf-fears-scarring-harm-from-iran-war/) | cityam.com | 9 | negative |
| 7 Apr 2026 | [Singapore's overall inflation for 2026 expected to rise amid ongoing Middle East conflict](https://www.asiaone.com/singapore/overall-inflation-2026-expected-rise-middle-east-conflict) | asiaone.com | 9 | negative |
| 4 Apr 2026 | [No end in sight to hip-pocket pain amid Middle East tensions](https://thewest.com.au/business/sean-smith-no-end-in-sight-to-hip-pocket-agony-amid-middle-east-tensions-c-22082868) | thewest.com.au | 9 | negative |
| 3 Apr 2026 | [Letter to the editor: Trump not Making America Great Again](https://triblive.com/opinion/letter-to-the-editor-trump-not-making-america-great-again/) | triblive.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "inflation" --since 2026-01-01 --until 2026-04-30
prism-news trends "inflation" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "inflation" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "inflation", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "inflation", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Income Tax News](income-tax-news.md)
- [Sensex News](sensex-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
- [Nasdaq News](nasdaq-news.md)
