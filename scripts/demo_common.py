"""Shared helpers for the animated use-case demos (identical in both API repos).

The per-repo build script defines the stories; this module turns them into the
gallery data, the gallery page, the walkthrough article and the README section.
"""
from __future__ import annotations

import hashlib
import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "docs/demos"
EXAMPLES = ROOT / "docs/examples/demo"
COMMON = {"duration": 32, "width": 1280, "height": 800,
          "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run."}
README_START, README_END = "<!-- demos:start -->", "<!-- demos:end -->"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict:
    return json.loads((EXAMPLES / f"{name}.json").read_text())


def evidence(names: list[str]) -> list[dict]:
    return [{"file": f"../examples/demo/{n}.json", "sha256": sha(EXAMPLES / f"{n}.json"),
             "kind": read(n)["kind"]} for n in names]


def kind_of(names: list[str]) -> str:
    return "captured" if all(read(n)["kind"] == "captured" for n in names) else "illustrative"


def captured_on(names: list[str]) -> str:
    stamp = min(read(n)["captured_at"] for n in names)
    return date.fromisoformat(stamp[:10]).strftime("%-d %b %Y")


def coverage_note(names: list[str]) -> str | None:
    """A partial-news-index note carried by any captured source (counts are lower bounds)."""
    notes = {read(n).get("coverage_note") for n in names} - {None}
    return "; ".join(sorted(notes)) or None


def local(label: str, detail: str) -> dict:
    return {"type": "client", "label": label, "detail": detail}


def usd(n: float | None) -> str:
    if n is None:
        return "Not returned"
    for div, suffix in ((1e9, "B"), (1e6, "M"), (1e3, "k")):
        if abs(n) >= div:
            return f"${n / div:,.1f}{suffix}".replace(".0" + suffix, suffix)
    return f"${n:,.0f}"


def day(iso: str) -> str:
    return date.fromisoformat(iso[:10]).strftime("%-d %b")


def trim(s: str | None, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def write_outputs(stories: list[dict], site: dict, paragraphs: dict[str, str]) -> None:
    data = [{**COMMON, **s} for s in stories]
    DEMOS.mkdir(parents=True, exist_ok=True)
    (DEMOS / "demo-data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    (DEMOS / "demo-data.js").write_text("window.PRISM_DEMOS = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")
    (DEMOS / "index.html").write_text(gallery_html(data, site))
    (ROOT / "docs/ANIMATED_USE_CASES.md").write_text(article(data, site, paragraphs))
    readme = ROOT / "README.md"
    text = readme.read_text()
    section = readme_section(data, site)
    if README_START in text:
        head, rest = text.split(README_START, 1)
        text = head + section + rest.split(README_END, 1)[1]
    else:
        marker = "\n## Running the service"
        text = text.replace(marker, "\n" + section + "\n" + marker, 1) if marker in text else text + "\n" + section
    readme.write_text(text)


def gallery_html(data: list[dict], site: dict) -> str:
    e = html.escape
    first = data[0]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <title>{e(site['brand'])} workflow gallery</title>
  <meta name="description" content="{e(site['description'])}">
  <link rel="stylesheet" href="demo.css">
  <script src="demo-data.js" defer></script><script src="gallery.js" defer></script>
</head>
<body class="gallery-body">
  <header class="gallery-top"><span class="prism-mark" aria-hidden="true"></span><a class="wordmark" href="index.html" style="color:inherit;text-decoration:none">{e(site['brand'])}</a><span class="top-divider" aria-hidden="true"></span><span class="top-name">Workflow gallery</span><span class="private">Live API</span></header>
  <main class="gallery-main">
    <div class="gallery-intro"><h1>{site['headline']}</h1><p>{e(site['intro'])}</p></div>
    <div class="gallery-grid">
      <nav class="story-tabs" id="story-tabs" aria-label="Choose a workflow"></nav>
      <div>
        <section class="gallery-player" aria-label="Animated workflow demonstration">
          <img id="demo-image" width="1280" height="800" src="media/{first['id']}.png" alt="{e(first['title'])}">
          <div class="player-controls"><button id="play" class="primary" type="button">Play animation</button><button id="replay" type="button">Replay</button><span id="duration"></span><a id="download" href="media/{first['id']}.gif" download>Download GIF</a><a id="poster" href="media/{first['id']}.png" download>Still image</a><a id="full-size" href="media/{first['id']}.gif" target="_blank" rel="noopener">Open full size</a></div>
        </section>
        <div class="gallery-detail">
          <section><h2>Try this research brief</h2><p class="prompt-card" id="prompt"></p><div class="prompt-actions"><button class="copy-prompt" id="copy-prompt" type="button">Copy prompt</button><span id="copy-status" class="copy-status" role="status" aria-live="polite"></span></div></section>
          <section class="evidence-card"><span id="data-label" class="data-label"></span><h2>What you would see</h2><p id="takeaway"></p><p id="data-note" style="margin-top:10px"></p><a id="guide" href="{e(first['guide'])}">Read the API guide</a><details class="recipe"><summary>Inspect the request recipe</summary><pre id="recipe"></pre></details></section>
        </div>
        <div class="disclosure"><p><b>These are UI concepts, not recordings of the official Claude Code or Codex interfaces.</b> Each GIF opens with a large typed prompt, slides the search box away and presents a full-screen chart followed by detailed results. The request recipes beneath the player are the API calls behind each view. The page makes no API calls and stores no credentials.</p><p>{e(site['provenance'])}</p><p><a href="../ANIMATED_USE_CASES.md">Read all {len(data)} walkthroughs and provenance notes</a></p></div>
      </div>
    </div>
    <noscript><p class="no-js">Enable JavaScript to use the gallery, or browse <a href="../ANIMATED_USE_CASES.md">all GIFs and their text descriptions</a>.</p></noscript>
  </main>
</body>
</html>
"""


def recipe(story: dict) -> str:
    return ", ".join(f"`{s['method']} {s['path']}`" for s in story["steps"] if s["type"] == "api")


def article(data: list[dict], site: dict, paragraphs: dict[str, str]) -> str:
    rows = "\n".join(f"| {s['nav']} | {s['evidence_summary']} |" for s in data)
    out = f"""# {site['brand']} with Claude Code or Codex: {len(data)} animated use cases

These GIFs show **client-built research UI concepts**: a large typed prompt slides
off-screen, a full-screen chart appears, then a detailed result view follows. Each
32-second loop gives the prompt and the results their own space. The request
recipes list the {site['brand']} API calls behind each view. They are not screen
recordings of the official Claude Code or Codex interface; an assistant with your
API key can call these endpoints and build a similar local view when you ask.

Open the [interactive gallery](demos/index.html) locally for play/pause, replay,
copyable prompts, request recipes, GIF downloads and still images. All GIFs also
render below on GitHub. Each carries a persistent data-provenance badge.

| Workflow | Displayed evidence |
|---|---|
{rows}

{site['provenance']}

To ask an agent for a similar view, prepend this instruction to a prompt:

> Use the {site['brand']} API with my key in `PRISM_API_KEY`. Retrieve the
> available evidence, then build a simple local research view. Keep dates,
> windows, missing fields and coverage notes visible. Do not invent unavailable data.
"""
    for s in data:
        out += f"\n## {s['nav']}\n\n![{s['title']}. {s['badge']}.](demos/media/{s['id']}.gif)\n\n"
        out += f"**Prompt:** {s['prompt']}\n\n**What you would see:** {paragraphs[s['id']]}\n\n"
        out += f"**Request recipe:** {recipe(s)}. Selection, charting and file writing are client actions.\n\n"
        out += (f"[Download GIF](demos/media/{s['id']}.gif) · [Static image](demos/media/{s['id']}.png) · "
                f"[API guide]({s['guide'].removeprefix('../')})\n\n")
        captured = [x for x in s["sources"] if x["kind"] == "captured"]
        illustrative = [x for x in s["sources"] if x["kind"] != "captured"]
        if captured:
            out += "Captured responses: " + ", ".join(
                f"[{Path(x['file']).name}]({x['file'].removeprefix('../')})" for x in captured) + ".\n"
        if illustrative:
            out += ("Illustrative fixtures (fictional articles and counts in the real response shape; replaced by "
                    "`scripts/capture_demo_examples.py` once captured): " + ", ".join(
                        f"[{Path(x['file']).name}]({x['file'].removeprefix('../')})" for x in illustrative) + ".\n")
    out += ("\n## Reproduce and inspect\n\nThe [story data](demos/demo-data.json) records prompts, validated request "
            "bodies, source paths/hashes and data labels. The [renderer instructions](demos/README.md) explain "
            "capture, deterministic frame rendering, GIF encoding, reduced-motion behaviour and verification.\n")
    return out


def readme_section(data: list[dict], site: dict) -> str:
    cells = []
    for s in data:
        cells.append(f"""    <td width="50%" valign="top">
      <h3>{html.escape(s['nav'])}</h3>
      <a href="docs/demos/media/{s['id']}.gif"><img src="docs/demos/media/{s['id']}.gif" width="420" alt="{html.escape(s['title'])}"></a>
      <p>{html.escape(s['takeaway'])} {'Saved API responses.' if s['kind'] == 'captured' else 'Illustrative data.'}</p>
    </td>""")
    rows = "\n".join("  <tr>\n" + "\n".join(cells[i:i + 2]) + "\n  </tr>" for i in range(0, len(cells), 2))
    return f"""{README_START}
## See the API in a research UI

[{len(data)} animated Claude Code / Codex workflow concepts](docs/ANIMATED_USE_CASES.md) show
what an assistant can build on this API. {site['readme_blurb']} Each GIF labels saved API
responses or illustrative data; these are client-built UI concepts, not recordings of
official client interfaces or claims of live service availability. Open the
[interactive gallery](docs/demos/index.html) locally for prompts and request recipes.

<table>
{rows}
</table>
{README_END}"""
