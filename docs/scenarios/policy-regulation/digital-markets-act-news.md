# Digital Markets Act News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “digital markets act news” · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [digital-markets-act-news.json](../../examples/scenarios/digital-markets-act-news.json).

**Question.** How did coverage of digital markets act develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="digital markets act"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 421 |
| Negative · neutral · positive | 67% · 2.6% · 31% |
| Critical (priority 7–9) | 80% (337 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (233 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | tech patent disputes and lawsuits |

## Twelve months of coverage

Monthly matching articles for `digital markets act` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 151 | 84% | 112 | 39 | █████████████ |
| Jun 2025 | 200 | 76% | 130 | 55 | █████████████████ |
| Jul 2025 | 210 | 81% | 166 | 42 | ██████████████████ |
| Aug 2025 | 170 | 83% | 118 | 43 | ███████████████ |
| Sep 2025 | 232 | 76% | 171 | 60 | ████████████████████ |
| Oct 2025 | 166 | 86% | 118 | 47 | ██████████████ |
| Nov 2025 | 233 | 71% | 163 | 65 | ████████████████████ |
| Dec 2025 | 230 | 86% | 159 | 66 | ████████████████████ |
| Jan 2026 | 108 | 85% | 69 | 39 | █████████ |
| Feb 2026 | 81 | 76% | 60 | 19 | ███████ |
| Mar 2026 | 94 | 71% | 58 | 33 | ████████ |
| Apr 2026 | 138 | 84% | 93 | 39 | ████████████ |

The last four complete months averaged 105 articles a month against 183 in the first four (-42%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 41% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 80 | 19% |
| Belgium | 32 | 7.6% |
| South Korea | 17 | 4.0% |
| United Kingdom | 13 | 3.1% |
| Colombia | 6 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| tech patent disputes and lawsuits | 41 | 18% | -62% |
| social media platform updates | 15 | 6.6% | -65% |
| antitrust & competition law | 14 | 6.2% | -48% |
| mobile app innovations | 13 | 5.8% | -58% |
| tech policy and government regulations | 75 | 33% | -55% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 28 Apr 2026 | [Brussels consults on Google measures to give Android users choice on AI services - EUbusiness.com \| EU news,…](https://www.eubusiness.com/competition/eu-sends-google-measures-to-give-android-users-ai-choice/) | eubusiness.com | 8 | positive |
| 28 Apr 2026 | [The European Commission has launched a public consultation on draft measures requiring Alphabet (Google) to…](https://www.fonearena.com/blog/481182/eu-android-interoperability-rules-consultation-dma.html) | fonearena.com | 8 | positive |
| 22 Apr 2026 | [EU Commission proposes DMA measures for Google search data access \| The Paypers](https://www.thepaypers.com/fraud-and-fincrime/news/european-commission-proposes-measures-requiring-google-to-share-search-data-under-dma) | thepaypers.com | 8 | negative |
| 20 Apr 2026 | [EU Proposes Forcing Google To Share Proprietary Search Data With Rivals](https://www.ubergizmo.com/2026/04/eu-forcing-google-share-proprietary-search-data-with-rivals/) | ubergizmo.com | 8 | negative |
| 16 Apr 2026 | [Google must share search data with competitors, says EU - EUbusiness.com \| EU news, business and politics](https://www.eubusiness.com/competition/google-must-share-search-data-with-competitors-says-eu/) | eubusiness.com | 8 | negative |
| 16 Apr 2026 | [EU wants Google to share search data with third‑party engines, including AI chatbots](https://www.malaymail.com/news/money/2026/04/16/eu-wants-google-to-share-search-data-with-thirdparty-engines-including-ai-chatbots/216556) | malaymail.com | 8 | negative |
| 16 Apr 2026 | [Google should allow third-party search engines access to data, EU says](https://telecom.economictimes.indiatimes.com/news/internet/eu-calls-for-google-to-share-search-data-with-competitors/130305385) | telecom.economictimes.indiatimes.com | 8 | negative |
| 16 Apr 2026 | [EU forces Google's hand on search data, angering Google](https://www.theregister.com/2026/04/16/brussels_tells_google_to_open/) | theregister.com | 8 | negative |
| 16 Apr 2026 | [EU Pushes Google for Data Sharing in Favor of Competition \| Technology](https://www.devdiscourse.com/article/technology/3876212-eu-pushes-google-for-data-sharing-in-favor-of-competition) | devdiscourse.com | 8 | negative |
| 16 Apr 2026 | [Google Asked to Allow Other Search Engines Access to Its Data](https://www.republicworld.com/tech/google-asked-to-allow-other-search-engines-access-to-its-data) | republicworld.com | 8 | negative |
| 16 Apr 2026 | [EU pushes Google to open search data to rivals under Digital Markets Act](https://www.storyboard18.com/digital/eu-warns-google-on-dma-as-it-shifts-search-ads-to-ai-max-ws-l-95364.htm) | storyboard18.com | 8 | negative |
| 12 Feb 2026 | [EU reportedly opens another probe into Google's ads pricing](https://www.engadget.com/big-tech/eu-reportedly-opens-another-probe-into-googles-ads-pricing-194435095.html) | engadget.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "digital markets act" --since 2026-01-01 --until 2026-04-30
prism-news trends "digital markets act" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "digital markets act" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "digital markets act", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "digital markets act", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Content Moderation News](content-moderation-news.md)
- [Rent Control News](rent-control-news.md)
- [Railway Budget News](railway-budget-news.md)
- [Cryptocurrency Regulation News](cryptocurrency-regulation-news.md)
