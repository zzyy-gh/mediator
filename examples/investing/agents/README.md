# Agents

One markdown spec per agent. Each agent is a single-purpose, stateless function over graph + inquiries. The orchestrator loads the spec, builds a system prompt, and invokes the agent with file tools scoped to the spec's reads/writes whitelist.

## Spec shape

```yaml
---
id: agent.<name>
purpose: <one-line>
default_owner: agent | human | either
reads: [<file_or_glob>, ...]      # whitelist
writes: [<file_or_section>, ...]  # whitelist; usually a single section in an inquiry
prerequisites: [<condition>, ...]  # what must be ready before this agent runs
spawns: [<inquiry_kind>, ...]      # if it can open child inquiries (e.g. feed-prospector)
---

# <Agent Name>

## Purpose

## Inputs

## Process

## Output

## Failure modes
```

## Pluggability

Any inquiry section's `owner` field can be set to `human:<id>` to take an agent out of the loop for that section. The orchestrator simply notifies and waits.

## Adding an agent

Drop a new `<name>.md` here, write a matching wrapper at `orchestrator/agents/<name>.py`, and reference it by id from any inquiry section's `owner` field. No other registration required.
