# 🚀 Fuel Agent Kit

> **An AI agent toolkit for the Fuel Network ecosystem** — enabling autonomous on-chain interactions across DeFi protocols.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Fuel Network](https://img.shields.io/badge/powered%20by-Fuel%20Network-00F58C)](https://fuel.network/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)](https://www.typescriptlang.org/)
[![npm](https://img.shields.io/badge/npm-%E2%89%A516.0.0-red)](https://www.npmjs.com/)

---

## 📖 Overview

Fuel Agent Kit provides a modular, TypeScript-based framework for building AI agents that can interact with the Fuel Network. It includes built-in integrations with major Fuel DeFi protocols, transfer utilities, and a flexible tool-registration system.

### ✨ Features

- **Multi-Protocol Support** — Out-of-the-box integrations for SwayLend (lending), Mira (DEX/AMM), and Read (data indexing)
- **Transfer Utilities** — Secure asset transfer helpers with gas estimation and fee management
- **Agent Framework** — Pluggable agent architecture with configurable tool chains
- **Type-Safe** — Full TypeScript support with typed Fuel SDK interactions
- **Modular Design** — Add or remove protocol integrations without touching core logic

---

## 📦 Installation

```bash
npm install fuel-agent-kit
# or
pnpm install fuel-agent-kit
# or
yarn add fuel-agent-kit
```

---

## 🚀 Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';
import { registerTools } from 'fuel-agent-kit/tools';

// Initialize the agent
const agent = new FuelAgent({
  network: 'testnet',
  wallet: process.env.FUEL_WALLET,
});

// Register protocol tools
registerTools(agent, {
  swaylend: true,  // Enable lending/borrowing tools
  mira: true,      // Enable DEX swap tools
  read: true,      // Enable data read tools
  transfers: true, // Enable transfer tools
});

// Execute actions
const result = await agent.execute('swap', {
  fromAsset: 'ETH',
  toAsset: 'USDC',
  amount: 100,
});
```

---

## 🧩 Architecture

```
fuel-agent-kit/
├── src/
│   ├── index.ts          # Main entry point
│   ├── agent.ts           # Core agent implementation
│   ├── FuelAgent.ts       # Fuel-specific agent logic
│   ├── tools.ts           # Tool registration & routing
│   ├── constants.ts       # Shared constants
│   ├── mira/              # Mira DEX integration
│   ├── swaylend/          # SwayLend lending integration
│   ├── read/              # Read protocol data tools
│   ├── transfers/         # Asset transfer utilities
│   ├── types/             # TypeScript type definitions
│   └── utils/             # Shared utility functions
├── test/                  # Test suites
├── package.json
└── tsconfig.json
```

---

## 🔧 Protocol Integrations

### 💱 Mira (DEX/AMM)

Automated market maker integration for token swaps on Fuel.

```typescript
import { MiraTools } from 'fuel-agent-kit/mira';

const mira = new MiraTools(provider);
const swapResult = await mira.swap({
  inputToken: 'ETH',
  outputToken: 'USDC',
  amount: 100_000_000, // in atomic units
  slippage: 0.01,      // 1%
});
```

### 🏦 SwayLend (Lending)

Supply and borrow assets on Fuel's lending protocol.

```typescript
import { SwayLendTools } from 'fuel-agent-kit/swaylend';

const swaylend = new SwayLendTools(provider);
await swaylend.supply({
  asset: 'ETH',
  amount: 500_000_000,
});
```

### 📊 Read (Data Indexing)

Query indexed on-chain data with type-safe results.

```typescript
import { ReadTools } from 'fuel-agent-kit/read';

const read = new ReadTools(provider);
const balances = await read.getAccountBalances(address);
```

### 💸 Transfers

Secure asset transfers with gas estimation.

```typescript
import { TransferTools } from 'fuel-agent-kit/transfers';

const transfer = new TransferTools(provider);
const tx = await transfer.send({
  to: recipientAddress,
  asset: 'ETH',
  amount: 10_000_000,
});
```

---

## 🛠️ Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```env
FUEL_PROVIDER_URL=https://testnet.fuel.network/v1/graphql
FUEL_WALLET_PRIVATE_KEY=your_private_key_here
FUEL_NETWORK=testnet
```

### TypeScript Config

The project uses `tsconfig.json` targeting modern TypeScript with strict mode enabled.

---

## 🧪 Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npx vitest run test/FuelAgent.test.ts
```

---

## 📋 Prerequisites

- **Node.js** ≥ 16.0.0
- **npm** / **pnpm** / **yarn**
- **Fuel Wallet** — for signing transactions
- **Fuel Provider URL** — testnet or mainnet endpoint

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to the branch (`git push origin feat/your-feature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/priyanshudumps/fuel-agent-kit.git
cd fuel-agent-kit
npm install
npm run build
npm test
```

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- [Fuel Network](https://fuel.network/)
- [Fuel Documentation](https://docs.fuel.network/)
- [Mira DEX](https://mira.ly/)
- [SwayLend](https://swaylend.com/)
- [Report an Issue](https://github.com/priyanshudumps/fuel-agent-kit/issues)

---

<div align="center">
  <em>Built with ❤️ for the Fuel ecosystem</em>
</div>
