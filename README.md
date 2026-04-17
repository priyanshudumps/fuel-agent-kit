# Fuel Agent Kit

An AI-powered agent toolkit for interacting with the Fuel blockchain. Built with LangChain, it enables natural language control over DeFi operations.

## Features

- 🤖 **AI-Powered** - Uses LangChain with support for OpenAI, Anthropic, and Google Gemini models
- 💱 **Token Swaps** - Swap tokens on Mira DEX
- 💰 **Liquidity Management** - Add liquidity to Mira pools
- 🏦 **Lending Operations** - Supply collateral and borrow assets on SwayLend
- 💸 **Transfers** - Transfer assets between wallets
- 📊 **Balance Queries** - Check wallet balances

## Installation

```bash
npm install fuel-agent-kit
```

## Prerequisites

- Node.js 18+
- A Fuel wallet with private key
- API key for your chosen AI model (OpenAI, Anthropic, or Google Gemini)

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'YOUR_FUEL_PRIVATE_KEY',
  model: 'gpt-4', // or 'claude-3-sonnet', 'gemini-pro'
  openAiApiKey: 'YOUR_OPENAI_API_KEY',
});

// Use natural language to perform operations
await agent.execute('Swap 100 USDC for ETH on Mira');
await agent.execute('Check my wallet balance');
await agent.execute('Transfer 50 USDC to 0x...');
```

## Supported Models

- `gpt-4` / `gpt-3.5-turbo` (OpenAI)
- `claude-3-opus` / `claude-3-sonnet` (Anthropic)
- `gemini-pro` (Google)

## Available Operations

| Operation | Description |
|-----------|-------------|
| `swapExactInput` | Swap tokens on Mira DEX |
| `addLiquidity` | Add liquidity to Mira pools |
| `supplyCollateral` | Supply collateral to SwayLend |
| `borrowAsset` | Borrow assets from SwayLend |
| `transfer` | Transfer tokens to another address |
| `getOwnBalance` | Check wallet balance |

## Configuration

Create a `.env` file based on `.env.example`:

```env
FUEL_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_GEMINI_API_KEY=your_gemini_key
```

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm run test

# Format code
npm run format
```

## License

MIT © Dhaiwat Pandya

## Links

- [Fuel Documentation](https://docs.fuel.network/)
- [Mira DEX](https://mira.ly/)
- [SwayLend](https://swaylend.com/)
- [Original Repository](https://github.com/dhaiwat10/fuel-agent-kit)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
