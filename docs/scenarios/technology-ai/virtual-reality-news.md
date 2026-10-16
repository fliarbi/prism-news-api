# Virtual Reality News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “virtual reality news” · 140/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [virtual-reality-news.json](../../examples/scenarios/virtual-reality-news.json).

**Question.** How much virtual reality coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="virtual reality"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,963 |
| Negative · neutral · positive | 7.6% · 1.4% · 91% |
| Critical (priority 7–9) | 37% (1,449 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,185 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | vr training & simulation kits |

## Twelve months of coverage

Monthly matching articles for `virtual reality` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 943 | 28% | 66 | 858 | ████████████████ |
| Jun 2025 | 697 | 32% | 38 | 654 | ████████████ |
| Jul 2025 | 947 | 27% | 69 | 873 | ████████████████ |
| Aug 2025 | 1,072 | 31% | 64 | 1,002 | ██████████████████ |
| Sep 2025 | 927 | 38% | 144 | 766 | ████████████████ |
| Oct 2025 | 735 | 37% | 38 | 692 | ████████████ |
| Nov 2025 | 750 | 31% | 26 | 714 | █████████████ |
| Dec 2025 | 762 | 38% | 65 | 678 | █████████████ |
| Jan 2026 | 848 | 45% | 80 | 757 | ██████████████ |
| Feb 2026 | 949 | 37% | 56 | 883 | ████████████████ |
| Mar 2026 | 981 | 32% | 89 | 866 | █████████████████ |
| Apr 2026 | 1,185 | 34% | 76 | 1,100 | ████████████████████ |

The last four complete months averaged 991 articles a month against 915 in the first four (+8%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 741 | 19% |
| China | 132 | 3.3% |
| India | 124 | 3.1% |
| Colombia | 106 | 2.7% |
| United Kingdom | 101 | 2.5% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| vr training & simulation kits | 51 | 2.8% | +28% |
| vr social interaction platforms | 50 | 2.7% | +127% |
| digital health tools in medical education | 46 | 2.5% | +28% |
| telemedicine training programs | 42 | 2.3% | +50% |
| vr gaming accessories | 35 | 1.9% | +40% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [I would buy a phone now because smartphone prices are facing a second unexpected challenge](https://www.phonearena.com/news/smartphone-prices-facing-second-unexpected-challenge_id180026) | phonearena.com | 8 | negative |
| 8 Apr 2026 | [AI, AR-VR to power India’s e-commerce growth to $250 bn by 2030](https://www.techcircle.in/2026/04/08/ai-ar-vr-to-power-india-s-e-commerce-surge-to-250-bn-by-2030) | techcircle.in | 8 | positive |
| 17 Mar 2026 | [​Gaming Stocks in India: Top Picks, Risks & How to Invest](https://www.kotaksecurities.com/investing-guide/share-market/top-gaming-stocks-in-india/) | kotaksecurities.com | 8 | positive |
| 26 Feb 2026 | [A randomized control trial for assessing virtual reality for perioperative anxiolysis and postoperative pain…](https://pubmed.ncbi.nlm.nih.gov/41763294/) | pubmed.ncbi.nlm.nih.gov | 8 | negative |
| 25 Feb 2026 | [The Impact of Technology on Education - and What It Means for the Future of Learning](https://www.linkedin.com/pulse/impact-technology-education-what-means-future-fmlle) | linkedin.com | 8 | negative |
| 18 Feb 2026 | [AI, Robotics & Tech: The Future of Orthopedic Surgery - News Directory 3](https://www.newsdirectory3.com/ai-robotics-tech-the-future-of-orthopedic-surgery/) | newsdirectory3.com | 8 | positive |
| 5 Feb 2026 | [Stanford, Princeton scientists launch MedOS AI-XR-cobot clinical system - The Robot Report](https://www.therobotreport.com/stanford-princeton-scientists-launch-medos-ai-xr-cobot-clinical-system/) | therobotreport.com | 8 | positive |
| 29 Jan 2026 | [Meta's Reality Labs Records $19 Billion Loss as Strategic Focus Shifts](https://datafloq.com/metas-reality-labs-records-19-billion-loss-as-strategic-focus-shifts/) | datafloq.com | 8 | negative |
| 29 Jan 2026 | [Meta burned $19 billion on VR last year, and 2026 won’t be any better \| TechCrunch](https://techcrunch.com/2026/01/28/meta-burned-19-billion-on-vr-last-year-and-2026-wont-be-any-better/) | techcrunch.com | 8 | negative |
| 14 Jan 2026 | [Meta Scales Back Virtual Reality as Layoffs Signal Shift Toward AI](https://www.europeanbusinessreview.com/meta-scales-back-virtual-reality-as-layoffs-signal-shift-toward-ai/) | europeanbusinessreview.com | 8 | negative |
| 13 Jan 2026 | [Meta Reportedly Set to Axe 10% of Reality Labs Jobs](https://www.uctoday.com/immersive-workplace-xr-tech/meta-reportedly-reality-labs-layoffs-ai-priority/) | uctoday.com | 8 | negative |
| 30 Apr 2026 | [YouTube Premium crosses a new milestone as more users give in](https://www.phonearena.com/news/youtube-premium-crosses-new-milestone_id180075) | phonearena.com | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "virtual reality" --since 2026-01-01 --until 2026-04-30
prism-news trends "virtual reality" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "virtual reality" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "virtual reality", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "virtual reality", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Streaming News](streaming-news.md)
- [AI Agents News](ai-agents-news.md)
- [Android News](android-news.md)
- [Data Breach News](data-breach-news.md)
