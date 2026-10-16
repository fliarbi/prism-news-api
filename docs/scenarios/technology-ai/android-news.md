# Android News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “android news” · 720/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [android-news.json](../../examples/scenarios/android-news.json).

**Question.** How much android coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="android"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 62,104 |
| Negative · neutral · positive | 19% · 2.3% · 79% |
| Critical (priority 7–9) | 21% (13,153 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (31,572 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | mobile phone hardware components |

## Twelve months of coverage

Monthly matching articles for `android` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 13,666 | 16% | 1,880 | 9,958 | █████████ |
| Jun 2025 | 10,601 | 19% | 1,601 | 8,650 | ███████ |
| Jul 2025 | 14,869 | 17% | 2,379 | 11,993 | █████████ |
| Aug 2025 | 31,572 | 19% | 7,637 | 20,048 | ████████████████████ |
| Sep 2025 | 14,488 | 21% | 2,723 | 11,363 | █████████ |
| Oct 2025 | 12,462 | 20% | 2,119 | 9,759 | ████████ |
| Nov 2025 | 13,347 | 20% | 2,140 | 10,773 | ████████ |
| Dec 2025 | 14,074 | 18% | 1,858 | 9,989 | █████████ |
| Jan 2026 | 12,173 | 19% | 1,824 | 9,752 | ████████ |
| Feb 2026 | 13,953 | 22% | 2,517 | 11,147 | █████████ |
| Mar 2026 | 17,039 | 25% | 3,854 | 12,885 | ███████████ |
| Apr 2026 | 18,939 | 19% | 3,543 | 15,097 | ████████████ |

The last four complete months averaged 15,526 articles a month against 17,677 in the first four (-12%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 47% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 12,913 | 21% |
| India | 4,166 | 6.7% |
| South Korea | 2,983 | 4.8% |
| United Kingdom | 1,497 | 2.4% |
| China | 990 | 1.6% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mobile phone hardware components | 2,849 | 7.6% | +15% |
| mobile phone battery performance | 2,429 | 6.5% | -4% |
| mobile phone camera technology | 2,912 | 7.8% | -18% |
| mobile phone storage solutions | 1,444 | 3.8% | -35% |
| mobile phone display technologies | 2,291 | 6.1% | -3% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 7 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Android users eligible for payout as part of $135M settlement](https://abc11.com/post/android-users-eligible-payout-part-135-million-settlement/18891777/) | abc11.com | 9 | negative |
| 10 Mar 2026 | [Mental health apps are leaking your private thoughts. How do you protect yourself?](https://www.kaspersky.com/blog/mental-health-apps-issues-2026/55395/) | kaspersky.com | 9 | negative |
| 30 Apr 2026 | [EU orders Google to let rival AI assistants use 'Hey Google' wake word on Android](https://cybernews.com/ai-news/brussels-google-android-rival-ai-assistants/) | cybernews.com | 8 | positive |
| 29 Apr 2026 | [‘Time for Linux phones’: Android protests against major Google app change in September grow as developers…](https://www.techradar.com/phones/android/your-phone-is-about-to-stop-being-yours-anger-brewing-among-android-fans-as-major-google-app-change-draws-near) | techradar.com | 8 | negative |
| 28 Apr 2026 | ['Hey ChatGPT' on Android? EU wants Google to give users choice of AI](https://www.yahoo.com/news/articles/hey-chatgpt-android-eu-wants-130914493.html) | yahoo.com | 8 | negative |
| 28 Apr 2026 | [Brussels to Google: share Android's platform with AI rivals](https://www.theregister.com/software/2026/04/28/brussels-to-google-share-androids-platform-with-ai-rivals/5219634) | theregister.com | 8 | positive |
| 28 Apr 2026 | [Exactly when you need to opt in by to claim share of $135 million Android settlement](https://www.uniladtech.com/news/android-google-135m-settlement-deadline-212141-20260427) | uniladtech.com | 8 | negative |
| 28 Apr 2026 | [Brussels consults on Google measures to give Android users choice on AI services - EUbusiness.com \| EU news,…](https://www.eubusiness.com/competition/eu-sends-google-measures-to-give-android-users-ai-choice/) | eubusiness.com | 8 | positive |
| 28 Apr 2026 | [EU tells Google to open Android to AI rivals - TechCentral.ie](https://www.techcentral.ie/eu-tells-google-to-open-android-to-ai-rivals/) | techcentral.ie | 8 | negative |
| 28 Apr 2026 | [The European Commission has launched a public consultation on draft measures requiring Alphabet (Google) to…](https://www.fonearena.com/blog/481182/eu-android-interoperability-rules-consultation-dma.html) | fonearena.com | 8 | positive |
| 28 Apr 2026 | [EU tells Google to open Android to AI rivals](https://www.thehindu.com/sci-tech/technology/eu-tells-google-to-open-android-to-ai-rivals/article70914679.ece) | thehindu.com | 8 | negative |
| 27 Apr 2026 | [Old Android Phones Face WhatsApp Shutdown, Check if Your Device is on the List](https://www.analyticsinsight.net/news/old-android-phones-face-whatsapp-shutdown-check-if-your-device-is-on-the-list) | analyticsinsight.net | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "android" --since 2026-01-01 --until 2026-04-30
prism-news trends "android" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "android" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "android", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "android", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [AI Agents News](ai-agents-news.md)
- [Virtual Reality News](virtual-reality-news.md)
- [Data Breach News](data-breach-news.md)
- [Generative AI News](generative-ai-news.md)
