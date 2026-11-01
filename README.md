# TokenGuard

**Autonomous LLM FinOps & Cost Intelligence Gateway**

TokenGuard is a high-performance local-first proxy and telemetry engine designed to monitor, audit, and optimize LLM token spending across teams and applications.

## Current Project Status (20% Complete — 20 Hours Completed)
- [x] Multi-model pricing matrix (`gpt-4o`, `gpt-4o-mini`, `claude-3-5-sonnet`) (`src/tokenguard/engine.py`)
- [x] Pydantic telemetry models and embedded DuckDB call logging (`src/tokenguard/models.py`)
- [x] CLI for capturing and inspecting API telemetry (`src/tokenguard/cli.py`)
- [x] Comprehensive pytest test suite (`tests/test_guard.py`)

## Planned Roadmap (80% Remaining — 80 Hours Scoped)
- [ ] **Async FastAPI Proxy Server:** Intercept OpenAI/Anthropic SDK requests transparently with sub-millisecond overhead (25 hrs).
- [ ] **Budget Enforcer & Rate Limiter:** Real-time token budget threshold alerts and hard cutoffs per user/organization (20 hrs).
- [ ] **Semantic Caching Layer:** Vector similarity check to prevent duplicate prompt queries and save 40% token costs (20 hrs).
- [ ] **Web Dashboard UI:** Next.js + Tailwind analytics dashboard for visualizing token burn rates and latency distributions (15 hrs).
