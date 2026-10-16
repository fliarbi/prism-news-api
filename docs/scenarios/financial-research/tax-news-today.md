# Tax News Today: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tax news today” · 720/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [tax-news-today.json](../../examples/scenarios/tax-news-today.json).

**Question.** What did the news say about tax between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="tax"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 90,619 |
| Negative · neutral · positive | 43% · 8.3% · 49% |
| Critical (priority 7–9) | 54% (49,304 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (31,421 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | personal income tax filing strategies |

## Twelve months of coverage

Monthly matching articles for `tax` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19,336 | 56% | 9,493 | 7,664 | ████████████ |
| Jun 2025 | 13,917 | 59% | 7,221 | 5,480 | █████████ |
| Jul 2025 | 21,937 | 58% | 11,936 | 8,422 | ██████████████ |
| Aug 2025 | 24,385 | 60% | 12,570 | 10,424 | ████████████████ |
| Sep 2025 | 19,930 | 59% | 8,748 | 9,747 | █████████████ |
| Oct 2025 | 16,140 | 63% | 8,151 | 6,848 | ██████████ |
| Nov 2025 | 14,628 | 61% | 6,828 | 6,758 | █████████ |
| Dec 2025 | 31,421 | 27% | 6,607 | 23,557 | ████████████████████ |
| Jan 2026 | 15,184 | 59% | 6,517 | 7,466 | ██████████ |
| Feb 2026 | 22,987 | 63% | 10,180 | 11,087 | ███████████████ |
| Mar 2026 | 25,563 | 45% | 9,240 | 14,214 | ████████████████ |
| Apr 2026 | 26,885 | 54% | 12,875 | 11,414 | █████████████████ |

The last four complete months averaged 22,655 articles a month against 19,894 in the first four (+14%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 38% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 17,053 | 19% |
| India | 5,103 | 5.6% |
| United Kingdom | 2,581 | 2.9% |
| Nigeria | 920 | 1.0% |
| Australia | 770 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| personal income tax filing strategies | 2,526 | 5.0% | +145% |
| government taxation and revenue systems | 9,656 | 19% | +32% |
| government fiscal policy implementation | 6,574 | 13% | +41% |
| economy news: tax reform implications | 947 | 1.9% | -32% |
| retirement account tax implications (ira, 401k) | 900 | 1.8% | +79% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [California's Wealth Tax Plan Fuels UHNW Anxiety](https://www.thinkadvisor.com/2026/04/30/californias-proposed-wealth-tax-fuels-uhnw-anxiety/) | thinkadvisor.com | 8 | negative |
| 30 Apr 2026 | [Kemi Badenoch: Conservatives are the only party that actually stands up to Sadiq Khan](http://standard.co.uk/comment/kemi-badenoch-conservative-party-stands-up-to-sadiq-khan-london-elections-b1280520.html) | standard.co.uk | 8 | negative |
| 30 Apr 2026 | [Sergey Brin, Who Fled The Soviet Union, Now Warns California Could Head The Same Way As He Spends $57 Mil](https://www.benzinga.com/markets/treasuries/26/04/52161131/sergey-brin-who-fled-the-soviet-union-now-warns-california-could-head-the-same-way-as-he-spends-57-million-fighting-billionaire-tax) | benzinga.com | 8 | negative |
| 30 Apr 2026 | [Taxe sur les superprofits de Total, présidentielle 2027... Le "8h30 franceinfo" de Boris Vallaud](https://www.franceinfo.fr/replay-radio/8h30-fauvelle-dely/taxe-sur-les-superprofits-de-total-presidentielle-2027-le-8h30-franceinfo-de-boris-vallaud_7942385.html) | franceinfo.fr | 8 | negative |
| 30 Apr 2026 | [The debt crisis Congress has been ignoring could cost the average U.S. household $18,000 a year, according…](https://fortune.com/2026/04/30/national-debt-today-crisis-solutions-tax-brookings/) | fortune.com | 8 | negative |
| 30 Apr 2026 | [State Pension rise pushes UK pensioners near tax threshold](https://www.mirror.co.uk/money/triple-lock-state-pension-rise-37088259) | mirror.co.uk | 8 | negative |
| 29 Apr 2026 | [Adani Power Q4 Results](https://www.newsdrum.in/business/adani-power-q4-net-profit-jumps-64-pc-to-rs-4271-cr-11778729) | newsdrum.in | 8 | positive |
| 29 Apr 2026 | [HRA Alert: Income Tax Dept Using AI to Spot Fake Rent Claims](https://studycafe.in/hra-alert-income-tax-dept-using-ai-to-spot-fake-rent-claims-418529.html) | studycafe.in | 8 | negative |
| 29 Apr 2026 | [Sergey Brin joins the fight against socialism — better late than never](https://www.yahoo.com/news/articles/sergey-brin-joins-fight-against-002229089.html) | yahoo.com | 8 | negative |
| 29 Apr 2026 | [Sergey Brin opens up about harrowing Soviet past — says California lost its way - Amed Post](https://amedpost.com/sergey-brin-opens-up-about-harrowing-soviet-past-says-california-lost-its-way/) | amedpost.com | 8 | negative |
| 28 Apr 2026 | [Sergey Brin opens up about harrowing Soviet past — says California lost its way](https://www.yahoo.com/news/articles/sergey-brin-opens-harrowing-soviet-222933217.html) | yahoo.com | 8 | negative |
| 28 Apr 2026 | [Ray Dalio’s wealth tax warning for California voters - Amed Post](https://amedpost.com/ray-dalios-wealth-tax-warning-for-california-voters/) | amedpost.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "tax" --since 2026-01-01 --until 2026-04-30
prism-news trends "tax" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "tax" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "tax", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "tax", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Yen News](yen-news.md)
- [Market Crash News](market-crash-news.md)
- [IMF News](imf-news.md)
- [NBFC News](nbfc-news.md)
