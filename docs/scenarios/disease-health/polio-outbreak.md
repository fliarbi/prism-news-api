# Polio Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “polio outbreak” · 50/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [polio-outbreak.json](../../examples/scenarios/polio-outbreak.json).

**Question.** How much polio coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="polio"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 733 |
| Negative · neutral · positive | 50% · 2.5% · 48% |
| Critical (priority 7–9) | 86% (627 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (326 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | global vaccination campaigns (e.g., who, unicef) |

## Twelve months of coverage

Monthly matching articles for `polio` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 294 | 77% | 149 | 126 | ██████████████████ |
| Jun 2025 | 155 | 88% | 92 | 58 | ██████████ |
| Jul 2025 | 193 | 69% | 120 | 72 | ████████████ |
| Aug 2025 | 267 | 82% | 188 | 71 | ████████████████ |
| Sep 2025 | 326 | 91% | 228 | 95 | ████████████████████ |
| Oct 2025 | 239 | 87% | 102 | 130 | ███████████████ |
| Nov 2025 | 120 | 90% | 58 | 60 | ███████ |
| Dec 2025 | 263 | 78% | 65 | 193 | ████████████████ |
| Jan 2026 | 117 | 83% | 56 | 52 | ███████ |
| Feb 2026 | 232 | 91% | 120 | 105 | ██████████████ |
| Mar 2026 | 152 | 84% | 70 | 79 | █████████ |
| Apr 2026 | 232 | 82% | 116 | 110 | ██████████████ |

The last four complete months averaged 183 articles a month against 227 in the first four (-19%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 186 | 25% |
| Pakistan | 38 | 5.2% |
| India | 34 | 4.6% |
| Nigeria | 29 | 4.0% |
| United Kingdom | 12 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| global vaccination campaigns (e.g., who, unicef) | 79 | 17% | -50% |
| vaccine equity and access in low-income regions | 49 | 11% | -9% |
| vaccine distribution and cold chain logistics | 36 | 7.9% | +56% |
| vaccine myths and misinformation countermeasures | 35 | 7.7% | -22% |
| historical perspectives on vaccine development | 32 | 7.0% | +129% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Formula 1 driver Romain Grosjean partners with GPEI to ‘finish the race’ against Polio for World…](https://sportsz.news/news/formula-1-driver-romain-grosjean-partners-with-gpei-to-finish-the-race-against-polio-for-world-immunisation-week/) | sportsz.news | 9 | positive |
| 29 Apr 2026 | [Formula 1 driver Romain Grosjean partners with GPEI to ‘finish the race’ against Polio for World…](https://onlinemediacafe.com/news/formula-1-driver-romain-grosjean-partners-with-gpei-to-finish-the-race-against-polio-for-world-immunisation-week/) | onlinemediacafe.com | 9 | positive |
| 29 Apr 2026 | [Formula 1 driver Romain Grosjean partners with GPEI to ‘finish the race’ against Polio for World…](https://mediabulletins.com/news/formula-1-driver-romain-grosjean-partners-with-gpei-to-finish-the-race-against-polio-for-world-immunisation-week/) | mediabulletins.com | 9 | positive |
| 25 Apr 2026 | [Letters: I survived polio. I want others to be spared that ordeal.](https://www.chicagotribune.com/2026/04/25/letters-042526-polio/) | chicagotribune.com | 9 | positive |
| 17 Apr 2026 | [The Victorian-era disease that 'hasn't disappeared' from England](https://www.manchestereveningnews.co.uk/news/greater-manchester-news/victorian-era-disease-hasnt-disappeared-33787059) | manchestereveningnews.co.uk | 9 | negative |
| 17 Apr 2026 | [Polio team threatened in Pakistan, case registered \| Indiablooms - First Portal on Digital News Management](https://www.indiablooms.com/world/polio-team-threatened-in-pakistan-case-registered/details) | indiablooms.com | 9 | negative |
| 15 Apr 2026 | [Courage Amidst Conflict: Pakistan's Polio Battleground \| Law-Order](https://www.devdiscourse.com/article/law-order/3875184-courage-amidst-conflict-pakistans-polio-battleground) | devdiscourse.com | 9 | negative |
| 14 Apr 2026 | [No polio case reported in Balochistan during last 15 months](https://www.24newshd.tv/14-Apr-2026/polio-case-reported-balochistan-last-15-months) | 24newshd.tv | 9 | positive |
| 13 Apr 2026 | [Suspected militants kill police officer assigned to guard polio team](https://abcnews.com/International/wireStory/suspected-militants-kill-police-officer-assigned-guard-polio-131984411) | abcnews.com | 9 | negative |
| 13 Apr 2026 | [Tragedy Strikes: Militants Target Polio Vaccination Team in Pakistan \| Health](https://www.devdiscourse.com/article/health/3872059-tragedy-strikes-militants-target-polio-vaccination-team-in-pakistan) | devdiscourse.com | 9 | negative |
| 13 Apr 2026 | [Policeman martyred, four hurt in Hangu attack on polio security team](https://www.24newshd.tv/13-Apr-2026/policeman-martyred-four-hurt-hangu-attack-polio-security-team) | 24newshd.tv | 9 | negative |
| 3 Apr 2026 | [WHO Sending 1.2 Million Polio Vaccines to Gaza as Israel Continues Its Genocidal War](https://www.democracynow.org/2024/8/8/headlines/who_sending_12_million_polio_vaccines_to_gaza_as_israel_continues_its_genocidal_war) | democracynow.org | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "polio" --since 2026-01-01 --until 2026-04-30
prism-news trends "polio" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "polio" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "polio", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "polio", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Vaccine News](vaccine-news.md)
- [Ozempic News](ozempic-news.md)
- [Nipah Outbreak](nipah-outbreak.md)
- [Rabies Outbreak](rabies-outbreak.md)
