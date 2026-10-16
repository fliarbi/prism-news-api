# Income Tax News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “income tax news” · 8,100/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [income-tax-news.json](../../examples/scenarios/income-tax-news.json).

**Question.** What did the news say about income tax between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="income tax"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,088 |
| Negative · neutral · positive | 40% · 15% · 45% |
| Critical (priority 7–9) | 60% (6,087 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,199 articles) |
| Most-reported country | India (16% of matches) |
| Strongest theme by lift | personal income tax filing strategies |

## Twelve months of coverage

Monthly matching articles for `income tax` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,460 | 39% | 702 | 1,034 | ███████████████ |
| Jun 2025 | 1,369 | 50% | 452 | 674 | █████████ |
| Jul 2025 | 2,113 | 51% | 871 | 927 | █████████████ |
| Aug 2025 | 2,680 | 56% | 1,043 | 1,242 | █████████████████ |
| Sep 2025 | 2,341 | 61% | 932 | 1,064 | ███████████████ |
| Oct 2025 | 1,363 | 54% | 619 | 528 | █████████ |
| Nov 2025 | 1,832 | 65% | 987 | 619 | ███████████ |
| Dec 2025 | 1,523 | 63% | 698 | 606 | ██████████ |
| Jan 2026 | 1,694 | 61% | 725 | 777 | ███████████ |
| Feb 2026 | 2,458 | 66% | 1,004 | 1,131 | ███████████████ |
| Mar 2026 | 2,737 | 58% | 975 | 1,250 | █████████████████ |
| Apr 2026 | 3,199 | 57% | 1,311 | 1,373 | ████████████████████ |

The last four complete months averaged 2,522 articles a month against 2,156 in the first four (+17%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 37% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 1,628 | 16% |
| United States | 1,239 | 12% |
| United Kingdom | 246 | 2.4% |
| Canada | 55 | 0.6% |
| Singapore | 53 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| personal income tax filing strategies | 825 | 15% | +11% |
| tax law updates and legislative changes | 283 | 5.0% | +96% |
| income tax bracket revisions | 230 | 4.1% | +111% |
| government taxation strategies and reforms | 225 | 4.0% | +96% |
| government taxation and revenue systems | 1,342 | 24% | +55% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 3 Feb 2026 | [CJ Roy Suicide Case: Karnataka Home Minister G Parameshwara Says ‘Too Early’ To Blame Income Tax Pressure…](https://www.latestly.com/india/news/httpswww-latestly-comindianewscj-roy-suicide-case-karnataka-home-minister-g-parameshwara-says-too-early-to-blame-income-tax-pressure-for-death-of-confident-group-chairman-sit-probe-underway-7299-7299443.html) | latestly.com | 9 | negative |
| 30 Apr 2026 | [Ford Expects $1.3 Billion in Tariff Refunds After SCOTUS Ruling](http://autoweek.com/news/a71177860/ford-expects-13-billion-tariff-refunds/) | autoweek.com | 8 | negative |
| 30 Apr 2026 | [Missouri could move income tax vote from November to August](https://www.yahoo.com/news/articles/missouri-could-move-income-tax-165923621.html) | yahoo.com | 8 | positive |
| 30 Apr 2026 | [Income Tax Department grants stay to NDTV on Rs 420.36 Crore Income Tax Liability](https://studycafe.in/income-tax-department-grants-stay-to-ndtv-on-rs-420-36-crore-income-tax-liability-418766.html) | studycafe.in | 8 | negative |
| 30 Apr 2026 | [NDTV gets stay on ₹420.36 crore tax demand; subject to review](https://storyboard18.com/brand-marketing/ndtv-gets-stay-on-%e2%82%b9420-36-crore-tax-demand-subject-to-review-96767.htm) | storyboard18.com | 8 | negative |
| 30 Apr 2026 | [State Pension rise pushes UK pensioners near tax threshold](https://www.mirror.co.uk/money/triple-lock-state-pension-rise-37088259) | mirror.co.uk | 8 | negative |
| 28 Apr 2026 | [Delhi High Court Cancels Time-Barred Reassessment Notice and Assessment Order](https://studycafe.in/delhi-high-court-cancels-time-barred-reassessment-notice-and-assessment-order-418325.html) | studycafe.in | 8 | negative |
| 28 Apr 2026 | [Madras HC dismisses pleas seeking probe into AIADMK leaders D Jayakumar, CVe Shanmugam’s poll affidavits](https://www.newindianexpress.com/states/tamil-nadu/2026/Apr/28/madras-hc-dismisses-pleas-seeking-probe-into-aiadmk-leaders-d-jayakumar-cve-shanmugams-poll-affidavits) | newindianexpress.com | 8 | negative |
| 27 Apr 2026 | [Golpe do imposto de renda já infectou 16 mil celulares: você pode ser o próximo](https://fdr.com.br/2026/04/27/golpe-do-imposto-de-renda-ja-infectou-16-mil-celulares-voce-pode-ser-o-proximo/) | fdr.com.br | 8 | negative |
| 27 Apr 2026 | [Madras HC dismisses a fresh petition seeking probe into financial disclosures of Vijay in poll affidavit](https://www.newindianexpress.com/states/tamil-nadu/2026/Apr/27/madras-hc-dismisses-a-fresh-petition-seeking-probe-into-financial-disclosures-of-vijay-in-poll-affidavit) | newindianexpress.com | 8 | negative |
| 27 Apr 2026 | [Income Tax Department Uncovered Massive Unreported Property Deals Worth Rs 3.12 Lakh Crore Across Multiple…](https://studycafe.in/income-tax-department-uncovered-massive-unreported-property-deals-worth-rs-3-12-lakh-crore-across-multiple-states-418133.html) | studycafe.in | 8 | positive |
| 25 Apr 2026 | [TNCC chief doubles down on I-T raid claim](https://www.newindianexpress.com/states/tamil-nadu/2026/Apr/25/tncc-chief-doubles-down-on-i-t-raid-claim) | newindianexpress.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "income tax" --since 2026-01-01 --until 2026-04-30
prism-news trends "income tax" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "income tax" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "income tax", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "income tax", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Budget News](budget-news.md)
- [SEBI News](sebi-news.md)
- [Sensex News](sensex-news.md)
- [Inflation News](inflation-news.md)
