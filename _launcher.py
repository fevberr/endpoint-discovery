from __future__ import annotations

import importlib
import os
import sys


def main() -> int:
    _root = os.path.dirname(os.path.abspath(__file__))
    if _root not in sys.path:
        sys.path.insert(0, _root)
    _m = importlib.import_module("0001.0001.0002")
    return _m._0001(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())