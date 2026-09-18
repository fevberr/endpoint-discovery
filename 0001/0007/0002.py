from __future__ import annotations

import json


def _0001(_endpoints: list, _res, _opts) -> str:
    _doc = {
        "target": _opts.target or _opts.file,
        "scope": _opts.scope,
        "summary": {
            "pages": _res.pages,
            "bundles": _res.bundles,
            "sourcemaps": _res.maps,
            "candidates": _res.candidates,
            "endpoints": len(_endpoints),
        },
        "endpoints": [
            {
                "url": _e.url,
                "method": _e.method,
                "category": _e.category,
                "confidence": _e.confidence,
                "score": _e.score,
                "detector": _e.detector,
                "source": _e.source_resource,
                "line": _e.line,
                "column": _e.column,
                "parameters": list(_e.parameters),
                "evidence": list(_e.evidence),
            }
            for _e in _endpoints
        ],
        "errors": list(_res.errors),
    }
    return json.dumps(_doc, indent=2, sort_keys=True)