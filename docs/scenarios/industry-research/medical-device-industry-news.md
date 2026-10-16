# Medical Device Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “medical device industry news” · 90/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [medical-device-industry-news.json](../../examples/scenarios/medical-device-industry-news.json).

**Question.** How much news did the medical device industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="medical device industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 158 |
| Negative · neutral · positive | 18% · 0.0% · 82% |
| Critical (priority 7–9) | 57% (90 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (94 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | quality control in pharmaceutical manufacturing |

## Twelve months of coverage

Monthly matching articles for `medical device industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 30 | 60% | 6 | 24 | ██████ |
| Jun 2025 | 27 | 63% | 4 | 23 | ██████ |
| Jul 2025 | 27 | 52% | 0 | 27 | ██████ |
| Aug 2025 | 23 | 56% | 2 | 21 | █████ |
| Sep 2025 | 34 | 65% | 5 | 29 | ███████ |
| Oct 2025 | 44 | 64% | 3 | 41 | █████████ |
| Nov 2025 | 94 | 17% | 1 | 92 | ████████████████████ |
| Dec 2025 | 43 | 42% | 2 | 41 | █████████ |
| Jan 2026 | 35 | 54% | 5 | 30 | ███████ |
| Feb 2026 | 34 | 65% | 9 | 25 | ███████ |
| Mar 2026 | 49 | 57% | 10 | 39 | ██████████ |
| Apr 2026 | 40 | 52% | 4 | 36 | █████████ |

The last four complete months averaged 40 articles a month against 27 in the first four (+48%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 42 | 27% |
| China | 11 | 7.0% |
| India | 9 | 5.7% |
| Brazil | 6 | 3.8% |
| United Kingdom | 3 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| quality control in pharmaceutical manufacturing | 8 | 8.4% | +14% |
| disposable medical supplies and consumables | 8 | 8.4% | +167% |
| medical device safety and compliance standards | 7 | 7.4% | -22% |
| regulatory compliance (fda, ema, etc.) | 7 | 7.4% | +75% |
| pharmaceutical manufacturing techniques | 6 | 6.3% | +100% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 3 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Feb 2026 | [AdvaMed calls for 'certainty and stability' after Trump tariffs ruled illegal](https://www.medicaldesignandoutsourcing.com/advamed-trump-tariffs-ruled-illegal/) | medicaldesignandoutsourcing.com | 8 | negative |
| 29 Apr 2026 | [Director Chen Sicheng discusses his new movie Being Towards Deathat a recent promotional event in…](http://www.chinadaily.com.cn/a/202604/29/WS69f1a309a310d6866eb4637d.html) | chinadaily.com.cn | 7 | negative |
| 27 Apr 2026 | [Rising Tide in Southeast Asia: A New Global Chapter for China’s MedTech Industry](https://www.lek.com/insights/medtech/rising-tide-southeast-asia-new-global-chapter-chinas-medtech-industry) | lek.com | 7 | positive |
| 25 Apr 2026 | [Baja California alcanza los 100 mil empleos en la industria de dispositivos médicos; Marina del Pilar…](https://www.eluniversal.com.mx/estados/baja-california-alcanza-los-100-mil-empleos-en-la-industria-de-dispositivos-medicos-marina-del-pilar-destaca-innovacion/) | eluniversal.com.mx | 7 | positive |
| 28 Jan 2026 | [India-EU FTA a Boost for Medical Device Sector, Say Experts - India Seatrade News](https://indiaseatradenews.com/india-eu-fta-a-boost-for-medical-device-sector-say-experts/) | indiaseatradenews.com | 7 | positive |
| 1 Jan 2026 | [Med device task guide for UK conformity post-Brexit \| Pharmaceutical Commerce](https://www.pharmaceuticalcommerce.com/view/med-device-task-guide-for-uk-conformity-post-brexit) | pharmaceuticalcommerce.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "medical device industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "medical device industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "medical device industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "medical device industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "medical device industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cocoa Industry](cocoa-industry.md)
- [Glass Industry](glass-industry.md)
- [Railway Industry](railway-industry.md)
