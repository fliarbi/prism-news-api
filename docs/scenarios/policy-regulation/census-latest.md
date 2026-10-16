# Census Latest News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “census latest” · 320/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [census-latest.json](../../examples/scenarios/census-latest.json).

**Question.** How did coverage of census develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="census"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,051 |
| Negative · neutral · positive | 40% · 10% · 50% |
| Critical (priority 7–9) | 54% (4,877 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (4,294 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | government census and demographic data |

## Twelve months of coverage

Monthly matching articles for `census` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,766 | 53% | 1,365 | 1,142 | █████████████ |
| Jun 2025 | 1,637 | 54% | 765 | 684 | ████████ |
| Jul 2025 | 2,782 | 51% | 1,666 | 997 | █████████████ |
| Aug 2025 | 4,294 | 62% | 2,743 | 1,353 | ████████████████████ |
| Sep 2025 | 2,211 | 69% | 1,371 | 713 | ██████████ |
| Oct 2025 | 1,360 | 60% | 717 | 558 | ██████ |
| Nov 2025 | 1,337 | 56% | 644 | 576 | ██████ |
| Dec 2025 | 1,238 | 59% | 570 | 563 | ██████ |
| Jan 2026 | 1,219 | 58% | 536 | 551 | ██████ |
| Feb 2026 | 1,765 | 58% | 864 | 758 | ████████ |
| Mar 2026 | 1,964 | 52% | 753 | 998 | █████████ |
| Apr 2026 | 4,103 | 52% | 1,490 | 2,173 | ███████████████████ |

The last four complete months averaged 2,263 articles a month against 2,870 in the first four (-21%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,363 | 26% |
| India | 1,809 | 20% |
| China | 83 | 0.9% |
| United Kingdom | 71 | 0.8% |
| Cameroon | 58 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| government census and demographic data | 866 | 17% | +212% |
| census methodology and data collection techniques | 195 | 3.9% | +65% |
| government public records management | 667 | 13% | +290% |
| internal migration and regional population shifts | 108 | 2.2% | +192% |
| migration patterns and immigration rates | 94 | 1.9% | +141% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 9 Apr 2026 | [Stats Show Trump's Immigration Policies Are Doing Very Real and Long Term Damage to the Political Power of…](https://www.thegatewaypundit.com/2026/04/stats-show-trumps-immigration-policies-are-doing-very/) ⚠ | thegatewaypundit.com | 9 | negative |
| 9 Jan 2026 | [Bangladesh’s street children battle cold, hunger and neglect](https://www.dhakatribune.com/bangladesh/400664/bangladesh%E2%80%99s-street-children-battle-cold-hunger) | dhakatribune.com | 9 | negative |
| 29 Apr 2026 | ['National initiative shaping India's future': Rajasthan CM on Census 2027](https://www.aninews.in/news/national/general-news/national-initiative-shaping-indias-future-rajasthan-cm-on-census-202720260429163542) | aninews.in | 8 | positive |
| 29 Apr 2026 | [Rajasthan Census 2027 self-enumeration begins May 1, 2026](https://thenewsmill.com/2026/04/rajasthan-to-begin-census-2027-with-self-enumeration-in-may/) | thenewsmill.com | 8 | positive |
| 27 Apr 2026 | [MP Congress Chief Jitu Patwari Demands Women's Reservation](https://www.newkerala.com/news/a/bjp-should-implement-womens-reservation-existing-seats-mp-364.htm) | newkerala.com | 8 | positive |
| 27 Apr 2026 | [Two Teachers on Census Duty Die of Suspected Heatstroke in Odisha Within Two Days](https://www.thebridgechronicle.com/news/odisha-teachers-census-duty-heatstroke-deaths-mp99) | thebridgechronicle.com | 8 | negative |
| 27 Apr 2026 | [Two Odisha Teachers Die Of Suspected Sunstroke In 2 Days During Census 2027 Fieldwork](https://odishabytes.com/two-odisha-teachers-die-of-suspected-sunstroke-in-2-days-during-census-2027-fieldwork/) | odishabytes.com | 8 | negative |
| 26 Apr 2026 | [Census 2027: Telangana CM Registers for Self-Enumeration](https://www.newkerala.com/news/a/telangana-cm-registers-details-under-census-2027-self-enumeration-727.htm) | newkerala.com | 8 | positive |
| 26 Apr 2026 | [Mann Ki Baat Best Learning Platform: Delhi BJP Chief](https://www.newkerala.com/news/a/no-better-platform-learning-than-mann-ki-baat-175.htm) | newkerala.com | 8 | positive |
| 26 Apr 2026 | [Interactive map shows how vulnerable your neighborhood is to disaster](https://www.wkrn.com/news/national/interactive-map-shows-how-vulnerable-your-neighborhood-is-to-disaster/) | wkrn.com | 8 | negative |
| 26 Apr 2026 | [Pradhan Attends PM Modi’s Mann Ki Baat in Odisha Village](https://www.newkerala.com/news/a/dharmendra-pradhan-listens-pm-narendra-modis-mann-ki-343.htm) | newkerala.com | 8 | positive |
| 26 Apr 2026 | [PM Modi Urges Participation in Digital Census 2027](https://www.newkerala.com/news/a/pm-modi-urges-citizens-participate-census-2027-calls-894.htm) | newkerala.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "census" --since 2026-01-01 --until 2026-04-30
prism-news trends "census" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "census" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "census", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "census", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [FSSAI News](fssai-news.md)
- [Brexit News](brexit-news.md)
- [Capital Gains Tax News](capital-gains-tax-news.md)
- [Antitrust News](antitrust-news.md)
