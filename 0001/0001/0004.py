from __future__ import annotations

import sys

_VERSION = "1.0.0"


def _0001() -> str:
    return _VERSION


def _0002(_opts) -> str:
    if _opts.no_color or not sys.stdout.isatty():
        return (
            f"endpoint-discovery {_VERSION}\n"
            f"mode        {'interactive' if _opts.interactive else 'batch'}\n"
            f"scope       {_opts.scope}\n"
            f"depth       {_opts.depth}\n"
            f"source-maps {'on' if _opts.source_maps else 'off'}\n"
            f"frameworks  {'on' if _opts.frameworks else 'off'}\n"
        )
    return (
        f"\033[1mendpoint-discovery\033[0m \033[2m{_VERSION}\033[0m\n"
        f"\033[2mmode\033[0m        {'interactive' if _opts.interactive else 'batch'}\n"
        f"\033[2mscope\033[0m       {_opts.scope}\n"
        f"\033[2mdepth\033[0m       {_opts.depth}\n"
        f"\033[2msource-maps\033[0m {'on' if _opts.source_maps else 'off'}\n"
        f"\033[2mframeworks\033[0m  {'on' if _opts.frameworks else 'off'}\n"
    )