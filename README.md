# Fuel Agent Kit

An AI agent toolkit for the [Fuel](https://fuel.network) blockchain. Interact with Fuel DeFi protocols using natural language powered by LangChain and multiple LLM providers.

## Features

- **Token Transfers** - Send any verified Fuel asset to any wallet
- **DEX Swaps** - Swap tokens on [Mira DEX](https://mira.ly)
- **Liquidity Provision** - Add liquidity to Mira pools
- **Lending & Borrowing** - Supply collateral and borrow assets on [Swaylend](https://swaylend.com)
- **Balance Queries** - Check wallet balances for any asset
- **Multi-LLM Support** - Works with OpenAI (GPT-4o), Anthropic (Claude), and Google Gemini

## Installation

```bash
npm install fuel-agent-kit
```

## Prerequisites

- Node.js 18+
- A Fuel wallet private key with funds on Fuel mainnet
- An API key for at least one supported LLM provider

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'YOUR_FUEL_WALLET_PRIVATE_KEY',
  model: 'gpt-4o', // or 'claude-3-5-sonnet-latest', 'gemini-1.5-flash'
  openAiApiKey: 'YOUR_OPENAI_API_KEY',
});

// Use the AI agent with natural language
const response = await agent.execute('Swap 1 USDC for ETH on Mira');
console.log(response);
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

You can also call methods directly without the AI agent:

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'YOUR_FUEL_WALLET_PRIVATE_KEY',
  model: 'gpt-4o',
  openAiApiKey: 'YOUR_OPENAI_API_KEY',
});

// Transfer tokens
await agent.transfer({
  to: '0x...',
  amount: '10',
  symbol: 'USDC',
});

// Swap tokens on Mira
await agent.swapExactInput({
  amount: '1',
  fromSymbol: 'USDC',
  toSymbol: 'ETH',
  slippage: 0.01, // optional, defaults to 1%
});

// Add liquidity
await agent.addLiquidity({
  amount0: '10',
  asset0Symbol: 'USDC',
  asset1Symbol: 'ETH',
});

// Supply collateral on Swaylend
await agent.supplyCollateral({
  amount: '100',
  symbol: 'ETH',
});

// Borrow from Swaylend
await agent.borrowAsset({
  amount: '50',
});

// Check your balance
await agent.getOwnBalance({ symbol: 'USDC' });
```

## Tools (LangChain)

The kit exposes the following tools for LangChain agents:

| Tool | Description |
|---|---|
| `fuel_transfer` | Transfer any verified Fuel asset to another wallet |
| `swap_exact_input` | Swap exact input on Mira DEX |
| `supply_collateral` | Supply collateral on Swaylend |
| `borrow_asset` | Borrow asset on Swaylend |
| `add_liquidity` | Add liquidity to a Mira pool |
| `get_own_balance` | Get the balance of an asset in your wallet |
| `get_balance` | Get the balance of an asset for a given wallet address |

## Configuration

### Environment Variables

Copy `.env.example` and fill in your keys:

```bash
cp .env.example .env
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

[MIT](LICENSE)
