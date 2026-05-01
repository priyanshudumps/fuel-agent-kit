# Python Integration Guide
Currently, the Fuel Agent Kit is primarily implemented in TypeScript. To interact with this kit using Python, developers have three primary integration paths:

1. **REST API Wrapper:** Deploy the TS SDK as a microservice (e.g., using Express) and call it from Python via `requests`.
2. **CLI Subprocess:** Utilize the `subprocess` module in Python to trigger `npx ts-node` scripts.
3. **Native Rust Bindings:** Leverage the underlying Fuel Rust SDK through PyO3 for high-performance integrations.

Full Python SDK support is on the long-term roadmap.
