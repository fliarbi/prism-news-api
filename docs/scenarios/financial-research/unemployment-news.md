# Unemployment News: volume, tone and critical headlines (Jan–Apr 2026)

[Financial research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “unemployment news” · 320/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [unemployment-news.json](../../examples/scenarios/unemployment-news.json).

**Question.** What did the news say about unemployment between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?

**Request.** `q="unemployment"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,581 |
| Negative · neutral · positive | 66% · 3.3% · 31% |
| Critical (priority 7–9) | 74% (7,849 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (3,808 articles) |
| Most-reported country | United States (18% of matches) |
| Strongest theme by lift | economy news: unemployment rate trends |

## Twelve months of coverage

Monthly matching articles for `unemployment` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,252 | 70% | 2,207 | 914 | █████████████████ |
| Jun 2025 | 1,740 | 74% | 1,105 | 570 | █████████ |
| Jul 2025 | 2,420 | 62% | 1,526 | 806 | █████████████ |
| Aug 2025 | 3,808 | 73% | 2,698 | 1,047 | ████████████████████ |
| Sep 2025 | 2,663 | 78% | 1,756 | 832 | ██████████████ |
| Oct 2025 | 1,761 | 77% | 1,174 | 512 | █████████ |
| Nov 2025 | 1,760 | 75% | 1,108 | 596 | █████████ |
| Dec 2025 | 2,336 | 78% | 1,526 | 714 | ████████████ |
| Jan 2026 | 1,878 | 74% | 1,243 | 577 | ██████████ |
| Feb 2026 | 2,909 | 75% | 1,897 | 914 | ███████████████ |
| Mar 2026 | 2,596 | 76% | 1,820 | 671 | ██████████████ |
| Apr 2026 | 3,198 | 72% | 2,017 | 1,055 | █████████████████ |

The last four complete months averaged 2,645 articles a month against 2,805 in the first four (-6%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 41% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,947 | 18% |
| India | 524 | 5.0% |
| United Kingdom | 324 | 3.1% |
| Iran | 192 | 1.8% |
| South Africa | 164 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| economy news: unemployment rate trends | 3,372 | 49% | +41% |
| economy news: labor market dynamics | 3,350 | 49% | +50% |
| unemployment insurance benefits & claims | 216 | 3.2% | -68% |
| demographic economics and population trends | 152 | 2.2% | +39% |
| economy news: consumer confidence index updates | 138 | 2.0% | +23% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 19 Apr 2026 | [In recent years in this country Have suicides increased?](https://medianews.az/en/son-illerde-bu-olkede-intiharlar-artibmi) | medianews.az | 9 | negative |
| 6 Apr 2026 | [Jobless young Palestinians trapped as Israel holds Gaza’s economy hostage](https://www.aljazeera.com/economy/2026/4/6/jobless-young-palestinians-trapped-as-israel-holds-gazas-economy-hostage) | aljazeera.com | 9 | negative |
| 20 Mar 2026 | [Pakistan-Occupied Kashmir Crisis: Protests, Neglect, Crackdowns](https://www.newkerala.com/news/a/humanitarian-crisis-deepens-pakistan-occupied-kashmir-amid-crackdowns-systematic-886.htm) | newkerala.com | 9 | negative |
| 19 Jan 2026 | [Migrant who sexually assaulted girl, 15, & then fled to UK to be deported](https://www.thescottishsun.co.uk/news/15818964/migrant-sex-assault-girl-fleeing-germany-fighting-deportation/) | thescottishsun.co.uk | 9 | negative |
| 29 Apr 2026 | [Lloyds takes £151m hit from Iran war as it forecasts rise in UK unemployment](https://www.theguardian.com/business/2026/apr/29/lloyds-iran-war-forecasts-rise-in-uk-unemployment) | theguardian.com | 8 | negative |
| 29 Apr 2026 | [Indonesia’s AI strategy: Economically ambitious, socially hollow](https://www.thestar.com.my/business/insight/2026/04/29/indonesias-ai-strategy-economically-ambitious-socially-hollow) | thestar.com.my | 8 | positive |
| 28 Apr 2026 | [War With U.S. And Israel Pushes Millions Of Iranians Toward Unemployment As Economy Tanks](https://ibtimes.com/war-us-israel-pushes-millions-iranians-toward-unemployment-economy-tanks-3802093) | ibtimes.com | 8 | negative |
| 28 Apr 2026 | [Unemployment, migration concerns drive March and March protest](https://www.enca.com/news-top-stories-videos/unemployment-migration-concerns-drive-march-and-march-protest) | enca.com | 8 | negative |
| 28 Apr 2026 | [El paro sube en 231.500 personas hasta marzo, su mayor alza desde 2013](https://capital.es/actualidad/el-paro-sube-en-231-500-personas-hasta-marzo-su-mayor-alza-desde-2013-y-se-destruyen-170-300-empleos/180548/) | capital.es | 8 | negative |
| 27 Apr 2026 | [Informe de ONU Mujeres revela brechas salariales, violencia política y cargas de cuidado no remuneradas](https://www.eltiempo.com/politica/partidos-politicos/informe-de-onu-mujeres-revela-brechas-salariales-violencia-politica-y-cargas-de-cuidado-no-remuneradas-3551054) | eltiempo.com | 8 | negative |
| 25 Apr 2026 | [BJP to Secure 180 Seats in West Bengal: Raju Bista](https://www.newkerala.com/news/a/bjp-secure-180-seats-west-bengal-raju-bista-765.htm) | newkerala.com | 8 | positive |
| 24 Apr 2026 | [Surprise Fall In Unemployment But Threat Remains \| Herefordshire & Worcestershire Chamber of Commerce](https://hwchamber.co.uk/surprise-fall-in-unemployment-but-threat-remains/) | hwchamber.co.uk | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "unemployment" --since 2026-01-01 --until 2026-04-30
prism-news trends "unemployment" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "unemployment" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "unemployment", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "unemployment", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Dividend News](dividend-news.md)
- [Copper Price News](copper-price-news.md)
- [Retirement News](retirement-news.md)
- [Treasury Yields News](treasury-yields-news.md)
