# Film Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “film industry” · 5,400/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [film-industry.json](../../examples/scenarios/film-industry.json).

**Question.** How much news did the film industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="film industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 28,431 |
| Negative · neutral · positive | 23% · 0.7% · 77% |
| Critical (priority 7–9) | 22% (6,220 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (8,472 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | film production insurance |

## Twelve months of coverage

Monthly matching articles for `film industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5,400 | 27% | 1,922 | 3,386 | █████████████ |
| Jun 2025 | 3,193 | 16% | 805 | 2,356 | ████████ |
| Jul 2025 | 4,569 | 17% | 1,041 | 3,486 | ███████████ |
| Aug 2025 | 4,098 | 19% | 941 | 3,126 | ██████████ |
| Sep 2025 | 4,650 | 24% | 1,179 | 3,424 | ███████████ |
| Oct 2025 | 4,090 | 19% | 854 | 3,196 | ██████████ |
| Nov 2025 | 4,106 | 19% | 892 | 3,167 | ██████████ |
| Dec 2025 | 5,393 | 25% | 1,166 | 4,179 | █████████████ |
| Jan 2026 | 5,630 | 20% | 1,199 | 4,378 | █████████████ |
| Feb 2026 | 7,192 | 26% | 1,915 | 5,220 | █████████████████ |
| Mar 2026 | 7,137 | 18% | 1,358 | 5,723 | █████████████████ |
| Apr 2026 | 8,472 | 23% | 1,984 | 6,426 | ████████████████████ |

The last four complete months averaged 7,108 articles a month against 4,315 in the first four (+65%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,927 | 21% |
| India | 3,275 | 12% |
| United Kingdom | 845 | 3.0% |
| China | 284 | 1.0% |
| France | 254 | 0.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| film production insurance | 363 | 3.0% | +72% |
| film festivals & award ceremonies | 721 | 5.9% | +148% |
| film licensing & copyright management | 628 | 5.1% | +55% |
| film tax incentive programs | 448 | 3.7% | +35% |
| entertainment industry awards shows | 1,193 | 9.8% | +179% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Warner Bros. Shareholders Approve Merger With Paramount Despite Woke Hollywood Meltdown \| The Gateway Pundit…](https://www.thegatewaypundit.com/2026/04/warner-bros-shareholders-approve-merger-paramount-despite-woke/) | thegatewaypundit.com | 8 | negative |
| 24 Apr 2026 | [Film industry’s connection surfaces in Mumbai’s NESCO drug case; actress’ role under scanner](https://www.news9live.com/city/mumbai/film-industrys-connection-surfaces-in-mumbais-nesco-drugs-case-actress-role-under-scanner-2963104) | news9live.com | 8 | negative |
| 22 Apr 2026 | [Mamitha Baiju, co-star of Thalapathy Vijay, responds to the 'unfortunate' Jana Nayagan leak, emphasizing…](https://www.zoomtventertainment.com/south/mamitha-baiju-sympathizes-with-makers-leak-disappointing-painful-article-154139582) | zoomtventertainment.com | 8 | negative |
| 22 Apr 2026 | [Dacoit Worldwide Box Office Update on Day 4: Adivi Sesh Is Just 4 Crore Short of Exceeding the Global…](https://www.zoomtventertainment.com/bollywood/adivi-sesh-dacoit-worldwide-box-office-collection-article-154137207) | zoomtventertainment.com | 8 | positive |
| 21 Apr 2026 | [Watch: Tollywood Footfalls Fall, Revenue Still Holds Strong](https://www.gulte.com/movienews/407215/watch-tollywood-footfalls-fall-revenue-still-holds-strong) | gulte.com | 8 | positive |
| 20 Apr 2026 | [Chiranjeevi Donates Rs 20 Lakh For Medical Emergencies, Personally Visits Ailing Makeup Artist](https://www.newsx.com/entertainment/chiranjeevi-donates-rs-20-lakh-for-medical-emergencies-personally-visits-ailing-makeup-artist-202182/) | newsx.com | 8 | — |
| 14 Apr 2026 | [Alec Baldwin Says He Wants to Retire After Rust Tragedy - Time News](https://time.news/alec-baldwin-says-he-wants-to-retire-after-rust-tragedy/) | time.news | 8 | negative |
| 14 Apr 2026 | [Jana Nayagan Leak Controversy: Editors' Union Supports Pradeep E Raghav, Condemns Groundless Allegations -…](https://www.zoomtventertainment.com/south/tamil-nadu-police-investigate-jana-nayagan-leak-suspects-detained-piracy-links-blocked-article-154073893) | zoomtventertainment.com | 8 | negative |
| 14 Apr 2026 | [Paramount REPLIES To Hollywood's Open Letter Against Warner Bros Agreement - Their Statement](https://www.zoomtventertainment.com/hollywood/paramount-skydance-warner-bros-deal-opposition-article-154072710) | zoomtventertainment.com | 8 | negative |
| 14 Apr 2026 | [Paramount RESPONDS To Hollywood's Open Letter Opposing Warner Bros Deal - What They Said](https://www.timesnownews.com/entertainment-news/hollywood/paramount-responds-to-hollywoods-open-letter-opposing-warner-bros-deal-what-they-said-article-154072152) | timesnownews.com | 8 | negative |
| 14 Apr 2026 | [Alec Baldwin admits he 'doesn’t want to work anymore' after 'Rust' shooting death: 'I want to retire'](https://www.foxnews.com/entertainment/alec-baldwin-admits-doesnt-want-work-anymore-rust-shooting-death-want-retire) | foxnews.com | 8 | negative |
| 13 Apr 2026 | [Asha Bhosle Funeral: Ranveer Singh and Tabu Console Singer’s Granddaughter Zanai Bhosle As She Cries…](https://www.latestly.com/entertainment/bollywood/asha-bhosle-funeral-ranveer-singh-and-tabu-console-singers-daughter-zanai-bhosle-as-she-cries-inconsolably-watch-videos-7391661.html) | latestly.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "film industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "film industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "film industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "film industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "film industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Shipbuilding Industry](shipbuilding-industry.md)
- [Hospitality Industry](hospitality-industry.md)
- [Retail Industry News](retail-industry-news.md)
- [FMCG Industry](fmcg-industry.md)
