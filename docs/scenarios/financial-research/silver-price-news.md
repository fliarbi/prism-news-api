# Silver Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “silver price news” · 9,900/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [silver-price-news.json](../../examples/scenarios/silver-price-news.json).

**Question.** What did the news say about silver price between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="silver price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,428 |
| Negative · neutral · positive | 48% · 0.8% · 51% |
| Critical (priority 7–9) | 10% (145 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (463 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | derivatives trading (futures, options) |

## Twelve months of coverage

Monthly matching articles for `silver price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 117 | 18% | 82 | 35 | █████ |
| Jun 2025 | 111 | 12% | 47 | 62 | █████ |
| Jul 2025 | 116 | 5.2% | 46 | 64 | █████ |
| Aug 2025 | 116 | 9.5% | 36 | 73 | █████ |
| Sep 2025 | 173 | 5.8% | 35 | 137 | ███████ |
| Oct 2025 | 238 | 10% | 75 | 158 | ██████████ |
| Nov 2025 | 126 | 14% | 44 | 77 | █████ |
| Dec 2025 | 240 | 5.0% | 68 | 169 | ██████████ |
| Jan 2026 | 267 | 9.0% | 86 | 181 | ████████████ |
| Feb 2026 | 355 | 10% | 197 | 155 | ███████████████ |
| Mar 2026 | 343 | 9.0% | 173 | 168 | ███████████████ |
| Apr 2026 | 463 | 12% | 233 | 223 | ████████████████████ |

The last four complete months averaged 357 articles a month against 115 in the first four (+210%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 247 | 17% |
| India | 226 | 16% |
| Iran | 57 | 4.0% |
| China | 24 | 1.7% |
| Nepal | 12 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| derivatives trading (futures, options) | 498 | 41% | +76% |
| precious metal spot prices | 235 | 19% | +5% |
| commodity trading and price changes | 741 | 61% | +74% |
| precious metals trading trends (gold, silver, platinum) | 399 | 33% | -3% |
| market sentiment and investor behavior | 190 | 16% | +533% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Silber: Frist läuft ab!](https://www.boerse-express.com/news/articles/silber-frist-laeuft-ab-893069) | boerse-express.com | 8 | negative |
| 19 Feb 2026 | [Huge Jump in Gold Rate Today in India by Around Rs 23,000 per 100g of 24K After Recent Dip; Silver Price Rises](https://www.goodreturns.in/news/huge-jump-in-gold-rate-today-in-india-by-around-rs23000-per-24k-after-recent-dip-silver-price-rises-1490555.html) | goodreturns.in | 8 | negative |
| 21 Apr 2026 | [Gold Price Today: सोने का रेट 12586 रुपये बढ़ा, 1 महीने में चांदी की कीमतों 30803 रुपये की उछाल, चेक करें आज…](https://www.livehindustan.com/business/gold-price-today-in-last-one-month-gold-12586-rupee-jumped-and-silver-price-surged-30803-rupee-201776757020753.html) | livehindustan.com | 7 | positive |
| 19 Apr 2026 | [Akshaya Tritiya Gold Demand: ₹20000Cr की होगी बिक्री! सोना-चांदी महंगा, फिर भी अक्षय तृतीया पर तगड़ी डिमांड](https://www.aajtak.in/business/news/story/gold-silver-demand-more-than-20000-crore-rupee-trading-on-akshaya-tritiya-tutc-dskc-2527819-2026-04-19) | aajtak.in | 7 | positive |
| 13 Apr 2026 | [Silver holds majority losses near $74 as fears of hawkish Fed outlook revives](https://bitcoinethereumnews.com/finance/silver-holds-majority-losses-near-74-as-fears-of-hawkish-fed-outlook-revives/) | bitcoinethereumnews.com | 7 | negative |
| 10 Apr 2026 | [Silver Price Forecast: XAG/USD wobbles around $75 in countdown to US-Iran talks](https://bitcoinethereumnews.com/finance/silver-price-forecast-xag-usd-wobbles-around-75-in-countdown-to-us-iran-talks/) | bitcoinethereumnews.com | 7 | negative |
| 9 Apr 2026 | [Silver Price Forecast: XAG/USD trades flat around $74 ahead of US-Iran talks](https://bitcoinethereumnews.com/finance/silver-price-forecast-xag-usd-trades-flat-around-74-ahead-of-us-iran-talks/) | bitcoinethereumnews.com | 7 | negative |
| 31 Mar 2026 | [Silver jumps above $73 as Trump shows readiness for peace with Iran](https://bitcoinethereumnews.com/finance/silver-jumps-above-73-as-trump-shows-readiness-for-peace-with-iran/) | bitcoinethereumnews.com | 7 | negative |
| 28 Mar 2026 | [सोना इस हफ्ते ₹4,276 सस्ता, ₹1.43 लाख पर आया: चांदी ₹10,717 गिरकर ₹2.21 लाख पर पहुंची, डॉलर की डिमांड बढ़ने…](http://www.bhaskar.com/business/news/gold-silver-prices-fall-dollar-demand-boosts-rates-2026-137552088.html) | bhaskar.com | 7 | negative |
| 17 Feb 2026 | [XAG/USD tumbles to near $74 as dovish Fed bets remain confined](https://bitcoinethereumnews.com/finance/xag-usd-tumbles-to-near-74-as-dovish-fed-bets-remain-confined/) | bitcoinethereumnews.com | 7 | negative |
| 17 Feb 2026 | [XAG/USD drops to near $76.00 while investors await FOMC Minutes](https://bitcoinethereumnews.com/finance/xag-usd-drops-to-near-76-00-while-investors-await-fomc-minutes/) | bitcoinethereumnews.com | 7 | negative |
| 16 Feb 2026 | [XAG/USD declines to near $75 at the start of the week](https://bitcoinethereumnews.com/finance/xag-usd-declines-to-near-75-at-the-start-of-the-week/) | bitcoinethereumnews.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "silver price" --since 2026-01-01 --until 2026-04-30
prism-news trends "silver price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "silver price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "silver price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "silver price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through 24 Aug 2026; intake thins after May 2026.
- `q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- zero-count periods are included; partial_period marks buckets the window only partly covers
- Country shares use all matching articles. Location information is incomplete and varies by period.
- Theme shares use articles with identified themes; articles may have more than one theme.

## Related demonstrations

- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Mortgage Rates News](mortgage-rates-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
- [Interest Rates News](interest-rates-news.md)
