# Healthcare Industry News: volume, tone and critical headlines (Jan–Apr 2026)

[Industry research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “healthcare industry” · 1,300/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [healthcare-industry.json](../../examples/scenarios/healthcare-industry.json).

**Question.** How much news did healthcare receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?

**Request.** `q="healthcare"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 270,004 |
| Negative · neutral · positive | 28% · 2.6% · 69% |
| Critical (priority 7–9) | 70% (189,849 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (75,272 articles) |
| Most-reported country | United States (21% of matches) |
| Strongest theme by lift | patient safety and quality improvement studies |

## Twelve months of coverage

Monthly matching articles for `healthcare` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 59,156 | 69% | 18,702 | 38,094 | ████████████████ |
| Jun 2025 | 43,479 | 72% | 12,958 | 29,091 | ████████████ |
| Jul 2025 | 55,376 | 67% | 19,979 | 33,744 | ███████████████ |
| Aug 2025 | 57,320 | 68% | 20,036 | 35,681 | ███████████████ |
| Sep 2025 | 57,232 | 73% | 17,225 | 38,341 | ███████████████ |
| Oct 2025 | 56,686 | 74% | 16,551 | 38,515 | ███████████████ |
| Nov 2025 | 52,267 | 74% | 14,689 | 35,824 | ██████████████ |
| Dec 2025 | 58,718 | 74% | 15,445 | 41,280 | ████████████████ |
| Jan 2026 | 62,166 | 73% | 15,521 | 44,600 | █████████████████ |
| Feb 2026 | 70,660 | 71% | 21,247 | 47,674 | ███████████████████ |
| Mar 2026 | 61,906 | 70% | 17,997 | 42,237 | ████████████████ |
| Apr 2026 | 75,272 | 67% | 21,645 | 51,406 | ████████████████████ |

The last four complete months averaged 67,501 articles a month against 53,833 in the first four (+25%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 39% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United States | 56,698 | 21% |
| India | 14,979 | 5.5% |
| United Kingdom | 7,781 | 2.9% |
| China | 2,403 | 0.9% |
| Canada | 2,112 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| patient safety and quality improvement studies | 5,506 | 3.7% | +10% |
| public health initiatives and programs | 4,696 | 3.1% | +16% |
| health economics and resource allocation | 3,438 | 2.3% | +12% |
| health system strengthening initiatives | 3,085 | 2.1% | +16% |
| health disparities and equity research | 6,037 | 4.0% | +17% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 8 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [Measles surge accompanied by rising dengue prevalence](http://www.dhakatribune.com/bangladesh/health/408829/measles-surge-accompanied-by-rising-dengue) | dhakatribune.com | 9 | negative |
| 25 Apr 2026 | [Personal and Medical Records of 160,312 Americans Potentially Exposed After Major Data Breach Hits…](https://dailyhodl.com/2026/04/25/personal-and-medical-records-of-160312-americans-potentially-exposed-after-major-data-breach-hits-healthcare-firm/) | dailyhodl.com | 9 | negative |
| 22 Apr 2026 | [Duale tells Senate SHA system under strain from fraud](https://www.capitalfm.co.ke/business/2026/04/duale-tells-senate-sha-system-under-strain-from-fraud/) | capitalfm.co.ke | 9 | negative |
| 20 Apr 2026 | [Sensitive Information Belonging to 337,917 People Potentially Exposed As Tennessee Healthcare Firm Hit by…](https://dailyhodl.com/2026/04/20/sensitive-information-belonging-to-337917-people-potentially-exposed-as-tennessee-healthcare-firm-hit-by-data-breach/) | dailyhodl.com | 9 | negative |
| 18 Apr 2026 | [50,640 People Affected After Hackers Hit Healthcare Firm, Stealing Personal, Financial and Medical Data -…](https://dailyhodl.com/2026/04/18/50640-people-affected-after-hackers-hit-healthcare-firm-stealing-personal-financial-and-medical-data/) | dailyhodl.com | 9 | negative |
| 18 Apr 2026 | [Bay Area doctor highlights health inequities for Black pregnant women](https://www.fox13news.com/news/bay-area-doctors-health-black-pregnant-women) | fox13news.com | 9 | negative |
| 17 Apr 2026 | [First responders credit years of training for lives saved during the Florida State University shooting](https://www.wtxl.com/northeast-tallahassee/first-responders-credit-years-of-training-for-lives-saved-during-the-florida-state-university-shooting) ⚠ | wtxl.com | 9 | negative |
| 17 Apr 2026 | [Wasted Dollars, Wrong Priorities: What Trump and Miller's Mass Deportation Spending Spree Costs Working…](https://americasvoice.org/press_releases/wasted-dollars-wrong-priorities-what-trump-and-millers-mass-deportation-spending-spree-costs-working-families/) | americasvoice.org | 9 | negative |
| 17 Apr 2026 | [Average of 47 women and girls killed daily during Gaza war, UN says](https://www.straitstimes.com/world/middle-east/average-of-47-women-and-girls-killed-daily-during-gaza-war-un-says) | straitstimes.com | 9 | negative |
| 14 Apr 2026 | [This week, Republicans in the House of Representatives planned a vote to repeal President Barack Obama's…](https://www.bbc.co.uk/blogs/thereporters/markmardell/2011/01/sarah_palin_and_the_arizona_sh_1.html) | bbc.co.uk | 9 | negative |
| 12 Apr 2026 | [Trump’s new budget ignores dying Americans and gives away record sums to the US military](https://www.theguardian.com/us-news/2026/apr/12/trump-budget-healthcare-military) | theguardian.com | 9 | negative |
| 11 Apr 2026 | [46,666 People Affected After Hackers Hit Healthcare Firm – Company Warns Data Now on Dark Web in 'Limited…](https://dailyhodl.com/2026/04/11/46666-people-affected-after-hackers-hit-healthcare-firm-company-warns-data-now-on-dark-web-in-limited-amount/) | dailyhodl.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "healthcare" --since 2026-01-01 --until 2026-04-30
prism-news trends "healthcare" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "healthcare" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "healthcare", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "healthcare", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Diamond Industry](diamond-industry.md)
- [Gaming Industry](gaming-industry.md)
- [Plastics Industry](plastics-industry.md)
- [Aviation Industry](aviation-industry.md)
