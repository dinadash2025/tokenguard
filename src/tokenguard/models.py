from pydantic import BaseModel, Field

class LLMCallRecord(BaseModel):
    call_id: str
    model: str
    prompt_tokens: int = Field(..., ge=0)
    completion_tokens: int = Field(..., ge=0)
    latency_ms: float = Field(..., ge=0.0)
    user_id: str = "default_user"
