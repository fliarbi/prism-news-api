# Data Breach News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “data breach news” · 590/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [data-breach-news.json](../../examples/scenarios/data-breach-news.json).

**Question.** How much data breach coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="data breach"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,669 |
| Negative · neutral · positive | 78% · 0.5% · 21% |
| Critical (priority 7–9) | 87% (5,823 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,024 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | data breach notification systems |

## Twelve months of coverage

Monthly matching articles for `data breach` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,721 | 86% | 1,370 | 342 | █████████████████ |
| Jun 2025 | 1,268 | 84% | 969 | 298 | █████████████ |
| Jul 2025 | 1,706 | 76% | 1,343 | 360 | █████████████████ |
| Aug 2025 | 1,719 | 82% | 1,349 | 357 | █████████████████ |
| Sep 2025 | 1,393 | 88% | 1,081 | 302 | ██████████████ |
| Oct 2025 | 1,552 | 85% | 1,143 | 403 | ███████████████ |
| Nov 2025 | 1,324 | 86% | 938 | 381 | █████████████ |
| Dec 2025 | 1,505 | 86% | 1,168 | 330 | ███████████████ |
| Jan 2026 | 1,334 | 89% | 1,044 | 284 | █████████████ |
| Feb 2026 | 1,825 | 85% | 1,360 | 444 | ██████████████████ |
| Mar 2026 | 1,486 | 86% | 1,163 | 316 | ███████████████ |
| Apr 2026 | 2,024 | 89% | 1,647 | 366 | ████████████████████ |

The last four complete months averaged 1,667 articles a month against 1,604 in the first four (+4%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 40% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,215 | 18% |
| United Kingdom | 252 | 3.8% |
| India | 150 | 2.2% |
| South Korea | 95 | 1.4% |
| New Zealand | 94 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| data breach notification systems | 209 | 5.8% | -10% |
| data loss prevention (dlp) in networks | 308 | 8.6% | +38% |
| threat intelligence integration for networks | 269 | 7.5% | +74% |
| network security policy development and enforcement | 152 | 4.2% | +42% |
| malware and threat analysis in network traffic | 209 | 5.8% | +42% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Texas University Discloses Colossal Data Breach – Personal, Health and Financial Info of 813,892 People…](https://dailyhodl.com/2026/04/28/texas-university-discloses-colossal-data-breach-personal-health-and-financial-info-of-813892-people-exposed/) | dailyhodl.com | 9 | negative |
| 10 Apr 2026 | [China’s Tianjin Supercomputing Center Hit in Alleged 10-Petabyte Data Breach - Vision Times](https://www.visiontimes.com/2026/04/10/chinas-tianjin-supercomputing-center-hit-in-alleged-10-petabyte-data-breach.html) | visiontimes.com | 9 | negative |
| 9 Apr 2026 | [Chinese government hit by one of the biggest hacking attack as data from national Supercomputer allegedly…](https://timesofindia.indiatimes.com/technology/tech-news/chinese-government-hit-by-one-of-the-biggest-hacking-attack-as-data-from-national-supercomputer-allegedly-stolen/articleshow/130148924.cms) | timesofindia.indiatimes.com | 9 | negative |
| 9 Apr 2026 | [Chinese government hit by one of the biggest hacking attack as data from national Supercomputer allegedly…](https://timesofindia.indiatimes.com/articleshowprint/130148924.cms) | timesofindia.indiatimes.com | 9 | negative |
| 2 Apr 2026 | [Telehealth giant Hims & Hers says its customer support system was hacked \| TechCrunch](https://techcrunch.com/2026/04/02/telehealth-giant-hims-hers-says-its-customer-support-system-was-hacked/) | techcrunch.com | 9 | negative |
| 4 Mar 2026 | [LexisNexis confirms data breach, says hackers hit customer, business info](https://www.techradar.com/pro/security/lexisnexis-confirms-data-breach-says-hackers-hit-customer-and-business-info) | techradar.com | 9 | negative |
| 26 Feb 2026 | [PRIVACY ALERT: CatalystRCM Under Investigation for Data Breach of More Than 139,000 Records](https://www.prnewswire.com/news-releases/privacy-alert-catalystrcm-under-investigation-for-data-breach-of-more-than-139-000-records-302698947.html) | prnewswire.com | 9 | negative |
| 17 Feb 2026 | [Kettering Health Notifying Patients of Interlock Breach](https://www.bankinfosecurity.com/kettering-health-notifying-patients-interlock-breach-a-30774) | bankinfosecurity.com | 9 | negative |
| 10 Feb 2026 | [Data breach that went unnoticed in October 2024 may have left millions of Americans vulnerable](https://marketrealist.com/25-million-americans-affected-by-data-breach-from-2024/) | marketrealist.com | 9 | negative |
| 8 Feb 2026 | [Last chance for Americans to get up to $2,500 check from $500k data breach suit](https://www.the-sun.com/money/15907713/americans-2500-check-data-breach-payout-submit-form/) | the-sun.com | 9 | negative |
| 20 Jan 2026 | [Ingram Micro data breach affects 42,000 individuals](https://www.techzine.eu/news/security/138091/ingram-micro-data-breach-affects-42000-individuals/) | techzine.eu | 9 | negative |
| 19 Jan 2026 | [Grubhub Confirms New Data Breach, Hackers Reportedly Demand Ransom](https://www.pcmag.com/news/grubhub-confirms-new-data-breach-hackers-reportedly-demand-ransom) | pcmag.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "data breach" --since 2026-01-01 --until 2026-04-30
prism-news trends "data breach" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "data breach" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "data breach", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "data breach", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Virtual Reality News](virtual-reality-news.md)
- [Android News](android-news.md)
- [Generative AI News](generative-ai-news.md)
- [Esports News](esports-news.md)
