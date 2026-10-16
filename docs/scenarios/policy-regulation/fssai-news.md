# FSSAI News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “fssai news” · 1,000/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [fssai-news.json](../../examples/scenarios/fssai-news.json).

**Question.** How did coverage of fssai develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="FSSAI"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,088 |
| Negative · neutral · positive | 38% · 3.3% · 59% |
| Critical (priority 7–9) | 67% (734 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (420 articles) |
| Most-reported country | India (42% of matches) |
| Strongest theme by lift | agricultural policy and regulatory compliance |

## Twelve months of coverage

Monthly matching articles for `FSSAI` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 122 | 62% | 32 | 84 | ██████ |
| Jun 2025 | 206 | 56% | 62 | 139 | ██████████ |
| Jul 2025 | 273 | 54% | 85 | 183 | █████████████ |
| Aug 2025 | 254 | 64% | 66 | 176 | ████████████ |
| Sep 2025 | 215 | 62% | 53 | 158 | ██████████ |
| Oct 2025 | 259 | 65% | 88 | 153 | ████████████ |
| Nov 2025 | 290 | 56% | 87 | 193 | ██████████████ |
| Dec 2025 | 250 | 65% | 90 | 153 | ████████████ |
| Jan 2026 | 177 | 77% | 71 | 101 | ████████ |
| Feb 2026 | 239 | 66% | 83 | 152 | ███████████ |
| Mar 2026 | 252 | 55% | 74 | 152 | ████████████ |
| Apr 2026 | 420 | 72% | 181 | 237 | ████████████████████ |

The last four complete months averaged 272 articles a month against 214 in the first four (+27%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 459 | 42% |
| United States | 73 | 6.7% |
| United Kingdom | 12 | 1.1% |
| China | 10 | 0.9% |
| Austria | 5 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agricultural policy and regulatory compliance | 66 | 12% | +288% |
| farm-to-table logistics and distribution | 29 | 5.1% | +107% |
| food safety regulation compliance | 149 | 26% | +50% |
| public health nutrition programs | 22 | 3.9% | +267% |
| post-harvest storage and preservation | 44 | 7.7% | +100% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Central regulator FSSAI seeks detailed report on suspected food poisoning incident in Gujarat](https://www.dailyexcelsior.com/central-regulator-fssai-seeks-detailed-report-on-suspected-food-poisoning-incident-in-gujarat/) | dailyexcelsior.com | 8 | negative |
| 21 Apr 2026 | [Gujarat Horror Update: FSSAI Launches Probe into Wedding Food Poisoning; Over 400 Hospitalised, Statewide…](https://www.republicworld.com/india/gujarat-horror-update-fssai-launches-probe-into-wedding-food-poisoning-60-hospitalised-statewide-crackdown-ordered) | republicworld.com | 8 | negative |
| 18 Apr 2026 | [FSSAI Directs States to Enforce Ban on Calcium Carbide for Fruit Ripening \| Biz News Desk](https://biznewsdesk.com/news/fssai-directs-states-to-enforce-ban-on-calcium-carbide-for-fruit-ripening/) | biznewsdesk.com | 8 | positive |
| 18 Apr 2026 | [FSSAI Directs States to Enforce Ban on Calcium Carbide for Fruit Ripening](https://mediabulletins.com/news/fssai-directs-states-to-enforce-ban-on-calcium-carbide-for-fruit-ripening/) | mediabulletins.com | 8 | positive |
| 17 Apr 2026 | [India tightens enforcement on illegal fruit ripening agents](https://www.freshplaza.com/north-america/article/9830448/india-tightens-enforcement-on-illegal-fruit-ripening-agents/) | freshplaza.com | 8 | positive |
| 17 Apr 2026 | [FSSAI Bans Calcium Carbide for Fruit Ripening, Orders Vigilance](https://www.newkerala.com/news/a/fssai-orders-strict-vigilance-against-illegal-fruit-ripening-967.htm) | newkerala.com | 8 | negative |
| 13 Apr 2026 | [The Supreme Court of India has Reserved order on a Public Interest Litigation - Food Marketing Technology](https://fmtmagazine.in/the-supreme-court-of-india-has-reserved-order-on-a-public-interest-litigation/) | fmtmagazine.in | 8 | neutral |
| 9 Apr 2026 | [States Lead Crackdown as FSSAI Steps Up Food Safety Enforcement in FY26 - Agro & Food Processing](https://agronfoodprocessing.com/states-lead-crackdown-as-fssai-steps-up-food-safety-enforcement-in-fy26/) | agronfoodprocessing.com | 8 | positive |
| 9 Apr 2026 | [Police action targets data leak, not media: FSSAI sources - www.lokmattimes.com](https://www.lokmattimes.com/national/police-action-targets-data-leak-not-media-fssai-sources/) | lokmattimes.com | 8 | negative |
| 9 Apr 2026 | [Rs 155 crore penalty imposed for misbranding and substandard food products - The Tribune](https://www.tribuneindia.com/news/india/rs-155-crore-penalty-imposed-for-misbranding-and-substandard-food-products/) | tribuneindia.com | 8 | negative |
| 9 Apr 2026 | [FSSAI Data Leak FIR Targets Leakers, Not Media: Sources](https://www.newkerala.com/news/a/police-action-targets-data-leak-not-media-fssai-736.htm) | newkerala.com | 8 | negative |
| 8 Apr 2026 | [Police action targets data leak, not media: FSSAI sources](https://www.aninews.in/news/national/general-news/police-action-targets-data-leak-not-media-fssai-sources20260409002244) | aninews.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "FSSAI" --since 2026-01-01 --until 2026-04-30
prism-news trends "FSSAI" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "FSSAI" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "FSSAI", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "FSSAI", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [MSP News](msp-news.md)
- [Data Privacy News](data-privacy-news.md)
- [Brexit News](brexit-news.md)
- [Census Latest](census-latest.md)
