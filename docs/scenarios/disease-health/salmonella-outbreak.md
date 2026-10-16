# Salmonella Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “salmonella outbreak” · 260/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [salmonella-outbreak.json](../../examples/scenarios/salmonella-outbreak.json).

**Question.** How much salmonella coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="salmonella"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,508 |
| Negative · neutral · positive | 52% · 3.0% · 45% |
| Critical (priority 7–9) | 78% (1,964 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (752 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | antimicrobial stewardship programs |

## Twelve months of coverage

Monthly matching articles for `salmonella` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 556 | 80% | 330 | 212 | ███████████████ |
| Jun 2025 | 422 | 79% | 226 | 183 | ███████████ |
| Jul 2025 | 453 | 67% | 221 | 214 | ████████████ |
| Aug 2025 | 688 | 78% | 456 | 218 | ██████████████████ |
| Sep 2025 | 539 | 78% | 255 | 269 | ██████████████ |
| Oct 2025 | 495 | 80% | 214 | 263 | █████████████ |
| Nov 2025 | 513 | 71% | 221 | 277 | ██████████████ |
| Dec 2025 | 601 | 76% | 244 | 321 | ████████████████ |
| Jan 2026 | 703 | 80% | 306 | 367 | ███████████████████ |
| Feb 2026 | 550 | 82% | 275 | 253 | ███████████████ |
| Mar 2026 | 503 | 74% | 245 | 241 | █████████████ |
| Apr 2026 | 752 | 76% | 462 | 275 | ████████████████████ |

The last four complete months averaged 627 articles a month against 530 in the first four (+18%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 29% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 459 | 18% |
| United Kingdom | 47 | 1.9% |
| India | 38 | 1.5% |
| Canada | 29 | 1.2% |
| China | 27 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| antimicrobial stewardship programs | 228 | 13% | +25% |
| antimicrobial-resistant pathogens | 287 | 16% | +25% |
| product safety and recall notices | 76 | 4.3% | -16% |
| treatment of multidrug-resistant organisms | 153 | 8.7% | +38% |
| food safety regulation compliance | 373 | 21% | +2% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [One dead in German Salmonella outbreak \| Food and Farming \| Before It's News](https://beforeitsnews.com/food-and-farming/2026/04/one-dead-in-german-salmonella-outbreak-2543829.html) | beforeitsnews.com | 9 | negative |
| 30 Apr 2026 | [Salmonella Outbreak Across 13 States Has Been Linked To Backyard Chickens](https://www.yahoo.com/news/articles/salmonella-outbreak-across-13-states-201337475.html) | yahoo.com | 8 | negative |
| 29 Apr 2026 | [Alert after salmonella outbreak leaves 50 sick including a dozen Brits](https://www.thescottishsun.co.uk/health/16206465/salmonella-outbreak-hits-brits-salad-sprouts/) | thescottishsun.co.uk | 8 | negative |
| 28 Apr 2026 | [The CDC Has Identified the Source of the Latest Multistate Salmonella Outbreak](https://www.yahoo.com/news/articles/cdc-identified-source-latest-multistate-200801515.html) | yahoo.com | 8 | negative |
| 28 Apr 2026 | [Backyard poultry linked to salmonella outbreak sickening dozens](https://www.fox5ny.com/news/backyard-poultry-linked-salmonella-outbreak-sickening-dozens) | fox5ny.com | 8 | negative |
| 28 Apr 2026 | [Backyard Chickens Are Spreading Antibiotic-Resistant Salmonella Across the US, CDC Warns](https://gizmodo.com/backyard-chickens-are-spreading-antibiotic-resistant-salmonella-across-the-us-cdc-warns-2000751707) | gizmodo.com | 8 | negative |
| 28 Apr 2026 | [Salmonella outbreak spreads across Europe \| Food and Farming \| Before It's News](https://beforeitsnews.com/food-and-farming/2026/04/salmonella-outbreak-spreads-across-europe-2543897.html) | beforeitsnews.com | 8 | negative |
| 28 Apr 2026 | [Children sick in Danish Salmonella outbreak \| Food and Farming \| Before It's News](https://beforeitsnews.com/food-and-farming/2026/04/children-sick-in-danish-salmonella-outbreak-2543894.html) | beforeitsnews.com | 8 | negative |
| 28 Apr 2026 | [CDC Warns of Antibiotic-Resistant Salmonella in Backyard Flocks - Drugs.com MedNews](https://www.drugs.com/news/cdc-warns-antibiotic-resistant-salmonella-backyard-flocks-129823.html) | drugs.com | 8 | negative |
| 26 Apr 2026 | [Urgent 'do not eat' warnings for Aldi, Tesco and M&S products this week](https://www.dailystar.co.uk/news/latest-news/urgent-do-not-eat-warnings-37071423) | dailystar.co.uk | 8 | negative |
| 23 Apr 2026 | [Cantaloupes recalled nationwide over salmonella fears — what shoppers need to know](https://www.ktvu.com/news/cantaloupes-recalled-nationwide-over-salmonella-fears-what-shoppers-need-know) | ktvu.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "salmonella" --since 2026-01-01 --until 2026-04-30
prism-news trends "salmonella" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "salmonella" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "salmonella", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "salmonella", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [HIV News](hiv-news.md)
- [E Coli Outbreak](e-coli-outbreak.md)
- [Norovirus Outbreak](norovirus-outbreak.md)
- [Tuberculosis Outbreak](tuberculosis-outbreak.md)
