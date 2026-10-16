# Obamacare News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “obamacare news” · 10/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [obamacare-news.json](../../examples/scenarios/obamacare-news.json).

**Question.** How did coverage of obamacare develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="obamacare"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 800 |
| Negative · neutral · positive | 87% · 0.4% · 13% |
| Critical (priority 7–9) | 91% (731 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (1,494 articles) |
| Most-reported country | United States (54% of matches) |
| Strongest theme by lift | aca (affordable care act) health insurance policies |

## Twelve months of coverage

Monthly matching articles for `obamacare` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 332 | 82% | 285 | 36 | ████ |
| Jun 2025 | 241 | 85% | 227 | 14 | ███ |
| Jul 2025 | 612 | 63% | 541 | 67 | ████████ |
| Aug 2025 | 1,494 | 72% | 1,323 | 160 | ████████████████████ |
| Sep 2025 | 261 | 95% | 244 | 17 | ███ |
| Oct 2025 | 1,273 | 92% | 1,207 | 59 | █████████████████ |
| Nov 2025 | 1,041 | 93% | 952 | 74 | ██████████████ |
| Dec 2025 | 1,048 | 79% | 895 | 103 | ██████████████ |
| Jan 2026 | 277 | 96% | 235 | 41 | ████ |
| Feb 2026 | 197 | 92% | 154 | 42 | ███ |
| Mar 2026 | 158 | 92% | 146 | 12 | ██ |
| Apr 2026 | 168 | 82% | 158 | 9 | ██ |

The last four complete months averaged 200 articles a month against 670 in the first four (-70%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 56% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 435 | 54% |
| Iran | 4 | 0.5% |
| Ukraine | 2 | 0.2% |
| United Kingdom | 2 | 0.2% |
| Cuba | 1 | 0.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| aca (affordable care act) health insurance policies | 67 | 14% | -92% |
| health insurance marketplaces and exchanges | 39 | 8.2% | -60% |
| health insurance subsidies and tax credits | 56 | 12% | -91% |
| health insurance coverage and reform policies | 69 | 15% | -80% |
| mental health policy and advocacy | 26 | 5.5% | — |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Terry Savage: The health insurance sinkhole](https://www.chicagotribune.com/2026/04/23/terry-savage-the-health-insurance-sinkhole/) | chicagotribune.com | 8 | negative |
| 11 Apr 2026 | [Ezekiel Emanuel: ACA Has Done Good, But 'The System Sucks, It's Broken'](https://www.breitbart.com/clips/2026/04/11/ezekiel-emanuel-aca-has-done-good-but-the-system-sucks-its-broken/) | breitbart.com | 8 | negative |
| 28 Mar 2026 | [Analysis: Trump keeps saying ‘nobody’ knew or expected things lots of people knew or expected \| CNN Politics](https://www.cnn.com/2026/03/28/politics/trump-claims-nobody-knows-quotes) | cnn.com | 8 | negative |
| 27 Mar 2026 | [Rising health costs push some middle-aged adults to skip the doctor until Medicare](https://www.sandiegouniontribune.com/2026/03/27/waiting-until-medicare/) | sandiegouniontribune.com | 8 | negative |
| 26 Mar 2026 | [Travis Kelce Admits He Had a Job Selling Obamacare Before Being Drafted by the Chiefs](https://us.headtopics.com/news/travis-kelce-admits-he-had-a-job-selling-obamacare-before-81488793) | us.headtopics.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "obamacare" --since 2026-01-01 --until 2026-04-30
prism-news trends "obamacare" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "obamacare" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "obamacare", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "obamacare", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [EU AI Act News](eu-ai-act-news.md)
- [Citizenship News](citizenship-news.md)
- [Trade War News](trade-war-news.md)
- [MSP News](msp-news.md)
