# TokenGuard

**Autonomous LLM FinOps & Cost Intelligence Gateway**

TokenGuard is a high-performance local-first proxy and telemetry engine designed to monitor, audit, and optimize LLM token spending across teams and applications.

## Current Project Status (35% Complete)
- [x] Multi-model pricing matrix (`gpt-4o`, `gpt-4o-mini`, `claude-3-5-sonnet`) (`src/tokenguard/engine.py`)
- [x] Pydantic telemetry models and embedded DuckDB call logging (`src/tokenguard/models.py`)
- [x] CLI for capturing and inspecting API telemetry (`src/tokenguard/cli.py`)
- [x] Comprehensive pytest test suite (`tests/test_guard.py`)

## Planned Roadmap 
- [ ] **Async FastAPI Proxy Server:** Intercept OpenAI/Anthropic SDK requests transparently with sub-millisecond overhead.
- [ ] **Budget Enforcer & Rate Limiter:** Real-time token budget threshold alerts and hard cutoffs per user/organization .
- [ ] **Semantic Caching Layer:** Vector similarity check to prevent duplicate prompt queries and save 40% token costs.
- [ ] **Web Dashboard UI:** Next.js + Tailwind analytics dashboard for visualizing token burn rates and latency distributions.
