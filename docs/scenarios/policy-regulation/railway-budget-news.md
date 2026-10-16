# Railway Budget News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “railway budget news” · 110/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [railway-budget-news.json](../../examples/scenarios/railway-budget-news.json).

**Question.** How did coverage of railway budget develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="railway budget"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 102 |
| Negative · neutral · positive | 14% · 3.9% · 82% |
| Critical (priority 7–9) | 83% (85 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (61 articles) |
| Most-reported country | India (51% of matches) |
| Strongest theme by lift | rail infrastructure maintenance practices |

## Twelve months of coverage

Monthly matching articles for `railway budget` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 100% | 0 | 2 | █ |
| Jun 2025 | 1 | 100% | 0 | 1 | █ |
| Jul 2025 | 2 | 0.0% | 0 | 1 | █ |
| Aug 2025 | 1 | 100% | 0 | 1 | █ |
| Sep 2025 | 1 | 100% | 0 | 1 | █ |
| Oct 2025 | 0 | — | 0 | 0 |  |
| Nov 2025 | 0 | — | 0 | 0 |  |
| Dec 2025 | 4 | 100% | 3 | 1 | █ |
| Jan 2026 | 22 | 68% | 3 | 18 | ███████ |
| Feb 2026 | 61 | 85% | 4 | 55 | ████████████████████ |
| Mar 2026 | 12 | 100% | 5 | 6 | ████ |
| Apr 2026 | 7 | 86% | 2 | 5 | ██ |

The last four complete months averaged 26 articles a month against 2 in the first four (+1600%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 52 | 51% |
| United States | 2 | 2.0% |
| United Kingdom | 1 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| rail infrastructure maintenance practices | 21 | 43% | — |
| high-speed train operations and amenities | 9 | 18% | — |
| rail freight network infrastructure | 13 | 27% | — |
| railway station facilities and services | 5 | 10% | new |
| government fiscal policy implementation | 10 | 20% | — |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [The government will issue a gazette notification creating the South Coastal Railway Zone, effective June 1,…](https://investmentguruindia.com/newsdetail/south-coastal-railway-zone-to-become-operational-from-june-1-ashwini-vaishnaw746453) | investmentguruindia.com | 8 | positive |
| 2 Feb 2026 | [Railway Budget 2026 allocation: Delhi gets Rs 2711 cr, first bullet train route announced](https://indianexpress.com/article/cities/delhi/railway-budget-2026-allocation-delhi-gets-rs-2711-cr-first-bullet-train-route-announced-10509156/) | indianexpress.com | 8 | positive |
| 1 Feb 2026 | [Nothing For Common Man, Bengal In 'Directionless' Budget: Mamata Banerjee \| Outlook India](https://www.outlookindia.com/national/nothing-for-common-man-bengal-in-directionless-budget-mamata) | outlookindia.com | 8 | negative |
| 25 Jan 2026 | [Railway Budget 2026 expectations: a reform roadmap for India](https://www.railway.supply/railway-budget-2026-expectations-a-reform-roadmap-for-india/) | railway.supply | 8 | positive |
| 16 Mar 2026 | [Lok Sabha Today: अनुराग ठाकुर ने वित्त मंत्री सीतारमण से पूछा सवाल तो स्पीकर ओम बिरला ने ले ली चुटकी \| Today…](https://www.livemint.com/hindi/news/when-anurag-thakur-posed-a-question-to-finance-minister-nirmala-sitharaman-speaker-om-birla-took-a-lighthearted-jibe-241773651559127.html) | livemint.com | 7 | neutral |
| 3 Feb 2026 | [रेलवे ने दिया MP को अब तक सबसे बड़ा बजट, मिलेंगे 15,188 करोड़, जानिए क्या होगा काम](http://zeenews.india.com/hindi/india/madhya-pradesh-chhattisgarh/bhopal/railways-allocated-budget-15188-crore-to-madhya-pradesh-new-lines-doubling-tripling-station-development/3096297) | zeenews.india.com | 7 | positive |
| 3 Feb 2026 | [Odisha gets record Rs 10,928 crore in Railway Budget](https://www.newindianexpress.com/states/odisha/2026/Feb/03/odisha-gets-record-rs-10928-crore-in-railway-budget) | newindianexpress.com | 7 | positive |
| 3 Feb 2026 | [T.N. gets more than ₹7,500 crore in the railway budget 2026-27](https://www.thehindu.com/news/cities/chennai/tn-gets-more-than-7500-crore-in-the-railway-budget-2026-27/article70583663.ece) | thehindu.com | 7 | positive |
| 2 Feb 2026 | [Railway budget 2026 new train: More Vande Bharat, Amrit Bharat, Namo Bharat trains to join fleet, says…](https://indianexpress.com/article/india/railway-budget-2026-new-train-vande-bharat-amrit-bharat-namo-bharat-trains-ashwini-vaishnaw-10508969/) | indianexpress.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "railway budget" --since 2026-01-01 --until 2026-04-30
prism-news trends "railway budget" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "railway budget" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "railway budget", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "railway budget", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Rent Control News](rent-control-news.md)
- [Digital Markets Act News](digital-markets-act-news.md)
- [Cryptocurrency Regulation News](cryptocurrency-regulation-news.md)
- [Insurance Regulation News](insurance-regulation-news.md)
