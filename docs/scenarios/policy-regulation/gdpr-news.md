# GDPR News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gdpr news” · 20/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gdpr-news.json](../../examples/scenarios/gdpr-news.json).

**Question.** How did coverage of gdpr develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="GDPR"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 8,600 |
| Negative · neutral · positive | 22% · 5.6% · 72% |
| Critical (priority 7–9) | 55% (4,764 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (3,806 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | /people & society/social issues & advocacy/digital divide & technology access |

## Twelve months of coverage

Monthly matching articles for `GDPR` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,348 | 58% | 579 | 1,543 | ████████████ |
| Jun 2025 | 2,068 | 59% | 492 | 1,363 | ███████████ |
| Jul 2025 | 2,757 | 53% | 636 | 1,853 | ██████████████ |
| Aug 2025 | 2,344 | 63% | 666 | 1,524 | ████████████ |
| Sep 2025 | 3,465 | 71% | 1,193 | 2,118 | ██████████████████ |
| Oct 2025 | 3,806 | 76% | 1,377 | 2,341 | ████████████████████ |
| Nov 2025 | 3,661 | 77% | 1,381 | 2,202 | ███████████████████ |
| Dec 2025 | 2,913 | 67% | 915 | 1,849 | ███████████████ |
| Jan 2026 | 1,487 | 64% | 351 | 1,096 | ████████ |
| Feb 2026 | 2,661 | 59% | 668 | 1,858 | ██████████████ |
| Mar 2026 | 2,764 | 46% | 528 | 1,987 | ███████████████ |
| Apr 2026 | 1,688 | 57% | 354 | 1,268 | █████████ |

The last four complete months averaged 2,150 articles a month against 2,379 in the first four (-10%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 43% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,555 | 18% |
| United Kingdom | 410 | 4.8% |
| Nigeria | 391 | 4.5% |
| India | 176 | 2.0% |
| Germany | 149 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| /people & society/social issues & advocacy/digital divide & technology access | 384 | 9.2% | -3% |
| /people & society/social issues & advocacy/ethical technology & data privacy advocacy | 490 | 12% | -3% |
| data privacy compliance standards | 122 | 2.9% | +20% |
| data loss prevention (dlp) in networks | 153 | 3.7% | +11% |
| cloud storage security and encryption standards | 89 | 2.1% | +20% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Data Protection Insider, Issue 152 - Lexxion](https://www.lexxion.eu/en/dpi/data-protection-insider-issue-152/) | lexxion.eu | 8 | negative |
| 16 Apr 2026 | [Zara Parent Inditex Reports Third-Party Data Breach Involving Transaction Records – Outlook Business](https://www.outlookbusiness.com/deeptech/tech/zara-parent-inditex-reports-third-party-data-breach-involving-transaction-records) | outlookbusiness.com | 8 | negative |
| 16 Apr 2026 | [Digital Omnibus reality check: 83.5% of access requests not properly answered](https://noyb.eu/en/digital-omnibus-reality-check-835-access-requests-not-properly-answered) | noyb.eu | 8 | negative |
| 14 Apr 2026 | [GDPR Assessment Tool Market size to reach $5.96 Billion by 2035 \| Key players include OneTrust, TrustArc,…](https://www.openpr.com/news/4470489/gdpr-assessment-tool-market-size-to-reach-5-96-billion-by-2035) | openpr.com | 8 | positive |
| 14 Apr 2026 | [Four-Person Dutch Startup Launches Europe's First Sovereign AI Platform - Beyond the Reach of US Cloud Law](https://techrseries.com/artificial-intelligence/four-person-dutch-startup-launches-europes-first-sovereign-ai-platform-beyond-the-reach-of-us-cloud-law/) | techrseries.com | 8 | positive |
| 13 Apr 2026 | [General Data Protection Regulation (GDPR), Court of Justice of the European Union (CJEU), Data Controller \|…](https://www.jdsupra.com/topics/general-data-protection-regulation-gdpr/court-of-justice-of-the-european-union-cjeu/data-controller/) | jdsupra.com | 8 | negative |
| 24 Mar 2026 | [Data requests to support compensation claims can be refused](https://www.pinsentmasons.com/en-gb/out-law/news/data-requests-support-compensation-claims-refused) | pinsentmasons.com | 8 | negative |
| 23 Mar 2026 | [Compliance startup Delve accused of misleading customers about privacy regulations](https://americanbazaaronline.com/2026/03/23/compliance-startup-delve-accused-of-misleading-customers-477357/) | americanbazaaronline.com | 8 | negative |
| 22 Mar 2026 | [Delve accused of misleading customers with ‘fake compliance’ \| TechCrunch](https://techcrunch.com/2026/03/22/delve-accused-of-misleading-customers-with-fake-compliance/) | techcrunch.com | 8 | negative |
| 19 Mar 2026 | [Rechtsmissbrauch: Der EuGH erschwert das DSGVO-Hopping](https://www.lto.de/recht/nachrichten/n/eugh-urteil-c52624-brillen-rottler-rechtgsmissbrauch-exzessiv-erster-anspruch) | lto.de | 8 | negative |
| 16 Mar 2026 | [Court shoots down €746m 'flawed' Amazon GDPR fine - DecisionMarketing](https://www.decisionmarketing.co.uk/news/court-shoots-down-e746m-flawed-amazon-gdpr-fine) | decisionmarketing.co.uk | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "GDPR" --since 2026-01-01 --until 2026-04-30
prism-news trends "GDPR" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "GDPR" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "GDPR", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "GDPR", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Waqf News](waqf-news.md)
- [Minimum Wage News](minimum-wage-news.md)
- [Gun Control News](gun-control-news.md)
- [Uniform Civil Code News](uniform-civil-code-news.md)
