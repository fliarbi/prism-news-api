# Cell Therapy News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cell therapy news” · 10/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [cell-therapy-news.json](../../examples/scenarios/cell-therapy-news.json).

**Question.** How much cell therapy coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="cell therapy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,861 |
| Negative · neutral · positive | 2.9% · 0.8% · 96% |
| Critical (priority 7–9) | 87% (2,476 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (809 articles) |
| Most-reported country | United States (17% of matches) |
| Strongest theme by lift | gene therapy and crispr technologies |

## Twelve months of coverage

Monthly matching articles for `cell therapy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 602 | 90% | 22 | 575 | ███████████████ |
| Jun 2025 | 500 | 87% | 21 | 474 | ████████████ |
| Jul 2025 | 452 | 87% | 30 | 417 | ███████████ |
| Aug 2025 | 495 | 86% | 18 | 465 | ████████████ |
| Sep 2025 | 536 | 84% | 19 | 509 | █████████████ |
| Oct 2025 | 688 | 90% | 28 | 657 | █████████████████ |
| Nov 2025 | 608 | 89% | 15 | 587 | ███████████████ |
| Dec 2025 | 706 | 91% | 20 | 674 | █████████████████ |
| Jan 2026 | 809 | 91% | 20 | 785 | ████████████████████ |
| Feb 2026 | 748 | 83% | 18 | 724 | ██████████████████ |
| Mar 2026 | 604 | 88% | 24 | 575 | ███████████████ |
| Apr 2026 | 700 | 83% | 20 | 671 | █████████████████ |

The last four complete months averaged 715 articles a month against 512 in the first four (+40%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 32% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 488 | 17% |
| Central African Republic | 149 | 5.2% |
| China | 62 | 2.2% |
| United Kingdom | 45 | 1.6% |
| Germany | 34 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| gene therapy and crispr technologies | 747 | 39% | +26% |
| biotechnology innovations in medicine | 501 | 26% | +36% |
| stem cell research and applications | 486 | 25% | +27% |
| oncology and targeted therapy advancements | 292 | 15% | +8% |
| rare disease therapies and orphan drugs | 292 | 15% | +26% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [The Evolution of CAR T Cell Therapies: From Killers to Multifunctional Strategists](https://www.theedadvocate.org/the-evolution-of-car-t-cell-therapies-from-killers-to-multifunctional-strategists/) | theedadvocate.org | 8 | positive |
| 30 Apr 2026 | [From killers to strategists: CAR T cells enter their multifunctional era](https://www.news-medical.net/news/20260430/From-killers-to-strategists-CAR-T-cells-enter-their-multifunctional-era.aspx) | news-medical.net | 8 | positive |
| 30 Apr 2026 | [Single-cell sequencing reveals why some CAR-T therapies succeed while others fail](https://www.news-medical.net/news/20260430/Single-cell-sequencing-reveals-why-some-CAR-T-therapies-succeed-while-others-fail.aspx) | news-medical.net | 8 | positive |
| 29 Apr 2026 | [Lupus Breakthrough: Off-the-Shelf Cell Therapy Shows 'Immune Reset' Hope](https://briefglance.com/articles/lupus-breakthrough-off-the-shelf-cell-therapy-shows-immune-reset-hope) | briefglance.com | 8 | positive |
| 29 Apr 2026 | [India Strengthens Position as Global Centre for Affordable CAR-T Cancer Therapy \| SportsZ News](https://sportsz.news/health/india-strengthens-position-as-global-centre-for-affordable-car-t-cancer-therapy/) | sportsz.news | 8 | positive |
| 29 Apr 2026 | [India Strengthens Position as Global Centre for Affordable CAR-T Cancer Therapy - Online Media Cafe](https://onlinemediacafe.com/health/india-strengthens-position-as-global-centre-for-affordable-car-t-cancer-therapy/) | onlinemediacafe.com | 8 | positive |
| 29 Apr 2026 | [India Strengthens Position as Global Centre for Affordable CAR-T Cancer Therapy](https://mediabulletins.com/health/india-strengthens-position-as-global-centre-for-affordable-car-t-cancer-therapy/) | mediabulletins.com | 8 | positive |
| 29 Apr 2026 | [Scientists redesign CAR-T cells to fight more than cancer](https://www.news-medical.net/news/20260429/Scientists-redesign-CAR-T-cells-to-fight-more-than-cancer.aspx) | news-medical.net | 8 | positive |
| 28 Apr 2026 | [Cell-free knee arthritis therapy posts 93% response in pilot study](https://www.stocktitan.net/news/CELZ/creative-medical-technology-holdings-inc-reports-breakthrough-93-qexiv65bsjte.html) | stocktitan.net | 8 | positive |
| 22 Apr 2026 | [After 6 of 6 complete responses, Tempest moves toward pivotal CAR-T study](https://www.stocktitan.net/news/TPST/tempest-announces-key-manufacturing-milestone-for-tpst-2003-dual-sk1gnhgakk6b.html) | stocktitan.net | 8 | positive |
| 20 Apr 2026 | [After one dose, 7 myasthenia gravis patients stayed off immunotherapies](https://www.stocktitan.net/news/KYTX/kyverna-presents-longer-term-phase-2-data-for-miv-cel-in-generalized-ufzyog3gmus9.html) ⚠ | stocktitan.net | 8 | positive |
| 20 Apr 2026 | [UCB elevates epilepsy expertise with up to $1.15B Neurona takeover](https://www.biospace.com/deals/ucb-elevates-epilepsy-expertise-with-up-to-1-15b-neurona-takeover) | biospace.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "cell therapy" --since 2026-01-01 --until 2026-04-30
prism-news trends "cell therapy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "cell therapy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "cell therapy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "cell therapy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Hypertension News](hypertension-news.md)
- [Anxiety News](anxiety-news.md)
- [Telemedicine News](telemedicine-news.md)
- [Asthma News](asthma-news.md)
