#!/usr/bin/env python3
"""Check demo contracts/provenance and media hashes; optionally inspect GIF frames."""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_use_case_demos import validate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/demos"
RENDER_SOURCES = ("stage.html", "stage.js", "stage.css", "demo.css")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(stories: list[dict]) -> dict:
    from PIL import Image

    rows = []
    for story in stories:
        gif = BASE / "media" / (story["id"] + ".gif")
        png = gif.with_suffix(".png")
        with Image.open(gif) as image:
            duration, result_hashes, prompt_hashes = 0, set(), set()
            loop, frames = image.info.get("loop"), image.n_frames
            for i in range(frames):
                image.seek(i)
                duration += image.info.get("duration", 0)
                if i in (0, 15, 30, 60, 110, 250, frames - 1):
                    rgb = image.convert("RGB")
                    result_hashes.add(hashlib.sha256(rgb.crop((50, 190, 1230, 690)).tobytes()).hexdigest())
                    prompt_hashes.add(hashlib.sha256(rgb.crop((70, 310, 1210, 620)).tobytes()).hexdigest())
            assert image.size == (1280, 800) and frames >= 100 and loop == 0, gif
            assert abs(duration - story["duration"] * 1000) <= 100, gif
            assert len(result_hashes) >= 3 and len(prompt_hashes) >= 3, f"missing meaningful animation: {gif}"
        with Image.open(png) as image:
            assert image.size == (1280, 800), png
        rows.append({"id": story["id"], "gif": "media/" + gif.name, "poster": "media/" + png.name,
                     "width": 1280, "height": 800, "frames": frames, "duration_ms": duration, "loop": loop,
                     "gif_bytes": gif.stat().st_size, "poster_bytes": png.stat().st_size,
                     "gif_sha256": sha(gif), "poster_sha256": sha(png), "data_kind": story["kind"]})
    return {"scope": "Animated client UI concepts; captured responses and illustrative fixtures are labelled separately",
            "render_sources": [{"file": f, "sha256": sha(BASE / f)} for f in RENDER_SOURCES],
            "story_sha256": sha(BASE / "demo-data.json"), "gifs": len(rows), "clips": rows}


def check() -> None:
    stories = json.loads((BASE / "demo-data.json").read_text())
    assert len({s["id"] for s in stories}) == len(stories) >= 5
    javascript = (BASE / "demo-data.js").read_text()
    assert javascript == "window.PRISM_DEMOS = " + json.dumps(stories, ensure_ascii=False, indent=2) + ";\n"
    for story in stories:
        assert story["kind"] in {"captured", "illustrative"}
        assert "not a recording" in story["disclosure"] and story["badge"] and story["footnote"]
        assert story["badge"].startswith("Captured data" if story["kind"] == "captured" else "Illustrative data")
        assert story["sources"], story["id"]
        for source in story["sources"]:
            path = BASE / source["file"]
            assert sha(path) == source["sha256"], f"source changed since build: {source['file']}"
            record = json.loads(path.read_text())
            assert record["kind"] == source["kind"]
            if story["kind"] == "captured":
                assert record["kind"] == "captured" and record["captured_at"], source["file"]
            text = path.read_text()
            assert "pna_" not in text and '"quota"' not in text and '"email"' not in text, f"account data in {path}"
        for step in story["steps"]:
            assert step["type"] in {"api", "client"}
            if step["type"] == "api":
                validate(step["path"], step["body"])
        assert (BASE / story["guide"].split("#")[0]).exists(), story["guide"]
    manifest = json.loads((BASE / "media/manifest.json").read_text())
    for source in manifest["render_sources"]:
        assert sha(BASE / source["file"]) == source["sha256"], f"re-render needed: {source['file']} changed"
    assert manifest["story_sha256"] == sha(BASE / "demo-data.json"), "re-render needed: stories changed"
    assert {r["id"] for r in manifest["clips"]} == {s["id"] for s in stories}
    for row in manifest["clips"]:
        gif, png = BASE / row["gif"], BASE / row["poster"]
        assert sha(gif) == row["gif_sha256"] and sha(png) == row["poster_sha256"]
        assert gif.read_bytes()[:6] in (b"GIF87a", b"GIF89a")
        assert struct.unpack("<HH", gif.read_bytes()[6:10]) == (1280, 800)
        assert png.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
        assert struct.unpack(">II", png.read_bytes()[16:24]) == (1280, 800)
        assert row["frames"] >= 100 and row["loop"] == 0
    kinds = {k: sum(s["kind"] == k for s in stories) for k in ("captured", "illustrative")}
    print(f"Verified {len(stories)} GIF/poster pairs ({kinds}), media hashes, source provenance and validated request recipes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true", help="requires Pillow; decode GIF frames and refresh hashes")
    args = parser.parse_args()
    if args.write_manifest:
        records = json.loads((BASE / "demo-data.json").read_text())
        (BASE / "media/manifest.json").write_text(json.dumps(inspect(records), indent=2) + "\n")
    check()
