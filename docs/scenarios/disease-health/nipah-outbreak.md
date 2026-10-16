# Nipah Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nipah outbreak” · 210/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nipah-outbreak.json](../../examples/scenarios/nipah-outbreak.json).

**Question.** How much nipah coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="nipah"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,288 |
| Negative · neutral · positive | 77% · 1.9% · 21% |
| Critical (priority 7–9) | 95% (1,219 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (798 articles) |
| Most-reported country | India (31% of matches) |
| Strongest theme by lift | zoonotic disease prevention measures |

## Twelve months of coverage

Monthly matching articles for `nipah` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 68 | 81% | 39 | 28 | ██ |
| Jun 2025 | 94 | 92% | 39 | 51 | ██ |
| Jul 2025 | 180 | 85% | 138 | 40 | █████ |
| Aug 2025 | 64 | 89% | 33 | 24 | ██ |
| Sep 2025 | 82 | 94% | 40 | 41 | ██ |
| Oct 2025 | 46 | 98% | 21 | 24 | █ |
| Nov 2025 | 49 | 92% | 10 | 39 | █ |
| Dec 2025 | 42 | 86% | 7 | 33 | █ |
| Jan 2026 | 798 | 96% | 666 | 120 | ████████████████████ |
| Feb 2026 | 357 | 93% | 272 | 74 | █████████ |
| Mar 2026 | 53 | 91% | 17 | 35 | █ |
| Apr 2026 | 80 | 91% | 35 | 44 | ██ |

The last four complete months averaged 322 articles a month against 102 in the first four (+217%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 54% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 398 | 31% |
| Singapore | 97 | 7.5% |
| United States | 55 | 4.3% |
| Malaysia | 23 | 1.8% |
| Bangladesh | 18 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| zoonotic disease prevention measures | 310 | 41% | +4329% |
| global health challenges | 137 | 18% | +3325% |
| infectious disease control strategies | 122 | 16% | +3967% |
| infectious disease outbreaks | 90 | 12% | new |
| covid-19 public health policies and lockdown measures | 77 | 10% | +7600% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Feb 2026 | [Nurse with Nipah dies of organ failure becoming 1st death of India outbreak](https://www.thescottishsun.co.uk/health/15917626/nurse-nipah-virus-death-india-outbreak/) | thescottishsun.co.uk | 9 | negative |
| 28 Jan 2026 | [REGION ON ALERT AS INDIA REPORTS NIPAH VIRUS CASES](https://www.pressreader.com/china/south-china-morning-post-6150/20260129/281818585251185) | pressreader.com | 9 | negative |
| 23 Apr 2026 | [China issues Nipah virus guideline, reports no human infections](http://www.chinadaily.com.cn/a/202604/23/WS69e9e4f9a310d6866eb4528f.html) | chinadaily.com.cn | 8 | negative |
| 2 Apr 2026 | [Superspreading potential of Nipah virus disease despite self-limited human-to-human transmission in community.](https://pubmed.ncbi.nlm.nih.gov/41935612/) | pubmed.ncbi.nlm.nih.gov | 8 | negative |
| 1 Apr 2026 | [A structure-based mRNA vaccine for Nipah virus in healthy adults: a phase 1 trial.](https://pubmed.ncbi.nlm.nih.gov/41820674/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 26 Mar 2026 | [Nipah virus could turn into something “far more severe”, scientists warn](https://www.thehindu.com/sci-tech/health/nipah-virus-could-turn-into-something-far-more-severe-scientists-warn/article70787067.ece) | thehindu.com | 8 | negative |
| 25 Mar 2026 | [When Viruses Attack The Brain: Understanding Nipah Virus And Its Life-Threatening Impact](https://news.abplive.com/health/abp-live-doc-talk-when-viruses-attack-the-brain-understanding-nipah-virus-and-its-life-threatening-impact-1832818) | news.abplive.com | 8 | negative |
| 24 Mar 2026 | [Creative Diagnostics Launches Comprehensive Portfolio of Nipah Virus Antigens and Antibodies to Support…](https://www.1888pressrelease.com/creative-diagnostics-launches-comprehensive-portfolio-of-nip-pr-764440.html) | 1888pressrelease.com | 8 | positive |
| 22 Mar 2026 | [Kerala: Alert issued against Nipah virus from April to September](https://www.thehindu.com/news/national/kerala/alert-issued-against-nipah-in-kerala-from-april-to-september/article70772258.ece) | thehindu.com | 8 | negative |
| 12 Mar 2026 | [Could vaccine-carrying mosquitoes slow the spread of deadly diseases?](https://www.yahoo.com/news/articles/could-vaccine-carrying-mosquitoes-slow-200054206.html) | yahoo.com | 8 | positive |
| 2 Mar 2026 | [Nipah and mpox show Asia’s need for disease surveillan­ce](https://www.pressreader.com/china/south-china-morning-post-6150/20260303/281844355121972) | pressreader.com | 8 | negative |
| 2 Mar 2026 | [Why Colorado joined a global network to learn about infectious disease outbreaks in other countries](https://coloradosun.com/2026/03/02/who-global-outbreak-alert-response-network/) | coloradosun.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "nipah" --since 2026-01-01 --until 2026-04-30
prism-news trends "nipah" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "nipah" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "nipah", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "nipah", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Ozempic News](ozempic-news.md)
- [Polio Outbreak](polio-outbreak.md)
- [Rabies Outbreak](rabies-outbreak.md)
- [Mpox Outbreak](mpox-outbreak.md)
