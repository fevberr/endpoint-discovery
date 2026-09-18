from __future__ import annotations

import json


def _0001(_endpoints: list, _res, _opts) -> str:
    _lines = []
    for _e in _endpoints:
        _lines.append(json.dumps({
            "url": _e.url,
            "method": _e.method,
            "category": _e.category,
            "confidence": _e.confidence,
            "score": _e.score,
            "detector": _e.detector,
            "source": _e.source_resource,
            "line": _e.line,
            "column": _e.column,
        }, sort_keys=True))
    return "\n".join(_lines) + ("\n" if _lines else "")