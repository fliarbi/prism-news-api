# Crude Oil Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “crude oil price news” · 3,600/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [crude-oil-price-news.json](../../examples/scenarios/crude-oil-price-news.json).

**Question.** What did the news say about crude oil price between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="crude oil price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 407 |
| Negative · neutral · positive | 90% · 0.7% · 9.1% |
| Critical (priority 7–9) | 52% (213 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (172 articles) |
| Most-reported country | United States (34% of matches) |
| Strongest theme by lift | crude oil refining methods |

## Twelve months of coverage

Monthly matching articles for `crude oil price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 30 | 30% | 25 | 5 | ███ |
| Jun 2025 | 40 | 28% | 32 | 8 | █████ |
| Jul 2025 | 33 | 12% | 29 | 4 | ████ |
| Aug 2025 | 48 | 29% | 39 | 9 | ██████ |
| Sep 2025 | 29 | 17% | 28 | 1 | ███ |
| Oct 2025 | 27 | 11% | 20 | 7 | ███ |
| Nov 2025 | 25 | 4.0% | 25 | 0 | ███ |
| Dec 2025 | 39 | 18% | 34 | 3 | █████ |
| Jan 2026 | 38 | 10% | 36 | 2 | ████ |
| Feb 2026 | 28 | 54% | 26 | 2 | ███ |
| Mar 2026 | 172 | 60% | 160 | 12 | ████████████████████ |
| Apr 2026 | 169 | 53% | 145 | 21 | ████████████████████ |

The last four complete months averaged 102 articles a month against 38 in the first four (+170%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 55% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 138 | 34% |
| Iran | 34 | 8.3% |
| India | 18 | 4.4% |
| Pakistan | 8 | 2.0% |
| United Kingdom | 6 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| crude oil refining methods | 39 | 12% | +333% |
| petroleum distillation processes | 27 | 8.0% | +238% |
| economic impact of oil exports | 68 | 20% | +3300% |
| foreign exchange (forex) rate fluctuations | 36 | 11% | — |
| oil and gas market trends | 193 | 57% | +916% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Crude Oil Price Today - April 29: Brent Crude Crosses $111 Per Barrel; Check Latest Rates of WTI, Murban](https://www.oneindia.com/india/crude-oil-price-today-april-29-brent-crude-crosses-111-per-barrel-check-latest-rates-of-wti-mu-8072617.html) | oneindia.com | 8 | negative |
| 13 Apr 2026 | [Crude Oil Price Today - April 13: Brent Crude Crosses $102 Per Barrel; Check Latest Rates of WTI, Indian…](https://www.oneindia.com/india/crude-oil-price-today-april-13-brent-crude-crosses-102-per-barrel-check-latest-rates-of-wti-in-8056165.html) | oneindia.com | 8 | negative |
| 1 Apr 2026 | [These 6 stocks from NIFTY 100 stayed resilient despite the US-Iran war, rallied up to 12% in March](https://upstox.com/news/market-news/stocks/these-6-stocks-from-nifty-100-stayed-resilient-despite-the-us-iran-war-rallied-up-to-12-in-march/article-191541/) | upstox.com | 8 | negative |
| 22 Mar 2026 | [नहीं सुधर रहा विदेशी निवेशकों का मूड... बाजार से निकाले ₹88000Cr, जानिए क्यों](https://www.aajtak.in/business/news/story/us-iran-war-crude-price-impact-stock-market-fpi-selloff-88000-crore-rupee-tutc-dskc-2503723-2026-03-22) | aajtak.in | 8 | negative |
| 10 Mar 2026 | [Crude Oil Price is Down 8%, Now Trading at $83 After Soaring Amid Middle East Crisis](https://www.pulse.ng/story/crude-oil-drops-83-2026031010582279749) | pulse.ng | 8 | negative |
| 9 Mar 2026 | [⚡Crude Oil Price Climbs Above USD 100, Markets Brace for Impact](https://www.latestly.com/quickly/world/crude-oil-price-surges-above-usd-100-as-israel-iran-war-disrupts-global-supply-7347232.html) | latestly.com | 8 | negative |
| 23 Apr 2026 | [Govt On Petrol-Diesel Hike: क्या देश में महंगा होने वाला है पेट्रोल-डीजल? आ गया सरकार का बयान](https://www.aajtak.in/business/utility/story/modi-govt-denies-petrol-diesel-rate-hike-says-it-fake-and-mischevious-news-tutc-dskc-2531536-2026-04-23) | aajtak.in | 7 | negative |
| 8 Apr 2026 | [Crude Oil Price Today: ट्रंप के एक 'सीजफायर' से दुनिया भर में गिरे तेल का दाम! अब कितने पर पहुंचा क्रूड ऑयल?](https://hindi.oneindia.com/news/business/crude-oil-price-today-fuel-plunge-globally-after-us-iran-ceasefire-agreement-1537033.html) | hindi.oneindia.com | 7 | negative |
| 8 Apr 2026 | [Crude Oil Price Today - April 8: Check Prices of Brent, WTI, Urals, ESPO, Murban, and More As Markets Crash](https://www.oneindia.com/international/crude-oil-price-today-april-8-check-prices-of-brent-wti-urals-espo-murban-and-more-as-market-011-8051119.html) | oneindia.com | 7 | negative |
| 9 Mar 2026 | [युद्ध से तेल की कीमतों में आग... 2022 के बाद पहली बार कीमत $100 के पार, PAK-बांग्लादेश में हाहाकार](https://www.aajtak.in/business/news/story/crude-oil-price-cross-100-dollar-per-barrel-after-2022-amid-us-israel-iran-war-big-crisis-pakistan-bangladesh-tutc-dskc-2490253-2026-03-09) | aajtak.in | 7 | negative |
| 1 Mar 2026 | [ईरान-इजरायल तनाव के बीच होर्मुज स्ट्रेट बंद, क्या तेल की कीमतों में आएगा बड़ा उछाल? जानें डिटेल](https://www.abplive.com/business/crude-oil-price-today-1-march-iran-airstrike-on-dubai-bahrain-us-israel-war-news-3095946) | abplive.com | 7 | negative |
| 22 Apr 2026 | [Crude Price Surge: हांगकांग से कोरिया तक गिरावट, अचानक उछला कच्चा तेल, तो दबाव में विदेशी बाजार](https://www.aajtak.in/business/news/story/crude-oil-price-surge-again-asian-market-up-down-what-signal-for-india-tutc-dskc-2530279-2026-04-22) | aajtak.in | 6 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "crude oil price" --since 2026-01-01 --until 2026-04-30
prism-news trends "crude oil price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "crude oil price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "crude oil price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "crude oil price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Bank of Japan News](bank-of-japan-news.md)
- [US Dollar News](us-dollar-news.md)
- [Fintech News](fintech-news.md)
- [Mutual Fund News](mutual-fund-news.md)
