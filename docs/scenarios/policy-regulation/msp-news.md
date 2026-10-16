# MSP News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “msp news” · 260/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [msp-news.json](../../examples/scenarios/msp-news.json).

**Question.** How did coverage of msp develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="MSP"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 7,052 |
| Negative · neutral · positive | 41% · 1.8% · 58% |
| Critical (priority 7–9) | 65% (4,577 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,966 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | agricultural policy and regulatory compliance |

## Twelve months of coverage

Monthly matching articles for `MSP` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,192 | 64% | 464 | 713 | ████████████ |
| Jun 2025 | 1,165 | 64% | 440 | 709 | ████████████ |
| Jul 2025 | 1,001 | 61% | 390 | 597 | ██████████ |
| Aug 2025 | 1,511 | 68% | 782 | 703 | ███████████████ |
| Sep 2025 | 1,441 | 62% | 563 | 862 | ███████████████ |
| Oct 2025 | 1,657 | 69% | 678 | 969 | █████████████████ |
| Nov 2025 | 1,382 | 68% | 599 | 764 | ██████████████ |
| Dec 2025 | 1,151 | 66% | 505 | 629 | ████████████ |
| Jan 2026 | 1,288 | 66% | 487 | 778 | █████████████ |
| Feb 2026 | 1,883 | 64% | 742 | 1,122 | ███████████████████ |
| Mar 2026 | 1,915 | 64% | 828 | 1,063 | ███████████████████ |
| Apr 2026 | 1,966 | 65% | 804 | 1,092 | ████████████████████ |

The last four complete months averaged 1,763 articles a month against 1,217 in the first four (+45%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,317 | 19% |
| India | 944 | 13% |
| United Kingdom | 860 | 12% |
| Scotland | 167 | 2.4% |
| Australia | 40 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agricultural policy and regulatory compliance | 104 | 2.6% | +206% |
| farm labor management and safety protocols | 81 | 2.1% | +62% |
| zero trust network architecture | 62 | 1.6% | +24% |
| threat intelligence integration for networks | 90 | 2.3% | +190% |
| agricultural insurance and risk management | 141 | 3.6% | +25% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Belding resident arrested for possessing child sexually abusive material - The Daily News](https://www.thedailynews.cc/articles/belding-resident-arrested-for-possessing-child-sexually-abusive-material/) | thedailynews.cc | 9 | negative |
| 20 Feb 2026 | [Grand Rapids police shoot, kill man. What we know](https://www.freep.com/story/news/local/michigan/2026/02/20/fatal-shooting-michigan-state-police-grand-rapids-officer-gun/88775146007/) | freep.com | 9 | negative |
| 11 Feb 2026 | [St. Mary’s County man arrested, charged for viewing, accessing, distributing, possessing child pornography:…](https://www.yahoo.com/news/articles/st-mary-county-man-arrested-005954866.html) | yahoo.com | 9 | negative |
| 29 Apr 2026 | [25 Investigates: Bad arrests, an impounded kidney; the MSP liability crisis costing you millions](https://www.yahoo.com/news/articles/25-investigates-bad-arrests-impounded-214756652.html) | yahoo.com | 8 | negative |
| 29 Apr 2026 | [Guardz 2026 State of MSP Threat Report: AI and cybersecurity landscape](https://digitalisationworld.com/news/72225/guardz-2026-state-of-msp-threat-report-ai-and-cybersecurity-landscape) | digitalisationworld.com | 8 | negative |
| 27 Apr 2026 | [Police Blotter: Fatal I-95 crash; North End burglary suspect arrested](https://www.bostonherald.com/2026/04/27/police-blotter-fatal-i-95-crash-north-end-burglary-suspect-arrested/) | bostonherald.com | 8 | negative |
| 27 Apr 2026 | [Integris Announces Intent to Acquire MSP First Focus, Expanding SMB-Focused Managed Services Presence Across…](https://aithority.com/machine-learning/integris-announces-intent-to-acquire-msp-first-focus-expanding-smb-focused-managed-services-presence-across-australia-new-zealand-and-the-philippines/) | aithority.com | 8 | positive |
| 26 Apr 2026 | [Belding man arrested for alleged possession of child porn](https://www.yahoo.com/news/articles/belding-man-arrested-alleged-possession-181257154.html) | yahoo.com | 8 | negative |
| 24 Apr 2026 | [Paddy Procurement Yet to Begin in 13 Districts](https://www.telugu360.com/paddy-procurement-yet-to-begin-in-13-districts/) | telugu360.com | 8 | positive |
| 24 Apr 2026 | [Missing 8-month-old found safe: MSP](https://www.yahoo.com/news/articles/endangered-missing-advisory-issued-8-091904615.html) | yahoo.com | 8 | negative |
| 22 Apr 2026 | [Chandrababu is Anti-Farmer: YSRCP](http://www.sakshipost.com/news/andhrapradesh/chandrababu-anti-farmer-ysrcp-478978) | sakshipost.com | 8 | negative |
| 21 Apr 2026 | [Holyrood election candidates urged to back five pledges in support of Ukraine](https://www.thenational.scot/news/26040274.holyrood-candidates-urged-back-five-pledges-support-ukraine/) | thenational.scot | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "MSP" --since 2026-01-01 --until 2026-04-30
prism-news trends "MSP" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "MSP" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "MSP", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "MSP", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Obamacare News](obamacare-news.md)
- [Trade War News](trade-war-news.md)
- [Data Privacy News](data-privacy-news.md)
- [FSSAI News](fssai-news.md)
