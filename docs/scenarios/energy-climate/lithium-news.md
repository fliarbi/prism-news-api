# Lithium News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lithium news” · 140/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [lithium-news.json](../../examples/scenarios/lithium-news.json).

**Question.** How did lithium coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="lithium"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,189 |
| Negative · neutral · positive | 18% · 2.5% · 80% |
| Critical (priority 7–9) | 69% (6,324 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,909 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | battery charging systems |

## Twelve months of coverage

Monthly matching articles for `lithium` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,647 | 69% | 338 | 1,250 | ███████████ |
| Jun 2025 | 1,266 | 71% | 184 | 1,048 | █████████ |
| Jul 2025 | 1,602 | 72% | 279 | 1,296 | ███████████ |
| Aug 2025 | 1,572 | 74% | 319 | 1,228 | ███████████ |
| Sep 2025 | 1,874 | 74% | 420 | 1,412 | █████████████ |
| Oct 2025 | 2,105 | 72% | 401 | 1,657 | ██████████████ |
| Nov 2025 | 1,675 | 72% | 227 | 1,408 | ████████████ |
| Dec 2025 | 1,651 | 74% | 258 | 1,336 | ███████████ |
| Jan 2026 | 2,163 | 75% | 327 | 1,787 | ███████████████ |
| Feb 2026 | 2,145 | 67% | 336 | 1,757 | ███████████████ |
| Mar 2026 | 1,972 | 67% | 324 | 1,589 | ██████████████ |
| Apr 2026 | 2,909 | 66% | 622 | 2,215 | ████████████████████ |

The last four complete months averaged 2,297 articles a month against 1,522 in the first four (+51%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,462 | 16% |
| China | 377 | 4.1% |
| Canada | 359 | 3.9% |
| India | 281 | 3.1% |
| Australia | 145 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| battery charging systems | 1,227 | 20% | +21% |
| battery backup systems for electronics | 988 | 16% | +28% |
| mineral exploration drilling techniques | 289 | 4.8% | +26% |
| lithium-ion battery advancements for evs | 232 | 3.8% | +72% |
| ev battery recycling and sustainability | 215 | 3.5% | +69% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Expanding the lifespan of solid-state batteries](https://www.mpg.de/26391218/how-dendrites-shorten-the-lifespan-of-solid-state-batteries) | mpg.de | 8 | positive |
| 26 Apr 2026 | [Carbon neutrality mission: India’s clean energy future hinges on access to critical minerals \| Mint](http://livemint.com/opinion/online-views/carbon-neutrality-mission-india-clean-energy-future-critical-minerals-fossil-fuel-china-cobalt-lithium-rare-earths-11776934859342.html) | livemint.com | 8 | negative |
| 25 Apr 2026 | [Tesla’s ‘Clean’ Lithium Supply Faces Questions After Toxic Metals Found in Wastewater](https://www.yahoo.com/news/articles/tesla-clean-lithium-supply-faces-213000842.html) | yahoo.com | 8 | negative |
| 25 Apr 2026 | [Elevra Lithium Q3 Earnings Call Highlights](https://www.defenseworld.net/2026/04/25/elevra-lithium-q3-earnings-call-highlights.html) | defenseworld.net | 8 | positive |
| 23 Apr 2026 | [Siemens and Vulcan Energy partner to scale Europe’s sustainable lithium supply - theenergyst.com](https://theenergyst.com/siemens-and-vulcan-energy-partner-to-scale-europes-sustainable-lithium-supply/) | theenergyst.com | 8 | positive |
| 22 Apr 2026 | [Tesla's Texas Lithium Refinery Discharge Contains Toxic Metals, Independent Lab Testing Finds—Drainage Di](https://www.benzinga.com/markets/tech/26/04/51962611/teslas-texas-lithium-refinery-discharge-contains-toxic-metals-independent-lab-testing-finds-drainage-district-demands-cease-and-desist) | benzinga.com | 8 | negative |
| 20 Apr 2026 | [Rio Tinto trying to meet U.S. aluminum demand as Middle East war roils supply chains](https://www.theglobeandmail.com/business/article-rio-tinto-trying-to-meet-us-aluminum-demand-as-middle-east-war-roils/) | theglobeandmail.com | 8 | negative |
| 17 Apr 2026 | [Albemarle Stock 2026: Buy or Sell? Lithium Rebound Sparks 16% Surge as Analysts Eye Further Upside](https://ibtimes.com.au/albemarle-stock-2026-buy-sell-lithium-rebound-sparks-16-surge-analysts-eye-further-upside-1866851) | ibtimes.com.au | 8 | positive |
| 17 Apr 2026 | [Laufey, "Die Queen", "Stirb langsam 3": TV-Tipps für Freitag](https://www.derstandard.at/story/3000000315682/laufey-die-queen-stirb-langsam-3-tv-tipps-fuer-freitag) | derstandard.at | 8 | negative |
| 15 Apr 2026 | [Lithium Reduces Risk of Suicide and Recurrent Episodes of Bipolar and Major Depressive Disorders \|…](https://www.psychiatrictimes.com/view/lithium-reduces-risk-of-suicide-and-recurrent-episodes-of-bipolar-and-major-depressive-disorders) | psychiatrictimes.com | 8 | negative |
| 15 Apr 2026 | [Government announces royalty rate on mining of Lithium, Niobuim and Rare Earth Elements \| Autocar Professional](https://www.autocarpro.in/news/government-announces-royalty-rate-on-mining-of-lithium-niobuim-and-rare-earth-elements--117235) | autocarpro.in | 8 | positive |
| 14 Apr 2026 | [How to Fix Unusual Traffic Detected from Your Computer Network - Time News](https://time.news/how-to-fix-unusual-traffic-detected-from-your-computer-network-32/) | time.news | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "lithium" --since 2026-01-01 --until 2026-04-30
prism-news trends "lithium" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "lithium" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "lithium", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "lithium", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Solar Energy News](solar-energy-news.md)
- [Air Pollution Industry](air-pollution-industry.md)
- [Refinery News](refinery-news.md)
- [Energy Storage News](energy-storage-news.md)
