# Medicare News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “medicare news” · 90/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [medicare-news.json](../../examples/scenarios/medicare-news.json).

**Question.** How did coverage of medicare develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="medicare"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 22,346 |
| Negative · neutral · positive | 54% · 2.7% · 44% |
| Critical (priority 7–9) | 78% (17,455 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (8,028 articles) |
| Most-reported country | United States (52% of matches) |
| Strongest theme by lift | medicare and medicaid eligibility guidelines |

## Twelve months of coverage

Monthly matching articles for `medicare` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4,918 | 76% | 3,131 | 1,708 | ████████████ |
| Jun 2025 | 3,131 | 78% | 1,950 | 1,084 | ████████ |
| Jul 2025 | 5,985 | 68% | 3,834 | 2,019 | ███████████████ |
| Aug 2025 | 8,028 | 71% | 5,251 | 2,644 | ████████████████████ |
| Sep 2025 | 4,395 | 78% | 2,535 | 1,764 | ███████████ |
| Oct 2025 | 4,908 | 80% | 2,869 | 1,946 | ████████████ |
| Nov 2025 | 4,041 | 72% | 2,061 | 1,828 | ██████████ |
| Dec 2025 | 3,925 | 78% | 1,862 | 1,911 | ██████████ |
| Jan 2026 | 3,814 | 77% | 1,712 | 2,002 | ██████████ |
| Feb 2026 | 7,757 | 83% | 4,319 | 3,275 | ███████████████████ |
| Mar 2026 | 4,587 | 75% | 2,497 | 1,933 | ███████████ |
| Apr 2026 | 6,188 | 75% | 3,416 | 2,553 | ███████████████ |

The last four complete months averaged 5,586 articles a month against 5,516 in the first four (+1%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 57% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 11,608 | 52% |
| Australia | 232 | 1.0% |
| United Kingdom | 114 | 0.5% |
| Canada | 102 | 0.5% |
| Germany | 97 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| medicare and medicaid eligibility guidelines | 472 | 3.6% | -7% |
| patient safety and quality improvement studies | 270 | 2.1% | +11% |
| medical billing and coding services | 238 | 1.8% | +89% |
| medicare and medicaid policy updates | 825 | 6.3% | -7% |
| health insurance fraud awareness | 180 | 1.4% | +84% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Dr. Oz touts ‘Fraud War Room,’ ending payments to 400 Calif. hospices over fears of $100B fraud - Amed Post](https://amedpost.com/dr-oz-touts-fraud-war-room-ending-payments-to-400-calif-hospices-over-fears-of-100b-fraud/) | amedpost.com | 9 | negative |
| 22 Apr 2026 | [Exclusive \| Dr. Oz touts ‘Fraud War Room,’ ending payments to 400 hospices in California over fears of $100B…](https://nypost.com/2026/04/22/us-news/dr-oz-touts-fraud-war-room-ending-payments-to-400-calif-hospices-over-fears-of-100b-fraud/) | nypost.com | 9 | negative |
| 7 Apr 2026 | [War abroad, tyranny at home — and the theft of a nation](https://www.presstelegram.com/2026/04/07/war-abroad-tyranny-at-home-and-the-theft-of-a-nation/) | presstelegram.com | 9 | negative |
| 3 Apr 2026 | [8 people, including nurses, took over $50M in false claims, prosecutors say](https://www.aol.com/articles/8-people-including-nurses-took-050020581.html) | aol.com | 9 | negative |
| 3 Apr 2026 | [Multiple arrests in 'Operation Never Say Die,' targeting hospice, healthcare fraud in CA](https://www.ktul.com/news/nation-world/multiple-arrests-in-operation-never-say-die-targeting-hospice-healthcare-fraud-in-ca-gavin-newsom-justice-department-los-angeles) | ktul.com | 9 | negative |
| 2 Apr 2026 | [Oz Goes After California Fraud, Announces Sweeping Arrests](https://news.bloomberglaw.com/health-law-and-business/oz-goes-after-california-fraud-announces-sweeping-arrests) ⚠ | news.bloomberglaw.com | 9 | negative |
| 30 Mar 2026 | [The End of "Trust the Voice on the Phone": Is This a Real Human? \| Pindrop](https://www.pindrop.com/article/end-of-voice-trust-on-phone/) | pindrop.com | 9 | negative |
| 30 Apr 2026 | [Stopping fraud to save Medicare](https://standard-democrat.com/opinion/stopping-fraud-to-save-medicare-251b3cb8) | standard-democrat.com | 8 | negative |
| 30 Apr 2026 | [Trump administration defers $91M more in Minnesota Medicaid funding citing fraud vulnerabilities](https://www.ajc.com/news/2026/04/trump-administration-defers-91m-more-in-minnesota-medicaid-funding-citing-fraud-vulnerabilities/) | ajc.com | 8 | negative |
| 30 Apr 2026 | [New CAC Reimbursement for Routine Chest CT Scans - Riverain Tech](https://www.riveraintech.com/new-cac-reimbursement-for-routine-chest-ct-scans/) | riveraintech.com | 8 | positive |
| 30 Apr 2026 | [Trump's Medicaid Work Requirements Will Rob 5-10 Million of Health Coverage - NCPSSM](https://www.ncpssm.org/entitledtoknow/trumps-medicaid-work-requirements-will-rob-5-10-million-of-health-coverage/) ⚠ | ncpssm.org | 8 | negative |
| 29 Apr 2026 | [Lawmakers Support CMS Rules to Streamline Prior Authorizations \| Psychiatric Times](http://www.psychiatrictimes.com/view/lawmakers-support-cms-rules-to-streamline-prior-authorizations) | psychiatrictimes.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "medicare" --since 2026-01-01 --until 2026-04-30
prism-news trends "medicare" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "medicare" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "medicare", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "medicare", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI Regulation News](ai-regulation-news.md)
- [Food Safety News](food-safety-news.md)
- [EU AI Act News](eu-ai-act-news.md)
- [Citizenship News](citizenship-news.md)
