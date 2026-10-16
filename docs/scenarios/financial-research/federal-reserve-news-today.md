# Federal Reserve News Today: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “federal reserve news today” · 140/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [federal-reserve-news-today.json](../../examples/scenarios/federal-reserve-news-today.json).

**Question.** What did the news say about federal reserve between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="federal reserve"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 46,732 |
| Negative · neutral · positive | 62% · 5.3% · 33% |
| Critical (priority 7–9) | 72% (33,719 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (16,633 articles) |
| Most-reported country | United States (45% of matches) |
| Strongest theme by lift | market sentiment and investor behavior |

## Twelve months of coverage

Monthly matching articles for `federal reserve` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8,201 | 75% | 5,177 | 2,721 | ██████████ |
| Jun 2025 | 6,560 | 73% | 4,071 | 2,194 | ████████ |
| Jul 2025 | 11,218 | 65% | 7,365 | 3,451 | █████████████ |
| Aug 2025 | 14,737 | 75% | 9,511 | 4,624 | ██████████████████ |
| Sep 2025 | 16,633 | 74% | 9,556 | 6,321 | ████████████████████ |
| Oct 2025 | 10,632 | 72% | 5,836 | 4,438 | █████████████ |
| Nov 2025 | 10,141 | 71% | 5,879 | 3,959 | ████████████ |
| Dec 2025 | 12,850 | 67% | 6,622 | 5,637 | ███████████████ |
| Jan 2026 | 11,217 | 70% | 6,216 | 4,358 | █████████████ |
| Feb 2026 | 10,904 | 68% | 6,422 | 4,031 | █████████████ |
| Mar 2026 | 10,988 | 74% | 7,761 | 2,733 | █████████████ |
| Apr 2026 | 13,623 | 76% | 8,583 | 4,156 | ████████████████ |

The last four complete months averaged 11,683 articles a month against 10,179 in the first four (+15%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 59% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 20,812 | 45% |
| Iran | 2,179 | 4.7% |
| India | 805 | 1.7% |
| China | 747 | 1.6% |
| United Kingdom | 381 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market sentiment and investor behavior | 4,007 | 13% | +60% |
| market volatility and risk assessment | 4,024 | 13% | +54% |
| bull and bear market transitions | 4,204 | 13% | +6% |
| foreign exchange (forex) rate fluctuations | 2,584 | 8.1% | -0% |
| central bank monetary policy announcements | 4,964 | 16% | -38% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Former FedEx driver pleads guilty to killing 7-year-old girl after making delivery at her Texas home](https://www.winnipegfreepress.com/world/2026/04/22/former-fedex-driver-pleads-guilty-to-killing-7-year-old-girl-after-making-delivery-at-her-texas-home-2) ⚠ | winnipegfreepress.com | 9 | negative |
| 22 Apr 2026 | [Oil, stocks fall as traders weigh outlook after Trump extends truce - Markets - The Jakarta Post](http://www.thejakartapost.com/business/2026/04/22/oil-stocks-fall-as-traders-weigh-outlook-after-trump-extends-truce.html) ⚠ | thejakartapost.com | 9 | negative |
| 21 Apr 2026 | [Trump's Iran ceasefire about-face: did Tehran snub the peace talks first?](https://bitcoinethereumnews.com/finance/trumps-iran-ceasefire-about-face-did-tehran-snub-the-peace-talks-first/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 20 Apr 2026 | [Trump’s Iran bomb warning puts oil, Bitcoin and crypto risk back in play](https://bitcoinethereumnews.com/bitcoin/trumps-iran-bomb-warning-puts-oil-bitcoin-and-crypto-risk-back-in-play/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 17 Apr 2026 | [Oil Drops Stocks Surge: Small Caps Lead the Rally](https://fintech.tv/eddie-ghabours-bullish-outlook-small-caps-industrials-semiconductors-and-software-sectors-to-outperform-the-sp-500/) ⚠ | fintech.tv | 9 | negative |
| 9 Apr 2026 | [Asian Markets Retreat as Gulf Crisis Fuels Oil Surge and Inflation Fears - EconoTimes](https://econotimes.com/Asian-Markets-Retreat-as-Gulf-Crisis-Fuels-Oil-Surge-and-Inflation-Fears-1738517) ⚠ | econotimes.com | 9 | negative |
| 8 Apr 2026 | [Former FedEx driver pleads guilty to killing 7-year-old Texas girl after delivery at her home](https://www.nbcnews.com/news/us-news/former-fedex-driver-pleads-guilty-killing-athena-strand-texas-rcna267365) ⚠ | nbcnews.com | 9 | negative |
| 8 Apr 2026 | [Former FedEx driver pleads guilty to killing 7-year-old girl after making delivery at her home - WBBJ TV](https://www.wbbjtv.com/2026/04/08/former-fedex-driver-pleads-guilty-to-killing-7-year-old-girl-after-making-delivery-at-her-home/) ⚠ | wbbjtv.com | 9 | negative |
| 8 Apr 2026 | [Former FedEx driver pleads guilty to killing 7-year-old girl after making delivery at her home](https://www.kswo.com/2026/04/08/former-fedex-driver-pleads-guilty-killing-7-year-old-girl-after-making-delivery-her-home/) ⚠ | kswo.com | 9 | negative |
| 7 Apr 2026 | [US Iran war news today: Trump's civilization warning](https://bitcoinethereumnews.com/tech/us-iran-war-news-today-trumps-civilization-warning/) ⚠ | bitcoinethereumnews.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "federal reserve" --since 2026-01-01 --until 2026-04-30
prism-news trends "federal reserve" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "federal reserve" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "federal reserve", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "federal reserve", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [RBI News](rbi-news.md)
- [Nifty News](nifty-news.md)
- [Mortgage Rates News](mortgage-rates-news.md)
- [Silver Price News](silver-price-news.md)
