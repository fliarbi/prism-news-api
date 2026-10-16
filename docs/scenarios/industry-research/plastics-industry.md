# Plastics Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “plastics industry” · 2,400/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [plastics-industry.json](../../examples/scenarios/plastics-industry.json).

**Question.** How much news did the plastics industry receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="plastics industry"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,000 |
| Negative · neutral · positive | 1.0% · 0.0% · 99% |
| Critical (priority 7–9) | 2.3% (93 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (2,704 articles) |
| Most-reported country | United States (1.1% of matches) |
| Strongest theme by lift | plastics industry trade shows & conferences |

## Twelve months of coverage

Monthly matching articles for `plastics industry` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 30 | 43% | 2 | 27 | █ |
| Jun 2025 | 25 | 48% | 3 | 18 | █ |
| Jul 2025 | 19 | 63% | 4 | 13 | █ |
| Aug 2025 | 20 | 60% | 7 | 13 | █ |
| Sep 2025 | 51 | 35% | 2 | 47 | █ |
| Oct 2025 | 61 | 51% | 16 | 45 | █ |
| Nov 2025 | 40 | 60% | 4 | 36 | █ |
| Dec 2025 | 23 | 44% | 8 | 14 | █ |
| Jan 2026 | 1,195 | 1.7% | 5 | 1,190 | █████████ |
| Feb 2026 | 2,704 | 1.0% | 6 | 2,698 | ████████████████████ |
| Mar 2026 | 33 | 54% | 12 | 21 | █ |
| Apr 2026 | 68 | 41% | 16 | 52 | █ |

The last four complete months averaged 1,000 articles a month against 24 in the first four (+4155%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 2.0% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 45 | 1.1% |
| India | 15 | 0.4% |
| China | 6 | 0.1% |
| Spain | 4 | 0.1% |
| Mexico | 3 | 0.1% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| plastics industry trade shows & conferences | 3,001 | 96% | +21336% |
| plastics supply chain & logistics management | 2,997 | 96% | +33200% |
| plastics resin suppliers & distribution networks | 2,994 | 96% | +49800% |
| circular economy principles | 21 | 0.7% | -19% |
| recycling and waste reduction initiatives | 12 | 0.4% | +100% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 12 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Bundeshaushalt 2027 - Kunststoffindustrie kämpft gegen geplante Plastikabgabe - Lebensmittelpraxis.de](https://lebensmittelpraxis.de/industrie-aktuell/48515-bundeshaushalt-2027-kunststoffindustrie-kaempft-gegen-geplante-plastikabgabe.html) | lebensmittelpraxis.de | 7 | negative |
| 6 Apr 2026 | [Supreme Industries flags global supply disruptions despite duty relief - CNBC TV18](https://www.cnbctv18.com/business/companies/supreme-industries-global-supply-disruptions-duty-relief-mp-taparia-19880995.htm) | cnbctv18.com | 7 | positive |
| 17 Mar 2026 | [कच्चा माल महंगे होने से उत्पाद में कमी, मजदूरों को भी फिलहाल रोका](https://www.livehindustan.com/uttar-pradesh/chandauli/story-plastic-industry-crisis-raw-material-prices-soar-production-and-sales-plummet-201773771709195.html) | livehindustan.com | 7 | negative |
| 6 Feb 2026 | [NEW DELHI — February 5, 2026 — Milliken & Company is showcasing a full portfolio of advanced polymer…](https://textileworldasia.com/textile-world-asia/2026/02/milliken-highlights-next-generation-polymer-solutions-at-plastindia-2026/) | textileworldasia.com | 7 | positive |
| 3 Feb 2026 | [Monistrol-sur-Loire. Accidents du travail : au tribunal, une condamnation et une relaxe pour le groupe Barbier](http://www.leprogres.fr/economie/2026/02/03/accidents-du-travail-une-condamnation-et-une-relaxe-pour-l-entreprise-barbier) | leprogres.fr | 7 | negative |
| 27 Jan 2026 | [India’s plastics industry is projected to reach $44.5 billion by 2030 at a CAGR of 11 per cent, with exports…](https://investmentguruindia.com/newsdetail/india-s-plastics-exports-projected-to-double-to-20-billion-by-2030681230) | investmentguruindia.com | 7 | positive |
| 26 Jan 2026 | [Aimplas project recycles nylon fishing nets](https://www.recyclingtoday.com/news/aimplas-project-transforms-recycled-nylon-fishing-nets-into-industrial-applications/) | recyclingtoday.com | 7 | positive |
| 17 Jan 2026 | [With a nudge from industry, Congress takes aim at California recycling laws](https://www.latimes.com/environment/story/2026-01-17/with-nudge-from-industry-congress-considers-shutting-down-california-recycling-laws) | latimes.com | 7 | negative |
| 11 Apr 2026 | [Bangladesh’s next industrial frontier: Textiles, plastics or e-waste](https://www.tbsnews.net/economy/corporates/bangladeshs-next-industrial-frontier-textiles-plastics-or-e-waste-1408966) | tbsnews.net | 6 | positive |
| 6 Apr 2026 | [Hacia una industria del plástico más circular y competitiva](https://www.expansion.com/economia/2026/04/07/69d41388468aeb33458b4582.html) | expansion.com | 6 | negative |
| 31 Mar 2026 | [Surat Plast Show 2026 to showcase recycling and sustainability with advanced technologies - Up18 News](https://up18news.com/surat-plast-show-2026-to-showcase-recycling-and-sustainability-with-advanced-technologies/) | up18news.com | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "plastics industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "plastics industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "plastics industry" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "plastics industry", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "plastics industry", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Gaming Industry](gaming-industry.md)
- [Healthcare Industry](healthcare-industry.md)
- [Aviation Industry](aviation-industry.md)
- [Telecom Industry](telecom-industry.md)
