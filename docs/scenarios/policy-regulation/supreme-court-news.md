# Supreme Court News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “supreme court news” · 12,100/month India · 201,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [supreme-court-news.json](../../examples/scenarios/supreme-court-news.json).

**Question.** How did coverage of supreme court develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="supreme court"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 86,389 |
| Negative · neutral · positive | 80% · 5.5% · 15% |
| Critical (priority 7–9) | 90% (77,626 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (29,698 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | supreme court rulings and decisions |

## Twelve months of coverage

Monthly matching articles for `supreme court` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19,679 | 85% | 14,954 | 2,951 | █████████████ |
| Jun 2025 | 13,406 | 84% | 10,987 | 1,622 | █████████ |
| Jul 2025 | 21,743 | 71% | 18,143 | 2,612 | ███████████████ |
| Aug 2025 | 29,698 | 81% | 24,289 | 4,125 | ████████████████████ |
| Sep 2025 | 20,366 | 89% | 15,960 | 3,130 | ██████████████ |
| Oct 2025 | 13,770 | 88% | 10,683 | 2,252 | █████████ |
| Nov 2025 | 15,477 | 90% | 12,145 | 2,359 | ██████████ |
| Dec 2025 | 12,736 | 90% | 9,976 | 2,018 | █████████ |
| Jan 2026 | 12,919 | 89% | 9,848 | 2,240 | █████████ |
| Feb 2026 | 29,474 | 91% | 24,326 | 3,882 | ████████████████████ |
| Mar 2026 | 18,315 | 89% | 14,301 | 2,794 | ████████████ |
| Apr 2026 | 25,681 | 89% | 20,294 | 3,739 | █████████████████ |

The last four complete months averaged 21,597 articles a month against 21,132 in the first four (+2%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 51% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 25,211 | 29% |
| India | 11,508 | 13% |
| Philippines | 793 | 0.9% |
| China | 571 | 0.7% |
| United Kingdom | 552 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| supreme court rulings and decisions | 5,701 | 9.8% | +104% |
| judicial appointments and confirmations | 1,439 | 2.5% | +30% |
| gerrymandering controversies | 1,186 | 2.0% | +5% |
| judicial independence and accountability | 980 | 1.7% | +105% |
| human rights law and judicial enforcement | 1,389 | 2.4% | +75% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Evening news wrap: SC asks Centre to consider abortion beyond 20 weeks for rape survivors; & more \| India…](https://timesofindia.indiatimes.com/india/evening-news-wrap-sc-asks-centre-to-consider-abortion-beyond-20-weeks-for-rape-survivors-more/articleshow/130631908.cms) | timesofindia.indiatimes.com | 9 | negative |
| 30 Apr 2026 | [Supreme Court: 'Imagine the pain, humiliation': Supreme Court urges Centre to allow abortion beyond 20 weeks…](https://timesofindia.indiatimes.com/india/imagine-the-pain-humiliation-supreme-court-urges-centre-to-allow-abortion-beyond-20-weeks-for-rape-survivors/articleshow/130625509.cms) | timesofindia.indiatimes.com | 9 | negative |
| 30 Apr 2026 | [SC asks Centre to consider amending law on terminating pregnancy of rape survivors](https://economictimes.indiatimes.com/news/india/sc-asks-centre-to-consider-amending-law-on-terminating-pregnancy-of-rape-survivors/articleshow/130625368.cms) | economictimes.indiatimes.com | 9 | negative |
| 29 Apr 2026 | [California Attorney General seeks review of overturned murder conviction in Sierra LaMar case](https://www.cbsnews.com/sanfrancisco/news/sierra-lamar-case-antolin-garcia-torres-overturned-kidnapping-murder-conviction-review-sought/) | cbsnews.com | 9 | negative |
| 25 Apr 2026 | [Cubs place left-handed reliever Caleb Thielbar on injured list, 8th pitcher to get hurt](https://apnews.com/article/cubs-lopez-velasquez-thielbar-hodge-8ebedf8c9b3b154c41a910f3e8963bb4) | apnews.com | 9 | negative |
| 24 Apr 2026 | [Dozens of Thai opposition figures to go on trial over bid to amend royal insult law](https://www.thestandard.com.hk/world/article/330216/Dozens-of-Thai-opposition-figures-to-go-on-trial-over-bid-to-amend-royal-insult-law) | thestandard.com.hk | 9 | negative |
| 24 Apr 2026 | ['Her Choice Comes First, Unwanted Pregnancy Cannot Be Forced': SC Allows Teen To Terminate 7-Month Pregnancy](https://newsable.asianetnews.com/india/supreme-court-says-woman-cannot-be-forced-to-continue-unwanted-pregnancy-allows-teen-to-terminate-7-month-pregnancy-articleshow-tqts6uw) | newsable.asianetnews.com | 9 | negative |
| 22 Apr 2026 | [Supreme Court revives wounded veteran’s lawsuit against a contractor over suicide bombing](https://www.ajc.com/news/2026/04/supreme-court-revives-wounded-veterans-lawsuit-against-a-contractor-over-suicide-bombing/) | ajc.com | 9 | negative |
| 18 Apr 2026 | [BOOK: Liberal Justice Kagan Screamed "So Loudly" at Justice Breyer After Dobbs Draft Leak that the 'Wall Was…](https://www.thegatewaypundit.com/2026/04/book-liberal-justice-kagan-screamed-so-loudly-justice/) | thegatewaypundit.com | 9 | negative |
| 15 Apr 2026 | [Trump ‘prepared’ to nominate new Supreme Court justice if Alito, Thomas retire](https://thehill.com/homenews/administration/5831975-trump-prepared-name-supreme-justice/) | thehill.com | 9 | negative |
| 14 Apr 2026 | [Underworld figure Gavin Preston, 50, was gunned down by two men dressed in black while eating breakfast at a…](https://www.riverineherald.com.au/national/duo-face-trial-for-planned-underworld-hit-at-cafe/) | riverineherald.com.au | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "supreme court" --since 2026-01-01 --until 2026-04-30
prism-news trends "supreme court" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "supreme court" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "supreme court", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "supreme court", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tariffs News](tariffs-news.md)
- [AI Regulation News](ai-regulation-news.md)
