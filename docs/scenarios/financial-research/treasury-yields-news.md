# Treasury Yields News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “treasury yields news” · 50/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [treasury-yields-news.json](../../examples/scenarios/treasury-yields-news.json).

**Question.** What did the news say about treasury yields between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="treasury yields"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 688 |
| Negative · neutral · positive | 57% · 1.2% · 41% |
| Critical (priority 7–9) | 57% (395 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (330 articles) |
| Most-reported country | United States (33% of matches) |
| Strongest theme by lift | market sentiment and investor behavior |

## Twelve months of coverage

Monthly matching articles for `treasury yields` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 330 | 72% | 230 | 97 | ████████████████████ |
| Jun 2025 | 123 | 60% | 90 | 31 | ███████ |
| Jul 2025 | 120 | 48% | 59 | 61 | ███████ |
| Aug 2025 | 166 | 60% | 79 | 85 | ██████████ |
| Sep 2025 | 191 | 71% | 114 | 77 | ████████████ |
| Oct 2025 | 105 | 74% | 71 | 33 | ██████ |
| Nov 2025 | 93 | 62% | 55 | 37 | ██████ |
| Dec 2025 | 190 | 67% | 116 | 69 | ████████████ |
| Jan 2026 | 125 | 74% | 77 | 47 | ████████ |
| Feb 2026 | 167 | 52% | 79 | 88 | ██████████ |
| Mar 2026 | 253 | 59% | 171 | 78 | ███████████████ |
| Apr 2026 | 143 | 46% | 68 | 72 | █████████ |

The last four complete months averaged 172 articles a month against 185 in the first four (-7%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 229 | 33% |
| Iran | 45 | 6.5% |
| India | 17 | 2.5% |
| China | 12 | 1.7% |
| United Arab Emirates | 6 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market sentiment and investor behavior | 136 | 23% | +183% |
| foreign exchange (forex) rate fluctuations | 124 | 21% | +182% |
| central bank monetary policy announcements | 250 | 42% | -3% |
| market volatility and risk assessment | 155 | 26% | +198% |
| european central bank (ecb) decisions | 150 | 25% | -7% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 13 Apr 2026 | [Treasury yields are little changed as collapse of Iran talks clouds inflation outlook - IndiaVision India…](https://www.indiavision.com/business/treasury-yields-are-little-changed-as-collapse-of-iran-talks-clouds-inflation-outlook/601509/) | indiavision.com | 8 | negative |
| 31 Mar 2026 | [Analysis-Treasury market's next test: rising war costs](https://finance.yahoo.com/economy/policy/articles/analysis-treasury-markets-next-test-100526857.html) | finance.yahoo.com | 8 | negative |
| 25 Mar 2026 | [US Dollar Stable, Risks Remain On Diplomatic Hopes](https://businessnewsthisweek.com/business/us-dollar-stable-risks-remain-on-diplomatic-hopes/) | businessnewsthisweek.com | 8 | negative |
| 24 Mar 2026 | [Bank of America Stock Price Jumps 1.4%: Why BAC Rose While Wall Street Fell](https://ts2.tech/en/bank-of-america-stock-price-jumps-1-4-why-bac-rose-while-wall-street-fell/) | ts2.tech | 8 | negative |
| 24 Mar 2026 | [Wall Street indexes mixed on rising yields, worries about Middle East war \| Stock Market News](https://www.livemint.com/market/wall-street-indexes-mixed-on-rising-yields-worries-about-middle-east-war-11774378412615.html) | livemint.com | 8 | negative |
| 13 Mar 2026 | [Why the real market shock is in long bonds](https://malaysia.news.yahoo.com/why-the-real-market-shock-is-in-long-bonds-200720064.html) | malaysia.news.yahoo.com | 8 | negative |
| 12 Mar 2026 | [Treasury Yields Hold Above 4% as Oil Tensions, Fed Politics Rattle Bond Market](https://news.bitcoin.com/treasury-yields-hold-above-4-as-oil-tensions-fed-politics-rattle-bond-market/) | news.bitcoin.com | 8 | negative |
| 6 Feb 2026 | [**Duration Divergence: Bond Markets Signal Disbelief in the Fed’s Inflation Narrative** While the Federal…](https://cremarketbeat.com/bond-market-signals-doubt-in-feds-inflation-outlook-through-duration-divergence/) | cremarketbeat.com | 8 | negative |
| 24 Jan 2026 | [Treasury Yields Jump: Investors Monitor Bond Market Volatility Amid Geopolitical Concerns](https://world.infonasional.com/treasury-yields-jump-bond-market-volatility) | world.infonasional.com | 8 | negative |
| 20 Jan 2026 | [India bonds tick up; high US yields cap RBI buying hope](https://bfsi.economictimes.indiatimes.com/news/industry/india-bonds-tick-up-high-us-yields-cap-rbi-buying-hope/126800163) | bfsi.economictimes.indiatimes.com | 8 | positive |
| 19 Jan 2026 | [India bonds track U.S. debt lower, overlooking state supply cut](https://bfsi.economictimes.indiatimes.com/news/financial-services/india-bonds-decline-amid-rising-us-treasury-yields-despite-lower-state-debt-supply/126669082) | bfsi.economictimes.indiatimes.com | 8 | negative |
| 2 Jan 2026 | [Wall Street ends mixed at the top of the new year; Treasury yields move higher](https://za.investing.com/news/stock-market-news/stocks-make-upbeat-start-to-2026-precious-metals-extend-sparkling-rally-4044571) | za.investing.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "treasury yields" --since 2026-01-01 --until 2026-04-30
prism-news trends "treasury yields" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "treasury yields" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "treasury yields", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "treasury yields", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Unemployment News](unemployment-news.md)
- [Retirement News](retirement-news.md)
- [Yen News](yen-news.md)
- [Market Crash News](market-crash-news.md)
