# Instagram News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “instagram news” · 6,600/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [instagram-news.json](../../examples/scenarios/instagram-news.json).

**Question.** How much instagram coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="instagram"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 247,357 |
| Negative · neutral · positive | 36% · 0.9% · 63% |
| Critical (priority 7–9) | 28% (70,138 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (78,550 articles) |
| Most-reported country | United States (23% of matches) |
| Strongest theme by lift | sustainable construction materials and practices |

## Twelve months of coverage

Monthly matching articles for `instagram` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 43,371 | 26% | 15,327 | 27,426 | ███████████ |
| Jun 2025 | 36,419 | 25% | 12,023 | 23,947 | █████████ |
| Jul 2025 | 59,047 | 23% | 20,879 | 37,525 | ███████████████ |
| Aug 2025 | 68,154 | 25% | 23,042 | 44,355 | █████████████████ |
| Sep 2025 | 52,877 | 30% | 18,949 | 33,170 | █████████████ |
| Oct 2025 | 42,431 | 25% | 13,463 | 28,469 | ███████████ |
| Nov 2025 | 40,727 | 28% | 13,594 | 26,652 | ██████████ |
| Dec 2025 | 43,391 | 27% | 14,308 | 28,570 | ███████████ |
| Jan 2026 | 43,293 | 27% | 15,553 | 27,219 | ███████████ |
| Feb 2026 | 59,994 | 32% | 23,553 | 35,708 | ███████████████ |
| Mar 2026 | 65,520 | 28% | 24,206 | 40,319 | █████████████████ |
| Apr 2026 | 78,550 | 27% | 26,555 | 50,920 | ████████████████████ |

The last four complete months averaged 61,839 articles a month against 51,748 in the first four (+20%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 42% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 56,036 | 23% |
| India | 11,699 | 4.7% |
| United Kingdom | 7,400 | 3.0% |
| Australia | 2,270 | 0.9% |
| Italy | 1,953 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| sustainable construction materials and practices | 1,977 | 1.4% | +514% |
| green building certifications and standards | 1,974 | 1.4% | +517% |
| building automation and smart systems | 1,969 | 1.4% | +527% |
| indoor air quality management in buildings | 1,968 | 1.4% | +525% |
| mental health and support communities | 2,191 | 1.6% | +127% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Prosecutors say singer D4vd stabbed 14-year-old Celeste Rivas Hernandez to death to silence her \| Houston…](https://houstonpublicmedia.org/articles/news/crime/2026/04/30/550585/prosecutors-say-singer-d4vd-stabbed-14-year-old-celeste-rivas-hernandez-to-death-to-silence-her/) ⚠ | houstonpublicmedia.org | 9 | negative |
| 30 Apr 2026 | [Donald Trump Jr. needs dad to end Iran war so he can get married again](https://www.eastbaytimes.com/2026/04/30/donald-trump-jr-iran-war-wedding/) ⚠ | eastbaytimes.com | 9 | negative |
| 30 Apr 2026 | [HKL Responds After Netizen Expresses Concern Over Congestion At Specialist Clinic](https://says.com/my/news/hkl-responds-after-netizen-expresses-concern-over-congestion-at-specialist-clinic) | says.com | 9 | negative |
| 29 Apr 2026 | [Anonymous tip system started in wake of Sandy Hook shooting has fielded nearly 400,000 reports](https://www.nbcconnecticut.com/news/local/anonymous-tip-system-started-in-wake-of-sandy-hook-shooting-has-fielded-nearly-400000-reports/3730799/) ⚠ | nbcconnecticut.com | 9 | negative |
| 29 Apr 2026 | [Former FBI Director James Comey charged with threatening Donald Trump's life with creepy Instagram post](https://www.uniladtech.com/news/tech-news/former-fbi-director-james-comey-charged-threatening-donald-trump-life-073889-20260429) | uniladtech.com | 9 | negative |
| 29 Apr 2026 | [Mother fakes child cancer to fund lavish life in disturbing Australian case - Türkiye Today](https://www.turkiyetoday.com/lifestyle/mother-fakes-child-cancer-to-fund-lavish-life-in-disturbing-australia-case-3219053) ⚠ | turkiyetoday.com | 9 | negative |
| 29 Apr 2026 | [VIDEO: Father Beats Up Son With Belt On Instagram LIVE! Internet Divided](https://www.timesnownews.com/viral/viral-video-father-beats-up-son-with-belt-on-instagram-live-internet-divided-article-154196813) | timesnownews.com | 9 | negative |
| 29 Apr 2026 | [Former FBI director James Comey indicted over alleged threat to Trump - Social News XYZ](https://www.socialnews.xyz/2026/04/28/former-fbi-director-james-comey-indicted-over-alleged-threat-to-trump/) ⚠ | socialnews.xyz | 9 | negative |
| 28 Apr 2026 | [Violencia sexual organizada](https://www.informacion.es/opinion/2026/04/28/violencia-sexual-organizada-129629404.html) | informacion.es | 9 | negative |
| 28 Apr 2026 | [Laughing California teacher's disturbing nickname for boy, 13, she raped - AOL](https://www.aol.com/entertainment/laughing-california-teachers-disturbing-nickname-164913355.html) | aol.com | 9 | negative |
| 28 Apr 2026 | [White House responds directly to viral social media claims WHCD attempted shooting was 'staged'](https://www.uniladtech.com/news/tech-news/white-house-whcd-staged-claims-response-cole-tomas-allen-521460-20260428) ⚠ | uniladtech.com | 9 | negative |
| 28 Apr 2026 | [Indonesia commuter train crash toll rises to 15 as rescuers complete evacuation](https://www.thestar.com.my/news/world/2026/04/28/indonesia-commuter-train-crash-toll-rises-to-14-as-rescuers-complete-evacuation) ⚠ | thestar.com.my | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "instagram" --since 2026-01-01 --until 2026-04-30
prism-news trends "instagram" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "instagram" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "instagram", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "instagram", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Spacex News](spacex-news.md)
- [Cybersecurity News](cybersecurity-news.md)
- [Chatgpt News](chatgpt-news.md)
- [Whatsapp News](whatsapp-news.md)
