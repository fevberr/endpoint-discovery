from __future__ import annotations

_DATA_ATTR_HINTS = (
    "data-endpoint",
    "data-api",
    "data-url",
    "data-href",
    "data-action",
    "data-src",
    "data-path",
    "data-route",
    "data-target",
)


def _0001(_node) -> list:
    _out = []
    try:
        _attrs = _node.attributes
    except Exception:
        return _out
    for _k, _v in _attrs.items():
        if _k.lower() in _DATA_ATTR_HINTS and _v:
            _out.append((_k, _v))
    return _out