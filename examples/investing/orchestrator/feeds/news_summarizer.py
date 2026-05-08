"""News summarizer feed — RSS in, structured graph nodes out via Claude.

Reads a configurable RSS list (env: NEWS_RSS_URLS, comma-separated). Pulls
recent items, batches them into a single Claude call that returns YAML node
blocks for sentiment / themes / politics. Written here as a single-call
summariser to keep cost predictable; can later be split per topic.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

from .graph_writer import write_block

id = "feed.news-summarizer"
cadence_sec = 60 * 60  # hourly

WORKSPACE = Path(__file__).resolve().parents[2]
SENTIMENT_FILE = WORKSPACE / "graph" / "sentiment.md"
THEMES_FILE = WORKSPACE / "graph" / "themes.md"
POLITICS_FILE = WORKSPACE / "graph" / "politics.md"

DEFAULT_FEEDS: tuple[str, ...] = (
    "https://www.federalreserve.gov/feeds/press_all.xml",
    "https://feeds.reuters.com/reuters/businessNews",
    "https://feeds.reuters.com/reuters/marketsNews",
)

LOOKBACK_HOURS = 24


def _collect_items() -> list[dict]:
    import feedparser

    urls = os.environ.get("NEWS_RSS_URLS")
    feeds = tuple(u.strip() for u in urls.split(",")) if urls else DEFAULT_FEEDS
    cutoff = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
    out: list[dict] = []
    for url in feeds:
        try:
            parsed = feedparser.parse(url)
            for entry in parsed.entries[:30]:
                title = getattr(entry, "title", "")
                summary = getattr(entry, "summary", "") or getattr(entry, "description", "")
                link = getattr(entry, "link", "")
                out.append({"title": title, "summary": summary, "link": link, "source": url})
        except Exception as e:
            print(f"[{id}] {url}: {e}")
    return out


async def _summarise(items: list[dict]) -> str:
    """Single Claude call returns three YAML blocks (sentiment, themes, politics)."""
    from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

    items_text = "\n\n".join(
        f"- title: {it['title']}\n  source: {it['source']}\n  link: {it['link']}\n  summary: {it['summary'][:600]}"
        for it in items
    )
    prompt = (
        "You are a news summariser writing into a graph of macro / market state.\n\n"
        "Input items follow. Produce three YAML node lists:\n"
        "  1. sentiment nodes (id: sentiment.<topic>) — bounded distributions [-1, 1] with mean and sd.\n"
        "  2. theme nodes (id: themes.<arc>) — long-lived narrative arcs with assumptions list.\n"
        "  3. politics nodes (id: politics.<event>) — discrete distributions over plausible regime moves.\n\n"
        "Each node MUST include a `provenance` block referencing source URL and timestamp. "
        "Confidence values must be honest; flag fuzz_halo where the LLM summarisation is brittle.\n\n"
        "Output exactly:\n"
        "===SENTIMENT===\n<yaml>\n===THEMES===\n<yaml>\n===POLITICS===\n<yaml>\n\n"
        f"Items:\n{items_text}\n"
    )
    options = ClaudeAgentOptions(
        cwd=str(WORKSPACE),
        allowed_tools=[],
        permission_mode="default",
        model="claude-opus-4-6",
        thinking={"type": "adaptive"},
        max_turns=1,
    )
    final = ""
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            final = message.result or ""
    return final


def _split_sections(blob: str) -> tuple[str, str, str]:
    def _between(s: str, start: str, end: str | None) -> str:
        i = s.find(start)
        if i < 0:
            return ""
        i += len(start)
        if end is None:
            return s[i:].strip()
        j = s.find(end, i)
        return s[i:j].strip() if j >= 0 else s[i:].strip()

    sent = _between(blob, "===SENTIMENT===", "===THEMES===")
    them = _between(blob, "===THEMES===", "===POLITICS===")
    pol = _between(blob, "===POLITICS===", None)
    return sent, them, pol


async def run() -> None:
    items = _collect_items()
    if not items:
        print(f"[{id}] no items collected; skipping")
        return
    blob = await _summarise(items)
    if not blob:
        print(f"[{id}] empty summary; skipping write")
        return
    sent, them, pol = _split_sections(blob)
    if sent:
        write_block(SENTIMENT_FILE, id, f"```yaml\n{sent}\n```")
    if them:
        write_block(THEMES_FILE, id, f"```yaml\n{them}\n```")
    if pol:
        write_block(POLITICS_FILE, id, f"```yaml\n{pol}\n```")
    print(f"[{id}] wrote sentiment/themes/politics blocks from {len(items)} items")
