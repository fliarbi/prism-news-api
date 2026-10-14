"""Prevent the served guide and the reviewed user contract from drifting."""
from pathlib import Path
import re
from fastapi.testclient import TestClient
from prism_news_api.main import create_app


def test_packaged_guide_is_current_and_served_without_auth():
    root = Path(__file__).resolve().parents[1]
    canonical = (root / 'docs' / 'USER_GUIDE.md').read_text()
    packaged = (root / 'prism_news_api' / 'data' / 'user_guide.md').read_text()
    assert canonical == packaged
    client = TestClient(create_app())
    r = client.get('/guide')
    assert r.status_code == 200 and r.text == canonical
    assert r.headers['content-type'].startswith('text/markdown')
    public_docs = (root / 'README.md').read_text() + canonical
    assert not re.search(r'subcats|ClickHouse|Redis|MongoDB|192\.168\.|/home/|/mnt/', public_docs, re.I)
    assert '450M+' in public_docs
    for source in re.findall(r'```python\n(.*?)```', canonical, re.S):
        compile(source, '<user guide>', 'exec')


def test_smoke_csv_header_matches_export():
    import importlib.util
    from pathlib import Path
    from prism_news_api.features import export
    spec = importlib.util.spec_from_file_location("smoke", Path(__file__).resolve().parent.parent / "smoke_test.py")
    smoke = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(smoke)
    assert smoke.CSV_COLUMNS == export.CSV_COLUMNS
