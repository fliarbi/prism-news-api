# Recycling Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “recycling industry” · 260/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [recycling-industry.json](../../examples/scenarios/recycling-industry.json).

**Question.** How did recycling coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="recycling"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 22,556 |
| Negative · neutral · positive | 17% · 1.3% · 82% |
| Critical (priority 7–9) | 49% (11,050 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (6,857 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | circular economy principles |

## Twelve months of coverage

Monthly matching articles for `recycling` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,931 | 47% | 609 | 3,235 | ███████████ |
| Jun 2025 | 3,623 | 52% | 513 | 3,069 | ███████████ |
| Jul 2025 | 3,976 | 50% | 653 | 3,253 | ████████████ |
| Aug 2025 | 4,254 | 51% | 1,080 | 3,127 | ████████████ |
| Sep 2025 | 4,601 | 53% | 696 | 3,853 | █████████████ |
| Oct 2025 | 4,305 | 51% | 631 | 3,642 | █████████████ |
| Nov 2025 | 4,529 | 48% | 583 | 3,884 | █████████████ |
| Dec 2025 | 4,217 | 51% | 693 | 3,452 | ████████████ |
| Jan 2026 | 4,390 | 51% | 655 | 3,680 | █████████████ |
| Feb 2026 | 5,808 | 50% | 1,020 | 4,681 | █████████████████ |
| Mar 2026 | 5,501 | 48% | 955 | 4,485 | ████████████████ |
| Apr 2026 | 6,857 | 48% | 1,168 | 5,585 | ████████████████████ |

The last four complete months averaged 5,639 articles a month against 3,946 in the first four (+43%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 41% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,164 | 18% |
| United Kingdom | 1,225 | 5.4% |
| India | 808 | 3.6% |
| China | 333 | 1.5% |
| Australia | 310 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| circular economy principles | 1,649 | 11% | +16% |
| recycling and waste reduction initiatives | 967 | 6.6% | +106% |
| composting and organic waste management | 1,731 | 12% | +49% |
| electronic waste recycling programs | 762 | 5.2% | +45% |
| plastic pollution solutions | 1,390 | 9.4% | +22% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 15 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Why Kenya’s insurance industry must lead the circular revolution](https://www.businessdailyafrica.com/bd/opinion-analysis/columnists/why-kenya-s-insurance-industry-must-lead-circular-revolution-5423418) | businessdailyafrica.com | 9 | negative |
| 11 Jan 2026 | [Chaos as trains cancelled & delayed after massive fire near Heathrow Airport](https://www.thesun.co.uk/news/37879966/trains-cancelled-fire-heathrow-airport/) | thesun.co.uk | 9 | negative |
| 30 Apr 2026 | [Man Takes Safaricom to Court Over Recycled SIM Card](https://businesstoday.co.ke/man-takes-safaricom-to-court-over-recycled-sim-card/) | businesstoday.co.ke | 8 | negative |
| 23 Apr 2026 | [Mount Dora man arrested for impersonating an Ocoee firefighter](https://www.yahoo.com/news/articles/mount-dora-man-arrested-impersonating-020206825.html) | yahoo.com | 8 | negative |
| 22 Apr 2026 | [UNSW Sydney announced the opening of Australia's first solar panel recycling research centre on Wednesday,…](https://www.cobramcourier.com.au/national/after-the-sun-sets-hub-to-tackle-coming-e-waste-crisis/) | cobramcourier.com.au | 8 | positive |
| 21 Apr 2026 | [India’s textile waste holds billions, but inefficiencies block recovery \| Today News](https://www.livemint.com/news/india-losing-9-4-billion-from-textile-waste-due-to-gaps-in-collection-sorting-and-recycling-systems-ficci-report-11776775649498.html) | livemint.com | 8 | positive |
| 21 Apr 2026 | [Community Cares](https://www.madisoncourier.com/online_features/community_cares) | madisoncourier.com | 8 | negative |
| 17 Apr 2026 | [Sustainable recycling of spent aluminium electrolyte for AlF3 and efficient fluoride recovery via an…](https://pubmed.ncbi.nlm.nih.gov/41996551/) | pubmed.ncbi.nlm.nih.gov | 8 | positive |
| 16 Apr 2026 | [UK food-grade plastics recycling plant goes live](https://ecoplasticsinpackaging.com/processes/recycling/nextek-and-coveris-launch-uk-chemical-recycling-demo-plant/) | ecoplasticsinpackaging.com | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "recycling" --since 2026-01-01 --until 2026-04-30
prism-news trends "recycling" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "recycling" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "recycling", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "recycling", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Wildfire News](wildfire-news.md)
- [OPEC News](opec-news.md)
- [Nuclear Power News](nuclear-power-news.md)
- [LNG News](lng-news.md)
