from __future__ import annotations

from importlib import import_module


def _0001(_root, _opts) -> list:
    if not _root.body:
        return []
    try:
        from selectolax.parser import HTMLParser
        _doc = HTMLParser(_root.body.decode("utf-8", errors="replace"))
    except Exception:
        return []
    _tags = import_module("0001.0004.0002")
    _inline = import_module("0001.0004.0003")
    _forms_mod = import_module("0001.0004.0004")
    _data = import_module("0001.0004.0005")
    _resolve = import_module("0001.0005.0002")
    _mk = import_module("0001.0003.0002")
    _base = _root.url
    try:
        _meta_base = _doc.css_first("base")
        if _meta_base is not None:
            _bv = _meta_base.attributes.get("href")
            if _bv:
                _base = _resolve._0001(_root.url, _bv) or _root.url
    except Exception:
        pass
    _out = []
    _seen = set()
    try:
        _nodes = _doc.css("*")
    except Exception:
        return []
    for _n in _nodes:
        try:
            for _u, _kind in _tags._0001(_n, _base):
                if _u in _seen:
                    continue
                _seen.add(_u)
                _out.append(_mk._0001(_u, _kind))
            for _k, _v in _data._0001(_n):
                _u = _resolve._0001(_base, _v)
                if _u and _u not in _seen:
                    _seen.add(_u)
                    _out.append(_mk._0001(_u, "other"))
        except Exception:
            continue
    for _kind, _body in _inline._0001(_doc):
        if _kind != "json":
            continue
        try:
            for _p in _inline._0002(_body):
                _u = _resolve._0001(_base, _p)
                if _u and _u not in _seen:
                    _seen.add(_u)
                    _out.append(_mk._0001(_u, "other"))
        except Exception:
            continue
    for _f in _forms_mod._0001(_doc, _base):
        if _f["url"] and _f["url"] not in _seen:
            _seen.add(_f["url"])
            _r = _mk._0001(_f["url"], "form")
            _r.source = ",".join(_f["fields"])
            _out.append(_r)
    return _out