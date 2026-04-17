# Fuel Agent Kit (Python)

Python SDK for building AI agents on the Fuel blockchain.

## ✨ Features

- 🔑 **Wallet Management**: Secure handling of Fuel wallet credentials
- 🔄 **Token Swaps**: Integration with Mira DEX for token exchanges
- 💰 **Lending Operations**: Borrow and supply assets via SwayLend
- 📤 **Transfers**: Send tokens to any address
- 🤖 **AI Integration**: Support for OpenAI, Anthropic, and Google Gemini models

## 🚀 Quick Start

### Installation

```bash
pip install fuel-agent-kit
```

### Basic Usage

```python
from fuel_agent import FuelAgent

# Initialize agent
agent = FuelAgent(
    wallet_private_key="your-private-key",
    model="gpt-4",
    openai_api_key="your-openai-key"
)

# Execute natural language commands
response = await agent.execute("Swap 100 USDC for ETH")
print(response)
```

### Environment Setup

```bash
export FUEL_WALLET_PRIVATE_KEY="your-private-key"
export OPENAI_API_KEY="your-openai-key"
```

## 📁 Project Structure

```
fuel_agent/
├── __init__.py
├── fuel_agent.py      # Main agent class
├── agent.py           # AI agent setup
├── tools.py           # Available tools
├── mira/              # Mira DEX operations
├── swaylend/          # SwayLend operations
├── transfers/         # Transfer operations
├── read/              # Read operations
└── utils/             # Utilities
```

## 🧪 Development

```bash
git clone https://github.com/jonathan7591/fuel-agent-kit-python.git
cd fuel-agent-kit-python
pip install -e ".[dev]"
pytest
```

## 📖 License

MIT License

## 🙏 Acknowledgments

This is a Python port of the original TypeScript [fuel-agent-kit](https://github.com/priyanshudumps/fuel-agent-kit).
