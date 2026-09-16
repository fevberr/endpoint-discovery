from __future__ import annotations

from dataclasses import fields
from importlib import import_module


def _0003(_opts):
    _cfg = import_module("0001.0002.0001")
    _val = import_module("0001.0002.0002")
    _defaults_inst = type(_opts)()
    _explicit = set()
    for _f in fields(_opts):
        if getattr(_opts, _f.name) != getattr(_defaults_inst, _f.name):
            _explicit.add(_f.name)
    _merged = _cfg._0001()
    if _opts.config_path:
        _merged.update(_cfg._0002(_opts.config_path))
    _merged.update(_cfg._env_overrides())
    for _k, _v in _merged.items():
        if _k in _explicit:
            continue
        if hasattr(_opts, _k):
            setattr(_opts, _k, _v)
    _errs = _val._0001(_opts)
    if _errs:
        raise ValueError("; ".join(_errs))
    return _opts