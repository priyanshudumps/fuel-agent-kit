# Fuel Agent Kit

A TypeScript toolkit for building AI-powered agents on the [Fuel Network](https://fuel.network). Fuel Agent Kit provides the primitives and utilities you need to create autonomous agents that can read on-chain data, execute transfers, interact with DeFi protocols like **Mira** and **Swaylend**, and more — all driven by LLM tool-calling.

---

## ✨ Features

- **FuelAgent** — High-level agent class that wraps wallet management, tool registration, and LLM integration.
- **On-chain reads** — Query balances, contract state, and transaction history on the Fuel network.
- **Token transfers** — Programmatically send native and custom assets.
- **Mira DEX integration** — Swap tokens through the Mira decentralized exchange.
- **Swaylend integration** — Supply, borrow, and manage lending positions on Swaylend.
- **Extensible tool system** — Register custom tools so your agent can perform any on-chain action you define.

---

## 📦 Installation

```bash
npm install fuel-agent-kit
```

> **Prerequisites:** Node.js ≥ 18 and npm ≥ 9 are recommended.

---

## ⚙️ Configuration

Create a `.env` file in your project root (see `.env.example` for reference):

```env
FUEL_PRIVATE_KEY=your_fuel_wallet_private_key
OPENAI_API_KEY=your_openai_api_key          # or another supported LLM provider
```

---

## 🚀 How to Use

### 1. Basic setup

```typescript
import { FuelAgent } from "fuel-agent-kit";

const agent = new FuelAgent({
  privateKey: process.env.FUEL_PRIVATE_KEY,
});
```

### 2. Run the agent

```typescript
// Start an interactive agent session
await agent.run("What is my current ETH balance on Fuel?");
```

### 3. Execute a transfer

```typescript
await agent.run("Send 0.1 ETH to 0xABC...123");
```

### 4. Swap via Mira DEX

```typescript
await agent.run("Swap 0.5 ETH for USDC on Mira");
```

### 5. Interact with Swaylend

```typescript
await agent.run("Supply 100 USDC to Swaylend");
```

---

## 🏗️ Project Structure

```
fuel-agent-kit/
├── src/
│   ├── FuelAgent.ts     # Main agent class
│   ├── agent.ts         # Agent orchestration logic
│   ├── tools.ts         # Tool definitions for LLM function-calling
│   ├── constants.ts     # Network constants
│   ├── index.ts         # Package entry point
│   ├── mira/            # Mira DEX integration
│   ├── swaylend/        # Swaylend lending integration
│   ├── transfers/       # Token transfer utilities
│   ├── read/            # On-chain read operations
│   ├── types/           # TypeScript type definitions
│   └── utils/           # Shared helpers
├── test/                # Test suite (Vitest)
├── package.json
├── tsconfig.json
└── tsup.config.ts       # Build configuration
```

---

## 🧪 Running Tests

```bash
npm test
```

Tests are powered by [Vitest](https://vitest.dev/).

---

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/priyanshudumps/fuel-agent-kit.git
cd fuel-agent-kit

# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m "feat: add new feature"`)
4. Push to your branch (`git push origin feat/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
