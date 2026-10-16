# Autonomous Vehicles News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “autonomous vehicles news” · 20/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [autonomous-vehicles-news.json](../../examples/scenarios/autonomous-vehicles-news.json).

**Question.** How much autonomous vehicles coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="autonomous vehicles"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,719 |
| Negative · neutral · positive | 16% · 0.8% · 84% |
| Critical (priority 7–9) | 68% (3,198 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (1,227 articles) |
| Most-reported country | United States (33% of matches) |
| Strongest theme by lift | tesla motors autopilot & full self-driving technology |

## Twelve months of coverage

Monthly matching articles for `autonomous vehicles` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 945 | 61% | 155 | 779 | ███████████████ |
| Jun 2025 | 1,027 | 56% | 204 | 818 | █████████████████ |
| Jul 2025 | 1,038 | 59% | 206 | 829 | █████████████████ |
| Aug 2025 | 1,008 | 63% | 163 | 839 | ████████████████ |
| Sep 2025 | 940 | 60% | 95 | 838 | ███████████████ |
| Oct 2025 | 923 | 70% | 146 | 773 | ███████████████ |
| Nov 2025 | 929 | 63% | 90 | 822 | ███████████████ |
| Dec 2025 | 997 | 67% | 257 | 735 | ████████████████ |
| Jan 2026 | 1,227 | 70% | 227 | 994 | ████████████████████ |
| Feb 2026 | 1,200 | 65% | 193 | 996 | ████████████████████ |
| Mar 2026 | 1,119 | 71% | 158 | 946 | ██████████████████ |
| Apr 2026 | 1,173 | 65% | 163 | 1,004 | ███████████████████ |

The last four complete months averaged 1,180 articles a month against 1,004 in the first four (+17%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,550 | 33% |
| China | 192 | 4.1% |
| United Kingdom | 130 | 2.8% |
| India | 77 | 1.6% |
| Japan | 72 | 1.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| tesla motors autopilot & full self-driving technology | 254 | 8.8% | +5% |
| tesla motors autonomous driving data & regulatory compliance | 248 | 8.6% | +5% |
| connected car technologies | 217 | 7.5% | +54% |
| vehicle telematics and iot integration | 152 | 5.3% | +65% |
| autonomous ride-sharing fleets | 145 | 5.0% | -34% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 4 Mar 2026 | [Driverless taxi keeps emergency responders from Austin shooting](https://landline.media/driverless-taxi-keeps-emergency-responders-from-austin-shooting/) | landline.media | 9 | negative |
| 3 Mar 2026 | [Waymo car blocked ambulance trying to get to scene of Austin mass shooting](https://www.inkl.com/news/waymo-car-blocked-ambulance-trying-to-get-to-scene-of-austin-mass-shooting) | inkl.com | 9 | negative |
| 27 Apr 2026 | [Waymo declines to attend public meeting on self-driving cars, Austin city leaders say](https://www.yahoo.com/news/articles/waymo-declines-attend-public-meeting-210839798.html) | yahoo.com | 8 | negative |
| 22 Apr 2026 | [Tesla Stock Sinks On CapEx — Intel Pops On Elon Musk's Mention - Tesla (NASDAQ:TSLA)](https://benzinga.com/markets/earnings/26/04/51988221/tesla-capex-spike-hits-stock-as-intel-pops-on-elon-musk-comments) | benzinga.com | 8 | positive |
| 22 Apr 2026 | [Unleash AI Innovation: The Power of NVIDIA RTX PRO 6000Blackwell Workstation Edition Fueled by PNY-Supplied…](https://www.videomaker.com/sponsored/unleash-ai-innovation-the-power-of-nvidia-rtx-pro-6000blackwell-workstation-edition-fueled-by-pny-supplied-gpus/) | videomaker.com | 8 | positive |
| 17 Apr 2026 | [Unleash AI Innovation: The Power of NVIDIA RTX PRO 6000 Blackwell Workstation Edition Fueled by PNY-Supplied…](https://www.digitalengineering247.com/article/unleash-ai-innovation-the-power-of-nvidia-rtx-pro-6000-blackwell-workstation-edition-fueled-by-pny-supplied-gpus/pny-technologies) | digitalengineering247.com | 8 | positive |
| 15 Apr 2026 | [Uber’s $10 Bn Robotaxi Push Takes on Tesla, Waymo – Outlook Business](https://www.outlookbusiness.com/corporate/ubers-10-bn-robotaxi-push-takes-on-tesla-waymo) | outlookbusiness.com | 8 | positive |
| 15 Apr 2026 | [Baidu autonomous car to use NVIDIA’s artificial intelligence computer \| Autocar Professional](http://www.autocarpro.in/news-international/baidu-autonomous-car-nvidia-artificial-intelligence-21725) | autocarpro.in | 8 | positive |
| 13 Apr 2026 | [Elon Musk e Intel planean una megafábrica de chips - Roastbrief](https://roastbrief.com.mx/2026/04/elon-musk-e-intel-planean-una-megafabrica-de-chips/) | roastbrief.com.mx | 8 | positive |
| 23 Mar 2026 | [Elon Musk Announces Massive 'Terafab' Chip Factory in Austin to Power Tesla AI, SpaceX Satellites and Robotics](http://ibtimes.com/elon-musk-announces-massive-terafab-chip-factory-austin-power-tesla-ai-spacex-satellites-3799892) | ibtimes.com | 8 | positive |
| 23 Mar 2026 | [San Francisco: Waymo passenger attacked for paying a self-driving car](https://www.newsbytesapp.com/news/auto/san-francisco-man-trapped-inside-waymo-as-attacker-smashes-windows/story) | newsbytesapp.com | 8 | negative |
| 21 Mar 2026 | [Watch the road: these 5 states have the most irresponsible drivers](https://finance.yahoo.com/sectors/technology/articles/watch-road-5-states-most-134700436.html) | finance.yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "autonomous vehicles" --since 2026-01-01 --until 2026-04-30
prism-news trends "autonomous vehicles" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "autonomous vehicles" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "autonomous vehicles", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "autonomous vehicles", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Humanoid Robot News](humanoid-robot-news.md)
- [Blockchain News](blockchain-news.md)
- [EV Batteries News](ev-batteries-news.md)
- [Smart Home News](smart-home-news.md)
