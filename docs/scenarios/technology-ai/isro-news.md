# ISRO News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “isro news” · 5,400/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [isro-news.json](../../examples/scenarios/isro-news.json).

**Question.** How much isro coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="ISRO"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,923 |
| Negative · neutral · positive | 17% · 1.3% · 81% |
| Critical (priority 7–9) | 79% (1,526 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (1,346 articles) |
| Most-reported country | India (47% of matches) |
| Strongest theme by lift | rocket engine development |

## Twelve months of coverage

Monthly matching articles for `ISRO` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 598 | 76% | 120 | 468 | █████████ |
| Jun 2025 | 952 | 77% | 160 | 769 | ██████████████ |
| Jul 2025 | 1,044 | 71% | 83 | 951 | ████████████████ |
| Aug 2025 | 1,346 | 76% | 176 | 1,140 | ████████████████████ |
| Sep 2025 | 684 | 78% | 86 | 586 | ██████████ |
| Oct 2025 | 432 | 74% | 31 | 395 | ██████ |
| Nov 2025 | 710 | 79% | 34 | 671 | ███████████ |
| Dec 2025 | 584 | 83% | 53 | 526 | █████████ |
| Jan 2026 | 675 | 80% | 124 | 541 | ██████████ |
| Feb 2026 | 457 | 84% | 99 | 354 | ███████ |
| Mar 2026 | 311 | 75% | 54 | 252 | █████ |
| Apr 2026 | 480 | 76% | 58 | 412 | ███████ |

The last four complete months averaged 481 articles a month against 985 in the first four (-51%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 66% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 912 | 47% |
| United States | 234 | 12% |
| United Kingdom | 18 | 0.9% |
| China | 13 | 0.7% |
| Japan | 11 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| rocket engine development | 68 | 6.7% | -17% |
| cubesat and small satellite innovations | 59 | 5.8% | +168% |
| space launch infrastructure development | 89 | 8.7% | -32% |
| satellite communication technologies | 102 | 10% | -40% |
| space suit technology evolution | 81 | 8.0% | +146% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Mar 2026 | [Melting Glaciers Greater Threat](https://www.insightsonindia.com/2026/03/16/melting-glaciers-greater-threat/) | insightsonindia.com | 9 | negative |
| 30 Apr 2026 | [NISAR Satellite Data Shows Mexico City Sinking at Rapid Pace - INDIA New England News](https://indianewengland.com/nisar-satellite-data-shows-mexico-city-sinking-at-rapid-pace/) | indianewengland.com | 8 | negative |
| 30 Apr 2026 | ['State Must Be Model Employer' : Supreme Court Criticises Union For Not Regularising ISRO Workers Despite…](https://www.livelaw.in/supreme-court/state-must-be-model-employer-supreme-court-criticises-union-for-not-regularising-isro-workers-despite-earlier-directions-532338) | livelaw.in | 8 | negative |
| 30 Apr 2026 | [From bicycle to Moon: Flaying authorities, Supreme Court orders regularisation of ISRO workers behind…](https://indianexpress.com/article/legal-news/supreme-court-isro-daily-wage-workers-regularisation-bicycle-10663485/) | indianexpress.com | 8 | negative |
| 30 Apr 2026 | [Joint India-US venture NISAR shows Mexico City sinking at alarming pace - Mangalorean.com](https://www.mangalorean.com/joint-india-us-venture-nisar-shows-mexico-city-sinking-at-alarming-pace/) | mangalorean.com | 8 | negative |
| 29 Apr 2026 | [India explores large-scale 3D printing for space manufacturing](https://www.domain-b.com/technology/engineering/isro-3d-printing-space-manufacturing-2026) | domain-b.com | 8 | positive |
| 29 Apr 2026 | [Civilians next as Gaganyaan astronauts: Inside details of Isro’s big plan](https://www.indiatoday.in/science/story/isro-gaganyaan-second-astronaut-batch-selection-civilians-iaf-test-pilots-stem-2903122-2026-04-29) | indiatoday.in | 8 | positive |
| 27 Apr 2026 | [Optimized Electrotech Raises Rs.35 Crore for Space Imaging](https://www.newkerala.com/news/a/optimized-electrotech-raises-rs35-crore-round-led-exfinity-984.htm) | newkerala.com | 8 | positive |
| 24 Apr 2026 | [Space Infrastructure for National Security: Shukla](https://www.newkerala.com/news/a/need-create-space-infrastructure-national-security-iaf-group-399.htm) | newkerala.com | 8 | positive |
| 23 Apr 2026 | [Pune: Man Posing As ISRO Scientist Dupes Woman Of ₹26 Lakh; 11 Similar Cases Against Him In Mumbai & Navi…](https://www.freepressjournal.in/pune/pune-man-posing-as-isro-scientist-dupes-woman-of-26-lakh-11-similar-cases-against-him-in-mumbai-navi-mumbai) | freepressjournal.in | 8 | negative |
| 22 Apr 2026 | [Pune: Man Pose as ISRO Scientist on Matrimony Portal to Cheat Woman of Rs 26.5 Lakh, Arrested - Punekar News](https://www.punekarnews.in/pune-man-pose-as-isro-scientist-on-matrimony-portal-to-cheat-woman-of-rs-26-5-lakh-arrested/) | punekarnews.in | 8 | negative |
| 20 Apr 2026 | [ISRO, TIFR sign MoU for collaboration in space science, tech, exploration](https://english.varthabharati.in/science/isro-tifr-sign-mou-for-collaboration-in-space-science-tech-exploration) | english.varthabharati.in | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ISRO" --since 2026-01-01 --until 2026-04-30
prism-news trends "ISRO" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ISRO" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ISRO", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ISRO", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Iphone News](iphone-news.md)
- [Data Center News](data-center-news.md)
- [Online Gaming News](online-gaming-news.md)
- [Social Media News](social-media-news.md)
