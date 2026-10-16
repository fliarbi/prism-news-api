# Kidney Disease News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “kidney disease news” · 10/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [kidney-disease-news.json](../../examples/scenarios/kidney-disease-news.json).

**Question.** How much kidney disease coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="kidney disease"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,608 |
| Negative · neutral · positive | 15% · 6.4% · 78% |
| Critical (priority 7–9) | 90% (3,260 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,259 articles) |
| Most-reported country | United States (5.1% of matches) |
| Strongest theme by lift | patient safety and quality improvement studies |

## Twelve months of coverage

Monthly matching articles for `kidney disease` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 714 | 90% | 125 | 530 | ███████████ |
| Jun 2025 | 667 | 91% | 111 | 513 | ███████████ |
| Jul 2025 | 668 | 88% | 112 | 490 | ███████████ |
| Aug 2025 | 732 | 87% | 133 | 549 | ████████████ |
| Sep 2025 | 699 | 89% | 100 | 547 | ███████████ |
| Oct 2025 | 841 | 88% | 204 | 568 | █████████████ |
| Nov 2025 | 831 | 92% | 154 | 613 | █████████████ |
| Dec 2025 | 1,120 | 94% | 128 | 911 | ██████████████████ |
| Jan 2026 | 1,259 | 93% | 165 | 991 | ████████████████████ |
| Feb 2026 | 708 | 90% | 111 | 555 | ███████████ |
| Mar 2026 | 851 | 88% | 154 | 650 | ██████████████ |
| Apr 2026 | 790 | 88% | 119 | 627 | █████████████ |

The last four complete months averaged 902 articles a month against 695 in the first four (+30%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 12% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 184 | 5.1% |
| India | 76 | 2.1% |
| China | 25 | 0.7% |
| United Kingdom | 18 | 0.5% |
| Nigeria | 17 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| patient safety and quality improvement studies | 252 | 12% | +18% |
| public health initiatives and programs | 220 | 10% | +7% |
| diabetes medication management | 165 | 7.7% | +21% |
| health disparities and equity research | 333 | 16% | +13% |
| rare disease research publications | 156 | 7.3% | +14% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Mar 2026 | [World Kidney Day: Contaminated water raises alarm as Odisha sees rise in kidney diseases](https://sambadenglish.com/latest-news/world-kidney-day-contaminated-water-raises-alarm-as-odisha-sees-rise-in-kidney-diseases-11204807) | sambadenglish.com | 9 | negative |
| 23 Apr 2026 | [A Simple Rupees 300 Test Can Catch Chronic Kidney Disease Early - Here’s Why Doctors Urge Screening](https://www.timesnownews.com/health/a-simple-rupees-300-test-can-catch-chronic-kidney-disease-early-heres-why-doctors-urge-screening-article-154143351) | timesnownews.com | 8 | positive |
| 21 Apr 2026 | [Caring for Australians and New ZealandeRs with kidney Impairment guideline commentary on kidney disease:…](https://pubmed.ncbi.nlm.nih.gov/42011799/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 13 Apr 2026 | [Save kidney, save resources](https://www.thestar.com.my/news/nation/2026/04/13/save-kidney-save-resources) | thestar.com.my | 8 | positive |
| 31 Mar 2026 | [‘Real Housewives’ Star Shares the Symptoms Leading to Frightening Diagnosis](https://www.yahoo.com/entertainment/celebrity/articles/real-housewives-star-shares-symptoms-193812329.html) | yahoo.com | 8 | negative |
| 23 Mar 2026 | [Implications of AKI-D Versus ESKD Status.](https://pubmed.ncbi.nlm.nih.gov/41881384/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 21 Mar 2026 | [Latest News Manipal Hospital Yeshwanthpur Celebrates 50+ ABO-Incompatible and 500+ Kidney Transplants on…](https://businessfortnight.com/manipal-hospital-yeshwanthpur-celebrates-50-abo-incompatible-and-500-kidney-transplants-on-world-kidney-day-2026/) | businessfortnight.com | 8 | positive |
| 21 Mar 2026 | [Manipal Hospital Yeshwanthpur Celebrates 50+ ABO-Incompatible and 500+ Kidney Transplants on World Kidney…](https://mediabulletins.com/business/manipal-hospital-yeshwanthpur-celebrates-50-abo-incompatible-and-500-kidney-transplants-on-world-kidney-day-2026/) | mediabulletins.com | 8 | positive |
| 14 Mar 2026 | [World Kidney Day 2026: Experts highlight AI and advanced technologies in fight against kidney disease](https://www.kbc.co.ke/world-kidney-day-2026-experts-highlight-ai-and-advanced-technologies-in-fight-against-kidney-disease/) | kbc.co.ke | 8 | positive |
| 14 Mar 2026 | [Kidney health in the spotlight: SHEILD Ghana issues urgent call for national action on World Kidney Day -…](https://www.myjoyonline.com/kidney-health-in-the-spotlight-sheild-ghana-issues-urgent-call-for-national-action-on-world-kidney-day/) | myjoyonline.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "kidney disease" --since 2026-01-01 --until 2026-04-30
prism-news trends "kidney disease" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "kidney disease" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "kidney disease", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "kidney disease", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Asthma News](asthma-news.md)
- [Antibiotics News](antibiotics-news.md)
- [Leprosy News](leprosy-news.md)
- [Drug Shortage News](drug-shortage-news.md)
