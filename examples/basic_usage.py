"""Basic usage example"""
import asyncio
from fuel_agent_kit import FuelAgent, FuelAgentConfig

async def main():
    config = FuelAgentConfig(
        wallet_private_key="your_key",
        model="openai",
        openai_api_key="your_openai_key"
    )
    agent = FuelAgent(config)
    
    # Use AI Agent
    response = await agent.execute("Swap 1 ETH for USDC")
    print(f"Response: {response}")
    
    # Direct call
    result = await agent.swap_exact_input({
        "amount": "1",
        "from_asset": "ETH",
        "to_asset": "USDC"
    })
    print(f"Swap result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
