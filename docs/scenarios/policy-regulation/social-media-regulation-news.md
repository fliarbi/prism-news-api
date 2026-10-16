# Social Media Regulation News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “social media regulation news” · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [social-media-regulation-news.json](../../examples/scenarios/social-media-regulation-news.json).

**Question.** How did coverage of social media regulation develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="social media regulation"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 78 |
| Negative · neutral · positive | 71% · 0.0% · 29% |
| Critical (priority 7–9) | 77% (60 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (35 articles) |
| Most-reported country | United States (28% of matches) |
| Strongest theme by lift | mental health and support communities |

## Twelve months of coverage

Monthly matching articles for `social media regulation` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 22 | 50% | 14 | 8 | █████████████ |
| Jun 2025 | 13 | 85% | 12 | 0 | ███████ |
| Jul 2025 | 11 | 54% | 11 | 0 | ██████ |
| Aug 2025 | 19 | 84% | 14 | 4 | ███████████ |
| Sep 2025 | 22 | 68% | 13 | 7 | █████████████ |
| Oct 2025 | 4 | 100% | 3 | 1 | ██ |
| Nov 2025 | 4 | 100% | 3 | 1 | ██ |
| Dec 2025 | 12 | 75% | 11 | 1 | ███████ |
| Jan 2026 | 9 | 100% | 9 | 0 | █████ |
| Feb 2026 | 35 | 69% | 22 | 13 | ████████████████████ |
| Mar 2026 | 14 | 86% | 13 | 1 | ████████ |
| Apr 2026 | 20 | 75% | 11 | 8 | ███████████ |

The last four complete months averaged 20 articles a month against 16 in the first four (+20%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 60% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 22 | 28% |
| India | 4 | 5.1% |
| Indonesia | 3 | 3.9% |
| Ireland | 3 | 3.9% |
| Spain | 3 | 3.9% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| mental health and support communities | 11 | 26% | +1000% |
| parenting and family-oriented social groups | 8 | 19% | +300% |
| impact of technology on family bonds | 9 | 21% | +800% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 4 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 17 Feb 2026 | [Türkiye moves to require ID verification for social media users - Türkiye Today](https://www.turkiyetoday.com/business/turkiye-moves-to-require-id-verification-for-social-media-users-3214665) | turkiyetoday.com | 8 | positive |
| 13 Feb 2026 | [Oregon looks to regulate AI chatbots - East Oregonian](https://eastoregonian.com/2026/02/13/oregon-looks-to-regulate-ai-chatbots/) | eastoregonian.com | 8 | positive |
| 13 Feb 2026 | [Oregon looks to regulate AI chatbots \| Rogue Valley Times](https://rv-times.com/2026/02/13/oregon-looks-to-regulate-ai-chatbots/) | rv-times.com | 8 | positive |
| 13 Feb 2026 | [Oregon looks to regulate AI chatbots - Seaside Signal](https://seasidesignal.com/2026/02/13/oregon-looks-to-regulate-ai-chatbots/) | seasidesignal.com | 8 | positive |
| 13 Feb 2026 | [Oregon looks to regulate AI chatbots - The Bulletin](https://bendbulletin.com/2026/02/13/oregon-looks-to-regulate-ai-chatbots/) | bendbulletin.com | 8 | positive |
| 6 Feb 2026 | [Kunal Kamra Challenges IT Rules, Sahyog Portal In Bombay HC; Claims Risk Of Unfair Content Removal](https://www.etvbharat.com/en/entertainment/kunal-kamra-challenges-it-rules-sahyog-portal-in-bombay-high-court-claims-risk-of-unfair-content-removal-enn26020606071) | etvbharat.com | 8 | negative |
| 28 Apr 2026 | [No more scrolling: Türkiye bars under-15s from social media - Türkiye Today](https://www.turkiyetoday.com/nation/no-more-scrolling-turkiye-bars-under-15s-from-social-media-3219005) | turkiyetoday.com | 7 | positive |
| 24 Apr 2026 | [WHY ‘16’ IS THE THRESHOLD WE NEED FOR ONLINE SAFETY](https://www.thestar.com.my/news/nation/2026/04/24/why-16-is-the-threshold-we-need-for-online-safety) | thestar.com.my | 7 | positive |
| 19 Mar 2026 | [WhatsApp regulieren? Bildungsministerin Prien wagt brisanten Vorstoß](https://www.braunschweiger-zeitung.de/politik/article411500711/whatsapp-regulieren-bildungsministerin-prien-wagt-brisanten-vorstoss.html) | braunschweiger-zeitung.de | 7 | negative |
| 10 Mar 2026 | [How Sherrill's NJ budget pushes K-12 consolidation to cut costs](https://www.northjersey.com/story/news/education/2026/03/10/mikie-sherrill-nj-budget-pushes-k12-consolidation-cutting-costs/89086941007/) | northjersey.com | 7 | positive |
| 10 Apr 2026 | [Pix incomoda EUA e expõe disputa global \| CNN Brasil](https://www.cnnbrasil.com.br/economia/mercado/pix-incomoda-eua-e-expoe-disputa-global/) | cnnbrasil.com.br | 6 | positive |
| 26 Feb 2026 | [Angela Merkel Advocates for Multilateralism in the Face of Global Challenges \| Law-Order](https://www.devdiscourse.com/article/law-order/3819256-angela-merkel-advocates-for-multilateralism-in-the-face-of-global-challenges) | devdiscourse.com | 6 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "social media regulation" --since 2026-01-01 --until 2026-04-30
prism-news trends "social media regulation" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "social media regulation" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "social media regulation", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "social media regulation", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Insurance Regulation News](insurance-regulation-news.md)
- [Land Acquisition News](land-acquisition-news.md)
- [Disaster Management News](disaster-management-news.md)
- [Wealth Tax News](wealth-tax-news.md)
