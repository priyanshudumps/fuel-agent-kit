
# Running a Fuel Node Guide

This guide provides a step-by-step walkthrough for developers to run a local Fuel node using either Docker or the Fuel toolchain (`fuel-core`).

---

## Prerequisites

Before starting, ensure you have the following installed:

- **Docker** (for Docker-based setup)
- **Rust** (for Fuel toolchain setup)
- **Git** (for cloning repositories)

---

## Option 1: Running a Fuel Node with Docker

### Step 1: Pull the Fuel Docker Image

```bash
docker pull fuel-labs/fuel-node:latest
```

### Step 2: Run a Fuel Node Container

```bash
docker run -d \
  --name fuel-node \
  -p 4000:4000 \
  -p 4001:4001 \
  -v fuel-node-data:/data \
  fuel-labs/fuel-node:latest
```

### Step 3: Verify the Node is Running

Check the logs to ensure the node is running correctly:

```bash
docker logs fuel-node
```

### Step 4: Interact with the Node

You can interact with the node using the `fuel-core` CLI:

```bash
docker exec -it fuel-node fuel-core
```

---

## Option 2: Running a Fuel Node with Fuel Toolchain

### Step 1: Install Rust and Cargo

Ensure you have Rust and Cargo installed. If not, follow the [official Rust installation guide](https://www.rust-lang.org/tools/install).

### Step 2: Clone the Fuel Repository

```bash
git clone https://github.com/FuelLabs/fuel-core.git
cd fuel-core
```

### Step 3: Build and Run the Fuel Node

```bash
cargo build --release
./target/release/fuel-core --dev
```

### Step 4: Verify the Node is Running

Check the logs to ensure the node is running:

```bash
tail -f logs/dev.log
```

---

## Connecting to the Node

Once your node is running, you can connect to it using the following endpoints:

- **RPC Endpoint:** `http://localhost:4000`
- **WebSocket Endpoint:** `ws://localhost:4001`

---

## Next Steps

- Explore the [Fuel Documentation](https://docs.fuel.sh) for more advanced usage.
- Join the [Fuel Community](https://discord.gg/fuel) for support and discussions.
