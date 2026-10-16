# HIV News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hiv news” · 4,400/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [hiv-news.json](../../examples/scenarios/hiv-news.json).

**Question.** How much hiv coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="HIV"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 14,493 |
| Negative · neutral · positive | 28% · 3.9% · 68% |
| Critical (priority 7–9) | 56% (8,113 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,338 articles) |
| Most-reported country | India (29% of matches) |
| Strongest theme by lift | public health initiatives and programs |

## Twelve months of coverage

Monthly matching articles for `HIV` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2,453 | 59% | 842 | 1,527 | ███████████ |
| Jun 2025 | 2,301 | 55% | 613 | 1,599 | ███████████ |
| Jul 2025 | 3,132 | 56% | 1,124 | 1,891 | ██████████████ |
| Aug 2025 | 3,257 | 60% | 1,098 | 2,026 | ███████████████ |
| Sep 2025 | 3,011 | 61% | 999 | 1,909 | ██████████████ |
| Oct 2025 | 3,142 | 59% | 897 | 2,140 | ██████████████ |
| Nov 2025 | 2,791 | 60% | 763 | 1,925 | █████████████ |
| Dec 2025 | 3,309 | 64% | 955 | 2,203 | ███████████████ |
| Jan 2026 | 2,958 | 62% | 777 | 2,051 | ██████████████ |
| Feb 2026 | 3,759 | 56% | 1,163 | 2,506 | █████████████████ |
| Mar 2026 | 3,438 | 55% | 943 | 2,334 | ████████████████ |
| Apr 2026 | 4,338 | 53% | 1,237 | 2,875 | ████████████████████ |

The last four complete months averaged 3,623 articles a month against 2,786 in the first four (+30%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 61% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 4,164 | 29% |
| United States | 1,787 | 12% |
| Italy | 659 | 4.5% |
| Canada | 318 | 2.2% |
| Japan | 239 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| public health initiatives and programs | 538 | 6.5% | -2% |
| global health research collaborations | 285 | 3.4% | -3% |
| infectious disease research and prevention | 403 | 4.8% | +16% |
| epidemiology and disease control studies | 714 | 8.6% | +1% |
| community health outreach programs | 241 | 2.9% | -4% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 9 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [Uk Man Sentenced For Infecting With Hiv: UK man jailed for life after deliberately infecting seven victims…](https://timesofindia.indiatimes.com/world/uk/uk-man-jailed-for-life-after-deliberately-infecting-seven-victims-with-hiv-over-years/articleshow/130492723.cms) | timesofindia.indiatimes.com | 9 | negative |
| 23 Apr 2026 | [Washington rapist jailed for deliberate HIV infections](https://www.namibian.com.na/washington-rapist-jailed-for-deliberate-hiv-infections/) | namibian.com.na | 9 | negative |
| 23 Apr 2026 | [‘Monster’ who deliberately spread HIV jailed for life as checks urged for possible Yorkshire-based victims](https://www.yorkshirepost.co.uk/news/crime/monster-who-deliberately-spread-hiv-jailed-for-life-as-checks-urged-for-possible-yorkshire-based-victims-7297918) | yorkshirepost.co.uk | 9 | negative |
| 23 Apr 2026 | [HIV predator's youngest victim got doctor's call after getting off school bus](https://www.mirror.co.uk/news/uk-news/adam-hall-victim-school-bus-37057489) | mirror.co.uk | 9 | negative |
| 16 Apr 2026 | [Con jeringas reutilizadas y medicamentos reciclados: asÃ­ operaba el hospital que infectÃ³ de VIH a mÃ¡s de…](https://heraldodemexico.com.mx/mundo/2026/4/16/con-jeringas-reutilizadas-medicamentos-reciclados-asi-operaba-el-hospital-que-infecto-de-vih-mas-de-300-ninos-797152.html) | heraldodemexico.com.mx | 9 | negative |
| 14 Apr 2026 | [Syringe reuse at Pakistan hospital infects 331 children with HIV, probe reveals](https://gulfnews.com/world/asia/pakistan/syringe-reuse-at-pakistan-hospital-infects-331-children-with-hiv-probe-reveals-1.500506424) | gulfnews.com | 9 | negative |
| 11 Apr 2026 | [पूर्व मंगेतर ने जबरदस्ती लगाया HIV का इंजेक्शन, परेशान युवती ने दी जान](https://www.patrika.com/national-news/crime-news-woman-dies-by-sucide-after-ex-fiance-injected-her-with-hiv-injection-in-hyderabad-20491691) | patrika.com | 9 | negative |
| 11 Apr 2026 | [Hyderabad Shocker: Woman Ends Life Days After Being Forcibly Injected With HIV-Positive Blood](https://www.republicworld.com/india/hyderabad-hiv-injection-case-woman-suicide-trauma) | republicworld.com | 9 | negative |
| 11 Apr 2026 | [Hyderabad HIV Injection Suicide 2026: Trauma Leads to Tragic Death - Business League](https://www.businessleague.in/hyderabad-hiv-injection-suicide-2026-trauma-leads-to-tragic-death/) | businessleague.in | 9 | negative |
| 21 Mar 2026 | [Pensacola Police Officer Charged for Hiding He was HIV-Positive from Woman He Got Pregnant](https://www.ibtimes.sg/pensacola-police-officer-charged-hiding-he-was-hiv-positive-woman-he-got-pregnant-84588) | ibtimes.sg | 9 | negative |
| 14 Mar 2026 | [शादी टूटने से भड़का शख्स, युवती को लगा दिया HIV संक्रमित खून का इंजेक्शन](https://www.livehindustan.com/national/telangana-man-gave-hiv-infected-blood-to-girl-after-marriage-was-canceled-arrested-201773504865546.html) | livehindustan.com | 9 | negative |
| 6 Mar 2026 | [Sexual predator convicted of multiple counts of rape and intentional transmission of HIV](https://www.warrington-worldwide.co.uk/2026/03/06/sexual-predator-convicted-of-multiple-counts-of-rape-and-intentional-transmission-of-hiv/) | warrington-worldwide.co.uk | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "HIV" --since 2026-01-01 --until 2026-04-30
prism-news trends "HIV" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "HIV" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "HIV", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "HIV", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [COVID News](covid-news.md)
- [Bird Flu News](bird-flu-news.md)
- [E Coli Outbreak](e-coli-outbreak.md)
- [Salmonella Outbreak](salmonella-outbreak.md)
