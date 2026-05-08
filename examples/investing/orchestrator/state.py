"""Front-matter parsing, section-status reads/writes, snapshot helpers."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional

import frontmatter

WORKSPACE = Path(__file__).resolve().parents[1]
INQUIRIES_DIR = WORKSPACE / "inquiries"
GRAPH_DIR = WORKSPACE / "graph"


@dataclass
class Inquiry:
    path: Path
    post: frontmatter.Post

    @property
    def id(self) -> str:
        return self.post.get("id", self.path.stem)

    @property
    def status(self) -> str:
        return self.post.get("status", "open")

    @property
    def shape(self) -> str:
        return self.post.get("shape", "convergent")

    @property
    def collapse_flavour(self) -> str:
        return self.post.get("collapse_flavour", "belief")

    @property
    def owner(self) -> str:
        return self.post.get("owner", "either")

    @property
    def sections(self) -> dict:
        return self.post.get("sections", {}) or {}

    def section_status(self, name: str) -> str:
        return self.sections.get(name, "locked")

    def first_pending_section(self) -> Optional[str]:
        for name, status in self.sections.items():
            if status == "pending":
                return name
        return None

    def set_section_status(self, name: str, status: str) -> None:
        sections = dict(self.sections)
        sections[name] = status
        self.post["sections"] = sections
        self._write()

    def set_status(self, status: str) -> None:
        self.post["status"] = status
        self._write()

    def _write(self) -> None:
        with self.path.open("wb") as f:
            frontmatter.dump(self.post, f)


def load_inquiry(path: Path) -> Inquiry:
    return Inquiry(path=path, post=frontmatter.load(path))


def iter_open_inquiries() -> Iterator[Inquiry]:
    for p in sorted(INQUIRIES_DIR.glob("*.md")):
        try:
            inq = load_inquiry(p)
        except Exception as e:
            print(f"[skip] {p.name}: {e}")
            continue
        if inq.status not in ("closed", "aborted"):
            yield inq


def graph_snapshot_ref() -> str:
    """Return a reproducible reference to current graph state.

    Uses the current git HEAD if the workspace is a git repo; otherwise
    returns an mtime-based ref. Either way, the inquiry stores this ref
    so downstream agents can confirm what state they reasoned over.
    """
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(WORKSPACE),
            stderr=subprocess.DEVNULL,
        )
        return f"git:{out.decode().strip()}"
    except Exception:
        max_mtime = 0.0
        for p in GRAPH_DIR.rglob("*.md"):
            max_mtime = max(max_mtime, p.stat().st_mtime)
        return f"mtime:{max_mtime}"


# Default agent per section. Used when an inquiry's owner is "either"
# (or "agent:auto") and no per-section override is provided.
SECTION_TO_AGENT_DEFAULT = {
    "scope": "scope-sharpener",
    "assumptions": "assumption-lister",
    "graph_refs": "probe-world",
    "m_nodes": "probe-prior-art",
    "prediction": "predictor",
    "output": "predictor",  # convergent default; divergent inquiries override via owner
    "sensitivity": "sensitivity-analyzer",
    "outcome": "outcome-recorder",
    "reflection": "reflector",
}


def resolve_agent(inquiry: Inquiry, section: str) -> Optional[str]:
    """Resolve which agent should fill `section` for `inquiry`.

    Precedence:
      1. inquiry-level owner of form "agent:<name>"
      2. SECTION_TO_AGENT_DEFAULT
      3. None (no agent — likely a human gate)
    """
    owner = inquiry.owner
    if isinstance(owner, str) and owner.startswith("agent:"):
        return owner.split(":", 1)[1]
    if owner == "either" or owner.startswith("agent:auto"):
        return SECTION_TO_AGENT_DEFAULT.get(section)
    return None
