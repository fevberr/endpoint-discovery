from __future__ import annotations

from pathlib import Path
from importlib import import_module


def _0001(_opts):
    _r = import_module("0001.0003.0001")
    _scope_mod = import_module("0001.0014.0002")
    _url_mode = import_module("0001.0003.0004")
    _file_mode = import_module("0001.0005.0005")
    _res = _r._0003()
    _scope = _scope_mod._0001(_opts.scope, _opts.allowed_origins, _opts.allow_private)
    if _opts.file:
        return _file_mode._0005(_opts, _res, _scope)
    return _url_mode._0004(_opts, _res, _scope)


def _promote_html_resources(_res, _opts) -> None:
    _endpoint = import_module("0001.0003.0001")
    _known = {(e.url, e.method, e.detector) for e in _res.endpoints}
    for _r in _res.resources:
        if _r.source is None or _r.source == "html":
            continue
        if _r.kind not in ("form", "javascript", "stylesheet", "other"):
            continue
        if _r.kind == "form":
            _det = "form"
            _method = (_r.method or "GET").upper()
        elif _r.kind == "javascript":
            _det = "html"
            _method = "GET"
        else:
            _det = "preload"
            _method = "GET"
        _key = (_r.url, _method, _det)
        if _key in _known:
            continue
        _known.add(_key)
        _e = _endpoint._0002(
            url=_r.url,
            method=_method,
            category="unknown",
            confidence="low",
            score=0,
            detector=_det,
            source_resource=_r.source or "html",
            line=0,
            column=0,
            expression="html-ref",
        )
        _res.endpoints.append(_e)
        _res.candidates += 1


def _0003(_opts) -> int:
    _log = import_module("0001.0011.0002")
    _cls = import_module("0001.0008.0001")
    _conf = import_module("0001.0008.0002")
    _dedup = import_module("0001.0008.0003")
    _analyze = import_module("0001.0012.0002")
    _filt = import_module("0001.0007.0006")
    _term = import_module("0001.0007.0001")
    _js = import_module("0001.0007.0002")
    _jl = import_module("0001.0007.0003")
    _csv = import_module("0001.0007.0004")
    _sarif = import_module("0001.0007.0005")
    _sql = import_module("0001.0006.0004")
    _graph = import_module("0001.0009.0002")
    _endpoint = import_module("0001.0003.0001")

    _res = _0001(_opts)
    _promote_html_resources(_res, _opts)

    _log._0001(_opts, "verbose", "Analyzing JavaScript bundles")
    _seen = set()
    for _rr in list(_res.resources):
        if _rr.kind != "javascript" or not _rr.body:
            continue
        if _rr.url in _seen:
            continue
        _seen.add(_rr.url)
        try:
            _findings = _analyze._0001(_rr, _opts)
        except Exception as _e:
            _log._0001(_opts, "verbose", f"Analyzer error on {_rr.url}: {_e}")
            continue
        for _f in _findings:
            _e = _endpoint._0002(
                url=_f.get("url", ""),
                method=_f.get("method", "UNKNOWN"),
                category="unknown",
                confidence="low",
                score=0,
                detector=_f.get("detector", "unknown"),
                source_resource=_rr.url,
                line=int(_f.get("line", 0) or 0),
                column=int(_f.get("column", 0) or 0),
                expression=_f.get("expression", ""),
            )
            if not _e.url:
                continue
            _res.candidates += 1
            _res.endpoints.append(_e)
    for _e in _res.endpoints:
        _e.category = _cls._0001(_e.url)
        _score = _conf._0001(_e.detector, _e.url)
        _e.score = _score
        if _score >= 80:
            _e.confidence = "high"
        elif _score >= 50:
            _e.confidence = "medium"
        else:
            _e.confidence = "low"
        _e.evidence.append(f"detector={_e.detector}")
        _e.evidence.append(f"score={_score}")
    _dedup._0001(_opts, _res)
    _filtered = _filt._0001(_res.endpoints, _opts)
    if _opts.output_format == "json":
        _out = _js._0001(_filtered, _res, _opts)
        if _opts.output_path:
            Path(_opts.output_path).write_text(_out, encoding="utf-8")
            print(f"Wrote JSON to {_opts.output_path}")
        else:
            print(_out)
    elif _opts.output_format == "jsonl":
        _out = _jl._0001(_filtered, _res, _opts)
        if _opts.output_path:
            Path(_opts.output_path).write_text(_out, encoding="utf-8")
        else:
            print(_out)
    elif _opts.output_format == "csv":
        if not _opts.output_path:
            _opts.output_path = "results.csv"
        _csv._0001(_filtered, _opts)
        print(f"Wrote {len(_filtered)} endpoints to {_opts.output_path}")
    else:
        _term._0001(_filtered, _res, _opts)
    if _opts.sarif_path:
        _sarif._0001(_filtered, _opts.sarif_path)
    if _opts.sqlite_path:
        _sql._0001(_opts, _res)
    if _opts.graph_path:
        _graph._0001(_opts, _res)
    return 0 if not _res.errors else 1