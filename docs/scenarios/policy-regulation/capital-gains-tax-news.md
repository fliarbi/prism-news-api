# Capital Gains Tax News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “capital gains tax news” · 260/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [capital-gains-tax-news.json](../../examples/scenarios/capital-gains-tax-news.json).

**Question.** How did coverage of capital gains tax develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="capital gains tax"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 947 |
| Negative · neutral · positive | 43% · 6.7% · 51% |
| Critical (priority 7–9) | 66% (628 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (293 articles) |
| Most-reported country | Australia (16% of matches) |
| Strongest theme by lift | capital gains tax minimization strategies |

## Twelve months of coverage

Monthly matching articles for `capital gains tax` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 168 | 58% | 37 | 94 | ███████████ |
| Jun 2025 | 126 | 54% | 22 | 85 | █████████ |
| Jul 2025 | 162 | 57% | 55 | 95 | ███████████ |
| Aug 2025 | 185 | 58% | 84 | 87 | █████████████ |
| Sep 2025 | 142 | 61% | 55 | 82 | ██████████ |
| Oct 2025 | 215 | 66% | 83 | 118 | ███████████████ |
| Nov 2025 | 269 | 76% | 100 | 157 | ██████████████████ |
| Dec 2025 | 200 | 58% | 69 | 117 | ██████████████ |
| Jan 2026 | 149 | 72% | 62 | 77 | ██████████ |
| Feb 2026 | 289 | 71% | 125 | 155 | ████████████████████ |
| Mar 2026 | 216 | 62% | 87 | 107 | ███████████████ |
| Apr 2026 | 293 | 62% | 129 | 142 | ████████████████████ |

The last four complete months averaged 237 articles a month against 160 in the first four (+48%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| Australia | 150 | 16% |
| United States | 89 | 9.4% |
| India | 60 | 6.3% |
| United Kingdom | 54 | 5.7% |
| Nigeria | 44 | 4.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| capital gains tax minimization strategies | 107 | 17% | +51% |
| real estate tax incentives and deductions | 58 | 9.2% | +176% |
| estate and gift tax planning techniques | 82 | 13% | +32% |
| retirement account tax implications (ira, 401k) | 31 | 4.9% | +107% |
| real estate investment tax strategies | 78 | 12% | +100% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 3 Apr 2026 | [Losing $1 billion a day: Gurmeet Chadha urges PMO, Finance Ministry to revisit capital gains tax, STT](http://economictimes.indiatimes.com/markets/stocks/news/losing-1-billion-a-day-gurmeet-chadha-urges-pmo-finance-ministry-to-revisit-capital-gains-tax-stt/articleshow/129995974.cms) | economictimes.indiatimes.com | 8 | positive |
| 30 Mar 2026 | [Deloitte's Pre-Budget Submission 2027 \| Deloitte Ireland](http://www2.deloitte.com/ie/en/about/press-room/deloitte-urges-capital-gains-tax-cut.html) | deloitte.com | 8 | positive |
| 26 Feb 2026 | [Crypto now taxable but reporting gap raises compliance risk - Businessday NG](https://businessday.ng/business-economy/article/crypto-now-taxable-but-reporting-gap-raises-compliance-risk/) | businessday.ng | 8 | positive |
| 24 Feb 2026 | [India–France DTAA reset: Source-based capital gains may deter FPIs, boost strategic FDI, say experts](https://cfo.economictimes.indiatimes.com/news/tax-legal-accounting/indiafrance-dtaa-overhaul-source-based-capital-gains-tax-to-hit-fpis-boost-long-term-fdi/128740368) | cfo.economictimes.indiatimes.com | 8 | positive |
| 24 Feb 2026 | [Tax change would help first timers get a home: Treasury](https://www.smh.com.au/politics/federal/tax-change-would-help-first-timers-get-a-home-treasury-20260224-p5o4wo.html) | smh.com.au | 8 | negative |
| 20 Feb 2026 | [UK reports record-breaking budget surplus of £30.4bn in surprise boost for Rachel Reeves](https://www.theguardian.com/politics/2026/feb/19/uk-reports-record-breaking-surplus-rachel-reeves) | theguardian.com | 8 | positive |
| 16 Feb 2026 | [Australians back hit to capital gains and negative gearing to pay for tax cuts](https://www.watoday.com.au/politics/federal/australians-back-hit-to-capital-gains-and-negative-gearing-to-pay-for-tax-cuts-20260216-p5o2k9.html) | watoday.com.au | 8 | positive |
| 6 Feb 2026 | [Aussies dealt $250 billion blow as cost of controversial policy snowballs](https://www.9news.com.au/national/capital-gains-tax-discount-parliamentary-budget-office-analysis/4fc12d1b-e962-401e-b1ba-0b15d68ba03b) | 9news.com.au | 8 | negative |
| 26 Jan 2026 | [Youths, small investor s exempt fr om capital gains tax on equities](https://www.pressreader.com/nigeria/business-day-nigeria/20260126/281530822437119) | pressreader.com | 8 | negative |
| 20 Jan 2026 | [The Supreme Court just woke up every "Paper Company" in Mauritius.](https://www.linkedin.com/pulse/supreme-court-just-woke-up-every-paper-company-prabhash-choudhary-kxzhc) | linkedin.com | 8 | positive |
| 30 Apr 2026 | [Chalmers to play Mr Nice Guy to existing property investors - Switzer](https://switzer.com.au/chalmers-to-play-mr-nice-guy-to-existing-property-investors/) | switzer.com.au | 7 | negative |
| 29 Apr 2026 | [Storm As Tullow Oil Counters KRA Ksh23B Tax Claim](https://thekenyatimes.com/business/tullow-oil-kra-ksh23b-tax-claim/) | thekenyatimes.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "capital gains tax" --since 2026-01-01 --until 2026-04-30
prism-news trends "capital gains tax" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "capital gains tax" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "capital gains tax", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "capital gains tax", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Brexit News](brexit-news.md)
- [Census Latest](census-latest.md)
- [Antitrust News](antitrust-news.md)
- [Waqf News](waqf-news.md)
