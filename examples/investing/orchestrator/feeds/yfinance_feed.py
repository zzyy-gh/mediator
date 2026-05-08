"""yfinance feed — daily price/volume + simple vol-regime nodes for a curated universe.

Writes to graph/technicals.md (and optionally graph/fundamentals.md).
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .graph_writer import write_block

id = "feed.yfinance"
cadence_sec = 60 * 60 * 6  # every 6 hours

WORKSPACE = Path(__file__).resolve().parents[2]
TECHNICALS_FILE = WORKSPACE / "graph" / "technicals.md"

# Curated universe across asset classes. Edit this list to expand coverage.
DEFAULT_UNIVERSE: tuple[str, ...] = (
    # Equity broad indices / ETFs
    "SPY", "QQQ", "IWM", "EFA", "EEM",
    # Sectors
    "XLK", "XLE", "XLF", "XLV", "XLI", "XLU", "XLY", "XLP", "XLB", "XLRE",
    # Single names commonly referenced
    "GOOG", "NVDA", "TSLA", "BRK-B",
    # Macro / commodities / FX proxies
    "GLD", "USO", "DBC", "UUP", "TLT", "HYG", "LQD",
    # Crypto proxies via yfinance
    "BTC-USD", "ETH-USD",
)


def _compute_vol_regime(close_series) -> dict:
    """Compute a simple realised-vol summary from a daily close series."""
    import numpy as np

    if close_series is None or len(close_series) < 30:
        return {"realised_30d_pct": None, "n_obs": 0}
    rets = close_series.pct_change().dropna()
    realised_30d = float(rets.tail(30).std() * (252 ** 0.5) * 100)
    return {
        "realised_30d_pct": round(realised_30d, 2),
        "n_obs": int(len(rets)),
    }


def _yaml_node(symbol: str, last_close: float, vol: dict, ts: str) -> str:
    return (
        f"- id: technicals.{symbol.lower().replace('-', '_')}\n"
        f"  topic: technicals\n"
        f"  content: \"{symbol} daily close + realised vol\"\n"
        f"  last_close: {last_close}\n"
        f"  vol_regime: {vol}\n"
        f"  provenance:\n"
        f"    source: feed.yfinance\n"
        f"    timestamp: {ts}\n"
        f"  fuzz_halo: \"yahoo data; occasional revisions\""
    )


def run(universe: Iterable[str] = DEFAULT_UNIVERSE) -> None:
    import yfinance as yf

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    blocks = []
    for sym in universe:
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="6mo", interval="1d", auto_adjust=False)
            if hist is None or hist.empty:
                continue
            last_close = float(hist["Close"].iloc[-1])
            vol = _compute_vol_regime(hist["Close"])
            blocks.append(_yaml_node(sym, last_close, vol, ts))
        except Exception as e:
            print(f"[{id}] {sym}: {e}")

    body = "```yaml\n" + "\n\n".join(blocks) + "\n```"
    write_block(TECHNICALS_FILE, id, body)
    print(f"[{id}] wrote {len(blocks)} nodes to {TECHNICALS_FILE.name}")
