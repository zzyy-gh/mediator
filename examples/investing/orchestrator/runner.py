"""Main orchestrator loop.

One pass:
  1. Run feeds whose cadence is due.
  2. For each open inquiry, dispatch the agent for the first pending section.
  3. Surface human gates (Collapse, constitution edits) to stdout.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

import anyio
from dotenv import load_dotenv

from .agent_runner import run_agent
from .state import (
    WORKSPACE,
    graph_snapshot_ref,
    iter_open_inquiries,
    resolve_agent,
)
from .feeds import all_feeds, run_due_feeds

load_dotenv(WORKSPACE / "orchestrator" / ".env")

POLL_INTERVAL_SEC = 30


async def dispatch_inquiries() -> None:
    """One pass over inquiries; dispatch one section per inquiry per pass."""
    for inq in iter_open_inquiries():
        section = inq.first_pending_section()
        if section is None:
            continue

        # Snapshot graph at first dispatch for reproducibility.
        if not inq.post.get("graph_snapshot"):
            inq.post["graph_snapshot"] = graph_snapshot_ref()
            inq._write()

        # Human gate? Surface and skip.
        if inq.owner.startswith("human:"):
            print(
                f"[GATE] {inq.path.name} :: section `{section}` "
                f"awaits {inq.owner}"
            )
            continue

        agent_id = resolve_agent(inq, section)
        if agent_id is None:
            print(
                f"[GATE] {inq.path.name} :: section `{section}` has no "
                f"resolvable agent (owner={inq.owner})"
            )
            continue

        print(f"[dispatch] {agent_id} -> {inq.path.name} :: {section}")
        try:
            await run_agent(agent_id, inq.path, section=section)
        except Exception as e:
            print(f"[error] {agent_id} on {inq.path.name}: {e}")


async def tick() -> None:
    await run_due_feeds(all_feeds())
    await dispatch_inquiries()


async def feeds_once() -> None:
    await run_due_feeds(all_feeds(), force=True)


async def watch() -> None:
    print(f"[runner] watching {WORKSPACE} every {POLL_INTERVAL_SEC}s")
    while True:
        await tick()
        await anyio.sleep(POLL_INTERVAL_SEC)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Loop forever")
    parser.add_argument("--feeds", action="store_true", help="Run feeds once and exit")
    args = parser.parse_args()

    if args.feeds:
        anyio.run(feeds_once)
        return

    if args.watch:
        anyio.run(watch)
    else:
        anyio.run(tick)


if __name__ == "__main__":
    main()
