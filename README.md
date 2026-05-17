# Fuel Agent Kit

Fuel Agent Kit is a TypeScript toolkit for building AI agents that can read balances and execute transactions on the Fuel network.

It exposes a `FuelAgent` class plus LangChain tools for common Fuel actions:

- transfer verified Fuel assets
- check wallet balances
- swap on Mira
- add liquidity on Mira
- supply collateral on Swaylend
- borrow USDC on Swaylend

## Installation

```bash
npm install fuel-agent-kit fuels
```

`fuels` is a peer dependency and must be installed by your application.

## Environment variables

Create a `.env` file or pass the values directly to `FuelAgent`:

```bash
FUEL_WALLET_PRIVATE_KEY=your_wallet_private_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_GEMINI_API_KEY=your_gemini_key
```

Only the API key for the model you choose is required.

## Quick start

```ts
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o-mini',
  openAiApiKey: process.env.OPENAI_API_KEY,
});

const result = await agent.execute('What is my USDC balance?');
console.log(result);
```

## Direct API usage

You can call the Fuel actions directly without an LLM.

### Get own balance

```ts
const balance = await agent.getOwnBalance({ symbol: 'USDC' });
console.log(balance);
```

### Transfer

```ts
const tx = await agent.transfer({
  to: 'fuel1...',
  amount: '1.5',
  symbol: 'USDC',
});
console.log(tx);
```

### Swap exact input

```ts
const tx = await agent.swapExactInput({
  amount: '1',
  fromSymbol: 'USDC',
  toSymbol: 'ETH',
  slippage: 0.01,
});
console.log(tx);
```

### Add liquidity

```ts
const tx = await agent.addLiquidity({
  amount0: '10',
  asset0Symbol: 'USDC',
  asset1Symbol: 'ETH',
  slippage: 0.01,
});
console.log(tx);
```

### Supply collateral

```ts
const tx = await agent.supplyCollateral({
  amount: '10',
  symbol: 'USDC',
});
console.log(tx);
```

### Borrow USDC

```ts
const tx = await agent.borrowAsset({ amount: '5' });
console.log(tx);
```

## Supported models

`FuelAgent` supports the model names defined in `src/utils/models.ts`:

- `gpt-4o`
- `gpt-4o-mini`
- `gemini-1.5-flash`
- `gemini-2.0-flash-exp`
- `claude-3-5-sonnet-latest`
- `claude-3-5-haiku-latest`

## Tool list

`createTools(agent)` returns these LangChain tools:

| Tool                | Description                      |
| ------------------- | -------------------------------- |
| `fuel_transfer`     | Transfer a verified Fuel asset   |
| `swap_exact_input`  | Swap exact input on Mira         |
| `supply_collateral` | Supply collateral on Swaylend    |
| `borrow_asset`      | Borrow USDC on Swaylend          |
| `add_liquidity`     | Add liquidity to a Mira pool     |
| `get_own_balance`   | Get the connected wallet balance |
| `get_balance`       | Get any Fuel wallet balance      |

## Development

```bash
npm install
npm run build
npm test
npm run check-format
```

## Safety notes

This package can sign and submit real Fuel transactions. Use a test wallet first and never commit private keys or API keys.
