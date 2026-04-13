"""Constants for Fuel Agent Kit."""

DEFAULT_SLIPPAGE = 0.01  # 1%
FUEL_PROVIDER_URL = "https://mainnet.fuel.network/v1/graphql"
VERIFIED_ASSETS_URL = "https://verified-assets.fuel.network/assets.json"
TX_EXPLORER_URL = "https://app.fuel.network/tx/{tx_id}/simple"
SAYLEND_MARKET_CONTRACT_ID = (
    "0x657ab45a6eb98a4893a99fd104347179151e8b3828fd8f2a108cc09770d1ebae"
)
PYTH_CONTRACT_ID = (
    "0x1c86fdd9e0e7bc0d2ae1bf6817ef4834ffa7247655701ee1b031b52a24c523da"
)
PYTH_HERMES_URL = "https://hermes.pyth.network"

SUPPORTED_MODELS = {
    "gpt-4o": "openai",
    "gpt-4o-mini": "openai",
    "claude-3-5-sonnet-latest": "anthropic",
    "claude-3-5-haiku-latest": "anthropic",
    "gemini-1.5-flash": "google",
    "gemini-2.0-flash-exp": "google",
}
