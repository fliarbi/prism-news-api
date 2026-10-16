# Chips Act News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “chips act news” · 10/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [chips-act-news.json](../../examples/scenarios/chips-act-news.json).

**Question.** How did coverage of chips act develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="chips act"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 173 |
| Negative · neutral · positive | 24% · 1.7% · 74% |
| Critical (priority 7–9) | 88% (153 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (328 articles) |
| Most-reported country | United States (45% of matches) |
| Strongest theme by lift | semiconductor devices and components |

## Twelve months of coverage

Monthly matching articles for `chips act` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 47 | 81% | 19 | 28 | ███ |
| Jun 2025 | 35 | 91% | 11 | 23 | ██ |
| Jul 2025 | 50 | 74% | 21 | 29 | ███ |
| Aug 2025 | 328 | 95% | 203 | 119 | ████████████████████ |
| Sep 2025 | 66 | 92% | 30 | 35 | ████ |
| Oct 2025 | 50 | 90% | 16 | 34 | ███ |
| Nov 2025 | 44 | 100% | 8 | 36 | ███ |
| Dec 2025 | 48 | 88% | 13 | 34 | ███ |
| Jan 2026 | 39 | 92% | 11 | 28 | ██ |
| Feb 2026 | 80 | 88% | 16 | 63 | █████ |
| Mar 2026 | 21 | 76% | 7 | 14 | █ |
| Apr 2026 | 33 | 94% | 8 | 23 | ██ |

The last four complete months averaged 43 articles a month against 115 in the first four (-62%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 58% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 77 | 45% |
| Belgium | 6 | 3.5% |
| China | 4 | 2.3% |
| Finland | 4 | 2.3% |
| Germany | 2 | 1.2% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| semiconductor devices and components | 18 | 17% | -14% |
| microcontrollers and microprocessor units | 12 | 12% | -25% |
| integrated circuits (ics) and microchips | 11 | 11% | +10% |
| advanced materials science | 9 | 8.7% | new |
| semiconductor industry updates | 14 | 13% | -44% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [US Aims to Break China's Rare Earth Dominance](https://www.newkerala.com/news/a/us-working-break-chinas-rare-earth-chokehold-says-886.htm) | newkerala.com | 8 | negative |
| 13 Apr 2026 | [Intel and Biden Admin announce up to $8.5 billion in direct funding - News](https://www.siliconsemiconductor.net/article/119010/Intel_and_Biden_Admin_announce_up_to_85_billion_in_direct_funding) | siliconsemiconductor.net | 8 | positive |
| 12 Mar 2026 | [Intel 18A: The Make-or-Break Foundry Bet That Could End America's Dependence on TSMC](https://www.abhs.in/blog/intel-18a-foundry-tsmc-rival-us-chip-independence-2026) | abhs.in | 8 | negative |
| 5 Feb 2026 | [SIA Applauds Senate’s Procedural Vote to Advance CHIPS Act, Urges Final Passage · EMSNow](https://www.emsnow.com/sia-applauds-senates-procedural-vote-to-advance-chips-act-urges-final-passage/) | emsnow.com | 8 | positive |
| 5 Feb 2026 | [US to take 10% equity stake in Intel, in Trump's latest corporate move, Reuters reports · EMSNow](https://www.emsnow.com/us-to-take-10-equity-stake-in-intel-in-trumps-latest-corporate-move-reuters-reports/) | emsnow.com | 8 | negative |
| 5 Feb 2026 | [Electronics Industry Leaders Call on Congress to Support $100M in PCB Sector Funding · EMSNow](https://www.emsnow.com/electronics-industry-leaders-call-on-congress-to-support-100m-in-pcb-sector-funding/) | emsnow.com | 8 | positive |
| 2 Feb 2026 | [Intel Panther Lake Core Ultra review: Intel’s best laptop CPU in a very long time](https://arstechnica.com/civis/threads/intel-panther-lake-core-ultra-review-intel%E2%80%99s-best-laptop-cpu-in-a-very-long-time.1511466/post-44226195) | arstechnica.com | 8 | negative |
| 19 Jan 2026 | [The Semiconductor Talent Crisis: Why Global Workforce Solutions Are Now Mission-Critical](https://www.linkedin.com/pulse/semiconductor-talent-crisis-why-global-workforce-solutions-aicher-rrhkc) | linkedin.com | 8 | negative |
| 6 Feb 2026 | [PCBAA Issues Statement On CHIPS Act Funding · EMSNow](https://www.emsnow.com/pcbaa-issues-statement-on-chips-act-funding/) | emsnow.com | 7 | positive |
| 26 Jan 2026 | [USA: US-Regierung investiert 1,6 Milliarden Dollar in Seltene-Erden-Firma](http://www.handelsblatt.com/unternehmen/industrie/usa-us-regierung-investiert-16-milliarden-dollar-in-seltene-erden-firma/100194831.html) | handelsblatt.com | 7 | positive |
| 10 Jan 2026 | [Madurez del sector de dispositiv­os médicos desafía la atracción de IED](https://www.pressreader.com/costa-rica/el-financiero-costa-rica/20260110/281586656981087) | pressreader.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "chips act" --since 2026-01-01 --until 2026-04-30
prism-news trends "chips act" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "chips act" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "chips act", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "chips act", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [NEP News](nep-news.md)
- [Consumer Protection News](consumer-protection-news.md)
- [Content Moderation News](content-moderation-news.md)
- [Rent Control News](rent-control-news.md)
