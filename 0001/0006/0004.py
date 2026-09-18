from __future__ import annotations

import sqlite3
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS endpoints (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  method TEXT NOT NULL,
  category TEXT NOT NULL,
  confidence TEXT NOT NULL,
  score INTEGER NOT NULL,
  detector TEXT NOT NULL,
  source_resource TEXT NOT NULL,
  line INTEGER NOT NULL DEFAULT 0,
  column INTEGER NOT NULL DEFAULT 0,
  expression TEXT NOT NULL DEFAULT '',
  framework TEXT
);
CREATE TABLE IF NOT EXISTS parameters (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  endpoint_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  kind TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS evidence (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  endpoint_id INTEGER NOT NULL,
  text TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS resources (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  kind TEXT NOT NULL,
  status INTEGER NOT NULL DEFAULT 0,
  size INTEGER NOT NULL DEFAULT 0,
  content_type TEXT NOT NULL DEFAULT ''
);
CREATE UNIQUE INDEX IF NOT EXISTS ux_endpoints_key
  ON endpoints(url, method, detector);
CREATE INDEX IF NOT EXISTS ix_endpoints_confidence ON endpoints(confidence);
CREATE INDEX IF NOT EXISTS ix_endpoints_category ON endpoints(category);
"""


def _0001(_opts, _res):
    _p = Path(_opts.sqlite_path)
    if _p.parent and not _p.parent.exists():
        _p.parent.mkdir(parents=True, exist_ok=True)
    _conn = sqlite3.connect(str(_p))
    try:
        _conn.executescript(_SCHEMA)
        for _r in _res.resources:
            _conn.execute(
                "INSERT INTO resources(url, kind, status, size, content_type) "
                "VALUES (?, ?, ?, ?, ?)",
                (_r.url, _r.kind, _r.status, _r.size, _r.content_type),
            )
        for _e in _res.endpoints:
            _cur = _conn.execute(
                "INSERT OR IGNORE INTO endpoints"
                "(url, method, category, confidence, score, detector, "
                " source_resource, line, column, expression, framework) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (_e.url, _e.method, _e.category, _e.confidence, _e.score,
                 _e.detector, _e.source_resource, _e.line, _e.column,
                 _e.expression, _e.framework),
            )
            if _cur.rowcount:
                _eid = _cur.lastrowid
                for _pname in _e.parameters:
                    _conn.execute(
                        "INSERT INTO parameters(endpoint_id, name, kind) VALUES (?, ?, ?)",
                        (_eid, str(_pname), "unknown"),
                    )
                for _ev in _e.evidence:
                    _conn.execute(
                        "INSERT INTO evidence(endpoint_id, text) VALUES (?, ?)",
                        (_eid, str(_ev)),
                    )
        _conn.commit()
    finally:
        _conn.close()
    return _p