# IPO News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ipo news” · 14,800/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ipo-news.json](../../examples/scenarios/ipo-news.json).

**Question.** What did the news say about ipo between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="IPO"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 40,479 |
| Negative · neutral · positive | 26% · 2.0% · 72% |
| Critical (priority 7–9) | 67% (26,951 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (13,512 articles) |
| Most-reported country | United States (32% of matches) |
| Strongest theme by lift | initial public offerings (ipos) |

## Twelve months of coverage

Monthly matching articles for `IPO` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6,214 | 61% | 1,022 | 5,083 | █████████ |
| Jun 2025 | 6,701 | 64% | 961 | 5,630 | ██████████ |
| Jul 2025 | 7,895 | 57% | 1,321 | 6,443 | ████████████ |
| Aug 2025 | 10,210 | 55% | 1,765 | 8,289 | ███████████████ |
| Sep 2025 | 13,512 | 69% | 2,561 | 10,751 | ████████████████████ |
| Oct 2025 | 7,307 | 64% | 1,025 | 6,182 | ███████████ |
| Nov 2025 | 7,483 | 64% | 1,182 | 6,126 | ███████████ |
| Dec 2025 | 8,875 | 60% | 1,164 | 7,514 | █████████████ |
| Jan 2026 | 7,021 | 65% | 983 | 5,895 | ██████████ |
| Feb 2026 | 12,990 | 73% | 5,356 | 7,426 | ███████████████████ |
| Mar 2026 | 8,972 | 63% | 1,835 | 6,903 | █████████████ |
| Apr 2026 | 11,496 | 64% | 2,393 | 8,839 | █████████████████ |

The last four complete months averaged 10,120 articles a month against 7,755 in the first four (+30%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 12,851 | 32% |
| India | 3,761 | 9.3% |
| China | 1,372 | 3.4% |
| United Kingdom | 655 | 1.6% |
| Singapore | 466 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| initial public offerings (ipos) | 5,003 | 21% | -30% |
| stock splits and reverse splits | 957 | 4.1% | -0% |
| financial technology (fintech) innovations | 2,077 | 8.9% | -1% |
| initial public offerings (ipos) and listings | 3,236 | 14% | -40% |
| mergers and acquisitions in finance | 1,243 | 5.3% | +12% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [OnEMI Technology IPO: Price band Rs 162–171, GMP up 2% -Check key dates, expert view](https://www.financialexpress.com/market/ipo-news/onemi-technology-ipo-opens-today-price-band-rs-162171-gmp-up-2-key-dates-lot-size-expert-view/4223129/) | financialexpress.com | 8 | positive |
| 30 Apr 2026 | [SpaceX IPO ties Musk payout to $7.5 trillion Mars target](https://en.cryptonomist.ch/2026/04/30/spacex-ipo-musk-pay-plan/) | en.cryptonomist.ch | 8 | positive |
| 30 Apr 2026 | [SpaceX IPO filing says only Class B shareholders can remove Elon Musk, giving founder unique control over…](https://www.cnbctv18.com/world/only-elon-musk-can-fire-elon-musk-from-spacex-filing-shows-ipo-tesla-facebook-mark-zuckerberg-ws-l-19896247.htm) | cnbctv18.com | 8 | negative |
| 29 Apr 2026 | [Bill Ackman's Pershing Square USA tumbles 18% in its stock-market debut](https://www.businessinsider.com/bill-ackman-ps-psus-pershing-square-usa-ipo-trading-investing-2026-4) | businessinsider.com | 8 | negative |
| 29 Apr 2026 | [If You'd Put $1,000 Into Chipotle Mexican Grill Stock 20 Years Ago, Here's What You'd Have Today](https://www.kiplinger.com/investing/invested-1000-in-cmg-stock-worth-how-much-now) ⚠ | kiplinger.com | 8 | negative |
| 29 Apr 2026 | [Airtel Money IPO May Raise Up to $2 Bn, Report Says - TechStory](https://techstory.in/airtel-money-ipo-may-raise-up-to-2-bn-report-says/) | techstory.in | 8 | positive |
| 29 Apr 2026 | [Only Elon Musk can fire himself from SpaceX, filing shows - The Economic Times](https://economictimes.indiatimes.com/tech/technology/only-elon-musk-can-fire-himself-from-spacex-filing-shows/articleshow/130610155.cms) | economictimes.indiatimes.com | 8 | negative |
| 29 Apr 2026 | [SpaceX IPO: Millions of investors may make this costly mistake — don’t be one](https://economictimes.indiatimes.com/news/international/us/spacex-ipo-millions-of-investors-may-make-this-costly-mistake-dont-be-one/articleshow/130606344.cms) | economictimes.indiatimes.com | 8 | negative |
| 29 Apr 2026 | [Airtel Africa is lining up a potentially sizeable IPO of its mobile money business, with the deal expected…](https://www.developingtelecoms.com/telecom-technology/financial-services/20173-airtel-money-ipo-could-raise-up-to-2bn-in-blockbuster-listing.html) | developingtelecoms.com | 8 | positive |
| 29 Apr 2026 | [SpaceX IPO speculation grows; no confirmed filing or $1.75T valuation yet](https://www.domain-b.com/markets/stock-markets-world/spacex-ipo-rumors-2026-no-confirmation) | domain-b.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "IPO" --since 2026-01-01 --until 2026-04-30
prism-news trends "IPO" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "IPO" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "IPO", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "IPO", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Gold Price News](gold-price-news.md)
- [Housing Market News](housing-market-news.md)
- [RBI News](rbi-news.md)
- [Nifty News](nifty-news.md)
