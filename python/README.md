# Fuel Agent Kit (Python)

This directory contains the Python implementation of the Fuel Agent Kit.

## Usage

```python
from fuel_agent_kit import FuelAgent

agent = FuelAgent(
    private_key="your_private_key",
    provider_url="https://mainnet.fuel.network"
)

agent.transfer("0x...", 10, "0x...")
```
