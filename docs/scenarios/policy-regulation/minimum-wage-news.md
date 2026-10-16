# Minimum Wage News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “minimum wage news” · 210/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [minimum-wage-news.json](../../examples/scenarios/minimum-wage-news.json).

**Question.** How did coverage of minimum wage develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="minimum wage"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,545 |
| Negative · neutral · positive | 59% · 9.0% · 32% |
| Critical (priority 7–9) | 64% (2,896 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,396 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | compensation and benefits structures |

## Twelve months of coverage

Monthly matching articles for `minimum wage` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,067 | 56% | 576 | 374 | ███████████████ |
| Jun 2025 | 739 | 62% | 466 | 220 | ███████████ |
| Jul 2025 | 879 | 59% | 583 | 250 | █████████████ |
| Aug 2025 | 1,080 | 59% | 747 | 269 | ███████████████ |
| Sep 2025 | 638 | 69% | 407 | 176 | █████████ |
| Oct 2025 | 543 | 66% | 268 | 224 | ████████ |
| Nov 2025 | 738 | 65% | 355 | 291 | ███████████ |
| Dec 2025 | 1,316 | 57% | 690 | 476 | ███████████████████ |
| Jan 2026 | 965 | 55% | 512 | 351 | ██████████████ |
| Feb 2026 | 1,247 | 64% | 695 | 411 | ██████████████████ |
| Mar 2026 | 937 | 67% | 577 | 296 | █████████████ |
| Apr 2026 | 1,396 | 67% | 914 | 375 | ████████████████████ |

The last four complete months averaged 1,136 articles a month against 941 in the first four (+21%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 31% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 580 | 13% |
| United Kingdom | 247 | 5.4% |
| India | 173 | 3.8% |
| Nigeria | 58 | 1.3% |
| Canada | 32 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| compensation and benefits structures | 285 | 12% | +2% |
| minimum wage legislation debates | 302 | 13% | +35% |
| payroll management systems | 129 | 5.6% | +29% |
| labor & employment law - minimum wage legislation | 102 | 4.4% | +26% |
| hr compliance and labor laws | 203 | 8.8% | +29% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 13 Apr 2026 | [Haiti Workers Protest for Higher Minimum Wage - Time News](https://time.news/haiti-workers-protest-for-higher-minimum-wage/) | time.news | 9 | negative |
| 30 Apr 2026 | [¿Doscientos cuarenta… qué? \| El Feed \| Caracas Chronicles](https://www.caracaschronicles.com/el-feed/doscientos-cuarenta-que/) | caracaschronicles.com | 8 | negative |
| 29 Apr 2026 | [Minimum wage hikes 'killing off job opportunities for the young'](https://www.thisismoney.co.uk/money/markets/article-15776263/Minimum-wage-hikes-killing-job-opportunities-young-warns-CBI-chief.html) | thisismoney.co.uk | 8 | negative |
| 29 Apr 2026 | [WA rentals out of reach for thousands on income support](https://www.thewest.com.au/politics/state-politics/wa-rentals-falling-further-out-of-reach-for-thousands-on-income-support-and-minimum-wage-c-22207627) | thewest.com.au | 8 | negative |
| 29 Apr 2026 | [‘Zero options’ left for low income renters in parts of southern Qld - realestate.com.au](https://www.goldcoastbulletin.com.au/real-estate/queensland/zero-options-left-for-low-income-renters-in-parts-of-southern-qld/news-story/5b17181431cc3dfd53765e848f7d2518) | goldcoastbulletin.com.au | 8 | negative |
| 28 Apr 2026 | [Democrats Introduce Bill To More Than Triple The Minimum Wage](https://www.huffpost.com/entry/house-democrats-25-minimum-wage_n_69f0b51ce4b0093689a9cb3d) | huffpost.com | 8 | negative |
| 27 Apr 2026 | [Minimum wage, housing affordability, data center crackdown among NC Democrats' 2026 priorities](https://www.wral.com/news/nccapitol/nc-democrats-priorities-minimum-wage-data-center-housing-afford-april-2026/) | wral.com | 8 | negative |
| 26 Apr 2026 | [Regional wage hikes 'justified' due to fuel-driven inflation--Libanan](https://mb.com.ph/2026/04/26/regional-wage-hikes-justified-due-to-fuel-driven-inflation-libanan) | mb.com.ph | 8 | negative |
| 23 Apr 2026 | [ZCTU implores govt to review US$150 minimum wage - NewZimbabwe.com](https://www.newzimbabwe.com/zctu-implores-govt-to-review-us150-minimum-wage/) | newzimbabwe.com | 8 | positive |
| 22 Apr 2026 | [Colombia’s Petro Warns of Another Minimum Wage Gike if Interest Rates Rise Again](https://colombiaone.com/2026/04/22/colombia-petro-warns-minimum-wage-gike-interest-rates-rise/) | colombiaone.com | 8 | negative |
| 22 Apr 2026 | [2027: UK-based Surveyor declares for presidency under PDP](https://guardian.ng/news/2027-uk-based-surveyor-declares-for-presidency-under-pdp/) | guardian.ng | 8 | positive |
| 22 Apr 2026 | [027: UK-based Surveyor declares for presidency under PDP](https://guardian.ng/news/027-uk-based-surveyor-declares-for-presidency-under-pdp/) | guardian.ng | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "minimum wage" --since 2026-01-01 --until 2026-04-30
prism-news trends "minimum wage" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "minimum wage" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "minimum wage", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "minimum wage", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Antitrust News](antitrust-news.md)
- [Waqf News](waqf-news.md)
- [GDPR News](gdpr-news.md)
- [Gun Control News](gun-control-news.md)
