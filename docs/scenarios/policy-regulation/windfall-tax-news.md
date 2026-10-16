# Windfall Tax News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “windfall tax news” · 210/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [windfall-tax-news.json](../../examples/scenarios/windfall-tax-news.json).

**Question.** How did coverage of windfall tax develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="windfall tax"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 249 |
| Negative · neutral · positive | 96% · 0.8% · 2.8% |
| Critical (priority 7–9) | 87% (216 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (146 articles) |
| Most-reported country | Iran (18% of matches) |
| Strongest theme by lift | economic impact of oil exports |

## Twelve months of coverage

Monthly matching articles for `windfall tax` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 21 | 100% | 20 | 0 | ███ |
| Jun 2025 | 5 | 100% | 5 | 0 | █ |
| Jul 2025 | 6 | 100% | 6 | 0 | █ |
| Aug 2025 | 16 | 75% | 15 | 1 | ██ |
| Sep 2025 | 19 | 100% | 17 | 2 | ███ |
| Oct 2025 | 20 | 100% | 17 | 3 | ███ |
| Nov 2025 | 20 | 100% | 19 | 1 | ███ |
| Dec 2025 | 17 | 100% | 13 | 4 | ██ |
| Jan 2026 | 6 | 100% | 6 | 0 | █ |
| Feb 2026 | 10 | 100% | 10 | 0 | █ |
| Mar 2026 | 87 | 91% | 85 | 2 | ████████████ |
| Apr 2026 | 146 | 83% | 139 | 5 | ████████████████████ |

The last four complete months averaged 62 articles a month against 12 in the first four (+419%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 72% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| Iran | 45 | 18% |
| United Kingdom | 30 | 12% |
| United States | 24 | 9.6% |
| Australia | 14 | 5.6% |
| India | 13 | 5.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economic impact of oil exports | 52 | 26% | — |
| geopolitical factors in oil supply | 82 | 41% | +2633% |
| oil and gas market trends | 119 | 60% | +982% |
| renewable energy policy & regulation | 10 | 5.0% | +233% |
| oil and gas investment trends | 8 | 4.0% | +700% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Apr 2026 | [India Raises Windfall Tax On Fuel Exports Amid West Asia Tensions, Diesel Duty At ₹55.5/Litre & ATF At…](https://www.freepressjournal.in/business/india-raises-windfall-tax-on-fuel-exports-amid-west-asia-tensions-diesel-duty-at-555litre-atf-at-42litre) | freepressjournal.in | 8 | negative |
| 9 Apr 2026 | [Windfall tax delay exposes Indonesia’s challenge in capturing commodity gains](https://intellinews.com/windfall-tax-delay-exposes-indonesia-s-challenge-in-capturing-commodity-gains-436184/) | intellinews.com | 8 | negative |
| 4 Apr 2026 | [European ministers call for profit caps on energy companies as Iran war drives price surge](https://www.ajc.com/news/2026/04/european-ministers-call-for-profit-caps-on-energy-companies-as-iran-war-drives-price-surge/) | ajc.com | 8 | negative |
| 27 Mar 2026 | [【SMM Analysis】Windfall or Export Levy? Inside Indonesia's Upcoming Commodities’ Tax - Shanghai Metals Market…](https://news.metal.com/en/newscontent/103829040-SMM-AnalysisWindfall-or-Export-Levy-Inside-Indonesias-Upcoming-Commodities%E2%80%99-Tax) | news.metal.com | 8 | negative |
| 18 Mar 2026 | [VERBUND AG (ETR:OEWA) \|](https://www.webdisclosure.com/press-release/verbund-ag-full-year-2025-results-solid-results-despite-below-average-water-supply-and-windfall-tax-a6JSnNo80jh) | webdisclosure.com | 8 | positive |
| 25 Feb 2026 | [UK ministers 'in talks' over early end to windfall tax – Daily Business](https://dailybusinessgroup.co.uk/2026/02/uk-ministers-in-talks-over-early-end-to-windfall-tax/) | dailybusinessgroup.co.uk | 8 | negative |
| 18 Feb 2026 | [Shutting North Sea ‘will drive up carbon emissions’](https://www.yahoo.com/news/articles/shutting-north-sea-drive-carbon-070000064.html) | yahoo.com | 8 | negative |
| 27 Apr 2026 | [Lithuania takes note as Poland weighs windfall tax on energy firms](https://www.lrt.lt/en/news-in-english/19/2911147/lithuania-takes-note-as-poland-weighs-windfall-tax-on-energy-firms) | lrt.lt | 7 | negative |
| 23 Apr 2026 | [No plans for EU-wide windfall tax, commission says](https://www.yahoo.com/news/articles/no-plans-eu-wide-windfall-163824407.html) | yahoo.com | 7 | negative |
| 21 Apr 2026 | [UK Moves to Shield Households From Rising Bills](https://www.easterneye.biz/uk-windfall-tax-power-firms-household-bills/) | easterneye.biz | 7 | negative |
| 21 Apr 2026 | [Electricity bills targeted in planned shakeup to energy pricing](https://www.bbc.co.uk/news/articles/c79jg43vd8no) | bbc.co.uk | 7 | negative |
| 18 Apr 2026 | [Rachel Reeves Plans Increase in Windfall Tax on Low-Carbon Power Firms - The Beaver](https://www.beaveronline.co.uk/news/rachel-reeves-plans-increase-in/2361/) | beaveronline.co.uk | 7 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "windfall tax" --since 2026-01-01 --until 2026-04-30
prism-news trends "windfall tax" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "windfall tax" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "windfall tax", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "windfall tax", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Sanctions News](sanctions-news.md)
- [Banking Regulation News](banking-regulation-news.md)
- [CBAM News](cbam-news.md)
- [Immigration Policy News](immigration-policy-news.md)
