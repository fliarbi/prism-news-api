# SEBI News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sebi news” · 9,900/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [sebi-news.json](../../examples/scenarios/sebi-news.json).

**Question.** What did the news say about sebi between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="SEBI"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,218 |
| Negative · neutral · positive | 23% · 5.3% · 72% |
| Critical (priority 7–9) | 70% (3,676 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (2,206 articles) |
| Most-reported country | India (24% of matches) |
| Strongest theme by lift | initial public offerings (ipos) |

## Twelve months of coverage

Monthly matching articles for `SEBI` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,127 | 76% | 449 | 650 | ██████████ |
| Jun 2025 | 1,163 | 77% | 265 | 875 | ███████████ |
| Jul 2025 | 1,728 | 74% | 723 | 961 | ████████████████ |
| Aug 2025 | 2,206 | 70% | 735 | 1,400 | ████████████████████ |
| Sep 2025 | 1,862 | 78% | 607 | 1,193 | █████████████████ |
| Oct 2025 | 1,062 | 74% | 266 | 772 | ██████████ |
| Nov 2025 | 1,077 | 79% | 339 | 717 | ██████████ |
| Dec 2025 | 1,311 | 76% | 322 | 943 | ████████████ |
| Jan 2026 | 1,045 | 74% | 227 | 765 | █████████ |
| Feb 2026 | 1,265 | 63% | 233 | 940 | ███████████ |
| Mar 2026 | 1,610 | 72% | 434 | 1,092 | ███████████████ |
| Apr 2026 | 1,298 | 72% | 305 | 940 | ████████████ |

The last four complete months averaged 1,304 articles a month against 1,556 in the first four (-16%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 32% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 1,270 | 24% |
| United States | 161 | 3.1% |
| Singapore | 43 | 0.8% |
| Iran | 28 | 0.5% |
| United Kingdom | 21 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| initial public offerings (ipos) | 773 | 23% | -24% |
| corporate governance and board decisions | 268 | 8.0% | +148% |
| regulatory changes in financial markets | 888 | 26% | -20% |
| market manipulation and fraud cases | 611 | 18% | -15% |
| initial public offerings (ipos) and listings | 828 | 25% | -23% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Sebi clears faster launch path for AIF schemes with 30-day fast track \| Mint](https://www.livemint.com/industry/sebi-clears-faster-launch-path-for-aif-schemes-with-30-day-fast-track-11777551792975.html) | livemint.com | 8 | positive |
| 30 Apr 2026 | [SEBI Fast-Tracks AIF Launches: New 30-Day Rule for Fund Managers](https://www.republicworld.com/business/sebi-fast-track-mechanism-aif-placement-memorandum-30-day-rule) | republicworld.com | 8 | negative |
| 30 Apr 2026 | [Sebi clears fast track launch for AIF schemes \| Mint Bangalore â newspaper â Lesen Sie diese Geschichte…](https://www.magzter.com/de/stories/newspaper/Mint-Bangalore/SEBI-CLEARS-FAST-TRACK-LAUNCH-FOR-AIF-SCHEMES) | magzter.com | 8 | negative |
| 28 Apr 2026 | [Cupid receives administrative warning from SEBI for non-compliance - Business Upturn](https://www.businessupturn.com/business/cupid-receives-administrative-warning-from-sebi-for-non-compliance/) | businessupturn.com | 8 | positive |
| 28 Apr 2026 | [Punjab & Sind Bank plans ₹3,000-cr share sale this fiscal](https://www.thehindubusinessline.com/money-and-banking/punjab-sind-bank-plans-3000-cr-share-sale-this-fiscal/article70916322.ece) | thehindubusinessline.com | 8 | positive |
| 28 Apr 2026 | [Regulators intensify global crackdown on finfluencers; SEBI steps up AI-led surveillance in India](https://bfsi.economictimes.indiatimes.com/articles/global-regulators-crack-down-on-finfluencers-as-sebi-enhances-ai-surveillance-in-india/130567823) | bfsi.economictimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [SEBI Imposes Penalty of Rs 1.5 Crore on Eight Entities for Front-Running Trades](https://studycafe.in/sebi-imposes-penalty-of-rs-1-5-crore-on-eight-entities-for-front-running-trades-418443.html) | studycafe.in | 8 | negative |
| 28 Apr 2026 | [Sebi Fines 8 Entities Rs 1.50 Crore For Front-Running Trades - Outlook Money](https://www.outlookmoney.com/news/sebi-fines-8-entities-rs-150-crore-for-front-running-trades) | outlookmoney.com | 8 | negative |
| 28 Apr 2026 | [SEBI bans 8 including Ashok Maheshwari in front-running case](https://www.thehindubusinessline.com/money-and-banking/sebi-bars-ashok-maheshwari-7-others-in-front-running-case/article70914985.ece) | thehindubusinessline.com | 8 | negative |
| 28 Apr 2026 | [Manappuram Finance Limited Discloses SEBI Warning Against CMD in Personal Capacity](https://studycafe.in/manappuram-finance-limited-discloses-sebi-warning-against-cmd-in-personal-capacity-418379.html) | studycafe.in | 8 | negative |
| 27 Apr 2026 | [SEBI warns Manappuram Finance CMD over delayed shares pledge disclosure](https://cfo.economictimes.indiatimes.com/news/governance-risk-compliance/sebi-warns-manappuram-finance-cmd-over-delayed-shares-pledge-disclosure/130543004) | cfo.economictimes.indiatimes.com | 8 | negative |
| 26 Apr 2026 | [SEBI crackdown in suspected pump and dump case, searches at multiple locations conducted: Sources-…](https://www.moneycontrol.com/news/business/markets/sebi-crackdown-in-suspected-pump-and-dump-case-searches-at-multiple-location-conducted-sources-13900002.html) | moneycontrol.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "SEBI" --since 2026-01-01 --until 2026-04-30
prism-news trends "SEBI" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "SEBI" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "SEBI", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "SEBI", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [UPI News](upi-news.md)
- [Budget News](budget-news.md)
- [Income Tax News](income-tax-news.md)
- [Sensex News](sensex-news.md)
