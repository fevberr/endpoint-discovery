from __future__ import annotations

_API_HINTS = ("/api/", "/v1/", "/v2/", "/v3/", "/rest/", "/rpc/", "/graphql")
_AUTH_HINTS = ("/auth/", "/oauth/", "/login", "/logout", "/token", "/session")
_WS_HINTS = ("/ws", "/socket", "/realtime", "/live")


def _0001(_url: str) -> str:
    if not _url:
        return "unknown"
    _low = _url.lower()
    if _low.startswith(("ws://", "wss://")):
        return "websocket"
    if "graphql" in _low:
        return "graphql"
    if _low.startswith(("http://", "https://")):
        for _h in _WS_HINTS:
            if _h in _low:
                return "websocket"
        if any(_h in _low for _h in _AUTH_HINTS):
            return "authentication"
        if any(_h in _low for _h in _API_HINTS):
            return "api"
        return "absolute"
    if _low.startswith("/"):
        if any(_h in _low for _h in _AUTH_HINTS):
            return "authentication"
        if any(_h in _low for _h in _API_HINTS):
            return "api"
        if _low.endswith((".js", ".css", ".png", ".jpg", ".svg", ".ico")):
            return "static"
        return "relative"
    return "unknown"