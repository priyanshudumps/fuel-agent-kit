from pydantic import BaseModel, Field
from typing import Optional, Callable, Any, Awaitable
from langchain.tools import StructuredTool

# Import functions
from .mira.swap import swap_exact_input
from .transfers.transfers import transfer
from .swaylend.supply import supply_collateral
from .swaylend.borrow import borrow_asset
from .mira.add_liquidity import add_liquidity
from .read.balance import get_balance, get_own_balance

class TransferSchema(BaseModel):
    to: str = Field(description="The wallet address to transfer to")
    amount: str = Field(description="The amount to transfer")
    symbol: str = Field(description="The asset symbol to transfer. eg. USDC, ETH")

class SwapSchema(BaseModel):
    amount: str = Field(description="The amount to swap")
    fromSymbol: str = Field(description="The asset symbol to swap from. eg. USDC, ETH")
    toSymbol: str = Field(description="The asset symbol to swap to. eg. USDC, ETH")
    slippage: Optional[float] = Field(default=0.01, description="Slippage tolerance (default: 0.01 for 1%)")

class SupplyCollateralSchema(BaseModel):
    amount: str = Field(description="The amount to lend")
    symbol: str = Field(description="The asset symbol to lend. eg. USDC, ETH")

class BorrowAssetSchema(BaseModel):
    amount: str = Field(description="The amount to borrow")

class AddLiquiditySchema(BaseModel):
    amount0: str = Field(description="The amount of the first asset to add")
    asset0Symbol: str = Field(description="The symbol of the first asset")
    asset1Symbol: str = Field(description="The symbol of the second asset")
    slippage: Optional[float] = Field(default=0.01, description="Slippage tolerance (default: 0.01 for 1%)")

class GetOwnBalanceSchema(BaseModel):
    symbol: str = Field(description="The asset symbol to get the balance of. eg. USDC, ETH")

class GetBalanceSchema(BaseModel):
    walletAddress: str = Field(description="The wallet address to get the balance of")
    assetSymbol: str = Field(description="The asset symbol to get the balance of. eg. USDC, ETH")

def with_wallet_key(func: Callable, agent: Any) -> Callable:
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs, private_key=agent.get_credentials().get("walletPrivateKey"))
    return wrapper

def create_tools(agent: Any):
    return [
        StructuredTool.from_function(
            coroutine=with_wallet_key(transfer, agent),
            name="fuel_transfer",
            description="Transfer any verified Fuel asset to another wallet",
            args_schema=TransferSchema
        ),
        StructuredTool.from_function(
            coroutine=with_wallet_key(swap_exact_input, agent),
            name="swap_exact_input",
            description="Swap exact input on Mira",
            args_schema=SwapSchema
        ),
        StructuredTool.from_function(
            coroutine=with_wallet_key(supply_collateral, agent),
            name="supply_collateral",
            description="Supply collateral on swaylend",
            args_schema=SupplyCollateralSchema
        ),
        StructuredTool.from_function(
            coroutine=with_wallet_key(borrow_asset, agent),
            name="borrow_asset",
            description="Borrow asset on swaylend",
            args_schema=BorrowAssetSchema
        ),
        StructuredTool.from_function(
            coroutine=with_wallet_key(add_liquidity, agent),
            name="add_liquidity",
            description="Add liquidity to a Mira pool",
            args_schema=AddLiquiditySchema
        ),
        StructuredTool.from_function(
            coroutine=with_wallet_key(get_own_balance, agent),
            name="get_own_balance",
            description="Get the balance of an asset in your wallet",
            args_schema=GetOwnBalanceSchema
        ),
        StructuredTool.from_function(
            coroutine=get_balance,
            name="get_balance",
            description="Get the balance of an asset for a given wallet address",
            args_schema=GetBalanceSchema
        )
    ]
