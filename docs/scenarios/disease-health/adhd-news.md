# ADHD News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “adhd news” · 20/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [adhd-news.json](../../examples/scenarios/adhd-news.json).

**Question.** How much adhd coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="ADHD"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,254 |
| Negative · neutral · positive | 31% · 1.7% · 67% |
| Critical (priority 7–9) | 49% (1,599 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (872 articles) |
| Most-reported country | United States (16% of matches) |
| Strongest theme by lift | neurodevelopmental disorders (e.g., adhd, dyslexia) |

## Twelve months of coverage

Monthly matching articles for `ADHD` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 418 | 50% | 145 | 264 | ██████████ |
| Jun 2025 | 397 | 64% | 152 | 232 | █████████ |
| Jul 2025 | 425 | 62% | 166 | 251 | ██████████ |
| Aug 2025 | 524 | 63% | 188 | 328 | ████████████ |
| Sep 2025 | 547 | 64% | 268 | 270 | █████████████ |
| Oct 2025 | 500 | 60% | 196 | 288 | ███████████ |
| Nov 2025 | 503 | 61% | 192 | 303 | ████████████ |
| Dec 2025 | 577 | 63% | 206 | 353 | █████████████ |
| Jan 2026 | 846 | 53% | 257 | 577 | ███████████████████ |
| Feb 2026 | 861 | 41% | 246 | 605 | ████████████████████ |
| Mar 2026 | 675 | 50% | 216 | 445 | ███████████████ |
| Apr 2026 | 872 | 53% | 288 | 556 | ████████████████████ |

The last four complete months averaged 814 articles a month against 441 in the first four (+84%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 32% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 525 | 16% |
| United Kingdom | 194 | 6.0% |
| Australia | 44 | 1.4% |
| New Zealand | 42 | 1.3% |
| Canada | 29 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| neurodevelopmental disorders (e.g., adhd, dyslexia) | 418 | 24% | +31% |
| autism spectrum disorder behavioral therapies | 138 | 7.8% | +37% |
| pediatric dosage calculations | 73 | 4.1% | +30% |
| family therapy and counseling methods | 64 | 3.6% | +137% |
| mental health drug side effects | 230 | 13% | +113% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Mar 2026 | [ADHD medication shortage strains patients and families](https://www.pbssocal.org/shows/newshour/clip/adhd-drug-shortage-1698700721) | pbssocal.org | 9 | negative |
| 30 Apr 2026 | [ADHD Expert Reveals One Sign Commonly Missed With Girls](https://www.huffingtonpost.co.uk/entry/adhd-signs-girls-adults-mental-health_uk_69f34b2fe4b058c24a534be5) | huffingtonpost.co.uk | 8 | negative |
| 29 Apr 2026 | [AI Tool May Help Identify ADHD in Kids Long Before Typical Diagnosis](https://www.visionmonday.com/eyecare/health-watch/article/ai-tool-may-help-identify-adhd-in-kids-long-before-typical-diagnosis/) | visionmonday.com | 8 | positive |
| 29 Apr 2026 | [This Common Mental Disorder Has a Strange Link to Severe Chronic Pain](https://dnyuz.com/2026/04/29/this-common-mental-disorder-has-a-strange-link-to-severe-chronic-pain/) | dnyuz.com | 8 | negative |
| 29 Apr 2026 | [AI Tool May Help Identify ADHD in Kids Long Before Typical Diagnosis - Drugs.com MedNews](https://www.drugs.com/news/ai-tool-may-help-identify-adhd-kids-long-before-typical-diagnosis-129838.html) | drugs.com | 8 | positive |
| 28 Apr 2026 | [The Truth About ADHD and Dopamine](http://www.psychologytoday.com/us/blog/changing-minds/202604/the-truth-about-adhd-and-dopamine) | psychologytoday.com | 8 | negative |
| 28 Apr 2026 | [AI Tool may Spot ADHD Years Before Children are Diagnosed Attention-deficit/hyperactivity disorder (ADHD)…](https://www.ehealthnews.eu/research/7667-ai-tool-may-spot-adhd-years-before-children-are-diagnosed) | ehealthnews.eu | 8 | positive |
| 28 Apr 2026 | [AI tool could detect ADHD risk in children years before diagnosis, study finds](https://www.openaccessgovernment.org/ai-tool-could-detect-adhd-risk-in-children-years-before-diagnosis-study-finds/208746/) | openaccessgovernment.org | 8 | positive |
| 28 Apr 2026 | [Could AI help spot ADHD in children before symptoms fully emerge?](http://www.euronews.com/health/2026/04/28/ai-tool-could-help-predict-adhd-in-children-years-before-a-formal-diagnosis) | euronews.com | 8 | positive |
| 27 Apr 2026 | [AI tools can predict ADHD risk years before a formal diagnosis](https://news-medical.net/news/20260427/AI-tools-can-predict-ADHD-risk-years-before-a-formal-diagnosis.aspx) | news-medical.net | 8 | positive |
| 25 Apr 2026 | [Shared brain connectivity patterns found across major neurodevelopmental disorders](https://www.news-medical.net/news/20260425/Shared-brain-connectivity-patterns-found-across-major-neurodevelopmental-disorders.aspx) | news-medical.net | 8 | positive |
| 23 Apr 2026 | [Risk of Substance Abuse Not Increased by ADHD Drugs \| Psychiatric Times](http://www.psychiatrictimes.com/view/risk-substance-abuse-not-increased-adhd-drugs) | psychiatrictimes.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ADHD" --since 2026-01-01 --until 2026-04-30
prism-news trends "ADHD" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ADHD" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ADHD", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ADHD", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Chikungunya Outbreak](chikungunya-outbreak.md)
- [Pandemic News](pandemic-news.md)
- [Gene Therapy News](gene-therapy-news.md)
- [Zika Outbreak](zika-outbreak.md)
