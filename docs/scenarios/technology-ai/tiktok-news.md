# Tiktok News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tiktok news” · 4,400/month India · 49,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [tiktok-news.json](../../examples/scenarios/tiktok-news.json).

**Question.** How much tiktok coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="TikTok"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 97,813 |
| Negative · neutral · positive | 38% · 0.9% · 62% |
| Critical (priority 7–9) | 33% (32,624 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (30,208 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | mental health and support communities |

## Twelve months of coverage

Monthly matching articles for `TikTok` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18,200 | 32% | 6,798 | 11,207 | ████████████ |
| Jun 2025 | 16,812 | 29% | 5,824 | 10,724 | ███████████ |
| Jul 2025 | 22,192 | 28% | 8,860 | 13,053 | ███████████████ |
| Aug 2025 | 23,204 | 31% | 8,994 | 13,984 | ███████████████ |
| Sep 2025 | 26,749 | 41% | 11,303 | 14,878 | ██████████████████ |
| Oct 2025 | 19,725 | 33% | 7,336 | 12,199 | █████████████ |
| Nov 2025 | 17,745 | 32% | 6,486 | 11,101 | ████████████ |
| Dec 2025 | 18,602 | 35% | 7,066 | 11,336 | ████████████ |
| Jan 2026 | 18,210 | 34% | 6,737 | 11,270 | ████████████ |
| Feb 2026 | 24,239 | 36% | 9,640 | 14,237 | ████████████████ |
| Mar 2026 | 25,156 | 34% | 9,892 | 14,978 | █████████████████ |
| Apr 2026 | 30,208 | 30% | 10,348 | 19,557 | ████████████████████ |

The last four complete months averaged 24,453 articles a month against 20,102 in the first four (+22%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 48% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 27,520 | 28% |
| United Kingdom | 4,215 | 4.3% |
| Australia | 1,291 | 1.3% |
| China | 1,106 | 1.1% |
| Malaysia | 1,069 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mental health and support communities | 1,778 | 3.5% | +83% |
| parenting and family-oriented social groups | 1,347 | 2.7% | +57% |
| social media marketing campaigns | 627 | 1.2% | +16% |
| regulatory compliance frameworks | 513 | 1.0% | +1121% |
| legal aspects of intellectual property | 653 | 1.3% | +478% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Prosecutors say singer D4vd stabbed 14-year-old Celeste Rivas Hernandez to death to silence her \| Houston…](https://houstonpublicmedia.org/articles/news/crime/2026/04/30/550585/prosecutors-say-singer-d4vd-stabbed-14-year-old-celeste-rivas-hernandez-to-death-to-silence-her/) ⚠ | houstonpublicmedia.org | 9 | negative |
| 30 Apr 2026 | [HKL Responds After Netizen Expresses Concern Over Congestion At Specialist Clinic](https://says.com/my/news/hkl-responds-after-netizen-expresses-concern-over-congestion-at-specialist-clinic) | says.com | 9 | negative |
| 30 Apr 2026 | [Scots mum guilty of baby's murder posted disturbing TikTok videos after newborn's death](https://www.glasgowlive.co.uk/news/glasgow-news/scots-mum-guilty-babys-murder-33866226) | glasgowlive.co.uk | 9 | negative |
| 30 Apr 2026 | [‘Horror’ gender reveal before mum kills baby](https://www.news.com.au/lifestyle/real-life/news-life/glasgow-mum-nicole-blain-found-guilty-of-killing-newborn-after-blaming-another-child/news-story/169f0782eca61b2dc650900a01a3f45e) ⚠ | news.com.au | 9 | negative |
| 29 Apr 2026 | [Josh Duggar Reportedly Placed in Solitary Confinement for ‘Rule Violations’](https://www.yahoo.com/entertainment/celebrity/articles/josh-duggar-reportedly-placed-solitary-164753114.html) | yahoo.com | 9 | negative |
| 29 Apr 2026 | [Two Jewish men seriously injured in Golders Green knife rampage](https://www.thescottishsun.co.uk/news/16207191/two-stabbed-golders-green-knifeman-targeting-jewish-members-public/) ⚠ | thescottishsun.co.uk | 9 | negative |
| 28 Apr 2026 | [Texas man charged with paying 13-year-old Montgomery County girl for child porn](https://www.philly.com/crime/montgomery-county-texas-child-porn-arrest-20260428.html) ⚠ | philly.com | 9 | negative |
| 27 Apr 2026 | [Human remains found as search for 2nd missing USF student continues](https://www.usatoday.com/story/news/nation/2026/04/27/usf-missing-students-nahida-bristy-zamil-limon-updates/89816026007/) ⚠ | usatoday.com | 9 | negative |
| 25 Apr 2026 | [My brother’s kidnappers demanded N5m before going silent – Sibling](https://punchng.com/my-brothers-kidnappers-demanded-n5m-before-going-silent-sibling/) ⚠ | punchng.com | 9 | negative |
| 25 Apr 2026 | [Gunfire, blasts rock Mali's Bamako and other cities, army says unidentified terrorist groups targeted…](https://www.livemint.com/news/world/gunfire-blasts-rock-malis-bamako-and-other-cities-army-says-unidentified-terrorist-groups-targeted-locations-11777113315184.html) ⚠ | livemint.com | 9 | negative |
| 24 Apr 2026 | [Chris Olsen Posts Tearful Tribute to Late Grandmother as He Admits He's 'Sad and Angry' About Her Death](https://www.yahoo.com/entertainment/celebrity/articles/chris-olsen-posts-tearful-tribute-175944965.html) | yahoo.com | 9 | negative |
| 23 Apr 2026 | [Hearing in D4vd case set as autopsy details death of Celeste Rivas Hernandez](https://abc7.com/post/d4vd-celeste-rivas-hernandez-murder-case-updates-hearing-singers-set-autopsy-report-released/18950633/) ⚠ | abc7.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "TikTok" --since 2026-01-01 --until 2026-04-30
prism-news trends "TikTok" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "TikTok" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "TikTok", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "TikTok", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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
- [Spacex News](spacex-news.md)
- [Cybersecurity News](cybersecurity-news.md)
