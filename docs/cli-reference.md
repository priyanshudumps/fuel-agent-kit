

# Fuel Agent Kit CLI Reference

Fuel Agent Kit is a powerful toolkit for interacting with the Fuel blockchain. While it's primarily designed as a TypeScript library, it can be used programmatically through various commands and tools.

## Installation

First, install the Fuel Agent Kit:

```bash
npm install fuel-agent-kit
```

## Basic Usage

### Initializing a Fuel Agent

To initialize a Fuel Agent, you need to create an instance with your wallet private key and configuration:

```javascript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: 'your_private_key_here',
  model: 'gpt-4', // or other supported model
  openAiApiKey: 'your_openai_api_key' // if required
});
```

### Available Tools

Fuel Agent Kit provides several tools for interacting with the Fuel blockchain:

#### 1. Transfer Assets

Transfer assets from your wallet to another address:

```javascript
await agent.transfer({
  to: 'recipient_address',
  amount: '1000',
  symbol: 'USDC'
});
```

#### 2. Swap Assets

Swap one asset for another using Mira DEX:

```javascript
await agent.swapExactInput({
  amount: '1000',
  fromSymbol: 'USDC',
  toSymbol: 'ETH',
  slippage: 0.01 // optional, default is 0.01 (1%)
});
```

#### 3. Supply Collateral

Supply collateral to Swaylend for lending:

```javascript
await agent.supplyCollateral({
  amount: '1000',
  symbol: 'USDC'
});
```

#### 4. Borrow Assets

Borrow assets from Swaylend:

```javascript
await agent.borrowAsset({
  amount: '500'
});
```

#### 5. Add Liquidity

Add liquidity to a Mira pool:

```javascript
await agent.addLiquidity({
  amount0: '1000',
  asset0Symbol: 'USDC',
  asset1Symbol: 'ETH',
  slippage: 0.01 // optional, default is 0.01 (1%)
});
```

#### 6. Check Balances

Check your wallet balance:

```javascript
const balance = await agent.getOwnBalance({
  symbol: 'USDC'
});
```

Check another wallet's balance:

```javascript
const balance = await agent.getBalance({
  walletAddress: 'recipient_address',
  assetSymbol: 'USDC'
});
```

## Theoretical CLI Commands

While Fuel Agent Kit is primarily a library, here's a theoretical CLI interface that could be implemented:

### fuel-agent init

Initialize a new Fuel Agent configuration:

```bash
fuel-agent init --wallet-private-key <your_private_key> --model <model_name>
```

Example:
```bash
fuel-agent init --wallet-private-key 0x123...abc --model gpt-4
```

### fuel-agent deploy

Deploy a smart contract to the Fuel blockchain:

```bash
fuel-agent deploy --contract <contract_path> --args <arguments>
```

### fuel-agent run

Execute a transaction or command:

```bash
fuel-agent run <command> [options]
```

Common commands:
- `transfer`: Transfer assets
- `swap`: Swap assets
- `supply`: Supply collateral
- `borrow`: Borrow assets
- `add-liquidity`: Add liquidity to a pool
- `balance`: Check wallet balance

Examples:
```bash
fuel-agent run transfer --to 0x123...abc --amount 1000 --symbol USDC
fuel-agent run swap --amount 1000 --from USDC --to ETH
fuel-agent run balance --symbol USDC
```

### fuel-agent execute

Execute a custom transaction:

```bash
fuel-agent execute --script <script_path> [options]
```

## Configuration

Fuel Agent Kit can be configured with various options:

```javascript
const agent = new FuelAgent({
  walletPrivateKey: 'your_private_key',
  model: 'gpt-4',
  openAiApiKey: 'your_openai_api_key',
  anthropicApiKey: 'your_anthropic_api_key',
  googleGeminiApiKey: 'your_gemini_api_key'
});
```

## Supported Models

Fuel Agent Kit supports multiple AI models:
- OpenAI models (e.g., gpt-4, gpt-3.5-turbo)
- Anthropic models (e.g., claude-2)
- Google Gemini models

## Error Handling

Fuel Agent Kit provides detailed error handling. When a transaction fails, it returns a response in the following format:

```
The transaction failed.
[Error details]
```

For successful transactions, it returns:

```
The transaction was successful. The explorer link is: https://app.fuel.network/tx/0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef/simple
```

## API Reference

For more detailed API information, refer to the [Fuel Agent Kit documentation](https://github.com/dhaiwat10/fuel-agent-kit).

