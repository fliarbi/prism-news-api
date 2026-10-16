# Hypertension News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hypertension news” · 30/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [hypertension-news.json](../../examples/scenarios/hypertension-news.json).

**Question.** How much hypertension coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="hypertension"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,532 |
| Negative · neutral · positive | 28% · 6.8% · 65% |
| Critical (priority 7–9) | 86% (5,640 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (2,174 articles) |
| Most-reported country | United States (6.8% of matches) |
| Strongest theme by lift | hypertensive heart disease complications |

## Twelve months of coverage

Monthly matching articles for `hypertension` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,569 | 79% | 480 | 989 | ██████████████ |
| Jun 2025 | 1,419 | 78% | 370 | 944 | █████████████ |
| Jul 2025 | 1,523 | 78% | 384 | 1,001 | ██████████████ |
| Aug 2025 | 1,529 | 82% | 390 | 1,049 | ██████████████ |
| Sep 2025 | 1,927 | 77% | 461 | 1,376 | ██████████████████ |
| Oct 2025 | 1,909 | 79% | 388 | 1,409 | ██████████████████ |
| Nov 2025 | 1,477 | 88% | 372 | 1,006 | ██████████████ |
| Dec 2025 | 1,851 | 87% | 466 | 1,258 | █████████████████ |
| Jan 2026 | 2,174 | 91% | 505 | 1,471 | ████████████████████ |
| Feb 2026 | 1,363 | 81% | 400 | 876 | █████████████ |
| Mar 2026 | 1,392 | 86% | 391 | 909 | █████████████ |
| Apr 2026 | 1,603 | 85% | 523 | 1,002 | ███████████████ |

The last four complete months averaged 1,633 articles a month against 1,510 in the first four (+8%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 16% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 445 | 6.8% |
| India | 198 | 3.0% |
| China | 65 | 1.0% |
| United Kingdom | 54 | 0.8% |
| Nigeria | 27 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| hypertensive heart disease complications | 509 | 13% | -13% |
| hypertensive crisis management | 465 | 12% | -25% |
| hypertensive emergency protocols | 407 | 10% | -22% |
| geriatric hypertension management strategies | 396 | 10% | -12% |
| public health initiatives and programs | 357 | 9.2% | +12% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Is your blood pressure 'healthy'? Why it's critical to know your number](https://www.floridatoday.com/story/news/healthcare/2026/04/21/what-is-considered-healthy-blood-pressure-number-american-heart-association/89700538007/) | floridatoday.com | 9 | negative |
| 14 Apr 2026 | [Man dies after overdose of ‘highly toxic’ heart drug - GPs must ‘be on alert’](https://www.thesun.co.uk/health/38812151/man-dies-toxic-heart-medication-gps-alert/) | thesun.co.uk | 9 | negative |
| 29 Apr 2026 | [Why hypertension remains one of the Caribbean’s deadliest health threats](https://www.caribbeannationalweekly.com/posts/why-hypertension-remains-one-of-the-caribbeans-deadliest-health-threats) | caribbeannationalweekly.com | 8 | negative |
| 28 Apr 2026 | [Arrested right-wing speaker Gautam Khattar hospitalised](https://www.newsdrum.in/national/arrested-right-wing-speaker-gautam-khattar-hospitalised-11776377) | newsdrum.in | 8 | negative |
| 28 Apr 2026 | [OMRON Healthcare Supports May Measurement Month 2026 with 3,000 Blood Pressure Monitors - citybuzz](https://www.citybuzz.co/2026/04/28/omron-healthcare-supports-may-measurement-month-2026-with-3000-blood-pressure-monitors/) | citybuzz.co | 8 | positive |
| 28 Apr 2026 | [Twice-yearly blood pressure treatment could reshape hypertension care, but doctors warn against a…](https://news-medical.net/news/20260427/Twice-yearly-blood-pressure-treatment-could-reshape-hypertension-care-but-doctors-warn-against-a-e2809cfire-and-forgete2809d-approach.aspx) | news-medical.net | 8 | negative |
| 27 Apr 2026 | [OMRON Healthcare Co., Ltd. \|](https://www.webdisclosure.com/press-release/advancing-early-detection-omron-healthcare-supports-may-measurement-month-2026-P5kLE0PolSe) | webdisclosure.com | 8 | positive |
| 23 Apr 2026 | [Six-Fold Renal Risk: The Potent Synergy of T2D and Hypertension in India, Study](https://medicaldialogues.in/nephrology/news/six-fold-renal-risk-the-potent-synergy-of-t2d-and-hypertension-in-india-study-168517) | medicaldialogues.in | 8 | negative |
| 20 Apr 2026 | [New free headline care initiative brings hope to Ghanaians battling silent killers - MyJoyOnline](https://www.myjoyonline.com/new-free-headline-care-initiative-brings-hope-to-ghanaians-battling-silent-killers/) | myjoyonline.com | 8 | positive |
| 20 Apr 2026 | [Free Primary Healthcare brings hope to Ghanaians battling silent killers - Adomonline.com](https://www.adomonline.com/free-primary-healthcare-brings-hope-to-ghanaians-battling-silent-killers/) | adomonline.com | 8 | positive |
| 16 Apr 2026 | [Louisiana Medicaid might add coverage for popular obesity treatment drugs](https://neworleanscitybusiness.com/blog/2026/04/16/louisiana-medicaid-weight-loss-drugs-expansion/) | neworleanscitybusiness.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "hypertension" --since 2026-01-01 --until 2026-04-30
prism-news trends "hypertension" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "hypertension" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "hypertension", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "hypertension", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Typhoid Outbreak](typhoid-outbreak.md)
- [Lupus News](lupus-news.md)
- [Anxiety News](anxiety-news.md)
- [Cell Therapy News](cell-therapy-news.md)
