# fuel-agent-kit

An AI agent toolkit for the [Fuel](https://fuel.network/) blockchain. Build intelligent agents that can interact with Fuel DeFi protocols using natural language.

## Features

- **Token Transfers** — Send tokens between Fuel wallets
- **DEX Trading** — Swap tokens via Mira DEX (exact input swaps, add liquidity)
- **Lending** — Supply collateral and borrow assets on SwayLend
- **Balance Queries** — Check wallet balances
- **Price Feeds** — Pyth oracle price data integration
- **Multi-LLM Support** — OpenAI, Anthropic Claude, Google Gemini

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_PRIVATE_KEY!,
  model: 'gpt-4o',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

// Chat with the agent
const response = await agent.execute("What is my ETH balance?");
console.log(response);

// Or use specific functions directly
await agent.transfer({
  to: '0x...',
  amount: '0.1',
  assetId: '0x...',
});

await agent.swapExactInput({
  amount: '1.0',
  assetIdIn: '0x...',
  assetIdOut: '0x...',
});
```

## Configuration

| Parameter | Required | Description |
|-----------|----------|-------------|
| `walletPrivateKey` | ✅ | Fuel wallet private key |
| `model` | ✅ | LLM model (`gpt-4o`, `claude-sonnet-4-20250514`, `gemini-pro`) |
| `openAiApiKey` | For OpenAI models | OpenAI API key |
| `anthropicApiKey` | For Claude models | Anthropic API key |
| `googleGeminiApiKey` | For Gemini models | Google AI API key |

## Available Tools

| Tool | Description |
|------|-------------|
| `transfer` | Transfer tokens to another wallet |
| `swapExactInput` | Swap tokens on Mira DEX |
| `addLiquidity` | Add liquidity to Mira DEX pools |
| `supplyCollateral` | Supply collateral on SwayLend |
| `borrowAsset` | Borrow assets from SwayLend |
| `getOwnBalance` | Check wallet token balance |

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test

# Lint
npm run lint

# Format
npm run format
```

## License

See [LICENSE](./LICENSE) for details.
