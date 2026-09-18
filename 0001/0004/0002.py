from __future__ import annotations

from importlib import import_module

_TAG_ATTRS = (
    ("a", "href"),
    ("link", "href"),
    ("script", "src"),
    ("img", "src"),
    ("iframe", "src"),
    ("source", "src"),
    ("video", "src"),
    ("audio", "src"),
    ("form", "action"),
    ("track", "src"),
    ("embed", "src"),
    ("object", "data"),
)


def _0001(_node, _base: str) -> list:
    _resolve = import_module("0001.0005.0002")
    _out = []
    try:
        _tag = _node.tag.lower()
        _attrs = _node.attributes
    except Exception:
        return _out
    for _t, _a in _TAG_ATTRS:
        if _tag != _t:
            continue
        _v = _attrs.get(_a)
        if not _v:
            continue
        _u = _resolve._0001(_base, _v)
        if _u:
            _out.append((_u, _classify_tag(_t, _a)))
    return _out


def _classify_tag(_tag: str, _attr: str) -> str:
    if _tag == "script" and _attr == "src":
        return "javascript"
    if _tag == "link" and _attr == "href":
        return "stylesheet"
    if _tag == "form" and _attr == "action":
        return "form"
    if _tag == "iframe" and _attr == "src":
        return "iframe"
    return "other"