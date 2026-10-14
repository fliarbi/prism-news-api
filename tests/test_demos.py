"""The animated demos stay consistent with their saved sources and media."""
import importlib.util
from pathlib import Path


def test_demo_provenance_requests_and_media():
    path = Path(__file__).resolve().parent.parent / "scripts/check_use_case_demos.py"
    spec = importlib.util.spec_from_file_location("check_use_case_demos", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.check()
