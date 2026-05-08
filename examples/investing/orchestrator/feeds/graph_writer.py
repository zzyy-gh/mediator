"""Atomic block replacement inside graph/<topic>.md files."""
from __future__ import annotations

from pathlib import Path


def write_block(graph_file: Path, feed_id: str, body: str) -> None:
    """Replace the section bracketed by BEGIN/END markers for `feed_id`.

    Preserves any human-edited content outside the markers. Appends a
    new section if the markers are not yet present.
    """
    marker_begin = f"<!-- BEGIN {feed_id} -->"
    marker_end = f"<!-- END {feed_id} -->"
    block = f"{marker_begin}\n{body.strip()}\n{marker_end}"

    text = graph_file.read_text(encoding="utf-8") if graph_file.exists() else ""
    if marker_begin in text and marker_end in text:
        before, _, rest = text.partition(marker_begin)
        _, _, after = rest.partition(marker_end)
        new_text = f"{before}{block}{after}"
    else:
        sep = "" if text.endswith("\n") else "\n"
        new_text = f"{text}{sep}\n## Auto: {feed_id}\n\n{block}\n"

    graph_file.parent.mkdir(parents=True, exist_ok=True)
    graph_file.write_text(new_text, encoding="utf-8")
