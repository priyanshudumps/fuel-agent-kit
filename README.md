# Fuel Agent Kit ⛽️🤖

An AI agent library for the [Fuel Network](https://fuel.network), built on top of LangChain. This kit allows you to easily create autonomous agents that can interact with Fuel's ecosystem, including Mira DEX, SwayLend, and more.

## Features

- **Mira DEX Integration**: Swap assets and add liquidity.
- **SwayLend Support**: Supply collateral and borrow assets.
- **Wallet Operations**: Check balances and transfer tokens.
- **Multi-Model Support**: Use OpenAI, Anthropic, or Google Gemini.
- **LangChain Native**: Built as a LangChain Agent for easy extensibility.

## Installation

```bash
npm install fuel-agent-kit fuels
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-private-key',
  model: 'gpt-4o',
  openAiApiKey: 'your-openai-api-key'
});

const result = await agent.execute("What is my wallet balance?");
console.log(result);
```

## Configuration

The `FuelAgent` class accepts the following configuration:

| Property | Type | Description |
| --- | --- | --- |
| `walletPrivateKey` | `string` | Your Fuel wallet private key (Required) |
| `model` | `string` | AI model to use (e.g., `gpt-4o`, `claude-3-5-sonnet`) |
| `openAiApiKey` | `string` | (Optional) OpenAI API Key |
| `anthropicApiKey` | `string` | (Optional) Anthropic API Key |
| `googleGeminiApiKey` | `string` | (Optional) Google Gemini API Key |

## License

MIT
