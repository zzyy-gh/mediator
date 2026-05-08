# Orchestrator

Single Python entrypoint that watches `inquiries/` and `graph/`, dispatches agents (Claude Agent SDK), and runs feeds on cadence.

## Install

```bash
pip install -r requirements.txt
cp .env.example .env
# edit .env, set ANTHROPIC_API_KEY (and FRED_API_KEY if using FRED)
```

## Layout

- `runner.py` — main loop. Polls inquiries; dispatches agents; runs feed cadence.
- `state.py` — front-matter parsing, section-status reads/writes, snapshot helper.
- `agent_runner.py` — generic agent dispatch; loads spec markdown, builds system prompt, calls SDK.
- `feeds/<name>.py` — one module per feed.

## Run

From `examples/investing/`:

```bash
python -m orchestrator.runner             # tick once and exit
python -m orchestrator.runner --watch     # poll loop (default 30s interval)
python -m orchestrator.runner --feeds     # run feeds once and exit
```

Module form is required because the package uses relative imports.

## Discipline

- Sections write only to themselves (enforced by prompt + scoped tools).
- Per-inquiry serial; cross-inquiry parallel.
- Section status fields are the lock; no orchestrator-side locking.
- `taste/` is read-locally only; never written by agents.
