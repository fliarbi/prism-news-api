# Aerospace Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “aerospace industry” · 1,300/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [aerospace-industry.json](../../examples/scenarios/aerospace-industry.json).

**Question.** How much news did the aerospace industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="aerospace industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,154 |
| Negative · neutral · positive | 11% · 3.9% · 85% |
| Critical (priority 7–9) | 40% (456 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (364 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | aviation industry aircraft manufacturing processes |

## Twelve months of coverage

Monthly matching articles for `aerospace industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 237 | 43% | 25 | 207 | █████████████ |
| Jun 2025 | 311 | 53% | 50 | 255 | █████████████████ |
| Jul 2025 | 217 | 50% | 28 | 187 | ████████████ |
| Aug 2025 | 205 | 45% | 19 | 183 | ███████████ |
| Sep 2025 | 227 | 46% | 21 | 203 | ████████████ |
| Oct 2025 | 247 | 52% | 35 | 211 | ██████████████ |
| Nov 2025 | 219 | 42% | 16 | 202 | ████████████ |
| Dec 2025 | 197 | 39% | 16 | 176 | ███████████ |
| Jan 2026 | 234 | 42% | 39 | 188 | █████████████ |
| Feb 2026 | 335 | 35% | 30 | 291 | ██████████████████ |
| Mar 2026 | 221 | 50% | 29 | 185 | ████████████ |
| Apr 2026 | 364 | 36% | 33 | 313 | ████████████████████ |

The last four complete months averaged 288 articles a month against 242 in the first four (+19%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 51% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 329 | 29% |
| India | 57 | 4.9% |
| United Kingdom | 55 | 4.8% |
| China | 33 | 2.9% |
| Turkey | 13 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| aviation industry aircraft manufacturing processes | 41 | 6.0% | +11% |
| aerospace industry mergers and acquisitions | 40 | 5.8% | +82% |
| aerospace supply chain management strategies | 39 | 5.7% | +39% |
| aviation industry aerospace defense contracting | 32 | 4.7% | -18% |
| aerospace component manufacturing processes | 27 | 3.9% | +12% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Jan 2026 | [President Trump Targets Canada's Aerospace Industry/Bombardier](https://canadiandefencereview.com/president-trump-targets-canadas-aerospace-industry-bombardier/) | canadiandefencereview.com | 8 | negative |
| 30 Jan 2026 | [Trump threatens to block Canadian aircraft, warns of 50% tariff as tensions rise](https://www.financialexpress.com/world-news/us-news/trump-threatens-to-block-canadian-aircraft-warns-of-50-tariff-as-tensions-rise/4123959/) | financialexpress.com | 8 | negative |
| 29 Apr 2026 | [NATO looking at Canadian aircraft for its new airborne warning fleet](https://ca.news.yahoo.com/nato-looking-canadian-aircraft-airborne-080058642.html) | ca.news.yahoo.com | 7 | positive |
| 23 Apr 2026 | [Defense tech firm preparing to open 7th Beavercreek building](https://www.yahoo.com/news/articles/defense-tech-firm-preparing-open-190119467.html) | yahoo.com | 7 | positive |
| 22 Apr 2026 | [SAHA 2026 to bring defense, aerospace industry together in Istanbul - Türkiye News](https://www.hurriyetdailynews.com/saha-2026-to-bring-defense-aerospace-industry-together-in-istanbul-221324) | hurriyetdailynews.com | 7 | positive |
| 21 Apr 2026 | [Un nouveau satellite militaire confié à Airbus et Thales : quel pays a passé commande ?](https://actu.fr/occitanie/toulouse_31555/toulouse-airbus-et-thales-vont-developper-un-nouveau-satellite-militaire-quel-pays-en-a-t-il-fait-la-commande_64166028.html) | actu.fr | 7 | neutral |
| 16 Apr 2026 | [Improving sustainability outcomes for targeted scale-up of aviation fuel production](https://techxplore.com/news/2026-04-sustainability-outcomes-scale-aviation-fuel.html) | techxplore.com | 7 | positive |
| 14 Apr 2026 | [Embention Autopilots for Loitering Munitions & C-UAS: The New Standard for One-Way Drones](https://www.embention.com/news/veronte-autopilots-loitering-munition-c-uas/) | embention.com | 7 | positive |
| 13 Apr 2026 | [AKTIEN IM FOKUS: Vorläufiges Ende der Iran-Verhandlungen belastet MTU und Airbus](https://www.deraktionaer.de/nachricht/aktien-im-fokus-vorlaeufiges-ende-der-iran-verhandlungen-belastet-mtu-und-airbus-516514.html) | deraktionaer.de | 7 | negative |
| 13 Apr 2026 | [Ölpreisschock belastet MTU und Airbus deutlich](https://www.onvista.de/news/2026/04-13-oelpreisschock-belastet-mtu-und-airbus-deutlich-0-10-26499807) | onvista.de | 7 | negative |
| 12 Apr 2026 | [Embraer, CIAC sign deal for aerospace work - APDR](https://asiapacificdefencereporter.com/embraer-ciac-sign-deal-for-aerospace-work/) | asiapacificdefencereporter.com | 7 | positive |
| 9 Apr 2026 | [► Embraer and CIAC sign memorandum of understanding to leverage Colombia's aerospace industry - EDR Magazine](https://www.edrmagazine.eu/%e2%96%ba-embraer-and-ciac-sign-memorandum-of-understanding-to-leverage-colombias-aerospace-industry) | edrmagazine.eu | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "aerospace industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "aerospace industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "aerospace industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "aerospace industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "aerospace industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Chemical Industry](chemical-industry.md)
- [Music Industry](music-industry.md)
- [Sugar Industry](sugar-industry.md)
- [3d Printing Industry](3d-printing-industry.md)
