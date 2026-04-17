"""Basic usage example."""

import asyncio
from fuel_agent import FuelAgent, FuelAgentConfig


async def main():
    """Example of basic usage."""
    # Initialize agent
    config = FuelAgentConfig(
        wallet_private_key="your-private-key",
        model="gpt-4",
        openai_api_key="your-openai-api-key",
    )
    
    agent = FuelAgent(config)
    
    # Execute natural language command
    response = await agent.execute("Swap 100 USDC for ETH")
    print(f"Response: {response['output']}")
    
    # Direct method calls
    balance = await agent.get_balance("ETH")
    print(f"ETH Balance: {balance['balance']}")
    
    # Transfer tokens
    result = await agent.transfer(
        to_address="0x123...",
        token="USDC",
        amount=100
    )
    print(f"Transfer result: {result['message']}")


if __name__ == "__main__":
    asyncio.run(main())
