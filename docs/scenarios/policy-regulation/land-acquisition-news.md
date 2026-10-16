# Land Acquisition News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “land acquisition news” · 90/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [land-acquisition-news.json](../../examples/scenarios/land-acquisition-news.json).

**Question.** How did coverage of land acquisition develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="land acquisition"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,401 |
| Negative · neutral · positive | 31% · 4.5% · 64% |
| Critical (priority 7–9) | 70% (2,373 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,060 articles) |
| Most-reported country | India (28% of matches) |
| Strongest theme by lift | land surveying and geotechnical analysis |

## Twelve months of coverage

Monthly matching articles for `land acquisition` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 501 | 71% | 168 | 311 | █████████ |
| Jun 2025 | 464 | 70% | 154 | 287 | █████████ |
| Jul 2025 | 681 | 60% | 236 | 420 | █████████████ |
| Aug 2025 | 714 | 62% | 284 | 405 | █████████████ |
| Sep 2025 | 622 | 76% | 227 | 381 | ████████████ |
| Oct 2025 | 388 | 68% | 127 | 250 | ███████ |
| Nov 2025 | 489 | 72% | 169 | 294 | █████████ |
| Dec 2025 | 649 | 73% | 224 | 398 | ████████████ |
| Jan 2026 | 624 | 68% | 179 | 412 | ████████████ |
| Feb 2026 | 891 | 74% | 326 | 531 | █████████████████ |
| Mar 2026 | 826 | 67% | 246 | 543 | ████████████████ |
| Apr 2026 | 1,060 | 69% | 315 | 691 | ████████████████████ |

The last four complete months averaged 850 articles a month against 590 in the first four (+44%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 945 | 28% |
| United States | 355 | 10% |
| United Kingdom | 57 | 1.7% |
| Nigeria | 35 | 1.0% |
| Ghana | 19 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| land surveying and geotechnical analysis | 258 | 16% | +63% |
| construction project management techniques | 146 | 8.9% | +204% |
| residential housing development projects | 62 | 3.8% | +148% |
| infrastructure development for new communities | 47 | 2.9% | +24% |
| infrastructure maintenance and repair strategies | 170 | 10% | +54% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Pune: ₹1.5 Crore Per Acre Fixed for Purandar Airport Land; Acquisition to Begin from May 4](https://www.thebridgechronicle.com/pune/purandar-airport-land-acquisition-1-5-crore-per-acre-pune-may-4-agn97) | thebridgechronicle.com | 8 | positive |
| 28 Apr 2026 | [Telangana CM Revanth Reddy says Future City land acquisition cannot be stopped](https://telanganatoday.com/telangana-cm-revanth-reddy-says-future-city-land-acquisition-cannot-be-stopped) | telanganatoday.com | 8 | negative |
| 25 Apr 2026 | [Maharashtra govt greenlights HUDCO funding for 3 major eastern Expressways – Know project cost, routes here](https://www.financialexpress.com/business/roadways/maharashtra-govt-greenlights-hudco-funding-for-3-major-expressways-know-project-cost-routes-herenbsp/4218074/) | financialexpress.com | 8 | positive |
| 25 Apr 2026 | [Railway Plans Faster Rollout Of Bullet Train Corridors With Single Window Clearance - Metro Rail News](https://metrorailnews.in/railway-plans-faster-rollout-of-bullet-train-corridors-with-single-window-clearance/) | metrorailnews.in | 8 | positive |
| 25 Apr 2026 | [Maha Govt grants ₹6,000 Crore guarantee to fast-track Purandar International Airport Project](http://www.uniindia.com/maha-govt-grants-6-000-crore-guarantee-to-fast-track-purandar-international-airport-project/west/news/3822804.html) | uniindia.com | 8 | positive |
| 22 Apr 2026 | [Maharashtra Approves Metro Line 5-A, Expressway Projects](https://www.newkerala.com/news/a/maha-govt-approves-metro-line-5-a-hudco-loans-705.htm) | newkerala.com | 8 | positive |
| 22 Apr 2026 | [Nod for Metro 5 & 5A linking Thane, Bhiwandi, Kalyan and Ulhasnagar](https://indianexpress.com/article/cities/mumbai/nod-for-metro-5-5a-linking-thane-bhiwandi-kalyan-and-ulhasnagar-10650952/) | indianexpress.com | 8 | positive |
| 18 Apr 2026 | [Maharashtra to fast-track land acquisition for data centre investments: CM Devendra Fadnavis](https://www.mid-day.com/mumbai/mumbai-news/article/maharashtra-to-fast-track-land-for-data-centre-investments-cm-devendra-fadnavis-23626394) | mid-day.com | 8 | positive |
| 16 Apr 2026 | [One of Britain’s largest housebuilders, Barratt Redrow, is scaling back its land acquisition plans, citing…](https://bebeez.eu/2026/04/16/major-housebuilder-cuts-land-buying-plans-amid-global-uncertainty/) | bebeez.eu | 8 | negative |
| 14 Apr 2026 | [Pune: Civic Panel Reviews 12 Missing Link Road Projects, Pushes Land Acquisition and Encroachment Removal -…](https://www.mypunepulse.com/pune-civic-panel-reviews-12-missing-link-road-projects-pushes-land-acquisition-and-encroachment-removal/) | mypunepulse.com | 8 | positive |
| 13 Apr 2026 | [SC suspends jail sentence, grants bail to ex-Jharkhand minister Anosh Ekka](https://www.hindustantimes.com/cities/ranchi-news/sc-suspends-jail-sentence-grants-bail-to-ex-jharkhand-minister-anosh-ekka-101776089729761.html) | hindustantimes.com | 8 | negative |
| 13 Apr 2026 | [Katraj-Kondhwa road widening project receives fresh push; state allocates ₹140cr for land acquisition](https://www.hindustantimes.com/cities/pune-news/katrajkondhwa-road-widening-project-receives-fresh-push-state-allocates-140cr-for-land-acquisition-101776020788212.html) | hindustantimes.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "land acquisition" --since 2026-01-01 --until 2026-04-30
prism-news trends "land acquisition" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "land acquisition" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "land acquisition", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "land acquisition", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cryptocurrency Regulation News](cryptocurrency-regulation-news.md)
- [Insurance Regulation News](insurance-regulation-news.md)
- [Social Media Regulation News](social-media-regulation-news.md)
- [Disaster Management News](disaster-management-news.md)
