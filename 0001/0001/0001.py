from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class _0001:
    target: Optional[str] = None
    file: Optional[str] = None
    output_format: str = "terminal"
    output_path: Optional[str] = None
    scope: str = "same-origin"
    allowed_origins: list = field(default_factory=list)
    depth: int = 1
    source_maps: bool = False
    frameworks: bool = False
    confidence: Optional[str] = None
    method: Optional[str] = None
    prefix: Optional[str] = None
    detector: Optional[str] = None
    resource_type: Optional[str] = None
    timeout: int = 15
    max_bytes: int = 5_000_000
    max_redirects: int = 5
    concurrency: int = 8
    rate_limit: float = 4.0
    cache: bool = True
    cache_ttl: int = 3600
    cache_max_entries: int = 4096
    sqlite_path: Optional[str] = None
    sarif_path: Optional[str] = None
    graph_path: Optional[str] = None
    interactive: bool = False
    verbosity: str = "normal"
    allow_private: bool = False
    config_path: Optional[str] = None
    no_color: bool = False