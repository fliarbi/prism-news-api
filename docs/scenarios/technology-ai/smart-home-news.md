# Smart Home News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “smart home news” · 10/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [smart-home-news.json](../../examples/scenarios/smart-home-news.json).

**Question.** How much smart home coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="smart home"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,535 |
| Negative · neutral · positive | 4.1% · 0.4% · 96% |
| Critical (priority 7–9) | 13% (745 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (1,533 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | internet of things (iot) devices |

## Twelve months of coverage

Monthly matching articles for `smart home` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 843 | 14% | 53 | 784 | ███████████ |
| Jun 2025 | 777 | 11% | 34 | 742 | ██████████ |
| Jul 2025 | 1,443 | 7.6% | 102 | 1,335 | ███████████████████ |
| Aug 2025 | 1,209 | 12% | 68 | 1,140 | ████████████████ |
| Sep 2025 | 1,532 | 8.3% | 44 | 1,481 | ████████████████████ |
| Oct 2025 | 1,251 | 12% | 52 | 1,198 | ████████████████ |
| Nov 2025 | 1,220 | 10% | 39 | 1,178 | ████████████████ |
| Dec 2025 | 1,127 | 10% | 46 | 1,067 | ███████████████ |
| Jan 2026 | 1,519 | 13% | 41 | 1,476 | ████████████████████ |
| Feb 2026 | 1,253 | 15% | 85 | 1,164 | ████████████████ |
| Mar 2026 | 1,533 | 14% | 52 | 1,475 | ████████████████████ |
| Apr 2026 | 1,230 | 13% | 47 | 1,175 | ████████████████ |

The last four complete months averaged 1,384 articles a month against 1,068 in the first four (+30%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,492 | 27% |
| South Korea | 228 | 4.1% |
| India | 175 | 3.2% |
| China | 136 | 2.5% |
| United Kingdom | 131 | 2.4% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| internet of things (iot) devices | 155 | 6.0% | +19% |
| smart home devices and systems | 255 | 9.9% | +20% |
| smart lighting systems | 118 | 4.6% | +14% |
| home automation hubs | 99 | 3.8% | +44% |
| surveillance camera systems | 145 | 5.6% | -2% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Semiconductor Market Poised for Strong Growth Amid AI and Chip Demand Surge Through 2033](https://www.openpr.com/news/4486068/semiconductor-market-poised-for-strong-growth-amid-ai-and-chip) | openpr.com | 8 | positive |
| 19 Apr 2026 | [Anker Innovation's Jeffrey Liu on AI, ecosystem growth and Middle East expansion](https://gulfbusiness.com/en/2026/interviews/anker-meas-gm-on-ai-ecosystem-growth-and-regional-expansion/) ⚠ | gulfbusiness.com | 8 | positive |
| 17 Apr 2026 | [Apple Veteran Stan Ng To Retire After 31 Years, Marketing Chief for Apple Watch and AirPods To Step Down…](https://www.latestly.com/technology/apple-veteran-stan-ng-to-retire-after-31-years-marketing-chief-for-apple-watch-and-airpods-to-step-down-amid-broader-executive-shuffle-7396290.html) | latestly.com | 8 | positive |
| 31 Mar 2026 | [India’s Consumer IoT Market Grows at 12.1% CAGR](https://www.electronicsforyou.biz/eb-specials/industry-report/indias-consumer-iot-market-grows-at-12-1-cagr/) | electronicsforyou.biz | 8 | positive |
| 30 Mar 2026 | [AI dreams: How tech boom is redefining work, creativity and daily life](https://www.philstar.com/business/technology/2026/03/30/2514066/ai-dreams-how-tech-boom-redefining-work-creativity-and-daily-life) ⚠ | philstar.com | 8 | positive |
| 29 Mar 2026 | [Samsung Topples LG in OLED Showdown as TV War Intensifies - channelnews](https://www.channelnews.com.au/samsung-topples-lg-in-oled-showdown-as-tv-war-intensifies/) ⚠ | channelnews.com.au | 8 | positive |
| 24 Mar 2026 | [TuyaClaw pushes AI off the screen to control lights, apps and home tasks](https://www.stocktitan.net/news/TUYA/tuya-smart-launches-tuya-claw-still-the-same-claw-but-actually-does-yt0of5hq84tw.html) | stocktitan.net | 8 | positive |
| 21 Mar 2026 | [Amazon eyes ‘Star Trek’-style smartphone years after Fire Phone failure](https://www.storyboard18.com/digital/amazon-ai-led-transformer-phone-to-revive-smartphone-ambitions-ws-l-92827.htm) | storyboard18.com | 8 | positive |
| 20 Mar 2026 | [Amazon working on new smartphone with Alexa at its core, report says \| TechCrunch](https://techcrunch.com/2026/03/20/amazon-working-on-new-smartphone-with-alexa-at-its-core-report-says/) | techcrunch.com | 8 | positive |
| 19 Mar 2026 | [Music and podcasts are coming to 100M Samsung smart TVs](https://www.stocktitan.net/news/LVO/live-one-nasdaq-lvo-announces-b2b-partnership-with-samsung-tv-x43f0tbnybj1.html) | stocktitan.net | 8 | positive |
| 12 Mar 2026 | [Ceva's NeuPro-Nano NPU Wins Artificial Intelligence Award at embedded world 2026 - Ceva](https://www.ceva-ip.com/press/cevas-neupro-nano-npu-wins-artificial-intelligence-award-at-embedded-world-2026/) | ceva-ip.com | 8 | positive |
| 9 Mar 2026 | [New Apple 'HomePad' Leak Tips 2026 Launch, MagSafe-Like Wall Mount](https://www.pcmag.com/news/new-apple-homepad-leak-tips-2026-launch-magsafe-like-wall-mount) | pcmag.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "smart home" --since 2026-01-01 --until 2026-04-30
prism-news trends "smart home" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "smart home" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "smart home", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "smart home", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Autonomous Vehicles News](autonomous-vehicles-news.md)
- [EV Batteries News](ev-batteries-news.md)
- [AI in Education News](ai-in-education-news.md)
- [Laptop News](laptop-news.md)
