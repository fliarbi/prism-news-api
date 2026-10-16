# Steel Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “steel industry” · 3,600/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [steel-industry.json](../../examples/scenarios/steel-industry.json).

**Question.** How much news did the steel industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="steel industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 749 |
| Negative · neutral · positive | 41% · 4.4% · 54% |
| Critical (priority 7–9) | 62% (466 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (250 articles) |
| Most-reported country | India (11% of matches) |
| Strongest theme by lift | metal export-import regulations |

## Twelve months of coverage

Monthly matching articles for `steel industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 250 | 75% | 139 | 91 | ████████████████████ |
| Jun 2025 | 228 | 79% | 141 | 81 | ██████████████████ |
| Jul 2025 | 152 | 58% | 75 | 73 | ████████████ |
| Aug 2025 | 143 | 61% | 58 | 82 | ███████████ |
| Sep 2025 | 168 | 63% | 75 | 85 | █████████████ |
| Oct 2025 | 214 | 68% | 95 | 117 | █████████████████ |
| Nov 2025 | 203 | 59% | 85 | 105 | ████████████████ |
| Dec 2025 | 123 | 61% | 39 | 78 | ██████████ |
| Jan 2026 | 132 | 69% | 69 | 60 | ███████████ |
| Feb 2026 | 177 | 62% | 62 | 103 | ██████████████ |
| Mar 2026 | 192 | 59% | 90 | 90 | ███████████████ |
| Apr 2026 | 248 | 62% | 87 | 155 | ████████████████████ |

The last four complete months averaged 187 articles a month against 193 in the first four (-3%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 81 | 11% |
| United States | 69 | 9.2% |
| China | 29 | 3.9% |
| United Kingdom | 18 | 2.4% |
| Indonesia | 7 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| metal export-import regulations | 78 | 18% | -15% |
| industrial metal market analysis | 79 | 18% | +5% |
| metal commodity trading trends | 47 | 11% | +12% |
| metal fabrication and industrial applications | 70 | 16% | +6% |
| base metal smelting and casting | 19 | 4.4% | +46% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Deepfake-Deckung: Stoïk erweitert Cyber-Versicherung](https://www.it-finanzmagazin.de/deepfake-deckung-stoik-erweitert-cyber-versicherung-243109/) | it-finanzmagazin.de | 8 | neutral |
| 14 Apr 2026 | [EU agrees to double tariffs to halve steel imports](https://www.dailysabah.com/business/economy/eu-agrees-to-double-tariffs-to-halve-steel-imports) | dailysabah.com | 8 | negative |
| 20 Mar 2026 | [UK steel industry backed by new government strategy - The Metal Packager](https://metalpackager.com/2026/03/uk-steel-industry-government-strategy/) | metalpackager.com | 8 | positive |
| 17 Feb 2026 | [Ministry Of Steel Invites AI Startups For Steel Industry Innovation - Sahyadri Startups](https://sahyadristartups.com/news/ministry-of-steel-invites-ai-startups-for-steel-industry-innovation/) | sahyadristartups.com | 8 | positive |
| 30 Jan 2026 | [2026 Circular Steel Summit: Taking stock of tariffs](https://www.recyclingtoday.com/news/2026-circular-steel-summit-taking-stock-of-tariffs/) | recyclingtoday.com | 8 | negative |
| 14 Apr 2026 | [Nigeria seals $1bn steel deal with Indian firm as FDI hits $2.2bn - Businessday NG](https://businessday.ng/news/article/nigeria-seals-1bn-steel-deal-with-indian-firm/) | businessday.ng | 7 | positive |
| 14 Apr 2026 | [EU einigt sich auf schärfere Regeln für Stahlimporte](https://www.wort.lu/wirtschaft/eu-einigt-sich-auf-schaerfere-regeln-fuer-stahlimporte/145749036.html) | wort.lu | 7 | negative |
| 14 Apr 2026 | [EU verschärft Einfuhrregeln für Stahlimporte](https://www.sueddeutsche.de/politik/eu-stahlimporte-zoelle-usa-china-indien-stahlindustrie-li.3467577) | sueddeutsche.de | 7 | negative |
| 13 Apr 2026 | [Industrie: EU einigt sich auf schärfere Regeln für Stahlimporte](https://www.news.de/wirtschaft/859518142/eu-einigt-sich-auf-schaerfere-regeln-fuer-stahlimporte-industrie-news-der-dpa-aktuell-zu-industrie-handel-und-eu/1/) | news.de | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "steel industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "steel industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "steel industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "steel industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "steel industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Retail Industry News](retail-industry-news.md)
- [FMCG Industry](fmcg-industry.md)
- [Chemical Industry](chemical-industry.md)
- [Music Industry](music-industry.md)
