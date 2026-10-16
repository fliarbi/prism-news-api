# Repo Rate News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “repo rate news” · 2,900/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [repo-rate-news.json](../../examples/scenarios/repo-rate-news.json).

**Question.** What did the news say about repo rate between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="repo rate"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 981 |
| Negative · neutral · positive | 26% · 17% · 57% |
| Critical (priority 7–9) | 75% (735 articles) |
| Busiest month, May 2025 – Apr 2026 | Jun 2025 (774 articles) |
| Most-reported country | India (29% of matches) |
| Strongest theme by lift | economy news: monetary policy changes |

## Twelve months of coverage

Monthly matching articles for `repo rate` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 115 | 53% | 35 | 72 | ███ |
| Jun 2025 | 774 | 66% | 279 | 437 | ████████████████████ |
| Jul 2025 | 205 | 59% | 76 | 104 | █████ |
| Aug 2025 | 437 | 68% | 143 | 237 | ███████████ |
| Sep 2025 | 131 | 66% | 42 | 52 | ███ |
| Oct 2025 | 242 | 70% | 50 | 160 | ██████ |
| Nov 2025 | 100 | 77% | 49 | 31 | ███ |
| Dec 2025 | 495 | 76% | 171 | 276 | █████████████ |
| Jan 2026 | 110 | 78% | 43 | 60 | ███ |
| Feb 2026 | 377 | 71% | 63 | 236 | ██████████ |
| Mar 2026 | 75 | 71% | 31 | 35 | ██ |
| Apr 2026 | 419 | 78% | 114 | 230 | ███████████ |

The last four complete months averaged 245 articles a month against 383 in the first four (-36%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 287 | 29% |
| United States | 95 | 9.7% |
| Iran | 28 | 2.9% |
| South Africa | 22 | 2.2% |
| China | 6 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: monetary policy changes | 312 | 48% | -12% |
| economy news: central bank interest rate decisions | 311 | 47% | -14% |
| foreign exchange (forex) rate fluctuations | 115 | 18% | +20% |
| economy news: inflation rate analysis | 274 | 42% | -10% |
| emerging markets economic updates | 56 | 8.6% | -2% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 14 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [RBI Maintains Repo Rate at 5.25% Amid Global Economic Uncertainty](https://currentaffairs.adda247.com/rbi-maintains-repo-rate-at-5-25-amid-global-economic-uncertainty/) | currentaffairs.adda247.com | 8 | positive |
| 9 Apr 2026 | [RBI holds the line: Stability signal amid global storm, growth engine intact](https://navjeevanexpress.com/rbi-holds-the-line-stability-signal-amid-global-storm-growth-engine-intact/) | navjeevanexpress.com | 8 | positive |
| 8 Apr 2026 | [RBI holds repo rate, sees GDP growth slowing to 6.9% in FY27](https://indianexpress.com/article/business/economy/rbi-holds-repo-rate-sees-gdp-growth-slowing-to-6-9-in-fy27-10626603/) | indianexpress.com | 8 | negative |
| 8 Apr 2026 | [RBI Keeps Repo Rate Unchanged, Experts Back Cautious Stance](https://www.newkerala.com/news/a/economists-industry-leaders-support-rbis-cautious-stance-as-923.htm) | newkerala.com | 8 | positive |
| 8 Apr 2026 | [RBI Pauses Rates: Analysts See Balanced Inflation, Growth Stance](https://www.newkerala.com/news/a/rbis-rate-pause-balances-inflation-control-growth-support-804.htm) | newkerala.com | 8 | positive |
| 8 Apr 2026 | [Banks, NBFCs back RBI status quo; expect steady rates to support credit growth](https://www.fortuneindia.com/markets/banks-nbfcs-back-rbi-status-quo-expect-steady-rates-to-support-credit-growth/132041) | fortuneindia.com | 8 | positive |
| 8 Apr 2026 | [RBI Maintains Repo Rate at 5.25% Amid Global Tensions](https://theunn.com/rbi-maintains-repo-rate-at-525-amid-global-tensions/) | theunn.com | 8 | positive |
| 8 Apr 2026 | [RBI policy seen as dovish, but experts warn hikes may return if oil and rupee risks worsen - CNBC TV18](https://www.cnbctv18.com/economy/rbi-monetary-policy-dovish-external-pressures-rate-hike-forecasts-economists-ws-l-19883134.htm) | cnbctv18.com | 8 | negative |
| 8 Apr 2026 | [RBI Projects FY27 GDP Growth At 6.9%, Holds Rates Amid Global Risks](https://www.freepressjournal.in/business/rbi-projects-fy27-gdp-growth-at-69-holds-rates-amid-global-risks) | freepressjournal.in | 8 | positive |
| 8 Apr 2026 | [RBI sounds alarm: 5 big risks for India as Iran war threatens economy](https://m.economictimes.indiatimes.com/news/economy/indicators/rbi-sounds-alarm-5-big-risks-for-india-as-iran-war-threatens-economy/videoshow/130111527.cms) | m.economictimes.indiatimes.com | 8 | negative |
| 8 Apr 2026 | [AU Small Finance Bank Comments on RBI Monetary Policy - Online Media Cafe](https://onlinemediacafe.com/business/au-small-finance-bank-comments-on-rbi-monetary-policy/) | onlinemediacafe.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "repo rate" --since 2026-01-01 --until 2026-04-30
prism-news trends "repo rate" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "repo rate" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "repo rate", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "repo rate", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Private Equity News](private-equity-news.md)
- [Pension News](pension-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
- [Rupee News](rupee-news.md)
