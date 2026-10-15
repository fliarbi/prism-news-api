# Local animation gallery

Open [index.html](index.html) in a browser, or serve the documentation folder:

```bash
python3 -m http.server 8820 --bind 127.0.0.1 --directory docs
```

Then open `http://127.0.0.1:8820/demos/`. This is a local preview, not a deployment.
The gallery uses local assets only: no API connection, key, analytics, remote fonts or
third-party JavaScript. It supports play/pause, replay, per-workflow selection, copying
prompts, inspecting the request recipe and downloading GIFs or still frames. With
reduced motion enabled it starts on a still image.

The GIFs depict a client-built research workspace, not an official Claude Code or Codex
screen. The [walkthroughs](../ANIMATED_USE_CASES.md) explain each case.

## Data

All six news demos read **captured responses** (15 Oct 2026). They were captured
while one of the archive's 14 shards was offline: 93% of rows were readable, and part
of the article store was unreachable. The capture ran with `PRISM_PARTIAL_CAPTURE=1`, a
demo-capture switch that is off by default and must never be set on a serving
deployment, so every count shown is a lower bound and each badge says so. Headline and
export demos state how many matching articles could not be fetched. Re-run the capture
with the archive fully available (and without the switch) to replace them.

`scripts/illustrative_demo_fixtures.py` can still write fictional stand-ins in the real
response shape (labelled "Illustrative data") for any capture that is missing; it
never overwrites a real capture.

Saved responses live in [../examples/demo/](../examples/demo/). Plan, quota and key
details are stripped before saving; the checker fails if account data appears.

## Rebuild

Development-only requirements: Python with this package importable, Node 22+ (built-in
WebSocket), Chrome/Chromium, FFmpeg with GIF palette filters, and Pillow. Set
`CHROME_BIN` and `FFMPEG_BIN` if they are not on the default paths.

```bash
PRISM_API_BASE=http://127.0.0.1:8800 PRISM_API_KEY=pna_... python3 scripts/capture_demo_examples.py
# during a shard outage only, against a separate capture instance started with PRISM_PARTIAL_CAPTURE=1:
#   PRISM_CAPTURE_COVERAGE="93% of archive rows (1 of 14 shards offline)" python3 scripts/capture_demo_examples.py
python3 scripts/build_use_case_demos.py
node scripts/render_use_case_demos.mjs --inspect     # layout check frames in qa/private/inspect
node scripts/render_use_case_demos.mjs --fps 10      # GIFs + posters
python3 scripts/check_use_case_demos.py --write-manifest
```

`--id <story>` renders one story. The renderer starts an isolated temporary headless
browser profile, opens only the local stage page, evaluates explicit animation times and
captures PNG frames into the ignored `qa/private/`; the profile is removed afterwards.
It fails when a result view overlaps its source note or a prompt overflows the search box.
Every loop is 1280 × 800 at 10 frames per second for 32 seconds: a typed prompt, then a
full-screen chart, then a detailed result view. The GIF palette is computed from the
whole clip and applied with ordered dithering.

## Evidence and limits

[demo-data.json](demo-data.json) is the story manifest: prompts, request bodies (each
validated with the API's own request model), source file paths and SHA-256 hashes, and
the data label. The checker (`python3 scripts/check_use_case_demos.py`, also run by the
test suite) verifies source hashes, provenance labels, request contracts, media
dimensions, loop settings and the [media manifest](media/manifest.json). Request activity
and latency in the animations are illustrated, not measured.
