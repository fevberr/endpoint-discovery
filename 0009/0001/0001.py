from __future__ import annotations

from importlib import import_module


def test_defaults():
    o = import_module("0001.0001.0001")._0001()
    assert o.scope == "same-origin"
    assert o.depth == 1
    assert o.timeout == 15