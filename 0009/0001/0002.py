from __future__ import annotations

from importlib import import_module


def test_parse_minimal():
    m = import_module("0001.0001.0002")
    o = m._0003(["https://example.com"])
    assert o.target == "https://example.com"
    assert o.scope == "same-origin"


def test_parse_flags():
    m = import_module("0001.0001.0002")
    o = m._0003([
        "https://example.com", "--json", "--depth", "2",
        "--source-maps", "--frameworks", "--confidence", "high",
    ])
    assert o.output_format == "json"
    assert o.depth == 2
    assert o.source_maps is True
    assert o.frameworks is True
    assert o.confidence == "high"