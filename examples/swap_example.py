"""Token swap example."""

import asyncio
from decimal import Decimal
from fuel_agent import FuelAgent, FuelAgentConfig


async def swap_example():
    """Example of token swapping."""
    config = FuelAgentConfig(
        wallet_private_key="your-private-key",
        model="gpt-4",
    )
    
    agent = FuelAgent(config)
    
    # Swap exact input
    result = await agent.swap_exact_input(
        from_token="USDC",
        to_token="ETH",
        amount=Decimal("1000"),
        min_output=Decimal("0.5")  # Slippage protection
    )
    
    if result["success"]:
        print(f"Swap successful!")
        print(f"Transaction hash: {result['tx_hash']}")
    else:
        print(f"Swap failed: {result.get('error')}")


if __name__ == "__main__":
    asyncio.run(swap_example())
