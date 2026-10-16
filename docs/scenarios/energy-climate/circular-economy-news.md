# Circular Economy News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “circular economy news” · 10/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [circular-economy-news.json](../../examples/scenarios/circular-economy-news.json).

**Question.** How did circular economy coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="circular economy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,959 |
| Negative · neutral · positive | 6.1% · 1.1% · 93% |
| Critical (priority 7–9) | 48% (1,891 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,285 articles) |
| Most-reported country | United States (7.5% of matches) |
| Strongest theme by lift | circular economy principles |

## Twelve months of coverage

Monthly matching articles for `circular economy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 635 | 50% | 37 | 592 | ██████████ |
| Jun 2025 | 691 | 56% | 42 | 642 | ███████████ |
| Jul 2025 | 737 | 51% | 39 | 689 | ███████████ |
| Aug 2025 | 565 | 53% | 29 | 532 | █████████ |
| Sep 2025 | 829 | 57% | 51 | 767 | █████████████ |
| Oct 2025 | 886 | 51% | 37 | 842 | ██████████████ |
| Nov 2025 | 913 | 54% | 48 | 860 | ██████████████ |
| Dec 2025 | 724 | 55% | 53 | 661 | ███████████ |
| Jan 2026 | 720 | 53% | 43 | 671 | ███████████ |
| Feb 2026 | 954 | 52% | 68 | 875 | ███████████████ |
| Mar 2026 | 1,000 | 47% | 59 | 929 | ████████████████ |
| Apr 2026 | 1,285 | 43% | 71 | 1,197 | ████████████████████ |

The last four complete months averaged 990 articles a month against 657 in the first four (+51%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 35% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 296 | 7.5% |
| India | 199 | 5.0% |
| United Kingdom | 139 | 3.5% |
| China | 98 | 2.5% |
| Spain | 73 | 1.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| circular economy principles | 517 | 19% | +4% |
| green technology innovations | 143 | 5.2% | +11% |
| recycling and waste reduction initiatives | 131 | 4.8% | +75% |
| composting and organic waste management | 259 | 9.5% | +36% |
| sustainable urban planning initiatives | 123 | 4.5% | -4% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Green economy to drive jobs, entrepreneurship; youth key to sustainable growth: Union MoS Jitendra Singh](https://www.aninews.in/news/business/green-economy-to-drive-jobs-entrepreneurship-youth-key-to-sustainable-growth-union-mos-jitendra-singh20260423181531) | aninews.in | 8 | positive |
| 22 Apr 2026 | [TRA Warning Over Low Compliance with UK Tyre Export Verification Rules](https://www.tyreandrubberrecycling.com/articles/business-news/tra-warning-over-low-compliance-with-uk-tyre-export-verification-rules/) | tyreandrubberrecycling.com | 8 | positive |
| 25 Mar 2026 | [Electrochemical Synthesis of Isolated Fluoride Reagents from PFAS.](https://pubmed.ncbi.nlm.nih.gov/41801112/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 18 Feb 2026 | [Prime Minister of Finland meets Prime Minister Modi](https://orissadiary.com/prime-minister-of-finland-meets-prime-minister-modi/) | orissadiary.com | 8 | positive |
| 26 Jan 2026 | [Circular economy, decent work and government’s duty](https://guardian.ng/opinion/editorial/circular-economy-decent-work-and-governments-duty/) | guardian.ng | 8 | positive |
| 30 Apr 2026 | [Plastic recyclers in tune at Eurovision Song Contest • Recycling International](https://recyclinginternational.com/business/business-news/plastic-recyclers-front-row-at-eurovision-song-contest/63987/) | recyclinginternational.com | 7 | positive |
| 29 Apr 2026 | [Govt rolls out policy brief to boost SMEs in circular economy](https://www.capitalfm.co.ke/business/2026/04/govt-rolls-out-policy-brief-to-boost-smes-in-circular-economy/) | capitalfm.co.ke | 7 | positive |
| 29 Apr 2026 | [Bluealp Chosen as Technology Partner for Biobtx Project in Netherlands](https://www.process-worldwide.com/bluealp-chosen-as-technology-partner-for-biobtx-project-in-netherlands-a-0cea8b5e0bb484e5e3c3bd285b69bb16/) | process-worldwide.com | 7 | positive |
| 28 Apr 2026 | [Inorganic Photoluminescent Microparticles as Identifiers for the Sorting of Lithium-Ion Battery Cathodes.](https://pubmed.ncbi.nlm.nih.gov/41999232/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 28 Apr 2026 | [Electrochemical Lithium-Ion Recovery from Battery Recycling Process Water.](https://pubmed.ncbi.nlm.nih.gov/42036109/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 27 Apr 2026 | [Pacto Português para os Plásticos define metas para 2030 e reforça ambição para a economia circular](https://jornaleconomico.sapo.pt/noticias/pacto-portugues-para-os-plasticos-define-metas-para-2030-e-reforca-ambicao-para-a-economia-circular/) | jornaleconomico.sapo.pt | 7 | positive |
| 24 Apr 2026 | [Govt working to finalise National Circular Textile Strategy by year-end](https://www.tbsnews.net/economy/rmg/govt-working-finalise-national-circular-textile-strategy-year-end-1420491) | tbsnews.net | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "circular economy" --since 2026-01-01 --until 2026-04-30
prism-news trends "circular economy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "circular economy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "circular economy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "circular economy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Drought News](drought-news.md)
- [Glacier News](glacier-news.md)
- [Geothermal News](geothermal-news.md)
- [Energy Efficiency Industry](energy-efficiency-industry.md)
