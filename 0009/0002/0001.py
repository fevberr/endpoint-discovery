from __future__ import annotations

from importlib import import_module


def test_normalize():
    n = import_module("0001.0005.0001")._0001
    assert n("https://EXAMPLE.com/a") == "https://example.com/a"


def test_classify():
    c = import_module("0001.0008.0001")._0001
    assert c("/api/v1/users") == "api"
    assert c("https://example.com") == "absolute"


def test_confidence():
    s = import_module("0001.0008.0002")._0001
    assert s("fetch", "/api/v1/users") >= 80
    assert s("fetch", "/foo") >= 40
    assert s("regex", "x") <= 40