"""Crypto feed — CoinGecko public API for spot prices and market caps."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import requests

from .graph_writer import write_block

id = "feed.crypto"
cadence_sec = 60 * 60  # hourly

WORKSPACE = Path(__file__).resolve().parents[2]
TECHNICALS_FILE = WORKSPACE / "graph" / "technicals.md"

DEFAULT_COINS = (
    "bitcoin",
    "ethereum",
    "solana",
    "ripple",
    "cardano",
)


def run() -> None:
    ids = ",".join(DEFAULT_COINS)
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={ids}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"
    )
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"[{id}] failed: {e}")
        return

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    blocks = []
    for coin, fields in data.items():
        price = fields.get("usd")
        mcap = fields.get("usd_market_cap")
        chg = fields.get("usd_24h_change")
        blocks.append(
            f"- id: technicals.crypto_{coin}\n"
            f"  topic: technicals\n"
            f"  content: \"{coin} spot via CoinGecko\"\n"
            f"  price_usd: {price}\n"
            f"  market_cap_usd: {mcap}\n"
            f"  change_24h_pct: {chg}\n"
            f"  provenance:\n"
            f"    source: feed.crypto\n"
            f"    timestamp: {ts}"
        )

    body = "```yaml\n" + "\n\n".join(blocks) + "\n```"
    write_block(TECHNICALS_FILE, id, body)
    print(f"[{id}] wrote {len(blocks)} crypto nodes")
