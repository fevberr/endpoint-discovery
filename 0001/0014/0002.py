from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class _0002:
    mode: str
    allowed_origins: list = field(default_factory=list)
    allow_private: bool = False
    origin_host: str = ""


def _0001(_mode: str, _allowed: list, _allow_private: bool):
    return _0002(
        mode=_mode,
        allowed_origins=list(_allowed or []),
        allow_private=bool(_allow_private),
    )