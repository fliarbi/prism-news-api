# Social Media News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “social media news” · 1,000/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [social-media-news.json](../../examples/scenarios/social-media-news.json).

**Question.** How much social media coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="social media"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 215,697 |
| Negative · neutral · positive | 54% · 1.5% · 44% |
| Critical (priority 7–9) | 43% (93,217 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (71,339 articles) |
| Most-reported country | United States (19% of matches) |
| Strongest theme by lift | mental health and support communities |

## Twelve months of coverage

Monthly matching articles for `social media` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 37,489 | 40% | 19,915 | 16,753 | ███████████ |
| Jun 2025 | 32,612 | 38% | 17,783 | 14,217 | █████████ |
| Jul 2025 | 42,427 | 35% | 22,509 | 19,133 | ████████████ |
| Aug 2025 | 44,562 | 39% | 23,389 | 20,342 | ████████████ |
| Sep 2025 | 43,209 | 49% | 24,929 | 17,445 | ████████████ |
| Oct 2025 | 34,403 | 41% | 17,570 | 16,203 | ██████████ |
| Nov 2025 | 32,141 | 42% | 16,716 | 14,867 | █████████ |
| Dec 2025 | 36,244 | 42% | 18,542 | 17,002 | ██████████ |
| Jan 2026 | 38,566 | 42% | 20,421 | 17,418 | ███████████ |
| Feb 2026 | 50,677 | 45% | 28,087 | 21,735 | ██████████████ |
| Mar 2026 | 55,115 | 45% | 30,423 | 23,655 | ███████████████ |
| Apr 2026 | 71,339 | 42% | 37,275 | 32,725 | ████████████████████ |

The last four complete months averaged 53,924 articles a month against 39,272 in the first four (+37%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 40,002 | 19% |
| India | 19,187 | 8.9% |
| United Kingdom | 4,929 | 2.3% |
| Australia | 1,925 | 0.9% |
| China | 1,399 | 0.7% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mental health and support communities | 3,687 | 3.3% | +123% |
| parenting and family-oriented social groups | 2,772 | 2.5% | +93% |
| social media marketing campaigns | 1,152 | 1.0% | +23% |
| impact of technology on family bonds | 2,783 | 2.5% | +54% |
| social media platforms for connecting friends and family | 627 | 0.6% | +175% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [West Warwick police say viral KKK video was hoax created by two brothers](https://www.providencejournal.com/story/news/crime/2026/04/30/ri-police-say-brothers-were-behind-viral-video-of-klan-lookalike/89880908007/) | providencejournal.com | 9 | negative |
| 30 Apr 2026 | [David Allen Coe’s estranged daughter claims she was ‘not given the opportunity’ to see him before his death](https://www.yahoo.com/entertainment/music/articles/david-allen-coe-estranged-daughter-203114596.html) | yahoo.com | 9 | negative |
| 30 Apr 2026 | [Scots mum guilty of baby's murder posted disturbing TikTok videos after newborn's death](https://www.glasgowlive.co.uk/news/glasgow-news/scots-mum-guilty-babys-murder-33866226) | glasgowlive.co.uk | 9 | negative |
| 30 Apr 2026 | [Trump appears to mix up Ukraine and Iran in latest blunder: 'We are so screwed'](https://www.indy100.com/politics/trump/trump-ukraine-iran-mix-up) | indy100.com | 9 | negative |
| 30 Apr 2026 | [Iran war propaganda and free speech questions swirl \| Opinion](https://www.poughkeepsiejournal.com/story/opinion/2026/04/30/iran-war-propaganda-free-speech/89837287007/) ⚠ | poughkeepsiejournal.com | 9 | negative |
| 29 Apr 2026 | [Disturbing video shows man taking his own life](https://punchng.com/disturbing-video-shows-man-taking-his-own-life/) | punchng.com | 9 | negative |
| 29 Apr 2026 | [Kasoa: Pregnant woman dies after C-section request allegedly denied due to lack of bed - Adomonline.com](https://www.adomonline.com/kasoa-pregnant-woman-dies-after-c-section-request-allegedly-denied-due-to-lack-of-bed/) ⚠ | adomonline.com | 9 | negative |
| 29 Apr 2026 | [Who Is Janette MacAusland? 'Failed Murder-Suicide' Speculation Goes Viral After Deaths of Her Two Children](https://www.ibtimes.co.uk/speculation-surrounds-janette-macausland-tragic-childrens-deaths-1794353) ⚠ | ibtimes.co.uk | 9 | negative |
| 29 Apr 2026 | [VIDEO: Father Beats Up Son With Belt On Instagram LIVE! Internet Divided](https://www.timesnownews.com/viral/viral-video-father-beats-up-son-with-belt-on-instagram-live-internet-divided-article-154196813) | timesnownews.com | 9 | negative |
| 29 Apr 2026 | [Mother Makes Son Break His PS5 The Same Way He Abused Family’s Pet Cat](https://www.timesnownews.com/viral/mother-makes-son-break-his-ps5-the-same-way-he-abused-family-pet-cat-viral-video-article-154196150) ⚠ | timesnownews.com | 9 | negative |
| 28 Apr 2026 | [Elon Musk Criticized for ‘Assassinate’ Comment After White House Correspondents’ Dinner Scare](https://www.yahoo.com/news/articles/elon-musk-criticized-assassinate-white-211149511.html) | yahoo.com | 9 | negative |
| 28 Apr 2026 | [Missing girl last seen in Union City found](https://www.yahoo.com/news/articles/missing-girl-last-seen-union-173052381.html) | yahoo.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "social media" --since 2026-01-01 --until 2026-04-30
prism-news trends "social media" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "social media" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "social media", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "social media", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [ISRO News](isro-news.md)
- [Online Gaming News](online-gaming-news.md)
- [Quantum Computing News](quantum-computing-news.md)
- [Robotics News](robotics-news.md)
