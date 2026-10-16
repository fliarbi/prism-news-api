# Disaster Management News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “disaster management news” · 70/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [disaster-management-news.json](../../examples/scenarios/disaster-management-news.json).

**Question.** How did coverage of disaster management develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="disaster management"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,797 |
| Negative · neutral · positive | 53% · 2.8% · 45% |
| Critical (priority 7–9) | 78% (2,973 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (1,588 articles) |
| Most-reported country | India (23% of matches) |
| Strongest theme by lift | weather-related travel disruptions |

## Twelve months of coverage

Monthly matching articles for `disaster management` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,167 | 82% | 737 | 400 | ███████████████ |
| Jun 2025 | 851 | 76% | 470 | 356 | ███████████ |
| Jul 2025 | 1,100 | 74% | 680 | 399 | ██████████████ |
| Aug 2025 | 1,588 | 87% | 1,121 | 440 | ████████████████████ |
| Sep 2025 | 1,114 | 87% | 730 | 344 | ██████████████ |
| Oct 2025 | 851 | 85% | 539 | 300 | ███████████ |
| Nov 2025 | 984 | 90% | 646 | 315 | ████████████ |
| Dec 2025 | 845 | 84% | 478 | 344 | ███████████ |
| Jan 2026 | 712 | 79% | 374 | 315 | █████████ |
| Feb 2026 | 945 | 79% | 475 | 433 | ████████████ |
| Mar 2026 | 854 | 78% | 446 | 392 | ███████████ |
| Apr 2026 | 1,286 | 78% | 693 | 553 | ████████████████ |

The last four complete months averaged 949 articles a month against 1,176 in the first four (-19%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 52% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 875 | 23% |
| United States | 219 | 5.8% |
| Indonesia | 90 | 2.4% |
| Afghanistan | 81 | 2.1% |
| Japan | 63 | 1.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| weather-related travel disruptions | 72 | 2.9% | +118% |
| disaster response and recovery teams | 214 | 8.6% | -17% |
| emergency preparedness and public education | 175 | 7.0% | +28% |
| flood mitigation strategies and case studies | 572 | 23% | -35% |
| hurricane/cyclone impact studies and preparedness | 239 | 9.6% | -44% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Líbano afirma que han muerto 2,387 personas por el ataque de Israel a Hezbolá](http://www.eleconomista.com.mx/internacionales/libano-afirma-han-muerto-2-387-personas-ataque-israel-hezbola-20260420-809546.html) | eleconomista.com.mx | 9 | negative |
| 8 Apr 2026 | [Nationwide rain toll reaches 96 as NDMA reports widespread damage](https://www.24newshd.tv/08-Apr-2026/nationwide-rain-toll-reaches-96-ndma-reports-widespread-damage) | 24newshd.tv | 9 | negative |
| 8 Apr 2026 | [Durban Floods: Chatsworth, Morningside Hit Hard as City Teams Clear Debris](https://www.joburgetc.com/news/durban-flood-damage-city-teams-race-to-restore-order-after-weekend-storm/) | joburgetc.com | 9 | negative |
| 7 Apr 2026 | [Pakistan et Afghanistan \| Des intempéries font 188 morts](https://www.lapresse.ca/international/asie-et-oceanie/2026-04-07/pakistan-et-afghanistan/des-intemperies-font-188-morts.php) | lapresse.ca | 9 | negative |
| 5 Apr 2026 | [77 killed, over 100 injured in Afghanistan floods since March 26: Govt officials](https://businessnewsthisweek.com/international/77-killed-over-100-injured-in-afghanistan-floods-since-march-26-govt-officials/) | businessnewsthisweek.com | 9 | negative |
| 4 Apr 2026 | [Autoridades de Afganistán reportan 77 muertos en 10 días por inundaciones y deslaves](https://apnews.com/article/afganistan-tormentas-deslaves-inundaciones-d407e6d3a5935f8af1cedf10ad26a7da) | apnews.com | 9 | negative |
| 31 Mar 2026 | [PDMA issues rain alert for Punjab from tomorrow \| 24 News HD](https://www.24newshd.tv/31-Mar-2026/pdma-issues-rain-alert-punjab-tomorrow) | 24newshd.tv | 9 | negative |
| 30 Mar 2026 | [Heavy rains and floods kill at least 45 people](https://k24.digital/news/heavy-rains-and-floods-kill-at-least-45-people) | k24.digital | 9 | negative |
| 30 Mar 2026 | [All trapped victims rescued from Accra Newtown building collapse – NADMO - MyJoyOnline](https://www.myjoyonline.com/all-trapped-victims-rescued-from-accra-newtown-building-collapse-nadmo/) | myjoyonline.com | 9 | negative |
| 30 Mar 2026 | [पाकिस्तान में भारी बारिश के कारण नौ की मौत](https://www.livehindustan.com/ncr/new-delhi/story-heavy-rain-in-khyber-pakhtunkhwa-9-dead-including-8-children-201774867136467.html) | livehindustan.com | 9 | negative |
| 20 Feb 2026 | [Ascienden a 228 los muertos por las inundaciones que afectan a Mozambique desde octubre](https://cdn.com.do/internacionales/228-muertos-por-inundaciones-en-mozambique/) | cdn.com.do | 9 | negative |
| 16 Feb 2026 | [Ciclone deixa 59 mortos e milhares desalojados em Madagascar](https://veja.abril.com.br/mundo/ciclone-deixa-59-mortos-e-milhares-desalojados-em-madagascar/) | veja.abril.com.br | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "disaster management" --since 2026-01-01 --until 2026-04-30
prism-news trends "disaster management" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "disaster management" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "disaster management", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "disaster management", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Land Acquisition News](land-acquisition-news.md)
- [Social Media Regulation News](social-media-regulation-news.md)
- [Wealth Tax News](wealth-tax-news.md)
