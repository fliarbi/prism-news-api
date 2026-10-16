# Getting started with the Prism News API

[README](../README.md) · [Demonstrations](scenarios/README.md) · [User guide](USER_GUIDE.md)

This page takes you from no key to a working research query in about five minutes,
then lists every command of the `prism-news` client.

## 1. Get a key

Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi) and open
**API keys** (it is in both the Radar and the Fliar Prism workspace), then choose
**Create or manage API keys**. On the key page, choose **Connect Radar session**, enter an
application name, pick **All data** or **News only** access and an expiry, and create the
key. Copy it when shown; it is displayed once.

The key starts with `rdr_` and works on the Prism News API, the Prism Business News API
and the Radar API. Each API meters its own usage; the two News APIs share one monthly
quota. Older `pna_` keys keep working.

## 2. Install the client in one line

Requires Bash, curl and Python 3.8+ (standard library only).

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/prism-news-api/main/scripts/install.sh | bash
```

| Installer setting | Default | Meaning |
|---|---|---|
| `GH_TOKEN` | — | Only for installing from a private fork; read from stdin by curl, never written to disk |
| `PRISM_BIN_DIR` | `~/.local/bin` | Where `prism-news` and `prism-business-news` are placed |
| `PRISM_REF` | `main` | Branch, tag or commit to install |
| `PRISM_REPO` | `fliarbi/prism-news-api` | Repository to download the client from |

The installer downloads one file (`scripts/prism_cli.py`) to `~/.local/share/prism-cli/`,
compiles it as a check, and writes two small launchers. It never uses sudo, edits shell
profiles or starts a service. Run `bash install.sh --help` for the same table.

**Without the installer:** download `scripts/prism_cli.py` and run
`PRISM_CLI_PRODUCT=prism-news python3 prism_cli.py status`.

**Uninstall:** `rm ~/.local/bin/prism-news ~/.local/bin/prism-business-news && rm -r ~/.local/share/prism-cli ~/.config/prism`.

## 3. Log in once

```bash
prism-news login
```

You are asked for the News and Business News base URLs (press Enter for `https://radar-api.fliarbi.com/news` and `https://radar-api.fliarbi.com/business-news`) and your key (hidden input). The
client checks the key with `GET /v1/me` before saving anything, then stores it in
`~/.config/prism/config.json` with owner-only permissions.

| Environment variable | Overrides |
|---|---|
| `PRISM_API_KEY` | The saved key |
| `PRISM_API_BASE` | The saved News API base URL |
| `PRISM_BUSINESS_API_BASE` | The saved Business News API base URL |

`prism-news logout` removes the saved key.

## 4. Check access and make a first query

```bash
prism-news status        # service readiness and the data's latest date
prism-news me            # plan, limits and this month's usage
prism-news headlines "electric vehicle" --since 2026-01-01 --until 2026-04-30 --limit 10 --table
```

## 5. Copy a demonstration

Every [demonstration page](scenarios/README.md) ends with its exact commands. Copy them
and change the subject:

```bash
prism-news overview "cement industry" --since 2026-01-01 --until 2026-04-30
prism-news trends "cement industry" --since 2025-05-01 --until 2026-04-30 --granularity monthly --table
prism-news geography "cement industry" --since 2026-01-01 --until 2026-04-30 --table
prism-news themes "cement industry" --since 2026-01-01 --until 2026-04-30 --table
prism-news headlines "cement industry" --match focused --priority-min 6 --sort priority --limit 25 --table
```

## How options become requests

| You type | The request gets |
|---|---|
| A quoted phrase after the command | `q` |
| `--priority-min 7` | `priority_min: 7` (dashes become underscores; numbers and true/false are typed) |
| `--sentiment negative --sentiment neutral` | `sentiment: ["negative", "neutral"]` |
| `--json '{"queries": [...]}'` | That JSON body, merged with any other options |
| `--cursor <value>` | The next page; the client prints the value under a `--table` |
| `--table` | A compact table of the returned items instead of JSON |
| `-o file.csv` | The raw response written to a file (`export` picks the format from the extension) |

Exit status is 0 on success and 1 on an API error, so the commands work in scripts.

<!-- cli:start -->
## Command reference

| Command | Request | Typical use |
|---|---|---|
| `prism-news article ID` | `GET /v1/articles/{arg}` | One full article (1 export) |
| `prism-news class ID` | `GET /v1/classes/{arg}` | A GCP content class and its recent coverage |
| `prism-news class-headlines ID` | `GET /v1/classes/{arg}/headlines` | Headlines under one class |
| `prism-news classes "phrase"` | `GET /v1/classes` | Find up to five GCP content class codes |
| `prism-news compare --json '{...}'` | `POST /v1/compare` | Compare 2–5 named filter sets |
| `prism-news coverage "phrase"` | `POST /v1/coverage` | Sentiment, theme and location availability |
| `prism-news export "phrase"` | `POST /v1/export` | Full article bodies as json, ndjson or csv |
| `prism-news geography "phrase"` | `POST /v1/geography` | Top five countries |
| `prism-news headlines "phrase"` | `POST /v1/headlines` | Headlines for a filter set |
| `prism-news me` | `GET /v1/me` | Your key, plan, limits and usage |
| `prism-news overview "phrase"` | `POST /v1/overview` | Article count, tone and critical share |
| `prism-news priority "phrase"` | `POST /v1/priority` | Priority distribution against the archive |
| `prism-news related ID` | `GET /v1/articles/{arg}/related` | Related headlines |
| `prism-news sentiment "phrase"` | `POST /v1/sentiment` | Sentiment distribution and timeline |
| `prism-news status` | `GET /v1/status` | Service readiness and data dates |
| `prism-news theme-headlines NAME` | `GET /v1/themes/{arg}/headlines` | Headlines carrying one theme |
| `prism-news themes "phrase"` | `POST /v1/themes` | Themes ranked by lift |
| `prism-news trends "phrase"` | `POST /v1/trends` | Article volume over time |
| `prism-news vocabulary` | `GET /v1/vocabulary` | Sentiments, priority bands and options |
| `prism-news call METHOD PATH [JSON]` | any | Any endpoint, including new ones |
| `prism-news login` / `logout` | — | Save or remove your key |
<!-- cli:end -->

## Troubleshooting

| Message | What to do |
|---|---|
| `Not configured` | Run `prism-news login`, or set `PRISM_API_BASE` and `PRISM_API_KEY` |
| `command not found` | Add `~/.local/bin` to your `PATH`, or run it by full path |
| `401 unauthenticated` / `invalid_key` | The key is wrong or revoked; create a new one in the dashboard and log in again |
| `402 quota_exceeded` | Check `prism-news me`; the quota resets monthly |
| `404 no_data` | The filters matched nothing in the window; drop a filter or widen the dates |
| `429 rate_limited` | Wait for `Retry-After` and lower concurrency |
| `503 coverage_unavailable` | Part of the archive is offline; retry later and do not record the result as zero |
| Download failed during install | Check your connection to github.com; a private fork also needs `GH_TOKEN` with Contents: read |

The full API contract (filters, pagination, exports, errors) is in the [User guide](USER_GUIDE.md).
