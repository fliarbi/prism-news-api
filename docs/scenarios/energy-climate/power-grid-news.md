# Power Grid News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “power grid news” · 1,300/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [power-grid-news.json](../../examples/scenarios/power-grid-news.json).

**Question.** How did power grid coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="power grid"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,961 |
| Negative · neutral · positive | 42% · 1.1% · 57% |
| Critical (priority 7–9) | 73% (2,165 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (903 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | asian financial market developments |

## Twelve months of coverage

Monthly matching articles for `power grid` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 578 | 63% | 213 | 354 | █████████████ |
| Jun 2025 | 449 | 62% | 122 | 322 | ██████████ |
| Jul 2025 | 452 | 56% | 151 | 296 | ██████████ |
| Aug 2025 | 631 | 57% | 218 | 410 | ██████████████ |
| Sep 2025 | 620 | 58% | 162 | 448 | ██████████████ |
| Oct 2025 | 598 | 59% | 234 | 358 | █████████████ |
| Nov 2025 | 501 | 58% | 139 | 360 | ███████████ |
| Dec 2025 | 529 | 63% | 151 | 376 | ████████████ |
| Jan 2026 | 601 | 78% | 302 | 290 | █████████████ |
| Feb 2026 | 769 | 65% | 225 | 535 | █████████████████ |
| Mar 2026 | 903 | 77% | 467 | 431 | ████████████████████ |
| Apr 2026 | 688 | 72% | 243 | 433 | ███████████████ |

The last four complete months averaged 740 articles a month against 528 in the first four (+40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 532 | 18% |
| India | 360 | 12% |
| China | 127 | 4.3% |
| Iran | 49 | 1.6% |
| Russia | 38 | 1.3% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| asian financial market developments | 151 | 7.5% | -32% |
| stock market index composition | 227 | 11% | -20% |
| market volatility indicators | 215 | 11% | -13% |
| electricity transmission infrastructure & grid systems | 195 | 9.7% | +93% |
| international/emerging markets stocks | 215 | 11% | -20% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 16 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Apr 2026 | [Trump afirma que usinas e pontes do Irã ainda são possíveis alvos \| CNN Brasil](https://www.cnnbrasil.com.br/internacional/trump-afirma-que-usinas-e-pontes-do-ira-ainda-sao-possiveis-alvos/) | cnnbrasil.com.br | 9 | negative |
| 7 Apr 2026 | [Perto do fim do prazo, Trump ameaça aniquilação do Irã e país denuncia genocídio na ONU](https://veja.abril.com.br/brasil/sob-fim-do-prazo-trump-ameaca-aniquilacao-do-ira-e-pais-denuncia-genocidio-na-onu/) | veja.abril.com.br | 9 | negative |
| 7 Apr 2026 | [The Last Temptation of Trump at the End of a Failed War](https://newlinesmag.com/argument/the-last-temptation-of-trump-at-the-end-of-a-failed-war/) ⚠ | newlinesmag.com | 9 | negative |
| 7 Feb 2026 | [Pressure for Ukraine-Russia deal mounts ahead of fall elections in US](https://www.politico.eu/article/pressure-ukraine-russia-deal-mounts-ahead-us-elections/) ⚠ | politico.eu | 9 | negative |
| 4 Feb 2026 | [Russia bombards Ukraine with drones and missiles a day before planned peace talks](https://www.thehindu.com/news/international/russia-bombards-ukraine-with-drones-and-missiles-a-day-before-planned-peace-talks/article70590074.ece) ⚠ | thehindu.com | 9 | negative |
| 3 Feb 2026 | [Russia fires barrage of drones and missiles on Ukraine’s power grid](https://www.pressreader.com/india/hindustan-times-st-jaipur/20260204/281496462716046) | pressreader.com | 9 | negative |
| 2 Feb 2026 | [Default ICS Credentials Exploited in Destructive Attack on Polish Energy Facilities](https://www.securityweek.com/default-ics-credentials-exploited-in-destructive-attack-on-polish-energy-facilities/) | securityweek.com | 9 | negative |
| 21 Jan 2026 | [Ukraine endures a bitter winter after Russian attacks as peace efforts overshadowed](https://thehimalayantimes.com/world/ukraine-endures-a-bitter-winter-after-russian-attacks-as-peace-efforts-overshadowed) | thehimalayantimes.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "power grid" --since 2026-01-01 --until 2026-04-30
prism-news trends "power grid" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "power grid" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "power grid", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "power grid", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [El Nino News](el-nino-news.md)
- [EV Charging News](ev-charging-news.md)
- [Uranium News](uranium-news.md)
- [Solar Panels Industry](solar-panels-industry.md)
