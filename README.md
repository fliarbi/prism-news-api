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

## Running the service

Copy `.env.example` to `.env` and fill in the deployment's addresses, credentials and table names. `.env` is never committed. Then:

```bash
pip install -r requirements.txt
./run.sh --bg        # gunicorn on :8800, logs under logs/
python3 -m pytest -q # offline tests, no data stores needed
```
