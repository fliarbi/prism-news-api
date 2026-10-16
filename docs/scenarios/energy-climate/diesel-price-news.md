# Diesel Price News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “diesel price news” · 1,300/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [diesel-price-news.json](../../examples/scenarios/diesel-price-news.json).

**Question.** How did diesel price coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="diesel price"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,030 |
| Negative · neutral · positive | 94% · 1.2% · 4.6% |
| Critical (priority 7–9) | 14% (140 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (536 articles) |
| Most-reported country | India (62% of matches) |
| Strongest theme by lift | regional gas price variations and trends |

## Twelve months of coverage

Monthly matching articles for `diesel price` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 29 | 24% | 25 | 2 | █ |
| Jun 2025 | 14 | 21% | 10 | 4 | █ |
| Jul 2025 | 30 | 20% | 21 | 8 | █ |
| Aug 2025 | 41 | 12% | 36 | 3 | ██ |
| Sep 2025 | 17 | 5.9% | 14 | 3 | █ |
| Oct 2025 | 17 | 29% | 15 | 2 | █ |
| Nov 2025 | 25 | 28% | 19 | 4 | █ |
| Dec 2025 | 12 | 8.3% | 11 | 1 | █ |
| Jan 2026 | 8 | 12% | 4 | 4 | █ |
| Feb 2026 | 37 | 24% | 34 | 2 | █ |
| Mar 2026 | 449 | 13% | 429 | 17 | █████████████████ |
| Apr 2026 | 536 | 14% | 504 | 24 | ████████████████████ |

The last four complete months averaged 258 articles a month against 28 in the first four (+804%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 75% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 637 | 62% |
| United States | 46 | 4.5% |
| Iran | 15 | 1.5% |
| South Africa | 11 | 1.1% |
| Australia | 9 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| regional gas price variations and trends | 431 | 57% | +2168% |
| diesel fuel pricing and availability | 151 | 20% | +7450% |
| gasoline production technologies | 178 | 23% | +493% |
| oil and gas market trends | 253 | 33% | +954% |
| non-toxic skincare products | 27 | 3.5% | new |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 31 Mar 2026 | [Dieselpreis explodiert: Busverkehr auf dem Land ist bedroht](https://www.stuttgarter-nachrichten.de/inhalt.dieselpreis-explodiert-busverkehr-auf-dem-land-ist-bedroht.bedc15c9-7b85-4096-9198-09fd3ec11333.html) | stuttgarter-nachrichten.de | 7 | negative |
| 30 Mar 2026 | [Gestiegener Preis für Diesel: Kommt der Bus auf dem Land bald nicht mehr wie gewohnt?](https://www.swr.de/swraktuell/baden-wuerttemberg/wegen-dieselpreisen-busunternehmen-fuerchten-um-linien-auf-dem-land-100.html) | swr.de | 7 | negative |
| 30 Apr 2026 | [UAE Fuel Price Committee announces prices for May](https://www.zawya.com/en/business/retail-and-consumer/uae-fuel-price-committee-announces-prices-for-may-lqkaovj4) | zawya.com | 6 | positive |
| 2 Apr 2026 | [Fiskalrat will streichen: Pendlerpauschale vor dem Aus, so sicherst du dir dein Geld](https://www.meinbezirk.at/st-poelten/c-lokales/pendlerpauschale-vor-dem-aus-so-sicherst-du-dir-dein-geld_a8549839) | meinbezirk.at | 6 | negative |
| 21 Mar 2026 | [Centre rolls back diesel price hike for Gujarat fishermen](https://telanganatoday.com/centre-rolls-back-diesel-price-hike-for-gujarat-fishermen) | telanganatoday.com | 6 | negative |
| 21 Mar 2026 | [Gujarat fishermen get relief as Centre rolls back diesel price hike](https://businessnewsthisweek.com/business/gujarat-fishermen-get-relief-as-centre-rolls-back-diesel-price-hike/) | businessnewsthisweek.com | 6 | negative |
| 19 Mar 2026 | [Diesel sobe em média para R$ 7,17 por litro apesar de medidas do governo, revela pesquisa](https://www.diariodepernambuco.com.br/economia/2026/03/11710278-diesel-sobe-em-media-para-rs-717-por-litro-apesar-de-medidas-do-governo-revela-pesquisa.html) | diariodepernambuco.com.br | 6 | negative |
| 18 Mar 2026 | [Preço do diesel gera inquérito da PF e ameaça de greve de caminhoneiros \| CNN Brasil](https://www.cnnbrasil.com.br/politica/preco-do-diesel-gera-inquerito-da-pf-e-ameaca-de-greve-de-caminhoneiros/) | cnnbrasil.com.br | 6 | negative |
| 4 Mar 2026 | [Diesel-Preis spingt über die Zwei Euro-Marke - Benzin nähert sich](https://www.n-tv.de/wirtschaft/So-viel-kostet-der-Sprit-Preise-fuer-Diesel-und-Benzin-erreicht-Marke-von-zwei-Euro-je-Liter-id30429310.html) | n-tv.de | 6 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "diesel price" --since 2026-01-01 --until 2026-04-30
prism-news trends "diesel price" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "diesel price" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "diesel price", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "diesel price", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [LNG News](lng-news.md)
- [Rare Earths News](rare-earths-news.md)
- [El Nino News](el-nino-news.md)
- [EV Charging News](ev-charging-news.md)
