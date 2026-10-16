# Cosmetics Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cosmetics industry” · 880/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cosmetics-industry.json](../../examples/scenarios/cosmetics-industry.json).

**Question.** How much news did the cosmetics industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="cosmetics industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 323 |
| Negative · neutral · positive | 8.4% · 5.9% · 86% |
| Critical (priority 7–9) | 24% (79 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (117 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | mergers and acquisitions in the chemical sector |

## Twelve months of coverage

Monthly matching articles for `cosmetics industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 73 | 22% | 7 | 63 | ████████████ |
| Jun 2025 | 44 | 46% | 2 | 42 | ████████ |
| Jul 2025 | 76 | 22% | 9 | 65 | █████████████ |
| Aug 2025 | 38 | 34% | 4 | 33 | ██████ |
| Sep 2025 | 52 | 38% | 2 | 50 | █████████ |
| Oct 2025 | 52 | 33% | 4 | 44 | █████████ |
| Nov 2025 | 77 | 38% | 11 | 64 | █████████████ |
| Dec 2025 | 56 | 27% | 5 | 49 | ██████████ |
| Jan 2026 | 47 | 36% | 4 | 41 | ████████ |
| Feb 2026 | 67 | 33% | 5 | 60 | ███████████ |
| Mar 2026 | 92 | 17% | 4 | 73 | ████████████████ |
| Apr 2026 | 117 | 20% | 14 | 103 | ████████████████████ |

The last four complete months averaged 81 articles a month against 58 in the first four (+40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 68 | 21% |
| India | 10 | 3.1% |
| China | 7 | 2.2% |
| United Kingdom | 7 | 2.2% |
| France | 5 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mergers and acquisitions in the chemical sector | 20 | 11% | +1900% |
| global chemical market trends and analysis | 21 | 12% | +2000% |
| industry-specific business trends | 10 | 5.6% | +400% |
| cosmetic ingredients and safety standards | 7 | 3.9% | +0% |
| quality control in pharmaceutical manufacturing | 7 | 3.9% | +40% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 5 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Polizei-News Regensburg, 30.04.26: Nägel schwarz lackiert - Wiederholte Schwarzarbeit in Nagelstudios endet…](https://www.news.de/lokales/859570444/blaulicht-news-polizei-news-regensburg-30-04-26-verkehrsunfall-in-regensburg-heute/1/) | news.de | 7 | negative |
| 1 Jan 2026 | [Bridging digital tools and human skills: A sustainable competence framework for implementing digital product…](https://pubmed.ncbi.nlm.nih.gov/41401607/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 16 Apr 2026 | [BRIN targets strategic research to boost Indonesia's cosmetic industry](https://en.antaranews.com/news/412595/brin-targets-strategic-research-to-boost-indonesias-cosmetic-industry) | en.antaranews.com | 6 | positive |
| 12 Apr 2026 | [Federal Food Drug and Cosmetic Act (FFDCA), Manufacturing Facilities, Modernization of Cosmetics Regulation…](https://www.jdsupra.com/topics/federal-food-drug-and-cosmetic-act-ffdca/manufacturing-facilities/modernization-of-cosmetics-regulation-act-of-2022-mocra/) | jdsupra.com | 6 | positive |
| 10 Apr 2026 | [Federal Food Drug and Cosmetic Act (FFDCA), Regulatory Authority, Modernization of Cosmetics Regulation Act…](https://www.jdsupra.com/topics/federal-food-drug-and-cosmetic-act-ffdca/regulatory-authority/modernization-of-cosmetics-regulation-act-of-2022-mocra/) | jdsupra.com | 6 | positive |
| 6 Apr 2026 | [Sauberes Wasser: Carsten Schneider will die Industrie zur Kasse bitten](https://www.braunschweiger-zeitung.de/politik/article411636501/sauberes-wasser-schneider-will-die-industrie-zur-kasse-bitten.html) | braunschweiger-zeitung.de | 6 | positive |
| 11 Feb 2026 | [Vytrus Biotech aumenta un 66% sus ventas y duplica su Ebitda en 2025](https://www.alimarket.es/nonfood/noticia/421359/vytrus-biotech-aumenta-un-66--sus-ventas-y-duplica-su-ebitda-en-2025) | alimarket.es | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cosmetics industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "cosmetics industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cosmetics industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cosmetics industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cosmetics industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Hotel Industry](hotel-industry.md)
- [Tourism Industry](tourism-industry.md)
- [Mining Industry](mining-industry.md)
- [Paper Industry](paper-industry.md)
