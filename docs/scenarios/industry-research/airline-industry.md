# Airline Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “airline industry” · 480/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [airline-industry.json](../../examples/scenarios/airline-industry.json).

**Question.** How much news did the airline industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="airline industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 7,807 |
| Negative · neutral · positive | 59% · 1.8% · 39% |
| Critical (priority 7–9) | 62% (4,813 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,413 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | aviation fuel management |

## Twelve months of coverage

Monthly matching articles for `airline industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 937 | 59% | 386 | 533 | █████ |
| Jun 2025 | 748 | 58% | 316 | 407 | ████ |
| Jul 2025 | 985 | 51% | 423 | 546 | ██████ |
| Aug 2025 | 937 | 53% | 444 | 476 | █████ |
| Sep 2025 | 1,019 | 55% | 423 | 571 | ██████ |
| Oct 2025 | 902 | 54% | 357 | 534 | █████ |
| Nov 2025 | 1,078 | 60% | 487 | 556 | ██████ |
| Dec 2025 | 1,631 | 71% | 920 | 682 | ██████████ |
| Jan 2026 | 1,063 | 53% | 426 | 625 | ██████ |
| Feb 2026 | 1,303 | 60% | 621 | 659 | ████████ |
| Mar 2026 | 2,028 | 66% | 1,260 | 735 | ████████████ |
| Apr 2026 | 3,413 | 63% | 2,329 | 1,010 | ████████████████████ |

The last four complete months averaged 1,952 articles a month against 902 in the first four (+116%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,098 | 27% |
| India | 484 | 6.2% |
| Iran | 187 | 2.4% |
| United Kingdom | 151 | 1.9% |
| Nigeria | 148 | 1.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| aviation fuel management | 841 | 15% | +824% |
| airline bankruptcy and restructuring | 735 | 13% | +76% |
| air travel carbon offset initiatives | 688 | 12% | +664% |
| airline mergers and alliances | 626 | 11% | +69% |
| aviation industry commercial airline services | 369 | 6.5% | +111% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Mar 2026 | [$53 billion wiped out: Middle East war shakes global airline industry](https://www.indiatoday.in/business/story/middle-east-conflict-disrupts-global-airlines-jet-fuel-prices-surge-2885612-2026-03-22) | indiatoday.in | 9 | negative |
| 29 Apr 2026 | [ATF price surge threatens Ops: Airlines to govt](https://energy.economictimes.indiatimes.com/news/oil-and-gas/atf-price-surge-threatens-ops-airlines-to-govt/130600723) | energy.economictimes.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [Air India, IndiGo, SpiceJet seek ATF price revision, financial support from Centre; warn of possible…](http://livemint.com/industry/air-india-indigo-spicejet-seek-atf-price-revision-financial-support-from-centre-warn-of-possible-shutdown-11777389278700.html) | livemint.com | 8 | negative |
| 28 Apr 2026 | [Air India, IndiGo, SpiceJet warn of grounding aircraft amid ATF price surge; seek govt support](https://telanganatoday.com/air-india-indigo-spicejet-warn-of-grounding-aircraft-amid-atf-price-surge-seek-govt-support) | telanganatoday.com | 8 | negative |
| 28 Apr 2026 | [Is Indian Aviation Industry On Brink Of Shutdown? ATF Prices Surge Amid West Asia Conflict, FIA Seek Urgent…](https://www.newsx.com/india/is-indian-aviation-industry-on-brink-of-shutdown-atf-prices-surge-amid-west-asia-conflict-fia-seek-urgent-government-relief-206681/) | newsx.com | 8 | negative |
| 28 Apr 2026 | ['Industry in extreme stress, verge of shutting down': Federation of Indian Airlines seeks urgent help from…](https://www.hindustantimes.com/india-news/industry-in-extreme-stress-verge-of-shutting-down-federation-of-indian-airlines-seeks-urgent-help-from-government-101777376145146.html) | hindustantimes.com | 8 | negative |
| 28 Apr 2026 | ['On verge of stopping operations': In letter to Centre, airlines sound alarm over fuel prices - The Times of…](https://timesofindia.indiatimes.com/business/india-business/on-verge-of-stopping-operations-in-letter-to-centre-airlines-sound-alarm-over-fuel-prices/articleshow/130575938.cms) | timesofindia.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [AI, IndiGo, SpiceJet seek ATF price relief; say airline industry on verge of 'stopping operations' -…](https://www.orissapost.com/ai-indigo-spicejet-seek-atf-price-relief-say-airline-industry-on-verge-of-stopping-operations/) | orissapost.com | 8 | negative |
| 28 Apr 2026 | [Holiday update for Jet2, Ryanair and easyJet passengers from UK Foreign Office](https://www.chroniclelive.co.uk/lifestyle/travel/holiday-update-jet2-ryanair-easyjet-33849658) | chroniclelive.co.uk | 8 | negative |
| 23 Apr 2026 | [Tesla's AI Ambitions and Airline Earnings Challenges](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/tesla-s-ai-ambitions-and-airline-earnings-challenges) | startuphub.ai | 8 | positive |
| 23 Apr 2026 | [United Airlines CEO makes worrying statement as fares are expected to surge](https://www.uniladtech.com/vehicles/plane-news/united-airlines-ceo-worrying-oil-iran-statement-966616-20260423) | uniladtech.com | 8 | negative |
| 22 Apr 2026 | [JetBlue CEO Confidently Rules Out Bankruptcy Filing... But Only For 2026](https://onemileatatime.com/news/jetblue-ceo-rules-out-bankruptcy-filing/) | onemileatatime.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "airline industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "airline industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "airline industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "airline industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "airline industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Packaging Industry](packaging-industry.md)
- [Logistics Industry News](logistics-industry-news.md)
- [Apparel Industry](apparel-industry.md)
- [Sports Industry](sports-industry.md)
