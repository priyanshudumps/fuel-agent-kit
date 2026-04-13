# Fuel Agent Kit (Python)

Python port of [fuel-agent-kit](https://github.com/dhaiwat10/fuel-agent-kit) - an AI agent toolkit for the [Fuel](https://fuel.network) blockchain.

## Features

- **Token Transfers** - Send any verified Fuel asset to any wallet
- **DEX Swaps** - Swap tokens on [Mira DEX](https://mira.ly)
- **Liquidity Provision** - Add liquidity to Mira pools
- **Lending & Borrowing** - Supply collateral and borrow assets on [Swaylend](https://swaylend.com)
- **Balance Queries** - Check wallet balances for any asset
- **Multi-LLM Support** - Works with OpenAI, Anthropic, and Google Gemini

## Installation

```bash
pip install fuel-agent-kit
```

## Quick Start

```python
from fuel_agent_kit import FuelAgent

agent = FuelAgent(
    wallet_private_key="YOUR_FUEL_WALLET_PRIVATE_KEY",
    model="gpt-4o",
    openai_api_key="YOUR_OPENAI_API_KEY",
)

# Use the AI agent with natural language
response = agent.execute("Swap 1 USDC for ETH on Mira")
print(response)
```

## Supported Models

| Model | Provider |
|---|---|
| `gpt-4o` | OpenAI |
| `gpt-4o-mini` | OpenAI |
| `claude-3-5-sonnet-latest` | Anthropic |
| `claude-3-5-haiku-latest` | Anthropic |
| `gemini-1.5-flash` | Google |
| `gemini-2.0-flash-exp` | Google |

## Direct Method Usage

```python
from fuel_agent_kit import FuelAgent

agent = FuelAgent(
    wallet_private_key="YOUR_FUEL_WALLET_PRIVATE_KEY",
    model="gpt-4o",
    openai_api_key="YOUR_OPENAI_API_KEY",
)

# Transfer tokens
agent.transfer(to="0x...", amount="10", symbol="USDC")

# Swap tokens on Mira
agent.swap(amount="1", from_symbol="USDC", to_symbol="ETH", slippage=0.01)

# Add liquidity
agent.add_liquidity(amount0="10", asset0_symbol="USDC", asset1_symbol="ETH")

# Supply collateral on Swaylend
agent.supply_collateral(amount="100", symbol="ETH")

# Borrow from Swaylend
agent.borrow(amount="50")

# Check balance
agent.get_own_balance(symbol="USDC")
```

## License

MIT
