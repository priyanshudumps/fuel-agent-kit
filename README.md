# fuel-agent-kit

AI agent toolkit for Fuel.

## Install

```bash
npm i fuel-agent-kit
```

## Use

```ts
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  walletPrivateKey: process.env.FUEL_WALLET_PRIVATE_KEY!,
  model: 'gpt-4o-mini',
  openAiApiKey: process.env.OPENAI_API_KEY,
});
```

See `src/` for available tools and methods.
