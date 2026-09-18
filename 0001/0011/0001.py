from __future__ import annotations

_STATE = {"level": "normal"}


def _0001(_level: str) -> None:
    _STATE["level"] = _level


def _0002() -> str:
    return _STATE["level"]