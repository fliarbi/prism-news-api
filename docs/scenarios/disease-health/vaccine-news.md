# Vaccine News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “vaccine news” · 320/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [vaccine-news.json](../../examples/scenarios/vaccine-news.json).

**Question.** How much vaccine coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="vaccine"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,906 |
| Negative · neutral · positive | 44% · 1.8% · 54% |
| Critical (priority 7–9) | 86% (11,113 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (8,864 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | vaccine development and clinical trials |

## Twelve months of coverage

Monthly matching articles for `vaccine` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5,713 | 74% | 1,945 | 3,499 | █████████████ |
| Jun 2025 | 2,575 | 85% | 1,213 | 1,310 | ██████ |
| Jul 2025 | 3,933 | 70% | 1,957 | 1,917 | █████████ |
| Aug 2025 | 8,864 | 78% | 4,559 | 4,225 | ████████████████████ |
| Sep 2025 | 5,735 | 81% | 2,680 | 2,981 | █████████████ |
| Oct 2025 | 2,781 | 74% | 835 | 1,879 | ██████ |
| Nov 2025 | 2,307 | 83% | 830 | 1,430 | █████ |
| Dec 2025 | 4,193 | 85% | 1,750 | 2,303 | █████████ |
| Jan 2026 | 3,176 | 88% | 1,184 | 1,922 | ███████ |
| Feb 2026 | 3,491 | 86% | 1,599 | 1,829 | ████████ |
| Mar 2026 | 2,898 | 87% | 1,419 | 1,433 | ███████ |
| Apr 2026 | 3,341 | 84% | 1,462 | 1,804 | ████████ |

The last four complete months averaged 3,226 articles a month against 5,271 in the first four (-39%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 35% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,700 | 21% |
| India | 371 | 2.9% |
| United Kingdom | 278 | 2.1% |
| Australia | 116 | 0.9% |
| Canada | 104 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| vaccine development and clinical trials | 840 | 8.6% | +18% |
| covid-19 vaccine development and efficacy trials | 2,112 | 22% | -30% |
| vaccine mandates and policy debates | 609 | 6.2% | -42% |
| vaccine myths and misinformation countermeasures | 555 | 5.7% | -40% |
| covid-19 vaccination campaigns and rollout strategies | 1,381 | 14% | -31% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Letters: I survived polio. I want others to be spared that ordeal.](https://www.chicagotribune.com/2026/04/25/letters-042526-polio/) | chicagotribune.com | 9 | positive |
| 19 Apr 2026 | [Flu shots not helping many of us](https://lancasteronline.com/news/flu-shots-not-helping-many-of-us/article_0e0dc769-0727-5917-a33b-de60dd95a4a0.html) | lancasteronline.com | 9 | negative |
| 13 Apr 2026 | [Felt like I was dying: Musk backs insider who said Covid vaccine killed thousands](https://www.indiatoday.in/science/story/elon-musk-pfizer-toxicologist-covid-vaccine-bundestag-germany-60000-deaths-mrna-approval-2895204-2026-04-13) | indiatoday.in | 9 | negative |
| 5 Apr 2026 | [Bangladesh says suspected measles outbreak kills about 100 children](https://www.straitstimes.com/asia/south-asia/bangladesh-says-suspected-measles-outbreak-kills-about-100-children) | straitstimes.com | 9 | negative |
| 3 Apr 2026 | [WHO Sending 1.2 Million Polio Vaccines to Gaza as Israel Continues Its Genocidal War](https://www.democracynow.org/2024/8/8/headlines/who_sending_12_million_polio_vaccines_to_gaza_as_israel_continues_its_genocidal_war) | democracynow.org | 9 | negative |
| 13 Mar 2026 | [Shields and Brooks on inviting Netanyahu](https://www.pbssocal.org/shows/newshour/clip/shields-and-brooks-on-inviting-netanyahu-1429311841) | pbssocal.org | 9 | negative |
| 14 Jan 2026 | [NCDHHS: 63 flu-related deaths reported in one week](https://abc11.com/post/nc-flu-deaths-63-related-reported-week-according-ncdhhs/18403529/) | abc11.com | 9 | negative |
| 30 Apr 2026 | [Study projects hepatitis B vaccine delay could increase infections, deaths](https://triblive.com/news/world/study-projects-hepatitis-b-vaccine-delay-could-increase-infections-deaths/) | triblive.com | 8 | negative |
| 30 Apr 2026 | [Miranda Devine: The Biden admin’s COVID vaccine cover-up and lies can no longer be denied – or the damage…](https://nypost.com/2026/04/29/opinion/miranda-devine-the-biden-admins-covid-vaccine-cover-up-and-lies-can-no-longer-be-denied-or-the-damage-it-caused/) | nypost.com | 8 | negative |
| 30 Apr 2026 | [Trump administration appeals ruling that blocked RFK Jr.'s vaccine overhaul](https://www.yahoo.com/news/articles/trump-administration-appeals-ruling-blocked-004059111.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "vaccine" --since 2026-01-01 --until 2026-04-30
prism-news trends "vaccine" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "vaccine" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "vaccine", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "vaccine", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tuberculosis Outbreak](tuberculosis-outbreak.md)
- [Cholera Outbreak](cholera-outbreak.md)
- [Ozempic News](ozempic-news.md)
- [Polio Outbreak](polio-outbreak.md)
