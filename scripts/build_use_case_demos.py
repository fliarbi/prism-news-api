#!/usr/bin/env python3
"""Build source-qualified UI animation stories from saved responses; no live calls.

Every chart is computed from docs/examples/demo/*.json. A file is either a real
capture (scripts/capture_demo_examples.py) or an illustrative fixture in the
same response shape (scripts/illustrative_demo_fixtures.py); the story's badge
follows the files it reads. Every request body is validated with the API's own
request models before it is written into a recipe.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from demo_common import captured_on, coverage_note, day, evidence, kind_of, local, read, trim, write_outputs  # noqa: E402
from prism_news_api.features.explore import CompareRequest  # noqa: E402
from prism_news_api.features.export import ExportRequest  # noqa: E402
from prism_news_api.filters import Filters  # noqa: E402
from prism_news_api.routers import FiltersWithGranularity, ThemeFilters  # noqa: E402

GUIDE = "../USER_GUIDE.md"
MODELS = {"/v1/themes": ThemeFilters, "/v1/headlines": Filters, "/v1/sentiment": FiltersWithGranularity,
          "/v1/trends": FiltersWithGranularity, "/v1/priority": Filters, "/v1/compare": CompareRequest,
          "/v1/export": ExportRequest}
TONE = {"negative": "negative", "positive": "positive", "neutral": "neutral"}


def validate(path: str, body: dict) -> None:
    """Raise unless the API itself would accept this request body."""
    if path in MODELS:
        MODELS[path].model_validate(body)
    else:
        assert path == "/v1/classes" and 2 <= len(body["q"]) <= 120 and 1 <= body["limit"] <= 5, path


def step(name: str, label: str) -> dict:
    req = read(name)["request"]
    validate(req["path"], req["body"])
    return {"type": "api", "method": req["method"], "path": req["path"], "body": req["body"], "label": label}


def badge(names: list[str], fiction: str) -> tuple[str, str]:
    kind = kind_of(names)
    if kind != "captured":
        return kind, f"Illustrative data · {fiction}"
    note = coverage_note(names)
    return kind, f"Captured data · {captured_on(names)}" + (f" · {note.split(' (')[0]}" if note else "")


def data(name: str) -> dict:
    return read(name)["response"]["data"]


def week(iso: str) -> str:
    return day(iso)


def label(theme: str) -> str:
    text = re.sub(r"\b(ev|hev|ai|ipo|suv)\b", lambda m: m.group(1).upper(), theme)
    return trim(text[:1].upper() + text[1:], 40)


def unique(items: list[dict]) -> list[dict]:
    """Drop repeated headlines from one publisher (republished copies)."""
    seen, out = set(), []
    for a in items:
        key = (a["publisher"], a["headline"].strip().lower())
        if key not in seen:
            seen.add(key)
            out.append(a)
    return out


def trend_note(reg: dict, inv: dict) -> str:
    def half(t):
        pts = [p["articles"] for p in t["points"]]
        a, b = sum(pts[: len(pts) // 2]), sum(pts[len(pts) // 2:])
        return (b - a) / a * 100 if a else None
    r, i = half(reg), half(inv)
    return (f"Second half vs first half of the window: AI regulation {r:+.0f}%, AI investment {i:+.0f}%. "
            "Overlapping articles are counted once in the union.")


def missing(d: dict) -> str:
    return f" {d['unresolved']} matching article(s) were unavailable from the article store at capture." if d.get("unresolved") else ""


def card(a: dict) -> dict:
    s = a.get("sentiment") or {}
    tags = [{"text": s.get("label", "no sentiment").replace("_", " "), "tone": TONE.get(s.get("group"), "neutral")}]
    if a.get("priority"):
        tags.append({"text": f"priority {a['priority']}", "tone": "warn" if a["priority"] >= 7 else ""})
    tags += [{"text": f"class {c['code']}", "tone": ""} for c in (a.get("classes") or [])[:1]]
    return {"headline": a["headline"], "meta": f"{a['publisher']} · {day(a['published_at'])}", "tags": tags}


def story(id, names, fiction, **kw):
    kind, label = badge(names, fiction)
    note = coverage_note(names) if kind == "captured" else None
    if note:
        why = note.split("(", 1)[1].rstrip(")") if "(" in note else note
        kw["footnote"] = f"Lower-bound counts ({why}). " + kw["footnote"]
    return {"id": id, "brand": "Prism News", "kind": kind, "badge": label, "sources": evidence(names), **kw}


def provenance(stories: list[dict]) -> str:
    out = "Green badges cite saved responses of the real API, captured on the date shown."
    notes = {coverage_note([src["file"].rsplit("/", 1)[1][:-5]]) for st in stories for src in st["sources"] if src["kind"] == "captured"} - {None}
    if notes:
        out += (f" These were captured while part of the archive was offline ({'; '.join(sorted(notes))}), so counts "
                "are lower bounds, and some articles could not be fetched; each demo says how many.")
    if any(st["kind"] == "illustrative" for st in stories):
        out += (" Purple badges mark illustrative fixtures: fictional articles, publishers (.example domains) and counts in the "
                "exact response shape. Rerunning scripts/capture_demo_examples.py replaces them with real captures.")
    return out


def build() -> None:
    stories = []

    themes, theme_heads = data("ev-themes"), data("ev-theme-headlines")
    top = themes["items"][0]["theme"]
    stories.append(story(
        "ev-theme-discovery", ["ev-themes", "ev-theme-headlines"], "fictional articles and counts",
        nav="EV theme discovery", client="Claude Code", heading="Find what drives a topic",
        title="Discover the themes behind a topic",
        prompt="What is driving electric vehicle news in March and April 2026? Rank the themes, then show me the headlines behind the strongest one.",
        steps=[step("ev-themes", "Discover up to five themes"), step("ev-theme-headlines", "Read the selected theme's headlines"),
               local("Chart lift and support", "Client-side ranking view")],
        overview={"type": "bars", "title": "Five themes behind electric-vehicle coverage", "labelWidth": 500,
                  "subtitle": f"Ranked by lift over the 30-day archive share · {themes['matched']:,} matching articles",
                  "axisLabel": "Lift: theme share vs archive share",
                  "rows": [{"label": label(t["theme"]), "sub": f"{t['count']:,} articles" + (f" · {t['delta_pct']:+.0f}% vs previous period" if t["delta_pct"] is not None else ""),
                            "value": t["lift"] or 0, "display": f"{t['lift']:.0f}× lift" if t["lift"] else "new vs baseline"} for t in themes["items"]],
                  "stats": [{"value": f"{themes['matched']:,}", "label": "matching articles"},
                            {"value": f"{themes['carrying']:,}", "label": "carry theme labels"},
                            {"value": f"{themes['carrier_share_pct']:.0f}%", "label": "theme coverage"},
                            {"value": "5", "label": "suggestions (discovery cap)"}]},
        detail={"type": "cards", "title": f"Headlines for “{top}”",
                "subtitle": f"{theme_heads['total_estimate']:,} matching headlines · newest first · sentiment and priority kept",
                "items": [card(a) for a in unique(theme_heads["items"])[:4]],
                "note": "Headlines omit theme metadata; the theme was selected through discovery and passed as a filter." + missing(theme_heads)},
        footnote="Lift compares with a 30-day archive baseline ending at data_through, when ingest is thin; it is relative prominence, not reliability.",
        takeaway="Ask a broad topic, get ranked themes, then open the coverage behind the strongest one.",
        evidence_summary="Theme discovery plus headlines for the top theme",
        guide=f"{GUIDE}#discover-themes-and-read-articles"))

    sent, neg = data("tariff-sentiment"), data("tariff-negative-headlines")
    tl = sent["timeline"]
    peak = max(tl, key=lambda p: p["negative"])
    groups = {g["group"]: g for g in sent["groups"]}
    stories.append(story(
        "tariff-sentiment", ["tariff-sentiment", "tariff-negative-headlines"], "fictional articles and counts",
        nav="Tariff sentiment shift", client="Codex", heading="Track how coverage turns",
        title="Watch the tone of a story change week by week",
        prompt="Track the tone of tariff coverage week by week from March to April 2026. When was it most negative, and which important headlines carried that tone?",
        steps=[step("tariff-sentiment", "Weekly sentiment timeline"), step("tariff-negative-headlines", "Negative headlines, priority 6+"),
               local("Mark the turning point", "Client compares weekly negative shares")],
        overview={"type": "columns", "stacked": True, "title": "Tariff coverage by tone, week by week",
                  "subtitle": "Articles carrying a sentiment label · weekly buckets starting Monday",
                  "labels": [week(p["period"]) for p in tl], "unit": "articles per week",
                  "series": [{"name": "Negative", "tone": "negative", "values": [p["negative"] for p in tl]},
                             {"name": "Neutral", "tone": "neutral", "values": [p["neutral"] for p in tl]},
                             {"name": "Positive", "tone": "positive", "values": [p["positive"] for p in tl]}],
                  "height": 270,
                  "stats": [{"value": f"{sent['matched']:,}", "label": "matching articles"},
                            {"value": f"{groups['negative']['share']:.0f}%", "label": "negative share"},
                            {"value": f"{sent['negative_to_positive_ratio']:.2f} : 1", "label": "negative to positive"},
                            {"value": week(peak["period"]), "label": f"peak negative week ({peak['negative_share']:.0f}%)"}]},
        detail={"type": "cards", "title": "Negative tariff headlines that mattered",
                "subtitle": "sentiment = negative · priority ≥ 6 · same window · newest first",
                "items": [card(a) for a in unique(neg["items"])[:4]],
                "note": f"Baseline negative-to-positive ratio is {sent['baseline']['negative_to_positive_ratio']}; this window runs {sent['vs_baseline_ratio']}× the archive norm." + missing(neg)},
        footnote="Shares divide by articles carrying a sentiment label. A recent decline can reflect thinner coverage.",
        takeaway="See when a story turned, how far it moved from the archive norm, and which headlines drove it.",
        evidence_summary="Weekly sentiment timeline plus negative headlines",
        guide=f"{GUIDE}#tone-priority-and-trends"))

    cmp_, reg, inv = data("ai-compare"), data("ai-regulation-trends"), data("ai-investment-trends")
    items = {i["name"]: i for i in cmp_["items"]}
    stories.append(story(
        "ai-topic-compare", ["ai-compare", "ai-regulation-trends", "ai-investment-trends"], "fictional counts",
        nav="Compare two topics", client="Claude Code", heading="Compare competing narratives",
        title="Compare two narratives over the same window",
        prompt="Compare AI regulation and AI investment coverage over March–April 2026. Which grew faster, how much do they overlap, and how critical is each?",
        steps=[step("ai-compare", "Exact union and per-query counts"), step("ai-regulation-trends", "Weekly volume: regulation"),
               step("ai-investment-trends", "Weekly volume: investment")],
        overview={"type": "lines", "title": "AI regulation vs AI investment, weekly",
                  "subtitle": "Articles per week · identical dates and matching mode for both queries",
                  "labels": [week(p["period"]) for p in reg["points"]], "unit": "articles per week", "height": 280,
                  "series": [{"name": "AI regulation", "color": "#c0453b", "values": [p["articles"] for p in reg["points"]]},
                             {"name": "AI investment", "color": "#3b4fd8", "values": [p["articles"] for p in inv["points"]]}],
                  "stats": [{"value": f"{items['AI regulation']['count']:,}", "label": "AI regulation articles"},
                            {"value": f"{items['AI investment']['count']:,}", "label": "AI investment articles"},
                            {"value": f"{cmp_['matched']:,}", "label": "match at least one (exact union)"},
                            {"value": f"{items['AI regulation']['count'] + items['AI investment']['count'] - cmp_['matched']:,}", "label": "articles in both"}]},
        detail={"type": "table", "title": "The comparison, measured", "subtitle": "Shares use the union of both queries, so they can sum past 100%",
                "headers": ["Query", "Articles", "Share of union", "Peak week", "Critical share"], "widths": [26, 16, 18, 18, 22],
                "rows": [[{"main": n, "sub": f"q = “{n}”"}, {"num": f"{items[n]['count']:,}"}, {"num": f"{items[n]['share_pct']:.1f}%"},
                          day(t["peak"]), {"num": f"{t['critical_total'] / t['total'] * 100:.1f}%"}]
                         for n, t in (("AI regulation", reg), ("AI investment", inv))],
                "stats": [{"value": f"{cmp_['matched']:,}", "label": "union: match at least one"},
                          {"value": f"{(items['AI regulation']['count'] + items['AI investment']['count'] - cmp_['matched']) / cmp_['matched'] * 100:.1f}%", "label": "of the union match both"},
                          {"value": f"{reg['complete_periods']} weeks", "label": "complete periods, no partial buckets"}],
                "note": trend_note(reg, inv)},
        footnote="Sets may overlap. Keep dates, content-class scope and matching mode identical when comparing.",
        takeaway="Put two narratives on one scale, with exact overlap and per-topic criticality.",
        evidence_summary="Compare union counts plus weekly trends per query",
        guide=f"{GUIDE}#compare-25-named-queries"))

    pri, crit = data("semiconductor-priority"), data("semiconductor-critical")
    stories.append(story(
        "critical-alerts", ["semiconductor-priority", "semiconductor-critical"], "fictional articles and counts",
        nav="Critical news alerts", client="Codex", heading="Separate signal from noise",
        title="Surface the critical stories in a busy topic",
        prompt="Show how semiconductor news splits by priority in March–April 2026, then list only the critical stories rated 7 or higher.",
        steps=[step("semiconductor-priority", "Priority distribution"), step("semiconductor-critical", "Critical headlines only")],
        overview={"type": "columns", "title": "Semiconductor coverage by priority band",
                  "subtitle": "Priority 1–9 · bands 7–9 are critical", "unit": "articles", "height": 280,
                  "labels": [f"P{b['band']}" for b in pri["bands"]],
                  "sublabels": ["critical" if b["critical"] else "" for b in pri["bands"]],
                  "series": [{"name": "Articles", "values": [b["count"] for b in pri["bands"]]}],
                  "stats": [{"value": f"{pri['carrying']:,}", "label": "articles with a priority"},
                            {"value": f"{pri['critical']['count']:,}", "label": "critical (7–9)"},
                            {"value": f"{pri['critical']['share']:.1f}%", "label": f"critical share (archive {pri['baseline']['critical_share']}%)"},
                            {"value": f"{pri['mean_priority']}", "label": "mean priority"}]},
        detail={"type": "cards", "title": "Critical semiconductor stories", "subtitle": "priority_min = 7 · newest first",
                "items": [card(a) for a in unique(crit["items"])[:4]],
                "note": "Priority is the pipeline's urgency rating, not a reliability measure. Repeated headlines are shown once." + missing(crit)},
        footnote="Critical share divides by articles carrying a priority, not by all matching articles.",
        takeaway="Quantify how much of a topic is urgent, then read just those stories.",
        evidence_summary="Priority bands plus critical headlines",
        guide=f"{GUIDE}#sentiment-and-priority"))

    veh, bank = data("class-map-vehicle"), data("class-map-banking")
    groups_ = [{"query": "vehicle", "items": veh["items"]}, {"query": "banking", "items": bank["items"]}]
    stories.append(story(
        "class-code-map", ["class-map-vehicle", "class-map-banking"], "codes as returned",
        nav="GCP class code map", client="Claude Code", heading="Map topics to content classes",
        title="Turn a topic into GCP content-class codes",
        prompt="Which GCP content-class codes cover vehicles and banking? Give me the codes and full paths so I can filter headlines by class.",
        steps=[step("class-map-vehicle", "Find vehicle class codes"), step("class-map-banking", "Find banking class codes"),
               local("Use the codes as filters", "classes=63,42 on any news endpoint")],
        overview={"type": "tree", "title": "Content-class codes for two topics",
                  "subtitle": "Up to five matches per query · integer code → full GCP path", "groups": groups_,
                  "note": "Use any returned code as `classes=` on headlines, trends, sentiment, themes or export."},
        detail={"type": "table", "title": "Codes ready to use as filters", "subtitle": "Leaf class, parent path and request parameter",
                "headers": ["Code", "Class", "Parent path", "30-day articles", "Filter"], "widths": [9, 30, 32, 13, 16],
                "rows": [[{"num": str(i["code"])}, {"main": i["path"].split("/")[-1]}, {"sub": i["parent"]},
                          {"num": f"{i['articles_30d']:,}"} if i.get("articles_30d") is not None else {"missing": "unavailable"},
                          {"tag": f"classes={i['code']}"}] for i in (veh["items"][:4] + bank["items"][:3])],
                "note": ("30-day volumes count the 30 days ending at data_through, when ingest is thin; use them to compare classes, not as totals."
                         if any(i.get("articles_30d") is not None for i in veh["items"]) else
                         "30-day article volumes were unavailable at capture time; codes and paths are complete.")},
        footnote="Class matches use the pipeline's 0.39 score threshold. One article can carry several classes.",
        takeaway="Find the right content-class codes by name, then filter any endpoint by them.",
        evidence_summary="Class discovery for two topics",
        guide=f"{GUIDE}#find-a-gcp-content-code"))

    exp = data("battery-export")
    stories.append(story(
        "full-article-export", ["battery-export"], "fictional articles",
        nav="Full articles to CSV", client="Codex", heading="Export full articles for analysis",
        title="Export full article text to a spreadsheet",
        prompt="Export the full text of battery-storage articles from March–April 2026 to a CSV with headline, publisher, date, sentiment, priority and classes.",
        steps=[step("battery-export", "Export a batch of full articles"), local("Write the CSV locally", "or request format=csv directly")],
        overview={"type": "bars", "title": "Full bodies, not ledes", "labelWidth": 470,
                  "subtitle": f"{exp['charged_exports']} articles delivered of {exp['total_estimate']:,} matches · characters of full text",
                  "axisLabel": "Characters of article body",
                  "rows": [{"label": trim(a["headline"], 38), "sub": f"{a['publisher']} · {day(a['published_at'])}",
                            "value": a["body_chars"], "display": f"{a['body_chars']:,} chars · lede {len(a['lede'])}"} for a in exp["items"]],
                  "stats": [{"value": str(exp["charged_exports"]), "label": "exports charged"},
                            {"value": str(exp["unresolved"]), "label": "unavailable, not charged"},
                            {"value": str(exp["duplicates_dropped"]), "label": "duplicates dropped, not charged"},
                            {"value": f"{exp['total_estimate']:,}", "label": "matching articles"}]},
        detail={"type": "sheet", "title": "Full articles, as a CSV file", "subtitle": "The export's CSV columns, one row per delivered article",
                "filename": "battery-storage.csv", "status": "format=csv · next batch via cursor (json)",
                "headers": ["headline", "publisher", "published_at", "sentiment", "priority", "classes"], "widths": [36, 22, 14, 12, 8, 8],
                "rows": [[trim(a["headline"], 44), a["publisher"], a["published_at"][:10], {"tag": a["sentiment"]["label"], "tone": TONE[a["sentiment"]["group"]]},
                          str(a["priority"]), "|".join(str(c["code"]) for c in a["classes"])] for a in exp["items"]],
                "note": "The body column holds the complete article text; it is omitted here for width."},
        footnote="Exports are charged per delivered article. Save IDs across batches to deduplicate a full download.",
        takeaway="Move from a filter to full article text in a file your analysis tools can read.",
        evidence_summary="One full-article export batch",
        guide=f"{GUIDE}#full-articles-and-exports"))

    for s in stories:
        s["title"] = s["title"]
    kinds = Counter(s["kind"] for s in stories)
    paragraphs = {
        "ev-theme-discovery": "Theme discovery ranks up to five themes for a required phrase by lift: how much more often a theme appears in this coverage than in the 30-day archive baseline, weighted by support. The chart shows lift with each theme's article count and period-over-period change, then the detail view opens newest headlines for the strongest theme with sentiment, priority and class kept visible. Headlines do not carry theme metadata; the selected theme is passed back as a filter.",
        "tariff-sentiment": "The weekly sentiment timeline splits labelled articles into negative, neutral and positive groups. The stacked columns show the most negative week, and the summary compares the window's negative-to-positive ratio with the archive baseline. The detail view lists negative headlines rated priority 6 or higher from the same window, so a reader can see which stories carried the tone. Shares divide by articles carrying a sentiment label.",
        "ai-topic-compare": "Compare returns each query's count and the exact union of both, so overlap is measured rather than guessed. Weekly trends for each query, over identical dates, draw the two lines. The detail table adds each topic's peak week and critical share from its trend totals. Shares divide by the union and can sum past 100%.",
        "critical-alerts": "The priority distribution counts articles in bands 1–9 and reports the critical share (7–9) against the archive baseline. The detail view requests only priority 7 and above, so the reader sees just the urgent stories; repeated headlines from one publisher are shown once. Priority is an urgency rating from the pipeline, not a reliability judgement, and a keyword match can pull in non-news sources, so read the publisher.",
        "class-code-map": "Class discovery searches the GCP content-class taxonomy by name and returns up to five integer codes per query with full paths, parents and article volumes for the last 30 days of data. The tree shows the codes for two topics; the detail table turns them into ready-to-use `classes=` filters.",
        "full-article-export": "A JSON export returns full article bodies, not the short ledes in headline lists, and charges one export per delivered article. Articles that cannot be fetched, and republished copies of one article under different URLs, are dropped and not charged; the stats show both. The chart compares body lengths; the detail view shows the same batch in the CSV column layout. Continue with `next_cursor` from a JSON export when you need the next batch.",
    }
    site = {"brand": "Prism News",
            "description": f"{len(stories)} animated research UI concepts for the Prism News API: theme discovery, sentiment shifts, topic comparison, critical alerts, content-class codes and full-article export.",
            "headline": "See what a connected<br>news assistant can build.",
            "intro": "Write a brief in Claude Code or Codex. The Prism News API supplies filtered headlines, themes, tone, priority and full articles; your client turns them into a useful view.",
            "provenance": provenance(stories),
            "readme_blurb": "They cover theme discovery, a weekly sentiment shift, comparing two topics, critical alerts, GCP content-class codes and full-article export."}
    write_outputs(stories, site, paragraphs)
    print(f"Built {len(stories)} stories ({dict(kinds)}); all requests validated; no live calls.")


if __name__ == "__main__":
    build()
