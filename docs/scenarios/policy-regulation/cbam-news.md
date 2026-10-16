# CBAM News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cbam news” · 30/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cbam-news.json](../../examples/scenarios/cbam-news.json).

**Question.** How did coverage of cbam develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="CBAM"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,534 |
| Negative · neutral · positive | 41% · 2.0% · 57% |
| Critical (priority 7–9) | 87% (1,336 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (549 articles) |
| Most-reported country | India (13% of matches) |
| Strongest theme by lift | carbon footprint reduction techniques |

## Twelve months of coverage

Monthly matching articles for `CBAM` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 198 | 90% | 82 | 111 | ███████ |
| Jun 2025 | 180 | 87% | 54 | 122 | ███████ |
| Jul 2025 | 339 | 78% | 135 | 196 | ████████████ |
| Aug 2025 | 165 | 86% | 63 | 98 | ██████ |
| Sep 2025 | 201 | 90% | 63 | 126 | ███████ |
| Oct 2025 | 280 | 86% | 87 | 185 | ██████████ |
| Nov 2025 | 289 | 90% | 126 | 154 | ███████████ |
| Dec 2025 | 335 | 88% | 164 | 161 | ████████████ |
| Jan 2026 | 549 | 90% | 204 | 340 | ████████████████████ |
| Feb 2026 | 414 | 86% | 156 | 247 | ███████████████ |
| Mar 2026 | 263 | 89% | 122 | 139 | ██████████ |
| Apr 2026 | 308 | 82% | 149 | 146 | ███████████ |

The last four complete months averaged 384 articles a month against 220 in the first four (+74%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 57% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 196 | 13% |
| United States | 182 | 12% |
| United Kingdom | 81 | 5.3% |
| China | 75 | 4.9% |
| Belgium | 31 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| carbon footprint reduction techniques | 221 | 21% | +14% |
| metal export-import regulations | 60 | 5.8% | +100% |
| climate change mitigation strategies | 252 | 24% | +12% |
| political economy and resource allocation | 47 | 4.5% | +114% |
| industrial metal market analysis | 68 | 6.6% | +196% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [EU mulls carbon tax break on key Ukrainian military resource](https://www.politico.eu/article/kyiv-in-talks-with-brussels-over-steel-exemption-from-carbon-border-tax/) ⚠ | politico.eu | 8 | negative |
| 30 Apr 2026 | [Morocco's Energy Wager: What European Partners Should Expect by 2030](http://www.kas.de/de/web/europaeische-und-internationale-zusammenarbeit/laenderberichte/detail/-/content/morocco-s-energy-wager-what-european-partners-should-expect-by-2030) ⚠ | kas.de | 8 | negative |
| 28 Apr 2026 | [European Parliament demands €200 billion extra for EU budget](https://www.euronews.com/my-europe/2026/04/28/european-parliament-demands-200-billion-extra-for-eu-budget-in-hardball-talks) ⚠ | euronews.com | 8 | negative |
| 22 Apr 2026 | [How China’s AI carbon accounting model points the finger at the US](https://www.scmp.com/news/china/science/article/3351009/how-chinas-new-ai-carbon-accounting-model-points-finger-us) ⚠ | scmp.com | 8 | positive |
| 22 Apr 2026 | [Iran-linked disruption fuels calls to delay UK carbon border tax](https://www.farminguk.com/news/iran-linked-disruption-fuels-calls-to-delay-uk-carbon-border-tax_68373.html) | farminguk.com | 8 | negative |
| 20 Apr 2026 | [Global supply chains face “normalization” of overlapping risks](https://www.thescxchange.com/finance-strategy/global-supply-chains-face-normalization-of-overlapping-risks) ⚠ | thescxchange.com | 8 | negative |
| 17 Apr 2026 | [India’s quiet masterclass in managing an energy shock](https://www.financialexpress.com/policy/economy/indias-quiet-masterclass-in-managing-an-energy-shock/4210508/) ⚠ | financialexpress.com | 8 | positive |
| 17 Apr 2026 | [EU's proposed CBAM expansion may impact Indian exporters: GTRI](https://energy.economictimes.indiatimes.com/news/renewable/eus-proposed-cbam-expansion-may-impact-indian-exporters-gtri/130321276) | energy.economictimes.indiatimes.com | 8 | negative |
| 16 Apr 2026 | [EU to include more products under CBAM, several Indian exports to be hit](https://www.newindianexpress.com/business/2026/Apr/16/eu-to-include-more-products-under-cbam-several-indian-exports-to-be-hit) | newindianexpress.com | 8 | negative |
| 16 Apr 2026 | [Bidding Goodbye to COP33: Has India Missed a Trick?](https://www.thequint.com/climate-change/india-withdraws-bid-to-host-cop33-why) ⚠ | thequint.com | 8 | positive |
| 15 Apr 2026 | [Sustainability in an Age of Strategic Disorder](https://www.orfonline.org/expert-speak/sustainability-in-an-age-of-strategic-disorder) ⚠ | orfonline.org | 8 | negative |
| 14 Apr 2026 | [Meloni: 'Immediate stop EU stability pact, no Russian gas. Renewal of defence agreement with Israel suspended"](https://en.ilsole24ore.com/art/meloni-subito-stop-patto-stabilita-ue-gas-russo-capisco-descalzi-ma-fare-attenzione-AILwflUC) ⚠ | en.ilsole24ore.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "CBAM" --since 2026-01-01 --until 2026-04-30
prism-news trends "CBAM" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "CBAM" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "CBAM", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "CBAM", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Banking Regulation News](banking-regulation-news.md)
- [Windfall Tax News](windfall-tax-news.md)
- [Immigration Policy News](immigration-policy-news.md)
- [Right to Repair News](right-to-repair-news.md)
