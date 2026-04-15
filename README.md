# Fuel Agent Kit

An AI agent toolkit for the Fuel blockchain, built with LangChain.

## Features

- **Multi-LLM Support**: Works with OpenAI, Anthropic, and Google AI models
- **Fuel Blockchain Integration**: Built specifically for the Fuel network
- **Modular Architecture**: Easy to extend and customize
- **TypeScript**: Fully typed for better developer experience

## Installation

```bash
npm install fuel-agent-kit
```

## Quick Start

```typescript
import { FuelAgent } from 'fuel-agent-kit';

// Initialize the agent with your preferred LLM
const agent = new FuelAgent({
  llm: 'openai', // or 'anthropic', 'google'
  apiKey: process.env.OPENAI_API_KEY
});

// Start interacting with the Fuel blockchain
await agent.connect();
const balance = await agent.getBalance('0x...');
console.log('Balance:', balance);
```

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Required variables:
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` or `GOOGLE_API_KEY`
- `FUEL_PROVIDER_URL` (optional, defaults to testnet)

### LLM Providers

The kit supports multiple LLM providers:

1. **OpenAI** (default)
2. **Anthropic Claude**
3. **Google Gemini**

## Development

### Setup

```bash
git clone https://github.com/Halo11112222/fuel-agent-kit.git
cd fuel-agent-kit
npm install
```

### Scripts

- `npm run build` - Build the project
- `npm run test` - Run tests
- `npm run lint` - Check TypeScript types
- `npm run format` - Format code with Prettier

### Testing

```bash
npm run test
```

## API Reference

### FuelAgent

The main class for interacting with the Fuel blockchain.

#### Constructor Options

- `llm`: LLM provider ('openai', 'anthropic', 'google')
- `apiKey`: API key for the chosen LLM provider
- `providerUrl`: Fuel provider URL (optional)

#### Methods

- `connect()`: Connect to the Fuel network
- `getBalance(address: string)`: Get balance for an address
- `transfer(to: string, amount: number)`: Transfer tokens
- `callContract(contractId: string, method: string, args: any[])`: Call a smart contract method

## Examples

Check the `examples/` directory for more usage examples.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [Fuel Network](https://fuel.network/)
- DEX integration via [Mira Protocol](https://mira.ly/)