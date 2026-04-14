# Fuel Agent Kit 🤖⛽

An AI agent toolkit designed to seamlessly integrate with the **Fuel Network**. Connect your AI agents (via LangChain) to Fuel's powerful infrastructure, execute trades on Mira DEX, fetch real-time prices via Pyth oracles, and interact with smart contracts on the fly!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Ready-blue.svg)](https://www.typescriptlang.org/)
[![Fuel Network](https://img.shields.io/badge/Network-Fuel-00E182.svg)](https://fuel.network/)

## 🌟 Features

* **LLM Integration**: Built-in support for multiple LLM providers through LangChain (`@langchain/openai`, `@langchain/anthropic`, `@langchain/google-genai`).
* **DeFi Ready**: Out-of-the-box integration with [Mira DEX](https://mira.ly/) (`mira-dex-ts`) for executing token swaps on Fuel.
* **Price Oracles**: Real-time price feeds via [Pyth Network](https://pyth.network/) (`@pythnetwork/pyth-fuel-js`).
* **Fuel Native**: Uses the official `fuels` SDK under the hood for seamless blockchain interaction.

## 📦 Installation

```bash
npm install fuel-agent-kit
```

*Note: You also need to install the peer dependency `fuels` if you haven't already.*
```bash
npm install fuels
```

## 🛠️ Usage

To use the kit, import it into your project. Make sure you have your Fuel wallet private key and RPC URLs configured in your environment (`.env`).

```typescript
import { createAgent } from 'fuel-agent-kit';
// Add your specific integration code here
```

## 🏗️ Development & Scripts

This project uses `tsup` for bundling and `vitest` for testing.

* **Build**: `npm run build`
* **Test**: `npm run test`
* **Format code**: `npm run format`
* **Lint**: `npm run lint`

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. Ensure your code passes all checks by running `npm run ci` before pushing.

## 📄 License

[MIT License](LICENSE)
