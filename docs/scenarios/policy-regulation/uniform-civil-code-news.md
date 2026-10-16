# Uniform Civil Code News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “uniform civil code news” · 390/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [uniform-civil-code-news.json](../../examples/scenarios/uniform-civil-code-news.json).

**Question.** How did coverage of uniform civil code develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="uniform civil code"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 644 |
| Negative · neutral · positive | 49% · 1.9% · 49% |
| Critical (priority 7–9) | 91% (587 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (363 articles) |
| Most-reported country | India (67% of matches) |
| Strongest theme by lift | /people & society/social issues & advocacy/cultural preservation & indigenous rights |

## Twelve months of coverage

Monthly matching articles for `uniform civil code` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 14 | 86% | 7 | 5 | █ |
| Jun 2025 | 14 | 71% | 7 | 7 | █ |
| Jul 2025 | 23 | 61% | 9 | 12 | █ |
| Aug 2025 | 20 | 75% | 6 | 13 | █ |
| Sep 2025 | 19 | 95% | 10 | 7 | █ |
| Oct 2025 | 26 | 85% | 9 | 15 | █ |
| Nov 2025 | 44 | 89% | 16 | 28 | ██ |
| Dec 2025 | 19 | 79% | 10 | 8 | █ |
| Jan 2026 | 51 | 84% | 5 | 43 | ███ |
| Feb 2026 | 39 | 72% | 15 | 24 | ██ |
| Mar 2026 | 191 | 93% | 84 | 107 | ███████████ |
| Apr 2026 | 363 | 93% | 214 | 140 | ████████████████████ |

The last four complete months averaged 161 articles a month against 18 in the first four (+807%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 71% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 434 | 67% |
| United States | 15 | 2.3% |
| Bangladesh | 4 | 0.6% |
| Italy | 1 | 0.2% |
| Pakistan | 1 | 0.2% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| /people & society/social issues & advocacy/cultural preservation & indigenous rights | 34 | 7.6% | +386% |
| /people & society/social issues & advocacy/systemic discrimination & equity efforts | 38 | 8.4% | +375% |
| /people & society/social issues & advocacy/religious discrimination & interfaith initiatives | 38 | 8.4% | +217% |
| political reform and policy changes | 53 | 12% | +2550% |
| /people & society/social issues & advocacy/marginalized communities support | 19 | 4.2% | +850% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Uniform Civil Code Has Nothing To Do With Religion, It's A Constitutional Ambition: CJI Surya Kant](https://www.livelaw.in/top-stories/supreme-court-muslim-inheritance-rights-cji-surya-kant-uniform-civil-code-a-constitutional-ambition-it-has-nothing-to-do-with-religion-530589) | livelaw.in | 8 | negative |
| 15 Apr 2026 | [Chhattisgarh cabinet forms committee to prepare UCC draft - The Shillong Times](https://theshillongtimes.com/2026/04/16/chhattisgarh-cabinet-forms-committee-to-prepare-ucc-draft/) | theshillongtimes.com | 8 | positive |
| 15 Apr 2026 | [Chhattisgarh moves to draft Uniform Civil Code; Rtd Justice Ranjana Desai to head panel](https://www.newindianexpress.com/states/others/2026/Apr/15/chhattisgarh-moves-to-draft-uniform-civil-code-rtd-justice-ranjana-desai-to-head-panel) | newindianexpress.com | 8 | positive |
| 14 Apr 2026 | [As UCC debate resurfaces in poll-bound states, remembering what Ambedkar said in Constituent Assembly](https://indianexpress.com/article/explained/explained-history/uniform-civil-code-ucc-ambedkar-bjp-bengal-assam-10636452/) | indianexpress.com | 8 | positive |
| 14 Apr 2026 | [One Nation One Election is no ‘trial balloon’ for Modi. Sceptics are missing the mark](https://theprint.in/opinion/one-nation-one-election-is-no-trial-balloon-for-modi-sceptics-are-missing-the-mark/2904001/) | theprint.in | 8 | positive |
| 12 Apr 2026 | [Bengal polls: PM Modi says BJP will implement UCC to end ‘appeasement politics’](https://scroll.in/latest/1092048/bengal-modi-says-will-implement-ucc-to-end-appeasement-politics-mamata-calls-it-dangerous) | scroll.in | 8 | positive |
| 12 Apr 2026 | [Uniform Civil Code becomes latest flashpoint between TMC, BJP in Bengal ahead of polls](https://www.hindustantimes.com/india-news/uniform-civil-code-becomes-latest-flashpoint-between-tmc-bjp-in-west-bengal-ahead-of-polls-101775955727543.html) | hindustantimes.com | 8 | negative |
| 11 Apr 2026 | [Bengal Assembly Elections 2026: Wont let Bengalis be a minority, says PM Modi in WB](https://www.mid-day.com/news/india-news/article/bengal-assembly-elections-2026-wont-let-bengalis-be-a-minority-says-pm-modi-in-wb-23625283) | mid-day.com | 8 | negative |
| 11 Apr 2026 | [West Bengal elections 2026: Modi promises women’s quota, police reforms, UCC push](https://economictimes.indiatimes.com/news/elections/assembly-elections/west-bengal/west-bengal-elections-2026-modi-promises-womens-quota-police-reforms-ucc-in-wb/articleshow/130196129.cms) | economictimes.indiatimes.com | 8 | positive |
| 11 Apr 2026 | [Modi promises UCC in Bengal, says Bengalis will not become minority](https://telanganatoday.com/modi-promises-ucc-in-bengal-says-bengalis-will-not-become-minority) | telanganatoday.com | 8 | positive |
| 11 Apr 2026 | [‘Free polls not possible’: Mamata targets BJP over UCC, delimitation](https://www.newindianexpress.com/elections/west-bengal-elections/2026/Apr/11/when-they-won-t-be-in-majority-we-will-revoke-ucc-bill-west-bengal-cm-mamata-banerjee-ahead-of-assembly-polls) | newindianexpress.com | 8 | negative |
| 11 Apr 2026 | [⚡'We Will Revoke UCC Bill': Mamata Banerjee Ahead of West Bengal Assembly Elections 2026](https://www.latestly.com/quickly/agency-news/when-they-wont-be-in-majority-we-will-revoke-ucc-bill-mamata-banerjee-ahead-of-west-bengal-assembly-elections-2026-7389482.html) | latestly.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "uniform civil code" --since 2026-01-01 --until 2026-04-30
prism-news trends "uniform civil code" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "uniform civil code" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "uniform civil code", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "uniform civil code", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [GDPR News](gdpr-news.md)
- [Gun Control News](gun-control-news.md)
- [Stablecoin Regulation News](stablecoin-regulation-news.md)
- [Education Policy News](education-policy-news.md)
