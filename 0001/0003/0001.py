from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class _0001:
    url: str
    kind: str
    status: int = 0
    content_type: str = ""
    size: int = 0
    body: Optional[bytes] = None
    source: Optional[str] = None
    error: Optional[str] = None
    method: Optional[str] = None


@dataclass
class _0002:
    url: str
    method: str
    category: str
    confidence: str
    score: int
    detector: str
    source_resource: str
    line: int = 0
    column: int = 0
    expression: str = ""
    framework: Optional[str] = None
    parameters: list = field(default_factory=list)
    evidence: list = field(default_factory=list)


@dataclass
class _0003:
    resources: list = field(default_factory=list)
    endpoints: list = field(default_factory=list)
    frameworks: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    pages: int = 0
    bundles: int = 0
    maps: int = 0
    candidates: int = 0
    skipped_duplicates: int = 0