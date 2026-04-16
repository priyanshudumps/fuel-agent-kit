# Fuel Agent Kit

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/fuel-agent-kit.svg)](https://www.npmjs.com/package/fuel-agent-kit)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)

一个用于构建 Fuel 区块链代理的完整工具包。

## 📖 目录

- [简介](#简介)
- [特性](#特性)
- [安装](#安装)
- [快速开始](#快速开始)
- [使用指南](#使用指南)
- [API 文档](#api-文档)
- [示例](#示例)
- [配置](#配置)
- [故障排除](#故障排除)
- [贡献](#贡献)
- [许可证](#许可证)

## ✨ 简介

Fuel Agent Kit 是一个强大的 TypeScript 工具包，用于在 Fuel 网络上构建和部署去中心化代理。它提供了完整的开发体验，从项目设置到部署的全流程支持。

## 🚀 特性

- 🚀 **快速部署** - 一键部署 Fuel 代理
- 🔧 **可配置** - 灵活配置智能合约参数
- 📊 **内置监控** - 实时监控代理状态和日志
- 🔐 **安全密钥管理** - 支持环境变量和密钥加密
- 📦 **TypeScript 支持** - 完整的类型定义
- 🧪 **测试工具** - 内置测试框架和 Mock 数据
- 📚 **详细文档** - 完整的 API 文档和示例

## 📦 安装

### npm 安装

```bash
npm install fuel-agent-kit
```

### yarn 安装

```bash
yarn add fuel-agent-kit
```

### pnpm 安装

```bash
pnpm add fuel-agent-kit
```

## 🚀 快速开始

### 1. 初始化项目

```bash
npx fuel-agent-kit init my-agent
cd my-agent
```

### 2. 配置环境变量

创建 `.env` 文件：

```bash
FUEL_ENDPOINT=https://mainnet.fuel.network
FUEL_PRIVATE_KEY=your_private_key_here
LOG_LEVEL=info
```

### 3. 创建代理

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  endpoint: process.env.FUEL_ENDPOINT,
  privateKey: process.env.FUEL_PRIVATE_KEY
});

await agent.start();
console.log('Agent started!');
```

### 4. 运行代理

```bash
npm start
```

## 📚 使用指南

### 基础用法

#### 创建代理实例

```typescript
import { FuelAgent } from 'fuel-agent-kit';

const agent = new FuelAgent({
  endpoint: 'https://mainnet.fuel.network',
  privateKey: process.env.FUEL_PRIVATE_KEY,
  maxRetries: 5,
  timeout: 30000,
  logging: true
});
```

#### 启动和停止

```typescript
// 启动代理
await agent.start();

// 停止代理
await agent.stop();

// 检查运行状态
const isRunning = agent.isRunning();
```

#### 查询状态

```typescript
const status = await agent.getStatus();
console.log(status);
// 输出:
// {
//   running: true,
//   uptime: 3600,
//   transactions: 42,
//   lastBlock: 1234567
// }
```

## 📖 API 文档

### FuelAgent 类

主代理类，提供所有核心功能。

#### 构造函数

```typescript
constructor(config: FuelAgentConfig)
```

**参数 `FuelAgentConfig`：**

| 属性 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `endpoint` | `string` | ✅ | - | Fuel 节点 RPC 端点 |
| `privateKey` | `string` | ✅ | - | 私钥（建议使用环境变量） |
| `maxRetries` | `number` | ❌ | `3` | 最大重试次数 |
| `timeout` | `number` | ❌ | `30000` | 请求超时（毫秒） |
| `logging` | `boolean` | ❌ | `true` | 启用日志 |
| `logLevel` | `string` | ❌ | `'info'` | 日志级别 |

#### 方法

##### `start()`

启动代理。

```typescript
await agent.start();
```

##### `stop()`

停止代理。

```typescript
await agent.stop();
```

##### `getStatus(): Promise<AgentStatus>`

获取代理状态。

```typescript
const status = await agent.getStatus();
```

**返回 `AgentStatus`：**

```typescript
interface AgentStatus {
  running: boolean;
  uptime: number;
  transactions: number;
  lastBlock: number;
  errors: number;
}
```

##### `getBalance(address: string): Promise<bigint>`

查询指定地址的余额。

```typescript
const balance = await agent.getBalance('0x...');
```

##### `transfer(to: string, amount: bigint): Promise<string>`

转账到指定地址。

```typescript
const txHash = await agent.transfer('0x...', 1000000n);
```

##### `getTransaction(txHash: string): Promise<Transaction>`

查询交易详情。

```typescript
const tx = await agent.getTransaction('0x...');
```

### 工具函数

#### `generateWallet()`

生成新钱包。

```typescript
import { generateWallet } from 'fuel-agent-kit';

const wallet = generateWallet();
console.log(wallet.address);
console.log(wallet.privateKey);
```

#### `validateAddress(address: string): boolean`

验证地址格式。

```typescript
import { validateAddress } from 'fuel-agent-kit';

const isValid = validateAddress('0x...');
```

## 💡 示例

### 示例 1：基本代理

```typescript
import { FuelAgent } from 'fuel-agent-kit';

async function main() {
  const agent = new FuelAgent({
    endpoint: 'https://mainnet.fuel.network',
    privateKey: process.env.FUEL_PRIVATE_KEY
  });

  await agent.start();
  
  const status = await agent.getStatus();
  console.log('Agent status:', status);
  
  await agent.stop();
}

main().catch(console.error);
```

### 示例 2：批量转账

```typescript
import { FuelAgent } from 'fuel-agent-kit';

async function batchTransfer() {
  const agent = new FuelAgent({
    endpoint: 'https://mainnet.fuel.network',
    privateKey: process.env.FUEL_PRIVATE_KEY
  });

  await agent.start();

  const recipients = [
    { address: '0x...', amount: 1000000n },
    { address: '0x...', amount: 2000000n },
    { address: '0x...', amount: 3000000n }
  ];

  for (const recipient of recipients) {
    const txHash = await agent.transfer(recipient.address, recipient.amount);
    console.log(`Transferred to ${recipient.address}: ${txHash}`);
  }

  await agent.stop();
}

batchTransfer().catch(console.error);
```

### 示例 3：监听交易

```typescript
import { FuelAgent } from 'fuel-agent-kit';

async function monitorTransactions() {
  const agent = new FuelAgent({
    endpoint: 'https://mainnet.fuel.network',
    privateKey: process.env.FUEL_PRIVATE_KEY,
    logging: true
  });

  await agent.start();

  agent.on('transaction', (tx) => {
    console.log('New transaction:', tx);
  });

  agent.on('error', (error) => {
    console.error('Error:', error);
  });

  // 保持运行
  await new Promise(() => {});
}

monitorTransactions().catch(console.error);
```

## ⚙️ 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `FUEL_ENDPOINT` | Fuel 节点 RPC 端点 | - |
| `FUEL_PRIVATE_KEY` | 私钥 | - |
| `LOG_LEVEL` | 日志级别 | `info` |
| `MAX_RETRIES` | 最大重试次数 | `3` |
| `TIMEOUT` | 请求超时（毫秒） | `30000` |

### 配置文件

创建 `fuel.config.json`：

```json
{
  "endpoint": "https://mainnet.fuel.network",
  "maxRetries": 5,
  "timeout": 30000,
  "logging": true,
  "logLevel": "info"
}
```

## 🔧 故障排除

### 常见问题

#### Q: 连接超时错误

**A:** 检查网络连接和节点端点是否正确。

```bash
# 测试端点连通性
curl -X POST https://mainnet.fuel.network \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

#### Q: 签名失败

**A:** 确认私钥格式正确，建议使用环境变量。

```bash
# 正确的私钥格式（64 字符十六进制）
export FUEL_PRIVATE_KEY=0x1234567890abcdef...
```

#### Q: 余额不足

**A:** 确保账户有足够的 FUEL 代币。

```typescript
const balance = await agent.getBalance(agent.address);
console.log('Balance:', balance.toString());
```

### 日志级别

设置不同的日志级别：

```typescript
const agent = new FuelAgent({
  // ...
  logLevel: 'debug' // 'error' | 'warn' | 'info' | 'debug'
});
```

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

### 开发设置

```bash
# 克隆仓库
git clone https://github.com/priyanshudumps/fuel-agent-kit.git
cd fuel-agent-kit

# 安装依赖
npm install

# 运行测试
npm test

# 构建
npm run build
```

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件

---

**维护者：** [@priyanshudumps](https://github.com/priyanshudumps)  
**版本：** 1.0.0  
**最后更新：** 2026-04-16
