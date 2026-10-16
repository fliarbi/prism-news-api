# Diamond Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “diamond industry” · 1,600/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [diamond-industry.json](../../examples/scenarios/diamond-industry.json).

**Question.** How much news did the diamond industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="diamond industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 125 |
| Negative · neutral · positive | 30% · 4.0% · 66% |
| Critical (priority 7–9) | 62% (78 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (41 articles) |
| Most-reported country | India (21% of matches) |
| Strongest theme by lift | designer scarves and shawls |

## Twelve months of coverage

Monthly matching articles for `diamond industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 27 | 52% | 8 | 19 | █████████████ |
| Jun 2025 | 25 | 88% | 10 | 15 | ████████████ |
| Jul 2025 | 23 | 70% | 13 | 10 | ███████████ |
| Aug 2025 | 34 | 76% | 25 | 9 | █████████████████ |
| Sep 2025 | 35 | 77% | 13 | 22 | █████████████████ |
| Oct 2025 | 25 | 68% | 16 | 9 | ████████████ |
| Nov 2025 | 20 | 55% | 3 | 17 | ██████████ |
| Dec 2025 | 19 | 84% | 7 | 12 | █████████ |
| Jan 2026 | 41 | 54% | 9 | 28 | ████████████████████ |
| Feb 2026 | 33 | 76% | 10 | 22 | ████████████████ |
| Mar 2026 | 26 | 62% | 9 | 17 | █████████████ |
| Apr 2026 | 25 | 60% | 9 | 16 | ████████████ |

The last four complete months averaged 31 articles a month against 27 in the first four (+15%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 26 | 21% |
| South Africa | 12 | 9.6% |
| United States | 9 | 7.2% |
| Namibia | 4 | 3.2% |
| China | 2 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| designer scarves and shawls | 16 | 24% | +46% |
| luxury silk scarves | 16 | 24% | +23% |
| decorative hair clips and headbands | 11 | 16% | +57% |
| elegant ties and bow ties | 10 | 15% | +0% |
| designer cufflinks and tie clips | 9 | 13% | +29% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Mar 2026 | [Indian Jeweller (IJ) – Government Issues SOP on Bank Account Freezing, Bringing Relief to Surat Diamond…](https://www.indianjeweller.in/Indian-Jewellery-News/16026/government-issues-sop-on-bank-account-freezing-bringing-relief-to-surat-diamond-industry) | indianjeweller.in | 8 | positive |
| 22 Apr 2026 | [‘Worst in 60 years’: SRK Chairman & BJP MP Govind Dholakia on India’s diamond sector crisis, sees recovery…](https://www.thehindubusinessline.com/companies/worst-in-60-years-srk-chairman-bjp-mp-govind-dholakia-on-indias-diamond-sector-crisis-sees-recovery-ahead/article70892465.ece) | thehindubusinessline.com | 7 | negative |
| 10 Mar 2026 | [Bhopal News: Middle East Crisis Takes Shine Off Panna Diamond Trade, Auction Uncertain](https://www.freepressjournal.in/bhopal/bhopal-news-middle-east-crisis-takes-shine-off-panna-diamond-trade-auction-uncertain) | freepressjournal.in | 7 | negative |
| 5 Feb 2026 | [US Tariff Slash Set To Revive Surat’s Diamond Industry & Boost Exports](https://www.freepressjournal.in/business/us-slashes-tariff-on-indian-goods-from-50-to-18-set-to-revive-surats-diamond-industry-boost-exports) | freepressjournal.in | 7 | negative |
| 2 Feb 2026 | [Diamonds, wigs, cucumbers and carpets exporters set for rebound as India–US trade deal eases tariffs-…](https://www.moneycontrol.com/news/business/economy/diamonds-wigs-cucumbers-and-carpets-exporters-set-for-rebound-as-india-us-trade-deal-eases-tariffs-13806758.html) | moneycontrol.com | 7 | negative |
| 19 Jan 2026 | [Indian Jeweller (IJ) – We are optimistic about India’s diamond export trajectory in 2026 Sabyasachi Ray, ED,…](https://www.indianjeweller.in/Indian-Jewellery-News/15922/we-are-optimistic-about-indias-diamond-export-trajectory-in-2026-sabyasachi-ray-ed-gjepc) | indianjeweller.in | 7 | positive |
| 1 Jan 2026 | [Indian Jeweller (IJ) – BIS Notifies Diamond Disclosure Standard IS 19469:2025](https://www.indianjeweller.in/Indian-Jewellery-News/15878/bis-notifies-diamond-disclosure-standard-is-19469:2025) | indianjeweller.in | 7 | positive |
| 1 Apr 2026 | [Ashwini Vaishnaw shares Surat Bullet Train Station video with diamond design & smart functions](http://economictimes.indiatimes.com/news/india/ashwini-vaishnaw-shares-surat-bullet-train-station-video-with-diamond-design-smart-functions/videoshow/129948032.cms) | economictimes.indiatimes.com | 6 | positive |
| 24 Mar 2026 | [Amid war concerns, Dubai group to auction rough diamonds in Surat](https://indianexpress.com/article/cities/ahmedabad/amid-war-concerns-dubai-group-to-auction-rough-diamonds-in-surat-10599355/) | indianexpress.com | 6 | positive |
| 27 Jan 2026 | [Textile traders’ body sends wish list to FM: ‘Textile varsity in Surat, funds for R&D’](https://indianexpress.com/article/cities/ahmedabad/textile-traders-body-sends-wish-list-to-fm-textile-varsity-in-surat-funds-for-rd-10498279/) | indianexpress.com | 6 | positive |
| 27 Jan 2026 | [Indian Jeweller (IJ) – De Beers is investing more in natural diamond marketing than it has in over a decade…](https://www.indianjeweller.in/Indian-Jewellery-News/15945/cover-story.html) | indianjeweller.in | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "diamond industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "diamond industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "diamond industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "diamond industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "diamond industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cement Industry](cement-industry.md)
- [Fashion Industry](fashion-industry.md)
- [Gaming Industry](gaming-industry.md)
- [Healthcare Industry](healthcare-industry.md)
