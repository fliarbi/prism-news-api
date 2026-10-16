# Right to Repair News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “right to repair news” · 10/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [right-to-repair-news.json](../../examples/scenarios/right-to-repair-news.json).

**Question.** How did coverage of right to repair develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="right to repair"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 243 |
| Negative · neutral · positive | 37% · 1.6% · 61% |
| Critical (priority 7–9) | 64% (156 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (123 articles) |
| Most-reported country | United States (60% of matches) |
| Strongest theme by lift | mobile phone customer support services |

## Twelve months of coverage

Monthly matching articles for `right to repair` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 58% | 1 | 11 | ██ |
| Jun 2025 | 14 | 57% | 5 | 9 | ██ |
| Jul 2025 | 13 | 38% | 3 | 9 | ██ |
| Aug 2025 | 22 | 68% | 8 | 14 | ████ |
| Sep 2025 | 8 | 12% | 0 | 8 | █ |
| Oct 2025 | 13 | 54% | 5 | 8 | ██ |
| Nov 2025 | 11 | 64% | 3 | 8 | ██ |
| Dec 2025 | 14 | 86% | 8 | 6 | ██ |
| Jan 2026 | 19 | 63% | 9 | 9 | ███ |
| Feb 2026 | 123 | 64% | 55 | 68 | ████████████████████ |
| Mar 2026 | 42 | 62% | 13 | 27 | ███████ |
| Apr 2026 | 59 | 66% | 13 | 45 | ██████████ |

The last four complete months averaged 61 articles a month against 15 in the first four (+298%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 68% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 147 | 60% |
| France | 4 | 1.6% |
| Canada | 3 | 1.2% |
| Germany | 3 | 1.2% |
| South Korea | 3 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone customer support services | 23 | 19% | +1050% |
| mobile phone repair and maintenance | 22 | 18% | +1000% |
| mobile phone health and safety standards | 19 | 16% | +850% |
| tractors and tractor attachments | 12 | 10% | new |
| mobile phone recycling and sustainability | 11 | 9.2% | +450% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 19 Feb 2026 | [Apple Emails Reveal Internal Debate on Right to Repair](https://www.ifixit.com/News/43008/apple-emails-reveal-internal-debate-on-right-to-repair) | ifixit.com | 8 | negative |
| 19 Feb 2026 | [The Five Worst Repair Stories People Told the FTC](https://www.ifixit.com/News/30680/the-five-worst-repair-stories-people-told-the-ftc) | ifixit.com | 8 | negative |
| 28 Apr 2026 | [EU Right to Repair rules are coming to save your phone battery in 2027 - CyberShack](https://cybershack.com.au/other/eu-right-to-repair-rule-2027/) | cybershack.com.au | 7 | positive |
| 17 Apr 2026 | [Nachhaltigkeit: Reparatur-Recht gefährdet Garantien](https://www.lebensmittelzeitung.net/politik/nachrichten/nachhaltigkeit-reparatur-recht-gefaehrdet-garantien-190507) | lebensmittelzeitung.net | 7 | positive |
| 27 Feb 2026 | [Right to Repair Is Gaining Ground in 2020](https://www.ifixit.com/News/35606/right-to-repair-is-gaining-ground-in-2020) | ifixit.com | 7 | negative |
| 27 Feb 2026 | [New Poll Finds Americans Overwhelmingly Support Right to Repair](https://www.ifixit.com/News/35567/new-poll-finds-americans-overwhelmingly-support-right-to-repair) | ifixit.com | 7 | negative |
| 27 Feb 2026 | [Right to Repair Laws Have Now Been Introduced in All 50 US States](https://www.ifixit.com/News/108371/right-to-repair-laws-have-now-been-introduced-in-all-50-us-states) | ifixit.com | 7 | negative |
| 27 Feb 2026 | [Iowa Farmers Are Leading the Fight for Repair](https://www.ifixit.com/News/115722/iowa-farmers-are-leading-the-fight-for-repair) | ifixit.com | 7 | negative |
| 19 Feb 2026 | [Australia&#8217;s Right to Repair Proposal for Motor Vehicles Is a Good Start](http://www.ifixit.com/News/13993/australias-right-to-repair-proposal-is-a-good-start-but-its-not-enough) | ifixit.com | 7 | positive |
| 19 Feb 2026 | [FTC Unanimously Approves Policy of Fighting Repair Restrictions](http://www.ifixit.com/News/51520/ftc-unanimously-approves-policy-of-fighting-repair-restrictions) | ifixit.com | 7 | positive |
| 19 Feb 2026 | [Action, please! Europe’s vision for a circular economy](http://www.ifixit.com/News/36283/eu-circular-economy-action-plan) | ifixit.com | 7 | negative |
| 19 Feb 2026 | [Victory! New York Senate Passes Landmark Right to Repair Bill](http://www.ifixit.com/News/50722/victory-new-york-senate-passes-landmark-right-to-repair-bill) | ifixit.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "right to repair" --since 2026-01-01 --until 2026-04-30
prism-news trends "right to repair" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "right to repair" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "right to repair", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "right to repair", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [CBAM News](cbam-news.md)
- [Immigration Policy News](immigration-policy-news.md)
- [Drug Pricing News](drug-pricing-news.md)
- [Export Controls News](export-controls-news.md)
