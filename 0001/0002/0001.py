from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def _0001() -> dict:
    return {
        "scope": "same-origin",
        "depth": 1,
        "timeout": 15,
        "concurrency": 8,
        "rate_limit": 4.0,
        "cache": True,
        "verbosity": "normal",
    }


def _0002(_path) -> dict:
    _p = Path(_path)
    if not _p.is_file():
        raise FileNotFoundError(f"Configuration file not found: {_p}")
    _raw = _p.read_text(encoding="utf-8")
    if _p.suffix.lower() == ".json":
        try:
            _data: Any = json.loads(_raw)
        except json.JSONDecodeError as _e:
            raise ValueError(f"Configuration file is not valid JSON: {_e}") from None
    else:
        _data = _parse_toml_like(_raw)
    if not isinstance(_data, dict):
        raise ValueError("Configuration root must be an object/table.")
    return _data


def _parse_toml_like(_text: str) -> dict:
    try:
        import tomllib
        return tomllib.loads(_text)
    except ModuleNotFoundError:
        pass
    _out: dict = {}
    for _ln in _text.splitlines():
        _s = _ln.strip()
        if not _s or _s.startswith("#") or _s.startswith("["):
            continue
        if "=" not in _s:
            continue
        _k, _v = _s.split("=", 1)
        _out[_k.strip()] = _coerce(_v.strip())
    return _out


def _coerce(_v: str):
    _v = _v.split("#", 1)[0].strip()
    if _v.lower() in ("true", "false"):
        return _v.lower() == "true"
    try:
        if "." in _v:
            return float(_v)
        return int(_v)
    except ValueError:
        pass
    if _v.startswith('"') and _v.endswith('"'):
        return _v[1:-1]
    if _v.startswith("'") and _v.endswith("'"):
        return _v[1:-1]
    return _v


def _env_overrides() -> dict:
    _out: dict = {}
    _map = {
        "ENDPOINT_DISCOVERY_SCOPE": ("scope", str),
        "ENDPOINT_DISCOVERY_DEPTH": ("depth", int),
        "ENDPOINT_DISCOVERY_TIMEOUT": ("timeout", int),
        "ENDPOINT_DISCOVERY_CONCURRENCY": ("concurrency", int),
        "ENDPOINT_DISCOVERY_RATE_LIMIT": ("rate_limit", float),
        "ENDPOINT_DISCOVERY_VERBOSITY": ("verbosity", str),
    }
    for _k, (_field, _cast) in _map.items():
        if _k in os.environ:
            try:
                _out[_field] = _cast(os.environ[_k])
            except ValueError:
                pass
    if "ENDPOINT_DISCOVERY_CACHE" in os.environ:
        _out["cache"] = os.environ["ENDPOINT_DISCOVERY_CACHE"].lower() in (
            "1", "true", "yes", "on",
        )
    if "ENDPOINT_DISCOVERY_ALLOW_ORIGIN" in os.environ:
        _out["allowed_origins"] = [
            x.strip() for x in os.environ["ENDPOINT_DISCOVERY_ALLOW_ORIGIN"].split(",")
            if x.strip()
        ]
    return _out