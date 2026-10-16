# Sugar Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sugar industry” · 3,600/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [sugar-industry.json](../../examples/scenarios/sugar-industry.json).

**Question.** How much news did the sugar industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="sugar industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 339 |
| Negative · neutral · positive | 35% · 1.5% · 64% |
| Critical (priority 7–9) | 69% (235 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (119 articles) |
| Most-reported country | India (11% of matches) |
| Strongest theme by lift | agri-business financing and investment |

## Twelve months of coverage

Monthly matching articles for `sugar industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 67 | 64% | 17 | 46 | ███████████ |
| Jun 2025 | 53 | 66% | 15 | 35 | █████████ |
| Jul 2025 | 56 | 73% | 22 | 33 | █████████ |
| Aug 2025 | 90 | 77% | 57 | 30 | ███████████████ |
| Sep 2025 | 90 | 74% | 39 | 51 | ███████████████ |
| Oct 2025 | 62 | 74% | 17 | 44 | ██████████ |
| Nov 2025 | 53 | 70% | 20 | 31 | █████████ |
| Dec 2025 | 42 | 79% | 13 | 28 | ███████ |
| Jan 2026 | 69 | 80% | 23 | 45 | ████████████ |
| Feb 2026 | 65 | 72% | 30 | 34 | ███████████ |
| Mar 2026 | 86 | 78% | 32 | 53 | ██████████████ |
| Apr 2026 | 119 | 56% | 32 | 85 | ████████████████████ |

The last four complete months averaged 85 articles a month against 66 in the first four (+27%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 37 | 11% |
| United States | 31 | 9.1% |
| Nigeria | 21 | 6.2% |
| South Africa | 19 | 5.6% |
| Kenya | 9 | 2.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agri-business financing and investment | 23 | 12% | +360% |
| agricultural export and international trade | 41 | 22% | +46% |
| agricultural policy and regulatory compliance | 15 | 8.0% | +275% |
| agricultural education and extension services | 11 | 5.8% | +175% |
| farm labor management and safety protocols | 6 | 3.2% | +200% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 2 Apr 2026 | [LPG Crunch Sours India’s Sugar Demand: Mills Struggle to Meet Quotas as Eateries Go Cold - Agro & Food…](https://agronfoodprocessing.com/lpg-crunch-sours-indias-sugar-demand-mills-struggle-to-meet-quotas-as-eateries-go-cold/) | agronfoodprocessing.com | 8 | negative |
| 12 Mar 2026 | [Sugar industry takes R1.5bn knock as imports engulf SA](https://businesslive.co.za/economy/2026-03-12-sa-sugar-industry-faces-r15bn-loss-amid-import-crisis/) | businesslive.co.za | 8 | negative |
| 6 Mar 2026 | [Sugar industry calls for national ethanol mandate amid Iran war oil shock](https://www.abc.net.au/news/2026-03-07/sugar-industry-calls-for-ethanol-mandate/106419518) | abc.net.au | 8 | positive |
| 17 Feb 2026 | [Tongaat Hulett Crisis: Liquidation Threatens 250,000 Jobs](https://www.joburgetc.com/news/tongaat-hulett-liquidation-sugar-farmers-crisis/) | joburgetc.com | 8 | negative |
| 13 Jan 2026 | [Canegrowers group urges government to scrap sugar tax amid surge in imports](https://www.businesslive.co.za/economy/2026-01-13-canegrowers-group-urges-government-to-scrap-sugar-tax-amid-surge-in-imports/) | businesslive.co.za | 8 | negative |
| 5 Jan 2026 | [Kenya exits COMESA sugar safeguard after 24 years, signals readiness to compete regionally - Farmers Review…](https://farmersreviewafrica.com/kenya-exits-comesa-sugar-safeguard-after-24-years-signals-readiness-to-compete-regionally/) | farmersreviewafrica.com | 8 | positive |
| 4 Jan 2026 | [Uncertainty For Sugar Sector As Kenya Exits COMESA Safeguard After 24 Years](https://thekenyatimes.com/business/uncertainty-for-sugar-sector-as-kenya-exits-comesa-safeguard-after-24-years/) | thekenyatimes.com | 8 | positive |
| 22 Apr 2026 | [60 साल पुराने गन्ना कानून में बदलाव की तैयारी: इथेनॉल व डिजिटल नियम जोड़े गए; सरकार ने 20 मई तक मांगे सुझाव](https://www.amarujala.com/business/business-diary/government-overhauls-six-decade-old-sugarcane-law-seeks-comments-on-draft-by-may-20-news-in-hindi-2026-04-22) | amarujala.com | 7 | positive |
| 21 Apr 2026 | [[Vantage Point] Sweetener tariff: Saccharine protection, bitter outcome](https://www.rappler.com/voices/newsletters/vantage-point-tariff-hike-sugar-economy-agriculture/) | rappler.com | 7 | negative |
| 16 Apr 2026 | [South Africa is stabilising its sugar industry through deliberate reform and investment](https://www.sanews.gov.za/south-africa/south-africa-stabilising-its-sugar-industry-through-deliberate-reform-and-investment) | sanews.gov.za | 7 | negative |
| 13 Apr 2026 | [Sugar industry targets diversification push as Phase 2 Master Plan signed](https://iol.co.za/business-report/economy/2026-04-13-sugar-industry-targets-diversification-push-as-phase-2-master-plan-signed/) | iol.co.za | 7 | positive |
| 3 Apr 2026 | [Maharashtra sugar output jumps 22% as 2025–26 crushing season ends](https://www.thehindubusinessline.com/economy/agri-business/maharashtra-sugar-output-jumps-22-as-202526-crushing-season-ends/article70819549.ece) | thehindubusinessline.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "sugar industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "sugar industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "sugar industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "sugar industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "sugar industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Music Industry](music-industry.md)
- [Aerospace Industry](aerospace-industry.md)
- [3d Printing Industry](3d-printing-industry.md)
- [Agriculture Industry](agriculture-industry.md)
