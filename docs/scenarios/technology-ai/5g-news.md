# 5G News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “5g news” · 140/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [5g-news.json](../../examples/scenarios/5g-news.json).

**Question.** How much 5g coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="5G"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,258 |
| Negative · neutral · positive | 4.8% · 1.5% · 94% |
| Critical (priority 7–9) | 46% (5,697 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (4,374 articles) |
| Most-reported country | India (14% of matches) |
| Strongest theme by lift | mobile phone battery performance |

## Twelve months of coverage

Monthly matching articles for `5G` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,445 | 40% | 141 | 1,987 | ███████████ |
| Jun 2025 | 2,350 | 50% | 137 | 2,176 | ███████████ |
| Jul 2025 | 2,824 | 41% | 220 | 2,540 | █████████████ |
| Aug 2025 | 4,374 | 40% | 340 | 3,477 | ████████████████████ |
| Sep 2025 | 3,042 | 45% | 145 | 2,862 | ██████████████ |
| Oct 2025 | 2,572 | 55% | 127 | 2,433 | ████████████ |
| Nov 2025 | 2,532 | 53% | 141 | 2,365 | ████████████ |
| Dec 2025 | 3,420 | 32% | 105 | 2,305 | ████████████████ |
| Jan 2026 | 2,345 | 44% | 154 | 2,116 | ███████████ |
| Feb 2026 | 3,101 | 49% | 142 | 2,915 | ██████████████ |
| Mar 2026 | 3,573 | 50% | 145 | 3,402 | ████████████████ |
| Apr 2026 | 3,239 | 42% | 151 | 3,046 | ███████████████ |

The last four complete months averaged 3,064 articles a month against 2,998 in the first four (+2%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 1,772 | 14% |
| United States | 1,382 | 11% |
| China | 298 | 2.4% |
| South Korea | 244 | 2.0% |
| United Kingdom | 207 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone battery performance | 1,116 | 15% | -17% |
| mobile phone connectivity standards (5g, lte) | 1,003 | 14% | +57% |
| mobile phone hardware components | 995 | 14% | -8% |
| 5g network infrastructure | 1,209 | 16% | +20% |
| mobile phone storage solutions | 583 | 8.0% | -50% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Orange weighs Nvidia against Intel for 5G chips ahead of new RFP](https://lightreading.com/5g/orange-weighs-nvidia-against-intel-for-5g-chips-ahead-of-new-rfp) | lightreading.com | 8 | negative |
| 28 Apr 2026 | [Google to build $15 billion, 1 GW AI data centre in Andhra Pradesh; state targets 6.5 GW digital capacity](https://www.fortuneindia.com/technology/google-to-build-15-billion-1-gw-ai-data-centre-in-andhra-pradesh-state-targets-65-gw-digital-capacity/134657) ⚠ | fortuneindia.com | 8 | positive |
| 27 Apr 2026 | [Forex, domestic declines weigh on ZTE](https://www.mobileworldlive.com/ranvendors/forex-domestic-declines-weigh-on-zte/) ⚠ | mobileworldlive.com | 8 | positive |
| 25 Apr 2026 | [AI & 5G: Experts Call for Secure Digital Ecosystem](https://www.newkerala.com/news/a/experts-call-secure-resilient-ai-driven-digital-ecosystem-493.htm) | newkerala.com | 8 | positive |
| 25 Apr 2026 | [Sekhar Pemmasani Calls for Deeper Industry Role to Shape 6G Future - TelecomDrive](https://telecomdrive.com/sekhar-pemmasani-calls-for-deeper-industry-role-to-shape-6g-future/) | telecomdrive.com | 8 | positive |
| 24 Apr 2026 | [Reliance Jio clocks strong FY26 with Rs 30,053 crore profit; IPL tailwinds to aid growth momentum](https://storyboard18.com/digital/reliance-jio-q4-profit-up-13-percent-on-5g-and-arpu-growth-ws-l-96168.htm) | storyboard18.com | 8 | positive |
| 24 Apr 2026 | [Building India’s Digital Triangle: The Backbone of a 5G, IoT, and AI-Ready Economy](https://cxotoday.com/expert-opinion/building-indias-digital-triangle-the-backbone-of-a-5g-iot-and-ai-ready-economy/) | cxotoday.com | 8 | positive |
| 24 Apr 2026 | [MoS calls for Design-led Innovation and Deeper Industry Role to Shape 6G Future](https://timestech.in/mos-calls-for-design-led-innovation-and-deeper-industry-role-to-shape-6g-future/) | timestech.in | 8 | positive |
| 24 Apr 2026 | [Zero Trust in India's public sector: why it matters now](https://techobserver.in/news/opinion/zero-trust-india-public-sector-technology-backbone-323393/) | techobserver.in | 8 | positive |
| 24 Apr 2026 | [MoS Chandra Sekhar Pemmasani calls for Design-led Innovation and Deeper Industry Role to Shape 6G Future](https://cxotoday.com/media-coverage/mos-chandra-sekhar-pemmasani-calls-for-design-led-innovation-and-deeper-industry-role-to-shape-6g-future/) | cxotoday.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "5G" --since 2026-01-01 --until 2026-04-30
prism-news trends "5G" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "5G" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "5G", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "5G", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Large Language Model News](large-language-model-news.md)
- [Search Engine News](search-engine-news.md)
- [Digital Identity News](digital-identity-news.md)
