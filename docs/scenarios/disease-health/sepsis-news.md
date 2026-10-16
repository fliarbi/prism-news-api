# Sepsis News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sepsis news” · 70/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [sepsis-news.json](../../examples/scenarios/sepsis-news.json).

**Question.** How much sepsis coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="sepsis"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,149 |
| Negative · neutral · positive | 26% · 5.0% · 69% |
| Critical (priority 7–9) | 92% (2,894 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,161 articles) |
| Most-reported country | United States (6.0% of matches) |
| Strongest theme by lift | infectious disease research and prevention |

## Twelve months of coverage

Monthly matching articles for `sepsis` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 571 | 87% | 162 | 369 | ██████████ |
| Jun 2025 | 484 | 92% | 130 | 319 | ████████ |
| Jul 2025 | 565 | 90% | 160 | 368 | ██████████ |
| Aug 2025 | 625 | 92% | 168 | 416 | ███████████ |
| Sep 2025 | 809 | 92% | 286 | 485 | ██████████████ |
| Oct 2025 | 636 | 90% | 183 | 413 | ███████████ |
| Nov 2025 | 596 | 94% | 126 | 432 | ██████████ |
| Dec 2025 | 756 | 93% | 156 | 556 | █████████████ |
| Jan 2026 | 1,161 | 95% | 187 | 894 | ████████████████████ |
| Feb 2026 | 617 | 89% | 172 | 410 | ███████████ |
| Mar 2026 | 719 | 92% | 260 | 430 | ████████████ |
| Apr 2026 | 652 | 89% | 187 | 436 | ███████████ |

The last four complete months averaged 787 articles a month against 561 in the first four (+40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 15% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 189 | 6.0% |
| United Kingdom | 111 | 3.5% |
| China | 23 | 0.7% |
| India | 22 | 0.7% |
| Canada | 16 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| infectious disease research and prevention | 305 | 15% | +52% |
| antimicrobial stewardship programs | 179 | 8.9% | +4% |
| patient safety and quality improvement studies | 172 | 8.6% | +20% |
| biomedical research grant proposals | 140 | 7.0% | +164% |
| diagnosis of atypical pathogens | 133 | 6.6% | +46% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 8 Apr 2026 | [Scots oil worker dies in Australia after message of support from Celtic fans](https://www.thescottishsun.co.uk/news/16130082/scots-oil-worker-dies-infection-australia-celtic-fans-support/) | thescottishsun.co.uk | 9 | negative |
| 26 Mar 2026 | [Kristen Johnston Slams Perez Hilton for Past Remarks About Her Weight During ‘Darkest Time’ of Her Life](https://www.yahoo.com/entertainment/celebrity/articles/kristen-johnston-slams-perez-hilton-034451130.html) | yahoo.com | 9 | negative |
| 19 Mar 2026 | [Lancaster University student’s death by sepsis linked to hospital's 'inadequate' hygiene](https://thetab.com/2026/03/19/lancaster-university-students-death-by-sepsis-linked-to-hospitals-inadequate-hygiene) | thetab.com | 9 | negative |
| 11 Feb 2026 | [‘It started as a UTI’: British traveller’s close call after infection turns to sepsis](https://www.nzherald.co.nz/lifestyle/sepsis-from-uti-how-a-common-infection-became-life-threatening-for-rosie-beveridge/MCGFL5VOWNACPHVJOQU3XEKUYQ/) | nzherald.co.nz | 9 | negative |
| 7 Jan 2026 | [I gave birth but all went black after I vomited blood - I ended up in a coma](https://www.thescottishsun.co.uk/fabulous/15772753/breastfed-baby-nearly-died-lucky-alive/) | thescottishsun.co.uk | 9 | negative |
| 29 Apr 2026 | [Volition Reports Successful Finger-Prick Detection of Nucleosomes for Sepsis Testing](https://clpmag.com/diagnostic-technologies/immunoassay/immunoassay-reagents-kits/volition-finger-prick-nucleosome-test-sepsis-detection/) | clpmag.com | 8 | positive |
| 28 Apr 2026 | [The role of astrocytic GSDME in Sepsis-associated cognitive dysfunction.](https://pubmed.ncbi.nlm.nih.gov/42055495/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 23 Apr 2026 | [My botched boob job has cost taxpayers thousands - I needed 3 NHS ops to fix it](https://www.thescottishsun.co.uk/fabulous/16186160/botched-turkey-boob-job-cost-taxpayers-thousands/) | thescottishsun.co.uk | 8 | negative |
| 22 Apr 2026 | [A Deep Dive Into Artificial Intelligence Naics Code](https://www.thedetroitbureau.com/www-news/a-deep-dive-into-artificial-intelligence-naics-code-dhzd8bwjbg99) | thedetroitbureau.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "sepsis" --since 2026-01-01 --until 2026-04-30
prism-news trends "sepsis" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "sepsis" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "sepsis", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "sepsis", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Clinical Trial News](clinical-trial-news.md)
- [Depression News](depression-news.md)
- [Dengue News](dengue-news.md)
- [Candida Auris Outbreak](candida-auris-outbreak.md)
