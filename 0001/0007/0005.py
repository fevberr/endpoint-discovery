from __future__ import annotations

import json
from pathlib import Path


def _0001(_endpoints: list, _path) -> None:
    _results = []
    for _e in _endpoints:
        _results.append({
            "ruleId": f"endpoint/{_e.detector}",
            "level": "note",
            "message": {"text": f"{_e.method} {_e.url}"},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {"uri": _e.source_resource},
                    "region": {"startLine": max(1, _e.line)},
                }
            }],
            "properties": {
                "confidence": _e.confidence,
                "score": _e.score,
                "category": _e.category,
            },
        })
    _doc = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {"driver": {
                "name": "endpoint-discovery",
                "informationUri": "https://example.invalid/",
                "rules": [],
            }},
            "results": _results,
        }],
    }
    Path(_path).write_text(json.dumps(_doc, indent=2, sort_keys=True), encoding="utf-8")