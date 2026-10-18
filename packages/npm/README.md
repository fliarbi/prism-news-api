# prism-news-api

[![npm](https://img.shields.io/npm/v/prism-news-api.svg)](https://www.npmjs.com/package/prism-news-api)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/fliarbi/prism-news-api/blob/main/packages/npm/LICENSE)

Zero-dependency JavaScript / TypeScript client and CLI for the
[Prism News API](https://github.com/fliarbi/prism-news-api) by Fliar (450M+ historical and
real-time news articles with sentiment, priority, themes, geography and content classes), plus
helpers for **60 open news-topic datasets** covering January 2019 to July 2026.

ESM, `fetch`-based, Node 18+ and modern browsers. Type definitions included.

```bash
npm install prism-news-api
```

## Client

Create a key in the Fliar dashboard (free tier included; one key works on the Radar API and both
News APIs).

```js
import { PrismNews, PrismAPIError } from "prism-news-api";

const prism = new PrismNews({ apiKey: process.env.PRISM_API_KEY });
// base URL defaults to https://radar-api.fliarbi.com/news

const { data } = await prism.headlines("electric vehicle", { since: "2026-01-01", until: "2026-04-30", limit: 20 });
for (const item of data.items) console.log(item.published_at, item.headline);

await prism.trends("tariffs", { granularity: "monthly" });
await prism.sentiment("heatwave", { since: "2026-04-01" });
await prism.themes("data centers", { limit: 5 });
await prism.compare(["electric vehicle", "battery storage"], { since: "2026-01-01", until: "2026-04-30" });

// Business News API, same key
await prism.business("funding", undefined, { sector: "fintech", sort: "amount", limit: 10 });
await prism.companyNews("tesla.com", { since: "2026-01-01" });

try {
  await prism.me();
} catch (e) {
  if (e instanceof PrismAPIError) console.error(e.status, e.kind);
}
```

Every method resolves to the JSON envelope `{ ok, data, window, meta }`; non-2xx answers reject
with `PrismAPIError`. `prism.request(method, path, body)` calls any endpoint directly. Options:
`apiKey`, `baseUrl`, `businessBaseUrl`, `timeoutMs`, `fetch`.

## Open datasets (no key)

```js
import { listTopics, loadTable, tableUrl } from "prism-news-api";

listTopics({ cluster: "health" });          // [{ slug, topic, cluster, repo, url }, ...]
const monthly = await loadTable("floods", "monthly");   // array of row objects
tableUrl("floods", "sample");               // direct CSV URL
```

Each dataset lives at `https://huggingface.co/datasets/fliarbi/<slug>-news-2019-2026`
(data licence CC BY-NC 4.0). Tables: `sample`, `monthly`, `countries`, `cities`, `continents`,
`country_tone`, `country_trend`, `organisations`, `themes`, `tone_by_year`, `states_india`,
`states_us`, `research_by_year`, `top_papers`, `patents_by_year`, `patent_offices`, `patent_cpc`.

## CLI

```bash
npx prism-news-api --help
export PRISM_API_KEY=rdr_...
npx prism-news-api headlines "electric vehicle" --since 2026-01-01 --limit 20
npx prism-news-api trends tariffs --granularity monthly
npx prism-news-api call POST /v1/business/funding '{"sector":"fintech"}' --business
npx prism-news-api datasets list
npx prism-news-api datasets get floods monthly
```

Installed globally (`npm i -g prism-news-api`), the command is also available as `prism-news`.

## Links

- API docs and 300 worked examples: https://github.com/fliarbi/prism-news-api
- Python client: `pip install prism-news`
- Contact: b2b@fliarbi.com

## Licence

Code: MIT. Datasets: CC BY-NC 4.0.
