# Apparel Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “apparel industry” · 1,300/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [apparel-industry.json](../../examples/scenarios/apparel-industry.json).

**Question.** How much news did the apparel industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="apparel industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 359 |
| Negative · neutral · positive | 18% · 0.3% · 82% |
| Critical (priority 7–9) | 46% (165 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (123 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | textile manufacturing advancements |

## Twelve months of coverage

Monthly matching articles for `apparel industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 34 | 59% | 3 | 31 | ██████ |
| Jun 2025 | 35 | 40% | 3 | 32 | ██████ |
| Jul 2025 | 56 | 55% | 11 | 44 | █████████ |
| Aug 2025 | 54 | 61% | 22 | 32 | █████████ |
| Sep 2025 | 56 | 39% | 14 | 41 | █████████ |
| Oct 2025 | 43 | 63% | 12 | 31 | ███████ |
| Nov 2025 | 37 | 32% | 4 | 33 | ██████ |
| Dec 2025 | 57 | 35% | 6 | 51 | █████████ |
| Jan 2026 | 79 | 58% | 25 | 54 | █████████████ |
| Feb 2026 | 123 | 58% | 18 | 105 | ████████████████████ |
| Mar 2026 | 55 | 44% | 4 | 51 | █████████ |
| Apr 2026 | 102 | 22% | 17 | 84 | █████████████████ |

The last four complete months averaged 90 articles a month against 45 in the first four (+101%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 64 | 18% |
| India | 39 | 11% |
| China | 16 | 4.5% |
| United Kingdom | 10 | 2.8% |
| France | 5 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| textile manufacturing advancements | 27 | 14% | +440% |
| sustainable fashion and ethical consumption | 14 | 7.2% | +27% |
| sustainable manufacturing practices | 14 | 7.2% | +250% |
| textile market analysis and forecasts | 13 | 6.7% | +30% |
| eco-friendly sustainable fashion | 20 | 10% | +400% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [European Textile Industry Faces Continued Decline, Urgent Action Needed: EURATEX - Textile Insights](https://textileinsights.in/european-textile-industry-faces-continued-decline-urgent-action-needed-euratex/) | textileinsights.in | 8 | negative |
| 24 Feb 2026 | [European FTA... unstoppable India! - Indian Textile Journal](https://indiantextilejournal.com/european-fta-unstoppable-india/) | indiantextilejournal.com | 8 | positive |
| 9 Feb 2026 | [India–US trade pact sparks optimism in textile, apparel sector](https://www.fibre2fashion.com/news/apparel-trade-news/india-us-trade-pact-sparks-optimism-in-textile-apparel-sector-308147-newsdetails.htm) | fibre2fashion.com | 8 | positive |
| 4 Feb 2026 | [Textile and apparel units in Tamil Nadu confident of reviving investments](https://www.thehindu.com/news/cities/Coimbatore/textile-and-apparel-units-in-tamil-nadu-confident-of-reviving-investments/article70588280.ece) | thehindu.com | 8 | negative |
| 28 Jan 2026 | [Sanjay Jain: The Budget must place stronger emphasis on productivity-linked skilling - Indian Textile Journal](https://indiantextilejournal.com/sanjay-jain-the-budget-must-place-stronger-emphasis-on-productivity-linked-skilling/) | indiantextilejournal.com | 8 | positive |
| 13 Jan 2026 | [CITI calls for removal of cotton import duty for good - India Seatrade News](https://indiaseatradenews.com/citi-calls-for-removal-of-cotton-import-duty-for-good/) | indiaseatradenews.com | 8 | negative |
| 6 Apr 2026 | [Taiwan Textiles Advancing Sustainable Innovation for Global Brands - Fibre2Fashion](https://www.fibre2fashion.com/industry-article/11377/taiwan-textiles-advancing-sustainable-innovation-for-global-brands) | fibre2fashion.com | 7 | positive |
| 18 Mar 2026 | [To reach US$8 billion, Sri Lanka apparel must grow differently - Adaderana Biz English \| Sri Lanka Business…](http://bizenglish.adaderana.lk/to-reach-us8-billion-sri-lanka-apparel-must-grow-differently/) | bizenglish.adaderana.lk | 7 | positive |
| 10 Feb 2026 | [TAI Mumbai’s Textiles 2030 Conference Focuses On The Future Of Textiles - Textile Insights](https://textileinsights.in/tai-mumbais-textiles-2030-conference-focuses-on-the-future-of-textiles/) | textileinsights.in | 7 | positive |
| 9 Feb 2026 | [Textile groups back Mercosur-EU deal, call it “essential” for regions](https://www.just-style.com/news/mercosur-eu-agreement-textiles/) | just-style.com | 7 | positive |
| 9 Feb 2026 | [Sri Lankan Apparel Industry Eyes India To Boost Competitiveness - Textile Insights](https://textileinsights.in/sri-lankan-apparel-industry-eyes-india-to-boost-competitiveness/) | textileinsights.in | 7 | positive |
| 9 Feb 2026 | [FITA, ABIT and EURATEX reaffirm support for Mercosur–EU textile pact](https://www.fibre2fashion.com/news/announcement/fita-abit-and-euratex-reaffirm-support-for-mercosur-eu-textile-pact-308233-newsdetails.htm) | fibre2fashion.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "apparel industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "apparel industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "apparel industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "apparel industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "apparel industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Logistics Industry News](logistics-industry-news.md)
- [Airline Industry](airline-industry.md)
- [Sports Industry](sports-industry.md)
- [Insurance Industry](insurance-industry.md)
