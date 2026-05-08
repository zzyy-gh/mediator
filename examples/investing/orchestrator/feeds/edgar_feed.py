"""SEC EDGAR feed — stub.

On-demand pulls for tickers referenced in active inquiries; weekly sweep
across the watch universe in graph/strategies.md. Full implementation
requires per-form parsing (10-K, 10-Q, 8-K) and rate-limit etiquette.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .graph_writer import write_block

id = "feed.edgar"
cadence_sec = 60 * 60 * 24 * 7  # weekly sweep

WORKSPACE = Path(__file__).resolve().parents[2]
FUNDAMENTALS_FILE = WORKSPACE / "graph" / "fundamentals.md"


def run() -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    body = (
        f"# Stub feed — wire up edgar pulls per inquiry.\n"
        f"# last_attempt: {ts}\n"
    )
    write_block(FUNDAMENTALS_FILE, id, body)
    print(f"[{id}] stub written; replace with real EDGAR client")
