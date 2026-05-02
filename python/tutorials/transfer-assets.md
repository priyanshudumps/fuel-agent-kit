
# Transferring Assets on the Fuel Network with Python

This tutorial provides a step-by-step guide for a Python developer to transfer assets on the Fuel blockchain using the Fuel Agent Kit.

## Prerequisites

Before you begin, ensure you have:
- Node.js and npm installed
- Python 3.7+ installed
- Basic understanding of blockchain concepts

## Setup

1. **Install the Fuel Agent Kit**

   Clone the repository and install the package:

   ```bash
   git clone https://github.com/priyanshudumps/fuel-agent-kit.git
   cd fuel-agent-kit
   npm install
   ```

2. **Install Python dependencies**

   ```bash
   pip install fuel-py
   ```

## Understanding the Fuel Network

The Fuel network is a blockchain platform that supports asset transfers. Assets can be tokens, NFTs, or any other digital property.

## Step 1: Initialize the Fuel Client

First, create a Python script to initialize the Fuel client:

```python
from fuel_python.client import Client
from fuel_python.core import Contract

# Initialize the client
client = Client(
    url="https://api.testnet.fuel.network/graphql",
    wallet_path="path/to/your/wallet.json"
)
```

## Step 2: Load Your Wallet

Load your wallet credentials to sign transactions:

```python
wallet = client.wallet.load("your_wallet_name")
```

## Step 3: Get Asset Information

Before transferring, you need to know the asset ID you want to transfer:

```python
asset_id = "YOUR_ASSET_ID"  # Replace with your asset ID
asset = client.get_asset(asset_id)
print(f"Asset name: {asset.name}, Symbol: {asset.symbol}")
```

## Step 4: Prepare the Transfer Transaction

Create a transfer transaction object:

```python
from fuel_python.core import Transaction

# Prepare the transfer transaction
transfer_tx = Transaction(
    amount=1000000,  # Amount to transfer (in smallest units)
    asset_id=asset_id,
    to="RECIPIENT_ADDRESS",  # Replace with recipient address
    from_=wallet.address
)
```

## Step 5: Sign and Broadcast the Transaction

Sign the transaction with your wallet and broadcast it to the network:

```python
# Sign the transaction
signed_tx = wallet.sign(transfer_tx)

# Broadcast the transaction
tx_hash = client.broadcast(signed_tx)
print(f"Transaction hash: {tx_hash}")
```

## Step 6: Verify the Transaction

Check the transaction status to confirm it was successful:

```python
tx = client.get_transaction(tx_hash)
print(f"Transaction status: {tx.status}")
print(f"Transaction confirmed: {tx.confirmed}")
```

## Complete Example

Here's a complete example combining all steps:

```python
from fuel_python.client import Client
from fuel_python.core import Transaction

# Initialize client
client = Client(
    url="https://api.testnet.fuel-network.com/graphql",
    wallet_path="path/to/wallet.json"
)

# Load wallet
wallet = client.wallet.load("my_wallet")

# Asset information
asset_id = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
recipient_address = "0x9876543210fedcba09876543210fedcba09876543210fedcba09876543210fedcba"

# Prepare transfer
transfer_tx = Transaction(
    amount=1000000,
    asset_id=asset_id,
    to=recipient_address,
    from_=wallet.address
)

# Sign and broadcast
signed_tx = wallet.sign(transfer_tx)
tx_hash = client.broadcast(signed_tx)

# Verify
tx = client.get_transaction(tx_hash)
print(f"Transfer successful: {tx.confirmed}")
```

## Important Notes

1. **Testnet vs Mainnet**: Use testnet for development and testing.
2. **Gas Fees**: Ensure you have enough fuel to cover gas fees.
3. **Security**: Never expose your private keys or wallet files.
4. **Error Handling**: Implement proper error handling for production use.

## Next Steps

- Explore the [Fuel Agent Kit documentation](https://docs.fuel.network)
- Learn about [Fuel Scripts](https://docs.fuel.network/fuel-scripts)
- Experiment with different asset types and transfer scenarios
