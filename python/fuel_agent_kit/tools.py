"""Tool definitions for the Fuel Agent Kit Python version."""

from langchain_core.tools import tool
from pydantic import BaseModel, Field


class TransferInput(BaseModel):
    to: str = Field(description="The wallet address to transfer to")
    amount: str = Field(description="The amount to transfer")
    symbol: str = Field(
        description="The asset symbol to transfer, e.g. USDC, ETH"
    )


class SwapInput(BaseModel):
    amount: str = Field(description="The amount to swap")
    from_symbol: str = Field(
        description="The asset symbol to swap from, e.g. USDC, ETH"
    )
    to_symbol: str = Field(
        description="The asset symbol to swap to, e.g. USDC, ETH"
    )
    slippage: float = Field(
        default=0.01, description="Slippage tolerance (default: 0.01 for 1%)"
    )


class SupplyCollateralInput(BaseModel):
    amount: str = Field(description="The amount to lend")
    symbol: str = Field(
        description="The asset symbol to lend, e.g. USDC, ETH"
    )


class BorrowAssetInput(BaseModel):
    amount: str = Field(description="The amount to borrow")


class AddLiquidityInput(BaseModel):
    amount0: str = Field(description="The amount of the first asset to add")
    asset0_symbol: str = Field(description="The symbol of the first asset")
    asset1_symbol: str = Field(description="The symbol of the second asset")
    slippage: float = Field(
        default=0.01, description="Slippage tolerance (default: 0.01 for 1%)"
    )


class GetOwnBalanceInput(BaseModel):
    symbol: str = Field(
        description="The asset symbol to get the balance of, e.g. USDC, ETH"
    )


class GetBalanceInput(BaseModel):
    wallet_address: str = Field(
        description="The wallet address to get the balance of"
    )
    asset_symbol: str = Field(
        description="The asset symbol to get the balance of, e.g. USDC, ETH"
    )


def create_tools(fuel_agent):
    """Create and return all LangChain tools with injected agent credentials."""

    @tool("fuel_transfer", args_schema=TransferInput)
    def fuel_transfer(to: str, amount: str, symbol: str) -> str:
        """Transfer any verified Fuel asset to another wallet."""
        return fuel_agent.transfer(to=to, amount=amount, symbol=symbol)

    @tool("swap_exact_input", args_schema=SwapInput)
    def swap_exact_input(
        amount: str, from_symbol: str, to_symbol: str, slippage: float = 0.01
    ) -> str:
        """Swap exact input on Mira DEX."""
        return fuel_agent.swap(
            amount=amount,
            from_symbol=from_symbol,
            to_symbol=to_symbol,
            slippage=slippage,
        )

    @tool("supply_collateral", args_schema=SupplyCollateralInput)
    def supply_collateral(amount: str, symbol: str) -> str:
        """Supply collateral on Swaylend."""
        return fuel_agent.supply_collateral(amount=amount, symbol=symbol)

    @tool("borrow_asset", args_schema=BorrowAssetInput)
    def borrow_asset(amount: str) -> str:
        """Borrow asset on Swaylend."""
        return fuel_agent.borrow(amount=amount)

    @tool("add_liquidity", args_schema=AddLiquidityInput)
    def add_liquidity(
        amount0: str,
        asset0_symbol: str,
        asset1_symbol: str,
        slippage: float = 0.01,
    ) -> str:
        """Add liquidity to a Mira pool."""
        return fuel_agent.add_liquidity(
            amount0=amount0,
            asset0_symbol=asset0_symbol,
            asset1_symbol=asset1_symbol,
            slippage=slippage,
        )

    @tool("get_own_balance", args_schema=GetOwnBalanceInput)
    def get_own_balance(symbol: str) -> str:
        """Get the balance of an asset in your wallet."""
        return fuel_agent.get_own_balance(symbol=symbol)

    @tool("get_balance", args_schema=GetBalanceInput)
    def get_balance(wallet_address: str, asset_symbol: str) -> str:
        """Get the balance of an asset for a given wallet address."""
        return fuel_agent.get_balance(
            wallet_address=wallet_address, asset_symbol=asset_symbol
        )

    return [
        fuel_transfer,
        swap_exact_input,
        supply_collateral,
        borrow_asset,
        add_liquidity,
        get_own_balance,
        get_balance,
    ]
