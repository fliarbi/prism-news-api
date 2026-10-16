# Monsoon News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “monsoon news” · 6,600/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [monsoon-news.json](../../examples/scenarios/monsoon-news.json).

**Question.** How did monsoon coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="monsoon"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,296 |
| Negative · neutral · positive | 42% · 8.4% · 50% |
| Critical (priority 7–9) | 69% (1,582 articles) |
| Busiest month, May 2025 – Apr 2026 | Jul 2025 (5,381 articles) |
| Most-reported country | India (37% of matches) |
| Strongest theme by lift | disaster recovery and emergency construction |

## Twelve months of coverage

Monthly matching articles for `monsoon` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,012 | 66% | 1,066 | 755 | ███████ |
| Jun 2025 | 3,257 | 59% | 1,650 | 1,239 | ████████████ |
| Jul 2025 | 5,381 | 56% | 2,854 | 1,936 | ████████████████████ |
| Aug 2025 | 4,624 | 66% | 2,686 | 1,433 | █████████████████ |
| Sep 2025 | 2,624 | 71% | 1,477 | 810 | ██████████ |
| Oct 2025 | 1,178 | 68% | 611 | 447 | ████ |
| Nov 2025 | 689 | 71% | 355 | 306 | ███ |
| Dec 2025 | 556 | 69% | 293 | 235 | ██ |
| Jan 2026 | 294 | 62% | 120 | 156 | █ |
| Feb 2026 | 463 | 68% | 132 | 215 | ██ |
| Mar 2026 | 454 | 60% | 181 | 260 | ██ |
| Apr 2026 | 1,085 | 75% | 519 | 517 | ████ |

The last four complete months averaged 574 articles a month against 3,818 in the first four (-85%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 842 | 37% |
| United States | 177 | 7.7% |
| United Kingdom | 107 | 4.7% |
| Malaysia | 71 | 3.1% |
| Philippines | 19 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| disaster recovery and emergency construction | 50 | 3.2% | +138% |
| monsoon season updates | 379 | 25% | -63% |
| el niño and la niña effects | 226 | 15% | +242% |
| election result certification | 40 | 2.6% | +3900% |
| agricultural weather impacts | 84 | 5.5% | -21% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Apr 2026 | [Eye on monsoon: Part of Delhi Gate drain, covered for 40 yrs, being cleaned, says Minister](https://indianexpress.com/article/cities/delhi/delhi-gate-drain-desilting-samta-sthal-ito-flooding-relief-10630189/) | indianexpress.com | 9 | negative |
| 19 Feb 2026 | [4 years on, Rangirkhal guard wall project stuck; flood fear resurfaces - Times of India](https://timesofindia.indiatimes.com/articleshowprint/128522172.cms) | timesofindia.indiatimes.com | 9 | negative |
| 6 Jan 2026 | [Inundaciones repentinas en Indonesia dejan al menos 16 muertos y arrasan viviendas](https://apnews.com/article/indonesia-celebes-septentrional-inundaciones-repentinas-siau-50069a503f27881a4d39632d8fac7ac7) | apnews.com | 9 | negative |
| 30 Apr 2026 | [A ‘Below Normal’ Monsoon? What El Niño Could Mean for India’s Economy – Outlook Business](https://www.outlookbusiness.com/economy-and-policy/a-below-normal-monsoon-what-el-ni%C3%B1o-could-mean-for-indias-economy) | outlookbusiness.com | 8 | negative |
| 29 Apr 2026 | [Ahead Of Monsoon, BMC Flags 174 Unsafe Buildings, 496 Flood Spots And 249 Landslide Zones In Mumbai](https://curlytales.com/india/trending/ahead-of-monsoon-bmc-flags-unsafe-buildings-flood-spots-and-landslide-zones-in-mumbai/) | curlytales.com | 8 | negative |
| 28 Apr 2026 | [Mumbai monsoon preparedness: BMC to deploy 547 dewatering pumps across city](https://www.mid-day.com/mumbai/mumbai-news/article/mumbai-monsoon-preparedness-bmc-to-deploy-547-dewatering-pumps-across-city-23627890) | mid-day.com | 8 | positive |
| 28 Apr 2026 | [Weak monsoon to have moderate impact on crops](https://www.financialexpress.com/india-news/weak-monsoon-to-havenbspmoderate-impact-on-crops/4221105/) | financialexpress.com | 8 | negative |
| 28 Apr 2026 | [Study warns of another climate risk for TN: Monsoon moist heatwaves](https://www.dtnext.in/news/tamilnadu/study-warns-of-another-climate-risk-for-tn-monsoon-moist-heatwaves) | dtnext.in | 8 | positive |
| 26 Apr 2026 | [Andheri Subway Flooding Set to Persist This Monsoon; BMC Holds Pond Solution Under Consideration](https://www.mumbailive.com/en/civic/andheri-subway-flooding-set-to-persist-this-monsoon-92550) | mumbailive.com | 8 | negative |
| 24 Apr 2026 | [Over 57% desilting work completed in large Delhi drains: Flood control minister](https://infra.economictimes.indiatimes.com/news/urban-infrastructure/delhis-drain-desilting-progress-over-57-completed-ahead-of-monsoon/130489179) | infra.economictimes.indiatimes.com | 8 | positive |
| 24 Apr 2026 | [Early Monsoon Alert: Weather Models Signal Advance Arrival in India](https://www.newsmobile.in/climate/early-monsoon-alert-weather-models-signal-advance-arrival-in-india/) | newsmobile.in | 8 | positive |
| 23 Apr 2026 | [Over 57% desilting of Delhi drains completed ahead of monsoon](https://www.hindustantimes.com/cities/delhi-news/over-57-desilting-of-delhi-drains-completed-ahead-of-monsoon-101776968525341.html) | hindustantimes.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "monsoon" --since 2026-01-01 --until 2026-04-30
prism-news trends "monsoon" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "monsoon" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "monsoon", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "monsoon", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Coal Industry](coal-industry.md)
- [Cyclone News](cyclone-news.md)
- [Climate Change News](climate-change-news.md)
- [Gas Prices News](gas-prices-news.md)
