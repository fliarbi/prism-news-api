# Biotech Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “biotech industry” · 1,600/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [biotech-industry.json](../../examples/scenarios/biotech-industry.json).

**Question.** How much news did biotech receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="biotech"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,201 |
| Negative · neutral · positive | 11% · 2.1% · 87% |
| Critical (priority 7–9) | 64% (6,497 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (11,481 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | biotechnology innovations in medicine |

## Twelve months of coverage

Monthly matching articles for `biotech` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,057 | 66% | 306 | 1,703 | ████ |
| Jun 2025 | 1,686 | 68% | 200 | 1,466 | ███ |
| Jul 2025 | 1,816 | 66% | 300 | 1,490 | ███ |
| Aug 2025 | 11,481 | 12% | 374 | 11,079 | ████████████████████ |
| Sep 2025 | 2,433 | 64% | 250 | 2,143 | ████ |
| Oct 2025 | 2,481 | 69% | 222 | 2,235 | ████ |
| Nov 2025 | 2,220 | 70% | 223 | 1,964 | ████ |
| Dec 2025 | 2,274 | 66% | 272 | 1,959 | ████ |
| Jan 2026 | 2,500 | 63% | 183 | 2,275 | ████ |
| Feb 2026 | 2,945 | 64% | 292 | 2,586 | █████ |
| Mar 2026 | 2,195 | 66% | 286 | 1,847 | ████ |
| Apr 2026 | 2,561 | 62% | 316 | 2,187 | ████ |

The last four complete months averaged 2,550 articles a month against 4,260 in the first four (-40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,685 | 26% |
| China | 443 | 4.3% |
| India | 413 | 4.0% |
| United Kingdom | 255 | 2.5% |
| Australia | 205 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| biotechnology innovations in medicine | 713 | 12% | +73% |
| oncology and targeted therapy advancements | 670 | 12% | +20% |
| gene therapy and crispr technologies | 613 | 11% | +31% |
| rare disease therapies and orphan drugs | 507 | 8.8% | +11% |
| drug discovery and development processes | 329 | 5.7% | +92% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Janux Halts EGFR-Targeted T-cell Engager Program](http://www.precisionmedicineonline.com/precision-oncology/janux-halts-egfr-targeted-t-cell-engager-program) | precisionmedicineonline.com | 8 | positive |
| 29 Apr 2026 | [Biotech company patenting world's first AI voice test for substance abuse](https://themarketonline.ca/biotech-company-patenting-worlds-first-ai-voice-test-for-substance-abuse-2026-04-29/) | themarketonline.ca | 8 | positive |
| 29 Apr 2026 | [What will define the winners in a crowded GLP-1 era? - Drug Discovery World (DDW)](https://www.ddw-online.com/what-will-define-the-winners-in-a-crowded-glp-1-era-41438-202604/) | ddw-online.com | 8 | positive |
| 28 Apr 2026 | [A 20-Year Mouse Cloning Experiment Reached a Grim Breaking Point](https://www.yahoo.com/news/articles/20-mouse-cloning-experiment-reached-123200085.html) | yahoo.com | 8 | positive |
| 24 Apr 2026 | [IPO Pipeline Thaws in 2026: Cerebras AI Chips, Clean Energy Giants X-energy and Fervo Lead Massive Public…](https://beamstart.com/news/the-ipo-pipeline-finally-gets-17770286302730) | beamstart.com | 8 | positive |
| 24 Apr 2026 | [EU privacy regulators adopt a single data-processing lawful basis for clinical trials](https://www.osborneclarke.com/insights/eu-privacy-regulators-adopt-single-data-processing-lawful-basis-clinical-trials) | osborneclarke.com | 8 | positive |
| 22 Apr 2026 | [Aktien von RevMed und BioNTech sinken: Neue Wirkstoffe wecken Hoffnung bei Bauchspeicheldrüsenkrebs](https://www.finanzen.ch/nachrichten/aktien/aktien-von-revmed-und-biontech-sinken-neue-wirkstoffe-wecken-hoffnung-bei-bauchspeicheldruesenkrebs-1036047756) | finanzen.ch | 8 | positive |
| 21 Apr 2026 | [SEC accuses ex-adviser associate of trading biotech tips through relative](https://www.investmentnews.com/regulation-legal-compliance/sec-accuses-ex-adviser-associate-of-trading-biotech-tips-through-relative/266239) | investmentnews.com | 8 | negative |
| 21 Apr 2026 | [Medtronic: During an Altaviva Implant, the Patient Talked About Lunch. That Was the Point](https://www.finanznachrichten.de/nachrichten-2026-04/68255640-medtronic-during-an-altaviva-implant-the-patient-talked-about-lunch-that-was-the-point-200.htm) | finanznachrichten.de | 8 | positive |
| 20 Apr 2026 | [Biotech has become a good news story. Let the sun shine](https://www.biospace.com/drug-development/biotech-has-become-a-good-news-story-let-the-sun-shine) | biospace.com | 8 | positive |
| 17 Apr 2026 | [Kailera makes history with record-breaking $625m IPO - Pharmaceutical Technology](https://www.pharmaceutical-technology.com/news/kailera-therapeutics-625m-biotech-ipo/) | pharmaceutical-technology.com | 8 | positive |
| 17 Apr 2026 | [In Brief This Week: Grace Science, Sophia Genetics, City of Hope, Medera](https://www.precisiononcologynews.com/precision-oncology/brief-week-grace-science-sophia-genetics-city-hope-medera) | precisiononcologynews.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "biotech" --since 2026-01-01 --until 2026-04-30
prism-news trends "biotech" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "biotech" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "biotech", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "biotech", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Mining Industry](mining-industry.md)
- [Paper Industry](paper-industry.md)
- [Trucking Industry](trucking-industry.md)
- [Packaging Industry](packaging-industry.md)
