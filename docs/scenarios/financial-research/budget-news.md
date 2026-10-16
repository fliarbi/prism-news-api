# Budget News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “budget news” · 6,600/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [budget-news.json](../../examples/scenarios/budget-news.json).

**Question.** What did the news say about budget between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="budget"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 108,920 |
| Negative · neutral · positive | 33% · 3.8% · 63% |
| Critical (priority 7–9) | 49% (53,625 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (34,849 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | interior comfort and ergonomics reviews |

## Twelve months of coverage

Monthly matching articles for `budget` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18,635 | 55% | 9,219 | 8,540 | ███████████ |
| Jun 2025 | 14,634 | 58% | 7,446 | 6,645 | ████████ |
| Jul 2025 | 18,952 | 51% | 9,475 | 8,760 | ███████████ |
| Aug 2025 | 22,875 | 49% | 10,842 | 11,304 | █████████████ |
| Sep 2025 | 21,712 | 40% | 7,596 | 13,258 | ████████████ |
| Oct 2025 | 16,761 | 54% | 8,213 | 7,638 | ██████████ |
| Nov 2025 | 28,066 | 40% | 17,503 | 9,598 | ████████████████ |
| Dec 2025 | 19,956 | 43% | 6,901 | 11,825 | ███████████ |
| Jan 2026 | 19,210 | 51% | 6,359 | 11,826 | ███████████ |
| Feb 2026 | 34,849 | 57% | 10,944 | 22,659 | ████████████████████ |
| Mar 2026 | 30,767 | 36% | 8,307 | 21,631 | ██████████████████ |
| Apr 2026 | 24,094 | 53% | 10,614 | 12,362 | ██████████████ |

The last four complete months averaged 27,230 articles a month against 18,774 in the first four (+45%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 46% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 16,262 | 15% |
| India | 15,047 | 14% |
| United Kingdom | 2,718 | 2.5% |
| Central African Republic | 2,489 | 2.3% |
| Greece | 1,843 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| interior comfort and ergonomics reviews | 2,841 | 4.7% | +41% |
| vehicle dimensions and cargo space specs | 2,016 | 3.3% | +15% |
| kia fuel efficiency and emissions data | 1,866 | 3.1% | +979% |
| kia performance and gt-line models | 1,824 | 3.0% | +967% |
| kia engine specifications and technologies | 1,723 | 2.9% | +908% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 21 Apr 2026 | [Budget surplus while families struggle to heat homes, says Sinn Fein leader](https://www.limerickleader.ie/news/national-news/2066789/budget-surplus-while-families-struggle-to-heat-homes-says-sinn-fein-leader.html) | limerickleader.ie | 9 | negative |
| 29 Mar 2026 | [Experts: Sanctions less effective than Ukraine's attacks on Russia's oil ports](https://news.err.ee/1609980979/experts-sanctions-less-effective-than-ukraine-s-attacks-on-russia-s-oil-ports) | news.err.ee | 9 | negative |
| 25 Mar 2026 | [Delhi Assembly gets bomb threat for second time in 24 hours, search operation underway](https://www.indiatvnews.com/delhi/delhi-assembly-gets-bomb-threat-for-second-time-in-24-hours-search-operation-underway-2026-03-25-1035026) | indiatvnews.com | 9 | negative |
| 20 Mar 2026 | [Deux cents milliards de dollars, des fissures au CongrÃ¨s et un alliÃ© qui nâobÃ©it plus](https://www.24heures.ch/iran-trump-demande-200-milliards-au-congres-pour-la-guerre-482151531148) | 24heures.ch | 9 | negative |
| 26 Jan 2026 | [Minneapolis: Nach Todesschüssen breitet sich Protest aus](https://www.moneycab.com/international/wut-und-protest-nach-toedlichen-schuessen-in-minneapolis/) | moneycab.com | 9 | negative |
| 26 Jan 2026 | [Abschiebepolitik: Minneapolis: Nach Todesschüssen breitet sich Protest aus](https://www.tagesspiegel.de/internationales/abschiebepolitik-minneapolis-nach-todesschussen-breitet-sich-protest-aus-15180161.html) | tagesspiegel.de | 9 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Quesnel Cariboo Observer](https://quesnelobserver.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | quesnelobserver.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Abbotsford News](https://abbynews.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | abbynews.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Cloverdale Reporter](https://cloverdalereporter.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | cloverdalereporter.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Chemainus Valley Courier](https://chemainusvalleycourier.ca/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | chemainusvalleycourier.ca | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Lake Country Calendar](https://lakecountrycalendar.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | lakecountrycalendar.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Northern Sentinel](https://northernsentinel.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | northernsentinel.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "budget" --since 2026-01-01 --until 2026-04-30
prism-news trends "budget" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "budget" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "budget", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "budget", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [S&P 500 News Today](s-p-500-news-today.md)
- [UPI News](upi-news.md)
- [SEBI News](sebi-news.md)
- [Income Tax News](income-tax-news.md)
