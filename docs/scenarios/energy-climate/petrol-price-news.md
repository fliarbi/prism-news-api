# Petrol Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “petrol price news” · 22,200/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [petrol-price-news.json](../../examples/scenarios/petrol-price-news.json).

**Question.** How did petrol price coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="petrol price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,332 |
| Negative · neutral · positive | 55% · 41% · 3.5% |
| Critical (priority 7–9) | 9.7% (129 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (695 articles) |
| Most-reported country | India (67% of matches) |
| Strongest theme by lift | crude oil refining methods |

## Twelve months of coverage

Monthly matching articles for `petrol price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 33% | 11 | 1 | █ |
| Jun 2025 | 14 | 36% | 12 | 2 | █ |
| Jul 2025 | 19 | 47% | 16 | 3 | █ |
| Aug 2025 | 20 | 5.0% | 18 | 1 | █ |
| Sep 2025 | 20 | 15% | 16 | 4 | █ |
| Oct 2025 | 9 | 33% | 7 | 1 | █ |
| Nov 2025 | 12 | 25% | 8 | 2 | █ |
| Dec 2025 | 23 | 39% | 20 | 3 | █ |
| Jan 2026 | 18 | 28% | 14 | 4 | █ |
| Feb 2026 | 19 | 26% | 12 | 7 | █ |
| Mar 2026 | 695 | 10% | 131 | 16 | ████████████████████ |
| Apr 2026 | 600 | 8.0% | 579 | 20 | █████████████████ |

The last four complete months averaged 333 articles a month against 16 in the first four (+1949%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 78% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 896 | 67% |
| Iran | 27 | 2.0% |
| United States | 19 | 1.4% |
| Pakistan | 18 | 1.4% |
| Nigeria | 15 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| crude oil refining methods | 293 | 29% | +7225% |
| regional gas price variations and trends | 203 | 20% | +1253% |
| gasoline production technologies | 618 | 61% | +2990% |
| oil and gas market trends | 635 | 63% | +3075% |
| crude oil market impact on fuel prices | 48 | 4.7% | +4700% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Petrol Price in Krishnagiri, Check Today's Krishnagiri Petrol Rates 29th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-krishnagiri-today) | businesstoday.in | 6 | negative |
| 29 Apr 2026 | [Petrol Price in Lower Subansiri, Check Today's Lower Subansiri Petrol Rates 29th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-lower-subansiri-today) | businesstoday.in | 6 | negative |
| 29 Apr 2026 | [Petrol Price in Kottayam, Check Today's Kottayam Petrol Rates 29th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-kottayam-today) | businesstoday.in | 6 | negative |
| 28 Apr 2026 | [Petrol Price in Longding, Check Today's Longding Petrol Rates 28th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-longding-today) | businesstoday.in | 6 | negative |
| 28 Apr 2026 | [Petrol Price in Mahe, Check Today's Mahe Petrol Rates 28th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-mahe-today) | businesstoday.in | 6 | negative |
| 26 Apr 2026 | [Petrol Price in Andhra Pradesh, Check Today's Andhra Pradesh Petrol Rates 26th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-andhra-pradesh-today) | businesstoday.in | 6 | negative |
| 26 Apr 2026 | [Petrol Price in Papumpare, Check Today's Papumpare Petrol Rates 26th April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-papumpare-today) | businesstoday.in | 6 | negative |
| 23 Apr 2026 | [Petrol Price in Changlang, Check Today's Changlang Petrol Rates 23rd April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-changlang-today) | businesstoday.in | 6 | negative |
| 23 Apr 2026 | [Petrol Price in Bargarh, Check Today's Bargarh Petrol Rates 23rd April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-bargarh-today) | businesstoday.in | 6 | negative |
| 23 Apr 2026 | [Petrol Price in Ahmednagar, Check Today's Ahmednagar Petrol Rates 23rd April 2026](https://www.businesstoday.in/fuel-price/petrol-price-in-ahmednagar-today) | businesstoday.in | 6 | negative |
| 5 Apr 2026 | [पावर, परफॉर्मेंस या माइलेज पर असर! 160 रुपये लीटर वाले 100 ऑक्टेन पेट्रोल में क्या है ख़ास](https://www.aajtak.in/auto/news/story/100-octane-petrol-explained-what-is-xp100-or-power100-fuel-price-benefits-features-regular-car-bike-use-engine-auaw-dskc-2515695-2026-04-05) | aajtak.in | 6 | positive |
| 31 Mar 2026 | [पेट्रोल और डीजल हुआ महंगा, इस खाड़ी देश ने किया दाम बढ़ाने का ऐलान](https://www.livehindustan.com/business/petrol-and-diesel-price-hike-announced-in-uae-know-details-201774947705635.html) | livehindustan.com | 6 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "petrol price" --since 2026-01-01 --until 2026-04-30
prism-news trends "petrol price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "petrol price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "petrol price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "petrol price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Natural Gas News](natural-gas-news.md)
- [Coal Industry](coal-industry.md)
- [Cyclone News](cyclone-news.md)
