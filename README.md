# Fuel Agent Kit

Fuel Agent Kit is a TypeScript toolkit for building AI agents that can read balances and perform common Fuel ecosystem actions through LangChain tools.

The package wraps wallet-aware operations for:

- Fuel asset transfers
- Mira swaps
- Mira liquidity provision
- Swaylend collateral supply
- Swaylend borrowing
- Wallet and address balance lookups

> **Security note:** the kit signs transactions with the wallet private key you provide. Use a funded development wallet first, never commit secrets, and carefully review every agent instruction before allowing real transactions.

## Installation

```bash
npm install fuel-agent-kit fuels
```

`fuels` is a peer dependency and must be installed by the consuming project.

## Environment variables

Copy `.env.example` and fill in only the providers you plan to use:

```bash
cp .env.example .env
```

Required:

```bash
FUEL_WALLET_PRIVATE_KEY=your-development-wallet-private-key
```

Optional model provider keys:

```bash
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_GEMINI_API_KEY=your-gemini-key
```

## Quick start

```ts
import { FuelAgent } from "fuel-agent-kit";

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: "openai:gpt-4o-mini",
  openAiApiKey: process.env.OPENAI_API_KEY,
});

const response = await agent.execute(
  "Check my ETH balance and explain the result in one sentence.",
);

console.log(response);
```

## Direct API usage

You can also call supported actions directly without natural-language execution.

```ts
import { FuelAgent } from "fuel-agent-kit";

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: "openai:gpt-4o-mini",
  openAiApiKey: process.env.OPENAI_API_KEY,
});

await agent.transfer({
  to: "fuel1...",
  amount: "1.0",
  symbol: "ETH",
});

const balance = await agent.getOwnBalance({
  symbol: "ETH",
});

console.log(balance);
```

## Available tools

`createTools(agent)` exposes the following LangChain tools:

- `fuel_transfer` — transfer a verified Fuel asset to another wallet.
- `swap_exact_input` — swap exact input on Mira.
- `supply_collateral` — supply collateral on Swaylend.
- `borrow_asset` — borrow an asset on Swaylend.
- `add_liquidity` — add liquidity to a Mira pool.
- `get_own_balance` — read the connected wallet balance for an asset.
- `get_balance` — read an asset balance for any wallet address.

## Configuration

`FuelAgent` accepts:

```ts
interface FuelAgentConfig {
  walletPrivateKey: string;
  model: "openai:gpt-4o-mini" | "anthropic:claude-3-5-sonnet" | string;
  openAiApiKey?: string;
  anthropicApiKey?: string;
  googleGeminiApiKey?: string;
}
```

The exact model names are defined in `src/utils/models.ts`.

## Development

```bash
npm install
npm run build
npm test
npm run lint
npm run check-format
```

For the full CI sequence:

```bash
npm run ci
```

## Repository structure

```text
src/
  FuelAgent.ts          Main class and direct action methods
  agent.ts              LangChain agent construction
  tools.ts              LangChain tool definitions
  mira/                 Mira swap and liquidity operations
  swaylend/             Swaylend supply and borrow operations
  transfers/            Fuel asset transfers
  read/                 Balance readers
  utils/                Shared setup, assets, explorer, and model helpers
test/                   Vitest test suite
```

## Safety checklist

Before running an agent with a real wallet:

1. Start with a fresh development wallet.
2. Keep private keys in environment variables only.
3. Never paste private keys into prompts.
4. Review tool calls and transaction parameters before signing.
5. Add spending limits or human approval in production agents.

## License

MIT
