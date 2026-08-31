# fuel-agent-kit

An AI agent toolkit for the [Fuel](https://fuel.network/) blockchain. It lets you spin up a LangChain-powered agent that can read balances, swap tokens, add liquidity, transfer assets, and interact with [SwayLend](https://swaylend.com/) — all from natural language.

## Features

- **Natural-language execution** – ask the agent to swap, transfer, supply collateral, borrow, or check balances.
- **Multi-model support** – works with OpenAI, Anthropic, or Google Gemini models.
- **Fuel-native operations** – built on top of `fuels` and `mira-dex-ts` for swaps and liquidity, plus SwayLend for lending/borrowing.
- **Extensible tool set** – add new capabilities by registering extra tools in `src/tools.ts`.

## Install

```bash
npm install fuel-agent-kit
```

`fuel-agent-kit` declares `fuels` as a peer dependency, so make sure it is installed in your project:

```bash
npm install fuels@^0.96.1
```

## Quick start

1. Copy `.env.example` to `.env` and fill in the required keys:

```bash
cp .env.example .env
```

2. Create an agent instance:

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o-mini', // or any supported model key
  openAiApiKey: process.env.OPENAI_API_KEY,
});

const result = await agent.execute('Swap 10 USDC for ETH on Fuel.');
console.log(result.output);
```

## Supported actions

| Action | Description | Entry point |
|---|---|---|
| `getOwnBalance` | Read the wallet's balance for a given asset | `FuelAgent.getOwnBalance` |
| `transfer` | Send an asset to another address | `FuelAgent.transfer` |
| `swapExactInput` | Swap one asset for another via Mira DEX | `FuelAgent.swapExactInput` |
| `addLiquidity` | Add liquidity to a Mira pool | `FuelAgent.addLiquidity` |
| `supplyCollateral` | Supply collateral on SwayLend | `FuelAgent.supplyCollateral` |
| `borrowAsset` | Borrow an asset from SwayLend | `FuelAgent.borrowAsset` |

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `FUEL_WALLET_PRIVATE_KEY` | Yes | Private key of the Fuel wallet the agent will use |
| `OPENAI_API_KEY` | For OpenAI models | API key for OpenAI |
| `ANTHROPIC_API_KEY` | For Anthropic models | API key for Anthropic |
| `GOOGLE_GEMINI_API_KEY` | For Gemini models | API key for Google Gemini |

See `.env.example` for the exact format.

## Development

```bash
# Install dependencies
npm install

# Run the build
npm run build

# Run tests
npm run test

# Run the linter / type checker
npm run lint

# Format the code
npm run format
```

## Project structure

```
src/
├── FuelAgent.ts      # Main agent class
├── agent.ts          # LangChain agent setup
├── tools.ts          # Tool definitions exposed to the agent
├── mira/             # Mira DEX operations (swap, add liquidity)
├── swaylend/         # SwayLend operations (supply, borrow)
├── transfers/        # Asset transfers
├── read/             # Read-only blockchain calls
├── types/            # Shared TypeScript types
└── utils/            # Helpers (models, assets, explorer, setup)
```

## License

MIT
