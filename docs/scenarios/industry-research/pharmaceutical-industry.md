# Pharmaceutical Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pharmaceutical industry” · 14,800/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [pharmaceutical-industry.json](../../examples/scenarios/pharmaceutical-industry.json).

**Question.** How much news did the pharmaceutical industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="pharmaceutical industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 7,736 |
| Negative · neutral · positive | 20% · 1.9% · 78% |
| Critical (priority 7–9) | 62% (4,766 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (2,644 articles) |
| Most-reported country | United States (23% of matches) |
| Strongest theme by lift | pharmaceutical manufacturing techniques |

## Twelve months of coverage

Monthly matching articles for `pharmaceutical industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,605 | 65% | 468 | 1,097 | ████████████ |
| Jun 2025 | 877 | 62% | 184 | 674 | ███████ |
| Jul 2025 | 1,225 | 64% | 368 | 831 | █████████ |
| Aug 2025 | 1,101 | 64% | 362 | 720 | ████████ |
| Sep 2025 | 1,510 | 70% | 452 | 1,029 | ███████████ |
| Oct 2025 | 1,535 | 69% | 446 | 1,074 | ████████████ |
| Nov 2025 | 1,511 | 57% | 254 | 1,240 | ███████████ |
| Dec 2025 | 1,404 | 64% | 269 | 1,102 | ███████████ |
| Jan 2026 | 1,505 | 63% | 237 | 1,248 | ███████████ |
| Feb 2026 | 2,644 | 60% | 483 | 2,112 | ████████████████████ |
| Mar 2026 | 1,692 | 64% | 387 | 1,275 | █████████████ |
| Apr 2026 | 1,895 | 62% | 434 | 1,415 | ██████████████ |

The last four complete months averaged 1,934 articles a month against 1,202 in the first four (+61%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 43% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,744 | 23% |
| India | 447 | 5.8% |
| United Kingdom | 203 | 2.6% |
| China | 154 | 2.0% |
| Germany | 84 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| pharmaceutical manufacturing techniques | 579 | 13% | +110% |
| quality control in pharmaceutical manufacturing | 480 | 11% | +92% |
| regulatory compliance (fda, ema, etc.) | 466 | 11% | +122% |
| pharmaceutical supply chain management | 727 | 17% | +54% |
| drug pricing and reimbursement strategies | 770 | 18% | -13% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [TrumpRx reshapes US drug pricing](https://xconomy.com/pricing-and-contracting/trump-administration-reshapes-drug-pricing-with-mfn-and-trumprx) | xconomy.com | 8 | positive |
| 21 Apr 2026 | [Pharma: Astra Zeneca droht mit Stopp neuer Medikamente in Deutschland](http://www.handelsblatt.com/unternehmen/industrie/pharma-astra-zeneca-droht-mit-stopp-neuer-medikamente-in-deutschland/100216722.html) | handelsblatt.com | 8 | positive |
| 21 Apr 2026 | [Bioengineered In Vitro 3D Cancer Models: A New Paradigm in Ethical and Predictive Oncology Research Toward…](https://pubmed.ncbi.nlm.nih.gov/42011630/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 16 Apr 2026 | [Novartis CEO Vas Narasimhan Joins Anthropic Board of Directors](https://n24.com.tr/en/business/novartis-ceo-vas-narasimhan-joins-anthropic-board-of-directors) | n24.com.tr | 8 | positive |
| 14 Apr 2026 | [`Indian pharma must balance generics with innovation' - The Times of India](https://timesofindia.indiatimes.com/business/india-business/indian-pharma-must-balance-generics-with-innovation/articleshow/130265993.cms) | timesofindia.indiatimes.com | 8 | positive |
| 14 Apr 2026 | [Pharma sector must 'leapfrog' into innovation phase to meet 2047 goals: Pharmexcil Chairman](https://www.aninews.in/news/business/pharma-sector-must-leapfrog-into-innovation-phase-to-meet-2047-goals-pharmexcil-chairman20260414083512) | aninews.in | 8 | positive |
| 11 Apr 2026 | [Nueve heridos en el incendio de una farmacéutica en Mollet: activado el plan químico](https://cronicaglobal.elespanol.com/vida/20260411/heridos-incendio-farmaceutica-barcelona-activado-plan-quimico/1003742750452_0.html) | cronicaglobal.elespanol.com | 8 | negative |
| 10 Apr 2026 | [Ireland’s EU presidency an ‘opportunity’ to safeguard pharma’s future, says industry group](https://www.irishtimes.com/business/2026/04/10/irelands-eu-presidency-an-opportunity-to-safeguard-pharmas-future-says-industry-group/) | irishtimes.com | 8 | negative |
| 10 Apr 2026 | [As the War in Iran persists, the pharmaceutical industry sees major delays with medications](https://www.klkntv.com/as-the-war-in-iran-persists-the-pharmaceutical-industry-sees-major-delays-with-medications/) | klkntv.com | 8 | negative |
| 9 Apr 2026 | [Iran conflict: Pharma supply chains may take months to recover](https://economictimes.indiatimes.com/industry/healthcare/biotech/pharmaceuticals/iran-conflict-pharma-supply-chains-may-take-months-to-recover/articleshow/130152316.cms) | economictimes.indiatimes.com | 8 | negative |
| 9 Apr 2026 | [Pharmalittle: We're reading about top pharma lobbyist stepping down, genes and GLP-1 drugs, and more](https://www.statnews.com/pharmalot/2026/04/09/pharma-top-lobbyist-step-down-genes-glp1-abbvie-340b/) | statnews.com | 8 | positive |
| 8 Apr 2026 | [Trump has battled the drug industry. Now its top lobbyist is leaving.](https://www.yahoo.com/news/sectors/healthcare/articles/washingtons-most-powerful-drug-industry-lobbyist-is-stepping-down-173558501.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "pharmaceutical industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "pharmaceutical industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "pharmaceutical industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "pharmaceutical industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "pharmaceutical industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Textile Industry](textile-industry.md)
- [Food Processing Industry](food-processing-industry.md)
- [Restaurant Industry](restaurant-industry.md)
- [Semiconductor Industry News](semiconductor-industry-news.md)
