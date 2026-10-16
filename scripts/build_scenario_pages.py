#!/usr/bin/env python3
"""Render the demonstration pages from saved captures.

Writes docs/scenarios/<segment>/<slug>.md for every kept scenario, one index per
segment, docs/scenarios/README.md, docs/research/KEYWORD_RESEARCH.md and the
demonstrations section at the top of README.md. Every number on a page comes from
a saved response in docs/examples/scenarios/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scenario_common as sc  # noqa: E402
from scenario_common import bar, day, esc, month, n, pct, table, title_case, trim  # noqa: E402

PRODUCT, CLI = "Prism News API", "prism-news"
SEGMENTS = {
    "industry-research": ("Industry research", "Track a sector's news volume, tone, critical stories, locations and emerging themes: market sizing desks, strategy teams, trade associations and analysts covering steel, textiles, pharma, autos or any other industry."),
    "financial-research": ("Financial research", "Follow markets, rates, currencies, commodities, crypto and policy-driven finance stories with tone and priority signals: equity research, treasury, fintech product and newsroom teams."),
    "disease-health": ("Disease and health research", "Monitor outbreak and disease coverage by month and country, with critical headlines and the themes reporters attach: public-health analysts, pharma intelligence, insurers and health journalists."),
    "policy-regulation": ("Policy and regulation research", "Watch tariffs, sanctions, AI rules, tax and sector regulation as they move through the news: policy, compliance, government-affairs and risk teams."),
    "technology-ai": ("Technology and AI research", "Measure coverage of AI, chips, cloud, cybersecurity, platforms and devices with themes and critical headlines: product strategy, competitive intelligence and tech journalists."),
    "energy-climate": ("Energy and climate research", "Follow energy markets, renewables, fuels, weather extremes and climate policy coverage over twelve months: energy analysts, ESG and sustainability teams and commodity desks."),
}
QUESTION = {
    "industry-research": "How much news did {t} receive between January and April 2026, how critical and how negative was it, where was it reported, and which themes stood out?",
    "financial-research": "What did the news say about {t} between January and April 2026: volume, tone, critical share, locations, themes and the most consequential headlines?",
    "disease-health": "How much {t} coverage appeared between January and April 2026, in which countries, how critical was it, and which themes did reporters attach?",
    "policy-regulation": "How did coverage of {t} develop over twelve months, how negative and critical was it in January–April 2026, and which themes and headlines led?",
    "technology-ai": "How much {t} coverage appeared between January and April 2026, how did it trend over twelve months, and which themes and critical headlines stood out?",
    "energy-climate": "How did {t} coverage move over twelve months, how critical and negative was it in January–April 2026, where was it reported, and which themes led?",
}


def subject(s: dict) -> str:
    t = s["topic"]
    return f"the {t} industry" if s["segment"] == "industry-research" and s["q"].endswith(" industry") else t


def headline_rows(items: list[dict], q: str) -> tuple[list[list], int]:
    words = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if w not in {"industry", "and", "the", "of"}] or [q.lower()]
    seen, rows, flagged = set(), [], 0
    for it in items:
        key = it["headline"].lower().strip()
        if key in seen or len(rows) == 12:
            continue
        seen.add(key)
        text = (it["headline"] + " " + (it.get("lede") or "")).lower()
        mark = "" if any(re.search(rf"\b{re.escape(w)}", text) for w in words) else " ⚠"
        flagged += bool(mark)
        rows.append([day(it["published_at"]), f"[{esc(trim(it['headline'], 110))}]({it['url']}){mark}",
                     esc(it["publisher"]), it.get("priority") or "—", (it.get("sentiment") or {}).get("group", "—")])
    return rows, flagged


def run_it(s: dict) -> str:
    ov = next(c for c in s["calls"] if c["name"] == "overview")["body"]
    hl = next(c for c in s["calls"] if c["name"] == "headlines")["body"]
    q = ov["q"]
    return f"""## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
{CLI} overview "{q}" --since {ov['since']} --until {ov['until']}
{CLI} trends "{q}" --since 2025-05-01 --until 2026-04-30 --granularity monthly
{CLI} headlines "{q}" --since {hl['since']} --until {hl['until']} --match focused --priority-min 6 --sort priority --limit 25
```

Or with curl (each request below is one of the five captured calls):

```bash
curl -sS "$API_BASE/v1/overview" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \\
  -d '{json.dumps(ov)}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/headlines", headers={{"X-API-Key": os.environ["PRISM_API_KEY"]}},
                  json={json.dumps(hl)}, timeout=60)
for a in r.json()["data"]["items"]:
    print(a["published_at"][:10], a["priority"], a["headline"])
```
"""


def page(s: dict, rec: dict, related: list[dict]) -> str:
    seg = s["segment"]
    seg_title = SEGMENTS[seg][0]
    ov, tr, geo, th, hl = (sc.response(rec, k) for k in ("overview", "trends", "geography", "themes", "headlines"))
    subj = subject(s)
    h1 = title_case(s["keyword"]["phrase"])
    if "news" not in h1.lower():
        h1 += " News"
    tone = {g["group"]: g for g in (ov.get("tone") or {}).get("groups") or []}
    crit = ov.get("critical") or {}
    pts = tr.get("points") or []
    peak = max(pts, key=lambda p: p["articles"]) if pts else None
    geo_items = geo.get("items") or []
    themes = th.get("items") or []
    rows, flagged = headline_rows(hl.get("items") or [], s["q"])
    unresolved = hl.get("unresolved") or 0

    glance = [["Matching articles, 1 Jan – 30 Apr 2026", n(ov.get("matched"))]]
    if tone:
        glance.append(["Negative · neutral · positive", " · ".join(pct(tone.get(g, {}).get("share_pct")) for g in ("negative", "neutral", "positive"))])
    if crit:
        glance.append(["Critical (priority 7–9)", f"{pct(crit.get('share_pct'))} ({n(crit.get('count'))} articles)"])
    if peak:
        glance.append(["Busiest month, May 2025 – Apr 2026", f"{month(peak['period'])} ({n(peak['articles'])} articles)"])
    if geo_items:
        glance.append(["Most-reported country", f"{title_case(geo_items[0]['country'])} ({pct(geo_items[0]['share_pct'])} of matches)"])
    if themes:
        glance.append(["Strongest theme by lift", esc(themes[0]["theme"])])

    out = [f"# {h1}: volume, tone and critical headlines (Jan–Apr 2026)", "",
           f"[{seg_title}](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)", "",
           f"> **Search demand:** {sc.search_line(s)}  ",
           f"> **Data:** {sc.coverage_line(rec)}. Five saved API responses: [{s['slug']}.json](../../examples/scenarios/{s['slug']}.json).", "",
           f"**Question.** {QUESTION[seg].format(t=subj)}", "",
           f"**Request.** `q=\"{s['q']}\"` on `/v1/overview`, `/v1/trends`, `/v1/geography`, `/v1/themes` and `/v1/headlines`.", "",
           "## At a glance", "", table(["Measure", "Value"], glance, "lr"), ""]

    if pts:
        top = max(p["articles"] for p in pts)
        out += ["## Twelve months of coverage", "",
                f"Monthly matching articles for `{s['q']}` (`POST /v1/trends`, `granularity=monthly`).", "",
                table(["Month", "Articles", "Critical", "Negative", "Positive", ""],
                      [[month(p["period"]) + (" (partial)" if p.get("partial_period") else ""), n(p["articles"]),
                        pct(p.get("critical_pct")), n(p.get("negative")), n(p.get("positive")), bar(p["articles"], top)]
                       for p in pts], "lrrrrl"), ""]
        first = [p for p in pts if not p.get("partial_period")]
        if len(first) >= 8:
            early = sum(p["articles"] for p in first[:4]) / 4
            late = sum(p["articles"] for p in first[-4:]) / 4
            if early:
                out += [f"The last four complete months averaged {n(round(late))} articles a month against {n(round(early))} in the first four ({late / early - 1:+.0%}). "
                        "News intake also varies by month, so treat changes as coverage signals rather than event counts.", ""]
    if geo_items:
        out += ["## Where it was reported", "",
                f"Top five countries (`POST /v1/geography`). {pct(geo.get('availability_pct'))} of matching articles carry a location.", "",
                table(["Country", "Articles", "Share of all matches"],
                      [[title_case(g["country"]), n(g["count"]), pct(g["share_pct"])] for g in geo_items], "lrr"), ""]
    if themes:
        out += ["## Themes that stood out", "",
                f"Ranked by lift over each theme's share of all news (`POST /v1/themes`). Change compares with {day(th['previous_period']['since'])} – {day(th['previous_period']['until'])}." if th.get("previous_period") else "Ranked by lift (`POST /v1/themes`).", "",
                table(["Theme", "Articles", "Share", "Change vs previous period"],
                      [[esc(t["theme"]), n(t["count"]), pct(t["share"]),
                        "new" if t.get("new_vs_baseline") and t.get("delta_pct") is None else (f"{t['delta_pct']:+.0f}%" if t.get("delta_pct") is not None else "—")]
                       for t in themes], "lrrr"), "",
                "Lift compares with the most recent 30 days of all news, which are thin (intake slows after May 2026), so very large lift values mostly reflect that small baseline. Use the ranking, not the size of the lift.", ""]
    out += ["## Critical headlines", "",
            "Priority 6 and above, `match=focused`, sorted by priority (`POST /v1/headlines`, limit 25; up to 12 distinct headlines shown)."
            + (f" {unresolved} of the requested articles were temporarily unavailable from the article store at capture time, so fewer rows are shown." if unresolved else ""), ""]
    if rows:
        out += [table(["Date", "Headline", "Publisher", "Priority", "Tone"], rows, "llllr"), ""]
        if flagged:
            out += ["⚠ The subject phrase does not appear in that headline or its opening text; the article matched on its tags or entities. Read it before relying on it.", ""]
    else:
        out += ["No headline could be shown: the matching articles were unavailable from the article store at capture time. Counts above are unaffected.", ""]
    out += [run_it(s), "## Read the result carefully", ""]
    caveats = [f"Window: 1 Jan – 30 Apr 2026 for counts, tone, locations, themes and headlines; May 2025 – Apr 2026 for the monthly series. Data runs through {day((sc.call_of(rec, 'overview')['response'].get('window') or {}).get('data_through'))}; intake thins after May 2026.",
               "`q` matches the opening text, article tags and named organisations or people, so broad words match broadly. Add `match=focused` or other filters to narrow it."]
    if rec.get("coverage_note"):
        caveats.append(f"Captured while part of the news index was offline ({rec['coverage_note']}). Every count is a lower bound.")
    caveats += [esc(x) for x in sc.notes(rec) if "unavailable" not in x.lower()]
    out += [f"- {c}" for c in caveats] + [""]
    out += ["## Related demonstrations", ""] + [f"- [{title_case(r['keyword']['phrase'])}]({r['slug']}.md)" for r in related] + [""]
    return "\n".join(out)


def segment_index(seg: dict, kept: list[dict], recs: dict) -> str:
    title, blurb = SEGMENTS[seg["id"]]
    rows = []
    for i, s in enumerate(kept, 1):
        ov = sc.response(recs[s["slug"]], "overview")
        crit = (ov.get("critical") or {}).get("share_pct")
        neg = next((g["share_pct"] for g in (ov.get("tone") or {}).get("groups") or [] if g["group"] == "negative"), None)
        v = s["keyword"]["volume"]
        rows.append([i, f"[{title_case(s['keyword']['phrase'])}]({s['slug']}.md)", f"`{esc(s['q'])}`",
                     n(v.get("in") or None), n(v.get("us") or None), n(ov.get("matched")), pct(neg), pct(crit)])
    return f"""# {title}: {len(kept)} worked demonstrations

[All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

{blurb}

Each page answers one researched search query with five live API responses: an overview,
a twelve-month monthly series, the top five countries, the strongest themes and the
critical headlines, plus the exact CLI, curl and Python requests. Pages are ordered by
search demand (India + US monthly searches for the target phrase and its variant).

| # | Demonstration | `q` | India searches/mo | US searches/mo | Articles Jan–Apr 2026 | Negative | Critical |
|---:|---|---|---:|---:|---:|---:|---:|
""" + "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in rows) + "\n"


def main() -> None:
    plan = json.loads(sc.PLAN.read_text())
    log = json.loads(sc.LOG.read_text())
    summary = []
    for seg in plan["segments"]:
        kept = [s for s in seg["scenarios"] if log.get(s["slug"], {}).get("kept")]
        recs = {s["slug"]: sc.load_capture(s["slug"]) for s in kept}
        d = sc.SCEN / seg["id"]
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        for i, s in enumerate(kept):
            related = [kept[j] for j in (i - 2, i - 1, i + 1, i + 2) if 0 <= j < len(kept) and j != i][:4]
            (d / f"{s['slug']}.md").write_text(page(s, recs[s["slug"]], related))
        (d / "README.md").write_text(segment_index(seg, kept, recs))
        summary.append((seg, kept, recs))
    write_hub(plan, summary)
    write_research(plan, log)
    write_readme(summary)
    print({seg["id"]: len(kept) for seg, kept, _ in summary})


def write_hub(plan: dict, summary: list) -> None:
    total = sum(len(k) for _, k, _ in summary)
    rows = []
    for seg, kept, recs in summary:
        top = ", ".join(f"[{title_case(s['keyword']['phrase'])}]({seg['id']}/{s['slug']}.md)" for s in kept[:3])
        rows.append([f"[{SEGMENTS[seg['id']][0]}]({seg['id']}/README.md)", len(kept), top])
    when = min(r["captured_at"] for _, _, recs in summary for r in recs.values())
    (sc.SCEN / "README.md").write_text(f"""# {PRODUCT} demonstrations: {total} worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [User guide](../USER_GUIDE.md) · [Animated gallery](../ANIMATED_USE_CASES.md)

Each demonstration answers one real search query with saved responses from the live API:
coverage volume and tone, a twelve-month series, countries, themes and critical
headlines, with the exact requests to reproduce it. Topics were chosen by
[keyword research](../research/KEYWORD_RESEARCH.md) (India and US monthly searches) and kept
only when the API returned populated results.

{table(["Segment", "Pages", "Highest-demand pages"], rows, "lrl")}

Captured {day(when)} from the live API. Part of the news index was offline (1 of 14 shards,
about 93% of rows available), so every count is a lower bound; some headlines were
temporarily unavailable from the article store and each page says how many.

Regenerate: `scripts/plan_scenarios.py` → `scripts/capture_scenarios.py` → `scripts/build_scenario_pages.py`.
""")


def write_research(plan: dict, log: dict) -> None:
    research = json.loads((sc.RESEARCH / plan["research"]).read_text())
    out = [f"# Keyword research for the demonstration pages", "",
           f"[All demonstrations](../scenarios/README.md) · [Raw data]({plan['research']})", "",
           f"Research date **{research['date']}**. {research['volume']}", "", research["method"], "",
           "Status: **page** = built; **thin** = captured but below the populated threshold; **excluded** = overlap or ambiguous query (reason shown); **not reached** = the segment already had its pages.", ""]
    for seg in research["segments"]:
        title = SEGMENTS[seg["id"]][0]
        rows = []
        for t in seg["topics"]:
            slug = sc.slugify(t["target"]["phrase"])
            entry = log.get(slug)
            if t.get("excluded"):
                status = f"excluded: {t['excluded']}"
            elif entry and entry.get("kept"):
                status = f"[page]({'../scenarios/' + seg['id'] + '/' + slug + '.md'})"
            elif entry:
                status = "not reached" if entry["why"] == "segment target reached" else f"thin ({esc(entry['why'])})"
            else:
                status = "not reached"
            ph = t["phrases"]
            rows.append([esc(t["topic"]), *(f"{esc(p['phrase'])}: {n(p['volume']['in'])} / {n(p['volume']['us'])}" for p in ph),
                         n(t["score"]), status])
        out += [f"## {title}", "", f"Phrases: {' and '.join('`' + v + '`' for v in seg['variants'])}. Volumes are India / US monthly searches.", "",
                table(["Topic", "Phrase 1", "Phrase 2", "Score", "Status"], rows, "lllrl"), ""]
    (sc.RESEARCH / "KEYWORD_RESEARCH.md").write_text("\n".join(out))


def write_readme(summary: list) -> None:
    total = sum(len(k) for _, k, _ in summary)
    rows = []
    for seg, kept, recs in summary:
        picks = " · ".join(f"[{title_case(s['topic'])}](docs/scenarios/{seg['id']}/{s['slug']}.md)" for s in kept[:4])
        rows.append([f"**[{SEGMENTS[seg['id']][0]}](docs/scenarios/{seg['id']}/README.md)**", len(kept), picks])
    section = f"""{sc.README_START}
## {total} worked demonstrations

Real questions, real responses: each page answers one researched search query with
saved live API output: volume, tone, a twelve-month series, countries, themes and
critical headlines, plus the exact CLI, curl and Python calls.
[Browse all {total}](docs/scenarios/README.md) or start with a segment:

{table(["Segment", "Pages", "Start with"], rows, "lrl")}

Topics come from [keyword research](docs/research/KEYWORD_RESEARCH.md) (India and US monthly searches).
Captured with 1 of 14 news-index shards offline, so counts are lower bounds.
{sc.README_END}"""
    readme = sc.ROOT / "README.md"
    readme.write_text(sc.replace_section(readme.read_text(), section, sc.README_START, sc.README_END,
                                         "## Get access and make a first request"))


if __name__ == "__main__":
    main()
