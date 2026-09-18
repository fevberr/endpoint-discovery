from __future__ import annotations

from importlib import import_module


def test_analyzer_fetch():
    m = import_module("0001.0012.0002")
    class R:
        pass
    r = R()
    r.body = b'fetch("/api/v1/users");'
    r.url = "x.js"
    r.kind = "javascript"
    out = m._0001(r, None)
    assert any(f["url"] == "/api/v1/users" for f in out)


def test_analyzer_ws():
    m = import_module("0001.0012.0002")
    class R:
        pass
    r = R()
    r.body = b'new WebSocket("wss://example.com/ws");'
    r.url = "x.js"
    r.kind = "javascript"
    out = m._0001(r, None)
    assert any(f["detector"] == "websocket" for f in out)