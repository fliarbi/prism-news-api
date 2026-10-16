# Esports News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “esports news” · 1,000/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [esports-news.json](../../examples/scenarios/esports-news.json).

**Question.** How much esports coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="esports"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,152 |
| Negative · neutral · positive | 9.5% · 2.2% · 88% |
| Critical (priority 7–9) | 22% (474 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (774 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | gaming controllers and computer gaming peripherals |

## Twelve months of coverage

Monthly matching articles for `esports` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 631 | 17% | 51 | 559 | ████████████████ |
| Jun 2025 | 405 | 22% | 50 | 351 | ██████████ |
| Jul 2025 | 590 | 22% | 48 | 521 | ███████████████ |
| Aug 2025 | 774 | 37% | 125 | 640 | ████████████████████ |
| Sep 2025 | 634 | 28% | 84 | 543 | ████████████████ |
| Oct 2025 | 603 | 26% | 62 | 530 | ████████████████ |
| Nov 2025 | 502 | 21% | 32 | 468 | █████████████ |
| Dec 2025 | 422 | 18% | 37 | 383 | ███████████ |
| Jan 2026 | 475 | 19% | 34 | 435 | ████████████ |
| Feb 2026 | 517 | 24% | 48 | 461 | █████████████ |
| Mar 2026 | 468 | 25% | 46 | 406 | ████████████ |
| Apr 2026 | 692 | 20% | 76 | 599 | ██████████████████ |

The last four complete months averaged 538 articles a month against 600 in the first four (-10%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 55% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 394 | 18% |
| India | 167 | 7.8% |
| United Kingdom | 88 | 4.1% |
| Saudi Arabia | 60 | 2.8% |
| China | 51 | 2.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| gaming controllers and computer gaming peripherals | 55 | 4.9% | +25% |
| esports sponsorship deals | 44 | 3.9% | +22% |
| esports revenue models | 42 | 3.8% | -11% |
| computer mice and pointing devices | 40 | 3.6% | +33% |
| esports collegiate programs | 31 | 2.8% | +19% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 1 Feb 2026 | [Ex-Free Fire Esports player and content creator Tahir Fuego dies by suicide](https://gamingonphone.com/news/ex-free-fire-esports-player-and-content-creator-tahir-fuego-dies-by-suicide/) | gamingonphone.com | 9 | negative |
| 18 Jan 2026 | [Sonmez becomes fan favourite in Melbourne after coming to aid of ball girl](https://www.straitstimes.com/sport/tennis/sonmez-becomes-fan-favourite-in-melbourne-after-coming-to-aid-of-ball-girl) ⚠ | straitstimes.com | 9 | negative |
| 24 Apr 2026 | [Hard-earned relief: Gaming leaders hail 2026 Rules as a green signal for global capital](https://www.adgully.com/post/14670/hard-earned-relief-gaming-leaders-hail-2026-rules-as-a-green-signal-for-global-capital) ⚠ | adgully.com | 8 | positive |
| 23 Apr 2026 | [Government Notifies Online Gaming Rules 2026, Effective from May 1](https://www.thequint.com/news/breaking-news/government-of-india-notifies-online-gaming-rules-2026-ban) ⚠ | thequint.com | 8 | positive |
| 23 Apr 2026 | [Govt centralises social gaming oversight under PROGA, limits TNOGA’s regulatory ambit? - Exchange4media](https://www.exchange4media.com/digital-news/govt-centralises-social-gaming-oversight-under-proga-limits-tnogas-regulatory-ambit-154080.html) | exchange4media.com | 8 | negative |
| 23 Apr 2026 | [Online Gaming Rules 2026 applauded for clarity, but industry flags gaps in oversight - Exchange4media](https://www.exchange4media.com/digital-news/online-gaming-rules-2026-applauded-for-clarity-but-industry-flags-gaps-in-oversight-154065.html) | exchange4media.com | 8 | positive |
| 22 Apr 2026 | [Govt notifies new online gaming rules to boost to esports](https://www.yourstory.com/2026/04/govt-notifies-new-online-gaming-rules-to-boost-to-esports) | yourstory.com | 8 | positive |
| 22 Apr 2026 | [India to Launch Much Needed Online Gaming Authority](https://www.gulte.com/shorts/407423/india-to-launch-much-needed-online-gaming-authority) | gulte.com | 8 | positive |
| 16 Apr 2026 | [Saudi PIF assets surge six-fold to $900bln](https://www.zawya.com/business/swf/saudi-pif-assets-surge-six-fold-to-900bln-d15368bs) ⚠ | zawya.com | 8 | positive |
| 12 Apr 2026 | [Markets Bet on Iran Conflict End](https://www.startuphub.ai/ai-news/prediction-markets/2026/markets-bet-on-iran-conflict-end) ⚠ | startuphub.ai | 8 | negative |
| 7 Apr 2026 | [8 months on, no clarity on PROGA implementation, half-baked OGAI website in testing phase released, then…](https://g2g.news/online-gaming-laws/8-months-on-no-clarity-on-proga-implementation-half-baked-ogai-website-in-testing-phase-released-then-withdrawn/) | g2g.news | 8 | positive |
| 7 Apr 2026 | [Outdated stereotypes: Elite university withdraws film after reducing female student to ‘mother’ role](https://thesun.my/going-viral/outdated-stereotypes-elite-university-withdraws-film-after-reducing-female-student-to-mother-role/) ⚠ | thesun.my | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "esports" --since 2026-01-01 --until 2026-04-30
prism-news trends "esports" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "esports" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "esports", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "esports", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Data Breach News](data-breach-news.md)
- [Generative AI News](generative-ai-news.md)
- [Cloud Computing News](cloud-computing-news.md)
- [Ransomware News](ransomware-news.md)
