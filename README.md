# Fuel Agent Kit

Fuel Agent Kit is a TypeScript package for building AI agents that can inspect
balances and execute common transactions on the Fuel network. It wraps Fuel
wallet credentials, LangChain tool calling, and Fuel ecosystem integrations into
one `FuelAgent` class.

## Features

- Run natural-language Fuel network requests through a LangChain agent
- Transfer verified Fuel assets
- Swap exact input assets on Mira
- Add liquidity to Mira pools
- Supply collateral and borrow assets on Swaylend
- Read wallet balances for the active wallet or another address
- Use OpenAI, Anthropic, or Gemini chat models

## Installation

Install the package together with its Fuel peer dependency:

```bash
npm install fuel-agent-kit fuels
```

## Configuration

Create a `FuelAgent` with a Fuel wallet private key, a supported model name, and
the API key for the selected model provider.

```ts
import { FuelAgent } from "fuel-agent-kit";

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: "gpt-4o-mini",
  openAiApiKey: process.env.OPENAI_API_KEY,
});
```

Supported model names:

| Model | Provider key |
| --- | --- |
| `gpt-4o` | `openAiApiKey` |
| `gpt-4o-mini` | `openAiApiKey` |
| `claude-3-5-sonnet-latest` | `anthropicApiKey` |
| `claude-3-5-haiku-latest` | `anthropicApiKey` |
| `gemini-1.5-flash` | `googleGeminiApiKey` |
| `gemini-2.0-flash-exp` | `googleGeminiApiKey` |

Never commit wallet private keys or model provider API keys. Load them from a
secret manager or local environment variables.

## Usage

Use `execute` for natural-language requests:

```ts
const response = await agent.execute("What is my USDC balance?");
console.log(response);
```

You can also call the Fuel operations directly:

```ts
await agent.transfer({
  to: "fuel1...",
  amount: "1.5",
  symbol: "USDC",
});

const balance = await agent.getOwnBalance({
  symbol: "ETH",
});
```

## Available Operations

| Method | Description |
| --- | --- |
| `execute(input)` | Runs a natural-language request through the configured agent |
| `transfer(params)` | Transfers a verified Fuel asset to another wallet |
| `swapExactInput(params)` | Swaps an exact input amount on Mira |
| `addLiquidity(params)` | Adds liquidity to a Mira pool |
| `supplyCollateral(params)` | Supplies collateral on Swaylend |
| `borrowAsset(params)` | Borrows an asset on Swaylend |
| `getOwnBalance(params)` | Reads the active wallet balance for an asset |

The exported LangChain tools are also available from `createTools` if you want
to compose them into a custom agent.

## Development

Install dependencies:

```bash
npm install
```

Run the main project checks:

```bash
npm run ci
```

Useful scripts:

| Script | Purpose |
| --- | --- |
| `npm run build` | Builds the package with tsup |
| `npm run test` | Runs the Vitest test suite |
| `npm run lint` | Type-checks the project |
| `npm run check-format` | Checks Prettier formatting |
| `npm run check-exports` | Validates package exports |

## License

MIT
