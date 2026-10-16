# Pension News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pension news” · 1,900/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [pension-news.json](../../examples/scenarios/pension-news.json).

**Question.** What did the news say about pension between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="pension"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,172 |
| Negative · neutral · positive | 42% · 6.5% · 52% |
| Critical (priority 7–9) | 58% (7,680 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,017 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | arts and creative community features |

## Twelve months of coverage

Monthly matching articles for `pension` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,939 | 57% | 1,407 | 1,233 | ███████████████ |
| Jun 2025 | 2,426 | 55% | 1,102 | 1,133 | ████████████ |
| Jul 2025 | 3,096 | 56% | 1,389 | 1,509 | ███████████████ |
| Aug 2025 | 3,899 | 59% | 1,936 | 1,763 | ███████████████████ |
| Sep 2025 | 3,664 | 58% | 1,451 | 1,974 | ██████████████████ |
| Oct 2025 | 3,130 | 61% | 1,455 | 1,425 | ████████████████ |
| Nov 2025 | 3,400 | 60% | 1,755 | 1,403 | █████████████████ |
| Dec 2025 | 2,891 | 58% | 1,292 | 1,370 | ██████████████ |
| Jan 2026 | 2,911 | 56% | 1,094 | 1,691 | ██████████████ |
| Feb 2026 | 3,251 | 57% | 1,346 | 1,685 | ████████████████ |
| Mar 2026 | 2,993 | 61% | 1,296 | 1,459 | ███████████████ |
| Apr 2026 | 4,017 | 59% | 1,758 | 1,947 | ████████████████████ |

The last four complete months averaged 3,293 articles a month against 3,090 in the first four (+7%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,913 | 15% |
| United Kingdom | 1,056 | 8.0% |
| India | 868 | 6.6% |
| Nigeria | 216 | 1.6% |
| Canada | 107 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| arts and creative community features | 206 | 3.0% | -42% |
| government pension schemes | 168 | 2.5% | -47% |
| retirement account tax implications (ira, 401k) | 148 | 2.2% | +51% |
| government labor and employment regulations | 413 | 6.1% | -11% |
| pension plan management | 140 | 2.1% | -10% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 17 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [SC directs Allahabad HC to urgently hear 77-year-old cancer patient’s nine-year-old pension plea](https://www.newindianexpress.com/india/2026/Apr/30/sc-directs-allahabad-hc-to-urgently-hear-77-year-old-cancer-patients-nine-year-old-pension-plea) | newindianexpress.com | 8 | negative |
| 29 Apr 2026 | [‘At no point was any decision taken to remove Davy Fitzgerald’ – Antrim GAA chief responds to players’ letter](https://www.independent.ie/sport/gaelic-games/hurling/at-no-point-was-any-decision-taken-to-remove-davy-fitzgerald-antrim-gaa-chief-responds-to-players-letter/a1815575245.html) | independent.ie | 8 | positive |
| 29 Apr 2026 | [89-Year-Old Man Arrested After Random Shootings in Athens Injure Five](https://us.headtopics.com/news/89-year-old-man-arrested-after-random-shootings-in-athens-82796903) | us.headtopics.com | 8 | negative |
| 28 Apr 2026 | [High Court Directs Punjab To Clear DA, DR Dues, Scraps Staggered Pension Arrears Payment - Outlook Money](https://outlookmoney.com/retirement/pension/high-court-directs-punjab-to-clear-da-dr-dues-scraps-staggered-pension-arrears-payment) | outlookmoney.com | 8 | negative |
| 19 Apr 2026 | [NPA pensioners threaten nationwide protest over unpaid benefits](https://www.vanguardngr.com/2026/04/npa-pensioners-threaten-nationwide-protest-over-unpaid-benefits/) | vanguardngr.com | 8 | negative |
| 16 Apr 2026 | [Son kept mum’s body in freezer home for years and spent her cash](https://www.dailystar.co.uk/news/uk-news/son-kept-elderly-mums-body-37027374) | dailystar.co.uk | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "pension" --since 2026-01-01 --until 2026-04-30
prism-news trends "pension" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "pension" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "pension", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "pension", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Mergers and Acquisitions News](mergers-and-acquisitions-news.md)
- [Private Equity News](private-equity-news.md)
- [Repo Rate News](repo-rate-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
