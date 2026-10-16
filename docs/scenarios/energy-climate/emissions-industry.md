# Emissions Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “emissions industry” · 390/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [emissions-industry.json](../../examples/scenarios/emissions-industry.json).

**Question.** How did emissions coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="emissions"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 25,176 |
| Negative · neutral · positive | 30% · 10% · 59% |
| Critical (priority 7–9) | 55% (13,778 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (8,113 articles) |
| Most-reported country | United States (10% of matches) |
| Strongest theme by lift | carbon footprint reduction techniques |

## Twelve months of coverage

Monthly matching articles for `emissions` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,853 | 71% | 1,318 | 2,367 | █████████ |
| Jun 2025 | 3,696 | 70% | 1,126 | 2,430 | █████████ |
| Jul 2025 | 4,426 | 66% | 1,611 | 2,635 | ███████████ |
| Aug 2025 | 3,859 | 69% | 1,415 | 2,309 | ██████████ |
| Sep 2025 | 4,991 | 73% | 1,661 | 3,103 | ████████████ |
| Oct 2025 | 4,644 | 73% | 1,650 | 2,832 | ███████████ |
| Nov 2025 | 5,642 | 67% | 1,904 | 3,485 | ██████████████ |
| Dec 2025 | 4,595 | 68% | 1,446 | 2,893 | ███████████ |
| Jan 2026 | 4,375 | 61% | 1,293 | 2,733 | ███████████ |
| Feb 2026 | 8,113 | 49% | 2,611 | 4,476 | ████████████████████ |
| Mar 2026 | 6,943 | 49% | 1,954 | 4,115 | █████████████████ |
| Apr 2026 | 5,745 | 65% | 1,752 | 3,577 | ██████████████ |

The last four complete months averaged 6,294 articles a month against 3,958 in the first four (+59%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 28% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,630 | 10% |
| India | 722 | 2.9% |
| United Kingdom | 614 | 2.4% |
| China | 276 | 1.1% |
| Australia | 235 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| carbon footprint reduction techniques | 2,526 | 17% | +5% |
| green technology innovations | 676 | 4.4% | +42% |
| energy-efficient home solutions | 653 | 4.3% | +27% |
| climate change mitigation strategies | 3,405 | 22% | -9% |
| eco-friendly transportation alternatives | 596 | 3.9% | -3% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [The achievability of low-emission IPCC sea-level rise scenarios.](https://pubmed.ncbi.nlm.nih.gov/42021658/) | pubmed.ncbi.nlm.nih.gov | 9 | negative |
| 13 Apr 2026 | [Collapse of key ocean current may release billions of tonnes of carbon](https://newscientist.com/article/2522765-collapse-of-key-ocean-current-may-release-billions-of-tonnes-of-carbon/) | newscientist.com | 9 | negative |
| 10 Apr 2026 | [Study: US Caused $10 Trillion in Climate Damage - Asia Plus](https://asiaplus.news/en/2026/04/10/study-us-caused-10-trillion-in-climate-damage/) | asiaplus.news | 9 | negative |
| 7 Apr 2026 | [Studie: Menschgemachte Treibhausgase verstärken gleichzeitige Hitzewellen und Dürren](http://www.n-tv.de/ticker/Studie-Menschgemachte-Treibhausgase-verstaerken-gleichzeitige-Hitzewellen-und-Duerren-id30689037.html) | n-tv.de | 9 | negative |
| 2 Apr 2026 | [Diese Promis verursachen mit Privatjets den größten Klima-Schaden](https://www.gmx.net/magazine/wissen/klima/promis-verursachen-privatjets-groessten-klima-schaden-42071952) | gmx.net | 9 | negative |
| 2 Apr 2026 | [Studie zeigt, welche Promis mit Privatjets den höchsten Schaden verursachen](https://www.gmx.net/magazine/wissen/klima/promis-privatjets-hoechsten-schaden-verursachen-42071952) | gmx.net | 9 | negative |
| 2 Apr 2026 | [Gates, Bezos & Co.: Privatjet-Flüge verursachen Millionenschäden](https://www.gmx.net/magazine/wissen/klima/gates-bezos-co-privatjet-fluege-verursachen-millionenschaeden-42071952) | gmx.net | 9 | negative |
| 31 Mar 2026 | [Russia: Nizhnekamsk Explosion Leaves Two Dead, Many Wounded](https://europeanconservative.com/articles/news-corner/russia-nizhnekamsk-explosion-chemical-two-dead-many-wounded/) | europeanconservative.com | 9 | negative |
| 26 Mar 2026 | [US responsible for $10T worth of global climate damage since 1990: Study](https://www.yahoo.com/news/articles/us-responsible-10t-worth-global-215637735.html) | yahoo.com | 9 | negative |
| 25 Mar 2026 | [US Carbon Emissions Caused $10 Trillion in Global Damages](https://world.infonasional.com/us-carbon-emissions-global-damages) | world.infonasional.com | 9 | negative |
| 20 Mar 2026 | [High heat, broken pump lead to elevated 'sewer gas' smells in South Bay](https://us.headtopics.com/news/high-heat-broken-pump-lead-to-elevated-sewer-gas-smells-81257943) | us.headtopics.com | 9 | negative |
| 4 Mar 2026 | [Somali Immigrants Fled Climate Change. Now They’re Facing ICE.](http://newrepublic.com/article/207231/somali-immigrants-climate-trump) | newrepublic.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "emissions" --since 2026-01-01 --until 2026-04-30
prism-news trends "emissions" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "emissions" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "emissions", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "emissions", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Refinery News](refinery-news.md)
- [Energy Storage News](energy-storage-news.md)
- [Power Outage News](power-outage-news.md)
- [Wind Energy News](wind-energy-news.md)
