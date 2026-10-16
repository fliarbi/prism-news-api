# Prism News API demonstrations: 300 worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [User guide](../USER_GUIDE.md) · [Animated gallery](../ANIMATED_USE_CASES.md)

Each demonstration answers one real search query with saved responses from the live API:
coverage volume and tone, a twelve-month series, countries, themes and critical
headlines, with the exact requests to reproduce it. Topics were chosen by
[keyword research](../research/KEYWORD_RESEARCH.md) (India and US monthly searches) and kept
only when the API returned populated results.

| Segment | Pages | Highest-demand pages |
| --- | ---: | --- |
| [Industry research](industry-research/README.md) | 50 | [Automotive Industry](industry-research/automotive-industry.md), [Textile Industry](industry-research/textile-industry.md), [Food Processing Industry](industry-research/food-processing-industry.md) |
| [Financial research](financial-research/README.md) | 50 | [Stock Market News](financial-research/stock-market-news.md), [Crypto News](financial-research/crypto-news.md), [GST News](financial-research/gst-news.md) |
| [Disease and health research](disease-health/README.md) | 50 | [Measles Outbreak](disease-health/measles-outbreak.md), [Ebola Outbreak](disease-health/ebola-outbreak.md), [Influenza Outbreak](disease-health/influenza-outbreak.md) |
| [Policy and regulation research](policy-regulation/README.md) | 50 | [Supreme Court News](policy-regulation/supreme-court-news.md), [Tariffs News](policy-regulation/tariffs-news.md), [AI Regulation News](policy-regulation/ai-regulation-news.md) |
| [Technology and AI research](technology-ai/README.md) | 50 | [Artificial Intelligence News](technology-ai/artificial-intelligence-news.md), [Tiktok News](technology-ai/tiktok-news.md), [Spacex News](technology-ai/spacex-news.md) |
| [Energy and climate research](energy-climate/README.md) | 50 | [Natural Gas News](energy-climate/natural-gas-news.md), [Petrol Price News](energy-climate/petrol-price-news.md), [Coal Industry](energy-climate/coal-industry.md) |

Captured 16 Oct 2026 from the live API. Part of the news index was offline (1 of 14 shards,
about 93% of rows available), so every count is a lower bound; some headlines were
temporarily unavailable from the article store and each page says how many.

Regenerate: `scripts/plan_scenarios.py` → `scripts/capture_scenarios.py` → `scripts/build_scenario_pages.py`.
