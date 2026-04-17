"""Main Fuel Agent class."""

from typing import Optional, Dict, Any
from decimal import Decimal

from .types import ModelType
from .mira import swap_exact_input, add_liquidity, SwapExactInputParams, AddLiquidityParams
from .swaylend import borrow_asset, supply_collateral, BorrowAssetParams, SupplyCollateralParams
from .transfers import transfer, TransferParams
from .read import get_own_balance, GetOwnBalanceParams
from .agent import create_agent


class FuelAgentConfig:
    """Configuration for FuelAgent."""
    
    def __init__(
        self,
        wallet_private_key: str,
        model: ModelType = "gpt-4",
        openai_api_key: Optional[str] = None,
        anthropic_api_key: Optional[str] = None,
        google_gemini_api_key: Optional[str] = None,
    ):
        self.wallet_private_key = wallet_private_key
        self.model = model
        self.openai_api_key = openai_api_key
        self.anthropic_api_key = anthropic_api_key
        self.google_gemini_api_key = google_gemini_api_key


class FuelAgent:
    """
    Main agent for interacting with the Fuel blockchain.
    
    This class provides a high-level interface for:
    - Wallet management
    - Token swaps via Mira DEX
    - Lending operations via SwayLend
    - Token transfers
    - AI-powered natural language interactions
    
    Example:
        >>> agent = FuelAgent(
        ...     wallet_private_key="your-key",
        ...     model="gpt-4",
        ...     openai_api_key="your-api-key"
        ... )
        >>> response = await agent.execute("Swap 100 USDC for ETH")
    """
    
    def __init__(self, config: FuelAgentConfig):
        """
        Initialize the FuelAgent.
        
        Args:
            config: Configuration object containing wallet and API keys
            
        Raises:
            ValueError: If wallet_private_key is not provided
        """
        self._wallet_private_key = config.wallet_private_key
        self._model = config.model
        self._openai_api_key = config.openai_api_key
        self._anthropic_api_key = config.anthropic_api_key
        self._google_gemini_api_key = config.google_gemini_api_key
        
        if not self._wallet_private_key:
            raise ValueError("Fuel wallet private key is required.")
        
        # Initialize AI agent executor
        self._agent_executor = create_agent(
            self,
            self._model,
            self._openai_api_key,
            self._anthropic_api_key,
            self._google_gemini_api_key,
        )
    
    def get_credentials(self) -> Dict[str, str]:
        """
        Get agent credentials (without exposing private key).
        
        Returns:
            Dictionary with credential info
        """
        return {
            "model": self._model,
            "has_openai": bool(self._openai_api_key),
            "has_anthropic": bool(self._anthropic_api_key),
            "has_google": bool(self._google_gemini_api_key),
        }
    
    async def execute(self, input_text: str) -> Dict[str, Any]:
        """
        Execute a natural language command.
        
        Args:
            input_text: Natural language instruction
            
        Returns:
            Agent response with execution result
        """
        response = await self._agent_executor.ainvoke({
            "input": input_text,
        })
        return response
    
    async def swap_exact_input(
        self,
        from_token: str,
        to_token: str,
        amount: Decimal,
        min_output: Optional[Decimal] = None,
    ) -> Dict[str, Any]:
        """
        Swap exact amount of input tokens.
        
        Args:
            from_token: Token to swap from
            to_token: Token to swap to
            amount: Amount to swap
            min_output: Minimum output amount (slippage protection)
            
        Returns:
            Transaction result
        """
        params = SwapExactInputParams(
            from_token=from_token,
            to_token=to_token,
            amount=amount,
            min_output=min_output or Decimal("0"),
        )
        return await swap_exact_input(params, self._wallet_private_key)
    
    async def transfer(
        self,
        to_address: str,
        token: str,
        amount: Decimal,
    ) -> Dict[str, Any]:
        """
        Transfer tokens to an address.
        
        Args:
            to_address: Recipient address
            token: Token to transfer
            amount: Amount to transfer
            
        Returns:
            Transaction result
        """
        params = TransferParams(
            to_address=to_address,
            token=token,
            amount=amount,
        )
        return await transfer(params, self._wallet_private_key)
    
    async def supply_collateral(
        self,
        asset: str,
        amount: Decimal,
    ) -> Dict[str, Any]:
        """
        Supply collateral to SwayLend.
        
        Args:
            asset: Asset to supply
            amount: Amount to supply
            
        Returns:
            Transaction result
        """
        params = SupplyCollateralParams(
            asset=asset,
            amount=amount,
        )
        return await supply_collateral(params, self._wallet_private_key)
    
    async def borrow_asset(
        self,
        asset: str,
        amount: Decimal,
    ) -> Dict[str, Any]:
        """
        Borrow assets from SwayLend.
        
        Args:
            asset: Asset to borrow
            amount: Amount to borrow
            
        Returns:
            Transaction result
        """
        params = BorrowAssetParams(
            asset=asset,
            amount=amount,
        )
        return await borrow_asset(params, self._wallet_private_key)
    
    async def get_balance(self, token: str) -> Dict[str, Any]:
        """
        Get wallet balance for a token.
        
        Args:
            token: Token to check balance for
            
        Returns:
            Balance information
        """
        params = GetOwnBalanceParams(token=token)
        return await get_own_balance(params, self._wallet_private_key)
