# Spacex News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “spacex news” · 1,300/month India · 27,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [spacex-news.json](../../examples/scenarios/spacex-news.json).

**Question.** How much spacex coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="SpaceX"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 19,855 |
| Negative · neutral · positive | 28% · 2.1% · 70% |
| Critical (priority 7–9) | 80% (15,797 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (6,907 articles) |
| Most-reported country | United States (41% of matches) |
| Strongest theme by lift | space launch infrastructure development |

## Twelve months of coverage

Monthly matching articles for `SpaceX` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,526 | 75% | 1,444 | 2,022 | ██████████ |
| Jun 2025 | 4,860 | 80% | 2,611 | 2,147 | ██████████████ |
| Jul 2025 | 4,234 | 68% | 1,769 | 2,373 | ████████████ |
| Aug 2025 | 4,840 | 74% | 1,595 | 3,103 | ██████████████ |
| Sep 2025 | 2,749 | 75% | 651 | 2,055 | ████████ |
| Oct 2025 | 2,859 | 78% | 744 | 2,087 | ████████ |
| Nov 2025 | 2,504 | 74% | 630 | 1,847 | ███████ |
| Dec 2025 | 3,251 | 77% | 910 | 2,265 | █████████ |
| Jan 2026 | 3,611 | 80% | 1,280 | 2,251 | ██████████ |
| Feb 2026 | 5,322 | 81% | 1,567 | 3,640 | ███████████████ |
| Mar 2026 | 4,015 | 78% | 1,044 | 2,881 | ████████████ |
| Apr 2026 | 6,907 | 80% | 1,655 | 5,106 | ████████████████████ |

The last four complete months averaged 4,964 articles a month against 4,365 in the first four (+14%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 53% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 8,189 | 41% |
| China | 273 | 1.4% |
| India | 191 | 1.0% |
| United Kingdom | 156 | 0.8% |
| Russia | 125 | 0.6% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| space launch infrastructure development | 1,245 | 9.6% | +15% |
| rocket engine development | 720 | 5.6% | +6% |
| reusable launch vehicle innovations | 983 | 7.6% | +6% |
| satellite communication technologies | 1,230 | 9.5% | +87% |
| space exploration technologies | 486 | 3.8% | +326% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Apr 2026 | [Russia–Ukraine Easter ceasefire begins despite deadly strikes hours before it took effect](https://www.malaymail.com/news/world/2026/04/12/russiaukraine-easter-ceasefire-begins-despite-deadly-strikes-hours-before-it-took-effect/216023) ⚠ | malaymail.com | 9 | negative |
| 12 Apr 2026 | [Easter truce between Russia and Ukraine begins](https://globalnation.inquirer.net/317809/easter-truce-between-russia-and-ukraine-begins) ⚠ | globalnation.inquirer.net | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine begin 32-hour ceasefire for Orthodox Easter](https://www.scmp.com/news/world/article/3349757/russia-and-ukraine-begin-32-hour-ceasefire-orthodox-easter) ⚠ | scmp.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine trade drone strikes ahead of Easter truce](https://www.straitstimes.com/world/europe/russia-and-ukraine-trade-drone-strikes-ahead-of-easter-truce) ⚠ | straitstimes.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce](https://myrepublica.nagariknetwork.com/news/russia-and-ukraine-set-to-begin-easter-truce-24-89.html) ⚠ | myrepublica.nagariknetwork.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce \| Today News](https://www.livemint.com/news/world/russia-and-ukraine-set-to-begin-easter-truce-11775885911120.html) ⚠ | livemint.com | 9 | negative |
| 11 Apr 2026 | [Russia and Ukraine set to begin Easter truce - World News](http://www.hurriyetdailynews.com/russia-and-ukraine-set-to-begin-easter-truce-220893) ⚠ | hurriyetdailynews.com | 9 | negative |
| 10 Apr 2026 | [Russia, Ukraine agree 32-hour ceasefire - Taipei Times](https://www.taipeitimes.com/News/world/archives/2026/04/11/2003855421) ⚠ | taipeitimes.com | 9 | negative |
| 10 Apr 2026 | [Ukraine and Russia will cease fire for Orthodox Easter](https://globalnation.inquirer.net/317629/ukraine-and-russia-will-cease-fire-for-orthodox-easter) ⚠ | globalnation.inquirer.net | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "SpaceX" --since 2026-01-01 --until 2026-04-30
prism-news trends "SpaceX" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "SpaceX" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "SpaceX", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "SpaceX", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Artificial Intelligence News](artificial-intelligence-news.md)
- [Tiktok News](tiktok-news.md)
- [Cybersecurity News](cybersecurity-news.md)
- [Instagram News](instagram-news.md)
