from __future__ import annotations

import ipaddress
from urllib.parse import urlsplit


def _0001(_url: str) -> bool:
    try:
        _p = urlsplit(_url)
    except ValueError:
        return False
    _host = (_p.hostname or "").lower()
    if not _host:
        return False
    if _host == "localhost":
        return True
    try:
        _ip = ipaddress.ip_address(_host)
        return _ip.is_private or _ip.is_loopback or _ip.is_link_local
    except ValueError:
        pass
    return False