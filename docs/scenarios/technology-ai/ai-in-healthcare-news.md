# AI in Healthcare News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ai in healthcare news” · 30/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [ai-in-healthcare-news.json](../../examples/scenarios/ai-in-healthcare-news.json).

**Question.** How much ai in healthcare coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="AI in healthcare"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 213 |
| Negative · neutral · positive | 9.4% · 0.0% · 91% |
| Critical (priority 7–9) | 90% (191 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (72 articles) |
| Most-reported country | United States (20% of matches) |
| Strongest theme by lift | telehealth and virtual care platforms |

## Twelve months of coverage

Monthly matching articles for `AI in healthcare` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 40 | 82% | 10 | 30 | ███████████ |
| Jun 2025 | 32 | 94% | 4 | 28 | █████████ |
| Jul 2025 | 37 | 95% | 1 | 36 | ██████████ |
| Aug 2025 | 39 | 92% | 4 | 35 | ███████████ |
| Sep 2025 | 40 | 98% | 4 | 36 | ███████████ |
| Oct 2025 | 34 | 91% | 3 | 31 | █████████ |
| Nov 2025 | 49 | 88% | 3 | 46 | ██████████████ |
| Dec 2025 | 40 | 82% | 1 | 39 | ███████████ |
| Jan 2026 | 43 | 86% | 6 | 37 | ████████████ |
| Feb 2026 | 72 | 93% | 6 | 66 | ████████████████████ |
| Mar 2026 | 47 | 89% | 6 | 41 | █████████████ |
| Apr 2026 | 51 | 88% | 2 | 49 | ██████████████ |

The last four complete months averaged 53 articles a month against 37 in the first four (+44%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 42 | 20% |
| India | 27 | 13% |
| United Kingdom | 12 | 5.6% |
| Colombia | 3 | 1.4% |
| Angola | 2 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| telehealth and virtual care platforms | 21 | 20% | +75% |
| clinical research and trial facilities | 13 | 12% | +86% |
| business intelligence and analytics platforms | 9 | 8.4% | +800% |
| medical imaging and diagnostic centers | 6 | 5.6% | +0% |
| medical billing and coding services | 5 | 4.7% | +150% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown).

No headline could be shown: the matching articles were unavailable from the article store at capture time. Counts above are unaffected.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "AI in healthcare" --since 2026-01-01 --until 2026-04-30
prism-news trends "AI in healthcare" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "AI in healthcare" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "AI in healthcare", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "AI in healthcare", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI Startups News](ai-startups-news.md)
- [Web3 News](web3-news.md)
- [Large Language Model News](large-language-model-news.md)
- [Search Engine News](search-engine-news.md)
