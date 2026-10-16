# Food Safety News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “food safety news” · 110/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [food-safety-news.json](../../examples/scenarios/food-safety-news.json).

**Question.** How did coverage of food safety develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="food safety"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 21,479 |
| Negative · neutral · positive | 52% · 2.6% · 46% |
| Critical (priority 7–9) | 66% (14,184 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (6,039 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | product safety and recall notices |

## Twelve months of coverage

Monthly matching articles for `food safety` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,896 | 60% | 1,946 | 1,845 | █████████████ |
| Jun 2025 | 3,230 | 61% | 1,555 | 1,598 | ███████████ |
| Jul 2025 | 4,129 | 56% | 2,019 | 2,016 | ██████████████ |
| Aug 2025 | 4,174 | 59% | 2,209 | 1,853 | ██████████████ |
| Sep 2025 | 4,402 | 62% | 1,961 | 2,338 | ███████████████ |
| Oct 2025 | 4,098 | 64% | 1,916 | 2,070 | ██████████████ |
| Nov 2025 | 4,075 | 60% | 1,664 | 2,344 | █████████████ |
| Dec 2025 | 4,007 | 64% | 1,803 | 2,115 | █████████████ |
| Jan 2026 | 4,909 | 70% | 2,599 | 2,208 | ████████████████ |
| Feb 2026 | 5,549 | 68% | 2,968 | 2,449 | ██████████████████ |
| Mar 2026 | 4,982 | 64% | 2,514 | 2,322 | ████████████████ |
| Apr 2026 | 6,039 | 63% | 2,984 | 2,859 | ████████████████████ |

The last four complete months averaged 5,370 articles a month against 3,857 in the first four (+39%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 3,987 | 19% |
| India | 1,296 | 6.0% |
| United Kingdom | 581 | 2.7% |
| China | 212 | 1.0% |
| Canada | 211 | 1.0% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| product safety and recall notices | 756 | 6.5% | -4% |
| food safety regulation compliance | 2,504 | 21% | +43% |
| agricultural policy and regulatory compliance | 436 | 3.7% | +130% |
| consumer health and safety standards | 434 | 3.7% | +61% |
| post-harvest storage and preservation | 736 | 6.3% | +38% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Mar 2026 | [9 sickened in E. coli outbreak tied to a California company’s raw milk and cheese](https://www.orlandosentinel.com/2026/03/26/raw-milk-cheese-e-coli-raw-farm/) | orlandosentinel.com | 9 | negative |
| 22 Mar 2026 | [Why 30 Countries Banned These American Foods (Video) \| Food and Farming \| Before It's News](https://beforeitsnews.com/food-and-farming/2026/03/why-30-countries-bsanned-these-american-foods-video-2543532.html) | beforeitsnews.com | 9 | negative |
| 23 Feb 2026 | [Milk ‘adulteration’ kills 4; AP announces Rs 10 lakh ex gratia](https://telanganatoday.com/milk-adulteration-kills-4-ap-announces-rs-10-lakh-ex-gratia) ⚠ | telanganatoday.com | 9 | negative |
| 20 Feb 2026 | [Burrell investigat­ors share new details on beloved chef’s death](https://www.pressreader.com/usa/the-commercial-appeal/20260220/281530822488827) | pressreader.com | 9 | negative |
| 9 Feb 2026 | [E. coli Outbreak Linked to McDonald's Quarter Pounders - CDC News - News Directory 3](https://www.newsdirectory3.com/e-coli-outbreak-linked-to-mcdonalds-quarter-pounders-cdc-news/) ⚠ | newsdirectory3.com | 9 | negative |
| 2 Feb 2026 | [Knowledge needed to curb Nipah panic](https://bangkokpost.com/opinion/opinion/3189190/knowledge-needed-to-curb-nipah-panic) ⚠ | bangkokpost.com | 9 | negative |
| 30 Apr 2026 | [Illegal Home Kitchen Exposed in Kuwait Raid, Workers Detained](https://www.arabtimesonline.com/news/illegal-home-kitchen-exposed-in-kuwait-raid-workers-detained/) | arabtimesonline.com | 8 | negative |
| 30 Apr 2026 | [The investigative police agency under the Thanh Hoa Department of Public Security on Thursday confirmed the…](https://news.tuoitre.vn/print/3-indicted-in-vietnams-thanh-hoa-for-selling-asf-infected-pork-103260430171546205.htm) | news.tuoitre.vn | 8 | negative |
| 29 Apr 2026 | [New FDA analysis says infant formula supply is safe after testing for potential contaminants](https://triblive.com/news/world/new-fda-analysis-says-infant-formula-supply-is-safe-after-testing-for-potential-contaminants/) | triblive.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "food safety" --since 2026-01-01 --until 2026-04-30
prism-news trends "food safety" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "food safety" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "food safety", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "food safety", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Tariffs News](tariffs-news.md)
- [AI Regulation News](ai-regulation-news.md)
- [Medicare News](medicare-news.md)
- [EU AI Act News](eu-ai-act-news.md)
