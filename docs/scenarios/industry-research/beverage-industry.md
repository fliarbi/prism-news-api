# Beverage Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “beverage industry” · 880/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [beverage-industry.json](../../examples/scenarios/beverage-industry.json).

**Question.** How much news did the beverage industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="beverage industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,151 |
| Negative · neutral · positive | 16% · 1.5% · 82% |
| Critical (priority 7–9) | 25% (790 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (864 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | microbrewery startup guides |

## Twelve months of coverage

Monthly matching articles for `beverage industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 638 | 22% | 79 | 549 | ███████████████ |
| Jun 2025 | 432 | 22% | 55 | 371 | ██████████ |
| Jul 2025 | 620 | 24% | 155 | 455 | ██████████████ |
| Aug 2025 | 602 | 29% | 102 | 496 | ██████████████ |
| Sep 2025 | 733 | 22% | 111 | 616 | █████████████████ |
| Oct 2025 | 655 | 32% | 127 | 516 | ███████████████ |
| Nov 2025 | 577 | 26% | 96 | 471 | █████████████ |
| Dec 2025 | 528 | 30% | 65 | 456 | ████████████ |
| Jan 2026 | 682 | 27% | 94 | 574 | ████████████████ |
| Feb 2026 | 864 | 27% | 140 | 702 | ████████████████████ |
| Mar 2026 | 758 | 24% | 124 | 627 | ██████████████████ |
| Apr 2026 | 847 | 22% | 147 | 691 | ████████████████████ |

The last four complete months averaged 788 articles a month against 573 in the first four (+37%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 55% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 904 | 29% |
| India | 226 | 7.2% |
| United Kingdom | 189 | 6.0% |
| Canada | 45 | 1.4% |
| Australia | 42 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| microbrewery startup guides | 161 | 9.2% | +44% |
| craft beer brewing techniques | 358 | 20% | +38% |
| craft beer competitions | 131 | 7.5% | +44% |
| non-alcoholic beer production | 78 | 4.4% | +0% |
| historical brewing techniques | 65 | 3.7% | +210% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Mar 2026 | [The packaging crisis about to hit food and beverage](https://www.foodnavigator-latam.com/Article/2026/03/16/iran-conflict-plastic-packaging-price-rise-for-food-and-drink/) | foodnavigator-latam.com | 8 | negative |
| 31 Mar 2026 | [3,84 Euro mehr pro Kiste Cola – so viel soll die neue Zuckersteuer bringen](https://www.fr.de/wirtschaft/84-euro-mehr-pro-kiste-cola-so-viel-soll-die-zusaetzliche-zuckersteuer-bringen-zr-94243506.html) | fr.de | 7 | positive |
| 27 Feb 2026 | [Tempted to return Conn.’s bottle deposit law to 5 cents, state Senate approves higher fines](https://www.pressreader.com/usa/the-middletown-press-middletown-ct/20260227/281522232568745) | pressreader.com | 7 | negative |
| 26 Feb 2026 | [Tempted to return Connecticut's bottle deposit law to five cents, state Senate approves higher fines](https://www.yahoo.com/news/articles/tempted-return-connecticuts-bottle-deposit-021111494.html) | yahoo.com | 7 | negative |
| 6 Feb 2026 | [‘Triple whammy’ headwinds push food sector toward ‘peak calories’](https://www.bakingbusiness.com/articles/65509-triple-whammy-headwinds-push-food-sector-toward-peak-calories) | bakingbusiness.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "beverage industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "beverage industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "beverage industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "beverage industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "beverage industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Defence Industry News](defence-industry-news.md)
- [Dairy Industry](dairy-industry.md)
- [Banking Industry](banking-industry.md)
- [Electronics Industry](electronics-industry.md)
