# ⛽ Fuel Agent Kit

<p align="center">
  <img src="https://img.shields.io/badge/Fuel-Network-000000?style=for-the-badge&logo=fuel" alt="Fuel Base Badge" />
  <img src="https://img.shields.io/npm/v/fuel-agent-kit?style=for-the-badge&logo=npm" alt="NPM Version" />
  <img src="https://img.shields.io/badge/LangChain-Integration-blue?style=for-the-badge&logo=langchain" alt="Langchain Integration" />
</p>

**Fuel Agent Kit** is an open-source AI agent toolkit designed specifically for the [Fuel](https://fuel.network) network. It enables AI agents (powered by LangChain, OpenAI, Anthropic, or Google GenAI) to autonomously interact with the Fuel blockchain, execute transfers, trade on decentralized exchanges (Mira DEX), and fetch real-time Pyth network data.

---

## ⚡ Features

* **AI-Ready Infrastructure:** First-class integration with `@langchain/core`. You can plug these tools directly into your `AgentExecutor`.
* **Asset Transfers:** Secure and autonomous `transfer` functionalities built on top of the official `fuels` SDK.
* **DeFi Integrations:** Pre-built modules to interact with **Mira Dex** (`mira-dex-ts`) and fetch accurate oracle feeds via **Pyth Network** (`@pythnetwork/pyth-fuel-js`).
* **Swaylend Operations:** Supports interactions with lending protocols.

---

## 📦 Installation

To use `fuel-agent-kit` in your project, install it alongside its peer dependency (`fuels`) and your LLM connector of choice.

```bash
npm install fuel-agent-kit fuels
```

If you are using LangChain and OpenAI:
```bash
npm install langchain @langchain/openai
```

---

## 🚀 Quickstart

Below is a minimal example demonstrating how to initialize the `FuelAgent` and utilize its built-in tools.

```typescript
import { FuelAgent } from "fuel-agent-kit";
import { ChatOpenAI } from "@langchain/openai";
import { AgentExecutor, createReactAgent } from "langchain/agents";
import { Provider, Wallet } from "fuels";

async function main() {
  // 1. Initialize the Fuel Wallet and Provider
  const provider = await Provider.create("https://mainnet.fuel.network/graphql");
  const wallet = Wallet.fromPrivateKey(process.env.FUEL_PRIVATE_KEY!, provider);

  // 2. Initialize the Fuel Agent Kit
  const agentKit = new FuelAgent({
    wallet: wallet
  });

  // 3. Extract the LangChain-compatible tools
  const tools = agentKit.getTools();
  
  // 4. Set up your LangChain standard agent
  const llm = new ChatOpenAI({ temperature: 0 });
  const agent = await createReactAgent({ llm, tools, prompt });
  const executor = new AgentExecutor({ agent, tools });

  // 5. Run it autonomously
  const result = await executor.invoke({
    messages: [
      { role: "user", content: "Transfer 0.1 ETH to fuel1... address." }
    ]
  });
  
  console.log(result.messages);
}

main();
```

---

## 🛠️ Architecture

The toolkit provides highly modular actions under `src/`:
- `FuelAgent.ts`: The central orchestrator uniting all available sub-modules.
- `/transfers`: Logic handling native asset and token transfers.
- `/mira`: Decentralized exchange interactions.
- `/swaylend`: Lending protocol interactions.
- `/read`: Data inspection (balances, chain-state, Pyth oracle).

---

## 💻 Contributing

We welcome community contributions! Please read our [CHANGELOG.md](CHANGELOG.md) for versioning history.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b dev/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Verify by running `npm run ci` to execute linters and typings checks.
5. Push to the Branch (`git push origin dev/AmazingFeature`)
6. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
