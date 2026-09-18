from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit


def _0001(_url: str) -> str:
    if not _url:
        return ""
    _u = _url.strip()
    try:
        _p = urlsplit(_u)
    except ValueError:
        return ""
    _scheme = _p.scheme.lower()
    _host = _p.netloc.lower()
    _path = _p.path or "/"
    while "//" in _path:
        _path = _path.replace("//", "/")
    if len(_path) > 1 and _path.endswith("/"):
        _path = _path[:-1]
    return urlunsplit((_scheme, _host, _path, _p.query, ""))