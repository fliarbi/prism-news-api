# RBI News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rbi news” · 14,800/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [rbi-news.json](../../examples/scenarios/rbi-news.json).

**Question.** What did the news say about rbi between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="RBI"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 44,419 |
| Negative · neutral · positive | 33% · 3.5% · 63% |
| Critical (priority 7–9) | 50% (22,233 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (20,704 articles) |
| Most-reported country | United States (31% of matches) |
| Strongest theme by lift | emerging markets economic updates |

## Twelve months of coverage

Monthly matching articles for `RBI` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10,335 | 40% | 2,770 | 7,019 | ██████████ |
| Jun 2025 | 8,468 | 50% | 2,560 | 5,549 | ████████ |
| Jul 2025 | 9,361 | 45% | 3,202 | 5,762 | █████████ |
| Aug 2025 | 20,704 | 47% | 8,160 | 11,882 | ████████████████████ |
| Sep 2025 | 10,545 | 53% | 3,873 | 6,228 | ██████████ |
| Oct 2025 | 8,484 | 59% | 2,799 | 5,424 | ████████ |
| Nov 2025 | 7,423 | 57% | 2,423 | 4,802 | ███████ |
| Dec 2025 | 8,120 | 63% | 2,920 | 4,941 | ████████ |
| Jan 2026 | 6,107 | 57% | 1,992 | 3,959 | ██████ |
| Feb 2026 | 9,851 | 53% | 2,342 | 7,156 | ██████████ |
| Mar 2026 | 11,060 | 49% | 3,856 | 6,796 | ███████████ |
| Apr 2026 | 17,401 | 46% | 6,516 | 10,169 | █████████████████ |

The last four complete months averaged 11,105 articles a month against 12,217 in the first four (-9%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 63% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 13,935 | 31% |
| India | 7,621 | 17% |
| United Kingdom | 1,565 | 3.5% |
| Iran | 381 | 0.9% |
| China | 347 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| emerging markets economic updates | 1,625 | 5.2% | +13% |
| foreign exchange (forex) rate fluctuations | 1,950 | 6.3% | +19% |
| asian financial market developments | 1,069 | 3.4% | +5% |
| central bank monetary policy announcements | 1,516 | 4.9% | +8% |
| interest rate decisions and impacts | 1,690 | 5.4% | +14% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 6 Feb 2026 | [12-year-old boy found hanging In Palakkad \| Kochi News - The Times of India](https://timesofindia.indiatimes.com/city/kochi/12-year-old-boy-found-hanging-in-palakkad/articleshow/127951363.cms) | timesofindia.indiatimes.com | 9 | negative |
| 30 Apr 2026 | [India central bank's FX forward book balloons to over $100bln as Iran war pummels rupee](https://www.zawya.com/en/world/indian-sub-continent/india-central-banks-fx-forward-book-balloons-to-over-100bln-as-iran-war-pummels-rupee-j6qk9p72) | zawya.com | 8 | negative |
| 30 Apr 2026 | [Centre reviews Hyderabad Police’s Operation Octopus, pushes anti-fraud AI tool](https://www.siasat.com/centre-reviews-hyderabad-polices-operation-octopus-pushes-anti-fraud-ai-tool-3462916/) | siasat.com | 8 | positive |
| 30 Apr 2026 | [RBI Permits Banks To Provide Relief Without Borrowers’ Request In Disaster-affected Areas - Outlook Money](https://outlookmoney.com/banking/rbi-permits-banks-to-provide-relief-without-borrowers-request-in-disaster-affected-areas) | outlookmoney.com | 8 | positive |
| 29 Apr 2026 | [How long-term bet on rupee saved Rs 14,000 crore of forex in February](https://indianexpress.com/article/business/market/how-long-term-bet-on-rupee-saved-rs-14000-crore-of-forex-in-february-10663112/) | indianexpress.com | 8 | negative |
| 29 Apr 2026 | [Banks allowed to offer natural calamity relief suo motu from July 1](https://economictimes.indiatimes.com/industry/banking/finance/banking/banks-allowed-to-offer-natural-calamity-relief-suo-motu-from-july-1/articleshow/130617158.cms) | economictimes.indiatimes.com | 8 | positive |
| 29 Apr 2026 | [RBI overhauls framework for Banks for handling loans affected by natural disasters](https://www.thehindubusinessline.com/money-and-banking/rbi-overhauls-framework-for-banks-for-handling-loans-affected-by-natural-disasters/article70921629.ece) | thehindubusinessline.com | 8 | positive |
| 29 Apr 2026 | [Prashant Bhushan urges RBI to intervene in the proposed re-appointment of Bakhshi as ICICI Bank’s MD and CEO](https://www.thehindubusinessline.com/money-and-banking/prashant-bhushan-urges-rbi-to-intervene-in-the-proposed-re-appointment-of-bakhshi-as-icici-banks-md-and-ceo/article70921239.ece) | thehindubusinessline.com | 8 | negative |
| 29 Apr 2026 | [RBIâs new disaster loan relief rules explained: Banks can help borrowers automatically; what changes from…](https://timesofindia.indiatimes.com/business/india-business/rbis-new-disaster-loan-relief-rules-explained-banks-can-help-borrowers-automatically-what-changes-from-july-1/articleshow/130610752.cms) | timesofindia.indiatimes.com | 8 | positive |
| 29 Apr 2026 | [Why RBI Cancelled Paytm Payments Bank Licence: Vijay Shekhar Sharma Exit And Fintech Shake-Up Explained](https://www.newsx.com/business/why-rbi-cancelled-paytm-payments-bank-licence-vijay-shekhar-sharma-exit-and-fintech-shake-up-explained-207198/) | newsx.com | 8 | negative |
| 29 Apr 2026 | [Digital Arrest: 2-3 घंटे में ब्लॉक हो जाएगा सिम कार्ड, डिजिटल अरेस्ट को रोकने की पूरी तैयारी, व्हाट्सऐप ने…](https://navbharattimes.indiatimes.com/tech/gadgets-news/new-system-block-fraud-sim-card-within-2-3-hour-to-stop-digital-arrest-scam-whatsapp-banned-9400-accounts/articleshow/130597463.cms) | navbharattimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [RBI Revokes Paytm Payments Bank Licence](https://paymentsindustryintelligence.com/rbi-revokes-paytm-payments-bank-licence/) | paymentsindustryintelligence.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "RBI" --since 2026-01-01 --until 2026-04-30
prism-news trends "RBI" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "RBI" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "RBI", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "RBI", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Housing Market News](housing-market-news.md)
- [IPO News](ipo-news.md)
- [Nifty News](nifty-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
