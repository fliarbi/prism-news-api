# Brexit News: volume, tone and critical headlines (Jan–Apr 2026)

[Policy and regulation research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “brexit news” · 320/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [brexit-news.json](../../examples/scenarios/brexit-news.json).

**Question.** How did coverage of brexit develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?

**Request.** `q="brexit"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,745 |
| Negative · neutral · positive | 59% · 4.7% · 36% |
| Critical (priority 7–9) | 62% (6,074 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (3,575 articles) |
| Most-reported country | United Kingdom (22% of matches) |
| Strongest theme by lift | hate crime legislation and enforcement |

## Twelve months of coverage

Monthly matching articles for `brexit` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3,575 | 63% | 1,907 | 1,337 | ████████████████████ |
| Jun 2025 | 1,693 | 54% | 877 | 686 | █████████ |
| Jul 2025 | 2,530 | 56% | 1,429 | 943 | ██████████████ |
| Aug 2025 | 1,851 | 57% | 1,094 | 644 | ██████████ |
| Sep 2025 | 2,279 | 61% | 1,294 | 845 | █████████████ |
| Oct 2025 | 1,910 | 61% | 1,041 | 801 | ███████████ |
| Nov 2025 | 1,897 | 62% | 1,096 | 736 | ███████████ |
| Dec 2025 | 2,073 | 63% | 1,221 | 759 | ████████████ |
| Jan 2026 | 2,021 | 61% | 1,183 | 742 | ███████████ |
| Feb 2026 | 2,747 | 63% | 1,633 | 994 | ███████████████ |
| Mar 2026 | 2,398 | 63% | 1,448 | 833 | █████████████ |
| Apr 2026 | 2,579 | 62% | 1,523 | 929 | ██████████████ |

The last four complete months averaged 2,436 articles a month against 2,412 in the first four (+1%). News intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 50% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| United Kingdom | 2,121 | 22% |
| United States | 1,301 | 13% |
| Belgium | 252 | 2.6% |
| Bahrain | 113 | 1.2% |
| China | 102 | 1.1% |

## Themes that stood out

Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| hate crime legislation and enforcement | 153 | 2.5% | +1430% |
| domestic violence intervention programs | 380 | 6.1% | +1210% |
| juvenile justice and delinquency prevention | 380 | 6.1% | +1210% |
| sex offender registration and community notification | 381 | 6.1% | +1170% |
| biometric data collection for visas | 54 | 0.9% | +8% |

Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 11 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Mar 2026 | [UK should brace for fuel rationing over Iran war crisis, Starmer warned](http://www.independent.co.uk/news/uk/politics/uk-oil-prices-fuel-rationing-starmer-iran-war-b2939318.html) | independent.co.uk | 9 | negative |
| 6 Feb 2026 | [Brexit countdown: UK producers face uncertainty over EU shoots](https://www.screendaily.com/news/brexit-countdown-uk-producers-face-uncertainty-over-eu-shoots/5137702.article) | screendaily.com | 9 | negative |
| 30 Apr 2026 | [Polanski accuses ‘authoritarian’ Labour of ‘using Jewish pain’ to ban marches](https://www.independent.co.uk/news/uk/politics/polanski-mahmood-ban-marches-pro-palestine-jewish-b2967950.html) | independent.co.uk | 8 | negative |
| 30 Apr 2026 | [Reform hopeful slammed for previous anti-Brexit statement despite party stance](https://www.thenational.scot/news/26068358.reform-hopeful-slammed-previous-anti-brexit-statement-despite-party-stance/) | thenational.scot | 8 | negative |
| 29 Apr 2026 | [Keir Starmer accused of losing control of his party after failing to suspend rebels](http://www.independent.co.uk/news/uk/politics/keir-starmer-mandelson-rebel-labour-suspend-b2967287.html) | independent.co.uk | 8 | negative |
| 29 Apr 2026 | [Are Rachel Reeves’ days as chancellor numbered?](https://www.independent.co.uk/news/uk/politics/rachel-reeves-chancellor-sacked-reshuffle-starmer-b2967250.html) | independent.co.uk | 8 | negative |
| 29 Apr 2026 | [Pig sector warns EU reset could weaken UK biosecurity defences](https://www.farminguk.com/news/pig-sector-warns-eu-reset-could-weaken-uk-biosecurity-defences_68411.html) | farminguk.com | 8 | negative |
| 29 Apr 2026 | [What If Reform Wins? by Peter Chappell review – a massive wake-up call](https://www.theguardian.com/books/2026/apr/29/what-if-reform-wins-by-peter-chappell-review-a-massive-wake-up-call) | theguardian.com | 8 | negative |
| 28 Apr 2026 | [Starmer survives crucial vote – but at a cost to his MPs and parliament](https://www.independent.co.uk/news/uk/politics/keir-starmer-privileges-committee-vote-b2966524.html) | independent.co.uk | 8 | negative |
| 27 Apr 2026 | [British businesses 'need a bazooka' to take on Trump, China and the effects of Brexit - Business Biscuit](https://businessbiscuit.com/business-news/economy-news/uk-needs-a-trade-bazooka/) | businessbiscuit.com | 8 | negative |
| 27 Apr 2026 | [More and more people realising those Brexiters sold them a pup](https://www.heraldscotland.com/politics/viewpoint/26052365.brexit-sold-pup-reality-snp-greens-libdems-say/) | heraldscotland.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "brexit" --since 2026-01-01 --until 2026-04-30
prism-news trends "brexit" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "brexit" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$PRISM_API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "brexit", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_API_BASE", "https://radar-api.fliarbi.com/news") + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "brexit", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Data Privacy News](data-privacy-news.md)
- [FSSAI News](fssai-news.md)
- [Census Latest](census-latest.md)
- [Capital Gains Tax News](capital-gains-tax-news.md)
