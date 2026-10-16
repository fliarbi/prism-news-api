# Mutual Fund News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mutual fund news” · 3,600/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [mutual-fund-news.json](../../examples/scenarios/mutual-fund-news.json).

**Question.** What did the news say about mutual fund between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="mutual fund"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,148 |
| Negative · neutral · positive | 8.7% · 2.5% · 89% |
| Critical (priority 7–9) | 14% (1,829 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (7,505 articles) |
| Most-reported country | India (7.1% of matches) |
| Strongest theme by lift | fund prospectus analysis |

## Twelve months of coverage

Monthly matching articles for `mutual fund` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 514 | 40% | 49 | 454 | █ |
| Jun 2025 | 610 | 41% | 81 | 511 | ██ |
| Jul 2025 | 1,363 | 23% | 74 | 1,269 | ████ |
| Aug 2025 | 1,093 | 43% | 216 | 858 | ███ |
| Sep 2025 | 2,422 | 18% | 106 | 2,291 | ██████ |
| Oct 2025 | 888 | 41% | 81 | 787 | ██ |
| Nov 2025 | 712 | 41% | 62 | 639 | ██ |
| Dec 2025 | 971 | 45% | 82 | 786 | ███ |
| Jan 2026 | 1,407 | 19% | 83 | 1,298 | ████ |
| Feb 2026 | 7,505 | 11% | 809 | 6,433 | ████████████████████ |
| Mar 2026 | 2,351 | 15% | 123 | 2,200 | ██████ |
| Apr 2026 | 1,885 | 19% | 120 | 1,723 | █████ |

The last four complete months averaged 3,287 articles a month against 895 in the first four (+267%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 12% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 935 | 7.1% |
| United States | 353 | 2.7% |
| Nigeria | 50 | 0.4% |
| Canada | 35 | 0.3% |
| China | 26 | 0.2% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| fund prospectus analysis | 3,194 | 28% | +243% |
| fund expense ratios and fees | 2,915 | 25% | +236% |
| asset allocation and balanced funds | 2,878 | 25% | +215% |
| fund benchmarking methodologies | 2,875 | 25% | +171% |
| tax-efficient fund structures | 2,436 | 21% | +260% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Democrat Rep David Scott dead at 80](https://www.foxnews.com/politics/democrat-rep-david-scott-dead-80) | foxnews.com | 8 | negative |
| 16 Apr 2026 | [Or Moshe](https://www.foxnews.com/person/m/or-moshe) | foxnews.com | 8 | positive |
| 26 Mar 2026 | [Fidelity Beats Lawsuit Over Fees in $439 Billion Money Market Fund](https://www.insurancejournal.com/news/national/2026/03/26/863479.htm) | insurancejournal.com | 8 | negative |
| 20 Mar 2026 | [EXCLUSIVE: Ohio Gubernatorial Candidate Amy Acton’s Insane Deleted COVID Tweets Surface](https://www.foxnews.com/analysis/exclusive-ohio-gubernatorial-candidate-blasts-nfl-fans-over-covid-rules-resurfaced-posts) | foxnews.com | 8 | negative |
| 7 Mar 2026 | [From money-shy to money-smart, it’s a woman’s day](https://www.financialexpress.com/business/news/from-money-shy-to-money-smart-its-a-womans-day/4165603/) | financialexpress.com | 8 | positive |
| 24 Feb 2026 | [HDFC oldest fund turns Rs 1,000 SIP into Rs 1.6 crore, grows lump sum 195 times since launch](https://www.financialexpress.com/money/hdfcs-oldest-fund-turns-rs-1000-sip-into-rs-1-6-crore-grows-lump-sum-195-times-since-launch-4153347/) | financialexpress.com | 8 | positive |
| 10 Feb 2026 | [Gold ETF Inflows Jump 50%, Exceed Equity Funds in Jan: AMFI](https://www.newkerala.com/news/a/gold-etfs-see-steep-50-pc-rise-rs-520.htm) | newkerala.com | 8 | positive |
| 10 Feb 2026 | [Gold ETF inflows eclipse equity funds as investors chase bullion boom in record-breaking rally - The…](https://economictimes.indiatimes.com/markets/commodities/news/gold-etf-inflows-eclipse-equity-funds-as-investors-chase-bullion-boom-in-record-breaking-rally/printarticle/128146979.cms) | economictimes.indiatimes.com | 8 | positive |
| 10 Feb 2026 | [Gold ETF inflows eclipse equity funds as investors chase bullion boom in record-breaking rally](https://economictimes.indiatimes.com/markets/commodities/news/gold-etf-inflows-eclipse-equity-funds-as-investors-chase-bullion-boom-in-record-breaking-rally/articleshow/128146979.cms) | economictimes.indiatimes.com | 8 | positive |
| 6 Feb 2026 | [PGIM India MF resumes subscription in 3 international funds](https://economictimes.indiatimes.com/mf/mf-news/pgim-india-mf-resumes-subscription-in-3-international-funds/articleshow/127982330.cms) | economictimes.indiatimes.com | 8 | negative |
| 4 Feb 2026 | [India’s mutual fund Industry to more than double in 5 years](https://www.thehindubusinessline.com/markets/indias-mutual-fund-industry-to-more-than-double-in-5-years/article70592564.ece) | thehindubusinessline.com | 8 | positive |
| 21 Jan 2026 | [SBI MF to take at least 10% of Adani Group's biggest rupee bond issue, bankers say](https://www.thehindu.com/business/markets/sbi-mf-to-take-at-least-10-of-adani-groups-biggest-rupee-bond-issue-bankers-say/article70534918.ece) | thehindu.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "mutual fund" --since 2026-01-01 --until 2026-04-30
prism-news trends "mutual fund" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "mutual fund" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "mutual fund", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "mutual fund", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Crude Oil Price News](crude-oil-price-news.md)
- [Fintech News](fintech-news.md)
- [Mergers and Acquisitions News](mergers-and-acquisitions-news.md)
- [Private Equity News](private-equity-news.md)
