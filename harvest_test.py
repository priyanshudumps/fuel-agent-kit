import asyncio
import os
from dotenv import load_dotenv
from fuel_agent.fuel_agent import FuelAgent, FuelAgentConfig

# Load your sniper configuration
load_dotenv()

async def start_harvest():
    print("=== 2026 Bounty Sniper: Fuel Agent Kit Python ===\n")
    
    # Initialize the real sniper agent
    config = FuelAgentConfig(
        wallet_private_key=os.getenv("FUEL_WALLET_PRIVATE_KEY", "your_secret_key_here"),
        model="deepseek-chat",
        openai_api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    
    agent = FuelAgent(config)
    
    # Test natural language reasoning
    test_command = "Send 0.001 ETH to fuel1234567890abcdef1234567890abcdef12345678"
    print(f"User Input: {test_command}")
    print("Agent is thinking (DeepSeek Mode)...")
    
    try:
        response = await agent.execute(test_command)
        print("\n=== Agent Response ===")
        print(response.get("output", "No response from AI"))
    except Exception as e:
        print(f"\nExecution error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(start_harvest())
