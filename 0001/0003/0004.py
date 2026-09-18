from __future__ import annotations

import asyncio
from importlib import import_module


def _0004(_opts, _res, _scope):
    _log = import_module("0001.0011.0002")
    _scope_check = import_module("0001.0014.0001")
    _html = import_module("0001.0004.0001")
    _fetch = import_module("0001.0016.0001")
    if not _opts.target:
        _res.errors.append("No target URL provided.")
        return _res
    _log._0001(_opts, "normal", f"Retrieving {_opts.target}")
    try:
        _roots = asyncio.run(_fetch._0001(
            _opts, [_opts.target], _scope, _opts.max_bytes, _opts.timeout
        ))
    except Exception as _e:
        _res.errors.append(f"Network error: {_e}")
        return _res
    if not _roots:
        _res.errors.append(f"Unable to retrieve target: {_opts.target}")
        return _res
    _first = _roots[0]
    if _first.error:
        _res.errors.append(
            f"Unable to retrieve target: {_opts.target}\n"
            f"Reason: {_first.error}"
        )
        return _res
    _res.resources.append(_first)
    if _first.kind == "html":
        _res.pages += 1
    elif _first.kind == "javascript":
        _res.bundles += 1
    if _first.kind == "html":
        _children = _html._0001(_first, _opts)
        _queue = []
        for _c in _children:
            if _c.url == _first.url:
                continue
            if not _scope_check._0001(_scope, _c.url):
                continue
            _queue.append(_c)
        if _queue:
            _fetched = asyncio.run(_fetch._0001(
                _opts, [q.url for q in _queue], _scope,
                _opts.max_bytes, _opts.timeout,
            ))
            for _r in _fetched:
                if _r.error:
                    _res.errors.append(f"{_r.url}: {_r.error}")
                    continue
                _res.resources.append(_r)
                if _r.kind == "javascript":
                    _res.bundles += 1
                elif _r.kind == "sourcemap":
                    _res.maps += 1
                elif _r.kind == "html":
                    _res.pages += 1
    return _res