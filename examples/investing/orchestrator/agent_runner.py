"""Generic agent dispatcher backed by the Claude Agent SDK.

Loads the agent's markdown spec, builds a system prompt that anchors on
objective + architecture + strategies + spec, then runs a single SDK
query scoped to the workspace. The agent edits the inquiry file in place.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import frontmatter
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)

from .state import WORKSPACE

AGENTS_DIR = WORKSPACE / "agents"

# Files baked into every agent's system prompt as the reflex layer.
ANCHOR_FILES = ("objective.md", "architecture.md", "strategies.md")

# Use Opus 4.6 with adaptive thinking for all agents (per claude-api skill).
DEFAULT_MODEL = "claude-opus-4-6"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _build_system_prompt(agent_id: str) -> str:
    spec_path = AGENTS_DIR / f"{agent_id}.md"
    spec = frontmatter.load(spec_path)
    anchors = "\n\n".join(
        f"# {name}\n{_read(WORKSPACE / name)}" for name in ANCHOR_FILES
    )
    return (
        f"You are agent.{agent_id} operating inside the mediator/investing workspace.\n\n"
        f"{anchors}\n\n"
        f"# Your spec\n{spec.content}\n\n"
        "Operating rules:\n"
        "- Workspace root: workspace files relative to your cwd.\n"
        "- Read what you need from `graph/`, `inquiries/`, `methods.md`, `blind-spots.md`, "
        "  `strategies.md`, closed inquiries, and `agents/<name>.md` if you need other agent specs.\n"
        "- Write only the section(s) listed in your spec's `writes` field.\n"
        "- Never write to `taste/` and never modify `objective.md`, `architecture.md`, "
        "  or `strategies.md` (those require human approval).\n"
        "- Preserve provenance, distributions, and explicit assumptions; avoid point estimates "
        "  dressed as facts.\n"
        "- When you finish, return a short summary of what you wrote and any flags for the human."
    )


async def run_agent(
    agent_id: str,
    inquiry_path: Path,
    section: Optional[str] = None,
    extra_user_context: str = "",
) -> str:
    """Dispatch the named agent against the inquiry file.

    Returns the agent's final result text (also persisted in the inquiry file).
    """
    system_prompt = _build_system_prompt(agent_id)
    section_hint = f" Section: {section}." if section else ""
    user_prompt = (
        f"Work on inquiry `{inquiry_path.relative_to(WORKSPACE).as_posix()}`."
        f"{section_hint}\n"
        "Fill the section(s) you are responsible for, per your spec. "
        "Mark each section's status as `ready` (or `locked` if the spec requires) "
        "in the inquiry's front-matter once written.\n\n"
        f"{extra_user_context}".strip()
    )

    options = ClaudeAgentOptions(
        cwd=str(WORKSPACE),
        allowed_tools=["Read", "Edit", "Write", "Glob", "Grep", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
        system_prompt=system_prompt,
        model=DEFAULT_MODEL,
        thinking={"type": "adaptive"},
        max_turns=30,
    )

    final = ""
    async for message in query(prompt=user_prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"[{agent_id}] {block.text[:160]}")
        elif isinstance(message, ResultMessage):
            final = message.result or ""
    return final
