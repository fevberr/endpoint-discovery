from __future__ import annotations

import csv
from pathlib import Path

_FIELDS = [
    "url", "method", "category", "confidence",
    "score", "detector", "source_resource",
    "line", "column", "expression",
]


def _0001(_endpoints: list, _opts) -> None:
    _p = Path(_opts.output_path)
    if _p.parent and not _p.parent.exists():
        _p.parent.mkdir(parents=True, exist_ok=True)
    with _p.open("w", encoding="utf-8", newline="") as _f:
        _w = csv.DictWriter(_f, fieldnames=_FIELDS)
        _w.writeheader()
        for _e in _endpoints:
            _w.writerow({
                "url": _e.url,
                "method": _e.method,
                "category": _e.category,
                "confidence": _e.confidence,
                "score": _e.score,
                "detector": _e.detector,
                "source_resource": _e.source_resource,
                "line": _e.line,
                "column": _e.column,
                "expression": _e.expression,
            })