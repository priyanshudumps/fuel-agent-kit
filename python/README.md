# ⛽ Fuel Agent Kit (Python)

**Fuel Agent Kit** is an open-source AI agent toolkit designed specifically for the [Fuel](https://fuel.network) network. It enables AI agents (powered by LangChain, OpenAI, Anthropic, or Google GenAI) to autonomously interact with the Fuel blockchain, execute transfers, trade on decentralized exchanges (Mira DEX), and fetch real-time data.

## ⚡ Features

* **AI-Ready Infrastructure:** First-class integration with `langchain`.
* **Asset Transfers:** Secure and autonomous `transfer` functionalities.
* **DeFi Integrations:** Pre-built modules to interact with **Mira Dex** and **Swaylend**.

## 📦 Installation

To use `fuel-agent-kit` in your python project:

```bash
pip install fuel-agent-kit fuels
pip install langchain langchain-openai pydantic requests
```

## 🚀 Quickstart

Below is a minimal example demonstrating how to initialize the `FuelAgent` and utilize its built-in tools.

```python
import os
import asyncio
from fuel_agent_kit import FuelAgent, FuelAgentConfig

async def main():
    config = FuelAgentConfig(
        wallet_private_key=os.environ.get("FUEL_PRIVATE_KEY"),
        model="gpt-4-turbo-preview",
        open_ai_api_key=os.environ.get("OPENAI_API_KEY")
    )

    agent = FuelAgent(config)

    result = await agent.execute("Transfer 0.1 ETH to fuel1... address.")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

## 🛠️ Architecture

The toolkit provides highly modular actions under `src/`:
- `fuel_agent.py`: The central orchestrator uniting all available sub-modules.
- `transfers/`: Logic handling native asset and token transfers.
- `mira/`: Decentralized exchange interactions.
- `swaylend/`: Lending protocol interactions.
- `read/`: Data inspection (balances).

## 📄 License

Distributed under the MIT License.
