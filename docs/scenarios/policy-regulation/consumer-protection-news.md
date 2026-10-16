# Consumer Protection News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “consumer protection news” · 40/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [consumer-protection-news.json](../../examples/scenarios/consumer-protection-news.json).

**Question.** How did coverage of consumer protection develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="consumer protection"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 21,456 |
| Negative · neutral · positive | 58% · 8.3% · 33% |
| Critical (priority 7–9) | 73% (15,622 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (6,504 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | consumer protection laws and regulations |

## Twelve months of coverage

Monthly matching articles for `consumer protection` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,572 | 67% | 2,153 | 1,255 | ███████████ |
| Jun 2025 | 2,658 | 65% | 1,424 | 1,115 | ████████ |
| Jul 2025 | 3,731 | 64% | 2,257 | 1,358 | ███████████ |
| Aug 2025 | 3,346 | 67% | 2,169 | 1,059 | ██████████ |
| Sep 2025 | 3,363 | 69% | 1,893 | 1,307 | ██████████ |
| Oct 2025 | 3,084 | 69% | 1,688 | 1,215 | █████████ |
| Nov 2025 | 3,072 | 69% | 1,695 | 1,219 | █████████ |
| Dec 2025 | 3,239 | 70% | 1,870 | 1,211 | ██████████ |
| Jan 2026 | 2,875 | 67% | 1,597 | 1,153 | █████████ |
| Feb 2026 | 6,277 | 77% | 3,921 | 2,042 | ███████████████████ |
| Mar 2026 | 5,800 | 72% | 3,391 | 1,854 | ██████████████████ |
| Apr 2026 | 6,504 | 72% | 3,619 | 2,085 | ████████████████████ |

The last four complete months averaged 5,364 articles a month against 3,327 in the first four (+61%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,435 | 25% |
| India | 728 | 3.4% |
| United Kingdom | 527 | 2.5% |
| Nigeria | 523 | 2.4% |
| Australia | 170 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| consumer protection laws and regulations | 409 | 4.0% | +35% |
| consumer rights advocacy groups | 269 | 2.6% | +130% |
| electricity metering systems & smart meters | 252 | 2.5% | +108% |
| unfair trade practice reporting | 247 | 2.4% | +87% |
| product safety and recall notices | 245 | 2.4% | +22% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [France: 75% of imported products did not meet EU rules](https://ecommercenews.eu/france-75-of-imported-products-did-not-meet-eu-rules/) | ecommercenews.eu | 8 | negative |
| 30 Apr 2026 | [Can You Recognize An Artificial Intelligence (AI) Scam?](https://mountaineagle.com/online_features/money_and_finance/can-you-recognize-an-artificial-intelligence-ai-scam/article_bdfea258-57d2-52f8-a8cd-83a2f835de30.html) | mountaineagle.com | 8 | negative |
| 29 Apr 2026 | [Perth landscaper fined in Joondalup over unfinished jobs](https://www.perthnow.com.au/wa/perth/north/joondalup/perth-landscaper-fined-in-joondalup-magistrates-court-after-pocketing-thousands-and-not-completing-work-c-22188025) | perthnow.com.au | 8 | negative |
| 28 Apr 2026 | [BoG urges fintechs to match innovation with responsibility - Ghanaian Times](https://ghanaiantimes.com.gh/bog-urges-fintechs-to-match-innovation-with-responsibility/) | ghanaiantimes.com.gh | 8 | positive |
| 27 Apr 2026 | [California Privacy Agency Opposes âWeakerâ Federal Privacy Bill](https://news.bloomberglaw.com/privacy-and-data-security/california-privacy-agency-opposes-weaker-federal-privacy-bill) | news.bloomberglaw.com | 8 | negative |
| 27 Apr 2026 | [Telcos Lose Grip as FCCPC Approves New Data and Airtime Lenders - Innovation Village \| Technology, Product…](https://innovation-village.com/telcos-lose-grip-as-fccpc-approves-new-data-and-airtime-lenders/) | innovation-village.com | 8 | positive |
| 24 Apr 2026 | [FCCPC seals Abuja supermarket over pricing irregularities, expired products](https://www.premiumtimesng.com/news/874471-fccpc-seals-abuja-supermarket-over-pricing-irregularities-expired-products.html) | premiumtimesng.com | 8 | negative |
| 24 Apr 2026 | [High Court: FCCPC can investigate consumers' complaints about banks, other financial institutions - The…](https://thenationonlineng.net/high-court-fccpc-can-investigate-consumers-complaints-about-banks-other-financial-institutions/) | thenationonlineng.net | 8 | negative |
| 23 Apr 2026 | [👨🏿‍🚀TechCabal Daily – New airtime lenders are in town \| TechCabal](https://techcabal.com/2026/04/23/techcabal-daily-new-airtime-lenders-are-in-town/) | techcabal.com | 8 | negative |
| 23 Apr 2026 | [FCCPC Licenses 5 Firms for Airtime, Data Lending as Telcos Step Aside](https://www.nigeriacommunicationsweek.com.ng/fccpc-licenses-5-firms-for-airtime-data-lending-as-telcos-step-aside/) | nigeriacommunicationsweek.com.ng | 8 | negative |
| 22 Apr 2026 | [Meta faces fresh lawsuit over fake ads on Facebook and Instagram promising free phones, government payouts](https://www.digit.in/news/apps/meta-faces-fresh-lawsuit-over-fake-ads-on-facebook-and-instagram-promising-free-phones-government-payouts.html) | digit.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "consumer protection" --since 2026-01-01 --until 2026-04-30
prism-news trends "consumer protection" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "consumer protection" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "consumer protection", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "consumer protection", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Export Controls News](export-controls-news.md)
- [NEP News](nep-news.md)
- [Chips Act News](chips-act-news.md)
- [Content Moderation News](content-moderation-news.md)
