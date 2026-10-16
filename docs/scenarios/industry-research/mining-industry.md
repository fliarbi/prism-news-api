# Mining Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mining industry” · 880/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [mining-industry.json](../../examples/scenarios/mining-industry.json).

**Question.** How much news did the mining industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="mining industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,642 |
| Negative · neutral · positive | 22% · 1.9% · 76% |
| Critical (priority 7–9) | 48% (2,238 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,329 articles) |
| Most-reported country | United States (12% of matches) |
| Strongest theme by lift | mining equipment automation and innovation |

## Twelve months of coverage

Monthly matching articles for `mining industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 803 | 50% | 224 | 556 | ████████████ |
| Jun 2025 | 600 | 46% | 119 | 467 | █████████ |
| Jul 2025 | 731 | 49% | 238 | 476 | ███████████ |
| Aug 2025 | 692 | 56% | 184 | 490 | ██████████ |
| Sep 2025 | 854 | 61% | 193 | 642 | █████████████ |
| Oct 2025 | 818 | 52% | 170 | 637 | ████████████ |
| Nov 2025 | 728 | 56% | 165 | 546 | ███████████ |
| Dec 2025 | 808 | 57% | 135 | 661 | ████████████ |
| Jan 2026 | 938 | 49% | 201 | 710 | ██████████████ |
| Feb 2026 | 1,316 | 49% | 305 | 989 | ████████████████████ |
| Mar 2026 | 1,059 | 48% | 200 | 842 | ████████████████ |
| Apr 2026 | 1,329 | 47% | 325 | 978 | ████████████████████ |

The last four complete months averaged 1,160 articles a month against 706 in the first four (+64%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 548 | 12% |
| Canada | 289 | 6.2% |
| Austria | 204 | 4.4% |
| Australia | 131 | 2.8% |
| India | 115 | 2.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mining equipment automation and innovation | 658 | 21% | +110% |
| mining safety and regulatory compliance | 453 | 14% | +134% |
| underground mining ventilation systems | 268 | 8.5% | +294% |
| mining software and data analytics | 260 | 8.2% | +313% |
| mining energy efficiency solutions | 399 | 13% | +102% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Friedland: We have never been so close to global conflict](https://miningmagazine.com/africa/news-analysis/4530333/friedland-close-global-conflict) | miningmagazine.com | 8 | negative |
| 22 Apr 2026 | [South32 lowers manganese guidance, braces for prolonged Middle East conflict](https://www.businesslive.co.za/companies/2026-04-22-south32-lowers-manganese-guidance-braces-for-prolonged-middle-east-conflict/) | businesslive.co.za | 8 | negative |
| 17 Apr 2026 | [Bitcoin Pressure Builds As Miners Dump 32K BTC In Just 3 Months](https://www.newsbtc.com/bitcoin-news/bitcoin-pressure-builds-as-miners-dump-32k-btc-in-just-3-months/) | newsbtc.com | 8 | positive |
| 30 Mar 2026 | [Up To 20% Of Rigs Now Bleeding Cash](https://bitcoinethereumnews.com/tech/up-to-20-of-rigs-now-bleeding-cash/) | bitcoinethereumnews.com | 8 | negative |
| 28 Mar 2026 | [Bitcoin miners are becoming AI companies and selling their BTC to fund the transition](https://bitcoinethereumnews.com/bitcoin/bitcoin-miners-are-becoming-ai-companies-and-selling-their-btc-to-fund-the-transition/) | bitcoinethereumnews.com | 8 | positive |
| 20 Mar 2026 | [Disruptive Technologies, Skills And Investment Will Define The Future Of South African Mining](https://techfinancials.co.za/2026/03/20/disruptive-technologies-skills-and-investment-will-define-the-future-of-south-african-mining/) | techfinancials.co.za | 8 | positive |
| 19 Mar 2026 | [Hycroft Mining Stock Plummets Amid Gold Selloff And Dollar Strength - Hycroft Mining Holding (NASDAQ:HYMC](https://www.benzinga.com/trading-ideas/movers/26/03/51365800/hycroft-mining-stock-plummets-amid-gold-selloff-and-dollar-strength) | benzinga.com | 8 | negative |
| 19 Mar 2026 | [Mining industry flags policy, infrastructure risks to investment despite improved outlook](https://www.iol.co.za/business-report/2026-03-19-mining-industry-flags-policy-infrastructure-risks-to-investment-despite-improved-outlook/) | iol.co.za | 8 | negative |
| 10 Mar 2026 | [Venezuelan lawmakers open debate on a mining bill to lure foreign capital](https://www.yahoo.com/news/articles/venezuelan-lawmakers-open-debate-mining-005234934.html) | yahoo.com | 8 | negative |
| 24 Feb 2026 | [The ocular confusion of a dishonest hack - Businessday NG](https://businessday.ng/opinion/article/the-ocular-confusion-of-a-dishonest-hack/) | businessday.ng | 8 | negative |
| 17 Feb 2026 | [Minnesota House Republican leaders don’t want to talk about immigration enforcement](https://www.yahoo.com/news/articles/minnesota-house-republican-leaders-don-040446995.html) | yahoo.com | 8 | negative |
| 10 Feb 2026 | [2026 Australia Immigration News - Getting Down Under](https://gettingdownunder.com/australian-immigration-news/2026-australia-immigration-news/) | gettingdownunder.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "mining industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "mining industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "mining industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "mining industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "mining industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tourism Industry](tourism-industry.md)
- [Cosmetics Industry](cosmetics-industry.md)
- [Paper Industry](paper-industry.md)
- [Biotech Industry](biotech-industry.md)
