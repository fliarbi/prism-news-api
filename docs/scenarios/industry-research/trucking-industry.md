# Trucking Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “trucking industry” · 90/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [trucking-industry.json](../../examples/scenarios/trucking-industry.json).

**Question.** How much news did the trucking industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="trucking industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 728 |
| Negative · neutral · positive | 43% · 1.0% · 56% |
| Critical (priority 7–9) | 56% (409 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (263 articles) |
| Most-reported country | United States (35% of matches) |
| Strongest theme by lift | freight workforce training |

## Twelve months of coverage

Monthly matching articles for `trucking industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 140 | 60% | 54 | 86 | ███████████ |
| Jun 2025 | 94 | 62% | 43 | 51 | ███████ |
| Jul 2025 | 120 | 58% | 49 | 71 | █████████ |
| Aug 2025 | 126 | 62% | 70 | 56 | ██████████ |
| Sep 2025 | 110 | 62% | 45 | 62 | ████████ |
| Oct 2025 | 193 | 64% | 97 | 91 | ███████████████ |
| Nov 2025 | 104 | 66% | 64 | 40 | ████████ |
| Dec 2025 | 155 | 76% | 97 | 56 | ████████████ |
| Jan 2026 | 127 | 50% | 38 | 88 | ██████████ |
| Feb 2026 | 162 | 66% | 92 | 68 | ████████████ |
| Mar 2026 | 263 | 52% | 101 | 162 | ████████████████████ |
| Apr 2026 | 176 | 57% | 83 | 87 | █████████████ |

The last four complete months averaged 182 articles a month against 120 in the first four (+52%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 254 | 35% |
| Australia | 40 | 5.5% |
| Canada | 36 | 5.0% |
| Iran | 10 | 1.4% |
| India | 9 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| freight workforce training | 151 | 32% | +38% |
| freight fleet maintenance | 114 | 24% | +322% |
| freight compliance standards | 71 | 15% | -23% |
| freight cost management | 63 | 13% | +200% |
| freight security protocols | 60 | 13% | -22% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [SONAR Sitrep: AI data center build-out fuels US freight surge](https://www.freightwaves.com/news/sonar-sitrep-ai-data-center-build-out-fuels-us-freight-surge) | freightwaves.com | 8 | positive |
| 20 Mar 2026 | [California truck driver bill put to rest](https://landline.media/california-truck-driver-bill-put-to-rest/) | landline.media | 8 | positive |
| 1 Mar 2026 | ['There's a real problem.' Colorado widow reacts Trump push to ban undocumented immigrants from driving semis](https://www.denver7.com/news/investigations/theres-a-real-problem-colorado-widow-reacts-to-trump-push-to-ban-undocumented-immigrants-from-driving-semis) | denver7.com | 8 | negative |
| 23 Feb 2026 | [USDOT teams with state DOTs for sting operations](https://www.thetrucker.com/trucking-news/business/usdot-teams-with-state-dots-for-sting-operations) | thetrucker.com | 8 | negative |
| 19 Feb 2026 | [Industry reacts to USDOT action on 'CDL mills'](https://www.thetrucker.com/trucking-news/the-nation/industry-reacts-to-usdot-action-on-cdl-mills) | thetrucker.com | 8 | negative |
| 19 Feb 2026 | [After a string of fatal crashes, Indiana makes push for crackdown on immigrant truck drivers](https://www.pressreader.com/usa/the-indianapolis-star/20260219/281513642617411) | pressreader.com | 8 | negative |
| 12 Feb 2026 | [Trump EPA ends basis for heavy-duty truck emissions rules](https://www.yahoo.com/news/articles/trump-epa-ends-basis-heavy-201153631.html) | yahoo.com | 8 | negative |
| 11 Jan 2026 | [Australia’s Trucking Shake-Out in 2025 Who left, what broke, and why 2026 will be harder for operators](https://www.linkedin.com/pulse/australias-trucking-shake-out-2025-who-left-what-broke-ali-raza-tfwnc) | linkedin.com | 8 | negative |
| 24 Apr 2026 | [Trucking industry reacts to Trump's marijuana reclassification](https://www.thetrucker.com/trucking-news/the-nation/trucking-industry-reacts-to-trumps-marijuana-reclassification) | thetrucker.com | 7 | positive |
| 16 Apr 2026 | [US Truckers Hit by 50% Diesel Price Surge Amid Iran War; Renewed Talks Bring Cautious Optimism - Vision Times](https://www.visiontimes.com/2026/04/15/us-truckers-hit-by-50-diesel-price-surge-amid-iran-war-renewed-talks-bring-cautious-optimism.html) | visiontimes.com | 7 | negative |
| 15 Apr 2026 | [Truck drivers halt ops as take-home pay drops to P500](https://newsinfo.inquirer.net/2212720/truck-drivers-group-on-losing-income-amid-rising-cost-of-fuel) | newsinfo.inquirer.net | 7 | negative |
| 15 Apr 2026 | [Most truckies fear they won't last 12 months, industry survey says](https://www.abc.net.au/news/2026-04-15/natroad-survey-of-200-truckers-shows-75pc-fear-closure/106567804) | abc.net.au | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "trucking industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "trucking industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "trucking industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "trucking industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "trucking industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Paper Industry](paper-industry.md)
- [Biotech Industry](biotech-industry.md)
- [Packaging Industry](packaging-industry.md)
- [Logistics Industry News](logistics-industry-news.md)
