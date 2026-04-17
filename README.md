# Fuel Agent Kit

A powerful toolkit for building AI agents on the Fuel Network. This kit provides a set of tools and a base agent class to interact with Fuel's high-performance blockchain.

## Features
- **Asset Management**: Check balances and fetch asset metadata.
- **Transfers**: Seamlessly transfer tokens on the Fuel network.
- **DeFi Integrations**:
  - **Mira**: Swap tokens and manage liquidity.
  - **SwayLend**: Deposit, borrow, and manage lending positions.
- **Extensible**: Easily add new tools and integrations.

## Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment**:
   Copy `.env.example` to `.env` and provide your Fuel private key and provider URL.
   ```bash
   cp .env.example .env
   ```

3. **Build the kit**:
   ```bash
   npm run build
   ```

## Usage

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  privateKey: process.env.FUEL_PRIVATE_KEY,
  providerUrl: process.env.FUEL_PROVIDER_URL
});

// Run commands or integrate with AI frameworks
```

## Contributing
Contributions are welcome! Please submit a PR or open an issue.

## License
MIT
