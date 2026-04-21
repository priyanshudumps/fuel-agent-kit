"""Available tools for the AI agent."""

from typing import Dict, Any, Callable, List
from decimal import Decimal


class Tool:
    """Represents a tool that the agent can use."""
    
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func
    
    async def __call__(self, **kwargs) -> Dict[str, Any]:
        """Execute the tool."""
        return await self.func(**kwargs)


def get_tools(fuel_agent) -> List[Tool]:
    """
    Get all available tools for the agent.
    
    Args:
        fuel_agent: FuelAgent instance
        
    Returns:
        List of available tools
    """
    return [
        Tool(
            name="swap_tokens",
            description="Swap tokens on Mira DEX. Parameters: from_token (str), to_token (str), amount (str)",
            func=lambda from_token, to_token, amount: fuel_agent.swap_exact_input(
                from_token, to_token, Decimal(amount)
            ),
        ),
        Tool(
            name="transfer_tokens",
            description="Transfer tokens to an address. Parameters: to_address (str), token (str), amount (str)",
            func=lambda to_address, token, amount: fuel_agent.transfer(
                to_address, token, Decimal(amount)
            ),
        ),
        Tool(
            name="get_balance",
            description="Get wallet balance for a token. Parameters: token (str)",
            func=lambda token: fuel_agent.get_balance(token),
        ),
        Tool(
            name="supply_collateral",
            description="Supply collateral to SwayLend. Parameters: asset (str), amount (str)",
            func=lambda asset, amount: fuel_agent.supply_collateral(
                asset, Decimal(amount)
            ),
        ),
        Tool(
            name="borrow_asset",
            description="Borrow assets from SwayLend. Parameters: asset (str), amount (str)",
            func=lambda asset, amount: fuel_agent.borrow_asset(
                asset, Decimal(amount)
            ),
        ),
    ]
