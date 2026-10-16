# Gene Therapy News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gene therapy news” · 90/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [gene-therapy-news.json](../../examples/scenarios/gene-therapy-news.json).

**Question.** How much gene therapy coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="gene therapy"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,990 |
| Negative · neutral · positive | 5.9% · 1.1% · 93% |
| Critical (priority 7–9) | 86% (2,563 articles) |
| Busiest month, May 2025 – Apr 2026 | Jan 2026 (810 articles) |
| Most-reported country | United States (24% of matches) |
| Strongest theme by lift | gene therapy and crispr technologies |

## Twelve months of coverage

Monthly matching articles for `gene therapy` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 695 | 88% | 75 | 612 | █████████████████ |
| Jun 2025 | 498 | 85% | 61 | 430 | ████████████ |
| Jul 2025 | 606 | 87% | 145 | 452 | ███████████████ |
| Aug 2025 | 488 | 85% | 47 | 423 | ████████████ |
| Sep 2025 | 732 | 83% | 35 | 669 | ██████████████████ |
| Oct 2025 | 602 | 88% | 38 | 557 | ███████████████ |
| Nov 2025 | 623 | 88% | 46 | 552 | ███████████████ |
| Dec 2025 | 693 | 87% | 32 | 637 | █████████████████ |
| Jan 2026 | 810 | 90% | 27 | 780 | ████████████████████ |
| Feb 2026 | 750 | 84% | 68 | 674 | ███████████████████ |
| Mar 2026 | 631 | 83% | 58 | 564 | ████████████████ |
| Apr 2026 | 799 | 85% | 23 | 760 | ████████████████████ |

The last four complete months averaged 748 articles a month against 572 in the first four (+31%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 713 | 24% |
| United Kingdom | 79 | 2.6% |
| Central African Republic | 45 | 1.5% |
| Switzerland | 44 | 1.5% |
| China | 42 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| gene therapy and crispr technologies | 899 | 46% | +5% |
| rare disease therapies and orphan drugs | 677 | 34% | +14% |
| biotechnology innovations in medicine | 581 | 29% | +22% |
| stem cell research and applications | 493 | 25% | +1% |
| personalized medicine and genomics | 293 | 15% | +17% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 10 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Gene therapy pioneer David Liu among 2026 Franklin Institute honorees](https://www.inquirer.com/health/franklin-institute-david-liu-honored-gene-therapy-20260430.html) | inquirer.com | 8 | positive |
| 30 Apr 2026 | [MoCo sickle cell patient makes MD history](https://thedailyrecord.com/2026/04/30/moco-woman-a-sickle-cell-patient-makes-md-history/) | thedailyrecord.com | 8 | positive |
| 30 Apr 2026 | [Genprex, Inc. Files Form 8-K With SEC: Company Information, Nasdaq Listing, and Regulatory Details](https://www.minichart.com.sg/2026/04/30/genprex-inc-files-form-8-k-with-sec-company-information-nasdaq-listing-and-regulatory-details/) | minichart.com.sg | 8 | positive |
| 30 Apr 2026 | [Genprex Receives Patent Grant from The Israel Patent Office for the Combination of Reqorsa® Gene Therapy and…](https://www.biospace.com/press-releases/genprex-receives-patent-grant-from-the-israel-patent-office-for-the-combination-of-reqorsa-gene-therapy-and-pd-1-antibodies-to-treat-cancer) | biospace.com | 8 | positive |
| 30 Apr 2026 | [Ray Therapeutics receives EMA PRIME status for gene therapy](https://www.yahoo.com/news/articles/ray-therapeutics-receives-ema-prime-102115316.html) | yahoo.com | 8 | positive |
| 29 Apr 2026 | [UMass Chan Licenses Maple Syrup Urine Disease Gene Therapy to Plowshare Therapies](https://www.precisiononcologynews.com/business-news/umass-chan-licenses-maple-syrup-urine-disease-gene-therapy-plowshare-therapies) | precisiononcologynews.com | 8 | positive |
| 29 Apr 2026 | [Rocket to sell PRV for $180m to advance gene therapy pipeline](https://www.pharmaceutical-business-review.com/news/rocket-to-sell-prv-180m-gene-therapy/) | pharmaceutical-business-review.com | 8 | positive |
| 29 Apr 2026 | [Dr. Jennifer Doudna highlights the future of gene therapy for sickle cell disease - Children's National](https://innovationdistrict.childrensnational.org/dr-jennifer-doudna-highlights-the-future-of-gene-therapy-for-sickle-cell-disease/) | innovationdistrict.childrensnational.org | 8 | positive |
| 28 Apr 2026 | [Why Neurogene chose a brain-delivery route for Rett gene therapy](https://www.stocktitan.net/news/NGNE/neurogene-announces-upcoming-presentation-on-the-therapeutic-4o3x45d1ixut.html) | stocktitan.net | 8 | positive |
| 28 Apr 2026 | [In diabetic mice, Genprex gene therapy reversed high blood sugar in 4 weeks](https://www.stocktitan.net/news/GNPX/genprex-collaborators-to-present-positive-preclinical-data-on-npmupd2n532g.html) | stocktitan.net | 8 | positive |
| 28 Apr 2026 | [News Archives - Pharmaceutical Business review](https://www.pharmaceutical-business-review.com/news/rocket-to-sell-prv-180m-gene-therapy/privacy-policy/privacy-policy/privacy-policy/privacy-policy/) ⚠ | pharmaceutical-business-review.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "gene therapy" --since 2026-01-01 --until 2026-04-30
prism-news trends "gene therapy" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "gene therapy" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "gene therapy", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "gene therapy", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Pandemic News](pandemic-news.md)
- [ADHD News](adhd-news.md)
- [Zika Outbreak](zika-outbreak.md)
- [Prostate Cancer News](prostate-cancer-news.md)
