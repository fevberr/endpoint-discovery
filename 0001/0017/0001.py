from __future__ import annotations

import re

_SECRET_RE = re.compile(
    r"(?i)(authorization|api[_-]?key|access[_-]?token|secret|password)"
    r"\s*[:=]\s*['\"]?([^'\"\s,;]{8,})['\"]?"
)


def _0001(_text: str) -> str:
    if not _text:
        return ""
    return _SECRET_RE.sub(lambda m: f"{m.group(1)}=<redacted>", _text)