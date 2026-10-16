# Tariffs News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tariffs news” · 60,500/month India · 110,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [tariffs-news.json](../../examples/scenarios/tariffs-news.json).

**Question.** How did coverage of tariffs develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="tariffs"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 63,958 |
| Negative · neutral · positive | 65% · 9.6% · 25% |
| Critical (priority 7–9) | 75% (48,124 articles) |
| Busiest month, May 2025 – Apr 2026 | Jul 2025 (32,519 articles) |
| Most-reported country | United States (30% of matches) |
| Strongest theme by lift | trade agreements and free trade zones |

## Twelve months of coverage

Monthly matching articles for `tariffs` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 32,199 | 76% | 22,218 | 9,200 | ████████████████████ |
| Jun 2025 | 13,166 | 72% | 8,733 | 4,036 | ████████ |
| Jul 2025 | 32,519 | 70% | 23,455 | 7,913 | ████████████████████ |
| Aug 2025 | 30,174 | 77% | 21,244 | 7,824 | ███████████████████ |
| Sep 2025 | 18,887 | 78% | 12,566 | 5,722 | ████████████ |
| Oct 2025 | 17,036 | 78% | 11,193 | 5,370 | ██████████ |
| Nov 2025 | 10,254 | 76% | 6,745 | 3,153 | ██████ |
| Dec 2025 | 8,864 | 75% | 5,460 | 3,119 | █████ |
| Jan 2026 | 17,608 | 80% | 12,519 | 4,577 | ███████████ |
| Feb 2026 | 27,953 | 71% | 16,510 | 6,518 | █████████████████ |
| Mar 2026 | 8,514 | 77% | 5,821 | 2,392 | █████ |
| Apr 2026 | 9,883 | 76% | 6,705 | 2,790 | ██████ |

The last four complete months averaged 15,990 articles a month against 27,014 in the first four (-41%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 19,432 | 30% |
| India | 5,792 | 9.1% |
| China | 1,632 | 2.5% |
| Canada | 503 | 0.8% |
| United Kingdom | 452 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| trade agreements and free trade zones | 1,368 | 3.5% | +203% |
| political economy and resource allocation | 1,229 | 3.1% | +146% |
| economy news: trade deficit/surplus announcements | 1,168 | 3.0% | +106% |
| economy news: global trade agreements | 1,830 | 4.6% | +50% |
| trade policies and agreements | 14,430 | 37% | +4% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Portion of road to close for 1 week in Moraine](https://www.yahoo.com/news/articles/portion-road-close-1-week-072959599.html) | yahoo.com | 9 | negative |
| 12 Apr 2026 | [Trump threatens 50% tariff on China if it sends arms to Iran](https://www.dailysabah.com/world/mid-east/trump-threatens-50-tariff-on-china-if-it-sends-arms-to-iran) | dailysabah.com | 9 | negative |
| 7 Apr 2026 | [Relief in the streets as US, Iran agree to a 2-week truce](https://www.businesstimes.com.sg/international/global/relief-streets-us-iran-agree-2-week-truce) | businesstimes.com.sg | 9 | negative |
| 1 Mar 2026 | [Trump cheers death of Iranian leader, says strikes will continue - Middle East and Africa - The Jakarta Post](http://www.thejakartapost.com/world/2026/03/01/trump-cheers-death-of-iranian-leader-says-strikes-will-continue.html) | thejakartapost.com | 9 | negative |
| 26 Feb 2026 | [Letter: Are you going to let Trump drag us into another war?](https://www.inforum.com/opinion/letters/letter-are-you-going-to-let-trump-drag-us-into-another-war) | inforum.com | 9 | negative |
| 21 Feb 2026 | ['India Deal Is On': Trump Reacts To US Supreme Court Decision On Tariffs](https://news.abplive.com/news/india-deal-is-on-donald-trump-reacts-to-us-supreme-court-decision-on-tariffs-1828062) | news.abplive.com | 9 | negative |
| 20 Feb 2026 | [Trump says 32,000 people were killed in Iran's crackdown on protesters](https://www.yahoo.com/news/articles/trump-says-32-000-people-200600845.html) | yahoo.com | 9 | negative |
| 20 Feb 2026 | [Trump calls Supreme Court decision to overturn most of his tariffs a ‘disgrace’](https://english.elpais.com/usa/2026-02-20/trump-calls-supreme-court-decision-to-overturn-most-of-his-tariffs-a-disgrace.html) | english.elpais.com | 9 | negative |
| 11 Feb 2026 | ['Would have been a nuclear war,' Trump reiterates claim of stopping India-Pakistan conflict](https://economictimes.indiatimes.com/news/india/would-have-been-a-nuclear-war-trump-reiterates-claim-of-stopping-india-pakistan-conflict/articleshow/128184021.cms) | economictimes.indiatimes.com | 9 | negative |
| 11 Feb 2026 | ['Would Have Been a Nuclear War', Trump Reiterates Claim of Stopping India-Pakistan Conflict](https://www.republicworld.com/world-news/would-have-been-a-nuclear-war-trump-reiterates-claim-of-stopping-india-pakistan-conflict) | republicworld.com | 9 | negative |
| 13 Jan 2026 | [Iran protests: Tehran acknowledges 2,000 deaths as US pressure escalates](http://gulfnews.com/world/mena/iran-protests-tehran-acknowledges-2000-deaths-as-us-pressure-escalates-1.500407132) | gulfnews.com | 9 | negative |
| 13 Jan 2026 | [Trump Issues Iran Ultimatum: Slaps 25% Tariff On Any Country Doing Business With 'Islamic Republic' — Say](https://www.benzinga.com/news/politics/26/01/49865053/trump-issues-iran-ultimatum-threatens-25-tariff-on-any-country-doing-business-with-islamic-republic-says-this-order-is-final) | benzinga.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "tariffs" --since 2026-01-01 --until 2026-04-30
prism-news trends "tariffs" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "tariffs" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "tariffs", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "tariffs", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Supreme Court News](supreme-court-news.md)
- [AI Regulation News](ai-regulation-news.md)
- [Food Safety News](food-safety-news.md)
