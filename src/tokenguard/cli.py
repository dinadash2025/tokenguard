import click
from .engine import TokenGuardEngine
from .models import LLMCallRecord

@click.group()
def main():
    """TokenGuard CLI: LLM FinOps & Cost Intelligence."""
    pass

@main.command()
@click.option("--model", default="gpt-4o", help="LLM model name")
@click.option("--prompt-tokens", type=int, default=500, help="Prompt tokens")
@click.option("--completion-tokens", type=int, default=150, help="Completion tokens")
def track(model: str, prompt_tokens: int, completion_tokens: int):
    """Simulate tracking an LLM API call."""
    engine = TokenGuardEngine()
    record = LLMCallRecord(call_id="call_test_123", model=model, prompt_tokens=prompt_tokens, completion_tokens=completion_tokens, latency_ms=320.5)
    cost = engine.log_call(record)
    click.echo(f"Logged call to {model}: ${cost:.5f} USD")

if __name__ == "__main__":
    main()
