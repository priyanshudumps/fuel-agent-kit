# Fuel Agent Kit

An AI agent for Fuel blockchain that provides automated interactions with various Fuel ecosystem protocols.

## 🚀 Features

- **AI-Powered Interactions**: Leverage LangChain with Anthropic, OpenAI, and Google GenAI for intelligent blockchain operations
- **Mira DEX Integration**: Automated token swaps and liquidity operations on Mira DEX
- **Swaylend Support**: Lending and borrowing operations on Swaylend protocol
- **Token Transfers**: Automated fuel token transfers with price oracle support (Pyth Network)
- **Type-Safe**: Built with TypeScript for robust, type-safe operations
- **Extensible**: Easy to add new tools and protocols

## 📦 Installation

```bash
# Install the package
npm install fuel-agent-kit

# Peer dependency required
npm install fuels@^0.96.1
```

## 🛠️ Usage

```typescript
import { FuelAgent } from 'fuel-agent-kit';

// Initialize the agent
const agent = new FuelAgent({
  providerUrl: 'https://mainnet.fuel.network/v1/graphql',
  wallet: 'your-wallet-private-key',
});

// Example: Perform a token swap on Mira DEX
const result = await agent.swap({
  fromToken: '0x...',
  toToken: '0x...',
  amount: '100',
});

console.log('Swap completed:', result);
```

## 📚 Documentation

### Core Modules

- **FuelAgent.ts**: Main agent class with core functionality
- **agent.ts**: Agent configuration and initialization
- **tools.ts**: Collection of available tools for AI interactions
- **constants.ts**: Protocol constants and configuration

### Protocol Integrations

- **mira/**: Mira DEX operations (swaps, liquidity)
- **swaylend/**: Swaylend lending protocol
- **transfers/**: Token transfer operations
- **read/**: Read-only operations and data queries

### Utilities

- **types/**: TypeScript type definitions
- **utils/**: Helper functions and utilities

## 🔧 Development

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm run test

# Format code
npm run format

# Check formatting
npm run check-format

# Lint
npm run lint

# Full CI check
npm run ci
```

## 📝 Available Scripts

| Script | Description |
|--------|-------------|
| `build` | Build the project with tsup |
| `test` | Run Vitest tests |
| `lint` | TypeScript type checking |
| `format` | Format code with Prettier |
| `check-format` | Verify code formatting |
| `check-exports` | Validate package exports |
| `ci` | Run full CI pipeline |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Fuel Network](https://fuel.network/) - The Fuel blockchain platform
- [LangChain](https://langchain.com/) - AI framework
- [Mira DEX](https://mira.network/) - Decentralized exchange
- [Swaylend](https://swaylend.finance/) - Lending protocol
- [Pyth Network](https://pyth.network/) - Price oracle

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/dhaiwat10/fuel-agent-kit/issues)
- **Author**: Dhaiwat Pandya - [@dhaiwat10](https://twitter.com/dhaiwat10)
- **Homepage**: [GitHub Repository](https://github.com/dhaiwat10/fuel-agent-kit)

---

Made with ❤️ for the Fuel ecosystem
