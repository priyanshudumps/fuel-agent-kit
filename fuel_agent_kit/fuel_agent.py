"""
Fuel Agent - Main class for interacting with Fuel blockchain
"""

from typing import Optional, Dict, Any
from .types import (
    SwapExactInputParams,
    AddLiquidityParams,
    SupplyCollateralParams,
    BorrowAssetParams,
    TransferParams,
    GetOwnBalanceParams,
    ModelType,
)
from .mira.swap import swap_exact_input
from .mira.add_liquidity import add_liquidity
from .swaylend.supply import supply_collateral
from .swaylend.borrow import borrow_asset
from .transfers.transfer import transfer
from .read.balance import get_own_balance
from .agent import create_agent


class FuelAgentConfig:
    def __init__(
        self,
        wallet_private_key: str,
        model: ModelType = "openai",
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
    def __init__(self, config: FuelAgentConfig):
        if not config.wallet_private_key:
            raise ValueError("Fuel wallet private key is required.")
        
        self.wallet_private_key = config.wallet_private_key
        self.model = config.model
        self.openai_api_key = config.openai_api_key
        self.anthropic_api_key = config.anthropic_api_key
        self.google_gemini_api_key = config.google_gemini_api_key
        
        self.agent_executor = create_agent(
            self,
            self.model,
            self.openai_api_key,
            self.anthropic_api_key,
            self.google_gemini_api_key,
        )
    
    def get_credentials(self) -> Dict[str, str]:
        return {
            "wallet_private_key": self.wallet_private_key,
            "openai_api_key": self.openai_api_key or "",
            "anthropic_api_key": self.anthropic_api_key or "",
            "google_gemini_api_key": self.google_gemini_api_key or "",
        }
    
    async def execute(self, input_text: str) -> Dict[str, Any]:
        response = await self.agent_executor.invoke({"input": input_text})
        return response
    
    async def swap_exact_input(self, params: SwapExactInputParams) -> Any:
        return await swap_exact_input(params, self.wallet_private_key)
    
    async def add_liquidity(self, params: AddLiquidityParams) -> Any:
        return await add_liquidity(params, self.wallet_private_key)
    
    async def supply_collateral(self, params: SupplyCollateralParams) -> Any:
        return await supply_collateral(params, self.wallet_private_key)
    
    async def borrow_asset(self, params: BorrowAssetParams) -> Any:
        return await borrow_asset(params, self.wallet_private_key)
    
    async def transfer(self, params: TransferParams) -> Any:
        return await transfer(params, self.wallet_private_key)
    
    async def get_own_balance(self, params: GetOwnBalanceParams) -> Any:
        return await get_own_balance(params, self.wallet_private_key)
