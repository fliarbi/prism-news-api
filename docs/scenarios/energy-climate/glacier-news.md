# Glacier News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “glacier news” · 90/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [glacier-news.json](../../examples/scenarios/glacier-news.json).

**Question.** How did glacier coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="glacier"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,558 |
| Negative · neutral · positive | 37% · 3.2% · 60% |
| Critical (priority 7–9) | 44% (684 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (694 articles) |
| Most-reported country | United States (23% of matches) |
| Strongest theme by lift | melting polar ice caps and sea level rise |

## Twelve months of coverage

Monthly matching articles for `glacier` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 601 | 68% | 393 | 185 | █████████████████ |
| Jun 2025 | 361 | 50% | 120 | 227 | ██████████ |
| Jul 2025 | 337 | 42% | 110 | 213 | ██████████ |
| Aug 2025 | 694 | 66% | 426 | 243 | ████████████████████ |
| Sep 2025 | 384 | 54% | 137 | 226 | ███████████ |
| Oct 2025 | 279 | 40% | 84 | 190 | ████████ |
| Nov 2025 | 330 | 46% | 143 | 175 | ██████████ |
| Dec 2025 | 269 | 51% | 106 | 156 | ████████ |
| Jan 2026 | 276 | 43% | 83 | 181 | ████████ |
| Feb 2026 | 404 | 52% | 189 | 198 | ████████████ |
| Mar 2026 | 350 | 40% | 115 | 227 | ██████████ |
| Apr 2026 | 528 | 41% | 192 | 321 | ███████████████ |

The last four complete months averaged 390 articles a month against 498 in the first four (-22%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 45% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 351 | 23% |
| India | 65 | 4.2% |
| Canada | 44 | 2.8% |
| Antarctica | 25 | 1.6% |
| Argentina | 25 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| melting polar ice caps and sea level rise | 106 | 12% | -33% |
| glacial retreat and freshwater resource impacts | 99 | 11% | -34% |
| polar region ecosystem vulnerability | 90 | 9.8% | -37% |
| national parks & protected reserves | 24 | 2.6% | +20% |
| kia engine specifications and technologies | 24 | 2.6% | new |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Central Asia’s climate future hinges on water and resilience - WMO Secretary-General](https://qazinform.com/news/central-asias-climate-future-hinges-on-water-and-resilience-wmo-secretary-general-674a52) | qazinform.com | 9 | negative |
| 13 Apr 2026 | [The melting of glaciers has accelerated - Sea level has risen](https://medianews.az/en/buzlaqlarin-erimesi-suretlenib-deniz-seviyyesi-artib) | medianews.az | 9 | negative |
| 5 Mar 2026 | [Fears Antarctica's 'doomsday' glacier is edging closer to a point of no return](https://metro.co.uk/2026/03/05/antarcticas-doomsday-glacier-edging-closer-a-point-no-return-scientists-fear-27242865/) | metro.co.uk | 9 | negative |
| 16 Feb 2026 | [$80 billion mission could stop Doomsday Glacier that would destroy entire countries](https://www.ladbible.com/news/world-news/doomsday-glacier-mission-stop-billion-585003-20260216) | ladbible.com | 9 | negative |
| 11 Feb 2026 | [The plan to wall off the ‘Doomsday’ glacier](https://theweek.com/environment/plan-wall-curtain-doomsday-glacier) | theweek.com | 9 | negative |
| 28 Apr 2026 | [« Glaciers, enquête sur une disparition » : comment sauver notre monde de glace ?](https://www.la-croix.com/culture/glaciers-enquete-sur-une-disparition-comment-sauver-notre-monde-de-glace-20260427) | la-croix.com | 8 | negative |
| 13 Apr 2026 | [Siachen Day 2024: Army Pays Tribute on Operation Meghdoot Anniversary](https://www.newkerala.com/news/a/army-pays-tribute-bravehearts-42nd-siachen-day-926.htm) | newkerala.com | 8 | positive |
| 13 Apr 2026 | [Op Meghdoot: 42 Years of India's Siachen Defence](https://www.newkerala.com/news/a/42-years-op-meghdoot-iaf-indian-army-pay-821.htm) | newkerala.com | 8 | positive |
| 13 Apr 2026 | [At -50°C on Siachen Glacier: Life on the World’s Highest Battlefield, 42 Years After Operation Meghdoot](https://www.timesnownews.com/lifestyle/people/at-50c-on-siachen-life-on-the-worlds-highest-battlefield-42-years-after-operation-meghdoot-article-154065034) | timesnownews.com | 8 | positive |
| 9 Apr 2026 | [Argentina approves Milei's bill that eases protections for glaciers despite environmental backlash](https://www.castanetkamloops.net/edition/news-story-607953-5-.htm) | castanetkamloops.net | 8 | negative |
| 27 Feb 2026 | [Greenland's largest glacier could soon reach a tipping point, scientists say](https://phys.org/news/2026-02-greenland-largest-glacier-scientists.html) | phys.org | 8 | negative |
| 26 Feb 2026 | [Antarctica Glacier Collapsed Rapidly Due to Flat Bedrock, Study Finds - TIme News](https://time.news/antarctica-glacier-collapsed-rapidly-due-to-flat-bedrock-study-finds/) | time.news | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "glacier" --since 2026-01-01 --until 2026-04-30
prism-news trends "glacier" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "glacier" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "glacier", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "glacier", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Deforestation News](deforestation-news.md)
- [Drought News](drought-news.md)
- [Circular Economy News](circular-economy-news.md)
- [Geothermal News](geothermal-news.md)
