# Fuel Agent Kit

[![npm version](https://img.shields.io/npm/v/fuel-agent-kit.svg?style=flat-square)](https://www.npmjs.com/package/fuel-agent-kit)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-Blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Fuel Network](https://img.shields.io/badge/Fuel-Network-orange?style=flat-square)](https://fuel.network/)

An AI agent toolkit for the [Fuel Network](https://fuel.network/) — enabling autonomous blockchain interactions through natural language.

## Features

- **AI-Powered Agent**: Interact with Fuel blockchain using LangChain agents
- **DeFi Operations**: Swap, lend, borrow, and provide liquidity on Fuel
- **Multi-Model Support**: Works with OpenAI, Anthropic, and Google Gemini
- **Type-Safe**: Full TypeScript support with strict typing

## Quick Start

### Installation

```bash
npm install fuel-agent-kit
```

### Basic Usage

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'YOUR_WALLET_PRIVATE_KEY',
  model: 'gpt-4',
  openAiApiKey: 'YOUR_OPENAI_API_KEY',
});

// Ask the agent to perform a blockchain operation
const result = await agent.execute('Swap 1 ETH for USDC on Fuel');
console.log(result);
```

### Supported Models

| Provider | Model Key | API Key Required |
|----------|-----------|-----------------|
| OpenAI | `gpt-4`, `gpt-3.5-turbo` | `openAiApiKey` |
| Anthropic | `claude-3-opus`, `claude-3-sonnet` | `anthropicApiKey` |
| Google | `gemini-pro` | `googleGeminiApiKey` |

## Available Operations

### MIRA (DEX)
- **Swap**: Exchange tokens via MIRA DEX
- **Add Liquidity**: Provide liquidity to MIRA pools

### SwayLend
- **Borrow**: Borrow assets against collateral
- **Supply**: Supply collateral to earn yield

### Transfers
- **Wallet Transfer**: Send tokens to other addresses
- **Balance Check**: Query your own account balance

## Configuration

```typescript
interface FuelAgentConfig {
  walletPrivateKey: string;    // Your Fuel wallet private key
  model: keyof typeof modelMapping;  // AI model to use
  openAiApiKey?: string;       // OpenAI API key
  anthropicApiKey?: string;    // Anthropic API key
  googleGeminiApiKey?: string; // Google Gemini API key
}
```

## Security

⚠️ **Never commit your private key or API keys.** Use environment variables:

```bash
# .env
FUEL_WALLET_PRIVATE_KEY=your_private_key_here
OPENAI_API_KEY=your_openai_key_here
```

## Development

```bash
# Clone and install
git clone https://github.com/dhaiwat10/fuel-agent-kit.git
cd fuel-agent-kit
npm install

# Build
npm run build

# Test
npm test
```

## License

MIT © [Dhai Patel](https://twitter.com/dhaiwat10)

## Links

- **Homepage**: https://github.com/dhaiwat10/fuel-agent-kit
- **Bug Reports**: https://github.com/dhaiwat10/fuel-agent-kit/issues
- **npm**: https://www.npmjs.com/package/fuel-agent-kit
