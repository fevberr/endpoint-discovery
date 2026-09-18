from __future__ import annotations

import os
import sys


def _enabled(_opts=None) -> bool:
    if _opts is not None and getattr(_opts, "no_color", False):
        return False
    if os.environ.get("NO_COLOR"):
        return False
    try:
        return sys.stdout.isatty()
    except Exception:
        return False


class _0001:
    def __init__(self, _on: bool):
        self._on = _on
        self.reset = "\033[0m" if _on else ""
        self.bold = "\033[1m" if _on else ""
        self.dim = "\033[2m" if _on else ""
        self.italic = "\033[3m" if _on else ""
        self.underline = "\033[4m" if _on else ""
        self.red = "\033[38;5;203m" if _on else ""
        self.green = "\033[38;5;114m" if _on else ""
        self.yellow = "\033[38;5;221m" if _on else ""
        self.blue = "\033[38;5;75m" if _on else ""
        self.magenta = "\033[38;5;176m" if _on else ""
        self.cyan = "\033[38;5;80m" if _on else ""
        self.grey = "\033[38;5;245m" if _on else ""
        self.white = "\033[38;5;255m" if _on else ""
        self.bg_high = "\033[48;5;22m\033[38;5;114m" if _on else ""
        self.bg_med = "\033[48;5;58m\033[38;5;221m" if _on else ""
        self.bg_low = "\033[48;5;52m\033[38;5;203m" if _on else ""


def _badge(_c: _0001, _level: str) -> str:
    _l = (_level or "").lower()
    if _l == "high":
        return f"{_c.bg_high}{_c.bold} HIGH {_c.reset}"
    if _l == "medium":
        return f"{_c.bg_med}{_c.bold} MED  {_c.reset}"
    if _l == "low":
        return f"{_c.bg_low}{_c.bold} LOW  {_c.reset}"
    return f" {_l.upper()} "


def _visible_len(_s: str) -> int:
    _n = 0
    _i = 0
    while _i < len(_s):
        if _s[_i] == "\033":
            while _i < len(_s) and _s[_i] != "m":
                _i += 1
            _i += 1
            continue
        _n += 1
        _i += 1
    return _n


def _pad(_s: str, _w: int) -> str:
    _v = _visible_len(_s)
    if _v >= _w:
        return _s
    return _s + (" " * (_w - _v))


def _rule(_c: _0001, _w: int = 66) -> str:
    return f"{_c.grey}{'─' * _w}{_c.reset}"


def _box_top(_c: _0001, _w: int = 66) -> str:
    return f"{_c.grey}╭{'─' * (_w - 2)}╮{_c.reset}"


def _box_bot(_c: _0001, _w: int = 66) -> str:
    return f"{_c.grey}╰{'─' * (_w - 2)}╯{_c.reset}"


def _box_row(_c: _0001, _content: str, _w: int = 66) -> str:
    _inner = _w - 4
    _padded = _pad(_content, _inner)
    return f"{_c.grey}│{_c.reset} {_padded} {_c.grey}│{_c.reset}"