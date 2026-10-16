# Sanctions News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sanctions news” · 50/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [sanctions-news.json](../../examples/scenarios/sanctions-news.json).

**Question.** How did coverage of sanctions develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="sanctions"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 32,207 |
| Negative · neutral · positive | 84% · 4.5% · 12% |
| Critical (priority 7–9) | 89% (28,773 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (9,683 articles) |
| Most-reported country | United States (24% of matches) |
| Strongest theme by lift | international certifications for oil & gas |

## Twelve months of coverage

Monthly matching articles for `sanctions` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7,536 | 85% | 6,313 | 828 | ████████████████ |
| Jun 2025 | 4,078 | 84% | 3,412 | 493 | ████████ |
| Jul 2025 | 7,365 | 82% | 6,354 | 661 | ███████████████ |
| Aug 2025 | 7,279 | 87% | 6,378 | 604 | ███████████████ |
| Sep 2025 | 8,024 | 90% | 6,976 | 763 | █████████████████ |
| Oct 2025 | 6,396 | 89% | 5,304 | 795 | █████████████ |
| Nov 2025 | 4,566 | 89% | 3,723 | 646 | █████████ |
| Dec 2025 | 5,244 | 90% | 4,327 | 718 | ███████████ |
| Jan 2026 | 5,947 | 90% | 5,067 | 678 | ████████████ |
| Feb 2026 | 8,161 | 88% | 6,591 | 1,077 | █████████████████ |
| Mar 2026 | 8,416 | 89% | 7,222 | 856 | █████████████████ |
| Apr 2026 | 9,683 | 90% | 8,073 | 1,181 | ████████████████████ |

The last four complete months averaged 8,052 articles a month against 6,564 in the first four (+23%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 44% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 7,766 | 24% |
| Russia | 1,098 | 3.4% |
| Iran | 778 | 2.4% |
| India | 562 | 1.7% |
| China | 530 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| international certifications for oil & gas | 686 | 3.0% | +159% |
| economic impact of oil exports | 1,676 | 7.3% | +48% |
| geopolitical factors in oil supply | 2,820 | 12% | +44% |
| oil tanker transportation logistics | 1,855 | 8.1% | +149% |
| environmental policy and climate governance | 429 | 1.9% | +200% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 26 Apr 2026 | [Ukraine-Krieg aktuell: Russland greift mit hunderten Drohnen an – Selenskyj appelliert an Partner](https://www.fr.de/politik/ins-visier-ukraine-krieg-aktuell-putins-verluste-steigen-weiter-eu-nimmt-russlands-wirtschaft-zr-94276764.html) | fr.de | 9 | negative |
| 25 Apr 2026 | [Ukraine: des frappes à Dnipro font au moins cinq morts, Volodymyr Zelensky demande plus de sanctions](https://www.bfmtv.com/international/europe/ukraine/ukraine-des-frappes-a-dnipro-font-au-moins-cinq-morts-volodymyr-zelensky-demande-plus-de-sanctions_AD-202604250228.html) | bfmtv.com | 9 | negative |
| 25 Apr 2026 | [Prime minister: EU should tax Russian goods to pay for Ukraine reconstruction](https://news.err.ee/1610006431/prime-minister-eu-should-tax-russian-goods-to-pay-for-ukraine-reconstruction) | news.err.ee | 9 | negative |
| 22 Apr 2026 | [Trump Extends Iran Ceasefire Indefinitely, Delays Talks As US Maintains Blockade \| Outlook India](https://www.outlookindia.com/international/trump-extends-iran-ceasefire-indefinitely-delays-talks-as-us-maintains-blockade) | outlookindia.com | 9 | negative |
| 19 Apr 2026 | [Zelensky slams oil sanctions relief for Russia](https://www.bangkokpost.com/world/3239798/zelensky-slams-oil-sanctions-relief-for-russia) | bangkokpost.com | 9 | negative |
| 11 Apr 2026 | [Iran set for peace talks but doubts emerge over Lebanon, sanctions](https://www.radionz.co.nz/news/world/592100/iran-set-for-peace-talks-but-doubts-emerge-over-lebanon-sanctions) | radionz.co.nz | 9 | negative |
| 10 Apr 2026 | [Ukraine, Zelensky calls for reinstatement of oil sanctions against Russia](https://en.ilsole24ore.com/art/ukraine-zelensky-calls-for-reinstatement-of-oil-sanctions-against-russia-AIPdrbQC) | en.ilsole24ore.com | 9 | negative |
| 9 Apr 2026 | [Carney says Canada not considering sanctioning Israel over Lebanon strikes](https://www.castanetkamloops.net/edition/news-story-607902-4-.htm) | castanetkamloops.net | 9 | negative |
| 9 Apr 2026 | [Iran-U.S Ceasefire: It Is Alive, But Very Shaky; Will It Hold?](https://www.oneindia.com/international/iran-u-s-ceasefire-it-is-alive-but-very-shaky-will-it-hold-8052455.html) | oneindia.com | 9 | negative |
| 9 Apr 2026 | [Why Iran thinks it won the war despite huge military losses \| Mint](https://www.livemint.com/global/why-iran-thinks-it-won-the-war-despite-huge-military-losses-11775704982317.html) | livemint.com | 9 | negative |
| 8 Apr 2026 | [„Totaler Sieg“ im Iran-Krieg - doch diese Punkte im Friedensplan werden zum Problem für Trump](https://www.gmuender-tagespost.de/welt/politik/nahost-krieg-wird-trump-den-10-punkte-plan-des-iran-akzeptieren-zr-94253725.html) | gmuender-tagespost.de | 9 | negative |
| 8 Apr 2026 | [Reports: Iran's 10-Point Peace Plan Demands Full End to Sanctions](https://www.breitbart.com/middle-east/2026/04/08/reports-irans-10-point-peace-plan-demands-full-end-sanctions-control-strait-hormuz-reparations/) | breitbart.com | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "sanctions" --since 2026-01-01 --until 2026-04-30
prism-news trends "sanctions" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "sanctions" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "sanctions", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "sanctions", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Climate Policy News](climate-policy-news.md)
- [Make in India News](make-in-india-news.md)
- [Banking Regulation News](banking-regulation-news.md)
- [Windfall Tax News](windfall-tax-news.md)
