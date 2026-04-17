# Fuel Agent Kit 🤖⛽

An AI agent toolkit for interacting with the [Fuel](https://fuel.network/) blockchain. Supports swaps, lending, transfers, and more through natural language commands.

## Features

- **Token Swaps** — Swap tokens on Mira DEX
- **Lending** — Supply collateral and borrow on SwayLend
- **Liquidity** — Add liquidity to Mira pools
- **Transfers** — Send tokens to any Fuel wallet
- **Balance Queries** — Check wallet balances
- **Natural Language** — Execute operations via plain English

## Supported AI Models

- OpenAI: `gpt-4o`, `gpt-4o-mini`
- Anthropic: `claude-3-5-sonnet-latest`, `claude-3-5-haiku-latest`
- Google: `gemini-1.5-flash`, `gemini-2.0-flash-exp`

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-fuel-wallet-private-key',
  model: 'gpt-4o-mini',
  openAiApiKey: 'your-openai-api-key',
});

// Natural language execution
const result = await agent.execute('Swap 0.1 USDC to ETH with 5% slippage');
console.log(result);

// Direct method calls
const balance = await agent.getOwnBalance({ symbol: 'ETH' });
const tx = await agent.transfer({
  to: '0x...',
  amount: '1.5',
  symbol: 'USDC',
});
```

## API Reference

### `new FuelAgent(config)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `walletPrivateKey` | `string` | Fuel wallet private key |
| `model` | `string` | AI model to use |
| `openAiApiKey` | `string?` | OpenAI API key |
| `anthropicApiKey` | `string?` | Anthropic API key |
| `googleGeminiApiKey` | `string?` | Google Gemini API key |

### Methods

#### `execute(prompt: string)`
Execute any operation via natural language.

#### `swapExactInput(params)`
```typescript
await agent.swapExactInput({
  amount: '0.1',
  fromSymbol: 'USDC',
  toSymbol: 'ETH',
  slippage: 0.05, // optional, default 1%
});
```

#### `transfer(params)`
```typescript
await agent.transfer({
  to: '0x...',
  amount: '10',
  symbol: 'USDC',
});
```

#### `getOwnBalance(params)`
```typescript
await agent.getOwnBalance({ symbol: 'ETH' });
```

#### `addLiquidity(params)`
```typescript
await agent.addLiquidity({
  amount0: '1',
  asset0Symbol: 'ETH',
  asset1Symbol: 'USDC',
  slippage: 0.01,
});
```

#### `supplyCollateral(params)`
```typescript
await agent.supplyCollateral({
  amount: '100',
  symbol: 'USDT',
});
```

#### `borrowAsset(params)`
```typescript
await agent.borrowAsset({ amount: '50' });
```

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests (requires .env with API keys)
npm test
```

## Environment Variables

Create a `.env` file based on `.env.example`:

```
FUEL_WALLET_PRIVATE_KEY=your-private-key
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_GEMINI_API_KEY=your-google-key
```

## License

MIT
