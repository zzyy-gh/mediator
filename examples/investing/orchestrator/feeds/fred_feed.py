"""FRED feed — minimum macro panel into graph/macro.md."""
from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

from .graph_writer import write_block

id = "feed.fred"
cadence_sec = 60 * 60 * 12  # twice daily

WORKSPACE = Path(__file__).resolve().parents[2]
MACRO_FILE = WORKSPACE / "graph" / "macro.md"

# (series_id, human_label)
DEFAULT_SERIES: tuple[tuple[str, str], ...] = (
    ("DGS10", "10y treasury yield"),
    ("DGS2", "2y treasury yield"),
    ("DFF", "fed funds effective"),
    ("CPIAUCSL", "headline CPI level"),
    ("PCEPI", "PCE price index"),
    ("UNRATE", "unemployment rate"),
    ("PAYEMS", "nonfarm payrolls"),
    ("DTWEXBGS", "broad dollar index"),
)


def _yaml_node(sid: str, label: str, value: float, asof: str, ts: str) -> str:
    return (
        f"- id: macro.{sid.lower()}\n"
        f"  topic: macro\n"
        f"  content: \"{label}\"\n"
        f"  value: {value}\n"
        f"  as_of: {asof}\n"
        f"  provenance:\n"
        f"    source: feed.fred\n"
        f"    series_id: {sid}\n"
        f"    timestamp: {ts}"
    )


def run() -> None:
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print(f"[{id}] FRED_API_KEY not set; skipping")
        return
    from fredapi import Fred

    fred = Fred(api_key=api_key)
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    blocks = []
    for sid, label in DEFAULT_SERIES:
        try:
            s = fred.get_series(sid).dropna()
            if s.empty:
                continue
            value = float(s.iloc[-1])
            asof = s.index[-1].date().isoformat()
            blocks.append(_yaml_node(sid, label, value, asof, ts))
        except Exception as e:
            print(f"[{id}] {sid}: {e}")

    body = "```yaml\n" + "\n\n".join(blocks) + "\n```"
    write_block(MACRO_FILE, id, body)
    print(f"[{id}] wrote {len(blocks)} nodes to {MACRO_FILE.name}")
