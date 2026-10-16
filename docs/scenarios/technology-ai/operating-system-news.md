# Operating System News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “operating system news” · 70/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [operating-system-news.json](../../examples/scenarios/operating-system-news.json).

**Question.** How much operating system coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="operating system"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 5,289 |
| Negative · neutral · positive | 15% · 2.4% · 83% |
| Critical (priority 7–9) | 37% (1,931 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,766 articles) |
| Most-reported country | United States (11% of matches) |
| Strongest theme by lift | software development and updates |

## Twelve months of coverage

Monthly matching articles for `operating system` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 799 | 25% | 151 | 609 | █████████ |
| Jun 2025 | 933 | 22% | 115 | 766 | ███████████ |
| Jul 2025 | 1,041 | 20% | 180 | 817 | ████████████ |
| Aug 2025 | 1,674 | 22% | 378 | 1,239 | ███████████████████ |
| Sep 2025 | 1,130 | 29% | 232 | 851 | █████████████ |
| Oct 2025 | 1,135 | 25% | 164 | 945 | █████████████ |
| Nov 2025 | 966 | 32% | 146 | 792 | ███████████ |
| Dec 2025 | 795 | 32% | 129 | 642 | █████████ |
| Jan 2026 | 973 | 38% | 146 | 800 | ███████████ |
| Feb 2026 | 1,193 | 34% | 162 | 998 | ██████████████ |
| Mar 2026 | 1,357 | 41% | 195 | 1,129 | ███████████████ |
| Apr 2026 | 1,766 | 33% | 284 | 1,445 | ████████████████████ |

The last four complete months averaged 1,322 articles a month against 1,112 in the first four (+19%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 24% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 605 | 11% |
| India | 94 | 1.8% |
| United Kingdom | 74 | 1.4% |
| South Korea | 67 | 1.3% |
| China | 38 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| software development and updates | 291 | 8.7% | -26% |
| linux distributions | 263 | 7.9% | +38% |
| open-source operating systems | 228 | 6.8% | +26% |
| mobile phone operating systems | 213 | 6.4% | +52% |
| desktop operating systems | 411 | 12% | -15% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Android users eligible for payout as part of $135M settlement](https://abc11.com/post/android-users-eligible-payout-part-135-million-settlement/18891777/) | abc11.com | 9 | negative |
| 30 Apr 2026 | [Ubuntu AI Integration: Canonical Clarifies Opt-In Features And User Privacy](https://www.ubergizmo.com/2026/04/ubuntu-ai-integration-canonical/) | ubergizmo.com | 8 | positive |
| 17 Apr 2026 | [Firstsource Unveils Kairos to Bridge AI-to-Execution Gap \| Analytics India Magazine](https://analyticsindiamag.com/ai-news/firstsource-unveils-kairos-to-bridge-ai-to-execution-gap) | analyticsindiamag.com | 8 | positive |
| 16 Apr 2026 | [US Bill Mandates On-Device Age Verification](https://reclaimthenet.org/us-bill-mandates-on-device-age-verification) | reclaimthenet.org | 8 | negative |
| 16 Apr 2026 | [Firstsource launches Kairos - the operating system](https://www.edinburghnews.scotsman.com/must-read/firstsource-launches-kairos-the-operating-system-powering-intelligence-that-operates-6578231) | edinburghnews.scotsman.com | 8 | positive |
| 16 Apr 2026 | [Firstsource Launches Kairos -- The Operating System Powering Intelligence That Operates](http://www.prnewswire.com/apac/news-releases/firstsource-launches-kairos--the-operating-system-powering-intelligence-that-operates-302744954.html) | prnewswire.com | 8 | positive |
| 16 Apr 2026 | [Firstsource Launches Kairos - The Operating System Powering Intelligence That Operates - TNGlobal](https://technode.global/prnasia/firstsource-launches-kairos-the-operating-system-powering-intelligence-that-operates/) | technode.global | 8 | positive |
| 16 Apr 2026 | [Firstsource Launches Kairos — The Operating System Powering Intelligence That Operates - Business Upturn](https://www.businessupturn.com/brand-post/firstsource-launches-kairos-the-operating-system-powering-intelligence-that-operates/) | businessupturn.com | 8 | positive |
| 16 Apr 2026 | [Firstsource Launches Kairos -- The Operating System Powering Intelligence That Operates \| India Shorts](https://indiashorts.com/firstsource-launches-kairos-the-operating-system-powering-intelligence-that-operates/284305/) | indiashorts.com | 8 | positive |
| 11 Apr 2026 | [Une nouvelle faille de sécurité sur l’iPhone permet le piratage à distance et nécessite une mise à jour…](https://www.mixvale.com.br/2026/04/11/une-nouvelle-faille-de-securite-sur-liphone-permet-le-piratage-a-distance-et-necessite-une-mise-a-jour-immediate-du-systeme-fr/) | mixvale.com.br | 8 | negative |
| 10 Apr 2026 | [Alerte urgente aux utilisateurs d’iPhone en raison d’une faille qui permet un contrôle total à distance de…](https://www.mixvale.com.br/2026/04/10/alerte-urgente-aux-utilisateurs-diphone-en-raison-dune-faille-qui-permet-un-controle-total-a-distance-de-lappareil-fr/) | mixvale.com.br | 8 | negative |
| 10 Apr 2026 | [Urgent alert to iPhone users due to flaw that allows full remote control of the device](https://www.mixvale.com.br/2026/04/10/urgent-alert-to-iphone-users-due-to-flaw-that-allows-full-remote-control-of-the-device-en/) | mixvale.com.br | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "operating system" --since 2026-01-01 --until 2026-04-30
prism-news trends "operating system" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "operating system" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "operating system", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "operating system", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI in Education News](ai-in-education-news.md)
- [Laptop News](laptop-news.md)
- [SAAS News](saas-news.md)
- [Cloud Security News](cloud-security-news.md)
