# fuel-agent-kit

TypeScript utilities for building AI agents that can read balances and execute
transactions on the Fuel network.

The package wraps Fuel wallet operations, Mira swaps and liquidity actions, and
Swaylend lending actions behind a LangChain tool-calling agent.

## Features

- Create a Fuel-aware LangChain agent with OpenAI, Anthropic, or Gemini models
- Transfer verified Fuel assets
- Read wallet balances
- Swap assets on Mira
- Add liquidity to Mira pools
- Supply collateral and borrow assets on Swaylend
- Build standalone transaction flows without using the agent executor

## Installation

```bash
npm install fuel-agent-kit fuels
```

`fuels` is a peer dependency and must be installed by the application using this
package.

## Quick Start

```ts
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o-mini',
  openAiApiKey: process.env.OPENAI_API_KEY!,
});

const result = await agent.execute('swap 5 USDC for ETH');

console.log(result);
```

## Configuration

Create a `.env` file or provide these values from your runtime environment:

```bash
FUEL_WALLET_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_GEMINI_API_KEY=your_gemini_key
```

Only the API key for the selected model provider is required.

```ts
const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'claude-3-5-sonnet-20241022',
  anthropicApiKey: process.env.ANTHROPIC_API_KEY!,
});
```

## Direct API Usage

You can call the Fuel helpers directly through the `FuelAgent` instance when you
do not want an LLM to decide which tool to use.

```ts
await agent.transfer({
  to: 'fuel1...',
  amount: '1',
  symbol: 'ETH',
});

await agent.getOwnBalance({
  symbol: 'USDC',
});
```

Available methods:

- `execute(input)` runs the LangChain agent
- `transfer(params)` transfers an asset
- `swapExactInput(params)` swaps an exact input amount on Mira
- `addLiquidity(params)` adds liquidity to a Mira pool
- `supplyCollateral(params)` supplies collateral on Swaylend
- `borrowAsset(params)` borrows from Swaylend
- `getOwnBalance(params)` reads the configured wallet balance

## Development

```bash
npm install
npm run build
npm test
npm run check-format
```

The main source files live in `src/`. Tests are in `test/` and use Vitest.

## Safety Notes

This package can submit real blockchain transactions. Use a test wallet while
developing, keep private keys out of source control, and review agent prompts
before allowing the agent to execute transactions.

## License

MIT
