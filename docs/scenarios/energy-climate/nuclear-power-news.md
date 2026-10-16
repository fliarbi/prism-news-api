# Nuclear Power News: volume, tone and critical headlines (Jan–Apr 2026)

[Energy and climate research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nuclear power news” · 480/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [nuclear-power-news.json](../../examples/scenarios/nuclear-power-news.json).

**Question.** How did nuclear power coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?

**Request.** `q="nuclear power"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,587 |
| Negative · neutral · positive | 53% · 3.1% · 44% |
| Critical (priority 7–9) | 82% (3,746 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,546 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | nuclear plant meltdowns and radiation leaks |

## Twelve months of coverage

Monthly matching articles for `nuclear power` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 960 | 75% | 460 | 453 | ████████████ |
| Jun 2025 | 1,054 | 79% | 493 | 532 | ██████████████ |
| Jul 2025 | 772 | 71% | 339 | 406 | ██████████ |
| Aug 2025 | 1,191 | 80% | 604 | 570 | ███████████████ |
| Sep 2025 | 930 | 77% | 297 | 617 | ████████████ |
| Oct 2025 | 906 | 81% | 344 | 537 | ████████████ |
| Nov 2025 | 821 | 75% | 323 | 455 | ███████████ |
| Dec 2025 | 913 | 78% | 394 | 502 | ████████████ |
| Jan 2026 | 803 | 82% | 317 | 468 | ██████████ |
| Feb 2026 | 894 | 79% | 407 | 455 | ████████████ |
| Mar 2026 | 1,344 | 84% | 827 | 480 | █████████████████ |
| Apr 2026 | 1,546 | 81% | 858 | 627 | ████████████████████ |

The last four complete months averaged 1,147 articles a month against 994 in the first four (+15%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 972 | 21% |
| India | 229 | 5.0% |
| Iran | 155 | 3.4% |
| Japan | 149 | 3.2% |
| Russia | 123 | 2.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| nuclear plant meltdowns and radiation leaks | 402 | 13% | +244% |
| critical infrastructure vulnerability assessments | 357 | 12% | +247% |
| dam breach emergency planning | 277 | 8.9% | +347% |
| cybersecurity breaches impacting critical infrastructure | 377 | 12% | +259% |
| space launch failures and satellite collision incidents | 335 | 11% | +319% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 26 Apr 2026 | [Wie ein Sicherheitstest zur Katastrophe von Tschernobyl führte](https://www.derstandard.at/story/3000000317834/wie-ein-sicherheitstest-zur-katastrophe-von-tschernobyl-fuehrte) | derstandard.at | 9 | negative |
| 9 Apr 2026 | [Manpreet Sethi : Read All The Stories Published by Manpreet Sethi](https://indianexpress.com/profile/guest-writer/manpreet-sethi/) | indianexpress.com | 9 | negative |
| 8 Apr 2026 | [Global energy system will be ‘profoundly transformed’ by Iran war, watchdog says](https://www.inkl.com/news/global-energy-system-will-be-profoundly-transformed-by-iran-war-watchdog-says) | inkl.com | 9 | negative |
| 8 Apr 2026 | [Nucléaire iranien: une tension persistante au cœur de la guerre au Moyen-Orient](http://www.bfmtv.com/international/moyen-orient/iran/video-nucleaire-iranien-une-tension-persistante-au-c-ur-de-la-guerre-au-moyen-orient_VN-202604080103.html) | bfmtv.com | 9 | negative |
| 27 Mar 2026 | [Iran War: ईरान का दावा- परमाणु ठिकानों को बनाया गया निशाना; इस्राइल बोला- सैन्य कार्रवाई को और तेज करेंगे](https://www.amarujala.com/world/iran-media-claims-nuclear-facilities-have-been-targeted-after-israel-says-attacks-will-escalate-and-expand-2026-03-27) | amarujala.com | 9 | negative |
| 25 Mar 2026 | [Missile Strikes Iran’s Bushehr Nuclear Plant Again as IAEA Urges Restraint - APN News \| Authentic Press…](https://www.apnnews.com/missile-strikes-irans-bushehr-nuclear-plant-again-as-iaea-urges-restraint/) | apnnews.com | 9 | negative |
| 24 Mar 2026 | [Guerre au Moyen-Orient: Les 15 conditions de Donald Trump pour mettre la fin à la guerre](https://www.bfmtv.com/international/moyen-orient/iran/video-guerre-au-moyen-orient-les-15-conditions-de-donald-trump-pour-mettre-la-fin-a-la-guerre_VN-202603240956.html) | bfmtv.com | 9 | neutral |
| 24 Mar 2026 | [Kim Jong Un calls Pyongyang's nuclear status irreversible, warns against 'most hostile' South Korea - The…](https://timesofindia.indiatimes.com/world/rest-of-world/kim-jong-un-calls-pyongyangs-nuclear-status-irreversible-warns-against-most-hostile-south-korea/articleshow/129765713.cms) | timesofindia.indiatimes.com | 9 | negative |
| 22 Mar 2026 | [Irán le responde a Trump sobre el estrecho de Ormuz y nueva oleada de ataques al centro de Israel](https://www.eltiempo.com/mundo/iran-le-responde-a-trump-sobre-el-estrecho-de-ormuz-y-nueva-oleada-de-ataques-al-centro-de-israel-3542142) | eltiempo.com | 9 | negative |
| 18 Mar 2026 | [The 5 States Where The Most People Rely On Nuclear Power](https://www.yahoo.com/news/articles/5-states-where-most-people-131000151.html) | yahoo.com | 9 | negative |
| 27 Feb 2026 | [Russia says local truce established to enable repairs at Zaporizhzhia nuclear plant](http://www.straitstimes.com/world/europe/russia-says-local-truce-established-to-enable-repairs-at-zaporizhzhia-nuclear-plant) | straitstimes.com | 9 | negative |
| 18 Feb 2026 | [60% uranium enrichment: What we know about Iran’s nuclear programme](https://theprint.in/world/60-uranium-enrichment-what-we-know-about-irans-nuclear-programme/2857665/) | theprint.in | 9 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "nuclear power" --since 2026-01-01 --until 2026-04-30
prism-news trends "nuclear power" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "nuclear power" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "nuclear power", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "nuclear power", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [OPEC News](opec-news.md)
- [Recycling Industry](recycling-industry.md)
- [LNG News](lng-news.md)
- [Rare Earths News](rare-earths-news.md)
