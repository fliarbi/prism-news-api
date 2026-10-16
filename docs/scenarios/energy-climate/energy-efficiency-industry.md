# Energy Efficiency Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “energy efficiency industry” · 90/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [energy-efficiency-industry.json](../../examples/scenarios/energy-efficiency-industry.json).

**Question.** How did energy efficiency coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="energy efficiency"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 57,760 |
| Negative · neutral · positive | 13% · 1.1% · 86% |
| Critical (priority 7–9) | 59% (34,073 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (17,764 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | energy-efficient home solutions |

## Twelve months of coverage

Monthly matching articles for `energy efficiency` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10,572 | 57% | 1,334 | 9,084 | ████████████ |
| Jun 2025 | 9,489 | 60% | 1,066 | 8,321 | ███████████ |
| Jul 2025 | 10,036 | 57% | 1,151 | 8,726 | ███████████ |
| Aug 2025 | 9,586 | 55% | 1,135 | 8,353 | ███████████ |
| Sep 2025 | 11,973 | 55% | 948 | 10,937 | █████████████ |
| Oct 2025 | 11,494 | 60% | 1,015 | 10,395 | █████████████ |
| Nov 2025 | 11,306 | 61% | 1,031 | 10,157 | █████████████ |
| Dec 2025 | 10,782 | 62% | 1,254 | 9,422 | ████████████ |
| Jan 2026 | 11,133 | 62% | 1,290 | 9,709 | █████████████ |
| Feb 2026 | 14,304 | 59% | 1,607 | 12,517 | ████████████████ |
| Mar 2026 | 14,559 | 58% | 2,224 | 12,172 | ████████████████ |
| Apr 2026 | 17,764 | 58% | 2,534 | 15,029 | ████████████████████ |

The last four complete months averaged 14,440 articles a month against 9,921 in the first four (+46%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 9,165 | 16% |
| India | 3,586 | 6.2% |
| United Kingdom | 2,367 | 4.1% |
| China | 1,304 | 2.3% |
| Australia | 654 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| energy-efficient home solutions | 1,613 | 4.5% | +28% |
| solar photovoltaic (pv) energy systems | 3,125 | 8.8% | +42% |
| green technology innovations | 942 | 2.6% | +64% |
| smart grid integration for renewables | 922 | 2.6% | +60% |
| renewable energy policy & regulation | 851 | 2.4% | +69% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [$100B AI Platform for India Growth: Jeet Adani](https://www.newkerala.com/news/a/we-committed-100-billion-build-platform-that-supports-386.htm) | newkerala.com | 8 | positive |
| 27 Apr 2026 | [Editorial: Grim outlook as Middle East conflict rages on](https://thebftonline.com/2026/04/27/editorial-grim-outlook-as-middle-east-conflict-rages-on/) | thebftonline.com | 8 | negative |
| 27 Apr 2026 | [Multilateral Development Banks’ Clean Electricity Finance](http://www.nrdc.org/resources/multilateral-development-banks-clean-electricity-finance) | nrdc.org | 8 | positive |
| 25 Apr 2026 | [India’s power demand hits record 252.07 GW amid heatwave](https://telanganatoday.com/indias-power-demand-hits-record-252-07-gw-amid-heatwave) ⚠ | telanganatoday.com | 8 | negative |
| 22 Apr 2026 | [Fraud probe launched into £44m eco scheme as arrests made \| TheBusinessDesk.com](https://www.thebusinessdesk.com/westmidlands/news/2110975-fraud-probe-launched-into-44m-eco-scheme-as-arrests-made/) | thebusinessdesk.com | 8 | negative |
| 21 Apr 2026 | [The EU Searches For a Solution to a Jet Fuel Crisis - Impakter](https://impakter.com/the-eu-searches-for-a-solution-to-a-jet-fuel-crisis/) | impakter.com | 8 | negative |
| 20 Apr 2026 | [Centres drafts energy-efficiency roadmap for MSME sector in Andhra Pradesh](https://energy.economictimes.indiatimes.com/news/coal/centres-drafts-energy-efficiency-roadmap-for-msme-sector-in-ap/130383969) | energy.economictimes.indiatimes.com | 8 | positive |
| 20 Apr 2026 | [EU denies bowing to tech lobby on data centre green impact](https://www.thestar.com.my/tech/tech-news/2026/04/20/eu-denies-bowing-to-tech-lobby-on-data-centre-green-impact) | thestar.com.my | 8 | negative |
| 17 Apr 2026 | [India’s artificial intelligence (AI) roadmap should be built on the principles of affordability and…](https://investmentguruindia.com/newsdetail/don-t-just-build-ai-make-it-affordable-energy-efficiency-bureau-official869029) | investmentguruindia.com | 8 | positive |
| 16 Apr 2026 | [Nokia, Orange advance AI‑RAN innovation with NVIDIA - TelecomDrive](https://telecomdrive.com/nokia-orange-advance-ai-ran-innovation-with-nvidia/) | telecomdrive.com | 8 | positive |
| 16 Apr 2026 | [Nokia, Orange Advance AI-RAN Technologies with NVIDIA AI Infrastructure for Spectral Efficiency](http://thefastmode.com/technology-solutions/48104-nokia-orange-advance-ai-ran-technologies-with-nvidia-ai-infrastructure-for-spectral-efficiency) | thefastmode.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "energy efficiency" --since 2026-01-01 --until 2026-04-30
prism-news trends "energy efficiency" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "energy efficiency" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "energy efficiency", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "energy efficiency", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Circular Economy News](circular-economy-news.md)
- [Geothermal News](geothermal-news.md)
