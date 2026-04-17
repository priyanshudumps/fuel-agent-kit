# fuel-agent-kit

An AI agent kit for executing transactions and interacting with the Fuel blockchain.

## Features

- **Multi-Model Support**: Use OpenAI, Anthropic, or Google Gemini.
- **Blockchain Actions**: Support for transfers, swapping on Mira DEX, supplying/borrowing on SwayLend, and adding liquidity.
- **LangChain Integration**: Built on top of LangChain for robust agentic workflows.

## Installation

```bash
npm install fuel-agent-kit fuels
```

## Getting Started

### Configuration

You will need a Fuel wallet private key and an API key for your chosen LLM provider.

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-private-key',
  model: 'gpt-4o', // or 'claude-3-5-sonnet-20240620', etc.
  openAiApiKey: 'your-openai-api-key',
});
```

### Usage

You can prompt the agent in natural language:

```typescript
const response = await agent.execute(
  "Swap 0.1 ETH for USDC and then supply that USDC to SwayLend"
);

console.log(response.output);
```

## Supported Actions

The agent is capable of:
- `transfer`: Send assets to another address.
- `swapExactInput`: Swap tokens on Mira DEX.
- `addLiquidity`: Provide liquidity to Mira pools.
- `supplyCollateral`: Supply assets to SwayLend.
- `borrowAsset`: Borrow assets from SwayLend.
- `getOwnBalance`: Check wallet balances.

## Environment Variables

See `.env.example` for the required keys:
- `FUEL_WALLET_PRIVATE_KEY`
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_GEMINI_API_KEY`

## Development

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm run test
```

## License

MIT
