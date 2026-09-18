from __future__ import annotations

import re

_FETCH_RE = re.compile(r"fetch\s*\(\s*(['\"`])([^'\"`]+)\1")
_XHR_RE = re.compile(r"\.open\s*\(\s*(['\"`])([A-Z]+)\1\s*,\s*(['\"`])([^'\"`]+)\3")
_AXIOS_RE = re.compile(r"axios\s*\.\s*(get|post|put|patch|delete)\s*\(\s*(['\"`])([^'\"`]+)\2")
_WS_RE = re.compile(r"new\s+WebSocket\s*\(\s*(['\"`])([^'\"`]+)\1")


def _0001(_root, _opts) -> list:
    if not _root.body:
        return []
    _src = _root.body.decode("utf-8", errors="replace")
    _found = []
    for _m in _FETCH_RE.finditer(_src):
        _line = _src.count("\n", 0, _m.start()) + 1
        _found.append({
            "url": _m.group(2),
            "method": "GET",
            "detector": "fetch",
            "line": _line,
            "column": 0,
            "expression": _m.group(0)[:120],
        })
    for _m in _XHR_RE.finditer(_src):
        _line = _src.count("\n", 0, _m.start()) + 1
        _found.append({
            "url": _m.group(4),
            "method": _m.group(2).upper(),
            "detector": "xhr",
            "line": _line,
            "column": 0,
            "expression": _m.group(0)[:120],
        })
    for _m in _AXIOS_RE.finditer(_src):
        _line = _src.count("\n", 0, _m.start()) + 1
        _found.append({
            "url": _m.group(3),
            "method": _m.group(1).upper(),
            "detector": "axios",
            "line": _line,
            "column": 0,
            "expression": _m.group(0)[:120],
        })
    for _m in _WS_RE.finditer(_src):
        _line = _src.count("\n", 0, _m.start()) + 1
        _found.append({
            "url": _m.group(2),
            "method": "WS",
            "detector": "websocket",
            "line": _line,
            "column": 0,
            "expression": _m.group(0)[:120],
        })
    return _found