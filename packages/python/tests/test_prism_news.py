"""Offline tests (network calls are mocked). Run: python -m unittest discover -s tests"""
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import prism_news  # noqa: E402
from prism_news import Client, PrismAPIError, cli, datasets  # noqa: E402


class FakeResponse(io.BytesIO):
    def __init__(self, body: bytes, status: int = 200):
        super().__init__(body)
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class ClientTests(unittest.TestCase):
    def test_post_sends_key_and_body(self):
        seen = {}

        def fake(req, timeout=None):
            seen["url"], seen["method"] = req.full_url, req.get_method()
            seen["key"] = req.get_header("X-api-key")
            seen["body"] = json.loads(req.data)
            return FakeResponse(b'{"ok": true, "data": {"items": []}}')

        with mock.patch("urllib.request.urlopen", fake):
            out = Client(api_key="k1", base_url="https://x.test/news/").headlines("floods", limit=5, since=None)
        self.assertTrue(out["ok"])
        self.assertEqual(seen["url"], "https://x.test/news/v1/headlines")
        self.assertEqual(seen["method"], "POST")
        self.assertEqual(seen["key"], "k1")
        self.assertEqual(seen["body"], {"q": "floods", "limit": 5})

    def test_get_uses_query_string(self):
        seen = {}

        def fake(req, timeout=None):
            seen["url"] = req.full_url
            return FakeResponse(b'{"ok": true}')

        with mock.patch("urllib.request.urlopen", fake):
            Client(api_key="k", base_url="https://x.test/news").class_headlines("medtop:01", limit=3)
        self.assertEqual(seen["url"], "https://x.test/news/v1/classes/medtop%3A01/headlines?limit=3")

    def test_business_base(self):
        seen = {}

        def fake(req, timeout=None):
            seen["url"] = req.full_url
            return FakeResponse(b'{"ok": true}')

        with mock.patch("urllib.request.urlopen", fake):
            Client(api_key="k", business_base_url="https://x.test/biz").business("funding", sector="fintech")
        self.assertEqual(seen["url"], "https://x.test/biz/v1/business/funding")

    def test_compare_shapes_queries(self):
        seen = {}

        def fake(req, timeout=None):
            seen["body"] = json.loads(req.data)
            return FakeResponse(b'{"ok": true}')

        with mock.patch("urllib.request.urlopen", fake):
            Client(api_key="k").compare(["ev", {"name": "Storage", "filters": {"q": "battery storage"}}],
                                        since="2026-01-01")
        self.assertEqual(seen["body"]["queries"], [
            {"name": "ev", "filters": {"since": "2026-01-01", "q": "ev"}},
            {"name": "Storage", "filters": {"since": "2026-01-01", "q": "battery storage"}}])

    def test_error_raises(self):
        import urllib.error

        def fake(req, timeout=None):
            raise urllib.error.HTTPError(req.full_url, 401, "no", {}, io.BytesIO(b'{"ok":false,"error":{"kind":"bad_key"}}'))

        with mock.patch("urllib.request.urlopen", fake):
            with self.assertRaises(PrismAPIError) as ctx:
                Client(api_key="bad").me()
        self.assertEqual(ctx.exception.status, 401)
        self.assertEqual(ctx.exception.kind, "bad_key")

    def test_missing_key(self):
        with mock.patch.dict(os.environ, {"PRISM_API_KEY": ""}):
            with self.assertRaises(PrismAPIError):
                Client().status()


class DatasetTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {"PRISM_NEWS_CACHE": self.tmp.name})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_list_topics(self):
        topics = datasets.list_topics()
        self.assertEqual(len(topics), 60)
        self.assertEqual(topics[0]["repo"], "fliarbi/snowfall-news-2019-2026")
        self.assertTrue(all(t["url"].startswith("https://huggingface.co/datasets/fliarbi/") for t in topics))
        self.assertTrue(datasets.list_topics(cluster="health"))

    def test_list_topics_online(self):
        listing = json.dumps([{"id": "fliarbi/floods-news-2019-2026"}, {"id": "fliarbi/other-thing"},
                              {"id": "fliarbi/new-topic-news-2019-2026"}]).encode()
        with mock.patch("urllib.request.urlopen", lambda req, timeout=None: FakeResponse(listing)):
            slugs = [t["slug"] for t in datasets.list_topics(online=True)]
        self.assertEqual(slugs, ["floods", "new-topic"])

    def test_load_lists_of_dicts(self):
        urls = []

        def fake(req, timeout=None):
            urls.append(req.full_url)
            return FakeResponse(b"month,articles\n2019-01,10\n2019-02,12\n")

        with mock.patch("urllib.request.urlopen", fake):
            t = datasets.load("floods", as_frame=False)
            again = datasets.load_table("floods", "monthly", as_frame=False)  # served from cache
        self.assertEqual(set(t), {"sample", "monthly", "countries"})
        self.assertEqual(t["monthly"][1], {"month": "2019-02", "articles": "12"})
        self.assertEqual(again, t["monthly"])
        self.assertEqual(len(urls), 3)
        self.assertIn("/datasets/fliarbi/floods-news-2019-2026/resolve/main/data/floods-news-sample.csv", urls[0])

    def test_unknown_table(self):
        with self.assertRaises(ValueError):
            datasets.download("floods", "nope")


class CliTests(unittest.TestCase):
    def test_help(self):
        buf = io.StringIO()
        with redirect_stdout(buf), mock.patch.object(sys, "argv", ["prism-news"]):
            cli.main(["--help"])
        self.assertIn("prism-news " + prism_news.__version__, buf.getvalue())
        self.assertIn("headlines", buf.getvalue())

    def test_datasets_list(self):
        buf = io.StringIO()
        with redirect_stdout(buf), mock.patch.object(sys, "argv", ["prism-news"]):
            cli.main(["datasets", "list"])
        self.assertEqual(len(buf.getvalue().strip().splitlines()), 60)

    def test_parse_fields(self):
        pos, fields, flags = cli.parse(["ev", "--priority-min", "7", "--sentiment", "negative",
                                        "--sentiment", "neutral", "--table"])
        self.assertEqual(pos, ["ev"])
        self.assertEqual(fields, {"priority_min": 7, "sentiment": ["negative", "neutral"]})
        self.assertEqual(flags, {"table": True})


if __name__ == "__main__":
    unittest.main()
