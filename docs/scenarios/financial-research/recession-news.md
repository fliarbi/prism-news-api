# Recession News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “recession news” · 1,900/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [recession-news.json](../../examples/scenarios/recession-news.json).

**Question.** What did the news say about recession between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="recession"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,699 |
| Negative · neutral · positive | 67% · 4.6% · 28% |
| Critical (priority 7–9) | 65% (3,050 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (3,026 articles) |
| Most-reported country | United States (24% of matches) |
| Strongest theme by lift | economy news: consumer confidence index updates |

## Twelve months of coverage

Monthly matching articles for `recession` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,026 | 64% | 2,070 | 853 | ████████████████████ |
| Jun 2025 | 1,026 | 62% | 675 | 310 | ███████ |
| Jul 2025 | 1,476 | 52% | 1,035 | 405 | ██████████ |
| Aug 2025 | 1,665 | 62% | 1,159 | 463 | ███████████ |
| Sep 2025 | 966 | 68% | 629 | 301 | ██████ |
| Oct 2025 | 900 | 63% | 601 | 247 | ██████ |
| Nov 2025 | 778 | 62% | 490 | 253 | █████ |
| Dec 2025 | 781 | 55% | 447 | 295 | █████ |
| Jan 2026 | 623 | 54% | 359 | 217 | ████ |
| Feb 2026 | 928 | 56% | 523 | 354 | ██████ |
| Mar 2026 | 1,411 | 70% | 1,060 | 298 | █████████ |
| Apr 2026 | 1,737 | 69% | 1,209 | 457 | ███████████ |

The last four complete months averaged 1,175 articles a month against 1,798 in the first four (-35%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 43% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,115 | 24% |
| Iran | 185 | 3.9% |
| United Kingdom | 107 | 2.3% |
| India | 103 | 2.2% |
| Australia | 94 | 2.0% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: consumer confidence index updates | 113 | 4.0% | +20% |
| market sentiment and investor behavior | 120 | 4.2% | +140% |
| economy news: economic forecast revisions | 74 | 2.6% | +45% |
| economy news: monetary policy changes | 213 | 7.5% | +48% |
| economy news: central bank interest rate decisions | 211 | 7.4% | +44% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [Iran war escalation could push global economy to brink of recession, IMF warns - Türkiye Today](https://www.turkiyetoday.com/business/iran-war-escalation-could-push-global-economy-to-brink-of-recession-imf-warns-3218153) | turkiyetoday.com | 9 | negative |
| 14 Apr 2026 | [Iran war wreaks havoc on global economy and could spark recession, says IMF](https://www.middleeasteye.net/news/iran-war-wreaks-havoc-global-economy-and-could-spark-recession-says-imf) | middleeasteye.net | 9 | negative |
| 19 Mar 2026 | [Strait of Hormuz blockade may have knock-on effect that can spiral into downturn: PM Wong](https://www.asiaone.com/singapore/strait-hormuz-blockade-may-have-knock-effect-can-spiral-downturn-pm-wong) | asiaone.com | 9 | negative |
| 13 Mar 2026 | [Temporary shock or wider downturn? Middle East energy crisis raises fresh cost pressures for UK retailers -…](https://www.retailgazette.co.uk/blog/2026/03/middle-east-energy-crisis-cost-pressures/) | retailgazette.co.uk | 9 | negative |
| 3 Mar 2026 | [Strait of Hormuz Closure is a Guaranteed Global Recession, Inflation Risks Surge on Rising Oil Prices](http://ibtimes.co.uk/strait-hormuz-closure-global-recession-1782789) | ibtimes.co.uk | 9 | negative |
| 30 Apr 2026 | [ONU advierte que bloqueo del estrecho de Ormuz empuja economía mundial hacia la recesión - PortalPortuario](https://portalportuario.cl/onu-advierte-que-bloqueo-del-estrecho-de-ormuz-empuja-economia-mundial-hacia-la-recesion/) | portalportuario.cl | 8 | negative |
| 30 Apr 2026 | [The global economy has a month—eight weeks at most—to avoid a recession, warns top economist \| Fortune](https://fortune.com/2026/04/30/global-economy-recession-oil-fears-mohamed-el-erian-zandi/) | fortune.com | 8 | negative |
| 30 Apr 2026 | [$200 Oil Could Trigger Global Recession](http://ibtimes.sg/200-oil-scenario-could-push-global-economy-into-recession-warns-bnp-paribas-85921) | ibtimes.sg | 8 | negative |
| 30 Apr 2026 | [The housing sector deserves better than being threatened with rent caps](https://www.cityam.com/the-housing-sector-deserves-better-than-being-threatened-with-rent-caps/) | cityam.com | 8 | negative |
| 29 Apr 2026 | ['Risk of recession' as inflation jumps and interest rate hike looms](https://www.abc.net.au/news/programs/the-business/2026-04-29/-risk-of-recession-as-inflation-jumps-and-interest/106622970) | abc.net.au | 8 | negative |
| 29 Apr 2026 | [UK economy set for £35bn hit from Middle East energy crisis, think tank says](https://www.yorkpress.co.uk/news/national/26061869.uk-economy-set-gbp35bn-hit-middle-east-energy-crisis-think-tank-says/) | yorkpress.co.uk | 8 | negative |
| 28 Apr 2026 | [UK set to suffer £35bn hit from Iran war as growth downgraded again](https://www.cityam.com/uk-set-to-suffer-35bn-hit-from-iran-war-as-growth-downgraded-again/) | cityam.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "recession" --since 2026-01-01 --until 2026-04-30
prism-news trends "recession" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "recession" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "recession", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "recession", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Venture Capital News Today](venture-capital-news-today.md)
- [Nasdaq News](nasdaq-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
- [US Dollar News](us-dollar-news.md)
