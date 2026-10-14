#!/usr/bin/env python3
"""Write the ILLUSTRATIVE stand-ins for demo captures that are not yet captured.

Each fixture has the exact response shape of its endpoint, but every article,
publisher, organization and number in it is fictional (publishers and URLs use
the reserved `.example` domain). Files are labelled `"kind": "illustrative"`
and are never written over a real capture: run capture_demo_examples.py when
the archive is fully available and the real responses replace these.
"""
from __future__ import annotations

import json
from pathlib import Path

from capture_demo_examples import CAPTURES, DEST, WINDOW

WEEKS = ["2026-03-02", "2026-03-09", "2026-03-16", "2026-03-23",
         "2026-03-30", "2026-04-06", "2026-04-13", "2026-04-20"]
LABELS = ("extreme_neg", "very_neg", "fair_neg", "slight_neg", "none",
          "slight_pos", "fair_pos", "very_pos", "extreme_pos")
GROUP = {**{l: "negative" for l in LABELS[:4]}, "none": "neutral", **{l: "positive" for l in LABELS[5:]}}
WINDOW_OUT = {"since": WINDOW["since"], "until": WINDOW["until"], "days": 56, "data_through": "2026-08-24",
              "freshness": "volume thins after 2026-05; the last months are partial"}
NOTE = "Illustrative response: fictional articles, publishers and counts in the real response shape."


def filters(**extra) -> dict:
    return {"filters": {**WINDOW, "limit": 100, "sort": "newest", "match": "any", **extra}}


def envelope(feature: str, data: dict, subject: dict, window: dict | None = WINDOW_OUT) -> dict:
    return {"ok": True, "feature": feature, "subject": subject, "data": data,
            "window": window or {}, "meta": {"coverage": {"available": True}, "notes": [NOTE]}}


def article(i, headline, publisher, day, label, priority, classes, orgs=(), lede="", body=None):
    if body is not None and not lede:
        lede = body[:318].rsplit(" ", 1)[0]
    a = {"id": f"illustr{i:017d}", "headline": headline, "url": f"https://{publisher}/news/{i}",
         "publisher": publisher, "published_at": f"{day}T{8 + i % 9:02d}:15:00", "lede": lede or headline,
         "sentiment": {"label": label, "score": 0.81, "group": GROUP[label]}, "priority": priority,
         "classes": [{"code": c, "path": p, "score": 0.74} for c, p in classes],
         "country": None, "organizations": list(orgs), "people": []}
    if body is not None:
        a.update(body=body, body_chars=len(body), authors=["Newsroom"], top_image=None,
                 meta_description=lede or headline, publish_date=day, language="en")
    return a


def headlines(items, **subj) -> dict:
    return envelope("news.headlines", {"items": items, "returned": len(items), "total_estimate": len(items) * 37,
                                       "next_cursor": "illustrative", "unresolved": 0, "duplicates_dropped": 0,
                                       "limit": len(items), "sort": "newest"},
                    filters(**subj))


AUTOS = [(63, "/Autos & Vehicles/Motor Vehicles (By Type)/Hybrid & Alternative Vehicles")]
TRADE = [(0, "/News/Business News/Company News")]
CHIPS = [(0, "/News/Business News/Company News")]


def trends(points) -> dict:
    pts = [{"period": w, "articles": n, "critical": c, "critical_pct": round(c / n * 100, 1),
            "negative": neg, "positive": pos, "partial_period": False}
           for w, (n, c, neg, pos) in zip(WEEKS, points)]
    peak = max(pts, key=lambda p: p["articles"])["period"]
    return {"granularity": "weekly", "points": pts, "total": sum(p["articles"] for p in pts),
            "critical_total": sum(p["critical"] for p in pts), "complete_periods": 8, "partial_periods": 0,
            "peak": peak}


def fixtures() -> dict[str, dict]:
    out = {}
    themes = [("charging network buildout", 412, 4.1), ("battery supply agreements", 366, 3.2),
              ("ev price cuts and incentives", 298, 2.7), ("autonomous driving pilots", 171, 1.9),
              ("plant retooling and jobs", 143, 1.6)]
    out["ev-themes"] = envelope("news.themes", {
        "items": [{"theme": t, "count": n, "share": round(n / 2140 * 100, 2), "lift": lift,
                   "baseline_count": int(n / lift * 1.6), "previous_period_count": int(n * 0.8),
                   "delta_pct": 25.0, "new_vs_baseline": False} for t, n, lift in themes],
        "returned": 5, "total_estimate": None, "next_cursor": None, "matched": 3870, "carrying": 2140,
        "carrier_share_pct": 55.3, "previous_period": {"since": "2026-01-05", "until": "2026-03-01"},
        "baseline": {"since": "2026-07-26", "until": "2026-08-24", "days": 30, "articles": 1800000,
                     "carrying": 990000, "note": "Archive comparison over the 30 days ending at data_through"},
        "min_articles": 5, "ranked_by": "lift over the theme's corpus-wide share, weighted by sqrt(count)"},
        filters(q="electric vehicle", limit=5))
    out["ev-theme-headlines"] = headlines([
        article(1, "Northwind Motors opens 400 fast-charging bays along the coastal corridor", "dailyauto.example", "2026-04-24", "fair_pos", 6, AUTOS, ["northwind motors"]),
        article(2, "City council approves curbside chargers for apartment districts", "metro-ledger.example", "2026-04-22", "slight_pos", 5, AUTOS),
        article(3, "Charging operator Voltway raises tariffs at highway sites", "energywire.example", "2026-04-17", "slight_neg", 6, AUTOS, ["voltway"]),
        article(4, "Fleet operators report longer queues at urban charging hubs", "logistics-today.example", "2026-04-09", "fair_neg", 5, AUTOS),
        article(5, "Contoso Energy and Northwind sign shared charging-network deal", "dailyauto.example", "2026-03-30", "fair_pos", 7, AUTOS, ["contoso energy", "northwind motors"]),
        article(6, "Regional grid operator studies peak load from new charging sites", "energywire.example", "2026-03-11", "none", 5, AUTOS),
    ], q="electric vehicle", themes=["charging network buildout"], limit=6)

    weekly = [(1210, 520, 240, 450), (1340, 610, 250, 480), (2980, 1810, 270, 900), (3420, 2140, 300, 980),
              (2650, 1520, 290, 840), (2210, 1180, 310, 720), (1890, 930, 330, 630), (1760, 840, 320, 600)]
    timeline = []
    for w, (tot, neg, neu, pos) in zip(WEEKS, weekly):
        labels = {l: 0 for l in LABELS}
        labels.update(very_neg=int(neg * .45), fair_neg=int(neg * .35), slight_neg=neg - int(neg * .45) - int(neg * .35),
                      none=neu, slight_pos=int(pos * .6), fair_pos=pos - int(pos * .6))
        timeline.append({"period": w, "total": tot, "negative": neg, "neutral": neu, "positive": pos,
                         "negative_share": round(neg / tot * 100, 2), "positive_share": round(pos / tot * 100, 2),
                         "labels": labels, "partial_period": False})
    groups = {g: sum(t[g] for t in timeline) for g in ("negative", "neutral", "positive")}
    carrying = sum(groups.values())
    labels_tot = {l: sum(t["labels"][l] for t in timeline) for l in LABELS}
    out["tariff-sentiment"] = envelope("news.sentiment", {
        "matched": 18930, "carrying": carrying, "carrier_share_pct": round(carrying / 18930 * 100, 2),
        "labels": [{"label": l, "group": GROUP[l], "count": labels_tot[l], "share": round(labels_tot[l] / carrying * 100, 2)} for l in LABELS],
        "groups": [{"group": g, "count": n, "share": round(n / carrying * 100, 2)} for g, n in groups.items()],
        "negative_to_positive_ratio": round(groups["negative"] / groups["positive"], 2),
        "baseline": {"since": "2026-07-26", "until": "2026-08-24", "days": 30, "articles": 1800000, "carrying": 1700000,
                     "note": "Archive comparison over the 30 days ending at data_through",
                     "groups": {"negative": {"count": 610000, "share": 35.88}, "neutral": {"count": 330000, "share": 19.41},
                                "positive": {"count": 760000, "share": 44.71}}, "negative_to_positive_ratio": 0.8},
        "vs_baseline_ratio": round(groups["negative"] / groups["positive"] / 0.8, 2), "granularity": "weekly",
        "timeline": timeline}, {**filters(q="tariffs"), "granularity": "weekly"})
    out["tariff-negative-headlines"] = headlines([
        article(11, "Importers warn of shelf-price rises as new tariff schedule takes effect", "tradeweekly.example", "2026-03-24", "very_neg", 8, TRADE),
        article(12, "Port of Eastbay reports 18% drop in container bookings after levy", "harbor-news.example", "2026-03-26", "very_neg", 8, TRADE, ["port of eastbay"]),
        article(13, "Fabrikam Foods cuts outlook, citing tariff costs on packaging", "markets-desk.example", "2026-03-31", "fair_neg", 7, TRADE, ["fabrikam foods"]),
        article(14, "Small exporters seek emergency credit lines amid retaliatory duties", "tradeweekly.example", "2026-04-02", "very_neg", 7, TRADE),
        article(15, "Retail association files challenge against tariff expansion", "metro-ledger.example", "2026-04-08", "fair_neg", 7, TRADE),
        article(16, "Electronics distributors pause orders pending tariff clarification", "markets-desk.example", "2026-04-14", "fair_neg", 7, TRADE),
    ], q="tariffs", sentiment=["negative"], priority_min=7, limit=6)

    reg = [(820, 210, 260, 180), (860, 230, 270, 190), (910, 250, 280, 200), (1460, 610, 420, 260),
           (1690, 720, 460, 300), (1180, 420, 330, 250), (990, 310, 290, 230), (940, 280, 270, 220)]
    inv = [(1520, 180, 220, 720), (1610, 200, 230, 760), (1580, 190, 240, 740), (1640, 210, 260, 770),
           (1910, 260, 280, 900), (2230, 330, 300, 1040), (2410, 360, 320, 1110), (2380, 350, 330, 1090)]
    out["ai-regulation-trends"] = envelope("news.trends", trends(reg), {**filters(q="AI regulation"), "granularity": "weekly"})
    out["ai-investment-trends"] = envelope("news.trends", trends(inv), {**filters(q="AI investment"), "granularity": "weekly"})
    reg_total, inv_total, both = sum(p[0] for p in reg), sum(p[0] for p in inv), 1310
    union = reg_total + inv_total - both
    out["ai-compare"] = envelope("news.compare", {
        "items": [{"name": n, "count": c, "share_pct": round(c / union * 100, 2),
                   "filters": {**WINDOW, "q": q, "match": "any"}, "window": {**WINDOW, "days": 56}}
                  for n, q, c in (("AI regulation", "AI regulation", reg_total), ("AI investment", "AI investment", inv_total))],
        "matched": union, "share_basis": "articles matching at least one query", "sets_may_overlap": True},
        {"queries": ["AI regulation", "AI investment"]})

    bands = [0, 30, 210, 1840, 2630, 1910, 1240, 520, 120]
    carrying = sum(bands)
    base = [0.4, 2.1, 6.3, 22.0, 31.5, 21.0, 11.4, 4.4, 0.9]
    out["semiconductor-priority"] = envelope("news.priority", {
        "matched": 8600, "carrying": carrying, "carrier_share_pct": round(carrying / 8600 * 100, 2),
        "bands": [{"band": i + 1, "count": n, "share": round(n / carrying * 100, 2), "critical": i + 1 >= 7,
                   "baseline_share": base[i]} for i, n in enumerate(bands)],
        "critical": {"min_band": 7, "count": sum(bands[6:]), "share": round(sum(bands[6:]) / carrying * 100, 2)},
        "mean_priority": 5.1,
        "baseline": {"since": "2026-07-26", "until": "2026-08-24", "days": 30, "articles": 1800000, "carrying": 1700000,
                     "note": "Archive comparison over the 30 days ending at data_through", "critical_share": 16.7,
                     "mean_priority": 4.9},
        "vs_baseline_critical": round(sum(bands[6:]) / carrying * 100 / 16.7, 2)}, filters(q="semiconductor"))
    out["semiconductor-critical"] = headlines([
        article(21, "Fab outage at Tailspin Semiconductor halts 12-inch wafer output", "chipwire.example", "2026-04-23", "very_neg", 9, CHIPS, ["tailspin semiconductor"]),
        article(22, "Export licence review delays shipments of advanced lithography tools", "tradeweekly.example", "2026-04-18", "fair_neg", 8, CHIPS),
        article(23, "Litware wins $2.1B subsidy for new packaging plant", "markets-desk.example", "2026-04-15", "fair_pos", 8, CHIPS, ["litware"]),
        article(24, "Memory prices jump 9% week on week as supply tightens", "chipwire.example", "2026-04-10", "slight_neg", 7, CHIPS),
        article(25, "Automakers flag microcontroller shortages for third quarter", "dailyauto.example", "2026-04-02", "fair_neg", 7, CHIPS),
        article(26, "Wide World Devices recalls modules over firmware defect", "chipwire.example", "2026-03-27", "very_neg", 7, CHIPS, ["wide world devices"]),
    ], q="semiconductor", priority_min=7, limit=6)

    body = ("Battery recycling capacity is expanding as automakers seek secure sources of lithium, nickel and cobalt. "
            "This illustrative article stands in for a full body: real exports return the complete article text. ")
    reps = (14, 6, 9, 21, 4)
    items = [article(31 + i, h, p, d, l, pr, AUTOS, (), body=body * reps[i]) for i, (h, p, d, l, pr) in enumerate([
        ("Proseware opens closed-loop battery recycling line", "energywire.example", "2026-04-21", "fair_pos", 6),
        ("Recyclers push for standard battery passports", "tradeweekly.example", "2026-04-16", "slight_pos", 5),
        ("Black-mass prices slide as new capacity arrives", "markets-desk.example", "2026-04-07", "slight_neg", 6),
        ("Automaker signs recovered-nickel supply agreement", "dailyauto.example", "2026-03-25", "fair_pos", 7),
        ("Fire at storage yard prompts safety review", "metro-ledger.example", "2026-03-12", "very_neg", 7)])]
    out["battery-export"] = envelope("news.export", {
        "items": items, "returned": 5, "total_estimate": 214, "next_cursor": "illustrative", "unresolved": 0,
        "duplicates_dropped": 0, "charged_exports": 5, "format": "json", "limit": 5},
        {**filters(q="battery recycling", limit=5), "format": "json"})
    return out


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    for name, response in fixtures().items():
        path = DEST / f"{name}.json"
        if path.exists() and json.loads(path.read_text()).get("kind") == "captured":
            print(f"{name}: real capture present, kept")
            continue
        method, api_path, body = CAPTURES[name]
        record = {"name": name, "kind": "illustrative", "captured_at": None,
                  "request": {"method": method, "path": api_path,
                              "body": {k: (["charging network buildout"] if isinstance(v, dict) else v)
                                       for k, v in body.items()}},
                  "response": response}
        path.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
        print(f"{name}: illustrative fixture written")


if __name__ == "__main__":
    main()
