from __future__ import annotations

import argparse
import sys
from importlib import import_module


def _0002() -> argparse.ArgumentParser:
    _p = argparse.ArgumentParser(
        prog="endpoint-discovery",
        description="Static endpoint and web reconnaissance framework.",
    )
    _p.add_argument("target", nargs="?", help="Target URL, e.g. https://example.com")
    _p.add_argument("--file", help="Analyze a local HTML or JS file instead of a URL.")
    _p.add_argument("--json", dest="output_format", action="store_const", const="json")
    _p.add_argument("--jsonl", dest="output_format", action="store_const", const="jsonl")
    _p.add_argument("--csv", dest="output_path", help="Write CSV to this path.")
    _p.add_argument("--sarif", dest="sarif_path", help="Write SARIF to this path.")
    _p.add_argument("--sqlite", dest="sqlite_path", help="Write findings to SQLite.")
    _p.add_argument("--graph", dest="graph_path", help="Write relationship graph JSON.")
    _p.add_argument("--scope", choices=["same-origin", "host", "any"], default=None)
    _p.add_argument("--allow-origin", action="append", default=None, dest="allowed_origins")
    _p.add_argument("--depth", type=int, default=None)
    _p.add_argument("--source-maps", action="store_true", default=None)
    _p.add_argument("--frameworks", action="store_true", default=None)
    _p.add_argument("--confidence", choices=["high", "medium", "low"], default=None)
    _p.add_argument("--method", default=None)
    _p.add_argument("--prefix", default=None)
    _p.add_argument("--detector", default=None)
    _p.add_argument("--resource-type", default=None)
    _p.add_argument("--timeout", type=int, default=None)
    _p.add_argument("--max-bytes", type=int, default=None)
    _p.add_argument("--max-redirects", type=int, default=None)
    _p.add_argument("--concurrency", type=int, default=None)
    _p.add_argument("--rate-limit", type=float, default=None)
    _p.add_argument("--no-cache", dest="cache", action="store_false", default=None)
    _p.add_argument("--cache-ttl", type=int, default=None)
    _p.add_argument("--interactive", action="store_true", default=False)
    _p.add_argument("--verbose", action="store_true", default=None)
    _p.add_argument("--debug", action="store_true", default=None)
    _p.add_argument("--quiet", action="store_true", default=None)
    _p.add_argument("--allow-private", action="store_true", default=None)
    _p.add_argument("--config", dest="config_path", default=None)
    _p.add_argument("--no-color", action="store_true", default=None)
    _p.add_argument("--version", action="version", version="endpoint-discovery 1.0.0")
    return _p


def _0003(_argv: list):
    _opts_mod = import_module("0001.0001.0001")
    _cfg_mod = import_module("0001.0002.0003")
    _ns = _0002().parse_args(_argv)
    _opts = _opts_mod._0001()
    _opts.target = _ns.target
    _opts.file = _ns.file
    if _ns.output_format:
        _opts.output_format = _ns.output_format
    if _ns.output_path:
        _opts.output_path = _ns.output_path
        _opts.output_format = "csv"
    if _ns.sarif_path:
        _opts.sarif_path = _ns.sarif_path
    if _ns.sqlite_path:
        _opts.sqlite_path = _ns.sqlite_path
    if _ns.graph_path:
        _opts.graph_path = _ns.graph_path
    if _ns.scope:
        _opts.scope = _ns.scope
    if _ns.allowed_origins:
        _opts.allowed_origins = list(_ns.allowed_origins)
    if _ns.depth is not None:
        _opts.depth = _ns.depth
    if _ns.source_maps is not None:
        _opts.source_maps = bool(_ns.source_maps)
    if _ns.frameworks is not None:
        _opts.frameworks = bool(_ns.frameworks)
    if _ns.confidence:
        _opts.confidence = _ns.confidence
    if _ns.method:
        _opts.method = _ns.method.upper()
    if _ns.prefix:
        _opts.prefix = _ns.prefix
    if _ns.detector:
        _opts.detector = _ns.detector
    if _ns.resource_type:
        _opts.resource_type = _ns.resource_type
    if _ns.timeout is not None:
        _opts.timeout = _ns.timeout
    if _ns.max_bytes is not None:
        _opts.max_bytes = _ns.max_bytes
    if _ns.max_redirects is not None:
        _opts.max_redirects = _ns.max_redirects
    if _ns.concurrency is not None:
        _opts.concurrency = _ns.concurrency
    if _ns.rate_limit is not None:
        _opts.rate_limit = _ns.rate_limit
    if _ns.cache is False:
        _opts.cache = False
    if _ns.cache_ttl is not None:
        _opts.cache_ttl = _ns.cache_ttl
    if _ns.interactive:
        _opts.interactive = True
    if _ns.verbose:
        _opts.verbosity = "verbose"
    if _ns.debug:
        _opts.verbosity = "debug"
    if _ns.quiet:
        _opts.verbosity = "quiet"
    if _ns.allow_private is not None:
        _opts.allow_private = bool(_ns.allow_private)
    if _ns.config_path:
        _opts.config_path = _ns.config_path
    if _ns.no_color is not None:
        _opts.no_color = bool(_ns.no_color)
    _opts = _cfg_mod._0003(_opts)
    return _opts


def _0001(_argv: list = None) -> int:
    _argv = list(sys.argv[1:] if _argv is None else _argv)
    try:
        _opts = _0003(_argv)
    except Exception as _e:
        sys.stderr.write(f"Configuration error: {_e}\n")
        return 2
    _log_mod = import_module("0001.0011.0001")
    _banner_mod = import_module("0001.0001.0004")
    _run_mod = import_module("0001.0003.0003")
    _log_mod._0001(_opts.verbosity)
    if not _opts.target and not _opts.file:
        sys.stderr.write(
            "No target provided.\n"
            "Try: endpoint-discovery https://example.com\n"
            "Or:  endpoint-discovery --file page.html\n"
        )
        return 2
    if _opts.verbosity != "quiet":
        sys.stdout.write(_banner_mod._0002(_opts))
    try:
        return _run_mod._0003(_opts)
    except KeyboardInterrupt:
        sys.stderr.write("\nInterrupted.\n")
        return 130


if __name__ == "__main__":
    raise SystemExit(_0001())