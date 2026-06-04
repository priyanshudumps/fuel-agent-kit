# fuel-agent-kit

An AI agent toolkit for interacting with the [Fuel](https://fuel.network/) blockchain. Execute transactions, manage DeFi positions, and interact with Fuel protocols using natural language.

## Features

- **Natural Language Transactions** — Execute blockchain operations by describing what you want to do
- **Token Transfers** — Send ETH and other tokens on Fuel
- **DEX Operations** — Swap tokens and add liquidity via [Mira DEX](https://mira.ly)
- **Lending** — Supply collateral and borrow assets on [Swaylend](https://swaylend.com)
- **Balance Queries** — Check token balances across assets
- **Multi-Model Support** — Works with OpenAI, Anthropic, and Google Gemini

## Installation

```bash
npm install fuel-agent-kit fuels
```

> `fuels` is a peer dependency and must be installed separately.

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: '0x...', // Your Fuel wallet private key
  model: 'gpt-4o',          // or 'claude-3-5-sonnet-20241022', 'gemini-1.5-flash'
  openAiApiKey: 'sk-...',   // API key for your chosen model
});

// Execute operations via natural language
const result = await agent.execute('Swap 0.1 ETH for USDC');
console.log(result);
```

## Programmatic API

You can also call methods directly without the AI agent:

```typescript
// Transfer tokens
await agent.transfer({
  to: '0x...',
  amount: '1000000', // in base units
  assetId: '0x...',
});

// Swap on Mira DEX
await agent.swapExactInput({
  assetIn: '0x...',
  assetOut: '0x...',
  amountIn: '1000000',
  minAmountOut: '900000',
});

// Supply collateral on Swaylend
await agent.supplyCollateral({
  assetId: '0x...',
  amount: '1000000',
});

// Borrow from Swaylend
await agent.borrowAsset({
  assetId: '0x...',
  amount: '500000',
});

// Check balance
const balance = await agent.getOwnBalance({ assetId: '0x...' });
```

## Supported Models

| Model | Provider |
|-------|----------|
| `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo` | OpenAI |
| `claude-3-5-sonnet-20241022`, `claude-3-opus-20240229` | Anthropic |
| `gemini-1.5-flash`, `gemini-1.5-pro` | Google |

## Environment Setup

Create a `.env` file based on `.env.example`:

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
```

## License

MIT
