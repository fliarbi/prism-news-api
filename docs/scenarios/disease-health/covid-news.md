# COVID News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “covid news” · 3,600/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [covid-news.json](../../examples/scenarios/covid-news.json).

**Question.** How much covid coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="COVID"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 45,178 |
| Negative · neutral · positive | 51% · 2.5% · 47% |
| Critical (priority 7–9) | 66% (29,857 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (52,355 articles) |
| Most-reported country | United States (26% of matches) |
| Strongest theme by lift | covid-19 public health policies and lockdown measures |

## Twelve months of coverage

Monthly matching articles for `COVID` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 21,428 | 65% | 11,290 | 8,890 | ████████ |
| Jun 2025 | 9,622 | 65% | 5,027 | 4,289 | ████ |
| Jul 2025 | 17,562 | 53% | 10,383 | 6,763 | ███████ |
| Aug 2025 | 52,355 | 63% | 31,216 | 20,383 | ████████████████████ |
| Sep 2025 | 13,676 | 69% | 7,205 | 6,128 | █████ |
| Oct 2025 | 9,339 | 66% | 4,330 | 4,707 | ████ |
| Nov 2025 | 8,744 | 64% | 4,136 | 4,361 | ███ |
| Dec 2025 | 10,714 | 69% | 5,374 | 5,009 | ████ |
| Jan 2026 | 9,243 | 67% | 4,158 | 4,734 | ████ |
| Feb 2026 | 11,261 | 64% | 5,337 | 5,649 | ████ |
| Mar 2026 | 12,157 | 66% | 6,638 | 5,195 | █████ |
| Apr 2026 | 12,517 | 67% | 6,856 | 5,392 | █████ |

The last four complete months averaged 11,294 articles a month against 25,242 in the first four (-55%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 49% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 11,722 | 26% |
| United Kingdom | 2,249 | 5.0% |
| India | 1,664 | 3.7% |
| Australia | 841 | 1.9% |
| New Zealand | 557 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| covid-19 public health policies and lockdown measures | 1,574 | 5.7% | +12% |
| covid-19 mental health impact and pandemic-related stress | 1,408 | 5.1% | -2% |
| covid-19 clinical trial design for therapeutics | 948 | 3.5% | +0% |
| covid-19 epidemiology and transmission modeling | 922 | 3.4% | -1% |
| covid-19 antiviral treatments and therapeutics | 885 | 3.2% | -5% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Lorraine Kelly admits 'I burst into tears' as she addresses 'false' diagnosis](https://www.mirror.co.uk/3am/celebrity-news/lorraine-kelly-admits-i-burst-37074394) | mirror.co.uk | 9 | negative |
| 13 Apr 2026 | [Felt like I was dying: Musk backs insider who said Covid vaccine killed thousands](https://www.indiatoday.in/science/story/elon-musk-pfizer-toxicologist-covid-vaccine-bundestag-germany-60000-deaths-mrna-approval-2895204-2026-04-13) | indiatoday.in | 9 | negative |
| 8 Apr 2026 | [Nine cops sentenced to death over Covid killings](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/04/08/nine-cops-sentenced-to-death-over-covid-killings) | thestar.com.my | 9 | negative |
| 31 Mar 2026 | [White House COVID response chief discusses new COVID surge](https://www.pbssocal.org/shows/newshour/clip/covid-crisis-1653162690) | pbssocal.org | 9 | negative |
| 26 Mar 2026 | [No one can foresee fallout: Putin warns Gulf war could rival COVID chaos](https://www.indiatoday.in/world/story/putin-warns-gulf-war-fallout-could-rival-covid-pandemic-impact-globally-2887650-2026-03-27) | indiatoday.in | 9 | negative |
| 25 Mar 2026 | [Iran’s military rejects Trump’s talk of negotiation, as Israel and Iran launch airstrikes](https://kathmandupost.com/world/2026/03/25/iran-s-military-rejects-trump-s-talk-of-negotiation-as-israel-and-iran-launch-airstrikes) | kathmandupost.com | 9 | negative |
| 23 Mar 2026 | [Stay united like during Covid as West Asia crisis may last long: Modi](https://telanganatoday.com/stay-united-like-during-covid-as-west-asia-crisis-may-last-long-modi) | telanganatoday.com | 9 | positive |
| 19 Mar 2026 | [Covid-19 Inquiry verdict today amid warning UK is unprepared for next pandemic](https://www.mirror.co.uk/news/health/covid-19-inquiry-gives-verdict-36887360) | mirror.co.uk | 9 | negative |
| 18 Mar 2026 | [COVID probably killed 150,000 more people in its first two years than official U.S. tolls show](https://www.yahoo.com/news/articles/covid-probably-killed-150-000-180000951.html) | yahoo.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "COVID" --since 2026-01-01 --until 2026-04-30
prism-news trends "COVID" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "COVID" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "COVID", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "COVID", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Ebola Outbreak](ebola-outbreak.md)
- [Influenza Outbreak](influenza-outbreak.md)
- [Bird Flu News](bird-flu-news.md)
- [HIV News](hiv-news.md)
