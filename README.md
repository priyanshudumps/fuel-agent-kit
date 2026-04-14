# Fuel Agent Kit

An AI agent toolkit for interacting with the Fuel blockchain ecosystem.

## Features

- **Wallet Management**: Create and manage Fuel wallets
- **Token Operations**: Transfer tokens, check balances
- **DeFi Integration**: Swap tokens on Mira DEX, provide liquidity
- **Lending**: Supply collateral and borrow assets on Swaylend
- **AI-Powered**: Use natural language to execute blockchain operations

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your-private-key',
  model: 'openai',
  openAiApiKey: 'your-openai-key',
});

// Use natural language to interact
const result = await agent.execute('Check my balance');
```

## Supported Operations

| Operation | Method | Description |
|-----------|--------|-------------|
| Swap | `swapExactInput()` | Swap tokens on Mira DEX |
| Transfer | `transfer()` | Transfer tokens to another address |
| Supply | `supplyCollateral()` | Supply collateral on Swaylend |
| Borrow | `borrowAsset()` | Borrow assets from Swaylend |
| Liquidity | `addLiquidity()` | Add liquidity to Mira pools |
| Balance | `getOwnBalance()` | Check token balances |

## Configuration

Create a `.env` file:

```env
WALLET_PRIVATE_KEY=your_private_key_here
OPENAI_API_KEY=your_openai_key_here
```

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Test
npm test

# Format code
npm run format
```

## Supported AI Models

- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google Gemini

## License

MIT

## Related Projects

- [Fuel Network](https://fuel.network/)
- [Mira Protocol](https://mira.ly/)
- [Swaylend](https://swaylend.com/)
