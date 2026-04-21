"""AI agent setup and configuration."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .fuel_agent import FuelAgent


from typing import Optional, List, Any, Dict
from .deepseek_agent import FuelDeepSeekAgent

def create_agent(
    fuel_agent: Any,
    model: str,
    api_key: Optional[str] = None,
    **kwargs
) -> Any:
    """
    Create a real AI agent executor using DeepSeek.
    """
    if not api_key:
        import os
        api_key = os.getenv("DEEPSEEK_API_KEY")
    
    agent = FuelDeepSeekAgent(api_key=api_key, model=model)
    
    # We will bind tools here as we implement them (e.g., Transfer, Balance)
    return agent

