from __future__ import annotations

from urllib.parse import urljoin, urlsplit
from importlib import import_module


def _0001(_base: str, _ref: str) -> str:
    _n = import_module("0001.0005.0001")
    if not _ref:
        return ""
    _r = _ref.strip()
    if _r.startswith(("data:", "javascript:", "mailto:", "tel:", "about:")):
        return ""
    if _r.startswith("#"):
        return ""
    try:
        _joined = urljoin(_base or "", _r)
    except ValueError:
        return ""
    try:
        _scheme = urlsplit(_joined).scheme.lower()
    except ValueError:
        return ""
    if _scheme not in ("http", "https", "ws", "wss"):
        return ""
    return _n._0001(_joined)