# Waqf News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “waqf news” · 590/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [waqf-news.json](../../examples/scenarios/waqf-news.json).

**Question.** How did coverage of waqf develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="waqf"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 387 |
| Negative · neutral · positive | 61% · 5.2% · 33% |
| Critical (priority 7–9) | 78% (303 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (540 articles) |
| Most-reported country | India (44% of matches) |
| Strongest theme by lift | religious laws and governance |

## Twelve months of coverage

Monthly matching articles for `waqf` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 486 | 82% | 368 | 62 | ██████████████████ |
| Jun 2025 | 155 | 65% | 92 | 51 | ██████ |
| Jul 2025 | 256 | 61% | 203 | 38 | █████████ |
| Aug 2025 | 118 | 75% | 69 | 44 | ████ |
| Sep 2025 | 540 | 91% | 421 | 80 | ████████████████████ |
| Oct 2025 | 172 | 84% | 125 | 41 | ██████ |
| Nov 2025 | 103 | 80% | 53 | 33 | ████ |
| Dec 2025 | 244 | 85% | 167 | 51 | █████████ |
| Jan 2026 | 94 | 86% | 63 | 26 | ███ |
| Feb 2026 | 89 | 78% | 54 | 29 | ███ |
| Mar 2026 | 95 | 72% | 47 | 43 | ████ |
| Apr 2026 | 109 | 78% | 73 | 31 | ████ |

The last four complete months averaged 97 articles a month against 254 in the first four (-62%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 57% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 171 | 44% |
| Israel | 20 | 5.2% |
| United States | 11 | 2.8% |
| Nigeria | 3 | 0.8% |
| Bangladesh | 2 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| religious laws and governance | 30 | 15% | -81% |
| religion and politics | 50 | 24% | -77% |
| religious persecution and freedom | 19 | 9.3% | -17% |
| religious conflicts and resolutions | 35 | 17% | -47% |
| endowment funds for social good | 5 | 2.4% | +400% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [NHRC Notices on Bhopal Waqf Mismanagement in Mecca, Medina](https://www.newkerala.com/news/a/nhrc-takes-cognisance-bhopal-waqf-properties-mismanagement-mecca-345.htm) | newkerala.com | 8 | negative |
| 14 Apr 2026 | [NHRC seeks reports from MP govt, MEA over alleged irregularities in Bhopal Waqf properties in Mecca-Medina](https://www.thehansindia.com/news/national/nhrc-seeks-reports-from-mp-govt-mea-over-alleged-irregularities-in-bhopal-waqf-properties-in-mecca-medina-1065647) | thehansindia.com | 8 | negative |
| 13 Apr 2026 | [Hundreds of Israeli settlers storm Al-Aqsa Mosque under police protection](https://www.dailysabah.com/world/mid-east/hundreds-of-israeli-settlers-storm-al-aqsa-mosque-under-police-protection) | dailysabah.com | 8 | negative |
| 10 Apr 2026 | [South India Dargah Mosque Association Supports AIADMK-NDA](https://www.newkerala.com/news/a/south-india-dargah-mosque-association-extends-support-aiadmk-nda-152.htm) | newkerala.com | 8 | negative |
| 7 Apr 2026 | [Supreme Court Daily Round-Up : April 7, 2026](https://www.livelaw.in/supreme-court/supreme-court-daily-round-up-april-7-2026-529418) | livelaw.in | 8 | negative |
| 31 Mar 2026 | [Munambam Waqf issue sparks local heat, Assembly polls impact uncertain](https://www.newindianexpress.com/states/kerala/2026/Mar/31/munambam-waqf-issue-sparks-local-heat-statewide-effect-uncertain) | newindianexpress.com | 8 | negative |
| 20 Mar 2026 | [India dismisses UN rapporteur’s report on Waqf law as false](https://telanganatoday.com/india-dismisses-un-rapporteurs-report-on-waqf-law-as-false) | telanganatoday.com | 8 | negative |
| 17 Mar 2026 | [Waqf Land Row in Karnataka: Majority of encroachers are Islamists](https://organiser.org/2026/03/17/344469/bharat/waqf-land-row-in-karnataka-minister-zameer-ahmed-claims-majority-of-encroachers-are-islamists/) | organiser.org | 8 | negative |
| 28 Feb 2026 | [What Is 'Waqf By User' & Why Is It A Scary Concept](https://edtimes.in/what-is-waqf-by-user-why-is-it-a-scary-concept/) | edtimes.in | 8 | negative |
| 11 Feb 2026 | [Delhi High Court issues notice to DDA in Shahi Idgah's plea](https://www.aninews.in/news/national/general-news/delhi-high-court-issues-notice-to-dda-in-shahi-idgahs-plea20260211220309) | aninews.in | 8 | negative |
| 31 Jan 2026 | [Left, right and Waqf: Secularism, reform and the 'double standards' debate at MBIFL 2026](https://english.mathrubhumi.com/features/mbifl-2026/left-right-waqf-secularism-reform-mbifl-2026-rwv44std) | english.mathrubhumi.com | 8 | negative |
| 28 Jan 2026 | [Jagan Pledges to Safeguard Waqf Lands](https://www.deccanchronicle.com/southern-states/andhra-pradesh/jagan-pledges-to-safeguard-waqf-lands-1933347) | deccanchronicle.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "waqf" --since 2026-01-01 --until 2026-04-30
prism-news trends "waqf" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "waqf" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "waqf", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "waqf", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Capital Gains Tax News](capital-gains-tax-news.md)
- [Antitrust News](antitrust-news.md)
- [Minimum Wage News](minimum-wage-news.md)
- [GDPR News](gdpr-news.md)
