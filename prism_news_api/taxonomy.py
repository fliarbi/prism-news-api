"""taxonomy — the vocabularies a caller filters with.

  * GCP content classes: 1,096 Google NL content categories, each with the
    pipeline's integer code (`classification_to_int_code`). Shipped as
    data/gcp_classes.json {code: path}; regenerate with
    scripts/export_gcp_code_map.py. Code 0 = /News/Business News/Company News,
    55 = /Business & Industrial/Business Finance/Venture Capital.
  * Sentiment: nine graded labels in order, grouped negative/neutral/positive.
  * Priority: bands 1–9, higher = more critical; 7+ is "critical".
  * Sort options.

Pure functions over static data — no I/O after import.
"""
from __future__ import annotations

import json

from . import config

with open(config.GCP_CLASSES_PATH, encoding="utf-8") as _f:
    _RAW = json.load(_f)

CODE_TO_PATH: dict[int, str] = {int(k): v for k, v in _RAW.items()}
PATH_TO_CODE: dict[str, int] = {v: k for k, v in CODE_TO_PATH.items()}
_LOWER_PATH_TO_CODE: dict[str, int] = {v.lower(): k for k, v in CODE_TO_PATH.items()}
CLASS_COUNT = len(CODE_TO_PATH)

SENTIMENTS: tuple[str, ...] = ("extreme_neg", "very_neg", "fair_neg", "slight_neg",
                               "none", "slight_pos", "fair_pos", "very_pos",
                               "extreme_pos")
GROUPS: dict[str, tuple[str, ...]] = {
    "negative": ("extreme_neg", "very_neg", "fair_neg", "slight_neg"),
    "neutral": ("none",),
    "positive": ("slight_pos", "fair_pos", "very_pos", "extreme_pos"),
}
LABEL_GROUP: dict[str, str] = {lbl: g for g, lbls in GROUPS.items() for lbl in lbls}

PRIORITY_BANDS: tuple[int, ...] = tuple(range(1, 10))
CRITICAL_MIN = config.CRITICAL_PRIORITY
PRIORITY_NOTES = {
    1: "boilerplate (cookie notices, fixture lists)",
    9: "geopolitics, disasters, the most consequential band",
}

SORTS: tuple[str, ...] = ("newest", "oldest", "priority")


# ── classes ──────────────────────────────────────────────────────────────────
def path_of(code: int) -> str | None:
    return CODE_TO_PATH.get(int(code))


def code_of(path: str) -> int | None:
    if path in PATH_TO_CODE:
        return PATH_TO_CODE[path]
    return _LOWER_PATH_TO_CODE.get(normalise_prefix(path).lower())


def normalise_prefix(prefix: str) -> str:
    p = (prefix or "").strip()
    if not p.startswith("/"):
        p = "/" + p
    return p.rstrip("/") or "/"


def expand_prefix(prefix: str) -> list[int]:
    """Every code whose path IS the prefix or sits under it. Case-insensitive
    (`/finance` finds `/Finance`). Sorted by code."""
    p = normalise_prefix(prefix).lower()
    if p == "/":
        return sorted(CODE_TO_PATH)
    out = [c for lp, c in _LOWER_PATH_TO_CODE.items()
           if lp == p or lp.startswith(p + "/")]
    return sorted(out)


def depth_of(path: str) -> int:
    return len([s for s in path.split("/") if s])


def parent_of(path: str) -> str | None:
    parts = [s for s in path.split("/") if s]
    if len(parts) <= 1:
        return None
    return "/" + "/".join(parts[:-1])


def children_of(path: str) -> list[int]:
    p = normalise_prefix(path).lower()
    d = depth_of(p)
    return sorted(c for lp, c in _LOWER_PATH_TO_CODE.items()
                  if lp.startswith(p + "/") and depth_of(lp) == d + 1)


def class_entry(code: int) -> dict:
    path = CODE_TO_PATH[int(code)]
    parent = parent_of(path)
    return {"code": int(code), "path": path, "depth": depth_of(path),
            "parent": parent, "parent_code": code_of(parent) if parent else None}


def validate_codes(codes) -> list[int]:
    """ints in, ints out; raises ValueError naming every unknown code."""
    out, bad = [], []
    for c in codes:
        try:
            i = int(str(c).strip())
        except (TypeError, ValueError):
            bad.append(str(c))
            continue
        if i not in CODE_TO_PATH:
            bad.append(str(i))
        elif i not in out:
            out.append(i)
    if bad:
        raise ValueError(f"unknown class code(s): {', '.join(bad)} — see /v1/classes")
    return out


def search(q: str | None = None, prefix: str | None = None) -> list[dict]:
    codes = expand_prefix(prefix) if prefix else sorted(CODE_TO_PATH)
    if q:
        ql = q.strip().lower()
        codes = [c for c in codes if ql in CODE_TO_PATH[c].lower()]
    return [class_entry(c) for c in codes]


# ── sentiment ────────────────────────────────────────────────────────────────
def expand_sentiment(tokens) -> list[str]:
    """Labels and/or group names -> ordered list of labels. ValueError on an
    unknown token."""
    out, bad = [], []
    for t in tokens:
        t = str(t).strip().lower()
        if not t:
            continue
        if t in GROUPS:
            out.extend(GROUPS[t])
        elif t in LABEL_GROUP:
            out.append(t)
        else:
            bad.append(t)
    if bad:
        raise ValueError(f"unknown sentiment(s): {', '.join(bad)}; labels are "
                         f"{', '.join(SENTIMENTS)} and groups are "
                         f"{', '.join(GROUPS)}")
    return [l for l in SENTIMENTS if l in set(out)]


def group_of(label: str | None) -> str | None:
    return LABEL_GROUP.get(label or "")


def vocabulary() -> dict:
    return {
        "sentiments": [{"label": l, "group": LABEL_GROUP[l], "rank": i + 1}
                       for i, l in enumerate(SENTIMENTS)],
        "sentiment_groups": {g: list(v) for g, v in GROUPS.items()},
        "sentiment_rule": "one article, one label: the highest-scoring of its up-to-three labels",
        "priority_bands": [{"band": b, "critical": b >= CRITICAL_MIN,
                            "note": PRIORITY_NOTES.get(b)} for b in PRIORITY_BANDS],
        "critical_min": CRITICAL_MIN,
        "priority_rule": "the article's top-scoring band; higher = more critical",
        "sort_options": list(SORTS),
        "granularities": list(config.GRANULARITIES),
        "export_formats": list(config.EXPORT_FORMATS),
        "class_count": CLASS_COUNT,
        "class_score_threshold": config.CLASS_THRESHOLD,
        "class_examples": {0: CODE_TO_PATH[0], 55: CODE_TO_PATH[55]},
        "themes_note": ("Discover at most five relevant themes with /v1/themes?q=your+topic. "
                        "Use the returned theme names unchanged when filtering headlines. "
                        "Use | as the separator when a name contains a comma."),
    }
