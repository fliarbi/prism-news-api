# Export Controls News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “export controls news” · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [export-controls-news.json](../../examples/scenarios/export-controls-news.json).

**Question.** How did coverage of export controls develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="export controls"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 923 |
| Negative · neutral · positive | 64% · 3.6% · 33% |
| Critical (priority 7–9) | 85% (780 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (1,651 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | semiconductor industry updates |

## Twelve months of coverage

Monthly matching articles for `export controls` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 332 | 88% | 242 | 89 | ████ |
| Jun 2025 | 346 | 85% | 245 | 91 | ████ |
| Jul 2025 | 328 | 75% | 198 | 122 | ████ |
| Aug 2025 | 191 | 88% | 121 | 62 | ██ |
| Sep 2025 | 179 | 85% | 114 | 59 | ██ |
| Oct 2025 | 1,651 | 91% | 1,292 | 324 | ████████████████████ |
| Nov 2025 | 316 | 86% | 220 | 83 | ████ |
| Dec 2025 | 252 | 82% | 140 | 98 | ███ |
| Jan 2026 | 208 | 85% | 129 | 70 | ███ |
| Feb 2026 | 221 | 87% | 140 | 76 | ███ |
| Mar 2026 | 217 | 84% | 144 | 64 | ███ |
| Apr 2026 | 277 | 82% | 174 | 93 | ███ |

The last four complete months averaged 231 articles a month against 299 in the first four (-23%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 258 | 28% |
| China | 141 | 15% |
| India | 15 | 1.6% |
| Japan | 10 | 1.1% |
| Singapore | 10 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| semiconductor industry updates | 64 | 11% | +7% |
| political economy and resource allocation | 38 | 6.7% | -10% |
| semiconductor devices and components | 21 | 3.7% | +110% |
| trade agreements and free trade zones | 20 | 3.5% | -26% |
| metal export-import regulations | 18 | 3.2% | -38% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [ASML boosts 2026 sales forecast despite shrinking China sales](https://www.scmp.com/tech/article/3350243/asml-boosts-2026-sales-forecast-despite-shrinking-china-sales) | scmp.com | 8 | positive |
| 14 Apr 2026 | [Russia places temporary export controls on helium](https://www.gasworld.com/story/russia-places-temporary-export-controls-on-helium/2246455.article/\) | gasworld.com | 8 | negative |
| 14 Apr 2026 | [Russia Introduces Helium Export Controls Amid Global Shortage - The Moscow Times](https://www.themoscowtimes.com/2026/04/14/russia-introduces-helium-export-controls-amid-global-shortage-a92496) | themoscowtimes.com | 8 | negative |
| 14 Apr 2026 | [YMTC Plans New Chip Factories Amid US-China Trade Tensions](https://www.electronicsforyou.biz/industry-buzz/ymtc-plans-new-chip-factories-amid-us-china-trade-tensions) | electronicsforyou.biz | 8 | positive |
| 14 Apr 2026 | [U.S. Tightens Export Controls to Cover Subsidiaries of Blacklisted Firms](https://www.caixinglobal.com/2025-09-30/us-tightens-export-controls-to-cover-subsidiaries-of-blacklisted-firms-102367784.html) | caixinglobal.com | 8 | negative |
| 10 Apr 2026 | [China Reveals $92 Mn AI Servers Using Restricted Nvidia Chips](https://www.electronicsforyou.biz/industry-buzz/china-reveals-92-mn-ai-servers-using-restricted-nvidia-chips/) | electronicsforyou.biz | 8 | negative |
| 9 Apr 2026 | [US lawmakers push new bill to tighten chip equipment curbs on China \| Communications Today](https://www.communicationstoday.co.in/us-lawmakers-push-new-bill-to-tighten-chip-equipment-curbs-on-china/) | communicationstoday.co.in | 8 | negative |
| 8 Apr 2026 | [Why Enforcement Will Determine the Chip Security Act’s Success](https://nationalinterest.org/blog/techland/why-enforcement-will-determine-the-chip-security-acts-success) | nationalinterest.org | 8 | negative |
| 8 Apr 2026 | [Rare earths need financing overhaul as China threat looms: IEA](https://www.gtreview.com/news/global/rare-earths-need-financing-overhaul-as-china-threat-looms-iea/) | gtreview.com | 8 | negative |
| 27 Mar 2026 | [America’s New Way of Economic War](https://foreignaffairs.com/united-states/americas-new-way-economic-war) | foreignaffairs.com | 8 | negative |
| 25 Mar 2026 | [US-China Tech War: AI, Chips & Biotech Become New Fronts](https://www.newkerala.com/news/a/us-sharpens-tech-war-china-across-ai-chips-334.htm) | newkerala.com | 8 | negative |
| 24 Mar 2026 | [China’s use of open‑source AI threatens the US lead in AI development, US Commission warns](https://www.computerworld.com/article/4149313/chinas-use-of-open%e2%80%91source-ai-threatens-the-us-lead-in-ai-development-us-commission-warns.html) | computerworld.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "export controls" --since 2026-01-01 --until 2026-04-30
prism-news trends "export controls" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "export controls" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "export controls", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "export controls", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Right to Repair News](right-to-repair-news.md)
- [Drug Pricing News](drug-pricing-news.md)
- [NEP News](nep-news.md)
- [Consumer Protection News](consumer-protection-news.md)
