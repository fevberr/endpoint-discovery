from __future__ import annotations


def _0001(_opts, _res) -> None:
    _seen = {}
    _out = []
    for _e in _res.endpoints:
        _key = (_e.url, _e.method, _e.detector)
        if _key in _seen:
            _existing = _seen[_key]
            _existing.evidence.extend(_e.evidence)
            _res.skipped_duplicates += 1
            continue
        _seen[_key] = _e
        _out.append(_e)
    _res.endpoints = _out