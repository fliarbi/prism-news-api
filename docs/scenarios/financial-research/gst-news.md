# GST News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gst news” · 49,500/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gst-news.json](../../examples/scenarios/gst-news.json).

**Question.** What did the news say about gst between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="GST"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 23,717 |
| Negative · neutral · positive | 49% · 1.6% · 50% |
| Critical (priority 7–9) | 40% (9,404 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (15,526 articles) |
| Most-reported country | India (35% of matches) |
| Strongest theme by lift | suzuki fuel efficiency & eco-friendly technologies |

## Twelve months of coverage

Monthly matching articles for `GST` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,685 | 37% | 1,675 | 1,903 | █████ |
| Jun 2025 | 2,918 | 47% | 859 | 1,958 | ████ |
| Jul 2025 | 4,117 | 40% | 1,551 | 2,459 | █████ |
| Aug 2025 | 11,901 | 38% | 3,306 | 8,364 | ███████████████ |
| Sep 2025 | 15,526 | 54% | 4,304 | 10,776 | ████████████████████ |
| Oct 2025 | 6,100 | 47% | 1,402 | 4,590 | ████████ |
| Nov 2025 | 4,781 | 48% | 1,186 | 3,529 | ██████ |
| Dec 2025 | 4,725 | 53% | 1,324 | 3,277 | ██████ |
| Jan 2026 | 4,936 | 53% | 2,121 | 2,734 | ██████ |
| Feb 2026 | 6,240 | 36% | 3,284 | 2,875 | ████████ |
| Mar 2026 | 5,948 | 36% | 3,250 | 2,598 | ████████ |
| Apr 2026 | 6,593 | 36% | 2,877 | 3,580 | ████████ |

The last four complete months averaged 5,929 articles a month against 5,655 in the first four (+5%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 73% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 8,271 | 35% |
| United States | 6,301 | 27% |
| United Kingdom | 610 | 2.6% |
| Australia | 336 | 1.4% |
| Canada | 259 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| suzuki fuel efficiency & eco-friendly technologies | 757 | 6.0% | +18825% |
| new model year updates and changes | 1,460 | 12% | +109% |
| suzuki compact car lineup | 363 | 2.9% | +36200% |
| suzuki engine technologies & specifications | 314 | 2.5% | new |
| economy news: tax reform implications | 255 | 2.0% | -83% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Mere GST Deposit not payment until debited and appropriated to Government: High Court](https://studycafe.in/mere-gst-deposit-not-payment-until-debited-and-appropriated-to-government-high-court-418476.html) | studycafe.in | 8 | negative |
| 30 Apr 2026 | [Meesho to appeal $1.5m tax demand in India](https://startupnews.fyi/ecommerce/meesho-to-appeal-1-5m-tax-demand-in-india) ⚠ | startupnews.fyi | 8 | negative |
| 30 Apr 2026 | [Anticipatory Bail Allowed in GST Case Involving Cancelled Supplier Entity](https://studycafe.in/anticipatory-bail-allowed-in-gst-case-involving-cancelled-supplier-entity-418616.html) | studycafe.in | 8 | negative |
| 29 Apr 2026 | [Partner who acted on Ponzi scheme fined £30k over conflict of interest](https://www.legalfutures.co.uk/latest-news/partner-who-acted-on-ponzi-scheme-fined-30k-over-conflict-of-interest) ⚠ | legalfutures.co.uk | 8 | negative |
| 29 Apr 2026 | [Three ways the spring economic update affects your wallet](https://www.theglobeandmail.com/investing/personal-finance/article-three-ways-the-spring-economic-statement-affects-your-wallet/) ⚠ | theglobeandmail.com | 8 | negative |
| 29 Apr 2026 | [Maruti Suzuki Share Price](https://www.newsdrum.in/business/maruti-shares-end-nearly-3-pc-higher-market-valuation-surges-by-rs-11422-cr-11778944) ⚠ | newsdrum.in | 8 | positive |
| 29 Apr 2026 | [Tesla’s Make-or-Break Play](https://brandequity.economictimes.indiatimes.com/news/marketing/teslas-make-or-break-play/130594720) ⚠ | brandequity.economictimes.indiatimes.com | 8 | positive |
| 29 Apr 2026 | [CGST officer, consultant arrested in Rs 20 lakh bribe case in Gujrat](https://assamtribune.com/national/cgst-officer-consultant-arrested-in-rs-20-lakh-bribe-case-in-gujrat-1611084) | assamtribune.com | 8 | negative |
| 28 Apr 2026 | [Liberals target affordability to meet era of uncertainty in spring fiscal update](https://cheknews.ca/liberals-target-affordability-to-meet-era-of-uncertainty-in-spring-fiscal-update-1321487/) ⚠ | cheknews.ca | 8 | negative |
| 28 Apr 2026 | [Nine highlights from the spring economic update](https://www.theglobeandmail.com/politics/article-spring-economic-update-highlights-cpp-sports-defence-april-28/) ⚠ | theglobeandmail.com | 8 | negative |
| 28 Apr 2026 | [Delhi HC Imposes Fine on Firm Due to Fake GST ITC Claim Using Fake Invoices](https://studycafe.in/delhi-hc-imposes-fine-on-firm-due-to-fake-gst-itc-claim-using-fake-invoices-418406.html) | studycafe.in | 8 | negative |
| 28 Apr 2026 | [Maruti Suzuki not chasing market share, growth tied to capacity addition: Chairman R C Bhargava-…](https://www.moneycontrol.com/automobile/maruti-suzuki-not-chasing-market-share-growth-tied-to-capacity-addition-chairman-r-c-bhargava-article-13902311.html) | moneycontrol.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "GST" --since 2026-01-01 --until 2026-04-30
prism-news trends "GST" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "GST" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "GST", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "GST", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Stock Market News](stock-market-news.md)
- [Crypto News](crypto-news.md)
- [Gold Price News](gold-price-news.md)
- [Housing Market News](housing-market-news.md)
