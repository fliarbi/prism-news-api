# Citizenship News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “citizenship news” · 590/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [citizenship-news.json](../../examples/scenarios/citizenship-news.json).

**Question.** How did coverage of citizenship develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="citizenship"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,512 |
| Negative · neutral · positive | 62% · 10% · 28% |
| Critical (priority 7–9) | 68% (8,525 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,228 articles) |
| Most-reported country | United States (36% of matches) |
| Strongest theme by lift | work visa categories (e.g., h-1b, l-1, tier 2) |

## Twelve months of coverage

Monthly matching articles for `citizenship` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,329 | 53% | 1,709 | 1,226 | ████████████████ |
| Jun 2025 | 1,953 | 68% | 1,338 | 486 | █████████ |
| Jul 2025 | 3,299 | 62% | 2,378 | 753 | ████████████████ |
| Aug 2025 | 2,877 | 60% | 1,872 | 811 | ██████████████ |
| Sep 2025 | 2,572 | 72% | 1,649 | 765 | ████████████ |
| Oct 2025 | 1,844 | 68% | 1,124 | 570 | █████████ |
| Nov 2025 | 2,062 | 74% | 1,446 | 494 | ██████████ |
| Dec 2025 | 2,863 | 76% | 2,052 | 683 | ██████████████ |
| Jan 2026 | 1,862 | 59% | 1,054 | 672 | █████████ |
| Feb 2026 | 3,601 | 68% | 1,983 | 1,018 | █████████████████ |
| Mar 2026 | 2,821 | 70% | 1,780 | 804 | █████████████ |
| Apr 2026 | 4,228 | 72% | 2,913 | 1,017 | ████████████████████ |

The last four complete months averaged 3,128 articles a month against 2,864 in the first four (+9%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 4,492 | 36% |
| India | 569 | 4.5% |
| Canada | 325 | 2.6% |
| United Kingdom | 212 | 1.7% |
| China | 99 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| work visa categories (e.g., h-1b, l-1, tier 2) | 916 | 11% | +4% |
| dual citizenship laws and regulations | 768 | 8.8% | +40% |
| citizenship and naturalization processes | 1,045 | 12% | -1% |
| skilled migration programs and criteria | 171 | 2.0% | -47% |
| family-based immigration sponsorship | 204 | 2.3% | +27% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 7 Apr 2026 | [Guerre au Moyen-Orient: l'Iran prêt à utiliser son peuple comme bouclier humain](http://www.bfmtv.com/international/moyen-orient/iran/video-guerre-au-moyen-orient-l-iran-pret-a-utiliser-son-peuple-comme-bouclier-humain_VN-202604070850.html) | bfmtv.com | 9 | negative |
| 2 Mar 2026 | [A U.S. veteran adopted an orphan from Iran over 50 years ago. ICE is trying to deport her](https://www.nbcnewyork.com/news/national-international/socal-woman-adopted-when-she-was-orphaned-iranian-toddler-now-faces-deportation/6471888/) ⚠ | nbcnewyork.com | 9 | negative |
| 25 Jan 2026 | [MÃ´nica Bergamo: Monitoramento registra 80 mortes de pessoas trans no Brasil no ano passado](https://www1.folha.uol.com.br/colunas/monicabergamo/2026/01/brasil-mantem-lideranca-global-em-assassinatos-de-pessoas-trans.shtml) | folha.uol.com.br | 9 | negative |
| 29 Apr 2026 | [Ahmed Shihab-Eldin, Subjected To ‘Grave Violations’ Of Fundamental Rights, Has Kuwaiti Citizenship Revoked -…](https://blackstarnews.com/ahmed-shihab-eldin-subjected-to-grave-violations-of-fundamental-rights-has-kuwaiti-citizenship-revoked/) | blackstarnews.com | 8 | negative |
| 29 Apr 2026 | [Trump Admin Requiring Enhanced Background Checks For Immigration Benefits \| Opinion - Conservative \| Before…](https://beforeitsnews.com/opinion-conservative/2026/04/trump-admin-requiring-enhanced-background-checks-for-immigration-benefits-3739158.html) ⚠ | beforeitsnews.com | 8 | negative |
| 29 Apr 2026 | [Navy rushes injured fisherman ashore for emergency care](http://island.lk/navy-rushes-injured-fisherman-ashore-for-emergency-care/) | island.lk | 8 | negative |
| 28 Apr 2026 | [Online scams: 231 foreign nationals arrested in immigration crackdown - The Observer](https://observer.ug/news/online-scams-231-foreign-nationals-arrested-in-immigration-crackdown/) | observer.ug | 8 | negative |
| 28 Apr 2026 | [US May Deny Visas Over Your Opinions as New DHS Policy Targets 'Extremist' Views: Critics Say It's Too Broad](https://www.ibtimes.co.uk/trump-immigration-policy-political-speech-scrutiny-1794068) ⚠ | ibtimes.co.uk | 8 | negative |
| 28 Apr 2026 | [Trump's War On Birthright Citizenship: POTUS Argues 'Birth Tourism' Justifies Reinterpretation Of The 14th…](https://www.ibtimes.co.uk/us-supreme-court-trump-birthright-citizenship-1794107) | ibtimes.co.uk | 8 | negative |
| 28 Apr 2026 | [Bahrain strips citizenship from Iran ‘sympathizers’](https://www.yahoo.com/news/articles/bahrain-strips-citizenship-iran-sympathizers-121128618.html) | yahoo.com | 8 | negative |
| 28 Apr 2026 | [“Tendrán que rendir cuentas”: el DOJ identificó a 384 naturalizados para revocarles la ciudadanía de EE.UU.…](http://www.lanacion.com.ar/estados-unidos/tendran-que-rendir-cuentas-el-doj-identifico-a-384-naturalizados-para-revocarles-la-ciudadania-de-nid27042026/) | lanacion.com.ar | 8 | negative |
| 27 Apr 2026 | [Americans back birthright citizenship 2-to-1, poll finds](https://www.yahoo.com/news/articles/americans-back-birthright-citizenship-2-215500867.html) | yahoo.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "citizenship" --since 2026-01-01 --until 2026-04-30
prism-news trends "citizenship" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "citizenship" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "citizenship", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "citizenship", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Medicare News](medicare-news.md)
- [EU AI Act News](eu-ai-act-news.md)
- [Obamacare News](obamacare-news.md)
- [Trade War News](trade-war-news.md)
