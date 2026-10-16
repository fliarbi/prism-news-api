# Paper Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “paper industry” · 1,900/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [paper-industry.json](../../examples/scenarios/paper-industry.json).

**Question.** How much news did the paper industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="paper industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 187 |
| Negative · neutral · positive | 21% · 1.1% · 78% |
| Critical (priority 7–9) | 42% (78 articles) |
| Busiest month, May 2025 – Apr 2026 | Nov 2025 (122 articles) |
| Most-reported country | United States (11% of matches) |
| Strongest theme by lift | agrochemicals development and distribution |

## Twelve months of coverage

Monthly matching articles for `paper industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 40 | 25% | 9 | 31 | ███████ |
| Jun 2025 | 35 | 40% | 8 | 27 | ██████ |
| Jul 2025 | 16 | 6.2% | 2 | 14 | ███ |
| Aug 2025 | 37 | 51% | 13 | 23 | ██████ |
| Sep 2025 | 60 | 32% | 13 | 44 | ██████████ |
| Oct 2025 | 47 | 49% | 6 | 40 | ████████ |
| Nov 2025 | 122 | 41% | 29 | 92 | ████████████████████ |
| Dec 2025 | 41 | 44% | 8 | 33 | ███████ |
| Jan 2026 | 38 | 58% | 4 | 34 | ██████ |
| Feb 2026 | 55 | 31% | 18 | 37 | █████████ |
| Mar 2026 | 55 | 36% | 9 | 46 | █████████ |
| Apr 2026 | 39 | 49% | 9 | 28 | ██████ |

The last four complete months averaged 47 articles a month against 32 in the first four (+46%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 34% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 20 | 11% |
| India | 7 | 3.7% |
| United Kingdom | 6 | 3.2% |
| China | 5 | 2.7% |
| Spain | 3 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| agrochemicals development and distribution | 6 | 7.1% | new |
| biofuel production & algae-based energy | 5 | 5.9% | +150% |
| circular economy principles | 6 | 7.1% | +50% |
| sustainability initiatives and esg reporting | 10 | 12% | +0% |
| company expansions and new market entries | 6 | 7.1% | +50% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 8 Apr 2026 | [Enzyme produced by fungus replace chemicals in paper industry](https://www.papermarket.co.in/enzyme-produced-by-fungus-may-replace-chemicals-in-the-paper-industry/) | papermarket.co.in | 7 | positive |
| 13 Mar 2026 | [West Asia Crisis: A Double Whammy for India’s Paper Industry](https://www.papermarket.co.in/west-asia-crisis-a-double-whammy-for-indias-paper-industry/) | papermarket.co.in | 7 | positive |
| 9 Mar 2026 | [Indian Paper Sector Faces Twin Pressures from Ongoing West Asia Conflict - India Seatrade News](https://indiaseatradenews.com/indian-paper-sector-faces-twin-pressures-from-ongoing-west-asia-conflict/) | indiaseatradenews.com | 7 | negative |
| 29 Jan 2026 | [- Cyprus Shipping News](https://cyprusshippingnews.com/2026/01/29/totalenergies-to-supply-800-gwh-of-renewable-electricity-to-paper-manufacturer-swm-over-10-years-in-france/) | cyprusshippingnews.com | 7 | positive |
| 29 Jan 2026 | [TotalEnergies locks in 10-yr clean power deal with SWM](https://www.indianchemicalnews.com/energy/totalenergies-locks-in-10-yr-clean-power-deal-with-swm-29084) | indianchemicalnews.com | 7 | positive |
| 21 Jan 2026 | [Could stable January lead to better year for recovered paper markets?](https://www.recyclingtoday.com/news/recovered-paper-industry-sees-january-pricing-demand-stability/) | recyclingtoday.com | 7 | negative |
| 9 Jan 2026 | [Emirados têm 750 milhões para revitalizar pasta de papel de Angola](https://jornaleconomico.sapo.pt/noticias/emirados-tem-750-milhoes-para-revitalizar-pasta-de-papel-de-angola/) | jornaleconomico.sapo.pt | 7 | positive |
| 6 Jan 2026 | [जीएसटी पंजीकरण का ग्राफ बढ़ा, 28 हजार व्यापारी सक्रिय](https://www.livehindustan.com/uttar-pradesh/muzaffar-nagar/story-significant-growth-in-gst-registrations-in-muzaffarnagar-28-585-active-traders-201767724270504.html) | livehindustan.com | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "paper industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "paper industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "paper industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "paper industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "paper industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cosmetics Industry](cosmetics-industry.md)
- [Mining Industry](mining-industry.md)
- [Biotech Industry](biotech-industry.md)
- [Trucking Industry](trucking-industry.md)
