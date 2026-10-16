# Depression News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “depression news” · 110/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [depression-news.json](../../examples/scenarios/depression-news.json).

**Question.** How much depression coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="depression"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 40,179 |
| Negative · neutral · positive | 22% · 1.2% · 77% |
| Critical (priority 7–9) | 38% (15,254 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (11,079 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | herbal medicine and plant-based remedies |

## Twelve months of coverage

Monthly matching articles for `depression` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,797 | 59% | 1,555 | 2,150 | ███████ |
| Jun 2025 | 2,783 | 64% | 1,237 | 1,475 | █████ |
| Jul 2025 | 4,196 | 57% | 1,888 | 2,233 | ████████ |
| Aug 2025 | 5,079 | 53% | 1,956 | 3,006 | █████████ |
| Sep 2025 | 4,516 | 56% | 1,724 | 2,673 | ████████ |
| Oct 2025 | 3,440 | 71% | 1,648 | 1,674 | ██████ |
| Nov 2025 | 3,306 | 64% | 1,397 | 1,810 | ██████ |
| Dec 2025 | 3,612 | 68% | 1,569 | 1,919 | ███████ |
| Jan 2026 | 10,755 | 39% | 2,230 | 8,330 | ███████████████████ |
| Feb 2026 | 11,079 | 35% | 2,441 | 8,513 | ████████████████████ |
| Mar 2026 | 9,267 | 37% | 1,985 | 7,163 | █████████████████ |
| Apr 2026 | 9,078 | 41% | 2,170 | 6,780 | ████████████████ |

The last four complete months averaged 10,045 articles a month against 3,964 in the first four (+153%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 25% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,900 | 15% |
| Iran | 682 | 1.7% |
| United Kingdom | 586 | 1.5% |
| India | 386 | 1.0% |
| Canada | 205 | 0.5% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| herbal medicine and plant-based remedies | 3,815 | 20% | +21094% |
| supplements for cognitive function enhancement | 3,095 | 17% | +416% |
| adaptogenic herbs for stress relief | 3,090 | 16% | +418% |
| herbal supplements and their uses | 3,072 | 16% | +415% |
| mental health research and foundations | 756 | 4.0% | +14% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [“Storage Wars”’ Darrell Sheets Opened Up About Depression Nearly 10 Years Before Death by Suicide](https://www.yahoo.com/entertainment/tv/articles/storage-wars-darrell-sheets-opened-032346109.html) | yahoo.com | 9 | negative |
| 23 Apr 2026 | [Storage Wars’ Darrell Sheets Opened Up About Depression Nearly 10 Years Before Death by Suicide](https://www.yahoo.com/entertainment/celebrity/articles/storage-wars-darrell-sheets-opened-234718030.html) | yahoo.com | 9 | negative |
| 10 Apr 2026 | [When a nation starts to question its own mind](https://www.monitor.co.ug/uganda/oped/commentary/when-a-nation-starts-to-question-its-own-mind-5418752) | monitor.co.ug | 9 | negative |
| 26 Mar 2026 | [25-year-old woman with depression to die by euthanasia in landmark case](https://www.uniladtech.com/news/tech-news/noelia-castillo-ramos-depression-euthanasia-case-744409-20260326) | uniladtech.com | 9 | negative |
| 10 Mar 2026 | [Rapist attacked vulnerable man in Lancashire 8 years after release for same offence](https://www.lancashiretelegraph.co.uk/news/25924288.rapist-attacked-vulnerable-man-lancashire-8-years-release-offence/) | lancashiretelegraph.co.uk | 9 | negative |
| 5 Mar 2026 | [TikToker Riziki Ilenre Died by Suicide, Alabama Officials Confirm](https://www.yahoo.com/entertainment/celebrity/articles/tiktoker-riziki-ilenre-died-suicide-164513334.html) | yahoo.com | 9 | negative |
| 4 Mar 2026 | [Traumas do estupro: medo, vergonha e culpa perseguem vítimas de violência sexual, dizem especialistas](https://oglobo.globo.com/rio/noticia/2026/03/04/traumas-do-estupro-medo-vergonha-e-culpa-perseguem-vitimas-de-violencia-sexual-dizem-especialistas.ghtml) | oglobo.globo.com | 9 | negative |
| 21 Feb 2026 | [Telangana: Depressed mother kills her 6-year-old son, dies by suicide in Telanganaâs Vikarabad \| Hyderabad…](https://timesofindia.indiatimes.com/city/hyderabad/depressed-mother-kills-her-6-yr-old-son-dies-by-suicide/articleshow/128648902.cms) | timesofindia.indiatimes.com | 9 | negative |
| 4 Feb 2026 | [Depressão Kristin \| Timor-Leste aprova donativo de 4,2 milhões de euros de apoio a Portugal](https://hojemacau.com.mo/2026/02/05/depressao-kristin-timor-leste-aprova-donativo-de-42-milhoes-de-euros-de-apoio-a-portugal/) | hojemacau.com.mo | 9 | negative |
| 28 Jan 2026 | [Tempestade Kristin deixou rasto de destruição. Como foi afetado o acesso à internet? - Tek Notícias](https://tek.sapo.pt/noticias/internet/artigos/tempestade-kristin-deixou-rasto-de-destruicao-como-foi-afetado-o-acesso-a-internet/) | tek.sapo.pt | 9 | negative |
| 22 Jan 2026 | [Hyderabad: Woman dies, three critical after alleged suicide attempt in Jagathgirigutta](https://telanganatoday.com/hyderabad-woman-dies-three-critical-after-alleged-suicide-attempt-in-jagathgirigutta) | telanganatoday.com | 9 | negative |
| 11 Jan 2026 | [Tamil Nadu Rains: Heavy downpour in several districts, IMD issues orange alert – See full forecast](https://www.financialexpress.com/india-news/tamil-nadu-rains-heavy-downpour-in-several-districts-imd-issues-orange-alert-see-full-forecast/4103555/) | financialexpress.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "depression" --since 2026-01-01 --until 2026-04-30
prism-news trends "depression" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "depression" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "depression", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "depression", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Malaria Outbreak](malaria-outbreak.md)
- [Clinical Trial News](clinical-trial-news.md)
- [Sepsis News](sepsis-news.md)
- [Dengue News](dengue-news.md)
