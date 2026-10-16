# Glass Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “glass industry” · 720/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [glass-industry.json](../../examples/scenarios/glass-industry.json).

**Question.** How much news did the glass industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="glass industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 272 |
| Negative · neutral · positive | 18% · 0.4% · 82% |
| Critical (priority 7–9) | 27% (73 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (111 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | industry trade shows and exhibitions |

## Twelve months of coverage

Monthly matching articles for `glass industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 29 | 38% | 6 | 23 | █████ |
| Jun 2025 | 31 | 42% | 9 | 20 | ██████ |
| Jul 2025 | 29 | 28% | 10 | 18 | █████ |
| Aug 2025 | 23 | 26% | 3 | 20 | ████ |
| Sep 2025 | 30 | 17% | 3 | 26 | █████ |
| Oct 2025 | 35 | 31% | 6 | 29 | ██████ |
| Nov 2025 | 36 | 19% | 5 | 31 | ██████ |
| Dec 2025 | 34 | 29% | 8 | 26 | ██████ |
| Jan 2026 | 42 | 17% | 6 | 36 | ████████ |
| Feb 2026 | 111 | 20% | 8 | 102 | ████████████████████ |
| Mar 2026 | 41 | 37% | 10 | 31 | ███████ |
| Apr 2026 | 78 | 37% | 25 | 53 | ██████████████ |

The last four complete months averaged 68 articles a month against 28 in the first four (+143%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 62% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 71 | 26% |
| China | 17 | 6.2% |
| India | 16 | 5.9% |
| United Kingdom | 14 | 5.2% |
| Italy | 9 | 3.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| industry trade shows and exhibitions | 14 | 12% | +250% |
| intellectual property and patent | 5 | 4.4% | — |
| company expansions and new market entries | 13 | 12% | +333% |
| major contract wins and losses | 18 | 16% | +500% |
| new product launches and innovations | 19 | 17% | +533% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [People's Daily Praises NorthGlass: From Breaking Monopolies to Digital & Green Development](http://www.glassonweb.com/news/peoples-daily-praises-northglass-breaking-monopolies-digital-green-development) | glassonweb.com | 7 | positive |
| 27 Apr 2026 | [Phoenix Award Honors Vitro Executive Roberto Cabrera as 2026 Glass Person of the Year](https://www.usglassmag.com/phoenix-award-honors-vitro-executive-roberto-cabrera-as-2026-glass-person-of-the-year/) | usglassmag.com | 7 | positive |
| 12 Apr 2026 | [A Saint-Gobain se le acaban las excusas para no hacer el horno de Avilés: radiografía del momento actual de…](https://www.lne.es/aviles/2026/04/12/saint-gobain-le-acaban-excusas-129000082.html) | lne.es | 7 | negative |
| 12 Apr 2026 | [Industrial Legacy and Glassmaking: Ecological and Human Health Risk Assessment in Paraćin, Serbia.](https://pubmed.ncbi.nlm.nih.gov/42043147/) | pubmed.ncbi.nlm.nih.gov | 7 | negative |
| 19 Mar 2026 | [गेल ने उद्योग एवं कमर्शियल प्रतिष्ठानों के गैस कोटा में 35 प्रतिशत कटौती](https://www.livehindustan.com/uttar-pradesh/firozabad/story-gas-quota-cut-by-35-for-glass-industry-entrepreneurs-warned-201773941183760.html) | livehindustan.com | 7 | negative |
| 19 Feb 2026 | [Glass Futures joins ResponsibleGlass certification programme](https://www.packagingnews.co.uk/news/environment/compliance/glass-futures-joins-responsibleglass-certification-programme-19-02-2026) | packagingnews.co.uk | 7 | positive |
| 12 Feb 2026 | [TK Lamijet Hybrid Pro: the new era of glass lamination](http://www.glassonweb.com/news/tk-lamijet-hybrid-pro-new-era-glass-lamination) | glassonweb.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "glass industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "glass industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "glass industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "glass industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "glass industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Wine Industry](wine-industry.md)
- [Cocoa Industry](cocoa-industry.md)
- [Medical Device Industry News](medical-device-industry-news.md)
- [Railway Industry](railway-industry.md)
