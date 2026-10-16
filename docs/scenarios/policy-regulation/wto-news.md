# WTO News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “wto news” · 140/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [wto-news.json](../../examples/scenarios/wto-news.json).

**Question.** How did coverage of wto develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="WTO"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,515 |
| Negative · neutral · positive | 37% · 2.9% · 60% |
| Critical (priority 7–9) | 51% (3,327 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (2,766 articles) |
| Most-reported country | United States (43% of matches) |
| Strongest theme by lift | political economy and resource allocation |

## Twelve months of coverage

Monthly matching articles for `WTO` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,587 | 56% | 768 | 746 | ███████████ |
| Jun 2025 | 952 | 56% | 401 | 526 | ███████ |
| Jul 2025 | 1,724 | 57% | 838 | 855 | ████████████ |
| Aug 2025 | 2,766 | 49% | 1,308 | 1,375 | ████████████████████ |
| Sep 2025 | 1,783 | 62% | 775 | 966 | █████████████ |
| Oct 2025 | 1,274 | 56% | 501 | 742 | █████████ |
| Nov 2025 | 1,053 | 55% | 364 | 664 | ████████ |
| Dec 2025 | 1,130 | 47% | 367 | 740 | ████████ |
| Jan 2026 | 1,195 | 50% | 434 | 742 | █████████ |
| Feb 2026 | 1,463 | 55% | 570 | 854 | ███████████ |
| Mar 2026 | 2,431 | 52% | 958 | 1,375 | ██████████████████ |
| Apr 2026 | 1,426 | 47% | 449 | 934 | ██████████ |

The last four complete months averaged 1,629 articles a month against 1,757 in the first four (-7%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 70% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,822 | 43% |
| India | 316 | 4.8% |
| United Kingdom | 242 | 3.7% |
| China | 217 | 3.3% |
| Brazil | 70 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| political economy and resource allocation | 206 | 5.1% | +217% |
| economy news: global trade agreements | 182 | 4.5% | +48% |
| economy news: trade deficit/surplus announcements | 104 | 2.6% | +131% |
| public policy analysis and implementation | 92 | 2.3% | +411% |
| environmental policy and climate governance | 141 | 3.5% | +66% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [India invokes WTO peace clause for FY25 rice subsidies for farmers](https://economictimes.indiatimes.com/news/economy/agriculture/india-invokes-wto-peace-clause-for-fy25-rice-subsidies-for-farmers/articleshow/130616628.cms) | economictimes.indiatimes.com | 8 | negative |
| 22 Apr 2026 | [WTO accepts request of India, Taipei to defer ICT import duty dispute ruling until Oct 2026](https://cfo.economictimes.indiatimes.com/news/news/wto-accepts-request-of-india-taipei-to-defer-ict-import-duty-dispute-ruling-until-oct-2026/130431205) | cfo.economictimes.indiatimes.com | 8 | negative |
| 21 Apr 2026 | [India, Taiwan get time till October to settle ICT tariff dispute - The Economic Times](https://economictimes.indiatimes.com/news/economy/foreign-trade/india-taiwan-get-time-till-october-to-settle-ict-tariff-dispute/printarticle/130426346.cms) | economictimes.indiatimes.com | 8 | negative |
| 21 Apr 2026 | [India, Taiwan get time till October to settle ICT tariff dispute](https://economictimes.indiatimes.com/news/economy/foreign-trade/india-taiwan-get-time-till-october-to-settle-ict-tariff-dispute/articleshow/130426346.cms) | economictimes.indiatimes.com | 8 | negative |
| 21 Apr 2026 | [WTO accepts request of India, Taipei to defer ICT import duty dispute ruling until Oct 2026 - The Economic…](https://economictimes.indiatimes.com/news/economy/foreign-trade/wto-accepts-request-of-india-taipei-to-defer-ict-import-duty-dispute-ruling-until-oct-2026/printarticle/130424327.cms) | economictimes.indiatimes.com | 8 | negative |
| 19 Apr 2026 | [Experts examine WTO verdict on cross-border subsidies, flag policy challenges](https://munsifdaily.com/experts-examine-wto-verdict-on-cross-border/) | munsifdaily.com | 8 | negative |
| 8 Apr 2026 | [World Trade Organization Ministerial Post-Mortem](https://www.csis.org/analysis/world-trade-organization-ministerial-post-mortem) | csis.org | 8 | negative |
| 7 Apr 2026 | [WTO moratorium lapse opens door for digital duties, experts warn of daunting task](https://www.financialexpress.com/business/news/wto-moratorium-lapse-opens-door-for-digital-duties-experts-warn-of-daunting-task/4197715/) | financialexpress.com | 8 | negative |
| 6 Apr 2026 | [OPINION \| Why India needs a duty-free trade in digitally delivered services- Moneycontrol.com](https://www.moneycontrol.com/news/opinion/why-india-needs-a-duty-free-trade-in-digitally-delivered-services-13880957.html) | moneycontrol.com | 8 | negative |
| 3 Apr 2026 | [China-India Trade Talks at WTO: Wang Meets Goyal](https://www.newkerala.com/news/a/china-calls-stronger-trade-cooperation-india-after-ministerial-557.htm) | newkerala.com | 8 | positive |
| 2 Apr 2026 | [India Secured ‘Best’ U.S. Trade Deal Among Peers, Says Piyush Goyal - IndUS Business Journal](https://indusbusinessjournal.com/2026/04/india-secured-best-u-s-trade-deal-among-peers-says-piyush-goyal/) | indusbusinessjournal.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "WTO" --since 2026-01-01 --until 2026-04-30
prism-news trends "WTO" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "WTO" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "WTO", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "WTO", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Education Policy News](education-policy-news.md)
- [Student Visa News](student-visa-news.md)
- [Labour Law News](labour-law-news.md)
- [National Security News](national-security-news.md)
