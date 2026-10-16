# Prism News API user guide

Explore Fliar’s **450M+ news archive**. Discover relevant themes, compare subjects, and retrieve articles using the same filters throughout a workflow. This guide also defines the shared authentication, GCP content codes, exports and error handling used by the [Business News API](https://github.com/fliarbi/prism-business-news-api/blob/main/docs/USER_GUIDE.md).

**Access status: live.** Base URL `https://radar-api.fliarbi.com/news`; business endpoints are at `https://radar-api.fliarbi.com/business-news`. Create a key in the Fliar dashboard under **API keys** (one key works on the Radar API and both News APIs). Free, Pro (₹4,000/month), Business (₹15,000/month) and Enterprise plans; prices exclude GST. Your `/v1/me` response gives the limits that apply to your key.

## Contents

- [Access and authentication](#access-and-authentication)
- [First query](#first-query)
- [Filters and combinations](#filters-and-combinations)
- [Discover themes and read articles](#discover-themes-and-read-articles)
- [Pagination and filter preservation](#pagination-and-filter-preservation)
- [Full articles and exports](#full-articles-and-exports)
- [Overview, comparison, geography and coverage](#overview-comparison-geography-and-coverage)
- [Interpret results and freshness](#interpret-results-and-freshness)
- [Example workflows](#example-workflows)
- [Quotas, errors and retry](#quotas-errors-and-retry)
- [Endpoint reference](#endpoint-reference)

## Access and authentication

1. Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi), open **API keys** (in the Radar or the Fliar Prism workspace) and choose **Create or manage API keys**. On the key page, choose **Connect Radar session**, pick **All data** or **News only** access and create a key. It starts with `rdr_` and also works on the Radar API.
2. You receive the key once; copy it when shown.
3. Use the base URL `https://radar-api.fliarbi.com/news`. Business endpoints are at `https://radar-api.fliarbi.com/business-news`.
4. Keep the key in an environment variable or your application's secret storage. Use it from your application backend; do not embed it in a public page, repository or URL.

For an interactive Bash session:

```bash
API_BASE=https://radar-api.fliarbi.com/news
read -r -s -p 'API key: ' PRISM_API_KEY
export API_BASE PRISM_API_KEY
```

Send either authentication header, using your issued key:

```bash
curl -sS "$API_BASE/v1/me" -H "X-API-Key: $PRISM_API_KEY"
curl -sS "$API_BASE/v1/me" -H "Authorization: Bearer $PRISM_API_KEY"
```

`/v1/me` returns `data.key`, `data.plan`, `data.limits` and `data.usage`. It does not return your full secret. One key is accepted by both APIs, and requests, exports and rate limits are shared by the account. Creating another key does not create another allowance. Revoke or replace keys through the dashboard once available; use your access contact during preview if key management is unavailable.

After access is enabled, `/guide` serves this user guide as Markdown. `/docs` and `/v1/openapi.json` describe the API available at your supplied base URL. A documentation URL is not proof of a public launch.

## First query

Start with a phrase and inspect the dates as well as the headlines:

```bash
curl -sS --get "$API_BASE/v1/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=electric vehicle' \
  --data-urlencode 'limit=100'
```

Endpoints marked `GET/POST` accept the same filter names in a GET query string or a flat POST JSON object. POST is convenient for lists:

```bash
curl -sS "$API_BASE/v1/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" \
  -H 'Content-Type: application/json' \
  --data '{"q":"electric vehicle","sentiment":["negative"],"priority_min":7,"classes":[0],"limit":100}'
```

The following Python helper, using `requests`, is reused in the examples below. It checks both the HTTP status and the API success flag; it performs no automatic retries.

```python
import os
import requests

BASE = os.environ["API_BASE"].rstrip("/")
session = requests.Session()
session.headers["X-API-Key"] = os.environ["PRISM_API_KEY"]

def call(method, path, **kwargs):
    response = session.request(method, BASE + path, timeout=60, **kwargs)
    payload = response.json()
    if not response.ok or not payload.get("ok"):
        error = payload.get("error") or {}
        raise RuntimeError(
            f"HTTP {response.status_code}: {error.get('kind')} — {error.get('reason')}"
        )
    return payload

page = call("GET", "/v1/headlines", params={"q": "electric vehicle", "limit": 100})
print(page["window"], page["meta"].get("notes", []))
for article in page["data"]["items"]:
    print(article["id"], article["headline"], article["url"])
```

For JSON responses, read:

| Field | Meaning |
|---|---|
| `ok` | Whether the operation succeeded. |
| `feature` | The operation that produced the result. |
| `subject.filters` | Normalized filters actually used, including date or limit adjustments. Not every endpoint has this field. |
| `data` | Result specific to the endpoint. Lists usually have `items`, `returned`, `total_estimate` and `next_cursor`. |
| `window` | Effective dates, `data_through`, and freshness information when applicable. |
| `meta` | Notes, coverage, timing, account plan and quota information when available. |
| `error` | Present on failure, with `kind` and `reason`; `data` is then `null`. |

## Filters and combinations

Different filters combine with **AND**. Multiple values within `sentiment`, `classes` or `themes` combine with **OR**. For example, `sentiment=negative&priority_min=7&classes=0` means negative company news with priority at least 7.

| Parameter | Accepted values and behavior |
|---|---|
| `q` | Free-text phrase, 2–120 characters after normalization, case-insensitive. News search uses the opening text and available subject and entity matches; it is not a full-body search. Required for theme and geography discovery. |
| `match` | Use `any` for broad matching (default), `opening` to require the phrase in the opening text, or `focused` for a more focused subject match that reduces broad roundups. Applies to `q` on news queries. |
| `sentiment` | One or more labels or groups listed below. |
| `priority_min`, `priority_max` | Inclusive integers from 1 to 9; minimum must not exceed maximum. |
| `classes` | One or more integer GCP content codes. A qualifying article must have at least one selected code with a score greater than `0.39`. Code `0` is valid. |
| `class_prefix` | GCP content path such as `/News/Business News` or `/Finance`. Includes codes under that path; combines with `classes` as a union. |
| `themes` | Up to five exact theme names returned by a discovery request. Prefer a JSON array so punctuation is preserved. |
| `country` | Country name, such as `united states`, matched against available article geography. Country information can lag article coverage. |
| `since`, `until` | Inclusive `YYYY-MM-DD` dates. Without dates, `until` is `data_through`, and `since` is 90 days before it. Both endpoints of the interval count, so `window.days` may be 91. History limits can shorten the interval. |
| `limit` | Positive integer. Headlines and exports default to 100; maxima depend on your plan and remaining exports. Theme and geography discovery accept only 1–5, default 5; out-of-range values return `400 bad_request`. Check the effective limit and notes. |
| `sort` | `newest` (default), `oldest`, or `priority` for article lists. |
| `cursor` | Opaque continuation token from the previous page of the same listing. Preserve filters and sort. |
| `granularity` | `daily`, `weekly` (default), or `monthly` on time-series endpoints. |

GET lists use comma-separated values, for example `classes=0,55`. For theme names containing commas, prefer POST with an array; pipe-separated GET values are also supported. Do not invent theme names or treat discovery as a browsable dictionary.

### Sentiment and priority

| Sentiment group | Labels, from negative to positive |
|---|---|
| `negative` | `extreme_neg`, `very_neg`, `fair_neg`, `slight_neg` |
| `neutral` | `none` |
| `positive` | `slight_pos`, `fair_pos`, `very_pos`, `extreme_pos` |

Each article uses its highest-scoring sentiment label and priority band. Higher priority means greater assessed consequence; bands **7–9** are counted as critical. A sentiment score describes the classification, not a percentage price change or a statement that the story is true.

These filters can be used alone or together:

| Goal | Filter object |
|---|---|
| Negative coverage | `{"q":"electric vehicle","sentiment":"negative"}` |
| High-priority coverage | `{"q":"electric vehicle","priority_min":7}` |
| Company news | `{"q":"electric vehicle","classes":[0]}` |
| Combined watchlist | `{"q":"electric vehicle","sentiment":"negative","priority_min":7,"classes":[0]}` |
| Positive company stories in a priority range | `{"sentiment":"positive","classes":[0],"priority_min":4,"priority_max":6}` |

### Find a GCP content code

GCP content codes map to public standardized content paths. `/v1/classes` requires a meaningful `q` (2–120 characters, at least two alphanumeric characters) or a nonroot `prefix` such as `/Finance`. `limit` is 1–5, default 5. Class detail returns the selected code, volume information and at most five children; it does not return themes.

```bash
curl -sS --get "$API_BASE/v1/classes" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=company' --data-urlencode 'limit=5'

curl -sS "$API_BASE/v1/classes/0" -H "X-API-Key: $PRISM_API_KEY"

curl -sS --get "$API_BASE/v1/classes/0/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'sentiment=negative' \
  --data-urlencode 'priority_min=7' --data-urlencode 'limit=100'
```

Code `0` maps to `/News/Business News/Company News`. Use returned `code` values in `classes`, or a public GCP path in `class_prefix`. If a class volume is `null`, it is unavailable, not zero.

## Discover themes and read articles

Theme discovery **requires a specific `q` of 2–120 characters, including at least two alphanumeric characters**. `limit` defaults to **5** and accepts only **1–5**; a larger value returns `400 bad_request`, rather than being reduced. `cursor` is rejected. Select an exact returned theme; discovery has no browse-all operation or dictionary pagination.

```bash
curl -sS --get "$API_BASE/v1/themes" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=electric vehicle' \
  --data-urlencode 'sentiment=negative' \
  --data-urlencode 'priority_min=7' \
  --data-urlencode 'classes=0' \
  --data-urlencode 'limit=5'
```

A discovery item contains `theme`, `count`, `share`, `lift`, `baseline_count`, `previous_period_count`, `delta_pct` and `new_vs_baseline`. The surrounding result includes `matched`, `carrying`, `carrier_share_pct`, `baseline`, `previous_period` and `ranked_by`.

Use the returned name and normalized filters for headlines and exports. This example makes three requests and the export consumes full-article allowance:

```python
discovery = call("POST", "/v1/themes", json={
    "q": "electric vehicle", "sentiment": "negative",
    "priority_min": 7, "classes": [0], "limit": 5,
})
selected_theme = discovery["data"]["items"][0]["theme"]
filters = dict(discovery["subject"]["filters"])
filters.pop("cursor", None)
filters.update(themes=[selected_theme], limit=100)

headlines = call("POST", "/v1/headlines", json=filters)
exported = call("POST", "/v1/export", json={**filters, "format": "json"})
print(headlines["data"]["returned"], exported["data"]["charged_exports"])
```

The dedicated `GET /v1/themes/{name}/headlines` route also accepts the common filters and `limit=100`. URL-encode the selected name, or use the POST pattern above to avoid path encoding. A theme in the path is added to any supplied `themes`; omit other themes when you want only the selected one.

Discovery's five-result limit applies to suggestions. A selected theme returns **100 headlines per page by default** and **100 full articles per export batch by default**, subject to account limits. Higher caps depend on your plan. Headlines, single articles and exports do not include theme metadata; select themes through discovery. Empty discovery can mean that no theme meets the minimum support of five matching articles, even when headlines exist.

## Pagination and filter preservation

Use `data.next_cursor` as the next request's `cursor`. It is tied to the listing and sort, not a page number. Do not decode or construct it. Preserve `q`, `match`, sentiment, GCP codes, themes, priority, country, dates and sort.

Freeze effective `since` and `until` from the first response. A default window can otherwise move when available coverage changes. `subject.filters.cursor` may be the Boolean `true`; it is only a marker and must never replace `data.next_cursor`.

```python
page = call("POST", "/v1/headlines", json={
    "q": "electric vehicle", "sentiment": "negative",
    "priority_min": 7, "classes": [0], "sort": "newest", "limit": 100,
})
fixed = dict(page["subject"]["filters"])
fixed.pop("cursor", None)
seen = set()

while True:
    for item in page["data"]["items"]:
        if item["id"] not in seen:
            seen.add(item["id"])
            print(item["headline"], item["url"])
    cursor = page["data"].get("next_cursor")
    if not cursor:
        break
    page = call("POST", "/v1/headlines", json={**fixed, "cursor": cursor})
```

This loop continues until the listing ends and consumes one request per page. Bound it in your application if you only need a sample. A short or empty page can still have a continuation token because some matching articles are unavailable or duplicates were omitted. Stop on a missing token, not merely on `returned < limit`.

When switching from discovery to headlines, or from headlines to exports, start the new listing without the old cursor. Obtain subsequent tokens from that endpoint. Distribution and discovery endpoints are not pageable article lists.

## Full articles and exports

Headline items include `id`, `headline`, `url`, `publisher`, `published_at`, `lede`, `sentiment`, `priority`, `classes`, `country`, `organizations` and `people`. Individual fields may be unavailable. Full articles add `body`, `body_chars`, `authors`, `top_image`, `meta_description`, `publish_date` and `language`.

Fetch one article using a returned headline ID:

```python
article_id = headlines["data"]["items"][0]["id"]
full = call("GET", f"/v1/articles/{article_id}")
print(full["data"]["article"]["body"])
```

`GET /v1/articles/{article_id}` consumes one request and one export allowance when the article is delivered. A full article can be unavailable even when a related record exists.

For batches, send common filters plus `format` to `POST /v1/export`. The default is 100 full articles per call. Your plan’s `max_export_batch` determines the cap; remaining export allowance can reduce the batch further.

```bash
curl -sS "$API_BASE/v1/export" \
  -H "X-API-Key: $PRISM_API_KEY" \
  -H 'Content-Type: application/json' \
  --data '{"q":"electric vehicle","sentiment":"negative","priority_min":7,"classes":[0],"limit":100,"format":"json"}'
```

| Format | Response and continuation |
|---|---|
| `json` (default) | Normal envelope, full articles in `data.items`, continuation in `data.next_cursor`. Best for paged exports. |
| `ndjson` | First line is the envelope with `data.stream=true` and no `items`; subsequent lines are individual article objects. The first line contains the next cursor. |
| `csv` | Columns: `id,headline,url,publisher,published_at,sentiment,priority,classes,body`. `classes` contains code/path pairs separated by pipes. Theme metadata is omitted in every export format. Use JSON or NDJSON when you need a continuation token. |

NDJSON parsing, using the same filters as the selected theme:

```python
import json

response = session.post(BASE + "/v1/export", json={**filters, "format": "ndjson"}, timeout=60)
if not response.ok:
    raise RuntimeError(response.json().get("error"))
lines = iter(line for line in response.text.splitlines() if line.strip())
envelope = json.loads(next(lines))
if not envelope.get("ok"):
    raise RuntimeError(envelope.get("error"))
print(envelope["data"]["charged_exports"], envelope["data"]["next_cursor"])
for line in lines:
    article = json.loads(line)
    print(article["headline"], article["body_chars"])
```

Export failures return a JSON error envelope even if you requested CSV or NDJSON. Check status before saving or parsing a download. CSV and NDJSON responses include `X-Export-Delivered` and quota headers when available.

`charged_exports` counts articles delivered, not the requested batch size. `unresolved` counts matching articles that could not be supplied, and `duplicates_dropped` counts omitted duplicate URLs within the page. Save article IDs across batches if you need to deduplicate the complete download. Repeating a successful export or single-article request consumes allowance again.

## Overview, comparison, geography and coverage

Use overview for an initial subject summary, comparison for named alternatives, geography for a bounded location breakdown, and coverage to assess whether a result supports your analysis. These endpoints are part of the preview contract; check availability on the base URL supplied with access.

```bash
curl -sS --get "$API_BASE/v1/overview" \
  -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'q=electric vehicle'

curl -sS --get "$API_BASE/v1/geography" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=electric vehicle' --data-urlencode 'limit=5'

curl -sS --get "$API_BASE/v1/coverage" \
  -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'q=electric vehicle'
```

### Overview response

`/v1/overview` returns `data.matched`, `data.tone` and `data.critical`. Tone includes `carrying`, `availability_pct` and `groups`; each group has `group`, `count` and `share_pct`. Critical includes `min_priority`, `carrying`, `count` and `share_pct`. Tone shares use articles carrying a recognized sentiment; critical share uses articles carrying priority. The summary covers the whole filtered window, independent of a headline page limit.

### Compare 2–5 named queries

`POST /v1/compare` takes a `queries` array of **2–5** objects. Each has `name` and a nested `filters` object. Names must be 1–80 characters and unique after ignoring case and normalizing whitespace. Ordinary POST search endpoints use flat filters; this endpoint uses the structure below.

```python
anchor = call("POST", "/v1/headlines", json={"q": "electric vehicle", "limit": 1})
window = {key: anchor["subject"]["filters"][key] for key in ("since", "until")}
comparison = call("POST", "/v1/compare", json={"queries": [
    {"name": "Electric vehicles", "filters": {**window, "q": "electric vehicle", "classes": [0]}},
    {"name": "Battery storage", "filters": {**window, "q": "battery storage", "classes": [0]}},
]})
print(comparison["data"])
```

`data.items` contains each query's `name`, `count`, `share_pct`, normalized `filters` and effective `window`. `data.matched` is the count of articles matching at least one query; `share_basis` describes that denominator and `sets_may_overlap` is `true`. Overlapping shares can sum to more than 100%. Each query retains its own effective window, so check those dates even when you supplied common dates.

Keep dates, GCP scope and matching mode comparable. Add `sentiment` or priority bounds to each query when comparing the same subset. Comparison returns article counts and shares; use `/v1/overview` or `/v1/sentiment` with each filter set for a tone comparison.

### Geography

`GET/POST /v1/geography` requires `q`, with `limit` from 1 to 5 and default 5. Reuse the same news filters as your headlines query. It returns `matched`, `carrying`, `availability_pct`, `items`, `returned`, `limit` and `other_located_count`. Items contain `country`, `count` and `share_pct`, ranked by count.

Country shares divide by **all matching articles**, including those without a known location. `other_located_count` covers located articles outside the returned countries; missing-location articles are `matched - carrying`. Location information can be less current than the articles. There is no country-directory pagination.

### Coverage

Archive size is supplied by Fliar; query counts reflect the available matching coverage.

`GET/POST /v1/coverage` returns `data.matched` and `data.availability`. Its `sentiment`, `theme` and `location` entries each have `count` and `percentage`, measured within your filters. It reports availability of those signals, without exposing theme names. Percentages use matching articles as the denominator.

Overview, comparison, geography and coverage can return successful zero counts. When the denominator is zero, percentages are `null`. These results differ from a failed coverage check (`503`) or the `404 no_data` used by some listing and discovery endpoints.

`/v1/status` returns `data.healthy`, `data.data_through`, `data.freshness`, `data.location_coverage_note` and `data.archive`. The archive description has `article_count_display="450M+"`, `scope="Fliar news archive"` and `note`. Read `data.healthy` even when the status endpoint returns HTTP 200; use `/v1/coverage` to examine your own query's available signals.

### Related reading

`GET /v1/articles/{article_id}/related` requires **both a returned seed article ID and `q`**. It accepts common news filters, sort, cursor and `limit` (default 100, plan-bounded). Keep the seed within the requested dates and preserve those dates while paging.

```python
seed = call("POST", "/v1/headlines", json={"q": "electric vehicle", "limit": 1})
article_id = seed["data"]["items"][0]["id"]
related_filters = dict(seed["subject"]["filters"])
related_filters.pop("cursor", None)
related_filters.update(limit=100)
# Encode array-valued GET filters as comma-separated values if adding any.
related = call("GET", f"/v1/articles/{article_id}/related", params=related_filters)
print(related["data"]["returned"], related["data"]["next_cursor"])
```

Related headlines must satisfy your filters and share relevant themes with the seed. The seed itself is excluded. The result uses the headline list shape, including `total_estimate`, `next_cursor`, `unresolved` and `duplicates_dropped`, and omits theme metadata. It consumes a request but no full-article allowance. An unavailable seed, a seed outside the window, or a seed without suitable theme information produces `404 no_data`; no related matches can return an empty successful list. Related coverage is a reading aid, not proof of independent corroboration.

## Interpret results and freshness

Always record the filters and dates alongside a count. A successful response establishes that the request succeeded, not that the archive is current to today or complete for every country and subject.

- **`data_through`** is the latest available date for the relevant coverage. It is not a promise of complete coverage through that day.
- **`since` and `until`** describe the query that ran. Dates beyond `data_through` are reduced to available coverage; history allowances may shorten the beginning. Read `meta.notes`.
- **`freshness`** describes limitations such as sparse recent coverage. A recent decline can reflect incomplete coverage rather than fewer real-world events.
- **Coverage status** describes availability for the response. `503 coverage_unavailable` is not an empty result.
- **Partial archive.** When part of the archive is temporarily offline, the service answers from the available part and puts "Part of the archive is temporarily offline … counts are lower bounds" first in `meta.notes`. Treat those counts as minimums.
- **`partial_period`** marks a time bucket only partly covered by the requested date interval. It does not certify that unflagged periods contain complete reporting. Compare complete periods with compatible freshness.
- **`total_estimate`** on an article list counts matches before unavailable articles and page-level duplicate removal. It can exceed the number of unique articles you can download. Theme and class discovery return `total_estimate=null`; they do not expose a complete result dictionary.

### Tone, priority and trends

`/v1/sentiment` returns `matched`, `carrying`, `carrier_share_pct`, nine `labels`, three `groups`, ratios, a `baseline` and a `timeline`. Shares divide by articles carrying a sentiment label. Ratios can be `null` when a denominator is absent; do not turn that into zero or infinity.

`/v1/priority` returns `bands`, `critical`, `mean_priority`, `baseline` and `vs_baseline_critical`, plus matching and carrying counts. Its critical share divides by articles carrying priority. By comparison, trend `critical_pct` uses all articles in its period.

`/v1/trends` returns `points` with `period`, `articles`, `critical`, `critical_pct`, `negative`, `positive` and `partial_period`. It also returns `total`, `critical_total`, `complete_periods`, `partial_periods` and `peak`. Empty buckets within a nonempty result are included as zero.

### Theme scores

Theme `share` is a percentage of matching articles carrying themes, not all matching articles. Multiple themes can occur in one article, so shares need not sum to 100%. `lift` compares that share with a 30-day archive baseline; the ranking also weights article support. A high lift is relative prominence, not evidence of factual reliability.

`previous_period_count` uses the immediately preceding interval of equal length when that interval is within your plan’s history allowance. If it is outside the allowance, `previous_period`, `previous_period_count` and `delta_pct` are `null`, with a note. `delta_pct` is also `null` when the previous count is zero. `lift=null` with `new_vs_baseline=true` means no finite baseline ratio is available. Inspect the returned comparison dates; they can differ from the analysis window.

## Example workflows

| Workflow | Sequence and interpretation |
|---|---|
| Subject briefing | Run overview and coverage with `q`; inspect dates; discover at most five themes; read 100 headlines for a selected theme; export the full articles needed for the briefing. |
| Risk monitoring | Combine `q`, `sentiment=negative`, `priority_min=7` and relevant GCP codes; inspect priority and trends; read original articles before escalating a finding. |
| Compare coverage | Use 2–5 named queries with the same dates and GCP scope; compare counts and overlapping shares; request overview or sentiment separately for tone, then inspect sample headlines. |
| Geographic context | Run geography with `q` and `limit=5`; inspect missing or lagging location information; apply a returned country to a headline query with the same dates. |
| Research collection | Freeze dates and filters; page through JSON or NDJSON exports in batches of 100; save cursors, article IDs and quota usage after each successful batch. |

Counts describe reporting in available coverage. They are not counts of unique real-world incidents, population sentiment, company performance or independent confirmations.

## Quotas, errors and retry

Check `/v1/me` for `data.limits` and `data.usage`; it is authoritative for your key. Upgrade in the Fliar dashboard under **API keys → Prism News API plans**. Relevant limits include `requests_per_month`, `exports_per_month`, `rate_per_minute`, `history_days`, `max_results` and `max_export_batch`.

Both headlines and exports default to **100**, on every plan. The caps per plan are below; your `/v1/me` response is authoritative for your access. Discovery remains capped at five regardless of plan.

| Plan | Headline cap (`max_results`) | Export batch cap (`max_export_batch`) |
|---|---|---|
| Free / Pro | 100 | 100 |
| Business | 500 | 500 |
| Enterprise | 1,000 | 1,000 |

Requests and delivered full articles are separate allowances. They are shared across both APIs and all keys for an account, and monthly allowances reset on the first day of the UTC month. A metered request can consume request allowance even if a later validation or data operation fails. Export allowance is charged for delivered articles; unavailable articles are not charged.

`/v1/me`, `/v1/status`, GCP code search and detail, and `/v1/vocabulary` do not consume monthly request allowance. **`/v1/classes/{code}/headlines` is metered.** Unmetered authenticated routes still count toward the rate limit.

Read these headers when present: `X-Plan`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-Quota-Requests-Remaining`, `X-Quota-Exports-Remaining` and `Retry-After`. JSON envelopes also carry `meta.quota` when available.

| HTTP | `error.kind` | What to do |
|---|---|---|
| 400 | `bad_request` | Correct the filters, date interval, code, ID or cursor. Supply `q` on discovery. Do not repeat the same invalid request. |
| 401 | `unauthenticated` | Supply one supported authentication header. |
| 401 | `invalid_key` | Check for a mistyped, revoked or invalid key; replace it through your access process. |
| 402 | `quota_exceeded` | Inspect `/v1/me`. Wait for the monthly reset or contact Fliar about access. There is no active plan checkout. |
| 404 | `no_data` | Check `reason`: the endpoint or article may not exist, the filters may match nothing, or discovery may lack enough support. Broaden filters or adjust dates where appropriate. |
| 429 | `rate_limited` | Wait at least the `Retry-After` duration, then retry with less concurrency. |
| 500 | `internal` | Retry a limited number of times; report persistent failures with endpoint, time and sanitized filters. |
| 502 | `upstream` | A dependency is temporarily unavailable. Retry with backoff. |
| 503 | `coverage_unavailable` | Required coverage could not be established. Retry later; never record this as a zero count. |

For transient 429/500/502/503 responses, use bounded exponential backoff with jitter, for example up to three retries at roughly 1, 2 and 4 seconds. Honor a longer `Retry-After` value. Stop when your application deadline or retry budget is reached. Ordinary retries may consume another request allowance.

Treat timeouts during full-article retrieval or exports separately: a lost response does not prove that no articles were charged. Check usage and saved output before repeating the request; there is no documented idempotency key for these operations. Never include your secret key in a support report.

## Endpoint reference

All `/v1` operations below require a key. “Request” means monthly request allowance; full articles also consume export allowance. Common filters are defined above; do not assume every route accepts every parameter.

| Method and path | Parameters / result | Allowance |
|---|---|---|
| `GET/POST /v1/headlines` | Common filters; 100 headline items by default with cursor pagination. | Request |
| `GET/POST /v1/overview` | Common news filters; `matched`, `tone` and `critical`. | Request |
| `POST /v1/compare` | `queries` with 2–5 unique `name`/`filters` objects; counts, union count and overlapping shares. | Request |
| `GET/POST /v1/geography` | Common filters; `q` required, `limit=1–5` (default 5); country counts and location availability. | Request |
| `GET/POST /v1/coverage` | Common news filters; `matched` and `availability` of sentiment, themes and location. | Request |
| `GET/POST /v1/themes` | Common filters; specific `q` required, `limit=1–5` (default 5); cursor rejected. | Request |
| `GET /v1/themes/{name}/headlines` | URL-encoded returned theme name plus common filters; 100 headlines by default. | Request |
| `GET/POST /v1/sentiment` | Common filters plus `granularity`; distribution, baseline and timeline. | Request |
| `GET/POST /v1/priority` | Common filters; bands and critical share. | Request |
| `GET/POST /v1/trends` | Common filters plus `granularity`; volume time series. | Request |
| `GET /v1/classes` | `q` or nonroot `prefix` required, `limit=1–5` (default 5). | No monthly request |
| `GET /v1/classes/{code}` | Integer GCP code including `0`; code detail, volume and at most five children; no themes. | No monthly request |
| `GET /v1/classes/{code}/headlines` | Integer code plus common filters; 100 headlines by default. | Request |
| `GET /v1/articles/{article_id}` | Returned article ID; full article in `data.article`. | Request + 1 delivered article |
| `GET /v1/articles/{article_id}/related` | Returned article ID plus required `q`; common filters, sort and cursor; 100 headlines by default, plan-bounded. | Request |
| `POST /v1/export` | Common filters plus `format=json\|ndjson\|csv`; 100 full articles per batch by default. | Request + delivered articles |
| `GET /v1/vocabulary` | Public sentiment labels, groups, priority bands, sort, format and plan metadata. No theme dictionary. | No monthly request |
| `GET /v1/me` | Account key summary, access limits and usage. | No monthly request |
| `GET /v1/status` | Service availability and freshness; inspect `data.healthy`, not HTTP status alone. | No monthly request |

`GET /guide` serves this guide as Markdown. `GET /healthz` is a liveness check without a key; it does not establish fresh or complete news coverage. `/docs` and `/v1/openapi.json` provide the interactive and machine-readable endpoint reference for your access environment.
