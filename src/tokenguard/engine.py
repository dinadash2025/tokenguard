import duckdb
from typing import Dict, Any, List
from .models import LLMCallRecord

# Standard pricing per 1M tokens (Input / Output)
MODEL_PRICING = {
    "gpt-4o": {"input": 5.00, "output": 15.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
}

class TokenGuardEngine:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = duckdb.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS llm_calls (
                call_id VARCHAR PRIMARY KEY,
                model VARCHAR,
                prompt_tokens INTEGER,
                completion_tokens INTEGER,
                latency_ms DOUBLE,
                user_id VARCHAR,
                cost_usd DOUBLE
            )
        """)

    def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        pricing = MODEL_PRICING.get(model, {"input": 1.00, "output": 3.00})
        cost = (prompt_tokens / 1_000_000 * pricing["input"]) + (completion_tokens / 1_000_000 * pricing["output"])
        return round(cost, 6)

    def log_call(self, record: LLMCallRecord) -> float:
        cost = self.calculate_cost(record.model, record.prompt_tokens, record.completion_tokens)
        self.conn.execute(
            "INSERT OR REPLACE INTO llm_calls VALUES (?, ?, ?, ?, ?, ?, ?)",
            [record.call_id, record.model, record.prompt_tokens, record.completion_tokens, record.latency_ms, record.user_id, cost]
        )
        return cost

    def get_usage_summary(self) -> Dict[str, Any]:
        row = self.conn.execute("SELECT COUNT(*), SUM(prompt_tokens + completion_tokens), SUM(cost_usd) FROM llm_calls").fetchone()
        return {
            "total_calls": row[0] or 0,
            "total_tokens": row[1] or 0,
            "total_cost_usd": round(row[2] or 0.0, 4)
        }
