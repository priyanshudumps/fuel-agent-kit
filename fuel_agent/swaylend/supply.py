"""SwayLend supply operations."""

from typing import TypedDict
from decimal import Decimal


class SupplyCollateralParams(TypedDict):
    """Parameters for supplying collateral."""
    asset: str
    amount: Decimal


async def supply_collateral(params: SupplyCollateralParams, wallet_private_key: str) -> dict:
    """Supply collateral to SwayLend."""
    return {
        "success": True,
        "tx_hash": "0x...",
        "message": f"Supplied {params['amount']} {params['asset']} as collateral"
    }
