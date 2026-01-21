# Repository Guidelines

## Project Structure & Module Organization
- `main.py`: quick entrypoint for sanity checks.
- `hello/01models.ipynb`: minimal LangChain chat example; requires `OPENAI_MODEL`.
- `hello/02model_with_tools.ipynb`: tool-calling demo instrumented with Traceloop (adjust `Traceloop.init` as needed).
- `hello/03create_agent.ipynb`: agent-style workflow example.
- `pyproject.toml` and `uv.lock`: source of truth for dependencies; add new tests under `tests/` when coverage is introduced.

## Setup & Environment
- Target Python 3.12; install dependencies with `uv sync`.
- Use a local `.env` for secrets and model settings. Required: `OPENAI_MODEL` (e.g., `ollama:qwen2.5:3b`). For telemetry, set `TRACELOOP_API_KEY` and tune `Traceloop.init` in notebooks.
- VS Code notebooks: select the `uv` kernel (with `ipykernel`).
- Do not commit `.env`; if you add new variables, provide a safe `.env.example`.

## Build, Test, and Development Commands
- `uv run python main.py` – repository smoke check.
- Open notebooks via VS Code/Jupyter and run cells directly (no CLI needed for the examples).
- `uv add <package>` then `uv sync` – add dependencies and refresh the lockfile (commit both).

## Coding Style & Naming Conventions
- Python with 4-space indents; prefer type hints for public functions and external-facing data.
- Use `snake_case` for modules, functions, and variables; `PascalCase` for classes.
- If introducing lint/format tools (e.g., ruff/black), wire them in `pyproject.toml` and document their run commands alongside the above.
- Keep examples runnable and fail fast when env vars are missing.

## Testing Guidelines
- No automated tests yet; place new coverage in `tests/` using `pytest` (add as a dev dependency).
- Favor fast, offline tests; mock external calls to LangChain/OpenAI and Traceloop. Run with `uv run pytest` once added.

## Commit & Pull Request Guidelines
- Match existing history: short, lower-case, imperative subject lines (e.g., “use ollama”, “model.bind_tools”).
- PRs should state purpose, key changes, commands executed, and required env vars; include screenshots only when output or UX meaningfully changes.
