from __future__ import annotations

_DETECTOR_WEIGHT = {
    "fetch": 50,
    "xhr": 50,
    "axios": 55,
    "websocket": 45,
    "html": 30,
    "form": 30,
    "preload": 25,
    "regex": 20,
}


def _0001(_detector: str, _url: str) -> int:
    _score = _DETECTOR_WEIGHT.get(_detector, 10)
    _low = (_url or "").lower()
    if _low.startswith(("/api/", "/v1/", "/v2/", "/v3/")):
        _score += 35
    elif _low.startswith("/"):
        _score += 15
    elif _low.startswith(("http://", "https://")):
        _score += 10
    if _low.startswith(("ws://", "wss://")):
        _score += 10
    if "graphql" in _low:
        _score += 5
    if not any(c.isalpha() for c in _low):
        _score -= 10
    return max(0, min(100, _score))