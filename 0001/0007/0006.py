from __future__ import annotations


def _0001(_endpoints: list, _opts) -> list:
    _out = list(_endpoints)
    if _opts.confidence:
        _out = [e for e in _out if e.confidence == _opts.confidence]
    if _opts.method:
        _out = [e for e in _out if e.method == _opts.method]
    if _opts.detector:
        _out = [e for e in _out if e.detector == _opts.detector]
    if _opts.prefix:
        _out = [e for e in _out if e.url.startswith(_opts.prefix)]
    _out.sort(key=lambda e: (-e.score, e.url, e.method, e.detector))
    return _out