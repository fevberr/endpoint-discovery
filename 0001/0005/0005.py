from __future__ import annotations

from pathlib import Path
from importlib import import_module


def _0005(_opts, _res, _scope):
    _mk = import_module("0001.0003.0002")
    _html = import_module("0001.0004.0001")
    _log = import_module("0001.0011.0002")
    _p = Path(_opts.file).resolve()
    if not _p.is_file():
        _res.errors.append(f"File not found: {_p}")
        return _res
    try:
        _data = _p.read_bytes()
    except OSError as _e:
        _res.errors.append(f"Cannot read {_p}: {_e}")
        return _res
    _suffix = _p.suffix.lower()
    if _suffix in (".html", ".htm"):
        _kind = "html"
    elif _suffix in (".js", ".mjs", ".cjs"):
        _kind = "javascript"
    elif _suffix in (".map",):
        _kind = "sourcemap"
    else:
        _kind = "other"
    _r = _mk._0001(str(_p), _kind)
    _r.body = _data
    _r.size = len(_data)
    _r.content_type = {
        "html": "text/html",
        "javascript": "application/javascript",
        "sourcemap": "application/json",
        "other": "application/octet-stream",
    }.get(_kind, "application/octet-stream")
    _res.resources.append(_r)
    if _kind == "html":
        _res.pages += 1
    elif _kind == "javascript":
        _res.bundles += 1
    elif _kind == "sourcemap":
        _res.maps += 1
    if _kind == "html":
        _log._0001(_opts, "verbose", "Extracting HTML resources")
        try:
            _children = _html._0001(_r, _opts)
        except Exception as _e:
            _res.errors.append(f"HTML parse failed: {_e}")
            _children = []
        _base_dir = _p.parent
        _html_path = str(_p)
        for _c in _children:
            _c.source = _html_path
            _res.resources.append(_c)
            if _c.kind == "javascript":
                _res.bundles += 1
            _local = _resolve_local(_base_dir, _c.url)
            if _local is None:
                continue
            try:
                _sub = _local.read_bytes()
            except OSError:
                continue
            _kind2 = "javascript" if _local.suffix.lower() in (".js", ".mjs", ".cjs") else "other"
            _r2 = _mk._0001(str(_local), _kind2)
            _r2.body = _sub
            _r2.size = len(_sub)
            _r2.source = _html_path
            _r2.content_type = (
                "application/javascript" if _kind2 == "javascript"
                else "application/octet-stream"
            )
            _res.resources.append(_r2)
            if _kind2 == "javascript":
                _res.bundles += 1
    return _res


def _resolve_local(_base_dir: Path, _url: str):
    _u = (_url or "").strip()
    if not _u:
        return None
    if _u.startswith("file://"):
        _candidate = Path(_u[7:])
    elif _u.startswith("/"):
        _candidate = _base_dir / _u.lstrip("/")
    elif "://" in _u:
        _candidate = _base_dir / _u.rsplit("/", 1)[-1]
    else:
        _candidate = _base_dir / _u
    try:
        _p = _candidate.resolve()
    except Exception:
        return None
    if _p.is_file():
        return _p
    return None