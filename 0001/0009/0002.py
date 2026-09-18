from __future__ import annotations

import json
from pathlib import Path


def _0001(_opts, _res) -> None:
    _nodes = []
    _edges = []
    _seen = set()
    for _r in _res.resources:
        if _r.url not in _seen:
            _seen.add(_r.url)
            _nodes.append({"id": _r.url, "kind": _r.kind})
    for _e in _res.endpoints:
        if _e.url not in _seen:
            _seen.add(_e.url)
            _nodes.append({"id": _e.url, "kind": "endpoint"})
        _edges.append({
            "from": _e.source_resource,
            "to": _e.url,
            "detector": _e.detector,
            "confidence": _e.confidence,
        })
    _g = {"nodes": _nodes, "edges": _edges}
    Path(_opts.graph_path).write_text(
        json.dumps(_g, indent=2, sort_keys=True), encoding="utf-8",
    )