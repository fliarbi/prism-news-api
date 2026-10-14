# Prism News with Claude Code or Codex: 6 animated use cases

These GIFs show **client-built research UI concepts**: a large typed prompt slides
off-screen, a full-screen chart appears, then a detailed result view follows. Each
32-second loop gives the prompt and the results their own space. The request
recipes list the Prism News API calls behind each view. They are not screen
recordings of the official Claude Code or Codex interface; an assistant with your
API key can call these endpoints and build a similar local view when you ask.

Open the [interactive gallery](demos/index.html) locally for play/pause, replay,
copyable prompts, request recipes, GIF downloads and still images. All GIFs also
render below on GitHub. Each carries a persistent data-provenance badge.

| Workflow | Displayed evidence |
|---|---|
| EV theme discovery | Theme discovery plus headlines for the top theme |
| Tariff sentiment shift | Weekly sentiment timeline plus critical negative headlines |
| Compare two topics | Compare union counts plus weekly trends per query |
| Critical news alerts | Priority bands plus critical headlines |
| GCP class code map | Class discovery for two topics |
| Full articles to CSV | One full-article export batch |

Green badges cite saved API responses. Purple badges mark illustrative fixtures: fictional articles, publishers (.example domains) and counts in the exact response shape, used while the archive cannot be captured in full. Rerunning scripts/capture_demo_examples.py replaces them with real captures.

To ask an agent for a similar view, prepend this instruction to a prompt:

> Use the Prism News API with my key in `PRISM_API_KEY`. Retrieve the
> available evidence, then build a simple local research view. Keep dates,
> windows, missing fields and coverage notes visible. Do not invent unavailable data.

## EV theme discovery

![Discover the themes behind a topic. Illustrative data · fictional articles and counts.](demos/media/ev-theme-discovery.gif)

**Prompt:** What is driving electric vehicle news in March and April 2026? Rank the themes, then show me the headlines behind the strongest one.

**What you would see:** Theme discovery ranks up to five themes for a required phrase by lift: how much more often a theme appears in this coverage than in the 30-day archive baseline, weighted by support. The chart shows lift with each theme's article count and period-over-period change, then the detail view opens newest headlines for the strongest theme with sentiment, priority and class kept visible. Headlines do not carry theme metadata; the selected theme is passed back as a filter.

**Request recipe:** `POST /v1/themes`, `POST /v1/headlines`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/ev-theme-discovery.gif) · [Static image](demos/media/ev-theme-discovery.png) · [API guide](USER_GUIDE.md#discover-themes-and-read-articles)

Illustrative fixtures (fictional articles and counts in the real response shape; replaced by `scripts/capture_demo_examples.py` once captured): [ev-themes.json](examples/demo/ev-themes.json), [ev-theme-headlines.json](examples/demo/ev-theme-headlines.json).

## Tariff sentiment shift

![Watch the tone of a story change week by week. Illustrative data · fictional articles and counts.](demos/media/tariff-sentiment.gif)

**Prompt:** Track the tone of tariff coverage week by week from March to April 2026. When did it turn negative, and which critical headlines drove it?

**What you would see:** The weekly sentiment timeline splits labelled articles into negative, neutral and positive groups. The stacked columns make the turning point visible, and the summary compares the window's negative-to-positive ratio with the archive baseline. The detail view lists critical negative headlines from the same window, so a reader can see which stories drove the shift. Shares divide by articles carrying a sentiment label.

**Request recipe:** `POST /v1/sentiment`, `POST /v1/headlines`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/tariff-sentiment.gif) · [Static image](demos/media/tariff-sentiment.png) · [API guide](USER_GUIDE.md#tone-priority-and-trends)

Illustrative fixtures (fictional articles and counts in the real response shape; replaced by `scripts/capture_demo_examples.py` once captured): [tariff-sentiment.json](examples/demo/tariff-sentiment.json), [tariff-negative-headlines.json](examples/demo/tariff-negative-headlines.json).

## Compare two topics

![Compare two narratives over the same window. Illustrative data · fictional counts.](demos/media/ai-topic-compare.gif)

**Prompt:** Compare AI regulation and AI investment coverage over March–April 2026. Which grew faster, how much do they overlap, and how critical is each?

**What you would see:** Compare returns each query's count and the exact union of both, so overlap is measured rather than guessed. Weekly trends for each query, over identical dates, draw the two lines. The detail table adds each topic's peak week and critical share from its trend totals. Shares divide by the union and can sum past 100%.

**Request recipe:** `POST /v1/compare`, `POST /v1/trends`, `POST /v1/trends`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/ai-topic-compare.gif) · [Static image](demos/media/ai-topic-compare.png) · [API guide](USER_GUIDE.md#compare-25-named-queries)

Illustrative fixtures (fictional articles and counts in the real response shape; replaced by `scripts/capture_demo_examples.py` once captured): [ai-compare.json](examples/demo/ai-compare.json), [ai-regulation-trends.json](examples/demo/ai-regulation-trends.json), [ai-investment-trends.json](examples/demo/ai-investment-trends.json).

## Critical news alerts

![Surface the critical stories in a busy topic. Illustrative data · fictional articles and counts.](demos/media/critical-alerts.gif)

**Prompt:** Show how semiconductor news splits by priority in March–April 2026, then list only the critical stories rated 7 or higher.

**What you would see:** The priority distribution counts articles in bands 1–9 and reports the critical share (7–9) against the archive baseline. The detail view requests only priority 7 and above, so the reader sees just the urgent stories. Priority is an urgency rating from the pipeline, not a reliability judgement.

**Request recipe:** `POST /v1/priority`, `POST /v1/headlines`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/critical-alerts.gif) · [Static image](demos/media/critical-alerts.png) · [API guide](USER_GUIDE.md#sentiment-and-priority)

Illustrative fixtures (fictional articles and counts in the real response shape; replaced by `scripts/capture_demo_examples.py` once captured): [semiconductor-priority.json](examples/demo/semiconductor-priority.json), [semiconductor-critical.json](examples/demo/semiconductor-critical.json).

## GCP class code map

![Turn a topic into GCP content-class codes. Captured data · 14 Oct 2026.](demos/media/class-code-map.gif)

**Prompt:** Which GCP content-class codes cover vehicles and banking? Give me the codes and full paths so I can filter headlines by class.

**What you would see:** Class discovery searches the GCP content-class taxonomy by name and returns up to five integer codes per query with full paths and parents. The tree shows the codes for two topics; the detail table turns them into ready-to-use `classes=` filters. These responses were captured live; 30-day article volumes were temporarily unavailable at capture time, so only codes and paths are shown.

**Request recipe:** `GET /v1/classes`, `GET /v1/classes`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/class-code-map.gif) · [Static image](demos/media/class-code-map.png) · [API guide](USER_GUIDE.md#find-a-gcp-content-code)

Captured responses: [class-map-vehicle.json](examples/demo/class-map-vehicle.json), [class-map-banking.json](examples/demo/class-map-banking.json).

## Full articles to CSV

![Export full article text to a spreadsheet. Illustrative data · fictional articles.](demos/media/full-article-export.gif)

**Prompt:** Export the full text of battery-recycling articles from March–April 2026 to a CSV with headline, publisher, date, sentiment, priority and classes.

**What you would see:** A JSON export returns full article bodies, not the short ledes in headline lists, and charges one export per delivered article. The chart compares body lengths; the detail view shows the same batch in the CSV column layout, ready for a spreadsheet or notebook. Continue with `next_cursor` from a JSON export when you need the next batch.

**Request recipe:** `POST /v1/export`. Selection, charting and file writing are client actions.

[Download GIF](demos/media/full-article-export.gif) · [Static image](demos/media/full-article-export.png) · [API guide](USER_GUIDE.md#full-articles-and-exports)

Illustrative fixtures (fictional articles and counts in the real response shape; replaced by `scripts/capture_demo_examples.py` once captured): [battery-export.json](examples/demo/battery-export.json).

## Reproduce and inspect

The [story data](demos/demo-data.json) records prompts, validated request bodies, source paths/hashes and data labels. The [renderer instructions](demos/README.md) explain capture, deterministic frame rendering, GIF encoding, reduced-motion behaviour and verification.
