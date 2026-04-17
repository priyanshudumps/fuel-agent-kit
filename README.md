# Fuel Agent Kit ⛽🤖

A powerful, type-safe toolkit for building AI agents that interact with the Fuel Network. This kit provides high-level abstractions for DeFi protocols, account management, and on-chain interactions, enabling agents to perform complex financial operations autonomously.

## ✨ Features

- **Agent Framework**: Seamlessly integrate with LLMs to perform Fuel actions.
- **DeFi Integrations**:
  - **Mira**: Automated liquidity provision and swaps.
  - **Swaylend**: Lending and borrowing operations.
- **On-chain Tools**:
  - Token transfers and balance checks.
  - Secure account management.
  - Type-safe Fuel standard interactions.
- **Developer Friendly**: Built with TypeScript, Vite, and Vitest for a modern DX.

## 🚀 Installation

```bash
npm install fuel-agent-kit
# or
yarn add fuel-agent-kit
```

## 🛠️ Usage

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  privateKey: process.env.FUEL_PRIVATE_KEY,
  providerUrl: 'https://mainnet.fuel.network/v1/graphql'
});

// Example: Get balance
const balance = await agent.getBalance();
console.log(`Current Balance: ${balance} ETH`);

// Example: Swap tokens on Mira
await agent.mira.swap({
  from: 'ETH',
  to: 'USDC',
  amount: 0.1
});
```

## 📂 Project Structure

- `src/agent.ts`: Core agent logic.
- `src/tools.ts`: Tool definitions for LLM function calling.
- `src/mira/`: Mira DEX integration.
- `src/swaylend/`: Swaylend protocol integration.
- `src/transfers/`: On-chain transfer utilities.

## 🤝 Contributing

Contributions and bug reports are welcome! Please see the `CONTRIBUTING.md` for guidelines.

---
*Powered by the Fuel Network Ecosystem.*
