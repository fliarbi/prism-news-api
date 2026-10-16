# Anxiety News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “anxiety news” · 20/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [anxiety-news.json](../../examples/scenarios/anxiety-news.json).

**Question.** How much anxiety coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="anxiety"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 55,297 |
| Negative · neutral · positive | 27% · 0.8% · 73% |
| Critical (priority 7–9) | 33% (18,082 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (14,805 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | herbal medicine and plant-based remedies |

## Twelve months of coverage

Monthly matching articles for `anxiety` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9,510 | 36% | 2,963 | 6,430 | █████████████ |
| Jun 2025 | 5,909 | 37% | 1,894 | 3,927 | ████████ |
| Jul 2025 | 13,432 | 24% | 3,092 | 10,241 | ██████████████████ |
| Aug 2025 | 10,075 | 37% | 3,034 | 6,939 | ██████████████ |
| Sep 2025 | 7,894 | 37% | 2,336 | 5,453 | ███████████ |
| Oct 2025 | 5,316 | 46% | 2,138 | 3,066 | ███████ |
| Nov 2025 | 5,815 | 42% | 2,194 | 3,530 | ████████ |
| Dec 2025 | 6,113 | 43% | 2,257 | 3,756 | ████████ |
| Jan 2026 | 13,915 | 31% | 3,198 | 10,544 | ███████████████████ |
| Feb 2026 | 14,805 | 29% | 3,549 | 11,126 | ████████████████████ |
| Mar 2026 | 13,466 | 35% | 3,827 | 9,501 | ██████████████████ |
| Apr 2026 | 13,111 | 36% | 4,064 | 8,904 | ██████████████████ |

The last four complete months averaged 13,824 articles a month against 9,732 in the first four (+42%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 28% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 8,282 | 15% |
| United Kingdom | 1,160 | 2.1% |
| India | 1,065 | 1.9% |
| Iran | 779 | 1.4% |
| Canada | 306 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| herbal medicine and plant-based remedies | 3,838 | 14% | +14115% |
| supplements for cognitive function enhancement | 3,095 | 11% | +141% |
| adaptogenic herbs for stress relief | 3,090 | 11% | +141% |
| herbal supplements and their uses | 3,072 | 11% | +141% |
| emotional intelligence development | 621 | 2.3% | +166% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Former Spandau Ballet singer jailed for 14 years for rape and sexual assault](http://standard.co.uk/news/crime/spandau-ballet-singer-jailed-rape-sexual-assault-b1280593.html) | standard.co.uk | 9 | negative |
| 30 Apr 2026 | [चार दिन बाद भी सहमी छात्रा ने स्कूल जाना नहीं किया शुरू](https://www.livehindustan.com/ncr/faridabad/story-fatehpur-billouch-sexual-harassment-case-victim-in-trauma-police-hunt-for-accused-201777549645072.html) | livehindustan.com | 9 | negative |
| 21 Apr 2026 | [High school counselor pleads guilty to multiple sex crimes involving teen she was meant to help](https://www.foxnews.com/us/high-school-counselor-pleads-guilty-multiple-sex-crimes-involving-teen-she-meant-help) | foxnews.com | 9 | negative |
| 14 Apr 2026 | [Man dies after overdose of ‘highly toxic’ heart drug - GPs must ‘be on alert’](https://www.thesun.co.uk/health/38812151/man-dies-toxic-heart-medication-gps-alert/) | thesun.co.uk | 9 | negative |
| 10 Apr 2026 | [When a nation starts to question its own mind](https://www.monitor.co.ug/uganda/oped/commentary/when-a-nation-starts-to-question-its-own-mind-5418752) | monitor.co.ug | 9 | negative |
| 24 Mar 2026 | [58 साल के शख्स पर 10 साल की बच्ची से दरिंदगी का आरोप, ठाणे में आरोपी के खिलाफ केस दर्ज](https://www.aajtak.in/crime/news/story/thane-bhiwandi-minor-rape-case-pocso-accused-arrest-pvzs-dskc-2505589-2026-03-24) | aajtak.in | 9 | negative |
| 21 Mar 2026 | [Joe Biden Hidden Illness: Physician Claims Cancer Spread to Bone During Presidency](https://www.ibtimes.co.uk/joe-biden-hidden-illness-physician-claims-cancer-spread-bone-during-presidency-1787216) | ibtimes.co.uk | 9 | negative |
| 14 Mar 2026 | [Iran fires six missile volleys at Israel; few injured as interceptions limit damage](https://www.yahoo.com/news/articles/teen-injured-eilat-iran-launches-154457904.html) | yahoo.com | 9 | negative |
| 10 Mar 2026 | [Rapist attacked vulnerable man in Lancashire 8 years after release for same offence](https://www.lancashiretelegraph.co.uk/news/25924288.rapist-attacked-vulnerable-man-lancashire-8-years-release-offence/) | lancashiretelegraph.co.uk | 9 | negative |
| 6 Mar 2026 | [Israel says more than 1,600 injured since start of Iran war](https://www.yahoo.com/news/articles/israel-says-more-1-600-105817467.html) | yahoo.com | 9 | negative |
| 4 Mar 2026 | [Traumas do estupro: medo, vergonha e culpa perseguem vítimas de violência sexual, dizem especialistas](https://oglobo.globo.com/rio/noticia/2026/03/04/traumas-do-estupro-medo-vergonha-e-culpa-perseguem-vitimas-de-violencia-sexual-dizem-especialistas.ghtml) | oglobo.globo.com | 9 | negative |
| 27 Feb 2026 | [How Israelis Feel About Another Potential War With Iran](https://indianexpress.com/article/world/how-israelis-feel-about-another-potential-war-with-iran-10556020/) | indianexpress.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "anxiety" --since 2026-01-01 --until 2026-04-30
prism-news trends "anxiety" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "anxiety" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "anxiety", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "anxiety", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Lupus News](lupus-news.md)
- [Hypertension News](hypertension-news.md)
- [Cell Therapy News](cell-therapy-news.md)
- [Telemedicine News](telemedicine-news.md)
