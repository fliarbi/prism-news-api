# Labour Law News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “labour law news” · 390/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [labour-law-news.json](../../examples/scenarios/labour-law-news.json).

**Question.** How did coverage of labour law develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="labour law"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 648 |
| Negative · neutral · positive | 33% · 18% · 49% |
| Critical (priority 7–9) | 39% (253 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (229 articles) |
| Most-reported country | India (7.6% of matches) |
| Strongest theme by lift | labor union negotiations and relations |

## Twelve months of coverage

Monthly matching articles for `labour law` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 85 | 34% | 20 | 52 | ███████ |
| Jun 2025 | 65 | 32% | 18 | 34 | ██████ |
| Jul 2025 | 90 | 40% | 34 | 43 | ████████ |
| Aug 2025 | 76 | 53% | 41 | 25 | ███████ |
| Sep 2025 | 104 | 40% | 28 | 55 | █████████ |
| Oct 2025 | 66 | 39% | 24 | 32 | ██████ |
| Nov 2025 | 91 | 43% | 16 | 56 | ████████ |
| Dec 2025 | 94 | 44% | 28 | 44 | ████████ |
| Jan 2026 | 128 | 48% | 35 | 71 | ███████████ |
| Feb 2026 | 124 | 43% | 47 | 64 | ███████████ |
| Mar 2026 | 167 | 38% | 64 | 84 | ███████████████ |
| Apr 2026 | 229 | 32% | 67 | 96 | ████████████████████ |

The last four complete months averaged 162 articles a month against 79 in the first four (+105%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 20% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 49 | 7.6% |
| United Arab Emirates | 27 | 4.2% |
| United States | 14 | 2.2% |
| South Africa | 7 | 1.1% |
| Canada | 4 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| labor union negotiations and relations | 20 | 6.4% | +150% |
| compensation and benefits structures | 17 | 5.4% | +89% |
| hr compliance and labor laws | 28 | 8.9% | +75% |
| payroll management systems | 13 | 4.1% | +86% |
| corporate legal counsel services | 13 | 4.1% | +225% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 25 Apr 2026 | [Inimigo Público: Trump prolonga cessar-fogo até o Irão apresentar a sua proposta de Lei Laboral](http://expresso.pt/inimigo-publico/2026-04-25-inimigo-publico-trump-prolonga-cessar-fogo-ate-o-irao-apresentar-a-sua-proposta-de-lei-laboral-23ea52fa) | expresso.pt | 8 | positive |
| 30 Mar 2026 | [US-Israel-Iran conflict: Airlines face fare dilemma as fuel spike threatens travel demand](https://gulfbusiness.com/en/2026/aviation/us-israel-iran-conflict-airlines-face-fare-dilemma-as-fuel-spike-threatens-travel-demand/) | gulfbusiness.com | 8 | negative |
| 13 Feb 2026 | [UAE Payroll & HR Compliance 2026: Why Dubai’s Growing Businesses Are Rebuilding Workforce Governance with Zoho](https://www.linkedin.com/pulse/uae-payroll-hr-compliance-2026-why-dubais-growing-businesses-y7kyc) | linkedin.com | 8 | positive |
| 14 Apr 2026 | [Reforma laboral em Portugal: entre o bloqueio político e a urgência de adaptação \| Por António Pedro Gonçalves](https://postal.pt/opiniao/reforma-laboral-em-portugal-entre-o-bloqueio-politico-e-a-urgencia-de-adaptacao/) | postal.pt | 7 | negative |
| 5 Apr 2026 | [छुट्टी नहीं ली? अब मिलेगा पैसा, नए लेबर कोड का बड़ा फायदा, जान लीजिए वरना पछताएंगे](https://www.livehindustan.com/business/now-you-are-eligible-for-earned-leave-under-new-labour-code-2025-check-details-201775392975259.html) | livehindustan.com | 7 | neutral |
| 31 Mar 2026 | [New Labour Code: PF बढ़ेगा, इन हैंड सैलरी घटेगी, 1 साल में ग्रेच्युटी... अप्रैल से कंपनियां धड़ाधड़ लागू…](https://www.aajtak.in/business/utility/story/india-new-labour-codes-from-1st-april-workforce-salary-gratuity-rule-change-tutc-dskc-2511762-2026-03-31) | aajtak.in | 7 | positive |
| 27 Mar 2026 | [A la défense des ruptures conventionnelles](http://www.lesechos.fr/idees-debats/editos-analyses/a-la-defense-des-ruptures-conventionnelles-2223472) | lesechos.fr | 7 | negative |
| 11 Mar 2026 | [Governo reúne-se com empresários a UGT na segunda-feira para discutir lei do trabalho](https://eco.sapo.pt/2026/03/11/governo-reune-se-na-proxima-semana-com-parceiros-sociais-para-negociar-lei-do-trabalho/) | eco.sapo.pt | 7 | positive |
| 8 Mar 2026 | [Qui paie le salaire si vous Ãªtes bloquÃ© Ã lâÃ©tranger?](https://www.tdg.ch/golfe-qui-paie-le-salaire-si-le-retour-est-impossible-733163100028) | tdg.ch | 7 | negative |
| 12 Feb 2026 | [ईस्ट सेंट्रल रेलवे कर्मचारी यूनियन ने जंक्शन पर किया प्रदर्शन](https://www.livehindustan.com/bihar/muzaffarpur/story-east-central-railway-employees-protest-against-new-labor-codes-in-muzaffarpur-201770901752367.html) | livehindustan.com | 7 | negative |
| 12 Feb 2026 | [मजदूर यूनियन ने किया प्रदर्शन सौंपा ज्ञापन](https://www.livehindustan.com/uttar-pradesh/banda/story-construction-workers-union-protests-against-anti-labor-laws-201770919821586.html) | livehindustan.com | 7 | negative |
| 2 Feb 2026 | [Legal Round-up 2nd February, 2026 Edition \| Kommunicate Volume 06 Issue 02](https://www.linkedin.com/pulse/legal-round-up-2nd-february-2026-edition-kommunicate-zc1uf) | linkedin.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "labour law" --since 2026-01-01 --until 2026-04-30
prism-news trends "labour law" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "labour law" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "labour law", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "labour law", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Student Visa News](student-visa-news.md)
- [WTO News](wto-news.md)
- [National Security News](national-security-news.md)
- [Climate Policy News](climate-policy-news.md)
