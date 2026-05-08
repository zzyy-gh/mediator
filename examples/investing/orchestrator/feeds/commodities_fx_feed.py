"""Commodities & FX feed — uses yfinance proxies (handled by yfinance_feed for ETF tickers).

This module intentionally piggybacks on yfinance proxies (GLD, USO, DBC, UUP,
EURUSD=X, USDJPY=X, etc.) by depending on the universe in yfinance_feed.
Kept as a separate registry entry so the user can flip cadence or universe
independently later.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .graph_writer import write_block
from . import yfinance_feed

id = "feed.commodities-fx"
cadence_sec = 60 * 60 * 12  # twice daily

WORKSPACE = Path(__file__).resolve().parents[2]
MACRO_FILE = WORKSPACE / "graph" / "macro.md"

CFX_UNIVERSE: tuple[str, ...] = (
    "GLD", "USO", "DBC", "UUP",
    "EURUSD=X", "USDJPY=X", "GBPUSD=X",
    "TLT", "HYG", "LQD",
)


def run() -> None:
    # Reuse yfinance pull for these tickers; output goes to macro for these proxies.
    import yfinance as yf

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    blocks = []
    for sym in CFX_UNIVERSE:
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="3mo", interval="1d", auto_adjust=False)
            if hist is None or hist.empty:
                continue
            last = float(hist["Close"].iloc[-1])
            blocks.append(
                f"- id: macro.cfx_{sym.lower().replace('=', '_').replace('-', '_')}\n"
                f"  topic: macro\n"
                f"  content: \"{sym} (commodities/FX/duration proxy)\"\n"
                f"  last_close: {last}\n"
                f"  provenance:\n"
                f"    source: feed.commodities-fx\n"
                f"    timestamp: {ts}\n"
                f"  fuzz_halo: \"ETF / FX-cross proxy; not the underlying\""
            )
        except Exception as e:
            print(f"[{id}] {sym}: {e}")

    body = "```yaml\n" + "\n\n".join(blocks) + "\n```"
    write_block(MACRO_FILE, id, body)
    print(f"[{id}] wrote {len(blocks)} CFX proxy nodes")
