# FMCG Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “fmcg industry” · 6,600/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [fmcg-industry.json](../../examples/scenarios/fmcg-industry.json).

**Question.** How much news did fmcg receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="fmcg"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,549 |
| Negative · neutral · positive | 11% · 0.6% · 88% |
| Critical (priority 7–9) | 42% (1,070 articles) |
| Busiest month, May 2025 – Apr 2026 | Jul 2025 (1,449 articles) |
| Most-reported country | India (28% of matches) |
| Strongest theme by lift | market research and consumer behavior analysis |

## Twelve months of coverage

Monthly matching articles for `fmcg` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 852 | 28% | 98 | 750 | ████████████ |
| Jun 2025 | 976 | 18% | 52 | 921 | █████████████ |
| Jul 2025 | 1,449 | 18% | 84 | 1,360 | ████████████████████ |
| Aug 2025 | 927 | 34% | 122 | 801 | █████████████ |
| Sep 2025 | 1,123 | 30% | 147 | 971 | ████████████████ |
| Oct 2025 | 604 | 38% | 76 | 523 | ████████ |
| Nov 2025 | 907 | 25% | 42 | 858 | █████████████ |
| Dec 2025 | 558 | 29% | 32 | 524 | ████████ |
| Jan 2026 | 608 | 40% | 61 | 545 | ████████ |
| Feb 2026 | 722 | 38% | 61 | 656 | ██████████ |
| Mar 2026 | 523 | 49% | 59 | 460 | ███████ |
| Apr 2026 | 696 | 42% | 98 | 592 | ██████████ |

The last four complete months averaged 637 articles a month against 1,051 in the first four (-39%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 55% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 716 | 28% |
| United States | 229 | 9.0% |
| United Kingdom | 82 | 3.2% |
| Nigeria | 46 | 1.8% |
| China | 32 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market research and consumer behavior analysis | 70 | 4.8% | -77% |
| stock market index composition | 106 | 7.3% | +41% |
| market volatility indicators | 104 | 7.1% | +33% |
| asian financial market developments | 58 | 4.0% | -15% |
| data governance frameworks | 47 | 3.2% | -77% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [FMCG stocks hit badly amid war](https://www.financialexpress.com/market/fmcg-stocks-hit-badly-amid-warnbsp-4208458/) | financialexpress.com | 8 | negative |
| 13 Apr 2026 | [Rain deficit clouds demand outlook for FMCG firms](https://www.financialexpress.com/business/industry-rain-deficit-cloudsnbspdemand-outlook-for-fmcg-firms-4206071/) | financialexpress.com | 8 | positive |
| 9 Apr 2026 | [West Asia tensions disrupt Indian FMCG recovery for FY27-28: Report - www.lokmattimes.com](https://www.lokmattimes.com/business/west-asia-tensions-disrupt-indian-fmcg-recovery-for-fy27-28-report/) | lokmattimes.com | 8 | positive |
| 9 Apr 2026 | [West Asia Tensions Disrupt Indian FMCG Sector Recovery](https://www.newkerala.com/news/a/west-asia-tensions-disrupt-indian-fmcg-recovery-fy27-28-204.htm) | newkerala.com | 8 | negative |
| 9 Apr 2026 | [West Asia tensions disrupt Indian FMCG recovery for FY27-28: Report](https://www.aninews.in/news/business/west-asia-tensions-disrupt-indian-fmcg-recovery-for-fy27-28-report20260409081427) | aninews.in | 8 | negative |
| 1 Apr 2026 | [Why India's Smartest FMCG Companies Are Buying Regional Brands and Refusing to Change Them](https://www.linkedin.com/pulse/why-indias-smartest-fmcg-companies-buying-regional-brands-i4vqf) | linkedin.com | 8 | negative |
| 12 Mar 2026 | [West Asia conflict keeps Indian FMCG brands on watch; industry executives see limited immediate impact](https://www.storyboard18.com/brand-marketing/gulf-tensions-hit-indian-fmcg-firms-dabur-marico-godrej-shares-fall-ws-l-91906.htm) | storyboard18.com | 8 | positive |
| 24 Feb 2026 | [The](https://retail.economictimes.indiatimes.com/news/blog/the-unlearning-curve-for-indias-fmcg-giants/128748231) | retail.economictimes.indiatimes.com | 8 | positive |
| 19 Feb 2026 | [Buy or sell: Vaishali Parekh recommends three intraday stocks to buy today — 19 February 2026 \| Stock Market…](https://www.livemint.com/market/stock-market-news/buy-or-sell-vaishali-parekh-recommends-three-intraday-stocks-to-buy-today-19-february-2026-11771470428204.html) | livemint.com | 8 | positive |
| 16 Feb 2026 | [Reliance Consumer Forms Nigeria JV with TGI Group](https://www.newkerala.com/news/a/reliance-consumer-products-form-jv-tgi-group-expand-925.htm) | newkerala.com | 8 | positive |
| 13 Feb 2026 | [Down 11%: What's spiking the FMCG-TV story - Exchange4media](https://www.exchange4media.com/marketing-news/digital-at-64-whats-driving-fmcgs-shift-away-from-tv-151974.html) | exchange4media.com | 8 | positive |
| 11 Feb 2026 | [Inside FMCG’s digital reset: What’s taking India’s biggest advertisers online - Exchange4media](https://www.exchange4media.com/digital-news/inside-fmcgs-digital-reset-whats-taking-indias-biggest-advertisers-online-151881.html) | exchange4media.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "fmcg" --since 2026-01-01 --until 2026-04-30
prism-news trends "fmcg" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "fmcg" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "fmcg", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "fmcg", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Film Industry](film-industry.md)
- [Retail Industry News](retail-industry-news.md)
- [Steel Industry](steel-industry.md)
- [Chemical Industry](chemical-industry.md)
