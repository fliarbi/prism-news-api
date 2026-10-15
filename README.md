# Prism News API

Explore Fliar’s **450M+ news archive**. Search news, combine sentiment, priority and GCP content codes, discover themes, compare subjects, and retrieve headlines or full articles.

**Private preview.** Production dashboard key issuance and the public API rollout are pending. Proposed API hosts are preview addresses, not confirmed live services. Use the `API_BASE` supplied when access is granted. Plans are drafts; there is no active checkout.

## Get access and make a first request

1. Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=apikeys), then open **Fliar Prism workspace → API keys**. Once enabled for your account, create a key and copy it when shown. If the control is unavailable, request preview access from Fliar.
2. Set `API_BASE` to the News API base URL supplied with your access and `PRISM_API_KEY` to your issued key. Keep the key private.
3. Check your access, then search:

```bash
curl -sS "$API_BASE/v1/me" -H "X-API-Key: $PRISM_API_KEY"

curl -sS --get "$API_BASE/v1/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=electric vehicle' \
  --data-urlencode 'sentiment=negative' \
  --data-urlencode 'priority_min=7' \
  --data-urlencode 'classes=0' \
  --data-urlencode 'limit=100'
```

GCP code `0` means `/News/Business News/Company News`. Filters combine, so a narrow request can return `404 no_data`. Start with `q` alone if needed. `Authorization: Bearer YOUR_API_KEY` is also accepted.

```python
import os
import requests

response = requests.get(
    os.environ["API_BASE"].rstrip("/") + "/v1/headlines",
    headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
    params={"q": "electric vehicle", "limit": 100},
    timeout=60,
)
payload = response.json()
if not response.ok or not payload.get("ok"):
    raise RuntimeError(f"HTTP {response.status_code}: {payload.get('error')}")
print(payload["window"], payload["meta"].get("notes", []))
for article in payload["data"]["items"]:
    print(article["headline"], article["url"])
```

## Choose a workflow

| Goal | Start here |
|---|---|
| Understand a subject | `/v1/overview`, then `/v1/headlines` |
| Discover themes | `/v1/themes` with required `q`; at most **5** results |
| Read a selected theme | `/v1/themes/{name}/headlines`; **100** per page by default |
| Compare subjects | `POST /v1/compare` with **2–5** named filter sets |
| Inspect tone, importance or volume | `/v1/sentiment`, `/v1/priority`, `/v1/trends` |
| Explore location and availability | `/v1/geography` with required `q` and at most **5** results; `/v1/coverage` |
| Retrieve full text | `/v1/articles/{article_id}` or `POST /v1/export`, **100** per batch by default |

Headline and export requests default to 100; higher limits depend on your plan. Check `/v1/me` for your caps.

Read the **[User guide](docs/USER_GUIDE.md)** for authentication, filters, theme drilldown, pagination, exports, comparisons, freshness, quotas, errors and the endpoint reference. The guide is also served as Markdown at `/guide` on your supplied API base. For company events and funding, see the [Business News API guide](https://github.com/fliarbi/prism-business-news-api/blob/main/docs/USER_GUIDE.md).

<!-- demos:start -->
## See the API in a research UI

[6 animated Claude Code / Codex workflow concepts](docs/ANIMATED_USE_CASES.md) show
what an assistant can build on this API. They cover theme discovery, a weekly sentiment shift, comparing two topics, critical alerts, GCP content-class codes and full-article export. Each GIF labels saved API
responses or illustrative data; these are client-built UI concepts, not recordings of
official client interfaces or claims of live service availability. Open the
[interactive gallery](docs/demos/index.html) locally for prompts and request recipes.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>EV theme discovery</h3>
      <a href="docs/demos/media/ev-theme-discovery.gif"><img src="docs/demos/media/ev-theme-discovery.gif" width="420" alt="Discover the themes behind a topic"></a>
      <p>Ask a broad topic, get ranked themes, then open the coverage behind the strongest one. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Tariff sentiment shift</h3>
      <a href="docs/demos/media/tariff-sentiment.gif"><img src="docs/demos/media/tariff-sentiment.gif" width="420" alt="Watch the tone of a story change week by week"></a>
      <p>See when a story turned, how far it moved from the archive norm, and which headlines drove it. Saved API responses.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Compare two topics</h3>
      <a href="docs/demos/media/ai-topic-compare.gif"><img src="docs/demos/media/ai-topic-compare.gif" width="420" alt="Compare two narratives over the same window"></a>
      <p>Put two narratives on one scale, with exact overlap and per-topic criticality. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Critical news alerts</h3>
      <a href="docs/demos/media/critical-alerts.gif"><img src="docs/demos/media/critical-alerts.gif" width="420" alt="Surface the critical stories in a busy topic"></a>
      <p>Quantify how much of a topic is urgent, then read just those stories. Saved API responses.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>GCP class code map</h3>
      <a href="docs/demos/media/class-code-map.gif"><img src="docs/demos/media/class-code-map.gif" width="420" alt="Turn a topic into GCP content-class codes"></a>
      <p>Find the right content-class codes by name, then filter any endpoint by them. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Full articles to CSV</h3>
      <a href="docs/demos/media/full-article-export.gif"><img src="docs/demos/media/full-article-export.gif" width="420" alt="Export full article text to a spreadsheet"></a>
      <p>Move from a filter to full article text in a file your analysis tools can read. Saved API responses.</p>
    </td>
  </tr>
</table>
<!-- demos:end -->

## Running the service

Copy `.env.example` to `.env` and fill in the deployment's addresses, credentials and table names. `.env` is never committed. Then:

```bash
pip install -r requirements.txt
./run.sh --bg        # gunicorn on :8800, logs under logs/
python3 -m pytest -q # offline tests, no data stores needed
```
