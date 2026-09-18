from __future__ import annotations

from importlib import import_module


def _0001(_url: str, _kind: str):
    _r_mod = import_module("0001.0003.0001")
    return _r_mod._0001(url=_url, kind=_kind)


def _0002(_resources: list) -> dict:
    _out = {"html": 0, "javascript": 0, "sourcemap": 0, "other": 0}
    for _r in _resources:
        if _r.kind in _out:
            _out[_r.kind] += 1
        else:
            _out["other"] += 1
    return _out