# Gun Control News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gun control news” · 10/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gun-control-news.json](../../examples/scenarios/gun-control-news.json).

**Question.** How did coverage of gun control develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="gun control"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 658 |
| Negative · neutral · positive | 79% · 2.3% · 19% |
| Critical (priority 7–9) | 82% (542 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (606 articles) |
| Most-reported country | United States (33% of matches) |
| Strongest theme by lift | assault weapon legislation and debates |

## Twelve months of coverage

Monthly matching articles for `gun control` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 102 | 64% | 74 | 26 | ███ |
| Jun 2025 | 97 | 69% | 77 | 18 | ███ |
| Jul 2025 | 204 | 58% | 164 | 35 | ███████ |
| Aug 2025 | 606 | 73% | 526 | 76 | ████████████████████ |
| Sep 2025 | 210 | 85% | 183 | 24 | ███████ |
| Oct 2025 | 116 | 86% | 94 | 22 | ████ |
| Nov 2025 | 94 | 81% | 71 | 20 | ███ |
| Dec 2025 | 201 | 88% | 177 | 19 | ███████ |
| Jan 2026 | 135 | 84% | 108 | 24 | ████ |
| Feb 2026 | 157 | 82% | 123 | 30 | █████ |
| Mar 2026 | 149 | 86% | 123 | 23 | █████ |
| Apr 2026 | 217 | 80% | 165 | 46 | ███████ |

The last four complete months averaged 164 articles a month against 252 in the first four (-35%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 45% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 216 | 33% |
| Australia | 34 | 5.2% |
| Canada | 17 | 2.6% |
| India | 6 | 0.9% |
| China | 4 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| assault weapon legislation and debates | 40 | 9.4% | -32% |
| firearm ownership laws and regulations | 99 | 23% | -38% |
| firearm accessories and modifications | 24 | 5.6% | +85% |
| concealed carry permits and policies | 43 | 10% | +16% |
| 3d-printed firearms and legality | 17 | 4.0% | +183% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 11 Feb 2026 | [Canada school shooting updates: 9 dead, 27 wounded in BC’s Tumbler Ridge](http://www.aljazeera.com/news/liveblog/2026/2/11/canada-school-shooting-live-10-dead-in-british-columbias-tumbler-ridge) | aljazeera.com | 9 | negative |
| 29 Apr 2026 | [Justice Department moves to roll back gun regulations as Senate confirms new ATF chief](https://www.sandiegouniontribune.com/2026/04/29/justice-department-gun-regulation-roll-back/) | sandiegouniontribune.com | 8 | negative |
| 29 Apr 2026 | [WATCH: Blanche, newly confirmed ATF head Cekada propose gun regulation rollbacks](https://www.pbs.org/newshour/politics/watch-blanche-newly-confirmed-atf-head-cekada-propose-gun-regulation-rollbacks) | pbs.org | 8 | negative |
| 29 Apr 2026 | [In the wake of Cole Tomas Allen’s alleged attempt to assassinate US President Donald Trump and/or other…](https://www.counterpunch.org/2026/04/29/ok-gun-control-had-its-chance-here-are-the-results/print/) | counterpunch.org | 8 | negative |
| 21 Apr 2026 | [Forbes slammed for asking readers to play odds on gun control in mass shooting story: ‘Gross, evil, ghoulish’](https://www.yahoo.com/news/articles/forbes-slammed-asking-readers-play-162439110.html) | yahoo.com | 8 | negative |
| 9 Apr 2026 | [Key Gun Control Bills Advance in Virginia as Firearm Sales Surge](https://rvamag.com/politics/virginia-politics/key-gun-control-bills-advance-in-virginia-as-firearm-sales-surge.html) | rvamag.com | 8 | positive |
| 3 Apr 2026 | [Congress MLA Jagdish Singh Sentenced to 3 Years in School Funds Misuse Case - The CSR Journal](https://thecsrjournal.in/congress-mla-jagdish-singh-sentenced-to-3-years-in-school-funds-misuse-case/) | thecsrjournal.in | 8 | negative |
| 3 Apr 2026 | [K. Kavitha Criticises Congress Over Cancellation of Handloom Orders - The CSR Journal](https://thecsrjournal.in/k-kavitha-criticises-congress-over-cancellation-of-handloom-orders/) | thecsrjournal.in | 8 | negative |
| 2 Apr 2026 | [Himachal Pradesh Assembly Approves Bill to Deny Pension to Disqualified MLAs - The CSR Journal](https://thecsrjournal.in/himachal-pradesh-assembly-approves-bill-to-deny-pension-to-disqualified-mlas/) | thecsrjournal.in | 8 | negative |
| 12 Mar 2026 | [Gun Control's Endgame: No Guns for Anyone](https://www.yahoo.com/news/articles/gun-controls-endgame-no-guns-104833433.html) | yahoo.com | 8 | negative |
| 9 Mar 2026 | [Why Gavin Newsom’s own gun laws complicate his ‘fabulous’ gift from podcaster Shawn Ryan](https://us.headtopics.com/news/why-gavin-newsom-s-own-gun-laws-complicate-his-fabulous-80729934) | us.headtopics.com | 8 | negative |
| 24 Feb 2026 | [New Mexico’s 2026 Gun Control Push Stalled, but the Overreach Will Return](https://www.nssf.org/articles/new-mexicos-2026-gun-control-push-stalled-but-the-overreach-will-return/) | nssf.org | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "gun control" --since 2026-01-01 --until 2026-04-30
prism-news trends "gun control" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "gun control" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "gun control", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "gun control", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Minimum Wage News](minimum-wage-news.md)
- [GDPR News](gdpr-news.md)
- [Uniform Civil Code News](uniform-civil-code-news.md)
- [Stablecoin Regulation News](stablecoin-regulation-news.md)
