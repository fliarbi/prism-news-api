# SAAS News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “saas news” · 140/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [saas-news.json](../../examples/scenarios/saas-news.json).

**Question.** How much saas coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="SaaS"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,570 |
| Negative · neutral · positive | 17% · 1.1% · 82% |
| Critical (priority 7–9) | 56% (7,547 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (4,148 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | customer relationship management (crm) systems |

## Twelve months of coverage

Monthly matching articles for `SaaS` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,306 | 48% | 235 | 2,034 | ███████████ |
| Jun 2025 | 2,204 | 48% | 231 | 1,947 | ███████████ |
| Jul 2025 | 3,092 | 45% | 353 | 2,723 | ███████████████ |
| Aug 2025 | 2,811 | 50% | 451 | 2,335 | ██████████████ |
| Sep 2025 | 2,903 | 53% | 399 | 2,476 | ██████████████ |
| Oct 2025 | 2,776 | 52% | 310 | 2,435 | █████████████ |
| Nov 2025 | 2,664 | 53% | 296 | 2,319 | █████████████ |
| Dec 2025 | 2,535 | 54% | 289 | 2,226 | ████████████ |
| Jan 2026 | 2,380 | 50% | 298 | 2,062 | ███████████ |
| Feb 2026 | 4,148 | 60% | 657 | 3,453 | ████████████████████ |
| Mar 2026 | 3,340 | 56% | 616 | 2,684 | ████████████████ |
| Apr 2026 | 3,702 | 54% | 668 | 2,983 | ██████████████████ |

The last four complete months averaged 3,392 articles a month against 2,603 in the first four (+30%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,353 | 17% |
| India | 710 | 5.2% |
| United Kingdom | 320 | 2.4% |
| Netherlands | 128 | 0.9% |
| Australia | 127 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| customer relationship management (crm) systems | 238 | 3.2% | -1% |
| technology adoption and digital transformation | 828 | 11% | +22% |
| enterprise-level cybersecurity solutions | 203 | 2.7% | +97% |
| zero trust network architecture | 197 | 2.7% | +89% |
| secure remote access solutions (e.g., rdp, ssh) | 178 | 2.4% | +74% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Ten airlines cancel thousands of flights as jet fuel crisis worsens](https://www.liverpoolecho.co.uk/travel/ten-airlines-cancel-thousands-flights-33803951) ⚠ | liverpoolecho.co.uk | 9 | negative |
| 2 Apr 2026 | [China says US-Israeli strikes 'root cause' of Starit of Hormuz disruption](https://economictimes.indiatimes.com/industry/energy/oil-gas/china-says-us-israeli-strikes-root-cause-of-starit-of-hormuz-disruption/articleshow/129973605.cms) ⚠ | economictimes.indiatimes.com | 9 | negative |
| 6 Mar 2026 | [A Personal Opinion: How Precision Strikes Silence the Conscience?](https://www.linkedin.com/pulse/personal-opinion-how-precision-strikes-silence-conscience-marty-yam-pb6rc) ⚠ | linkedin.com | 9 | negative |
| 20 Feb 2026 | [Trump sets 10-5 day ultimatum for Iran to make a deal as military buildup grows](https://dayton247now.com/news/nation-world/trump-sets-1015-day-ultimatum-for-iran-to-make-a-deal-as-military-buildup-grows-state-department-air-force) ⚠ | dayton247now.com | 9 | negative |
| 17 Feb 2026 | [American tourist beaten, stabbed to death in Bangkok after begging Thai girlfriend to take him back in love…](https://nypost.com/2026/02/17/world-news/american-tourist-beaten-stabbed-to-death-in-bangkok-after-begging-thai-girlfriend-to-take-him-back-in-love-triangle-horror/) ⚠ | nypost.com | 9 | negative |
| 30 Apr 2026 | [Nearly half of Australian firms hit by AI incidents](https://www.itbrief.com.au/story/nearly-half-of-australian-firms-hit-by-ai-incidents) ⚠ | itbrief.com.au | 8 | negative |
| 30 Apr 2026 | [What’s new: As agentic AI capabilities mature and enterprise software-as-a-service (SaaS) vendors build out…](https://deloitte.wsj.com/cmo/how-ai-agents-could-transform-saas-business-models-customer-experience-2d685f0d) | deloitte.wsj.com | 8 | positive |
| 30 Apr 2026 | [SaaS Security Risk Review \| CrowdStrike](https://www.crowdstrike.com/en-us/platform/falcon-shield/saas-security-risk-review/) | crowdstrike.com | 8 | negative |
| 30 Apr 2026 | [Nine Seconds to Zero: What the PocketOS Incident Reveals About Enterprise AI Risk](https://www.unite.ai/pocketos-incident-agentic-ai-security-risks/) | unite.ai | 8 | negative |
| 30 Apr 2026 | [Legora Raises $600M, Hits $5.6B Valuation in AI Boom](https://ventureburn.com/legora-raises-600m-hits-5-6b-valuation-in-ai-boom/) | ventureburn.com | 8 | positive |
| 30 Apr 2026 | [Dreamteam AI CRM startup eyes $40 Mn in Series A funding, targets disruption in global SaaS market \|…](https://businessreviewlive.com/dreamteam-ai-crm-startup-eyes-40-mn-in-series-a-funding-targets-disruption-in-global-saas-market/) | businessreviewlive.com | 8 | positive |
| 30 Apr 2026 | [Software: 10 companies that raised the most in 2025](https://tech.eu/2026/04/30/software-10-companies-that-raised-the-most-in-2025/www.grammarly.com) ⚠ | tech.eu | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "SaaS" --since 2026-01-01 --until 2026-04-30
prism-news trends "SaaS" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "SaaS" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "SaaS", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "SaaS", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Laptop News](laptop-news.md)
- [Operating System News](operating-system-news.md)
- [Cloud Security News](cloud-security-news.md)
- [Wearables News](wearables-news.md)
