from __future__ import annotations

import json

_INLINE_JSON_TYPES = (
    "application/json",
    "application/ld+json",
    "importmap",
    "speculationrules",
    "application/manifest+json",
)


def _0001(_doc) -> list:
    _out = []
    try:
        _scripts = _doc.css("script")
    except Exception:
        return _out
    for _s in _scripts:
        try:
            _t = (_s.attributes.get("type") or "").strip().lower()
            _body = _s.text() or ""
        except Exception:
            continue
        if _t in _INLINE_JSON_TYPES:
            _out.append(("json", _body))
        elif _t in ("", "text/javascript", "module", "application/javascript"):
            if _body:
                _out.append(("js", _body))
    return _out


def _0002(_text: str) -> list:
    _out = []
    try:
        _obj = json.loads(_text)
    except json.JSONDecodeError:
        return _out
    _walk(_obj, _out)
    return _out


def _walk(_node, _out: list, _depth: int = 0) -> None:
    if _depth > 32:
        return
    if isinstance(_node, dict):
        for _k, _v in _node.items():
            if isinstance(_k, str) and _looks_path(_k):
                _out.append(_k)
            _walk(_v, _out, _depth + 1)
    elif isinstance(_node, list):
        for _v in _node:
            _walk(_v, _out, _depth + 1)
    elif isinstance(_node, str):
        if _looks_path(_node):
            _out.append(_node)


def _looks_path(_s: str) -> bool:
    if not _s or len(_s) > 2048:
        return False
    if _s.startswith("/"):
        return True
    if _s.startswith("http://") or _s.startswith("https://"):
        return True
    return False