# Artificial Intelligence News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “artificial intelligence news” · 27,100/month India · 74,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [artificial-intelligence-news.json](../../examples/scenarios/artificial-intelligence-news.json).

**Question.** How much artificial intelligence coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="artificial intelligence"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 310,009 |
| Negative · neutral · positive | 22% · 1.2% · 77% |
| Critical (priority 7–9) | 67% (206,474 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (91,378 articles) |
| Most-reported country | United States (20% of matches) |
| Strongest theme by lift | cloud computing technologies |

## Twelve months of coverage

Monthly matching articles for `artificial intelligence` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 42,472 | 61% | 6,982 | 34,956 | █████████ |
| Jun 2025 | 38,492 | 63% | 5,974 | 32,114 | ████████ |
| Jul 2025 | 47,212 | 62% | 8,588 | 38,072 | ██████████ |
| Aug 2025 | 53,494 | 54% | 8,825 | 44,227 | ████████████ |
| Sep 2025 | 50,509 | 66% | 8,879 | 41,079 | ███████████ |
| Oct 2025 | 56,206 | 66% | 9,481 | 46,273 | ████████████ |
| Nov 2025 | 54,145 | 68% | 9,773 | 43,934 | ████████████ |
| Dec 2025 | 52,090 | 67% | 9,261 | 42,332 | ███████████ |
| Jan 2026 | 57,318 | 67% | 10,448 | 46,294 | █████████████ |
| Feb 2026 | 87,487 | 69% | 20,411 | 66,251 | ███████████████████ |
| Mar 2026 | 73,826 | 66% | 16,345 | 56,450 | ████████████████ |
| Apr 2026 | 91,378 | 65% | 19,666 | 70,400 | ████████████████████ |

The last four complete months averaged 77,502 articles a month against 45,418 in the first four (+71%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 40% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 60,771 | 20% |
| India | 14,781 | 4.8% |
| United Kingdom | 6,834 | 2.2% |
| China | 5,880 | 1.9% |
| Australia | 2,921 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| cloud computing technologies | 2,961 | 1.7% | +7% |
| technology adoption and digital transformation | 10,599 | 6.1% | +41% |
| machine learning applications | 2,029 | 1.2% | +111% |
| natural language processing models | 4,148 | 2.4% | +38% |
| digital transformation in industries | 1,938 | 1.1% | +75% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Fortinet warns ransomware victims rise 389% amid AI](https://securitybrief.news/story/fortinet-warns-ransomware-victims-rise-389-amid-ai) | securitybrief.news | 9 | negative |
| 30 Apr 2026 | [OpenAI sued in US by families of Canada school shooting victims](https://www.thestar.com.my/tech/tech-news/2026/04/30/openai-sued-in-us-by-families-of-canada-school-shooting-victims) | thestar.com.my | 9 | negative |
| 29 Apr 2026 | [Affidavit: Rogers man facing CSAM charges used AI to make sexually explicit images of former classmates](https://www.yahoo.com/news/articles/affidavit-rogers-man-facing-csam-200952440.html) | yahoo.com | 9 | negative |
| 29 Apr 2026 | [Families of Canada school shooting victims sue OpenAI over shooter’s use of ChatGPT](https://www.chicoer.com/2026/04/29/canada-school-shooting-victims-families-sue-openai/) | chicoer.com | 9 | negative |
| 29 Apr 2026 | [Families of Canada school shooting victims sue OpenAI over shooter's use of ChatGPT](https://www.wral.com/news/ap/26d63-families-of-canada-school-shooting-victims-sue-openai-over-shooters-use-of-chatgpt/) | wral.com | 9 | negative |
| 29 Apr 2026 | [L'IA se déchaîne sur le tireur présumé du gala de la presse américaine](https://www.journaldemontreal.com/2026/04/29/lia-se-dechaine-sur-le-tireur-presume-du-gala-de-la-presse-americaine) | journaldemontreal.com | 9 | negative |
| 29 Apr 2026 | ["Verbal und physisch" missbraucht: Mutmaßliches Epstein-Opfer aus Österreich](https://kurier.at/chronik/welt/mutmassliches-epstein-opfer-oesterreich-identifiziert/403155073) | kurier.at | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "artificial intelligence" --since 2026-01-01 --until 2026-04-30
prism-news trends "artificial intelligence" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "artificial intelligence" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "artificial intelligence", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "artificial intelligence", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tiktok News](tiktok-news.md)
- [Spacex News](spacex-news.md)
