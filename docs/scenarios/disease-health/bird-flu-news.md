# Bird Flu News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bird flu news” · 2,900/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [bird-flu-news.json](../../examples/scenarios/bird-flu-news.json).

**Question.** How much bird flu coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="bird flu"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 807 |
| Negative · neutral · positive | 85% · 0.2% · 15% |
| Critical (priority 7–9) | 83% (667 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (522 articles) |
| Most-reported country | United States (24% of matches) |
| Strongest theme by lift | emerging zoonotic viruses |

## Twelve months of coverage

Monthly matching articles for `bird flu` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 522 | 80% | 419 | 86 | ████████████████████ |
| Jun 2025 | 163 | 83% | 138 | 25 | ██████ |
| Jul 2025 | 321 | 68% | 292 | 27 | ████████████ |
| Aug 2025 | 280 | 80% | 235 | 39 | ███████████ |
| Sep 2025 | 153 | 86% | 135 | 17 | ██████ |
| Oct 2025 | 241 | 67% | 220 | 16 | █████████ |
| Nov 2025 | 425 | 84% | 388 | 35 | ████████████████ |
| Dec 2025 | 185 | 81% | 155 | 29 | ███████ |
| Jan 2026 | 152 | 87% | 133 | 19 | ██████ |
| Feb 2026 | 288 | 83% | 255 | 32 | ███████████ |
| Mar 2026 | 209 | 81% | 171 | 37 | ████████ |
| Apr 2026 | 158 | 80% | 125 | 33 | ██████ |

The last four complete months averaged 202 articles a month against 322 in the first four (-37%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 190 | 24% |
| India | 122 | 15% |
| United Kingdom | 36 | 4.5% |
| Nepal | 12 | 1.5% |
| Australia | 11 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| emerging zoonotic viruses | 278 | 44% | -8% |
| zoonotic disease transmission pathways | 347 | 55% | -24% |
| one health approaches | 214 | 34% | +10% |
| poultry farming & production | 78 | 12% | -42% |
| livestock biosecurity measures | 56 | 8.8% | +195% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Mar 2026 | [Scientists concerned about transmission of bird flu to cows](https://www.pbssocal.org/shows/newshour/clip/bird-flu-1715810471) | pbssocal.org | 9 | negative |
| 25 Feb 2026 | [Pa. Governor Josh Shapiro discusses bird flu outbreak](https://www.yahoo.com/news/articles/pa-governor-josh-shapiro-discusses-000011565.html) | yahoo.com | 9 | negative |
| 30 Apr 2026 | [France reports two bird flu outbreaks after easing restrictions](https://www.yahoo.com/news/articles/france-reports-two-bird-flu-161221230.html) | yahoo.com | 8 | negative |
| 29 Apr 2026 | [Housing order for all poultry, captive birds to be lifted](https://www.rte.ie/news/2026/0429/1570879-housing-order-birds/) | rte.ie | 8 | negative |
| 27 Apr 2026 | [New H5N1 bird flu vaccine shows strong protection in animals, researchers say](https://www.openaccessgovernment.org/new-h5n1-bird-flu-vaccine-shows-strong-protection-in-animals-researchers-say/208727/) | openaccessgovernment.org | 8 | positive |
| 26 Apr 2026 | [भागलपुर में फैला बर्ड फ्लू, सरकारी पोल्ट्री फॉर्म बना एपिक सेंटर](https://www.livehindustan.com/bihar/bhagalpur/story-bird-flu-outbreak-confirmed-at-bhagalpur-poultry-center-h5n1-variant-detected-201777231303926.html) | livehindustan.com | 8 | negative |
| 25 Apr 2026 | [Bird Flu Outbreak Contained in Bengaluru, No Human Cases](https://www.newkerala.com/news/a/bird-flu-outbreak-contained-bengaluru-no-human-cases-624.htm) | newkerala.com | 8 | negative |
| 23 Apr 2026 | [China bans Chile poultry imports due to bird flu](https://www.yahoo.com/news/articles/china-bans-chile-poultry-imports-085451221.html) | yahoo.com | 8 | negative |
| 22 Apr 2026 | [Moderna, after losing US funding, rebounds to start mRNA bird flu vaccine trial](https://www.biopharmadive.com/news/moderna-mrna-bird-flu-vaccine-trial-cepi-hhs/818172/) | biopharmadive.com | 8 | positive |
| 22 Apr 2026 | [First bird flu mRNA vaccine enters late-stage trial - The Times of India](https://timesofindia.indiatimes.com/etimes/wellness/first-bird-flu-mrna-vaccine-enters-late-stage-trial/articleshow/130433005.cms) | timesofindia.indiatimes.com | 8 | positive |
| 22 Apr 2026 | [Moderna launches H5N1 bird flu vaccine trial in US and UK after HHS funding cut - Time News](https://time.news/moderna-launches-h5n1-bird-flu-vaccine-trial-in-us-and-uk-after-hhs-funding-cut/) | time.news | 8 | negative |
| 21 Apr 2026 | [Moderna starts late-stage trial of bird flu vaccine in US, UK](https://www.globalbankingandfinance.com/moderna-starts-late-stage-trial-bird-flu-vaccine-us-uk/) | globalbankingandfinance.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "bird flu" --since 2026-01-01 --until 2026-04-30
prism-news trends "bird flu" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "bird flu" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "bird flu", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "bird flu", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Influenza Outbreak](influenza-outbreak.md)
- [COVID News](covid-news.md)
- [HIV News](hiv-news.md)
- [E Coli Outbreak](e-coli-outbreak.md)
