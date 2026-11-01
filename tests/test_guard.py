from tokenguard.engine import TokenGuardEngine
from tokenguard.models import LLMCallRecord

def test_cost_calculation_and_summary():
    engine = TokenGuardEngine()
    cost = engine.calculate_cost("gpt-4o", 1_000_000, 1_000_000)
    assert cost == 20.00  # $5 input + $15 output

    record = LLMCallRecord(call_id="c1", model="gpt-4o-mini", prompt_tokens=1000, completion_tokens=500, latency_ms=120.0)
    engine.log_call(record)
    summary = engine.get_usage_summary()
    assert summary["total_calls"] == 1
    assert summary["total_tokens"] == 1500
    assert summary["total_cost_usd"] > 0.0
