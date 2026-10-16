# Augmented Reality News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “augmented reality news” · 210/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [augmented-reality-news.json](../../examples/scenarios/augmented-reality-news.json).

**Question.** How much augmented reality coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="augmented reality"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,796 |
| Negative · neutral · positive | 15% · 0.9% · 85% |
| Critical (priority 7–9) | 34% (1,286 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,181 articles) |
| Most-reported country | United States (29% of matches) |
| Strongest theme by lift | augmented reality (ar) and virtual reality (vr) |

## Twelve months of coverage

Monthly matching articles for `augmented reality` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 843 | 26% | 77 | 754 | ██████████████ |
| Jun 2025 | 683 | 28% | 30 | 649 | ████████████ |
| Jul 2025 | 772 | 28% | 72 | 696 | █████████████ |
| Aug 2025 | 800 | 31% | 56 | 731 | ██████████████ |
| Sep 2025 | 833 | 28% | 42 | 780 | ██████████████ |
| Oct 2025 | 774 | 34% | 39 | 728 | █████████████ |
| Nov 2025 | 710 | 29% | 44 | 660 | ████████████ |
| Dec 2025 | 641 | 30% | 65 | 573 | ███████████ |
| Jan 2026 | 752 | 30% | 82 | 660 | █████████████ |
| Feb 2026 | 1,094 | 42% | 260 | 828 | ███████████████████ |
| Mar 2026 | 769 | 30% | 98 | 662 | █████████████ |
| Apr 2026 | 1,181 | 31% | 112 | 1,058 | ████████████████████ |

The last four complete months averaged 949 articles a month against 774 in the first four (+23%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,084 | 29% |
| India | 112 | 3.0% |
| China | 96 | 2.5% |
| United Kingdom | 94 | 2.5% |
| Colombia | 87 | 2.3% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| augmented reality (ar) and virtual reality (vr) | 112 | 5.4% | +10% |
| wearable technology innovations | 106 | 5.1% | +10% |
| smart glasses and wearable displays | 87 | 4.2% | -38% |
| augmented reality (ar) devices | 87 | 4.2% | -38% |
| virtual reality (vr) headsets | 81 | 3.9% | -40% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Campaign's Augmented Reality Tool Allows Students to Explore True Cost of Nuclear Weapons \| Common Dreams](https://www.commondreams.org/news/class-dismissed-nuclear-weapons) | commondreams.org | 8 | negative |
| 17 Apr 2026 | [‘White House, Black Hands’: New Orleans artist uses augmented reality to reveal history](https://www.yahoo.com/news/articles/white-house-black-hands-orleans-025308377.html) | yahoo.com | 8 | positive |
| 10 Apr 2026 | [Inside our Artemis II reporting](https://www.nbcnews.com/news/us-news/artemis-ii-reporting-rcna273732) | nbcnews.com | 8 | positive |
| 9 Apr 2026 | [How GenAIPI was built in a weekend and made $1M in 6 months with AI tools](https://www.utahbusiness.com/entrepreneurship/2026/04/09/genaipi-built-in-weekend-ai-jon-cheney-seek-infinity-pools-entrepreneurship/) | utahbusiness.com | 8 | positive |
| 17 Mar 2026 | [For Gen Z, AI is becoming a daily tool, not a trend](https://economictimes.indiatimes.com/industry/services/advertising/et-snapchat-gen-z-index-for-gen-z-ai-is-becoming-a-daily-tool-not-a-trend/articleshow/129625596.cms) | economictimes.indiatimes.com | 8 | positive |
| 10 Mar 2026 | [Caitlin Kalinowski Resigns After Pentagon Deal in 2026: Why AR Teams Are Worried](https://glassalmanac.com/caitlin-kalinowski-resigns-after-pentagon-deal-in-2026-why-ar-teams-are-worried/) | glassalmanac.com | 8 | negative |
| 9 Mar 2026 | [OpenAI Robotics head resigns after deal with Pentagon](https://hr.economictimes.indiatimes.com/news/industry/openai-robotics-head-resigns-over-pentagon-ai-deal-controversy/129304856) | hr.economictimes.indiatimes.com | 8 | negative |
| 28 Feb 2026 | [Artificial intelligence assisted 3D in the robotic urooncology? A systematic review and narrative synthesis…](https://pubmed.ncbi.nlm.nih.gov/41800506/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 18 Feb 2026 | [AI, Robotics & Tech: The Future of Orthopedic Surgery - News Directory 3](https://www.newsdirectory3.com/ai-robotics-tech-the-future-of-orthopedic-surgery/) | newsdirectory3.com | 8 | positive |
| 6 Feb 2026 | [WiMi Releases Hybrid Quantum-Classical Neural Network (H-QNN) Technology for Efficient MNIST Binary Image…](https://www.globenewswire.com/news-release/2026/02/06/3233807/0/en/WiMi-Releases-Hybrid-Quantum-Classical-Neural-Network-H-QNN-Technology-for-Efficient-MNIST-Binary-Image-Classification.html) | globenewswire.com | 8 | positive |
| 26 Jan 2026 | [This Will Replace The Smartphone Sparks AR Hiring Surge in 2025 - Here's Why](https://glassalmanac.com/this-will-replace-the-smartphone-sparks-ar-hiring-surge-in-2025-heres-why/) | glassalmanac.com | 8 | positive |
| 24 Jan 2026 | [Maia: Pioneering AI-Driven Surgical Assistance in Medicine](https://orthofeed.com/2026/01/24/maia-pioneering-ai-driven-surgical-assistance-in-medicine/) | orthofeed.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "augmented reality" --since 2026-01-01 --until 2026-04-30
prism-news trends "augmented reality" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "augmented reality" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "augmented reality", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "augmented reality", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI Chips News](ai-chips-news.md)
- [AI Safety News](ai-safety-news.md)
- [Humanoid Robot News](humanoid-robot-news.md)
- [Blockchain News](blockchain-news.md)
