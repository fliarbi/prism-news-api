# LNG News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lng news” · 590/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [lng-news.json](../../examples/scenarios/lng-news.json).

**Question.** How did lng coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="LNG"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 31,429 |
| Negative · neutral · positive | 63% · 1.4% · 36% |
| Critical (priority 7–9) | 85% (26,802 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (14,692 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | natural gas liquefaction processes |

## Twelve months of coverage

Monthly matching articles for `LNG` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,132 | 77% | 700 | 1,396 | ███ |
| Jun 2025 | 2,216 | 80% | 916 | 1,279 | ███ |
| Jul 2025 | 2,254 | 75% | 835 | 1,388 | ███ |
| Aug 2025 | 3,126 | 81% | 986 | 2,102 | ████ |
| Sep 2025 | 3,003 | 79% | 1,043 | 1,929 | ████ |
| Oct 2025 | 2,946 | 82% | 1,152 | 1,756 | ████ |
| Nov 2025 | 2,737 | 81% | 875 | 1,812 | ████ |
| Dec 2025 | 2,760 | 78% | 838 | 1,886 | ████ |
| Jan 2026 | 2,901 | 76% | 942 | 1,909 | ████ |
| Feb 2026 | 4,024 | 77% | 1,366 | 2,578 | █████ |
| Mar 2026 | 14,692 | 91% | 11,511 | 3,014 | ████████████████████ |
| Apr 2026 | 9,812 | 83% | 5,962 | 3,670 | █████████████ |

The last four complete months averaged 7,857 articles a month against 2,432 in the first four (+223%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 6,604 | 21% |
| India | 1,921 | 6.1% |
| Iran | 878 | 2.8% |
| China | 812 | 2.6% |
| United Arab Emirates | 637 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| natural gas liquefaction processes | 4,397 | 20% | +111% |
| liquefied natural gas (lng) storage | 4,646 | 21% | +119% |
| international certifications for oil & gas | 911 | 4.1% | +641% |
| natural gas extraction processes | 2,979 | 13% | +112% |
| gas flaring reduction techniques | 1,357 | 6.1% | +150% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [West Asia conflict could cause 120 bcm of LNG supply loss from 2026-2030, says International Energy Agency](https://www.thehindu.com/business/Industry/west-asia-conflict-could-cause-120-bcm-of-lng-supply-loss-from-2026-2030-says-international-energy-agency/article70900839.ece) | thehindu.com | 9 | negative |
| 24 Apr 2026 | [Transport blackout in 40 days – €50 billion and 500 million barrels of oil sunk in the Persian Gulf –…](https://www.bankingnews.gr/analyseis-ektheseis/articles/870696/transport-blackout-in-40-days-50-billion-and-500-million-barrels-of-oil-sunk-in-the-persian-gulf-waterloo-for-tourism) | bankingnews.gr | 9 | negative |
| 16 Apr 2026 | [LNG shortage triggers extensive blackouts in Pakistan](https://theprint.in/world/lng-shortage-triggers-extensive-blackouts-in-pakistan/2906583/) | theprint.in | 9 | negative |
| 14 Apr 2026 | [Energy prices set to rise as last Gulf Tankers reach Europe](https://euronews.com/my-europe/2026/04/14/energy-prices-set-to-rise-as-last-gulf-tankers-reach-europe-analysts-say) | euronews.com | 9 | negative |
| 14 Apr 2026 | [Strait of Hormuz Shipping Traffic: Security Risks and Future Outlook - Time News](https://time.news/strait-of-hormuz-shipping-traffic-security-risks-and-future-outlook/) | time.news | 9 | negative |
| 13 Apr 2026 | [Which Asian Countries Are Most at Risk From the Iran Energy Shock?](https://thediplomat.com/2026/04/which-asian-countries-are-most-at-risk-from-the-iran-energy-shock/) | thediplomat.com | 9 | negative |
| 9 Apr 2026 | [Southeast Asia Faces Energy Reality Check as War Bites](https://www.energyintel.com/0000019d-620b-d7a3-a59d-72af30f30000) | energyintel.com | 9 | negative |
| 8 Apr 2026 | [Facts about the Strait of Hormuz since its negotiated reopening](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/04/08/facts-about-the-strait-of-hormuz-since-its-negotiated-reopening) | thestar.com.my | 9 | negative |
| 8 Apr 2026 | [Shippers seek clarity on Hormuz reopening after US-Iran ceasefire deal](https://journalrecord.com/2026/04/08/hormuz-strait-shipping-clarity-us-iran-ceasefire/) | journalrecord.com | 9 | negative |
| 8 Apr 2026 | [Key Facts on Strait of Hormuz Following Its Negotiated Reopening](https://www.deccanchronicle.com/world/key-facts-on-the-strait-of-hormuz-following-its-negotiated-reopening-1949299) | deccanchronicle.com | 9 | negative |
| 8 Apr 2026 | [US ceasefire may boost LPG, LNG supplies to India in short term](https://www.thehindubusinessline.com/markets/commodities/us-ceasefire-may-boost-lpg-lng-supplies-to-india-in-short-term/article70837696.ece) | thehindubusinessline.com | 9 | negative |
| 6 Apr 2026 | [Why I'm Fading a 'Ceasefire Rally' as Trump's Iran Deadline Approaches \| TheStreet Pro](https://pro.thestreet.com/market-commentary/why-im-fading-a-ceasefire-rally-as-trumps-iran-deadline-approaches) | pro.thestreet.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "LNG" --since 2026-01-01 --until 2026-04-30
prism-news trends "LNG" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "LNG" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "LNG", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "LNG", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Recycling Industry](recycling-industry.md)
- [Nuclear Power News](nuclear-power-news.md)
- [Rare Earths News](rare-earths-news.md)
- [Diesel Price News](diesel-price-news.md)
