# fuel-agent-kit

An AI agent toolkit for the [Fuel](https://fuel.network/) blockchain, built with [LangChain](https://js.langchain.com/).

## Features

- **Multi-LLM support** — OpenAI, Anthropic, Google Gemini
- **DeFi tools** — Mira DEX swaps, SwayLend interactions
- **Price oracles** — Pyth Network integration for real-time price data
- **Transfer tools** — Send and manage Fuel assets
- **Extensible tool system** — Build custom tools for your agent

## Installation

\\\ash
npm install fuel-agent-kit
\\\

## Quick Start

1. Copy the environment template:

\\\ash
cp .env.example .env
\\\

2. Fill in your credentials:

\\\env
FUEL_WALLET_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_key
\\\

3. Create an agent:

\\\	ypescript
import { createFuelAgent } from "fuel-agent-kit";

const agent = createFuelAgent({
  model: "gpt-4",
  privateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
});

const result = await agent.run("What is the balance of my wallet?");
console.log(result);
\\\

## Development

\\\ash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm run test

# Format code
npm run format

# Type check
npm run lint
\\\

## API

### \createFuelAgent(options)\

Creates a new Fuel agent instance.

**Options:**
- \model\ — LLM model to use (e.g., \"gpt-4"\, \"claude-3-5-sonnet"\, \"gemini-pro"\)
- \privateKey\ — Fuel wallet private key

### Exports

- \FuelAgent\ — Main agent class
- \createFuelAgent\ — Factory function
- \	ools\ — Built-in tools (transfers, swaps, lending, price feeds)

## License

MIT