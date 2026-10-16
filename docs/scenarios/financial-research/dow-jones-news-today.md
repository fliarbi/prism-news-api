# Dow Jones News Today: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “dow jones news today” · 1,300/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [dow-jones-news-today.json](../../examples/scenarios/dow-jones-news-today.json).

**Question.** What did the news say about dow jones between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="dow jones"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,177 |
| Negative · neutral · positive | 56% · 3.5% · 40% |
| Critical (priority 7–9) | 48% (4,927 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,537 articles) |
| Most-reported country | United States (25% of matches) |
| Strongest theme by lift | market sentiment and investor behavior |

## Twelve months of coverage

Monthly matching articles for `dow jones` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,573 | 53% | 746 | 771 | █████████ |
| Jun 2025 | 1,277 | 50% | 677 | 539 | ███████ |
| Jul 2025 | 1,982 | 50% | 1,148 | 767 | ███████████ |
| Aug 2025 | 1,903 | 57% | 900 | 943 | ███████████ |
| Sep 2025 | 2,194 | 46% | 930 | 1,164 | ████████████ |
| Oct 2025 | 1,810 | 62% | 832 | 956 | ██████████ |
| Nov 2025 | 1,595 | 57% | 779 | 786 | █████████ |
| Dec 2025 | 1,520 | 43% | 677 | 795 | █████████ |
| Jan 2026 | 1,420 | 46% | 664 | 712 | ████████ |
| Feb 2026 | 2,683 | 45% | 1,335 | 1,286 | ███████████████ |
| Mar 2026 | 2,537 | 57% | 1,718 | 764 | ██████████████ |
| Apr 2026 | 3,537 | 46% | 2,000 | 1,343 | ████████████████████ |

The last four complete months averaged 2,544 articles a month against 1,684 in the first four (+51%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 37% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,554 | 25% |
| Iran | 323 | 3.2% |
| China | 198 | 1.9% |
| United Kingdom | 134 | 1.3% |
| India | 94 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| market sentiment and investor behavior | 1,473 | 20% | +192% |
| market volatility indicators | 1,110 | 15% | +72% |
| market volatility and risk assessment | 1,394 | 18% | +190% |
| trade wars and geopolitical impacts | 2,920 | 39% | +48% |
| stock market index composition | 934 | 12% | +72% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [S&P 500 Edges Higher Amid Mixed Mega-Cap Earnings; Dow Leads Market Indexes Overall \| The Motley Fool](https://www.fool.com/investing/2026/04/30/sp-500-edges-higher-amid-mixed-mega-cap-earnings-d/) | fool.com | 8 | positive |
| 29 Apr 2026 | [Wall Street recule, la Fed temporise, le pétrole flambe !](https://boursier.com/indices/actualites/news/wall-street-recule-la-fed-temporise-le-petrole-flambe-984479.html) | boursier.com | 8 | negative |
| 29 Apr 2026 | [Dow Jones estancado; S&P 500 y Nasdaq buscan rebotar antes de la Fed y los ‘magníficos’](https://www.estrategiasdeinversion.com/actualidad/noticias/bolsa-eeuu/dow-jones-busca-un-timido-rebote-a-la-espera-de-n-912665) | estrategiasdeinversion.com | 8 | negative |
| 29 Apr 2026 | [U.S. Stock Futures Edge Higher Ahead of Big Tech Earnings and Fed Decision - EconoTimes](https://econotimes.com/US-Stock-Futures-Edge-Higher-Ahead-of-Big-Tech-Earnings-and-Fed-Decision-1740296) | econotimes.com | 8 | negative |
| 28 Apr 2026 | [US stock markets today (April 28, 2026): Dow holds firm, Nasdaq weakens as AI doubts and oil spike shake…](https://timesofindia.indiatimes.com/business/international-business/us-stock-markets-today-april-28-2026-dow-holds-firm-nasdaq-weakens-as-ai-doubts-and-oil-spike-shake-tech/articleshow/130583735.cms) | timesofindia.indiatimes.com | 8 | negative |
| 28 Apr 2026 | [El Dow Jones cerró en 49.167,79 puntos, con una caída de 62,92 puntos (-0,13%)](https://www.negocios.com/articulo/dow-jones/dow-jones-cerro-49167-79-puntos-caida-6292-puntos-013/20260428065809484950.html) | negocios.com | 8 | negative |
| 25 Apr 2026 | [us market outlook bullish bias Intact](https://www.thehindubusinessline.com/portfolio/technical-analysis/us-market-outlook-bullish-bias-intact/article70904361.ece) | thehindubusinessline.com | 8 | negative |
| 24 Apr 2026 | [Dow Jones se atasca pendiente de Ormuz; Intel tira hacia arriba de S&P 500 y Nasdaq](https://www.estrategiasdeinversion.com/actualidad/noticias/bolsa-eeuu/dow-jones-cerrara-la-semana-a-la-baja-intel-tira-n-911201) | estrategiasdeinversion.com | 8 | negative |
| 24 Apr 2026 | [Dow Jones, S&P 500, Nasdaq: RekordstÃ¤nde â Eine US-BÃ¶rse schlieÃt besonders stark](http://www.handelsblatt.com/finanzen/maerkte/marktberichte/dow-jones-sp-500-nasdaq-rekordstaende-eine-us-boerse-schliesst-besonders-stark/100219764.html) | handelsblatt.com | 8 | negative |
| 23 Apr 2026 | [Wall Street: Verschnaufpause – Bilanzen im Fokus](https://www.deraktionaer.de/artikel/aktien/wall-street-verschnaufpause-bilanzen-im-fokus-20399637.html) | deraktionaer.de | 8 | negative |
| 23 Apr 2026 | [Dow Jones, S&P 500, Nasdaq: US-BÃ¶rsen schlieÃen nach Rekorden im Minus](http://www.handelsblatt.com/finanzen/maerkte/marktberichte/dow-jones-sp-500-nasdaq-us-boersen-schliessen-nach-rekorden-im-minus/100219442.html) | handelsblatt.com | 8 | negative |
| 23 Apr 2026 | [Dow Jones and Nasdaq drop back as ServiceNow, IBM and Tesla slide on earnings](https://www.proactiveinvestors.com/companies/news/1091068/dow-jones-and-nasdaq-drop-back-as-servicenow-ibm-and-tesla-slide-on-earnings-1091068.html) | proactiveinvestors.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "dow jones" --since 2026-01-01 --until 2026-04-30
prism-news trends "dow jones" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "dow jones" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "dow jones", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "dow jones", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Mortgage Rates News](mortgage-rates-news.md)
- [Silver Price News](silver-price-news.md)
- [Interest Rates News](interest-rates-news.md)
- [S&P 500 News Today](s-p-500-news-today.md)
