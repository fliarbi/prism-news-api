# Online Gaming News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “online gaming news” · 5,400/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [online-gaming-news.json](../../examples/scenarios/online-gaming-news.json).

**Question.** How much online gaming coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="online gaming"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 8,849 |
| Negative · neutral · positive | 21% · 1.6% · 78% |
| Critical (priority 7–9) | 23% (2,014 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,800 articles) |
| Most-reported country | United States (15% of matches) |
| Strongest theme by lift | online gambling forums and communities |

## Twelve months of coverage

Monthly matching articles for `online gaming` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1,334 | 19% | 227 | 1,065 | ██████████ |
| Jun 2025 | 1,191 | 19% | 227 | 942 | █████████ |
| Jul 2025 | 1,372 | 24% | 355 | 993 | ██████████ |
| Aug 2025 | 2,664 | 55% | 986 | 1,634 | ███████████████████ |
| Sep 2025 | 1,785 | 33% | 451 | 1,105 | █████████████ |
| Oct 2025 | 1,383 | 30% | 368 | 1,004 | ██████████ |
| Nov 2025 | 1,778 | 24% | 387 | 1,378 | █████████████ |
| Dec 2025 | 1,220 | 22% | 267 | 928 | █████████ |
| Jan 2026 | 1,870 | 20% | 373 | 1,467 | █████████████ |
| Feb 2026 | 2,060 | 26% | 526 | 1,506 | ███████████████ |
| Mar 2026 | 2,119 | 21% | 420 | 1,663 | ███████████████ |
| Apr 2026 | 2,800 | 24% | 504 | 2,243 | ████████████████████ |

The last four complete months averaged 2,212 articles a month against 1,640 in the first four (+35%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 1,352 | 15% |
| India | 503 | 5.7% |
| Australia | 385 | 4.3% |
| United Kingdom | 305 | 3.5% |
| Canada | 120 | 1.4% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| online gambling forums and communities | 632 | 14% | +572% |
| gambling-related software tools (e.g., odds calculators) | 195 | 4.4% | +261% |
| gambling-themed mobile applications | 690 | 16% | +522% |
| social casino gaming platforms and apps | 874 | 20% | +312% |
| gambling-themed entertainment content | 426 | 9.6% | +446% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 9 Apr 2026 | [Man jailed after grooming girl he met on Roblox](https://www.aol.com/articles/man-jailed-grooming-girl-met-135941315.html) | aol.com | 9 | negative |
| 24 Mar 2026 | [Karnataka MBBS Student Dies By Suicide After Losing Money In Online Gaming](https://www.ndtv.com/india-news/bidar-student-suicide-karnataka-mbbs-student-dies-by-suicide-after-losing-money-in-online-gaming-11259501) | ndtv.com | 9 | negative |
| 10 Feb 2026 | [Ghaziabad: Police urge UP govt to ban 5 game apps](https://www.hindustantimes.com/cities/noida-news/ghaziabad-police-urge-up-govt-to-ban-5-game-apps-101770665635605.html) | hindustantimes.com | 9 | negative |
| 5 Feb 2026 | [Homem é investigado por abuso virtual contra ao menos 459 crianças na Austrália e em outros 15 países](https://oglobo.globo.com/mundo/epoca/noticia/2026/02/05/homem-e-investigado-por-crimes-de-abuso-online-contra-ao-menos-459-criancas-na-australia-e-outros-15-paises.ghtml) | oglobo.globo.com | 9 | negative |
| 4 Feb 2026 | [Three sisters aged 12, 14, 16 die after jumping from high-rise in Ghaziabad; Online gaming angle suspected](https://www.india.com/news/india/three-sisters-aged-12-14-16-die-after-jumping-from-high-rise-in-ghaziabad-online-gaming-angle-suspected-8292672/) | india.com | 9 | negative |
| 4 Feb 2026 | [Three minor sisters die by suicide in Ghaziabad; police probing addiction to Korean task game](https://www.newindianexpress.com/nation/2026/Feb/04/three-minor-sisters-die-by-suicide-in-ghaziabad-police-probing-addiction-to-korean-task-game) | newindianexpress.com | 9 | negative |
| 30 Apr 2026 | [New online gaming rules from May 1: Violations will see 3 year jail term, ₹1 crore in fines - BusinessToday](https://www.businesstoday.in/technology/story/new-online-gaming-rules-from-may-1-violations-will-see-3-year-jail-term-rs1-crore-in-fines-528355-2026-04-30) | businesstoday.in | 8 | positive |
| 30 Apr 2026 | [New Online Gaming Rules To Come Into Force From May 1: Here Are The Changes Explained - Outlook Money](https://outlookmoney.com/news/new-online-gaming-rules-to-come-into-force-from-may-1-here-are-the-changes-explained) | outlookmoney.com | 8 | positive |
| 30 Apr 2026 | [Roblox Names Sunil Rao India Managing Director](https://technosports.co.in/roblox-appoints-sunil-rao-as-managing-director/) | technosports.co.in | 8 | positive |
| 30 Apr 2026 | [New Rules From May 1, 2026: From New Banking, PF, and LPG; List of Rule Changes That Will Impact Your Wallet…](https://www.latestly.com/india/information/new-rules-from-may-1-2026-from-new-banking-pf-and-lpg-list-of-rule-changes-that-will-impact-your-wallet-7413044.html) | latestly.com | 8 | positive |
| 28 Apr 2026 | [India's Online Gaming Law Goes Live May 1: What's at Stake for Operators](https://www.india-briefing.com/news/india-online-gaming-regulation-2026-what-operators-must-know-44355.html/) | india-briefing.com | 8 | positive |
| 28 Apr 2026 | [Know your laws: New online gaming rules from May 1 amid compliance challenges](https://www.indiatoday.in/india/law-news/story/know-your-laws-new-online-gaming-rules-from-may-1-amid-compliance-challenges-2902662-2026-04-28) | indiatoday.in | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "online gaming" --since 2026-01-01 --until 2026-04-30
prism-news trends "online gaming" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "online gaming" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "online gaming", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "online gaming", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Data Center News](data-center-news.md)
- [ISRO News](isro-news.md)
- [Social Media News](social-media-news.md)
- [Quantum Computing News](quantum-computing-news.md)
