# Influenza Outbreak News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “influenza outbreak” · 3,600/month India · 40,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [influenza-outbreak.json](../../examples/scenarios/influenza-outbreak.json).

**Question.** How much influenza coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="influenza"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,182 |
| Negative · neutral · positive | 52% · 3.2% · 44% |
| Critical (priority 7–9) | 73% (3,770 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (1,896 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | pandemic preparedness and response |

## Twelve months of coverage

Monthly matching articles for `influenza` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,764 | 56% | 933 | 763 | ███████████████████ |
| Jun 2025 | 769 | 73% | 353 | 391 | ████████ |
| Jul 2025 | 907 | 68% | 443 | 420 | ██████████ |
| Aug 2025 | 1,047 | 71% | 516 | 481 | ███████████ |
| Sep 2025 | 1,072 | 73% | 502 | 524 | ███████████ |
| Oct 2025 | 1,175 | 69% | 577 | 565 | ████████████ |
| Nov 2025 | 1,369 | 68% | 794 | 535 | ██████████████ |
| Dec 2025 | 1,896 | 66% | 1,042 | 777 | ████████████████████ |
| Jan 2026 | 1,593 | 75% | 850 | 682 | █████████████████ |
| Feb 2026 | 1,357 | 75% | 785 | 533 | ██████████████ |
| Mar 2026 | 984 | 69% | 478 | 478 | ██████████ |
| Apr 2026 | 1,248 | 70% | 595 | 611 | █████████████ |

The last four complete months averaged 1,296 articles a month against 1,122 in the first four (+15%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 27% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 737 | 14% |
| India | 126 | 2.4% |
| United Kingdom | 68 | 1.3% |
| Australia | 49 | 0.9% |
| China | 45 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| pandemic preparedness and response | 219 | 6.2% | -13% |
| zoonotic disease transmission pathways | 721 | 20% | -9% |
| emerging zoonotic viruses | 510 | 14% | -4% |
| covid-19 variants (alpha, delta, omicron) and mutations | 173 | 4.9% | +36% |
| immunization strategies for rare diseases | 162 | 4.6% | +4% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Triple alerta sanitaria en Cusco por brotes virales: menores de cinco años son los más afectados](https://larepublica.pe/sociedad/2026/04/14/triple-alerta-sanitaria-en-cusco-por-brotes-virales-menores-de-cinco-anos-son-los-mas-afectados-1339268) | larepublica.pe | 9 | negative |
| 7 Jan 2026 | [4 Massachusetts Children Killed By Flu](https://patch.com/massachusetts/across-ma/4-massachusetts-children-killed-flu) | patch.com | 9 | negative |
| 5 Jan 2026 | [MA Reports 1st Flu-Related Child Death Of Season](https://patch.com/massachusetts/across-ma/massachusetts-reports-1st-flu-related-child-death-season) | patch.com | 9 | negative |
| 28 Apr 2026 | [How the concept of ‘medical freedom’ is reshaping the military’s decades-long stance on the flu vaccine…](https://www.nationaltribune.com.au/how-the-concept-of-medical-freedom-is-reshaping-the-military-s-decades-long-stance-on-the-flu-vaccine-mandate-and-endangering-troops-readiness/) | nationaltribune.com.au | 8 | negative |
| 28 Apr 2026 | [How the concept of ‘medical freedom’ is reshaping the military’s decades-long stance on the flu vaccine…](http://theconversation.com/how-the-concept-of-medical-freedom-is-reshaping-the-militarys-decades-long-stance-on-the-flu-vaccine-mandate-and-endangering-troops-readiness-281387) | theconversation.com | 8 | negative |
| 23 Apr 2026 | [Annual influenza vaccines now optional under US Department of War guidance changes](https://www.defenceconnect.com.au/geopolitics-and-policy/18063-annual-influenza-vaccines-now-optional-under-us-department-of-war-guidance-changes) | defenceconnect.com.au | 8 | negative |
| 21 Apr 2026 | [ESCMID Global 2026: repeat vaccination with mRNA-1010 safe and effective](https://www.yahoo.com/news/articles/escmid-global-2026-repeat-vaccination-160817609.html) | yahoo.com | 8 | positive |
| 21 Apr 2026 | [Hegseth will mit Abschaffung der Impfpflicht "Ära des Verrats" beenden](https://www.n-tv.de/politik/Hegseth-will-mit-Abschaffung-der-Impfpflicht-Aera-des-Verrats-beenden-id30739610.html) | n-tv.de | 8 | negative |
| 21 Apr 2026 | [Why early action matters for cardiovascular health](https://www.politico.eu/sponsored-content/why-early-action-matters-for-cardiovascular-health/) | politico.eu | 8 | positive |
| 18 Apr 2026 | [Study: Flu plays larger role in winter deaths than recognized](https://healio.com/news/infectious-disease/20260418/study-flu-plays-larger-role-in-winter-deaths-than-recognized) | healio.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "influenza" --since 2026-01-01 --until 2026-04-30
prism-news trends "influenza" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "influenza" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "influenza", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "influenza", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Measles Outbreak](measles-outbreak.md)
- [Ebola Outbreak](ebola-outbreak.md)
- [COVID News](covid-news.md)
- [Bird Flu News](bird-flu-news.md)
