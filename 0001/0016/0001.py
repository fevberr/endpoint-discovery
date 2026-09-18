from __future__ import annotations

import asyncio
from importlib import import_module


def _guess_kind(_url: str, _content_type: str) -> str:
    _low = (_content_type or "").lower()
    if "html" in _low:
        return "html"
    if "javascript" in _low or "ecmascript" in _low:
        return "javascript"
    if "json" in _low and _url.endswith(".map"):
        return "sourcemap"
    _u = _url.lower()
    if _u.endswith((".html", ".htm")):
        return "html"
    if _u.endswith((".js", ".mjs", ".cjs")):
        return "javascript"
    if _u.endswith(".map"):
        return "sourcemap"
    return "other"


async def _0001(_opts, _urls: list, _scope, _max_bytes: int, _timeout: int) -> list:
    _r_mod = import_module("0001.0003.0001")
    _priv = import_module("0001.0014.0003")
    try:
        import httpx
    except ImportError:
        return [_r_mod._0001(url=_u, kind="other") for _u in _urls]
    _limits = httpx.Limits(
        max_connections=max(1, _opts.concurrency),
        max_keepalive_connections=max(1, _opts.concurrency),
    )
    _sem = asyncio.Semaphore(max(1, _opts.concurrency))

    async with httpx.AsyncClient(
        timeout=_timeout,
        follow_redirects=True,
        max_redirects=_opts.max_redirects,
        limits=_limits,
        headers={"User-Agent": "endpoint-discovery/1.0"},
    ) as _client:
        async def _fetch_one(_u: str):
            async with _sem:
                _r = _r_mod._0001(url=_u, kind="other")
                if _priv._0001(_u) and not _opts.allow_private:
                    _r.error = "blocked private target"
                    return _r
                try:
                    _resp = await _client.get(_u)
                except Exception as _e:
                    _r.error = str(_e)
                    return _r
                _body = _resp.content[:_max_bytes]
                _ct = _resp.headers.get("content-type", "")
                _r.kind = _guess_kind(_u, _ct)
                _r.status = _resp.status_code
                _r.content_type = _ct
                _r.size = len(_body)
                _r.body = _body
                return _r

        _coros = [_fetch_one(_u) for _u in _urls]
        _results = await asyncio.gather(*_coros, return_exceptions=False)
    return list(_results)