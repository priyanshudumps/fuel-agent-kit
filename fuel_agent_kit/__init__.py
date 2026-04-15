"""
Fuel Agent Kit - Python Version

An AI agent for interacting with the Fuel blockchain.
"""

from .fuel_agent import FuelAgent, FuelAgentConfig
from .types import (
    SwapExactInputParams,
    AddLiquidityParams,
    SupplyCollateralParams,
    BorrowAssetParams,
    TransferParams,
    GetOwnBalanceParams,
)

__version__ = "0.1.0"
__all__ = [
    "FuelAgent",
    "FuelAgentConfig",
    "SwapExactInputParams",
    "AddLiquidityParams",
    "SupplyCollateralParams",
    "BorrowAssetParams",
    "TransferParams",
    "GetOwnBalanceParams",
]
