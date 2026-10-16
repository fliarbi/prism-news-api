# Immigration Policy News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “immigration policy news” · 10/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [immigration-policy-news.json](../../examples/scenarios/immigration-policy-news.json).

**Question.** How did coverage of immigration policy develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="immigration policy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,903 |
| Negative · neutral · positive | 87% · 1.0% · 12% |
| Critical (priority 7–9) | 80% (2,327 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (872 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | immigration and border control agencies |

## Twelve months of coverage

Monthly matching articles for `immigration policy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 689 | 80% | 591 | 79 | ████████████████ |
| Jun 2025 | 676 | 74% | 598 | 60 | ████████████████ |
| Jul 2025 | 653 | 65% | 555 | 88 | ███████████████ |
| Aug 2025 | 677 | 68% | 602 | 66 | ████████████████ |
| Sep 2025 | 593 | 83% | 488 | 92 | ██████████████ |
| Oct 2025 | 516 | 83% | 446 | 61 | ████████████ |
| Nov 2025 | 538 | 87% | 492 | 40 | ████████████ |
| Dec 2025 | 688 | 87% | 626 | 51 | ████████████████ |
| Jan 2026 | 658 | 82% | 601 | 57 | ███████████████ |
| Feb 2026 | 872 | 78% | 734 | 124 | ████████████████████ |
| Mar 2026 | 679 | 84% | 602 | 70 | ████████████████ |
| Apr 2026 | 694 | 76% | 593 | 91 | ████████████████ |

The last four complete months averaged 726 articles a month against 674 in the first four (+8%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 34% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 781 | 27% |
| Australia | 34 | 1.2% |
| United Kingdom | 29 | 1.0% |
| Canada | 28 | 1.0% |
| India | 10 | 0.3% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| immigration and border control agencies | 139 | 7.6% | -4% |
| work visa categories (e.g., h-1b, l-1, tier 2) | 40 | 2.2% | -78% |
| /people & society/social issues & advocacy/immigration policy & migrant rights | 475 | 26% | -12% |
| deportation and removal defense strategies | 46 | 2.5% | -23% |
| skilled migration programs and criteria | 27 | 1.5% | -40% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Winning numbers drawn in Wednesday’s Ohio Pick 4 Evening](https://apnews.com/article/lotteries-3f56b703051242dba7aac22cc198c15f) | apnews.com | 8 | negative |
| 30 Apr 2026 | [Winning numbers drawn in Wednesday’s Ohio Classic Lotto](https://apnews.com/article/lotteries-855881c1fb9149a0b6d0e3738246c600) | apnews.com | 8 | negative |
| 29 Apr 2026 | [Winning numbers drawn in Tuesday’s South Carolina Cash Pop](https://apnews.com/article/lotteries-f90ebc1eae18463a8ec6ef3e5a71b704) | apnews.com | 8 | negative |
| 28 Apr 2026 | [US now weighs Israel and Palestine views in green card decisions under Trump: Report - Türkiye Today](https://www.turkiyetoday.com/world/us-now-weighs-israel-and-palestine-views-in-green-card-decisions-under-trump-report-3218960) | turkiyetoday.com | 8 | negative |
| 28 Apr 2026 | [Cleveland, Toronto tied 2-2 heading to game 5](https://apnews.com/article/toronto-raptors-cleveland-cavaliers-donovan-mitchell-nba-playoffs-3b9ebff71add49369cf4046855742173) | apnews.com | 8 | negative |
| 28 Apr 2026 | [Glaude: Trump Believes This Country 'Must Always Remain a White Republic'](https://www.breitbart.com/clips/2026/04/27/glaude-trump-believes-this-country-must-always-remain-a-white-republic/) | breitbart.com | 8 | negative |
| 27 Apr 2026 | [Winning numbers drawn in Sunday’s Maryland Cash Pop](https://apnews.com/article/lotteries-6080976f40ae4da5a91569ed4c9c1d51) | apnews.com | 8 | negative |
| 27 Apr 2026 | [Winning numbers drawn in Sunday’s Illinois Lucky Day Lotto (Evening)](https://apnews.com/article/lotteries-a3b7fc889c1d40298c24de61bac7e88c) | apnews.com | 8 | negative |
| 26 Apr 2026 | [Winning numbers drawn in Saturday’s Washington Match 4](https://apnews.com/article/lotteries-faa2825f43764fbbb38b2a0fd8919c81) | apnews.com | 8 | negative |
| 26 Apr 2026 | [Winning numbers drawn in Saturday’s Arkansas Cash 4 Evening](https://apnews.com/article/lotteries-406ffceb40154959b054548a3ca36917) | apnews.com | 8 | negative |
| 26 Apr 2026 | [Winning numbers drawn in Saturday’s Tennessee Cash 4](https://apnews.com/article/lotteries-600e1a08d9494da1b79dfd2b7653ad97) | apnews.com | 8 | negative |
| 23 Apr 2026 | [Police chief: Austin could lose up to $20M in fight with Abbott over ICE policy](https://www.statesman.com/news/local/article/austin-police-chief-abbott-ice-policy-22220524.php) | statesman.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "immigration policy" --since 2026-01-01 --until 2026-04-30
prism-news trends "immigration policy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "immigration policy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "immigration policy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "immigration policy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Windfall Tax News](windfall-tax-news.md)
- [CBAM News](cbam-news.md)
- [Right to Repair News](right-to-repair-news.md)
- [Drug Pricing News](drug-pricing-news.md)
