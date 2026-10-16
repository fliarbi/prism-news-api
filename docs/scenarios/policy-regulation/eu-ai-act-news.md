# EU AI Act News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “eu ai act news” · 10/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [eu-ai-act-news.json](../../examples/scenarios/eu-ai-act-news.json).

**Question.** How did coverage of eu ai act develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="AI Act"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 649 |
| Negative · neutral · positive | 31% · 2.5% · 67% |
| Critical (priority 7–9) | 81% (523 articles) |
| Busiest month, May 2025 – Apr 2026 | Jul 2025 (269 articles) |
| Most-reported country | United States (14% of matches) |
| Strongest theme by lift | network compliance and auditing standards |

## Twelve months of coverage

Monthly matching articles for `AI Act` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 95 | 82% | 40 | 54 | ███████ |
| Jun 2025 | 109 | 85% | 41 | 62 | ████████ |
| Jul 2025 | 269 | 80% | 102 | 160 | ████████████████████ |
| Aug 2025 | 167 | 86% | 53 | 111 | ████████████ |
| Sep 2025 | 148 | 87% | 45 | 101 | ███████████ |
| Oct 2025 | 191 | 75% | 46 | 143 | ██████████████ |
| Nov 2025 | 235 | 91% | 106 | 124 | █████████████████ |
| Dec 2025 | 154 | 83% | 43 | 109 | ███████████ |
| Jan 2026 | 140 | 77% | 40 | 100 | ██████████ |
| Feb 2026 | 158 | 79% | 53 | 99 | ████████████ |
| Mar 2026 | 161 | 81% | 44 | 112 | ████████████ |
| Apr 2026 | 190 | 84% | 63 | 122 | ██████████████ |

The last four complete months averaged 162 articles a month against 160 in the first four (+1%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 31% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 94 | 14% |
| United Kingdom | 24 | 3.7% |
| France | 15 | 2.3% |
| Belgium | 10 | 1.5% |
| Ireland | 9 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| network compliance and auditing standards | 26 | 5.7% | +2500% |
| ai in cybersecurity applications | 63 | 14% | +12% |
| ethical considerations in ai development | 172 | 38% | -11% |
| explainable ai (xai) techniques | 25 | 5.5% | -29% |
| compliance and regulatory risk controls | 13 | 2.9% | +44% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [EU AI Act Update: Omnibus Talks Stall, but Clock Is Still Ticking](https://natlawreview.com/article/eu-ai-act-update-omnibus-talks-stall-clock-still-ticking) | natlawreview.com | 8 | negative |
| 21 Apr 2026 | [AI Act and Digital Omnibus Integration of AI and health data 2026](https://www.taylorwessing.com/en/international-life-sciences-newsletter/life-sciences-legal-lens-vol-1/ai-act-and-digital-omnibus-integration-of-ai-and-health-data-2026) | taylorwessing.com | 8 | positive |
| 13 Apr 2026 | [Musk’s xAI Sues Colorado Over Landmark AI Regulation \| PYMNTS.com](https://www.pymnts.com/cpi-posts/musks-xai-sues-colorado-over-landmark-ai-regulation/) | pymnts.com | 8 | negative |
| 2 Apr 2026 | [Latest News Bureau Veritas Launches an Independent AI Assessment Offering for European Enterprises,…](https://businessfortnight.com/bureau-veritas-launches-an-independent-ai-assessment-offering-for-european-enterprises-developed-in-partnership-with-amazon-web-services-aws/) | businessfortnight.com | 8 | positive |
| 27 Mar 2026 | [EU Parliament backs delaying AI Act deadlines for biometrics, high-risk applications \| Biometric Update](https://www.biometricupdate.com/202603/eu-parliament-backs-delaying-ai-act-deadlines-for-biometrics-high-risk-applications) | biometricupdate.com | 8 | negative |
| 26 Mar 2026 | [45 industry associations sign joint statement to boost Europe's AI competitiveness](https://www.dqindia.com/esdm/45-industry-associations-sign-joint-statement-to-boost-europes-ai-competitiveness-11254940) | dqindia.com | 8 | negative |
| 13 Mar 2026 | [European Council includes ban on nudification tools in its proposal for amending AI Act](https://therecord.media/european-council-includes-nudification-ban-ai-act) | therecord.media | 8 | negative |
| 12 Mar 2026 | [EU lawmakers deal to ban AI non-consensual intimate deepfakes](https://thenextweb.com/news/eu-lawmakers-deal-to-ban-ai-non-consensual-intimate-deepfakes) | thenextweb.com | 8 | negative |
| 17 Feb 2026 | [EU: EDPB and EDPS publish joint opinion on the European Commission’s Proposal for the Digital Omnibus on AI](https://www.jdsupra.com/legalnews/eu-edpb-and-edps-publish-joint-opinion-1310614/) | jdsupra.com | 8 | positive |
| 16 Feb 2026 | [“Deepfake scams hurt everyone, but Big Tech platforms don’t care” says EBU in call for evidence](https://www.ebu.ch/news/2026/02/deepfake-scams-hurt-everyone-but-big-tech-platforms-don-t-care-says-ebu-in-call-for-evidence) | ebu.ch | 8 | negative |
| 6 Jan 2026 | [CES26: EU, South Korea Frame Early Global Push for AI Regulation](https://broadbandbreakfast.com/ces26-eu-south-korea-frame-early-global-push-for-ai-regulation/) | broadbandbreakfast.com | 8 | positive |
| 29 Apr 2026 | [PRAD The European Digital Capacity Index](https://www.politico.eu/prad-the-european-digital-capacity-index/) | politico.eu | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "AI Act" --since 2026-01-01 --until 2026-04-30
prism-news trends "AI Act" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "AI Act" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "AI Act", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "AI Act", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Food Safety News](food-safety-news.md)
- [Medicare News](medicare-news.md)
- [Citizenship News](citizenship-news.md)
- [Obamacare News](obamacare-news.md)
