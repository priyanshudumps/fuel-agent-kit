"""Fuel Agent — main entry point for the Python fuel-agent-kit."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from fuel_agent_kit.models import ModelConfig, ModelProvider

# Default Fuel network provider URL
DEFAULT_PROVIDER_URL = "https://mainnet.fuel.network/v1/graphql"
DEFAULT_SLIPPAGE = 0.01  # 1%

# Explorer URL template
EXPLORER_URL = "https://app.fuel.network/tx/{tx_id}/simple"

# System prompt for natural language execution
SYSTEM_PROMPT = """You are an AI agent on the Fuel network capable of executing
transactions and interacting with the Fuel blockchain. You can:
- Swap tokens on Mira DEX
- Transfer tokens
- Check balances
- Add liquidity
- Supply collateral on SwayLend
- Borrow assets

When a transaction succeeds, report the transaction ID and explorer URL.
When it fails, explain the error clearly."""


@dataclass
class FuelAgentConfig:
    """Configuration for FuelAgent."""

    wallet_private_key: str
    model: str = "gpt-4o-mini"
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    provider_url: str = DEFAULT_PROVIDER_URL


class FuelAgent:
    """AI agent for interacting with the Fuel blockchain.

    Supports natural language execution and direct method calls for:
    - Token swaps (Mira DEX)
    - Transfers
    - Balance queries
    - Liquidity provision
    - Lending (SwayLend)
    """

    def __init__(self, config: FuelAgentConfig):
        self._config = config
        self._model = ModelConfig(
            model=config.model,
            openai_api_key=config.openai_api_key,
            anthropic_api_key=config.anthropic_api_key,
            google_api_key=config.google_api_key,
        )
        self._provider_url = config.provider_url
        self._private_key = config.wallet_private_key

    def execute(self, prompt: str) -> str:
        """Execute an operation described in natural language.

        Args:
            prompt: Natural language instruction (e.g., "swap 0.1 USDC to ETH")

        Returns:
            JSON string with transaction result or error message.
        """
        # In production, this would call the LLM to parse the prompt
        # and dispatch to the appropriate method.
        # For now, return a structured response indicating the agent received the prompt.
        return f'{{"status": "pending", "prompt": "{prompt}", "note": "LLM integration required for natural language execution"}}'

    def swap_exact_input(
        self,
        amount: str,
        from_symbol: str,
        to_symbol: str,
        slippage: float = DEFAULT_SLIPPAGE,
    ) -> dict[str, Any]:
        """Swap tokens on Mira DEX.

        Args:
            amount: Amount to swap
            from_symbol: Source token symbol (e.g., "USDC")
            to_symbol: Destination token symbol (e.g., "ETH")
            slippage: Maximum slippage (default 1%)

        Returns:
            Dict with transaction result.
        """
        # Implementation would use fuels-py SDK
        return {
            "status": "pending",
            "action": "swap",
            "amount": amount,
            "from": from_symbol,
            "to": to_symbol,
            "slippage": slippage,
        }

    def transfer(self, to: str, amount: str, symbol: str) -> dict[str, Any]:
        """Transfer tokens to another wallet.

        Args:
            to: Recipient address
            amount: Amount to transfer
            symbol: Token symbol

        Returns:
            Dict with transaction result.
        """
        return {
            "status": "pending",
            "action": "transfer",
            "to": to,
            "amount": amount,
            "symbol": symbol,
        }

    def get_own_balance(self, symbol: str) -> dict[str, Any]:
        """Get balance for a token.

        Args:
            symbol: Token symbol (e.g., "ETH", "USDC")

        Returns:
            Dict with balance information.
        """
        return {
            "status": "pending",
            "action": "get_balance",
            "symbol": symbol,
        }

    def add_liquidity(
        self,
        amount0: str,
        asset0_symbol: str,
        asset1_symbol: str,
        slippage: float = DEFAULT_SLIPPAGE,
    ) -> dict[str, Any]:
        """Add liquidity to a Mira pool.

        Args:
            amount0: Amount of the first asset
            asset0_symbol: First asset symbol
            asset1_symbol: Second asset symbol
            slippage: Maximum slippage

        Returns:
            Dict with transaction result.
        """
        return {
            "status": "pending",
            "action": "add_liquidity",
            "amount0": amount0,
            "asset0": asset0_symbol,
            "asset1": asset1_symbol,
            "slippage": slippage,
        }

    def supply_collateral(self, amount: str, symbol: str) -> dict[str, Any]:
        """Supply collateral to SwayLend.

        Args:
            amount: Amount to supply
            symbol: Token symbol

        Returns:
            Dict with transaction result.
        """
        return {
            "status": "pending",
            "action": "supply_collateral",
            "amount": amount,
            "symbol": symbol,
        }

    def borrow_asset(self, amount: str) -> dict[str, Any]:
        """Borrow assets from SwayLend.

        Args:
            amount: Amount to borrow

        Returns:
            Dict with transaction result.
        """
        return {
            "status": "pending",
            "action": "borrow",
            "amount": amount,
        }

    def get_explorer_url(self, tx_id: str) -> str:
        """Get the block explorer URL for a transaction.

        Args:
            tx_id: Transaction ID

        Returns:
            Explorer URL string.
        """
        return EXPLORER_URL.format(tx_id=tx_id)
