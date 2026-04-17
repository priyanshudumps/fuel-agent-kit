"""Lending operations example."""

import asyncio
from decimal import Decimal
from fuel_agent import FuelAgent, FuelAgentConfig


async def lending_example():
    """Example of lending operations."""
    config = FuelAgentConfig(
        wallet_private_key="your-private-key",
        model="gpt-4",
    )
    
    agent = FuelAgent(config)
    
    # Supply collateral
    supply_result = await agent.supply_collateral(
        asset="ETH",
        amount=Decimal("10")
    )
    print(f"Supply result: {supply_result['message']}")
    
    # Borrow assets
    borrow_result = await agent.borrow_asset(
        asset="USDC",
        amount=Decimal("5000")
    )
    print(f"Borrow result: {borrow_result['message']}")


if __name__ == "__main__":
    asyncio.run(lending_example())
