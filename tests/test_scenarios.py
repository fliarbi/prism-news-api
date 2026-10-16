"""Demonstration pages, the command-line client and the installer."""
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import scenario_common as sc  # noqa: E402


def load_cli():
    spec = importlib.util.spec_from_file_location("prism_cli", ROOT / "scripts/prism_cli.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_pages_exist_link_and_come_from_captures():
    result = sc.check()
    assert result["pages"] >= 40 * result["segments"] * 0.9


def test_every_kept_page_is_backed_by_a_saved_capture_without_account_details():
    log = json.loads(sc.LOG.read_text())
    for slug, entry in log.items():
        if entry.get("kept"):
            rec = json.loads((sc.CAPS / f"{slug}.json").read_text())
            assert rec["kind"] == "captured"
            for c in rec["calls"]:
                assert not set(sc.PRIVATE_META) & set(c["response"].get("meta") or {}), slug


def test_readme_puts_demonstrations_first():
    text = (ROOT / "README.md").read_text()
    assert text.index(sc.README_START) < text.index("## Install in one line") < text.index("## Get started in five steps")


def test_cli_maps_options_to_request_fields():
    cli = load_cli()
    pos, fields, flags = cli.parse(["steel industry", "--priority-min", "7", "--sentiment", "negative",
                                    "--sentiment", "neutral", "--resolve=true", "--table", "-o", "x.csv"])
    assert pos == ["steel industry"]
    assert fields == {"priority_min": 7, "sentiment": ["negative", "neutral"], "resolve": True}
    assert flags == {"table": True, "output": "x.csv"}


def test_getting_started_documents_every_command():
    cli = load_cli()
    doc = (ROOT / "docs/GETTING_STARTED.md").read_text()
    for name, (_, commands, _) in cli.PRODUCTS.items():
        if name not in doc.split("<!-- cli:start -->")[1]:
            continue
        for cmd, (method, path) in commands.items():
            assert f"`{name} {cmd}" in doc, cmd
            assert path in doc, path


def test_cli_saves_key_owner_only(tmp_path, monkeypatch):
    cli = load_cli()
    monkeypatch.setattr(cli, "CONFIG", tmp_path / "prism" / "config.json")
    cli.save_config({"key": "pna_x", "news_base": "http://h"})
    assert oct(cli.CONFIG.stat().st_mode & 0o777) == "0o600"


def test_installer_is_valid_bash_and_never_uses_sudo():
    script = ROOT / "scripts/install.sh"
    subprocess.run(["bash", "-n", str(script)], check=True)
    text = script.read_text()
    assert "sudo" not in text.replace("never uses sudo", "").replace("Never uses sudo", "")
    out = subprocess.run(["bash", str(script), "--help"], capture_output=True, text=True, check=True).stdout
    assert "PRISM_BIN_DIR" in out


@pytest.mark.skipif(os.name != "posix", reason="POSIX launcher")
def test_cli_help_runs_without_configuration():
    out = subprocess.run([sys.executable, str(ROOT / "scripts/prism_cli.py"), "--help"], capture_output=True, text=True,
                         env={**os.environ, "PRISM_CLI_PRODUCT": "prism-news"}, check=True).stdout
    assert "headlines" in out
