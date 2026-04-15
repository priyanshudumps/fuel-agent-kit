"""
Type definitions for Fuel Agent Kit
"""

from typing import TypedDict, Optional, Literal


class SwapExactInputParams(TypedDict):
    amount: str
    from_asset: str
    to_asset: str
    slippage: Optional[float]


class AddLiquidityParams(TypedDict):
    amount0: str
    amount1: str
    asset0: str
    asset1: str


class SupplyCollateralParams(TypedDict):
    amount: str
    asset: str


class BorrowAssetParams(TypedDict):
    amount: str
    asset: str


class TransferParams(TypedDict):
    to: str
    amount: str
    asset: Optional[str]


class GetOwnBalanceParams(TypedDict):
    asset: str


ModelType = Literal["openai", "anthropic", "google"]
