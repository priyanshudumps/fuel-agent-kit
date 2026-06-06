from typing import Optional, Dict, Any
from .agent import create_agent
from .mira.swap import swap_exact_input
from .mira.add_liquidity import add_liquidity
from .swaylend.borrow import borrow_asset
from .swaylend.supply import supply_collateral
from .transfers.transfers import transfer as wallet_transfer
from .read.balance import get_own_balance

class FuelAgentConfig:
    def __init__(self, wallet_private_key: str, model: str, open_ai_api_key: Optional[str] = None, anthropic_api_key: Optional[str] = None, google_gemini_api_key: Optional[str] = None):
        self.wallet_private_key = wallet_private_key
        self.model = model
        self.open_ai_api_key = open_ai_api_key
        self.anthropic_api_key = anthropic_api_key
        self.google_gemini_api_key = google_gemini_api_key

class FuelAgent:
    def __init__(self, config: FuelAgentConfig):
        self.wallet_private_key = config.wallet_private_key
        self.model = config.model
        self.open_ai_api_key = config.open_ai_api_key
        self.anthropic_api_key = config.anthropic_api_key
        self.google_gemini_api_key = config.google_gemini_api_key

        if not self.wallet_private_key:
            raise ValueError("Fuel wallet private key is required.")

        self.agent_executor = create_agent(
            fuel_agent=self,
            model_name=self.model,
            openai_api_key=self.open_ai_api_key,
            anthropic_api_key=self.anthropic_api_key,
            google_gemini_api_key=self.google_gemini_api_key
        )

    def get_credentials(self) -> Dict[str, str]:
        return {
            "walletPrivateKey": self.wallet_private_key,
            "openAiApiKey": self.open_ai_api_key or "",
            "anthropicApiKey": self.anthropic_api_key or "",
            "googleGeminiApiKey": self.google_gemini_api_key or ""
        }
        
    def get_tools(self) -> list:
        from .tools import create_tools
        return create_tools(self)

    async def execute(self, input_str: str) -> Any:
        return await self.agent_executor.ainvoke({"input": input_str})

    async def swap_exact_input(self, params: dict):
        return await swap_exact_input(params, self.wallet_private_key)

    async def transfer(self, params: dict):
        return await wallet_transfer(params, self.wallet_private_key)

    async def supply_collateral(self, params: dict):
        return await supply_collateral(params, self.wallet_private_key)

    async def borrow_asset(self, params: dict):
        return await borrow_asset(params, self.wallet_private_key)

    async def add_liquidity(self, params: dict):
        return await add_liquidity(params, self.wallet_private_key)

    async def get_own_balance(self, params: dict):
        return await get_own_balance(params, self.wallet_private_key)
