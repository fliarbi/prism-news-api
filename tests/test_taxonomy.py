from __future__ import annotations

import pytest

from prism_news_api import taxonomy


def test_code_map_size_and_examples():
    assert taxonomy.CLASS_COUNT == 1096
    assert taxonomy.path_of(0) == "/News/Business News/Company News"
    assert taxonomy.path_of(55) == "/Business & Industrial/Business Finance/Venture Capital"
    assert taxonomy.code_of("/News/Business News/Company News") == 0
    assert taxonomy.code_of("/business & industrial/business finance/venture capital") == 55


def test_prefix_expansion_includes_self_and_children_only():
    codes = taxonomy.expand_prefix("/News/Business News")
    paths = [taxonomy.path_of(c) for c in codes]
    assert "/News/Business News/Company News" in paths
    assert all(p == "/News/Business News" or p.startswith("/News/Business News/") for p in paths)
    assert not any(p.startswith("/News/Business Newsletters") for p in paths)


def test_prefix_root_returns_everything_and_unknown_returns_nothing():
    assert len(taxonomy.expand_prefix("/")) == 1096
    assert taxonomy.expand_prefix("/Nope") == []


def test_depth_parent_children():
    e = taxonomy.class_entry(0)
    assert e["depth"] == 3 and e["parent"] == "/News/Business News"
    assert e["parent_code"] == taxonomy.code_of("/News/Business News")
    kids = taxonomy.children_of("/News/Business News")
    assert 0 in kids and all(taxonomy.depth_of(taxonomy.path_of(k)) == 3 for k in kids)


def test_validate_codes():
    assert taxonomy.validate_codes(["0", 55, " 0 "]) == [0, 55]
    with pytest.raises(ValueError) as e:
        taxonomy.validate_codes([0, 424242, "x"])
    assert "424242" in str(e.value) and "x" in str(e.value)


def test_search():
    hits = taxonomy.search(q="venture")
    assert any(h["code"] == 55 for h in hits)
    assert all(h["path"].startswith("/Finance") for h in taxonomy.search(prefix="/Finance"))


def test_sentiment_vocab():
    assert len(taxonomy.SENTIMENTS) == 9
    assert taxonomy.expand_sentiment(["positive"]) == list(taxonomy.GROUPS["positive"])
    assert taxonomy.expand_sentiment(["NONE"]) == ["none"]
    assert taxonomy.group_of("extreme_neg") == "negative" and taxonomy.group_of("zzz") is None
    with pytest.raises(ValueError):
        taxonomy.expand_sentiment(["meh"])


def test_vocabulary_block():
    v = taxonomy.vocabulary()
    assert [s["label"] for s in v["sentiments"]] == list(taxonomy.SENTIMENTS)
    assert v["critical_min"] == 7 and v["class_count"] == 1096
    assert v["class_examples"][0].endswith("Company News")
