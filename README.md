## Overview
Simple LangChain + Traceloop demos for learning and experimentation.

## Getting Started
1) Install Python 3.12+.  
2) Install dependencies: `uv sync`  
3) Set env vars in `.env`:  
   - `OPENAI_MODEL` (e.g., `ollama:qwen2.5:3b`)  
   - Optional: `TRACELOOP_API_KEY` if you enable telemetry

## Run Examples
- `uv run python main.py` — sanity check.
- `uv run python hello/01hello.py` — basic chat.
- `uv run python hello/02tool.py` — tool call demo with Traceloop instrumentation.

## Notes
- Keep `.env` out of version control; add new keys to `.env.example` if you create one.
- Dependencies live in `pyproject.toml` and `uv.lock`; commit both when they change.
