# Make in India News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “make in india news” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [make-in-india-news.json](../../examples/scenarios/make-in-india-news.json).

**Question.** How did coverage of make in india develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="make in india"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 716 |
| Negative · neutral · positive | 3.9% · 1.0% · 95% |
| Critical (priority 7–9) | 73% (524 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (297 articles) |
| Most-reported country | India (54% of matches) |
| Strongest theme by lift | aviation industry aerospace defense contracting |

## Twelve months of coverage

Monthly matching articles for `make in india` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 158 | 74% | 17 | 138 | ███████████ |
| Jun 2025 | 211 | 67% | 18 | 193 | ██████████████ |
| Jul 2025 | 179 | 58% | 22 | 155 | ████████████ |
| Aug 2025 | 297 | 71% | 24 | 270 | ████████████████████ |
| Sep 2025 | 246 | 76% | 10 | 234 | █████████████████ |
| Oct 2025 | 173 | 78% | 7 | 164 | ████████████ |
| Nov 2025 | 107 | 69% | 5 | 101 | ███████ |
| Dec 2025 | 107 | 74% | 4 | 103 | ███████ |
| Jan 2026 | 165 | 69% | 3 | 160 | ███████████ |
| Feb 2026 | 270 | 73% | 16 | 253 | ██████████████████ |
| Mar 2026 | 133 | 80% | 4 | 129 | █████████ |
| Apr 2026 | 148 | 71% | 5 | 139 | ██████████ |

The last four complete months averaged 179 articles a month against 211 in the first four (-15%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 66% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 387 | 54% |
| United States | 43 | 6.0% |
| China | 11 | 1.5% |
| France | 5 | 0.7% |
| Japan | 3 | 0.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| aviation industry aerospace defense contracting | 25 | 6.1% | +212% |
| company expansions and new market entries | 66 | 16% | +100% |
| aviation industry military aircraft development | 22 | 5.3% | +175% |
| global market entry strategies | 54 | 13% | +38% |
| aviation industry aircraft manufacturing processes | 18 | 4.4% | +800% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Make in India: Strengthening Manufacturing Growth \| IBEF](https://www.ibef.org/research/case-study/how-make-in-india-is-strengthening-manufacturing-industries-in-india) | ibef.org | 8 | positive |
| 26 Apr 2026 | [Robust indigenous materials supply chain: Key to Next-Gen Defence Capabilities - The Times of India](https://timesofindia.indiatimes.com/defence/news/robust-indigenous-materials-supply-chain-key-to-next-gen-defence-capabilities/articleshow/130534319.cms) | timesofindia.indiatimes.com | 8 | positive |
| 23 Apr 2026 | [Mahindra & Mahindra patent portfolio grows 20x over a decade \| SportsZ News](https://sportsz.news/news/mahindra-mahindra-patent-portfolio-grows-20x-over-a-decade/) | sportsz.news | 8 | positive |
| 23 Apr 2026 | [Mahindra & Mahindra patent portfolio grows 20x over a decade](https://businessnewsthisweek.com/news/mahindra-mahindra-patent-portfolio-grows-20x-over-a-decade/) | businessnewsthisweek.com | 8 | positive |
| 20 Apr 2026 | [Selfie Diplomacy: Samsung's Foldable Tech Steals the Spotlight \| International](https://www.devdiscourse.com/article/international/3881095-selfie-diplomacy-samsungs-foldable-tech-steals-the-spotlight) | devdiscourse.com | 8 | positive |
| 20 Apr 2026 | [In a significant boost to the Centre’s Make in India push, JSW Steel and POSCO on Sunday announced plans to…](https://investmentguruindia.com/newsdetail/make-in-india-boost-jsw-steel-posco-to-set-up-6-mtpa-plant-in-odisha463685) | investmentguruindia.com | 8 | positive |
| 19 Apr 2026 | [JSW Steel, POSCO to set up 6 MTPA steel plant in Odisha](https://sambadenglish.com/latest-news/jsw-steel-posco-to-set-up-6-mtpa-steel-plant-in-odisha-11743734) | sambadenglish.com | 8 | positive |
| 19 Apr 2026 | [Make in India boost: JSW Steel, POSCO to set up 6 MTPA plant in Odisha - Social News XYZ](https://www.socialnews.xyz/2026/04/19/make-in-india-boost-jsw-steel-posco-to-set-up-6-mtpa-plant-in-odisha/) | socialnews.xyz | 8 | positive |
| 29 Mar 2026 | [Adani Defence delivers light machine guns to army](https://www.thehansindia.com/business/adani-defence-delivers-light-machine-guns-to-army-1060663) | thehansindia.com | 8 | positive |
| 24 Mar 2026 | [Altos Launches ‘Make in India’ AI Server Portfolio](https://www.constructionworld.in/latest-construction-technology/altos-launches---make-in-india----ai-server-portfolio/88476) | constructionworld.in | 8 | positive |
| 23 Feb 2026 | [IceBattery® Launches India’s First Net-Zero Rail & Land Cold Chain Platform with CONCOR - India Seatrade News](https://indiaseatradenews.com/icebattery-launches-indias-first-net-zero-rail-land-cold-chain-platform-with-concor/) | indiaseatradenews.com | 8 | positive |
| 19 Feb 2026 | [France pledges strong bilateral defence cooperation with India regarding the domestic production of 114…](https://defence.in/threads/france-pledges-strong-bilateral-defence-cooperation-with-india-regarding-the-domestic-production-of-114-rafale-aircraft.16946/) | defence.in | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "make in india" --since 2026-01-01 --until 2026-04-30
prism-news trends "make in india" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "make in india" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "make in india", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "make in india", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [National Security News](national-security-news.md)
- [Climate Policy News](climate-policy-news.md)
- [Sanctions News](sanctions-news.md)
- [Banking Regulation News](banking-regulation-news.md)
