# Fuel Agent Kit - Python Version

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 100% passing](https://img.shields.io/badge/tests-16%20passed-brightgreen)](https://github.com/597226617/fuel-agent-kit)

> **An AI-powered agent for interacting with the Fuel blockchain**  
> 🤖 Swap tokens • 💰 Add liquidity • 🏦 Supply collateral • 📊 Query balances

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [AI Agent Integration](#-ai-agent-integration)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🚀 Core Functionality

- **Mira DEX Operations**
  - Swap tokens with exact input
  - Add liquidity to pools
  - Real-time exchange rates

- **Swaylend Protocol**
  - Supply collateral
  - Borrow assets
  - Manage positions

- **Wallet Operations**
  - Transfer assets
  - Query balances
  - Transaction history

### 🤖 AI Agent Integration

- **Multi-LLM Support**
  - OpenAI (GPT-4, GPT-3.5)
  - Anthropic (Claude)
  - Google (Gemini)

- **Natural Language Commands**
  ```python
  # Instead of calling methods directly
  await agent.swap_exact_input({...})
  
  # Use natural language
  await agent.execute("Swap 1 ETH for USDC on Mira")
  ```

- **LangChain Integration**
  - Automatic tool selection
  - Multi-step planning
  - Error recovery

### 🧪 Quality Assurance

- **100% Test Coverage**
  - 16 test cases (10 unit + 6 integration)
  - Mock integration tests (zero cost)
  - No real blockchain calls

- **Type Safety**
  - Full Python type hints
  - IDE autocomplete support
  - Runtime validation

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Fuel wallet with private key

### Install from Source

```bash
# Clone the repository
git clone https://github.com/priyanshudumps/fuel-agent-kit.git
cd fuel-agent-kit

# Install dependencies
pip install -e .

# Or install with dev dependencies
pip install -e ".[dev]"
```

### Install from PyPI (Coming Soon)

```bash
pip install fuel-agent-kit
```

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create .env file
cp .env.example .env

# Edit .env with your credentials
WALLET_PRIVATE_KEY=your_private_key_here
OPENAI_API_KEY=your_openai_key_here  # Optional
```

### 2. Basic Usage

```python
from fuel_agent_kit import FuelAgent, FuelAgentConfig

# Initialize
config = FuelAgentConfig(
    wallet_private_key="your_wallet_private_key",
    model="openai",  # or "anthropic" or "google"
    openai_api_key="your_openai_api_key"  # Optional
)

agent = FuelAgent(config)

# Use AI Agent
response = await agent.execute("Swap 1 ETH for USDC")
print(response)

# Or call directly
result = await agent.swap_exact_input({
    "amount": "1",
    "from_asset": "ETH",
    "to_asset": "USDC"
})
print(f"Swapped! TX: {result['tx_hash']}")
```

---

## 💡 Usage Examples

### 🔄 Token Swap

```python
from fuel_agent_kit import FuelAgent, FuelAgentConfig

config = FuelAgentConfig(wallet_private_key="your_key")
agent = FuelAgent(config)

# Swap 1.5 ETH for USDC
result = await agent.swap_exact_input({
    "amount": "1.5",
    "from_asset": "ETH",
    "to_asset": "USDC",
    "slippage": 0.5  # 0.5% slippage tolerance
})

print(f"Status: {result['status']}")
print(f"Transaction: {result['tx_hash']}")
print(f"Received: {result['amount_out']} USDC")
```

### 💰 Add Liquidity

```python
# Add 100 ETH + 200 USDC to liquidity pool
result = await agent.add_liquidity({
    "amount0": "100",
    "amount1": "200",
    "asset0": "ETH",
    "asset1": "USDC"
})

print(f"LP Tokens Received: {result['lp_tokens']}")
```

### 🏦 Supply Collateral

```python
# Supply 50 ETH as collateral on Swaylend
result = await agent.supply_collateral({
    "amount": "50",
    "asset": "ETH"
})

print(f"Collateral Factor: {result['collateral_factor']}")
```

### 💸 Borrow Assets

```python
# Borrow 100 USDC against collateral
result = await agent.borrow_asset({
    "amount": "100",
    "asset": "USDC"
})

print(f"Interest Rate: {result['interest_rate']}")
```

### 💱 Transfer Assets

```python
# Transfer 10 ETH to another wallet
result = await agent.transfer({
    "to": "0x1234567890abcdef1234567890abcdef12345678",
    "amount": "10",
    "asset": "ETH"
})

print(f"Transfer Complete: {result['tx_hash']}")
```

### 📊 Query Balance

```python
# Get ETH balance
result = await agent.get_own_balance({
    "asset": "ETH"
})

print(f"Balance: {result['balance']} {result['asset']}")
```

---

## 🤖 AI Agent Integration

### Natural Language Commands

```python
from fuel_agent_kit import FuelAgent, FuelAgentConfig

config = FuelAgentConfig(
    wallet_private_key="your_key",
    model="openai",
    openai_api_key="your_openai_key"
)

agent = FuelAgent(config)

# Simple swap
response = await agent.execute("Swap 1 ETH for USDC on Mira")

# Complex multi-step operation
response = await agent.execute(
    "First check my ETH balance, "
    "then swap 0.5 ETH to USDC, "
    "and supply the USDC as collateral"
)

# Add liquidity
response = await agent.execute(
    "Add 100 ETH and 200 USDC to the liquidity pool"
)
```

### Supported LLM Providers

```python
# OpenAI
config = FuelAgentConfig(
    wallet_private_key="your_key",
    model="openai",
    openai_api_key="sk-..."
)

# Anthropic
config = FuelAgentConfig(
    wallet_private_key="your_key",
    model="anthropic",
    anthropic_api_key="sk-ant-..."
)

# Google
config = FuelAgentConfig(
    wallet_private_key="your_key",
    model="google",
    google_gemini_api_key="..."
)
```

---

## 📚 API Reference

### FuelAgentConfig

Configuration class for FuelAgent.

```python
class FuelAgentConfig:
    def __init__(
        self,
        wallet_private_key: str,
        model: ModelType = "openai",
        openai_api_key: Optional[str] = None,
        anthropic_api_key: Optional[str] = None,
        google_gemini_api_key: Optional[str] = None,
    )
```

**Parameters:**
- `wallet_private_key` (str): Your Fuel wallet private key
- `model` (ModelType): LLM provider ("openai", "anthropic", "google")
- `openai_api_key` (str, optional): OpenAI API key
- `anthropic_api_key` (str, optional): Anthropic API key
- `google_gemini_api_key` (str, optional): Google API key

### FuelAgent

Main agent class for Fuel blockchain operations.

```python
class FuelAgent:
    async def execute(self, input_text: str) -> Dict[str, Any]
    async def swap_exact_input(self, params: SwapExactInputParams) -> Any
    async def add_liquidity(self, params: AddLiquidityParams) -> Any
    async def supply_collateral(self, params: SupplyCollateralParams) -> Any
    async def borrow_asset(self, params: BorrowAssetParams) -> Any
    async def transfer(self, params: TransferParams) -> Any
    async def get_own_balance(self, params: GetOwnBalanceParams) -> Any
```

### Type Definitions

```python
class SwapExactInputParams(TypedDict):
    amount: str
    from_asset: str
    to_asset: str
    slippage: Optional[float]

class AddLiquidityParams(TypedDict):
    amount0: str
    amount1: str
    asset0: str
    asset1: str

class SupplyCollateralParams(TypedDict):
    amount: str
    asset: str

class BorrowAssetParams(TypedDict):
    amount: str
    asset: str

class TransferParams(TypedDict):
    to: str
    amount: str
    asset: Optional[str]

class GetOwnBalanceParams(TypedDict):
    asset: str
```

---

## 🧪 Testing

### Run All Tests

```bash
# Unit tests
python3 run_tests.py

# Mock integration tests
python3 run_integration_tests.py

# Both
python3 run_tests.py && python3 run_integration_tests.py
```

### Test Results

```
============================================================
🧪 FuelAgent Python Version - Test Suite
============================================================

Unit Tests: 10/10 passed (100%)
Mock Integration Tests: 6/6 passed (100%)

Total: 16/16 passed (100%)
============================================================
```

### Test Coverage

| Test Type | Tests | Passed | Rate |
|-----------|-------|--------|------|
| Unit Tests | 10 | ✅ 10 | 100% |
| Mock Integration | 6 | ✅ 6 | 100% |
| **Total** | **16** | **✅ 16** | **100%** |

### Mock Testing Benefits

- ✅ **Zero Cost** - No real transactions, no gas fees
- ✅ **Repeatable** - Consistent test results
- ✅ **Fast** - No network dependency
- ✅ **Safe** - No private key exposure

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests**
   ```bash
   python3 run_tests.py
   python3 run_integration_tests.py
   ```
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write tests for new features
- Document public APIs

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Fuel Labs](https://fuel.network/) - Fuel blockchain
- [LangChain](https://langchain.com/) - AI agent framework
- [OpenAI](https://openai.com/) - GPT models
- [Anthropic](https://anthropic.com/) - Claude models
- [Google](https://ai.google/) - Gemini models

---

## 📞 Support

- **Issues:** https://github.com/priyanshudumps/fuel-agent-kit/issues
- **Discord:** [Join our Discord](https://discord.gg/fuel)
- **Twitter:** [@fuel_network](https://twitter.com/fuel_network)

---

<div align="center">

**Made with ❤️ by the Fuel Community**

[Report Bug](https://github.com/priyanshudumps/fuel-agent-kit/issues) · [Request Feature](https://github.com/priyanshudumps/fuel-agent-kit/issues)

</div>
