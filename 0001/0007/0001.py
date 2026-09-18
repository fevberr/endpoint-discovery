from __future__ import annotations

import shutil
import sys
from importlib import import_module


def _width() -> int:
    try:
        return max(60, min(96, shutil.get_terminal_size((80, 24)).columns))
    except Exception:
        return 80


def _0001(_endpoints: list, _res, _opts) -> None:
    _u = import_module("0001.0011.0003")
    _c = _u._0001(_u._enabled(_opts))
    _w = sys.stdout.write
    _W = _width()
    _inner = _W - 4

    _w("\n")
    _w(f"{_c.grey}  ╭─{_c.reset} {_c.bold}{_c.white}endpoint-discovery{_c.reset} "
       f"{_c.grey}{'─' * max(1, _inner - 22)}{_c.reset}\n")
    _w(f"{_c.grey}  │{_c.reset}\n")
    _target = _opts.target or _opts.file or "(none)"
    _w(f"{_c.grey}  │{_c.reset}  {_c.grey}target{_c.reset}    {_c.white}{_target}{_c.reset}\n")
    _w(f"{_c.grey}  │{_c.reset}  {_c.grey}scope{_c.reset}     {_c.cyan}{_opts.scope}{_c.reset}"
       f"   {_c.grey}depth{_c.reset} {_c.cyan}{_opts.depth}{_c.reset}"
       f"   {_c.grey}maps{_c.reset} {_c.cyan}{'on' if _opts.source_maps else 'off'}{_c.reset}"
       f"   {_c.grey}frameworks{_c.reset} {_c.cyan}{'on' if _opts.frameworks else 'off'}{_c.reset}\n")
    _w(f"{_c.grey}  ╰{'─' * (_W - 3)}{_c.reset}\n")

    _w("\n")
    _w(f"{_c.bold}{_c.white}  RESOURCES{_c.reset}\n")
    _w(_draw_metric(_c, "HTML", _res.pages, _c.green))
    _w(_draw_metric(_c, "JavaScript", _res.bundles, _c.blue))
    _w(_draw_metric(_c, "Source maps", _res.maps, _c.magenta))
    _w("\n")

    _w(f"{_c.bold}{_c.white}  ANALYSIS{_c.reset}\n")
    _w(_draw_metric(_c, "Candidates", _res.candidates, _c.yellow))
    _w(_draw_metric(_c, "Endpoints", len(_endpoints), _c.cyan))
    if _res.skipped_duplicates:
        _w(_draw_metric(_c, "Duplicates", _res.skipped_duplicates, _c.grey))
    _w("\n")

    _h = sum(1 for e in _endpoints if e.confidence == "high")
    _m = sum(1 for e in _endpoints if e.confidence == "medium")
    _l = sum(1 for e in _endpoints if e.confidence == "low")
    _total = max(1, len(_endpoints))
    _w(f"{_c.bold}{_c.white}  CONFIDENCE{_c.reset}\n")
    _w(_draw_bar(_c, "High", _h, _total, _c.green))
    _w(_draw_bar(_c, "Medium", _m, _total, _c.yellow))
    _w(_draw_bar(_c, "Low", _l, _total, _c.red))
    _w("\n")

    if _endpoints:
        _w(f"{_c.bold}{_c.white}  ENDPOINTS{_c.reset}  {_c.grey}({len(_endpoints)} total){_c.reset}\n")
        _w("\n")
        _max_url = min(60, max((len(e.url) for e in _endpoints[:40]), default=20))
        for _e in _endpoints[:40]:
            _badge = _u._badge(_c, _e.confidence)
            _method = _e.method[:6]
            _mc = _method_color(_c, _method)
            _url = _e.url
            if len(_url) > _max_url:
                _url = _url[: _max_url - 1] + "…"
            _cat = _e.category
            _w(f"    {_badge}  {_mc}{_method:<6}{_c.reset}  {_c.white}{_url}{_c.reset}\n")
            _src = _e.source_resource or ""
            _loc = f":{_e.line}" if _e.line else ""
            _w(f"              {_c.grey}{_cat}  ·  {_e.detector}  ·  {_src}{_loc}{_c.reset}\n")
        if len(_endpoints) > 40:
            _w(f"    {_c.grey}… and {len(_endpoints) - 40} more{_c.reset}\n")
        _w("\n")
    else:
        _w(f"  {_c.grey}No endpoints found.{_c.reset}\n\n")

    if _res.errors:
        _w(f"{_c.bold}{_c.red}  ERRORS{_c.reset}\n")
        for _err in _res.errors:
            _w(f"    {_c.red}✗{_c.reset}  {_err}\n")
        _w("\n")

    _w(f"{_c.grey}  done · {len(_endpoints)} endpoints · "
       f"{_h} high · {_m} medium · {_l} low{_c.reset}\n\n")


def _draw_metric(_c, _label: str, _value, _color: str) -> str:
    _l = f"  {_c.grey}{_label:<14}{_c.reset}"
    _v = f"{_color}{_c.bold}{_value:>6}{_c.reset}"
    return f"{_l}{_v}\n"


def _draw_bar(_c, _label: str, _count: int, _total: int, _color: str) -> str:
    _pct = int(round((_count / _total) * 100)) if _total else 0
    _bar_width = 30
    _filled = int(round((_count / _total) * _bar_width)) if _total else 0
    _bar = "█" * _filled + "░" * (_bar_width - _filled)
    _l = f"  {_c.grey}{_label:<14}{_c.reset}"
    _b = f"{_color}{_bar}{_c.reset}"
    _n = f"  {_c.white}{_count:>4}{_c.reset}  {_c.grey}{_pct:>3}%{_c.reset}"
    return f"{_l}{_b}{_n}\n"


def _method_color(_c, _method: str) -> str:
    _m = (_method or "").upper()
    if _m == "GET":
        return _c.green
    if _m == "POST":
        return _c.yellow
    if _m == "PUT":
        return _c.blue
    if _m == "PATCH":
        return _c.magenta
    if _m == "DELETE":
        return _c.red
    if _m in ("WS", "WSS"):
        return _c.cyan
    return _c.grey