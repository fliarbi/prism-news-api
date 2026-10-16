# Pandemic News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pandemic news” · 110/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [pandemic-news.json](../../examples/scenarios/pandemic-news.json).

**Question.** How much pandemic coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="pandemic"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 21,747 |
| Negative · neutral · positive | 51% · 3.1% · 46% |
| Critical (priority 7–9) | 67% (14,542 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (22,752 articles) |
| Most-reported country | United States (20% of matches) |
| Strongest theme by lift | covid-19 public health policies and lockdown measures |

## Twelve months of coverage

Monthly matching articles for `pandemic` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 11,303 | 62% | 6,114 | 4,556 | ██████████ |
| Jun 2025 | 4,668 | 63% | 2,370 | 2,072 | ████ |
| Jul 2025 | 10,001 | 51% | 5,867 | 3,939 | █████████ |
| Aug 2025 | 22,752 | 59% | 13,662 | 8,717 | ████████████████████ |
| Sep 2025 | 5,330 | 66% | 2,615 | 2,507 | █████ |
| Oct 2025 | 4,266 | 66% | 1,931 | 2,170 | ████ |
| Nov 2025 | 4,396 | 65% | 2,116 | 2,126 | ████ |
| Dec 2025 | 4,998 | 70% | 2,487 | 2,358 | ████ |
| Jan 2026 | 5,240 | 68% | 2,501 | 2,532 | █████ |
| Feb 2026 | 5,330 | 67% | 2,597 | 2,590 | █████ |
| Mar 2026 | 5,340 | 66% | 2,886 | 2,268 | █████ |
| Apr 2026 | 5,837 | 66% | 3,119 | 2,542 | █████ |

The last four complete months averaged 5,437 articles a month against 12,181 in the first four (-55%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,268 | 20% |
| India | 713 | 3.3% |
| United Kingdom | 638 | 2.9% |
| China | 314 | 1.4% |
| Canada | 230 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| covid-19 public health policies and lockdown measures | 1,123 | 8.7% | +20% |
| covid-19 mental health impact and pandemic-related stress | 1,094 | 8.5% | +6% |
| covid-19 epidemiology and transmission modeling | 307 | 2.4% | +5% |
| covid-19 long-term effects (long covid) and complications | 299 | 2.3% | -7% |
| covid-19 variants (alpha, delta, omicron) and mutations | 280 | 2.2% | -10% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Lorraine Kelly admits 'I burst into tears' as she addresses 'false' diagnosis](https://www.mirror.co.uk/3am/celebrity-news/lorraine-kelly-admits-i-burst-37074394) | mirror.co.uk | 9 | negative |
| 8 Apr 2026 | [Italy’s coronavirus deaths soar to over 1,800 with nearly 25k infected](http://www.rt.com/newsline/483187-italys-coronavirus-deaths-record/) | rt.com | 9 | negative |
| 24 Mar 2026 | [Five Plead Guilty in $14.6M Fraud Diverting Funds Intended for Child Nutrition Funds](https://www.ibtimes.co.uk/five-plead-guilty-146m-fraud-diverting-funds-intended-child-nutrition-funds-1788023) | ibtimes.co.uk | 9 | negative |
| 19 Mar 2026 | [Covid-19 Inquiry verdict today amid warning UK is unprepared for next pandemic](https://www.mirror.co.uk/news/health/covid-19-inquiry-gives-verdict-36887360) | mirror.co.uk | 9 | negative |
| 18 Mar 2026 | [COVID-19 death toll in early days of the pandemic undercounted by over 150K: study](https://us.headtopics.com/news/covid-19-death-toll-in-early-days-of-the-pandemic-81163043) | us.headtopics.com | 9 | negative |
| 18 Mar 2026 | [COVID probably killed 150,000 more people in its first two years than official U.S. tolls show](https://www.yahoo.com/news/articles/covid-probably-killed-150-000-180000951.html) | yahoo.com | 9 | negative |
| 13 Mar 2026 | [Americans reflect on hardship and loss from the pandemic](https://www.pbssocal.org/shows/newshour/clip/1-million-lives-tape-1652389963) | pbssocal.org | 9 | negative |
| 13 Mar 2026 | [How the pandemic made housing inequality worse](https://www.pbssocal.org/shows/newshour/clip/rising-rents-1626382104) | pbssocal.org | 9 | negative |
| 12 Mar 2026 | [ADHD medication shortage strains patients and families](https://www.pbssocal.org/shows/newshour/clip/adhd-drug-shortage-1698700721) | pbssocal.org | 9 | negative |
| 12 Mar 2026 | [COVID-19 vaccines and children: What you need to know](https://www.pbssocal.org/shows/newshour/clip/covid-19-vaccines-and-children-what-you-need-to-know-1638040761) | pbssocal.org | 9 | negative |
| 12 Mar 2026 | [Colombia protests enter week three as violence escalates](https://www.pbssocal.org/shows/newshour/clip/colombia-protests-enter-week-three-as-violence-escalates-1621191964) | pbssocal.org | 9 | negative |
| 11 Mar 2026 | [Three SC men indicted for ‘millions’ of thefts in flawed COVID testing scheme](https://www.yahoo.com/news/articles/three-sc-men-indicted-millions-172350205.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "pandemic" --since 2026-01-01 --until 2026-04-30
prism-news trends "pandemic" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "pandemic" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "pandemic", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "pandemic", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Whooping Cough Outbreak](whooping-cough-outbreak.md)
- [Chikungunya Outbreak](chikungunya-outbreak.md)
- [ADHD News](adhd-news.md)
- [Gene Therapy News](gene-therapy-news.md)
