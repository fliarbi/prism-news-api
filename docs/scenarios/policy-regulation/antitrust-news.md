# Antitrust News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “antitrust news” · 10/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [antitrust-news.json](../../examples/scenarios/antitrust-news.json).

**Question.** How did coverage of antitrust develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="antitrust"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,012 |
| Negative · neutral · positive | 67% · 5.0% · 28% |
| Critical (priority 7–9) | 82% (4,932 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (2,697 articles) |
| Most-reported country | United States (56% of matches) |
| Strongest theme by lift | antitrust & competition law |

## Twelve months of coverage

Monthly matching articles for `antitrust` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 972 | 81% | 744 | 193 | ███████ |
| Jun 2025 | 821 | 82% | 564 | 220 | ██████ |
| Jul 2025 | 909 | 74% | 652 | 225 | ███████ |
| Aug 2025 | 1,127 | 80% | 830 | 246 | ████████ |
| Sep 2025 | 1,592 | 83% | 1,208 | 347 | ████████████ |
| Oct 2025 | 650 | 81% | 440 | 180 | █████ |
| Nov 2025 | 953 | 86% | 707 | 224 | ███████ |
| Dec 2025 | 1,262 | 87% | 890 | 345 | █████████ |
| Jan 2026 | 725 | 81% | 492 | 204 | █████ |
| Feb 2026 | 2,697 | 83% | 1,636 | 852 | ████████████████████ |
| Mar 2026 | 1,224 | 80% | 869 | 325 | █████████ |
| Apr 2026 | 1,366 | 84% | 1,043 | 287 | ██████████ |

The last four complete months averaged 1,503 articles a month against 957 in the first four (+57%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 66% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 3,395 | 56% |
| India | 100 | 1.7% |
| United Kingdom | 90 | 1.5% |
| China | 67 | 1.1% |
| Italy | 36 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| antitrust & competition law | 240 | 7.1% | -27% |
| cannabis legalization trends & economic impact | 224 | 6.6% | new |
| corporate governance and board decisions | 152 | 4.5% | +171% |
| regulatory compliance frameworks | 131 | 3.9% | +773% |
| medical marijuana laws & regulatory frameworks | 119 | 3.5% | new |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Apple accuses India’s CCI of exceeding its powers in antitrust case](https://appleworld.today/2026/04/apple-accuses-indias-cci-of-exceeding-its-powers-in-antitrust-casein/) | appleworld.today | 8 | negative |
| 30 Apr 2026 | [Apple says India antitrust body overstepping judicial authority as spat intensifies - News India Times](https://newsindiatimes.com/apple-says-india-antitrust-body-overstepping-judicial-authority-as-spat-intensifies/) | newsindiatimes.com | 8 | negative |
| 30 Apr 2026 | [Apple says India's antitrust body overstepping judicial authority as spat intensifies](https://economictimes.indiatimes.com/industry/cons-products/electronics/apple-says-cci-overstepping-judicial-authority-as-spat-intensifies/articleshow/130640773.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Italy closes antitrust probes into AI firms after commitments on 'hallucination' risks - The Economic Times](https://economictimes.indiatimes.com/tech/artificial-intelligence/italy-closes-antitrust-probes-into-ai-firms-after-commitments-on-hallucination-risks/articleshow/130635689.cms) | economictimes.indiatimes.com | 8 | negative |
| 27 Apr 2026 | [Google gets pointers from EU regulators on helping AI rivals access services - The Economic Times](https://economictimes.indiatimes.com/tech/artificial-intelligence/google-gets-pointers-from-eu-regulators-on-helping-ai-rivals-access-services/articleshow/130560529.cms) | economictimes.indiatimes.com | 8 | negative |
| 27 Apr 2026 | [$2.67B Blue Cross Blue Shield settlement to finally start payouts soon – how to see if you’re eligible](https://nypost.com/2026/04/27/business/2-67b-blue-cross-blue-shield-settlement-to-finally-start-payouts-soon-heres-how-to-know-if-youre-eligible/) | nypost.com | 8 | negative |
| 27 Apr 2026 | [The death of the super carrier dream as United drops pursuit of American Airlines merger](https://www.domain-b.com/industry/industry-general/united-american-airlines-merger-speculation-ends-2026) | domain-b.com | 8 | negative |
| 24 Apr 2026 | [Brazil Opens a Formal Antitrust Case Against Google Over How AI Search Uses News Content](https://www.riotimesonline.com/brazil-cade-google-ai-news-antitrust-probe-april-2026/) | riotimesonline.com | 8 | negative |
| 21 Apr 2026 | [DOJ Pushes Back on Apple’s Bid to Obtain Samsung Documents in Antitrust Case \| PYMNTS.com](https://www.pymnts.com/cpi-posts/doj-pushes-back-on-apples-bid-to-obtain-samsung-documents-in-antitrust-case/) | pymnts.com | 8 | negative |
| 21 Apr 2026 | [Trump opposes United–American merger, signals support for Spirit](https://neworleanscitybusiness.com/blog/2026/04/21/trump-united-american-airlines-merger-opposition/) | neworleanscitybusiness.com | 8 | negative |
| 21 Apr 2026 | [Exclusive-India flips AB InBev from witness to target in antitrust probe, triggering court fight](https://retail.economictimes.indiatimes.com/news/food-entertainment/grocery/exclusive-india-flips-ab-inbev-from-witness-to-target-in-antitrust-probe-triggering-court-fight/130414983) | retail.economictimes.indiatimes.com | 8 | negative |
| 21 Apr 2026 | [U.S. Department of Justice criticizes Apple’s request in ongoing antitrust case](https://appleworld.today/2026/04/u-s-department-of-justice-criticizes-apples-request-in-ongoing-antitrust-case/) | appleworld.today | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "antitrust" --since 2026-01-01 --until 2026-04-30
prism-news trends "antitrust" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "antitrust" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "antitrust", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "antitrust", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Census Latest](census-latest.md)
- [Capital Gains Tax News](capital-gains-tax-news.md)
- [Waqf News](waqf-news.md)
- [Minimum Wage News](minimum-wage-news.md)
