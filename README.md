# Fuel Agent Kit

Fuel Agent Kit 是一个用于 Fuel 区块链网络的 AI 代理工具包。它提供了一套完整的工具和接口，让 AI 代理能够轻松地与 Fuel 网络交互。

## ✨ 特性

- 🤖 **AI 友好**: 专为 AI 代理设计，提供简洁的 API 接口
- ⚡ **高性能**: 基于 Fuel 网络的高性能区块链交互
- 🔧 **易于集成**: 简单的安装和配置流程
- 📦 **模块化**: 灵活的模块设计，按需使用

## 📦 安装

### 环境要求

- Node.js ≥ 18.0.0
- npm ≥ 9.0.0

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/priyanshudumps/fuel-agent-kit.git

# 进入项目目录
cd fuel-agent-kit

# 安装依赖
npm install

# 构建项目
npm run build
```

## 🚀 快速开始

### 基本用法

```typescript
import { FuelAgentKit } from 'fuel-agent-kit';

// 初始化 agent kit
const agent = new FuelAgentKit({
  providerUrl: 'https://testnet.fuel.network/v1/graphql',
  privateKey: process.env.PRIVATE_KEY,
});

// 检查账户余额
const balance = await agent.getBalance();
console.log(`Balance: ${balance} ETH`);

// 发送交易
const tx = await agent.send({
  to: 'fuel1...',
  amount: '0.1',
  assetId: '0x...',
});

console.log(`Transaction hash: ${tx.id}`);
```

### 环境变量配置

创建 `.env` 文件：

```env
PRIVATE_KEY=your_private_key_here
PROVIDER_URL=https://testnet.fuel.network/v1/graphql
```

## 📚 API 参考

### FuelAgentKit 类

#### 构造函数

```typescript
new FuelAgentKit(config: AgentConfig)
```

**参数：**
- `config.providerUrl`: Fuel 网络节点 URL
- `config.privateKey`: 钱包私钥

#### 方法

##### `getBalance(assetId?: string): Promise<string>`

获取账户余额。

**参数：**
- `assetId` (可选): 资产 ID，默认为 ETH

**返回：**
- 余额字符串

##### `send(params: SendParams): Promise<Transaction>`

发送交易。

**参数：**
- `params.to`: 接收地址
- `params.amount`: 发送金额
- `params.assetId`: 资产 ID

**返回：**
- 交易对象

##### `callContract(params: ContractCallParams): Promise<Transaction>`

调用智能合约。

**参数：**
- `params.contractId`: 合约 ID
- `params.method`: 合约方法名
- `params.args`: 方法参数

## 🧪 测试

```bash
# 运行单元测试
npm test

# 运行测试并生成覆盖率报告
npm run test:coverage
```

## 📝 示例

### 示例 1: 查询账户信息

```typescript
import { FuelAgentKit } from 'fuel-agent-kit';

const agent = new FuelAgentKit({
  providerUrl: 'https://testnet.fuel.network/v1/graphql',
  privateKey: process.env.PRIVATE_KEY,
});

async function getAccountInfo() {
  const address = agent.getAddress();
  const balance = await agent.getBalance();

  console.log('Address:', address);
  console.log('Balance:', balance);
}

getAccountInfo();
```

### 示例 2: 与智能合约交互

```typescript
import { FuelAgentKit } from 'fuel-agent-kit';

const agent = new FuelAgentKit({
  providerUrl: 'https://testnet.fuel.network/v1/graphql',
  privateKey: process.env.PRIVATE_KEY,
});

async function interactWithContract() {
  const result = await agent.callContract({
    contractId: '0x...',
    method: 'increment_counter',
    args: [],
  });

  console.log('Transaction:', result.id);
}

interactWithContract();
```

## 🔐 安全提示

⚠️ **重要**:
- 永远不要将私钥硬编码在代码中
- 使用环境变量或安全的密钥管理系统
- 在主网使用前先在测试网测试
- 定期轮换私钥

## 🌐 网络支持

| 网络 | URL | 状态 |
|------|-----|------|
| Testnet | https://testnet.fuel.network/v1/graphql | ✅ 可用 |
| Mainnet | https://mainnet.fuel.network/v1/graphql | ✅ 可用 |

## 🤝 贡献

我们欢迎所有形式的贡献！请查看我们的 [贡献指南](./CONTRIBUTING.md)。

### 提交 Issue

如果你发现了 bug 或有功能请求，请在 GitHub Issues 中提交。

### 提交 PR

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目使用 MIT 许可证 - 查看 [LICENSE](./LICENSE) 文件了解详情。

## 🔗 相关链接

- [Fuel 官方文档](https://docs.fuel.network/)
- [Fuel 区块链](https://fuel.network/)
- [Fuel 论坛](https://forum.fuel.network/)

## 💬 支持

如果你需要帮助或有任何问题，请：

1. 查看我们的 [文档](https://docs.fuel.network/)
2. 在 [GitHub Issues](https://github.com/priyanshudumps/fuel-agent-kit/issues) 中提问
3. 加入 [Fuel Discord](https://discord.gg/fuelnetwork)

---

**Built with ❤️ by the Fuel community**
