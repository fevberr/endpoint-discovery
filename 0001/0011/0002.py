from __future__ import annotations

import sys

_ORDER = {"quiet": 0, "normal": 1, "verbose": 2, "debug": 3}


def _0001(_opts, _level: str, _msg: str) -> None:
    _current = _ORDER.get(getattr(_opts, "verbosity", "normal"), 1)
    _wanted = _ORDER.get(_level, 1)
    if _wanted > _current:
        return
    sys.stderr.write(f"[{_level}] {_msg}\n")