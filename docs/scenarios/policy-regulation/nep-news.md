# NEP News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nep news” · 70/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nep-news.json](../../examples/scenarios/nep-news.json).

**Question.** How did coverage of nep develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="NEP"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,477 |
| Negative · neutral · positive | 21% · 3.3% · 76% |
| Critical (priority 7–9) | 46% (4,321 articles) |
| Busiest month, May 2025 – Apr 2026 | Jun 2025 (3,560 articles) |
| Most-reported country | India (23% of matches) |
| Strongest theme by lift | mobile phone hardware components |

## Twelve months of coverage

Monthly matching articles for `NEP` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,657 | 43% | 338 | 1,272 | █████████ |
| Jun 2025 | 3,560 | 23% | 2,056 | 1,472 | ████████████████████ |
| Jul 2025 | 2,445 | 40% | 396 | 1,990 | ██████████████ |
| Aug 2025 | 2,272 | 42% | 508 | 1,676 | █████████████ |
| Sep 2025 | 2,895 | 56% | 981 | 1,863 | ████████████████ |
| Oct 2025 | 2,023 | 40% | 382 | 1,605 | ███████████ |
| Nov 2025 | 1,866 | 39% | 304 | 1,535 | ██████████ |
| Dec 2025 | 2,061 | 45% | 314 | 1,555 | ████████████ |
| Jan 2026 | 1,892 | 47% | 350 | 1,480 | ███████████ |
| Feb 2026 | 1,908 | 51% | 430 | 1,439 | ███████████ |
| Mar 2026 | 2,655 | 52% | 614 | 1,928 | ███████████████ |
| Apr 2026 | 3,022 | 36% | 560 | 2,359 | █████████████████ |

The last four complete months averaged 2,369 articles a month against 2,484 in the first four (-5%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 76% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 2,182 | 23% |
| United States | 1,484 | 16% |
| Nepal | 1,060 | 11% |
| China | 480 | 5.1% |
| United Kingdom | 480 | 5.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone hardware components | 383 | 6.5% | +10% |
| mobile phone battery performance | 383 | 6.5% | +3% |
| mobile phone display technologies | 284 | 4.8% | +12% |
| mobile phone water and dust resistance | 140 | 2.4% | +56% |
| 2-in-1 convertible laptops & hybrid notebooks | 129 | 2.2% | +617% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Editor, Parenting a daughter is undoubtedly a lifelong labour of love. Parents pour their heart and soul…](https://theshillongtimes.com/2026/04/30/are-women-employees-safe-in-the-corporate-world/) ⚠ | theshillongtimes.com | 8 | negative |
| 28 Apr 2026 | [How Manipur University Stands Out in NEP 2020: 80 Percent ABC and 70 Percent FYUP Adoption](https://www.indiatodayne.in/opinion/story/how-manipur-university-stands-out-in-nep-2020-80-percent-abc-and-70-percent-fyup-adoption-1382545-2026-04-28) | indiatodayne.in | 8 | positive |
| 27 Apr 2026 | [Are AI and Robotics Essential Subjects in Schools? \| Analytics India Magazine](https://analyticsindiamag.com/ai-features/ai-and-robotics-are-no-longer-optional-subjects-in-schools) ⚠ | analyticsindiamag.com | 8 | positive |
| 26 Apr 2026 | [UNSW Sydney and Deloitte Collaborate to Build Industry Ready Talent in India](https://www.forpressrelease.com/forpressrelease/670145/7/unsw-sydney-and-deloitte-collaborate-to-build-industry-ready-talent-in-india) ⚠ | forpressrelease.com | 8 | positive |
| 25 Apr 2026 | [Centre acknowledges IIT demand in Nagaland, no clear timeline yet](https://www.indiatodayne.in/nagaland/story/centre-acknowledges-iit-demand-in-nagaland-no-clear-timeline-yet-1381485-2026-04-25) ⚠ | indiatodayne.in | 8 | positive |
| 25 Apr 2026 | [UNSW and Deloitte Collaborate to Build Industry Ready Talent in India](https://businessnewsthisweek.com/education/unsw-and-deloitte-collaborate-to-build-industry-ready-talent-in-india/) ⚠ | businessnewsthisweek.com | 8 | positive |
| 24 Apr 2026 | [6.68 Lakh Students Register for CBSE Class X Second Board Exam](https://www.newkerala.com/news/a/over-668-lakh-students-register-cbse-class-second-395.htm) | newkerala.com | 8 | positive |
| 24 Apr 2026 | [Transmission Sector FY27 Turnover: Rs 7.6 Trillion Opportunity](https://www.newkerala.com/news/a/transmission-sector-set-fy27-turnaround-after-five-sluggish-796.htm) ⚠ | newkerala.com | 8 | positive |
| 23 Apr 2026 | [Education must be inclusive, value-based: LS Speaker Om Birla](https://www.dailyexcelsior.com/education-must-be-inclusive-value-based-ls-speaker-om-birla/) ⚠ | dailyexcelsior.com | 8 | positive |
| 23 Apr 2026 | [LG Sinha Calls For Students, Teachers' Role In Nation-Building](https://www.dailyexcelsior.com/lg-sinha-calls-for-students-teachers-role-in-nation-building/) ⚠ | dailyexcelsior.com | 8 | positive |
| 23 Apr 2026 | [RoW, policy hurdles slow grid expansion; Rs 7.6 trillion push needed](https://www.financialexpress.com/policy/economy/row-policy-hurdles-slow-grid-expansion-rs-7-6-trillion-push-needed/4216399/) ⚠ | financialexpress.com | 8 | positive |
| 23 Apr 2026 | [NHRC issues notice over costly private textbooks, asks Centre and states to enforce NCERT norms](https://www.ibtimes.co.in/nhrc-issues-notice-over-costly-private-textbooks-asks-centre-states-enforce-ncert-norms-901441) ⚠ | ibtimes.co.in | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "NEP" --since 2026-01-01 --until 2026-04-30
prism-news trends "NEP" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "NEP" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "NEP", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "NEP", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Drug Pricing News](drug-pricing-news.md)
- [Export Controls News](export-controls-news.md)
- [Consumer Protection News](consumer-protection-news.md)
- [Chips Act News](chips-act-news.md)
