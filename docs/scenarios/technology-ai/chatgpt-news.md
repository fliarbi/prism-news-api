# Chatgpt News: volume, tone and critical headlines (Jan–Apr 2026)

[Technology and AI research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “chatgpt news” · 3,600/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [chatgpt-news.json](../../examples/scenarios/chatgpt-news.json).

**Question.** How much chatgpt coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?

**Request.** `q="ChatGPT"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 26,585 |
| Negative · neutral · positive | 28% · 1.2% · 70% |
| Critical (priority 7–9) | 59% (15,571 articles) |
| Busiest month, May 2025 – Apr 2026 | Aug 2025 (7,648 articles) |
| Most-reported country | United States (22% of matches) |
| Strongest theme by lift | natural language processing models |

## Twelve months of coverage

Monthly matching articles for `ChatGPT` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4,745 | 50% | 907 | 3,767 | ████████████ |
| Jun 2025 | 4,768 | 48% | 991 | 3,716 | ████████████ |
| Jul 2025 | 5,896 | 48% | 1,119 | 4,717 | ███████████████ |
| Aug 2025 | 7,648 | 60% | 2,338 | 5,201 | ████████████████████ |
| Sep 2025 | 6,551 | 56% | 1,486 | 4,993 | █████████████████ |
| Oct 2025 | 7,437 | 57% | 1,471 | 5,894 | ███████████████████ |
| Nov 2025 | 6,290 | 57% | 1,834 | 4,388 | ████████████████ |
| Dec 2025 | 5,769 | 57% | 1,245 | 4,451 | ███████████████ |
| Jan 2026 | 5,697 | 57% | 1,190 | 4,425 | ███████████████ |
| Feb 2026 | 6,847 | 58% | 1,849 | 4,919 | ██████████████████ |
| Mar 2026 | 6,777 | 58% | 2,034 | 4,635 | ██████████████████ |
| Apr 2026 | 7,264 | 61% | 2,456 | 4,732 | ███████████████████ |

The last four complete months averaged 6,646 articles a month against 5,764 in the first four (+15%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 36% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 5,741 | 22% |
| India | 750 | 2.8% |
| United Kingdom | 492 | 1.9% |
| Canada | 265 | 1.0% |
| Italy | 226 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| natural language processing models | 1,473 | 11% | -5% |
| speech recognition and processing systems | 293 | 2.2% | +10% |
| recommender system implementations | 283 | 2.2% | +26% |
| collaboration and communication tools for businesses | 263 | 2.0% | +22% |
| machine learning applications | 255 | 2.0% | +62% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 6 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [OpenAI sued in US by families of Canada school shooting victims](https://www.thestar.com.my/tech/tech-news/2026/04/30/openai-sued-in-us-by-families-of-canada-school-shooting-victims) | thestar.com.my | 9 | negative |
| 29 Apr 2026 | [Sam Altman, OpenAI sued in wake of mass school shooting](https://www.yahoo.com/news/articles/sam-altman-openai-sued-wake-203711202.html) | yahoo.com | 9 | negative |
| 29 Apr 2026 | [Families of Tumbler Ridge victims sue OpenAI and Sam Altman for negligence](https://www.theglobeandmail.com/canada/article-families-tumbler-ridge-shooting-sue-openai/) ⚠ | theglobeandmail.com | 9 | negative |
| 29 Apr 2026 | [Families of Canada school shooting victims sue OpenAI over shooter’s use of ChatGPT](https://www.chicoer.com/2026/04/29/canada-school-shooting-victims-families-sue-openai/) | chicoer.com | 9 | negative |
| 29 Apr 2026 | [Families of Canada school shooting victims sue OpenAI over shooter's use of ChatGPT](https://www.wral.com/news/ap/26d63-families-of-canada-school-shooting-victims-sue-openai-over-shooters-use-of-chatgpt/) | wral.com | 9 | negative |
| 29 Apr 2026 | [OpenAI Hit With Barrage of Lawsuits Over Failure to Report School Shooter Before Massacre](https://futurism.com/artificial-intelligence/openai-school-shooter-tumbler-ridge-lawsuits) ⚠ | futurism.com | 9 | negative |
| 29 Apr 2026 | [What to know about how a suspect in the killing of 2 Florida students used ChatGPT](https://www.joplinglobe.com/region/national_business/what-to-know-about-how-a-suspect-in-the-killing-of-2-florida-students-used/article_09a58c3c-21d2-5bee-b246-37bd8f6cf712.html) | joplinglobe.com | 9 | negative |
| 28 Apr 2026 | [Latest on killed USF students. Has Nahida Bristy's body been found?](https://www.floridatoday.com/story/news/crime/2026/04/28/bridge-help-murdered-usf-students-dashcam-video-abugharbieh-zamil-limon-nahida-bristy/89837448007/) ⚠ | floridatoday.com | 9 | negative |
| 27 Apr 2026 | [Prosecutors say suspect in missing students' killings asked ChatGPT about disposing of a body - KSLTV.com](https://ksltv.com/national-news/suspect-asked-chatgpt-dispose-body/902921/) | ksltv.com | 9 | negative |
| 27 Apr 2026 | [Murder Suspect Allegedly Asked ChatGPT How to Dump Bodies in Zamil Limon, Nahida Bristy Case](https://www.yahoo.com/news/articles/murder-suspect-allegedly-asked-chatgpt-143357468.html) | yahoo.com | 9 | negative |
| 27 Apr 2026 | [Hafiz Saeed aide Sheikh Yousuf Afridi shot dead in Khyber Pakhtunkhwa: Reports - Connected to India News I…](https://www.connectedtoindia.com/hafiz-saeed-aide-sheikh-yousuf-afridi-shot-dead-in-khyber-pakhtunkhwa-reports/) | connectedtoindia.com | 9 | negative |
| 25 Apr 2026 | [Altman says OpenAI ‘deeply sorry’ for not flagging Canadian school shooter’s ChatGPT posts](https://thehill.com/policy/technology/5848734-sam-altman-chatgpt-canada-shooting-messages/) | thehill.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "ChatGPT" --since 2026-01-01 --until 2026-04-30
prism-news trends "ChatGPT" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "ChatGPT" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "ChatGPT", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "ChatGPT", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Cybersecurity News](cybersecurity-news.md)
- [Instagram News](instagram-news.md)
- [Whatsapp News](whatsapp-news.md)
- [Iphone News](iphone-news.md)
