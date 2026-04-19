# Fuel Agent Kit ⛽🤖

Fuel Agent Kit is a powerful SDK designed to empower AI agents with the ability to interact directly with the **Fuel Network**. Built with LangChain and TypeScript, it provides a seamless interface for executing on-chain actions like swaps, lending, and transfers using natural language or programmatic calls.

## 🚀 Features

- **Swap Assets**: Integration with **Mira DEX** for exact input swaps.
- **Lending & Borrowing**: Interact with **SwayLend** to supply collateral or borrow assets.
- **Transfers**: Easily transfer assets across the Fuel Network.
- **Balance Checks**: Query wallet balances directly.
- **AI-Powered**: Native integration with LangChain (OpenAI, Anthropic, Google Gemini).

## 📦 Installation

```bash
npm install fuel-agent-kit
```

*Note: Requires `fuels` as a peer dependency.*

## 🛠 Usage

### Initialization

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-private-key',
  model: 'gpt-4o', // or 'claude-3-5-sonnet', 'gemini-1.5-pro'
  openAiApiKey: 'your-openai-key'
});
```

### Natural Language Execution

```typescript
const result = await agent.execute("Swap 0.1 ETH for USDC on Mira");
console.log(result.output);
```

### Programmatic API

```typescript
// Swap assets
await agent.swapExactInput({
  amount: 1000000,
  path: [ETH_ID, USDC_ID]
});

// Check balance
const balance = await agent.getOwnBalance({ assetId: ETH_ID });
```

## 🏗 Supported Integrations

- **Mira DEX**: Liquidity provision and swaps.
- **SwayLend**: DeFi lending protocols.
- **Pyth Network**: Real-time price feeds.

## 📜 License

MIT
