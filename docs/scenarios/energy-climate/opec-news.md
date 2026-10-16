# OPEC News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “opec news” · 880/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [opec-news.json](../../examples/scenarios/opec-news.json).

**Question.** How did opec coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="OPEC"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 8,528 |
| Negative · neutral · positive | 78% · 1.6% · 20% |
| Critical (priority 7–9) | 82% (6,968 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,580 articles) |
| Most-reported country | United States (27% of matches) |
| Strongest theme by lift | economic impact of oil exports |

## Twelve months of coverage

Monthly matching articles for `OPEC` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,266 | 72% | 794 | 445 | ███████ |
| Jun 2025 | 1,134 | 79% | 822 | 295 | ██████ |
| Jul 2025 | 1,226 | 67% | 747 | 464 | ███████ |
| Aug 2025 | 1,375 | 70% | 853 | 505 | ████████ |
| Sep 2025 | 1,074 | 79% | 609 | 449 | ██████ |
| Oct 2025 | 1,114 | 80% | 688 | 413 | ██████ |
| Nov 2025 | 1,162 | 81% | 732 | 421 | ██████ |
| Dec 2025 | 1,030 | 82% | 688 | 331 | ██████ |
| Jan 2026 | 1,681 | 87% | 1,293 | 363 | █████████ |
| Feb 2026 | 1,295 | 79% | 807 | 458 | ███████ |
| Mar 2026 | 1,972 | 88% | 1,651 | 298 | ███████████ |
| Apr 2026 | 3,580 | 77% | 2,903 | 611 | ████████████████████ |

The last four complete months averaged 2,132 articles a month against 1,250 in the first four (+71%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 65% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 2,318 | 27% |
| United Arab Emirates | 880 | 10% |
| India | 400 | 4.7% |
| China | 268 | 3.1% |
| Iran | 243 | 2.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economic impact of oil exports | 1,610 | 26% | +282% |
| geopolitical factors in oil supply | 2,501 | 40% | +180% |
| oil and gas market trends | 2,763 | 44% | +122% |
| oil tanker transportation logistics | 793 | 13% | +311% |
| international certifications for oil & gas | 214 | 3.4% | +398% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 5 Apr 2026 | [OPEC nations agree to adjust oil production: What to know](https://www.newsweek.com/opec-nations-agree-to-adjust-oil-production-what-to-know-11785259) | newsweek.com | 9 | negative |
| 30 Apr 2026 | [UAE Departure Foreshadows New Era for Opec](https://www.energyintel.com/0000019d-da5d-df5e-addf-dbdf54240000) | energyintel.com | 8 | negative |
| 30 Apr 2026 | [UAE exit signals OPECs declining grip on oil markets - IndiaVision India News & Information](https://www.indiavision.com/international/uae-exit-signals-opecs-declining-grip-on-oil-markets/602177/) | indiavision.com | 8 | negative |
| 30 Apr 2026 | [Gulf within: On the UAE leaving OPEC](https://www.thehindu.com/opinion/op-ed/gulf-within-on-the-uae-leaving-opec/article70925606.ece) | thehindu.com | 8 | negative |
| 30 Apr 2026 | [UAE's exit from Opec signals shift towards competitive oil order](https://www.newindianexpress.com/editorial/2026/Apr/30/uaes-exit-from-opec-signals-shift-towards-competitive-oil-order) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [UAE Opec Exit Signals Wider Gulf Divide](https://www.energyintel.com/0000019d-ddcf-dd89-abff-dddff2740000) | energyintel.com | 8 | negative |
| 30 Apr 2026 | [UAE to exit OPEC+: What it means for global oil prices and markets](https://qazinform.com/news/uae-exit-from-opec-shakes-oil-market-outlook-e31e4c) | qazinform.com | 8 | negative |
| 30 Apr 2026 | [Trump, Fox News praise UAE decision to leave Opec](http://www.middleeasteye.net/news/trump-fox-news-praise-uae-decision-to-leave-opec-oil-cartel) | middleeasteye.net | 8 | negative |
| 30 Apr 2026 | [Las consecuencias petroleras que generarÃ­a la salida de Emiratos Ãrabes de la OPEP](https://www.biobiochile.cl/noticias/economia/actualidad-economica/2026/04/30/las-consecuencias-petroleras-que-generaria-la-salida-de-emiratos-arabes-de-la-opep.shtml) | biobiochile.cl | 8 | negative |
| 30 Apr 2026 | [Indonesia: Ties Unruffled with UAE Following OPEC Exit](https://en.tempo.co/read/2101261/indonesia-ties-unruffled-with-uae-following-opec-exit) | en.tempo.co | 8 | negative |
| 30 Apr 2026 | [Opec's days of manipulating the market are over \| The National](https://www.thenationalnews.com/opinion/comment/2026/04/30/uae-opec-saudi-arabia-us-russia-oil-iran-war-strait-of-hormuz/) | thenationalnews.com | 8 | negative |
| 30 Apr 2026 | [United Arab Emirates To Quit OPEC After 59 Years](https://techmgzn.com/united-arab-emirates-to-quit-opec-after-59-years/) | techmgzn.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "OPEC" --since 2026-01-01 --until 2026-04-30
prism-news trends "OPEC" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "OPEC" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "OPEC", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "OPEC", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Electric Vehicles News](electric-vehicles-news.md)
- [Wildfire News](wildfire-news.md)
- [Recycling Industry](recycling-industry.md)
- [Nuclear Power News](nuclear-power-news.md)
