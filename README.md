# Fuel Agent Kit

An AI agent for Fuel blockchain that enables natural language interaction with Fuel ecosystem protocols.

## Features

- **Mira DEX Integration**
  - Swap tokens
  - Add liquidity to pools

- **Swaylend Integration**
  - Supply collateral
  - Borrow assets

- **Wallet Operations**
  - Transfer assets
  - Check balances

- **Multi-Model Support**
  - OpenAI (GPT)
  - Anthropic (Claude)
  - Google (Gemini)

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY,
  model: 'gpt-4',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

// The agent can now execute Fuel operations via natural language
```

## Configuration

Create a `.env` file based on `.env.example`:

```bash
FUEL_WALLET_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_GEMINI_API_KEY=your_google_key
```

## Available Tools

| Tool | Description |
|------|-------------|
| `swapExactInput` | Swap tokens on Mira DEX |
| `addLiquidity` | Add liquidity to Mira pools |
| `supplyCollateral` | Supply collateral to Swaylend |
| `borrowAsset` | Borrow assets from Swaylend |
| `transfer` | Transfer assets between wallets |
| `getOwnBalance` | Check wallet balance |

## Development

```bash
# Install dependencies
npm install

# Build the package
npm run build

# Run tests
npm test

# Type check
npm run lint
```

## License

MIT

## Contributing

Contributions are welcome! Please open an issue or submit a PR.
