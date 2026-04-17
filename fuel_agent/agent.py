"""AI agent setup and configuration."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .fuel_agent import FuelAgent


def create_agent(
    fuel_agent: "FuelAgent",
    model: str,
    openai_api_key: Optional[str] = None,
    anthropic_api_key: Optional[str] = None,
    google_gemini_api_key: Optional[str] = None,
):
    """
    Create an AI agent executor for natural language interactions.
    
    Args:
        fuel_agent: Reference to the FuelAgent instance
        model: Model identifier
        openai_api_key: OpenAI API key
        anthropic_api_key: Anthropic API key
        google_gemini_api_key: Google Gemini API key
        
    Returns:
        Agent executor instance
    """
    # For now, return a simple mock executor
    # In production, this would set up LangChain agent with proper tools
    return MockAgentExecutor(fuel_agent)


class MockAgentExecutor:
    """Mock agent executor for development."""
    
    def __init__(self, fuel_agent: "FuelAgent"):
        self.fuel_agent = fuel_agent
    
    async def ainvoke(self, inputs: dict) -> dict:
        """
        Mock invocation that parses basic commands.
        
        In production, this would use actual LLM for understanding.
        """
        input_text = inputs.get("input", "").lower()
        
        # Simple command parsing (replace with actual LLM in production)
        if "swap" in input_text:
            return {
                "input": input_text,
                "output": "I understand you want to swap tokens. Please use the swap_exact_input method with specific parameters.",
                "action": "swap",
            }
        elif "transfer" in input_text or "send" in input_text:
            return {
                "input": input_text,
                "output": "I understand you want to transfer tokens. Please use the transfer method with specific parameters.",
                "action": "transfer",
            }
        elif "balance" in input_text:
            return {
                "input": input_text,
                "output": "I can check your balance. Please use the get_balance method.",
                "action": "balance",
            }
        elif "borrow" in input_text:
            return {
                "input": input_text,
                "output": "I understand you want to borrow. Please use the borrow_asset method.",
                "action": "borrow",
            }
        elif "supply" in input_text or "deposit" in input_text:
            return {
                "input": input_text,
                "output": "I understand you want to supply collateral. Please use the supply_collateral method.",
                "action": "supply",
            }
        else:
            return {
                "input": input_text,
                "output": "I'm a Fuel blockchain agent. I can help you with: swapping tokens, transferring assets, checking balances, borrowing, and supplying collateral.",
                "action": "unknown",
            }
