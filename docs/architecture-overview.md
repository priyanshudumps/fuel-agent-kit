
# Fuel Agent SDK vs Fuel Node Architecture Guide

## Overview

This document explains the relationship between the **Fuel Agent SDK** and the **Fuel Node**, focusing on how they interact through **GraphQL communication**.

---

## Fuel Node

The **Fuel Node** is the core component of the Fuel blockchain infrastructure. It:
- Executes smart contracts
- Manages the blockchain state
- Provides access to blockchain data via APIs

The Fuel Node exposes a **GraphQL API** that allows external applications to query and interact with the blockchain.

---

## Fuel Agent SDK

The **Fuel Agent SDK** is a library designed to simplify interactions with the Fuel Node. It provides:
- High-level abstractions for common blockchain operations
- Type-safe interfaces for working with Fuel blockchain data
- Convenient methods for executing transactions, querying balances, and more

---

## GraphQL Communication

The Fuel Agent SDK communicates with the Fuel Node via **GraphQL queries and mutations**. This interaction can be broken down into:

### 1. Querying Data
The SDK sends GraphQL queries to the Fuel Node to fetch blockchain data such as:
- Account balances
- Transaction histories
- Smart contract states

Example query:
```graphql
query {
  account(id: "0x123...") {
    balance
    transactions {
      id
      status
    }
  }
}
```

### 2. Executing Transactions
The SDK translates high-level operations (e.g., transfers, swaps) into GraphQL mutations that the Fuel Node executes.

Example mutation:
```graphql
mutation {
  transfer(from: "0x123...", to: "0x456...", amount: 100) {
    id
    status
  }
}
```

### 3. Error Handling and Retries
The SDK includes logic for handling GraphQL errors and retrying failed operations, ensuring robustness in communication with the Fuel Node.

---

## Architecture Diagram

```
┌───────────────────────────────────────────────────────────────┐
│                        Fuel Agent SDK                          │
└───────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌───────────────────────────────────────────────────────────────┐
│                        GraphQL API                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │   Queries      │  │  Mutations      │  │  Subscriptions  │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└───────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌───────────────────────────────────────────────────────────────┐
│                        Fuel Node                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │  Blockchain     │  │  State          │  │  Execution      │  │
│  │  Execution      │  │  Management     │  │  Engine         │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

---

## Key Benefits

1. **Abstraction**: The SDK abstracts away the complexity of GraphQL communication, providing a simpler interface for developers.
2. **Type Safety**: TypeScript types ensure that developers interact with the blockchain in a type-safe manner.
3. **Convenience**: Common operations are exposed as methods, reducing boilerplate code.
4. **Extensibility**: The SDK can be extended to support additional Fuel Node features as they are introduced.

---

## Example Usage

Here's a simple example of how the Fuel Agent SDK can be used to transfer tokens:

```typescript
import { FuelAgent } from "@fuel-agent/sdk";

const agent = new FuelAgent("https://fuel-node.example.com/graphql");

async function transferTokens() {
  const result = await agent.transfer({
    from: "0x123...",
    to: "0x456...",
    amount: 100,
  });

  console.log("Transaction result:", result);
}

transferTokens();
```

---

## Conclusion

The Fuel Agent SDK provides a robust and user-friendly interface for interacting with the Fuel Node. By leveraging GraphQL, it enables developers to efficiently query and manipulate blockchain data while abstracting away the complexities of direct node interaction.
