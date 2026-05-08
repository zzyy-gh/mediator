---
id: agent.scope-sharpener
purpose: Convert a vague intent into a sharp, falsifiable scope statement.
default_owner: either
reads:
  - inquiries/<self>.md
  - objective.md
  - strategies.md
writes:
  - inquiries/<self>.md#scope
prerequisites:
  - sections.scope: pending
---

# Scope Sharpener

## Purpose

Take a fuzzy intent and produce a one-paragraph scope statement that names what is in-scope, what is deliberately deferred, and what would falsify the inquiry's premise.

## Inputs

- The inquiry file's intent / vague seed.
- `objective.md` (E[R]/E[risk] frame).
- `strategies.md` (archetype the inquiry is operating under, if any).

## Process

1. Identify the question being asked — capital decision, belief test, feed request, divergent search.
2. Bound it: name three things it is, three things it is not, the time horizon, and the vehicle universe (or note "open").
3. State the falsifier — what observation would make this inquiry not worth pursuing.

## Output

The `## Scope` section of the inquiry file. One paragraph plus a short list.

## Failure modes

- Scope still vague — missing in/out/falsifier. Re-run with explicit prompts.
- Scope too narrow — eliminated optionality the user wanted. Reflect and widen.
