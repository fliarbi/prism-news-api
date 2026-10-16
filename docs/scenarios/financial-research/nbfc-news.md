# NBFC News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nbfc news” · 720/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nbfc-news.json](../../examples/scenarios/nbfc-news.json).

**Question.** What did the news say about nbfc between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="NBFC"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,724 |
| Negative · neutral · positive | 13% · 1.5% · 85% |
| Critical (priority 7–9) | 72% (1,949 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (1,413 articles) |
| Most-reported country | India (35% of matches) |
| Strongest theme by lift | initial public offerings (ipos) |

## Twelve months of coverage

Monthly matching articles for `NBFC` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 523 | 76% | 61 | 458 | ███████ |
| Jun 2025 | 800 | 68% | 63 | 728 | ███████████ |
| Jul 2025 | 854 | 64% | 118 | 731 | ████████████ |
| Aug 2025 | 1,413 | 60% | 291 | 1,111 | ████████████████████ |
| Sep 2025 | 684 | 69% | 75 | 599 | ██████████ |
| Oct 2025 | 739 | 69% | 90 | 644 | ██████████ |
| Nov 2025 | 558 | 73% | 63 | 494 | ████████ |
| Dec 2025 | 605 | 79% | 58 | 455 | █████████ |
| Jan 2026 | 518 | 77% | 48 | 461 | ███████ |
| Feb 2026 | 770 | 73% | 70 | 692 | ███████████ |
| Mar 2026 | 514 | 76% | 71 | 437 | ███████ |
| Apr 2026 | 922 | 65% | 165 | 738 | █████████████ |

The last four complete months averaged 681 articles a month against 898 in the first four (-24%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 957 | 35% |
| United States | 81 | 3.0% |
| Iran | 20 | 0.7% |
| Singapore | 20 | 0.7% |
| Japan | 10 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| initial public offerings (ipos) | 149 | 8.8% | -44% |
| corporate governance and board decisions | 65 | 3.8% | +97% |
| microfinance and small-scale lending models | 47 | 2.8% | +34% |
| personal loan application process | 68 | 4.0% | +36% |
| challenges in rural banking access | 41 | 2.4% | +46% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Manappuram Finance Limited Discloses SEBI Warning Against CMD in Personal Capacity](https://studycafe.in/manappuram-finance-limited-discloses-sebi-warning-against-cmd-in-personal-capacity-418379.html) | studycafe.in | 8 | negative |
| 22 Apr 2026 | [Should You Invest in Indian Programming Tutorial Meme the Next Big Thing?](https://www.thedetroitbureau.com/www-news/should-you-invest-in-indian-programming-tutorial-meme-the-next-big-thing-dhzh8lcjkta1) | thedetroitbureau.com | 8 | positive |
| 20 Apr 2026 | [Moneyboxx Finance Limited Raises ₹35 Crore from IndusInd Bank and STCI Finance Limited to Boost Rural…](https://entrepreneurnewsnetwork.com/2026/04/20/moneyboxx-finance-limited-raises-%e2%82%b935-crore-from-indusind-bank-and-stci-finance-limited-to-boost-rural-lending/) | entrepreneurnewsnetwork.com | 8 | positive |
| 19 Apr 2026 | [The Essential Breakdown of Small Business 6 Million Asset Test and Why It Matters Now](https://www.thedetroitbureau.com/www-news/the-essential-breakdown-of-small-business-6-million-asset-test-and-why-it-matters-now-dhx2hn0j37r4) | thedetroitbureau.com | 8 | positive |
| 17 Apr 2026 | [RBI’s revised NBFC-UL norm could narrow valuation discount for these PSU stocks over medium term-…](https://www.moneycontrol.com/news/business/markets/rbi-s-revised-nbfc-ul-norm-could-narrow-valuation-discount-for-these-psu-stocks-over-medium-term-13892108.html) | moneycontrol.com | 8 | positive |
| 16 Apr 2026 | [PFC shares jump 5% to hit fresh 52-week high, surge 29% in April so far. What's heating up the stock?](https://economictimes.indiatimes.com/markets/stocks/news/pfc-shares-jump-5-to-hit-fresh-52-week-high-surge-29-in-april-so-far-whats-heating-up-the-stock/articleshow/130300662.cms) | economictimes.indiatimes.com | 8 | negative |
| 14 Apr 2026 | [Tata Sons’ CIC deregistration may be its only way out](https://www.financialexpress.com/business/industry-tata-sons-cic-deregistration-may-be-its-only-way-out-4207141/) | financialexpress.com | 8 | negative |
| 12 Apr 2026 | [MUFG Bank Announces ₹39,618 Crore Investment in Shriram Finance \| Autocar Professional](https://www.autocarpro.in/news/mufg-bank-announces-â¹39618-crore-investment-in-shriram-finance-130238) | autocarpro.in | 8 | positive |
| 11 Apr 2026 | [RBI proposals for large NBFCs leaves Tata Sons as only unlisted one \| Company Business News](https://livemint.com/companies/rbi-proposes-changes-to-nbfc-norms-upper-layer-list-not-revealed-yet-11775816636625.html) | livemint.com | 8 | negative |
| 10 Apr 2026 | [Will Tata Sons get listing waiver? RBI tweak will make it 'upper NBFC' - The Times of India](https://timesofindia.indiatimes.com/business/india-business/will-tata-sons-get-listing-waiver-rbi-tweak-will-make-it-upper-nbfc/articleshow/130182197.cms) | timesofindia.indiatimes.com | 8 | negative |
| 10 Apr 2026 | [Upper Layer NBFCs to be Defined by Absolute Asset Size of ₹1 Lcr+](https://economictimes.indiatimes.com/satet-front/upper-layer-nbfcs-to-be-defined-by-absolute-asset-size-of-1-lcr/articleshow/130180235.cms) | economictimes.indiatimes.com | 8 | positive |
| 10 Apr 2026 | [RBI must direct Tata Sons to list; changed regulatory landscape doesn't allow exemption: InGovern](https://www.newsdrum.in/business/rbi-must-direct-tata-sons-to-list-changed-regulatory-landscape-doesnt-allow-exemption-ingovern-11786957) | newsdrum.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "NBFC" --since 2026-01-01 --until 2026-04-30
prism-news trends "NBFC" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "NBFC" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "NBFC", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "NBFC", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tax News Today](tax-news-today.md)
- [IMF News](imf-news.md)
