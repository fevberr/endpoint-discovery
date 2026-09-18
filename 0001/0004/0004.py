from __future__ import annotations

from importlib import import_module


def _0001(_doc, _base: str) -> list:
    _resolve = import_module("0001.0005.0002")
    _out = []
    try:
        _forms = _doc.css("form")
    except Exception:
        return _out
    for _f in _forms:
        try:
            _action = _f.attributes.get("action") or ""
            _method = (_f.attributes.get("method") or "GET").upper()
        except Exception:
            continue
        _u = _resolve._0001(_base, _action) if _action else _base
        _fields = []
        try:
            for _i in _f.css("input, textarea, select"):
                _n = _i.attributes.get("name")
                if _n:
                    _fields.append(_n)
        except Exception:
            pass
        _out.append({"url": _u, "method": _method, "fields": _fields})
    return _out