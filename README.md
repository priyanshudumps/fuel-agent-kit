# Fuel Agent Kit

An AI-powered agent toolkit for interacting with the [Fuel Network](https://fuel.network/) blockchain. Build intelligent agents that can execute transactions, swap tokens, manage DeFi positions, and more — all through natural language.

## Features

- 🤖 **Natural Language Transactions** — Describe what you want to do in plain English
- 💱 **Token Swaps** — Swap assets on [Mira DEX](https://mira.ly/) with configurable slippage
- 💸 **Transfers** — Send any verified Fuel asset to another wallet
- 🏦 **DeFi (Swaylend)** — Supply collateral and borrow assets
- 💧 **Liquidity Provisioning** — Add liquidity to Mira pools
- 📊 **Balance Queries** — Check your own or any wallet's asset balances
- 🔌 **Multi-Model Support** — Works with OpenAI, Anthropic, and Google Gemini

## Installation

```bash
npm install fuel-agent-kit fuels
```

> **Note:** `fuels` is a required peer dependency (v0.96.1+).

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_PRIVATE_KEY!,
  model: 'gpt-4o',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

// Use natural language to interact with Fuel
const response = await agent.execute('Transfer 0.1 ETH to 0xABC...123');
console.log(response);
```

## Configuration

Create a `FuelAgent` instance with the following config:

```typescript
interface FuelAgentConfig {
  walletPrivateKey: string;          // Your Fuel wallet private key
  model: string;                     // LLM model name (see supported models below)
  openAiApiKey?: string;             // Required for OpenAI models
  anthropicApiKey?: string;          // Required for Anthropic models
  googleGeminiApiKey?: string;       // Required for Gemini models
}
```

### Supported Models

| Provider   | Models                                |
|-----------|---------------------------------------|
| OpenAI    | `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo` |
| Anthropic | `claude-3-5-sonnet-20241022`          |
| Gemini    | `gemini-1.5-flash`, `gemini-1.5-pro`  |

## Programmatic Usage

You can also call individual functions directly without the AI agent:

```typescript
const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_PRIVATE_KEY!,
  model: 'gpt-4o',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

// Swap tokens on Mira DEX
await agent.swapExactInput({
  amount: '1.0',
  fromSymbol: 'ETH',
  toSymbol: 'USDC',
  slippage: 0.01, // 1%
});

// Transfer assets
await agent.transfer({
  to: '0xRecipientAddress...',
  amount: '10',
  symbol: 'USDC',
});

// Check balance
const balance = await agent.getOwnBalance({ symbol: 'ETH' });

// Supply collateral to Swaylend
await agent.supplyCollateral({
  amount: '1.0',
  symbol: 'ETH',
});

// Borrow from Swaylend
await agent.borrowAsset({ amount: '100' });

// Add liquidity to Mira pool
await agent.addLiquidity({
  amount0: '1.0',
  asset0Symbol: 'ETH',
  asset1Symbol: 'USDC',
  slippage: 0.01,
});
```

## Available Tools (AI Agent)

When using the AI agent via `agent.execute()`, the following tools are available:

| Tool                 | Description                                      |
|---------------------|--------------------------------------------------|
| `fuel_transfer`     | Transfer any verified Fuel asset to another wallet |
| `swap_exact_input`  | Swap tokens on Mira DEX                           |
| `supply_collateral` | Supply collateral on Swaylend                      |
| `borrow_asset`      | Borrow assets on Swaylend                          |
| `add_liquidity`     | Add liquidity to a Mira pool                       |
| `get_own_balance`   | Get your wallet's asset balance                    |
| `get_balance`       | Get any wallet's asset balance                     |

## Environment Variables

```bash
FUEL_PRIVATE_KEY=your_fuel_wallet_private_key
OPENAI_API_KEY=your_openai_api_key        # If using OpenAI models
ANTHROPIC_API_KEY=your_anthropic_api_key  # If using Anthropic models
GOOGLE_GEMINI_API_KEY=your_gemini_key     # If using Gemini models
```

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test

# Format code
npm run format

# Lint
npm run lint
```

## License

MIT
