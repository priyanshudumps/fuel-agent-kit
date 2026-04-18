# Fuel Agent Kit

An AI agent kit for the Fuel blockchain that enables natural language-controlled DeFi operations. Powered by LangChain, the `FuelAgent` class wraps Fuel network interactions behind an LLM interface — just tell it what to do in plain English.

## Features

- **Natural Language Control** — Execute DeFi transactions via plain text prompts
- **Multi-LLM Support** — OpenAI, Anthropic Claude, Google Gemini
- **Built-in DeFi Tools**:
  - Transfer any verified Fuel asset
  - Swap tokens on [Mira DEX](https://www.mira.ooo/)
  - Supply collateral on [SwayLend](https://swaylend.com/)
  - Borrow assets on SwayLend
  - Add liquidity to Mira pools
  - Read wallet balances
- **TypeScript First** — Full type safety end-to-end
- **Fuel Network** — Built on the FuelVM for fast, secure execution

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

const result = await agent.execute(
  'Swap 10 USDC for ETH on Mira DEX with 0.5% slippage'
);

console.log(result);
```

## Configuration

### Environment Variables

Create a `.env` file (see `.env.example`):

```env
FUEL_WALLET_PRIVATE_KEY=your_private_key_here
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_GEMINI_API_KEY=your_gemini_key
```

### FuelAgentConfig

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `walletPrivateKey` | `string` | Yes | Your Fuel wallet private key |
| `model` | `'gpt-4o' \| 'gpt-4o-mini' \| 'claude-sonnet-4-20250514' \| 'claude-3-5-sonnet-20241022' \| 'claude-3-5-haiku-20241022' \| 'gemini-2.0-flash' \| 'gemini-1.5-flash'` | Yes | LLM model to use |
| `openAiApiKey` | `string` | If using OpenAI | Your OpenAI API key |
| `anthropicApiKey` | `string` | If using Anthropic | Your Anthropic API key |
| `googleGeminiApiKey` | `string` | If using Gemini | Your Google Gemini API key |

## Available Tools

The agent exposes the following tools, which can be triggered via natural language:

### `fuel_transfer`
Transfer any verified Fuel asset to another wallet.

```
"Transfer 100 USDC to 0x..."
```

**Parameters:**
- `to` — Recipient wallet address
- `amount` — Amount to transfer
- `symbol` — Asset symbol (e.g. USDC, ETH)

### `swap_exact_input`
Swap exact input amount on Mira DEX.

```
"Swap 50 ETH for USDC"
```

**Parameters:**
- `amount` — Amount to swap
- `fromSymbol` — Source asset symbol
- `toSymbol` — Target asset symbol
- `slippage` — Slippage tolerance (default: 0.01 = 1%)

### `supply_collateral`
Supply collateral to SwayLend to earn interest.

```
"Supply 500 USDC as collateral on SwayLend"
```

**Parameters:**
- `amount` — Amount to supply
- `symbol` — Asset symbol

### `borrow_asset`
Borrow USDC against your supplied collateral on SwayLend.

```
"Borrow 100 USDC on SwayLend"
```

**Parameters:**
- `amount` — Amount to borrow (USDC)

### `add_liquidity`
Add liquidity to a Mira pool.

```
"Add 100 ETH and 1000 USDC to the ETH/USDC pool on Mira"
```

**Parameters:**
- `amount0` — Amount of first asset
- `asset0Symbol` — First asset symbol
- `asset1Symbol` — Second asset symbol
- `slippage` — Slippage tolerance (default: 0.01 = 1%)

### `get_own_balance`
Check your wallet's balance for a specific asset.

```
"What's my USDC balance?"
```

**Parameters:**
- `symbol` — Asset symbol

### `get_balance`
Check any wallet's balance for a specific asset.

```
"What's 0x...'s ETH balance?"
```

**Parameters:**
- `walletAddress` — Wallet address to query
- `assetSymbol` — Asset symbol

## Direct API Usage

You can also call individual DeFi functions directly without the agent:

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

// Direct swap
await agent.swapExactInput({
  amount: '10',
  fromSymbol: 'USDC',
  toSymbol: 'ETH',
  slippage: 0.005,
});

// Direct transfer
await agent.transfer({
  to: '0x...',
  amount: '100',
  symbol: 'USDC',
});

// Check balance
const balance = await agent.getOwnBalance({ symbol: 'ETH' });
```

## Supported Assets

The kit uses verified Fuel network assets fetched dynamically. Common assets include:
- **ETH** — Fuel's base asset
- **USDC** — Stablecoin for DeFi operations
- **BTC** — Wrapped Bitcoin on Fuel
- And all other [Fuel-verified assets](https:// fuelscan.io/)

## Architecture

```
FuelAgent (main class)
  └── LangChain AgentExecutor
        └── createToolCallingAgent
              ├── fuel_transfer        → transfers/transfers.ts
              ├── swap_exact_input     → mira/swap.ts
              ├── supply_collateral    → swaylend/supply.ts
              ├── borrow_asset         → swaylend/borrow.ts
              ├── add_liquidity        → mira/addLiquidity.ts
              ├── get_own_balance      → read/balance.ts
              └── get_balance          → read/balance.ts
```

**Key Dependencies:**
- [LangChain](https://js.langchain.com/) — Agent framework
- [fuels](https://fuellabs.github.io/fuels-ts/) — Fuel blockchain SDK
- [mira-dex-ts](https://www.mira.ooo/) — Mira DEX SDK
- [@pythnetwork/pyth-fuel-js](https://pyth.network/) — Price oracle integration

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm run test

# Type check
npm run lint

# Check formatting
npm run check-format

# Full CI check
npm run ci
```

## Prerequisites

- Node.js 18+
- A funded Fuel wallet (for on-chain operations)
- API keys for your chosen LLM provider

## Disclaimer

This kit interacts with live DeFi protocols on the Fuel mainnet. Always verify transaction details before approving, and never share your private key.

## License

MIT
