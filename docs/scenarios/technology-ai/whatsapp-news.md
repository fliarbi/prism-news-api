# Whatsapp News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “whatsapp news” · 5,400/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [whatsapp-news.json](../../examples/scenarios/whatsapp-news.json).

**Question.** How much whatsapp coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="WhatsApp"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 88,703 |
| Negative · neutral · positive | 47% · 3.0% · 50% |
| Critical (priority 7–9) | 51% (45,412 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (32,570 articles) |
| Most-reported country | United States (13% of matches) |
| Strongest theme by lift | social media platform updates |

## Twelve months of coverage

Monthly matching articles for `WhatsApp` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19,012 | 40% | 8,756 | 9,705 | ████████████ |
| Jun 2025 | 14,734 | 41% | 6,057 | 8,202 | █████████ |
| Jul 2025 | 20,579 | 42% | 9,404 | 10,509 | █████████████ |
| Aug 2025 | 24,979 | 50% | 11,810 | 12,412 | ███████████████ |
| Sep 2025 | 23,028 | 50% | 10,783 | 11,436 | ██████████████ |
| Oct 2025 | 18,310 | 47% | 8,281 | 9,618 | ███████████ |
| Nov 2025 | 16,692 | 52% | 7,966 | 8,305 | ██████████ |
| Dec 2025 | 15,090 | 52% | 6,717 | 7,978 | █████████ |
| Jan 2026 | 15,153 | 49% | 6,666 | 8,122 | █████████ |
| Feb 2026 | 18,602 | 51% | 8,265 | 9,771 | ███████████ |
| Mar 2026 | 22,378 | 53% | 10,908 | 10,665 | ██████████████ |
| Apr 2026 | 32,570 | 51% | 15,693 | 15,779 | ████████████████████ |

The last four complete months averaged 22,176 articles a month against 19,826 in the first four (+12%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 40% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 11,211 | 13% |
| India | 7,118 | 8.0% |
| United Kingdom | 3,950 | 4.5% |
| Malaysia | 1,805 | 2.0% |
| Colombia | 943 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| social media platform updates | 379 | 0.8% | +20% |
| social media app integrations | 368 | 0.8% | +9% |
| mobile app innovations | 355 | 0.7% | +101% |
| mental health and support communities | 523 | 1.1% | +231% |
| cybercrime laws and digital forensics | 1,526 | 3.1% | +21% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [HKL Responds After Netizen Expresses Concern Over Congestion At Specialist Clinic](https://says.com/my/news/hkl-responds-after-netizen-expresses-concern-over-congestion-at-specialist-clinic) | says.com | 9 | negative |
| 30 Apr 2026 | [Everything we know about Golders Green stabbing suspect as he's named](https://inews.co.uk/news/everything-we-know-about-golders-green-stabbing-attack-4389961) | inews.co.uk | 9 | negative |
| 27 Apr 2026 | [Condenado un entrenador en prácticas de un club deportivo de Vigo por enviar una imagen pedófila a un grupo…](https://www.elperiodico.com/es/sucesos/20260428/condenado-entrenador-practicas-club-deportivo-129596374) | elperiodico.com | 9 | negative |
| 26 Apr 2026 | [Trump's latest brush with death will only fuel his anger](https://inews.co.uk/news/world/trump-latest-brush-with-death-will-only-fuel-his-anger-4381110) | inews.co.uk | 9 | negative |
| 24 Apr 2026 | ['It hit me like an AK-47 bullet' - Brother shattered after family of seven killed in KZN](https://www.enca.com/news/it-hit-me-ak-47-bullet-brother-shattered-after-family-seven-killed-kzn) | enca.com | 9 | negative |
| 23 Apr 2026 | [Starmer can't say his Cabinet backs him. Could a 'stalking horse' bring him down?](https://inews.co.uk/news/politics/starmer-cabinet-stalking-horse-down-4375061) | inews.co.uk | 9 | negative |
| 22 Apr 2026 | [Britain is unprepared for missile 'saturation' attack if Putin launches war](https://inews.co.uk/news/world/britain-unprepared-missile-saturation-putin-launches-war-4372205) | inews.co.uk | 9 | negative |
| 21 Apr 2026 | [Thrissur blast leaves at least 13 dead: ‘Felt like an earthquake,’ say residents](https://www.thenewsminute.com/kerala/thrissur-blast-leaves-at-least-13-dead-felt-like-an-earthquake-say-residents) | thenewsminute.com | 9 | negative |
| 21 Apr 2026 | [When the map turns red: Inside the lives upended by Israel’s expulsion orders](http://www.middleeasteye.net/news/when-map-turns-red-inside-lives-upended-israel-expulsion-orders) | middleeasteye.net | 9 | negative |
| 21 Apr 2026 | [Putin is nothing without war. The contrast with his overlord Xi couldn't be starker](https://inews.co.uk/opinion/putin-nothing-without-war-contrast-overlord-xi-starker-4343436) | inews.co.uk | 9 | negative |
| 21 Apr 2026 | [Telangana inter student sexually assaults girl, shares video on WhatsApp group](https://www.siasat.com/telangana-inter-student-sexually-assaults-girl-shares-video-on-whatsapp-group-3457344/) | siasat.com | 9 | negative |
| 20 Apr 2026 | [The vital lesson Britain must learn from Trump’s failure in Iran](https://inews.co.uk/opinion/vital-lesson-britain-learn-trumps-failure-iran-4360977) | inews.co.uk | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "WhatsApp" --since 2026-01-01 --until 2026-04-30
prism-news trends "WhatsApp" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "WhatsApp" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "WhatsApp", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "WhatsApp", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Instagram News](instagram-news.md)
- [Chatgpt News](chatgpt-news.md)
- [Iphone News](iphone-news.md)
- [Data Center News](data-center-news.md)
