"""Feed registry. Each feed module exposes:
  - id: str
  - cadence_sec: int (0 means on-demand only)
  - run() -> None | Awaitable[None]   (sync or async)
"""
from __future__ import annotations

import inspect
import time
from pathlib import Path
from typing import Iterable, Protocol

from . import (
    commodities_fx_feed,
    crypto_feed,
    edgar_feed,
    fred_feed,
    news_summarizer,
    yfinance_feed,
)

WORKSPACE = Path(__file__).resolve().parents[2]
FEED_STATE = WORKSPACE / "orchestrator" / ".feed-state"


class Feed(Protocol):
    id: str
    cadence_sec: int

    def run(self): ...


def all_feeds() -> list:
    return [
        yfinance_feed,
        fred_feed,
        edgar_feed,
        crypto_feed,
        commodities_fx_feed,
        news_summarizer,
    ]


def _last_run_path(feed_id: str) -> Path:
    return FEED_STATE / f"{feed_id}.last"


def _last_run(feed_id: str) -> float:
    p = _last_run_path(feed_id)
    if not p.exists():
        return 0.0
    try:
        return float(p.read_text().strip())
    except ValueError:
        return 0.0


def _mark_run(feed_id: str) -> None:
    FEED_STATE.mkdir(parents=True, exist_ok=True)
    _last_run_path(feed_id).write_text(str(time.time()))


async def run_due_feeds(feeds: Iterable, *, force: bool = False) -> None:
    now = time.time()
    for feed in feeds:
        cadence = getattr(feed, "cadence_sec", 0)
        last = _last_run(feed.id)
        if not force and cadence > 0 and (now - last) < cadence:
            continue
        try:
            print(f"[feed] {feed.id} running")
            result = feed.run()
            if inspect.isawaitable(result):
                await result
            _mark_run(feed.id)
        except Exception as e:
            print(f"[feed] {feed.id} failed: {e}")
