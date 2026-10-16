# Thalassemia News: volume, tone and critical headlines (Jan–Apr 2026)

[Disease and health research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “thalassemia news” · 20/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Five saved API responses: [thalassemia-news.json](../../examples/scenarios/thalassemia-news.json).

**Question.** How much thalassemia coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?

**Request.** `q="thalassemia"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 367 |
| Negative · neutral · positive | 15% · 1.6% · 84% |
| Critical (priority 7–9) | 81% (296 articles) |
| Busiest month, May 2025 – Apr 2026 | May 2025 (128 articles) |
| Most-reported country | India (16% of matches) |
| Strongest theme by lift | genetic and genomic research studies |

## Twelve months of coverage

Monthly matching articles for `thalassemia` (`POST /v1/trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 128 | 65% | 20 | 102 | ████████████████████ |
| Jun 2025 | 73 | 75% | 3 | 69 | ███████████ |
| Jul 2025 | 61 | 74% | 6 | 53 | ██████████ |
| Aug 2025 | 74 | 65% | 11 | 60 | ████████████ |
| Sep 2025 | 71 | 80% | 8 | 60 | ███████████ |
| Oct 2025 | 103 | 82% | 25 | 71 | ████████████████ |
| Nov 2025 | 94 | 82% | 14 | 76 | ███████████████ |
| Dec 2025 | 116 | 87% | 16 | 99 | ██████████████████ |
| Jan 2026 | 117 | 81% | 13 | 102 | ██████████████████ |
| Feb 2026 | 88 | 82% | 15 | 71 | ██████████████ |
| Mar 2026 | 77 | 78% | 12 | 63 | ████████████ |
| Apr 2026 | 85 | 81% | 13 | 70 | █████████████ |

The last four complete months averaged 92 articles a month against 84 in the first four (+9%). Archive intake also varies by month, so treat changes as coverage signals rather than event counts.

## Where it was reported

Top five countries (`POST /v1/geography`). 29% of matching articles carry a location.

| Country | Articles | Share of all matches |
| --- | ---: | ---: |
| India | 60 | 16% |
| United States | 28 | 7.6% |
| China | 3 | 0.8% |
| United Arab Emirates | 3 | 0.8% |
| United Kingdom | 3 | 0.8% |

## Themes that stood out

Ranked by lift over each theme's share of the whole archive (`POST /v1/themes`). Change compares with 3 Sep 2025 – 31 Dec 2025.

| Theme | Articles | Share | Change vs previous period |
| --- | ---: | ---: | ---: |
| genetic and genomic research studies | 29 | 14% | +61% |
| rare disease therapies and orphan drugs | 26 | 12% | -28% |
| gene therapy and crispr technologies | 22 | 10% | +22% |
| rare disease research organizations | 22 | 10% | +16% |
| biotechnology innovations in medicine | 19 | 8.9% | +19% |

Lift compares with the archive's most recent 30 days, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.

## Critical headlines

Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown). 13 of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Mar 2026 | [ABP Live Doc Talk \| The Growing Threat Of Sickle Cell And Thalassemia: What You Need To Know](https://news.abplive.com/health/abp-live-doc-talk-the-growing-threat-of-sickle-cell-and-thalassemia-what-you-need-to-know-1832627) | news.abplive.com | 8 | positive |
| 4 Feb 2026 | [Months after 5 children get HIV ‘from Jharkhand hospital’, High Court tells police to register case…](https://indianexpress.com/article/legal-news/5-children-get-hiv-jharkhand-hospital-court-tells-police-register-case-10513635/) | indianexpress.com | 8 | negative |
| 13 Jan 2026 | [Asian Thalassemia Conclave 2026 concludes in Hyderabad](https://indiamedtoday.com/asian-thalassemia-conclave-2026-concludes-in-hyderabad/) | indiamedtoday.com | 8 | positive |
| 11 Jan 2026 | [Telangana sets sights on becoming India’s first thalassemia-free State by 2035](https://www.thehindu.com/news/national/telangana/telangana-sets-sights-on-becoming-indias-first-thalassemia-free-state-by-2035/article70497487.ece) | thehindu.com | 8 | positive |
| 20 Apr 2026 | [झारखंड में बच्चों को चढ़ाया था HIV संक्रमित खून, HC के हस्तक्षेप के बाद हुई आरोपी की गिरफ्तारी](https://www.aajtak.in/india/jharkhand/story/chaibasa-hiv-infected-blood-case-lab-technician-arrested-after-6-months-in-jharkhand-ntc-dpmx-rpti-2528789-2026-04-20) | aajtak.in | 7 | negative |
| 14 Apr 2026 | [Iron Overload-Associated Oxidative Stress and Immune Cell Dysfunction in Thalassemia: Integrative Analysis…](https://pubmed.ncbi.nlm.nih.gov/42072124/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 2 Apr 2026 | [बिहार के 6 मेडिकल कॉलेजों में बनेगा हिमोफीलिया-थैलेसीमिया डे-केयर सेंटर, मरीजों को मिलेगी मुफ्त सुविधा](https://hindi.oneindia.com/news/india/bihar-day-care-centers-haemophilia-thalassemia-six-colleges-012-1533133.html) | hindi.oneindia.com | 7 | positive |
| 1 Apr 2026 | [Outcomes of hematopoietic stem cell transplantation for pediatric patients with transfusion-dependent…](https://pubmed.ncbi.nlm.nih.gov/41821157/) | pubmed.ncbi.nlm.nih.gov | 7 | positive |
| 31 Mar 2026 | [खून की कमी बढ़ा रही है डॉक्टरों की हार्टबीट: आइएमए](https://www.livehindustan.com/jharkhand/gridih/story-severe-blood-shortage-in-giridih-ima-urges-civil-surgeon-for-immediate-action-201774988889131.html) | livehindustan.com | 7 | negative |
| 27 Mar 2026 | [Thalassemia centres in Vijayawada, Anantapur soon: Nara Bhuvaneswari](https://www.thehindu.com/news/national/andhra-pradesh/thalassemia-centres-in-vijayawada-anantapur-soon-nara-bhuvaneswari/article70793183.ece) | thehindu.com | 7 | positive |
| 17 Mar 2026 | [थैलेसीमिया मरीजों के लिए सुरक्षित रक्त की मांग](https://www.livehindustan.com/ncr/faridabad/story-thalassemia-patients-rights-advocated-urgent-need-for-safe-blood-and-treatment-201773744355768.html) | livehindustan.com | 7 | positive |
| 14 Mar 2026 | [120 थैलेसीमिया रोगियों की हुई मुफ्त एचएलए जांच](https://www.livehindustan.com/jharkhand/dhanbad/story-thalassemia-awareness-camp-held-in-dhanbad-by-red-cross-society-201773519282813.html) | livehindustan.com | 7 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-news overview "thalassemia" --since 2026-01-01 --until 2026-04-30
prism-news trends "thalassemia" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-news headlines "thalassemia" --since 2026-01-01 --until 2026-04-30 --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "thalassemia", "since": "2026-01-01", "until": "2026-04-30"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "thalassemia", "since": "2026-01-01", "until": "2026-04-30", "match": "focused", "priority_min": 6, "sort": "priority", "limit": 25}, timeout=60)
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

- [Leprosy News](leprosy-news.md)
- [Drug Shortage News](drug-shortage-news.md)
- [Diabetes Outbreak](diabetes-outbreak.md)
