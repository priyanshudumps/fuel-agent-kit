# Fuel Agent Kit

> An AI agent for the [Fuel](https://fuel.network/) blockchain — powered by LangChain.

## What It Does

`fuel-agent-kit` provides a TypeScript toolkit that lets AI agents (powered by OpenAI, Anthropic, or Google Gemini) interact with the Fuel blockchain. It wraps common DeFi operations into LangChain tools that an LLM agent can reason about and execute autonomously.

## Features

| Capability | Description |
|------------|-------------|
| **Swap** | Token swaps on [Mira DEX](https://mira.fuel.network/) |
| **Add Liquidity** | Provide liquidity pairs on Mira DEX |
| **Transfer** | Send tokens to any Fuel address |
| **Balance Query** | Check wallet token balances |
| **Supply Collateral** | Deposit assets into [SwayLend](https://swaylend.fuel.network/) |
| **Borrow** | Borrow assets from SwayLend |
| **Price Feeds** | Real-time price data via [Pyth Network](https://pyth.network/) oracle |

## Supported AI Models

- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google Gemini

## Quick Start

```bash
# Install
npm install fuel-agent-kit

# Import
import { FuelAgent } from 'fuel-agent-kit';

// Initialize with your Fuel wallet private key and preferred AI model
const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_PRIVATE_KEY!,
  model: 'openai',       // 'openai' | 'anthropic' | 'google-gemini'
  openAiApiKey: process.env.OPENAI_API_KEY,
});
```

## Usage Example

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-fuel-wallet-private-key',
  model: 'anthropic',
  anthropicApiKey: process.env.ANTHROPIC_API_KEY,
});

// Ask the agent to perform a swap
const result = await.agent.execute('Swap 1 ETH for USDC on Mira DEX');
console.log(result);
```

## Available Tools

The agent has access to these LangChain tools:

| Tool | Function |
|------|----------|
| `swap` | Swap tokens on Mira DEX |
| `add_liquidity` | Add liquidity to a Mira pool |
| `transfer` | Transfer tokens to an address |
| `get_balance` | Query token balances |
| `supply` | Supply collateral to SwayLend |
| `borrow` | Borrow from SwayLend |

## Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `walletPrivateKey` | `string` | ✅ | Your Fuel wallet private key |
| `model` | `'openai' \| 'anthropic' \| 'google-gemini'` | ✅ | Which LLM to use |
| `openAiApiKey` | `string` | *conditional* | Required if `model='openai'` |
| `anthropicApiKey` | `string` | *conditional* | Required if `model='anthropic'` |
| `googleGeminiApiKey` | `string` | *conditional* | Required if `model='google-gemini'` |

## Development

```bash
# Install dependencies
npm install

# Run tests
npm test

# Build
npm build

# Lint
npm run lint

# Format
npm run format
```

## Dependencies

- [LangChain](https://js.langchain.com/) — Agent framework
- [@langchain/anthropic](https://js.langchain.com/docs/integrations/chat/anthropic) — Anthropic integration
- [@langchain/openai](https://js.langchain.com/docs/integrations/chat/openai) — OpenAI integration
- [@pythnetwork/pyth-fuel-js](https://github.com/pyth-network/pyth-fuel-js) — Pyth oracle for Fuel
- [mira-dex-ts](https://github.com/FuelLabs/mira-dex-ts) — Mira DEX SDK

## License

See [LICENSE](LICENSE) file.
