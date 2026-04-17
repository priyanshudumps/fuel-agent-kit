# fuel-agent-kit-python

Python version of [fuel-agent-kit](https://github.com/priyanshudumps/fuel-agent-kit) — an AI agent toolkit for interacting with the Fuel blockchain.

## Installation

```bash
pip install fuel-agent-kit
```

## Requirements

- Python 3.10+
- A Fuel wallet private key
- An AI provider API key (OpenAI, Anthropic, or Google)

## Quick Start

```python
from fuel_agent_kit import FuelAgent

agent = FuelAgent(
    wallet_private_key="your-fuel-wallet-private-key",
    model="gpt-4o-mini",
    openai_api_key="your-openai-api-key",
)

# Natural language execution
result = agent.execute("Swap 0.1 USDC to ETH with 5% slippage")
print(result)

# Direct method calls
balance = agent.get_own_balance("ETH")
tx = agent.transfer(to="0x...", amount="1.5", symbol="USDC")
```

## API

### `FuelAgent(config)`

```python
agent = FuelAgent(
    wallet_private_key="0x...",
    model="gpt-4o-mini",  # or "claude-3-5-sonnet-latest", "gemini-1.5-flash"
    openai_api_key="sk-...",       # optional
    anthropic_api_key="sk-...",    # optional
    google_api_key="...",          # optional
)
```

### Methods

#### `execute(prompt: str) -> str`
Execute any operation via natural language.

#### `swap_exact_input(amount, from_symbol, to_symbol, slippage=0.01) -> dict`
```python
result = agent.swap_exact_input("0.1", "USDC", "ETH", slippage=0.05)
```

#### `transfer(to, amount, symbol) -> dict`
```python
result = agent.transfer("0x...", "10", "USDC")
```

#### `get_own_balance(symbol) -> dict`
```python
result = agent.get_own_balance("ETH")
```

#### `add_liquidity(amount0, asset0_symbol, asset1_symbol, slippage=0.01) -> dict`
```python
result = agent.add_liquidity("1", "ETH", "USDC")
```

#### `supply_collateral(amount, symbol) -> dict`
```python
result = agent.supply_collateral("100", "USDT")
```

#### `borrow_asset(amount) -> dict`
```python
result = agent.borrow_asset("50")
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format
black .
ruff check --fix .

# Type check
mypy fuel_agent_kit/
```

## License

MIT
