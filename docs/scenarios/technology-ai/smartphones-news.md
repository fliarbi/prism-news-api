# Smartphones News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “smartphones news” · 320/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [smartphones-news.json](../../examples/scenarios/smartphones-news.json).

**Question.** How much smartphones coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="smartphones"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 13,239 |
| Negative · neutral · positive | 16% · 1.6% · 83% |
| Critical (priority 7–9) | 23% (3,088 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (4,128 articles) |
| Most-reported country | United States (9.4% of matches) |
| Strongest theme by lift | mobile phone hardware components |

## Twelve months of coverage

Monthly matching articles for `smartphones` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,750 | 23% | 428 | 2,239 | █████████████ |
| Jun 2025 | 2,382 | 25% | 460 | 1,890 | ████████████ |
| Jul 2025 | 3,315 | 20% | 526 | 2,743 | ████████████████ |
| Aug 2025 | 4,128 | 24% | 729 | 3,320 | ████████████████████ |
| Sep 2025 | 3,448 | 22% | 418 | 2,972 | █████████████████ |
| Oct 2025 | 2,621 | 23% | 390 | 2,201 | █████████████ |
| Nov 2025 | 2,324 | 22% | 310 | 1,981 | ███████████ |
| Dec 2025 | 2,866 | 29% | 587 | 2,237 | ██████████████ |
| Jan 2026 | 2,691 | 23% | 434 | 2,204 | █████████████ |
| Feb 2026 | 3,456 | 24% | 529 | 2,883 | █████████████████ |
| Mar 2026 | 3,449 | 22% | 497 | 2,900 | █████████████████ |
| Apr 2026 | 3,643 | 24% | 627 | 2,955 | ██████████████████ |

The last four complete months averaged 3,310 articles a month against 3,144 in the first four (+5%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,251 | 9.4% |
| India | 1,193 | 9.0% |
| South Korea | 894 | 6.8% |
| China | 357 | 2.7% |
| United Kingdom | 212 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone hardware components | 767 | 9.3% | +64% |
| mobile phone battery performance | 740 | 8.9% | +30% |
| latest gadgets and consumer electronics | 970 | 12% | +24% |
| mobile operating systems | 1,117 | 14% | -9% |
| mobile phone camera technology | 676 | 8.2% | +30% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [AI features and design shape India’s smartphone buying trends](https://domain-b.com/technology/artificial-intelligence/india-smartphone-ai-design-trends-2026) | domain-b.com | 8 | positive |
| 30 Apr 2026 | [OpenAI Eyes AI-first Smartphone Launch by 2028](https://www.electronicsforyou.biz/industry-buzz/openai-eyes-ai-first-smartphone-launch-by-2028/) | electronicsforyou.biz | 8 | positive |
| 30 Apr 2026 | [Qualcomm Stock Surges 15% on AI Chips & Data Center Push](https://theoutpost.ai/news-story/qualcomm-stock-surges-15-as-ai-chips-and-data-center-expansion-fuel-investor-confidence-26073/) | theoutpost.ai | 8 | positive |
| 30 Apr 2026 | [Hormuud Telecom, Somalia’s telecom operator, has partnered with Mogadishu-based Get-Phone to launch a…](https://www.itnewsafrica.com/2026/05/somalia-launches-smartphone-financing-model-targeting-low-income-users/) | itnewsafrica.com | 8 | positive |
| 29 Apr 2026 | [OpenAI Is Building an AI Phone. Will It Take on the iPhone?](https://www.republicworld.com/tech/openai-is-building-an-ai-phone-will-it-take-on-the-iphone) | republicworld.com | 8 | positive |
| 28 Apr 2026 | [Smartphones Emerge as India’s Top Export, Says Ashwini Vaishnaw - India Seatrade News](https://indiaseatradenews.com/smartphones-emerge-as-indias-top-export-says-ashwini-vaishnaw/) | indiaseatradenews.com | 8 | positive |
| 27 Apr 2026 | [OpenAI reportedly working with Qualcomm and MediaTek to build custom chips for AI-first smartphones - The…](https://thetechportal.com/2026/04/27/openai-reportedly-working-with-qualcomm-and-mediatek-to-build-custom-chips-for-ai-first-smartphones/) | thetechportal.com | 8 | positive |
| 27 Apr 2026 | [Expert issues warning to iPhone and Android users as video shows phone flashlight melting through plastic](https://www.uniladtech.com/news/tech-news/expert-warning-phone-flashlight-melting-through-plastic-412827-20260427) | uniladtech.com | 8 | negative |
| 27 Apr 2026 | [OpenAI Eyes 'AI Agent' Smartphone With Qualcomm And MediaTek, Targets App-Free Experience By 2028: Report](https://www.benzinga.com/markets/tech/26/04/52056811/openai-eyes-ai-agent-smartphone-with-qualcomm-and-mediatek-targets-app-free-experience-by-2028-report) | benzinga.com | 8 | positive |
| 25 Apr 2026 | [📱 Aadhaar App Pre-Install Plan Dropped: Government Withdraws Proposal](https://www.indiaherald.com/Politics/Read/994888495/-Aadhaar-App-PreInstall-Plan-Dropped-Government-Withdraws-Proposal) | indiaherald.com | 8 | negative |
| 25 Apr 2026 | [Kaspersky Discovers Vulnerability in Qualcomm Snapdragon Chips that can Lead to Data Loss & Device Compromise](https://www.nigeriacommunicationsweek.com.ng/kaspersky-discovers-vulnerability-in-qualcomm-snapdragon-chips-that-can-lead-to-data-loss-device-compromise/) | nigeriacommunicationsweek.com.ng | 8 | negative |
| 23 Apr 2026 | [Meta’s new AI feature lets parents track teen conversations \| Stuff](https://www.stuff.tv/news/metas-new-ai-feature-lets-parents-track-teen-conversations/) | stuff.tv | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "smartphones" --since 2026-01-01 --until 2026-04-30
prism-news trends "smartphones" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "smartphones" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "smartphones", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "smartphones", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cloud Security News](cloud-security-news.md)
- [Wearables News](wearables-news.md)
- [X Twitter News](x-twitter-news.md)
- [AI Startups News](ai-startups-news.md)
