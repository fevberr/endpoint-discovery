from __future__ import annotations

from urllib.parse import urlsplit


def _0001(_scope, _url: str) -> bool:
    if not _url:
        return False
    try:
        _p = urlsplit(_url)
    except ValueError:
        return False
    if _p.scheme not in ("http", "https", "ws", "wss"):
        return False
    if _scope.mode == "any":
        return True
    return (_p.netloc.lower() == _scope.origin_host)