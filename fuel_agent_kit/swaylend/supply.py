"""Swaylend - Supply collateral"""
from typing import Any
from ..types import SupplyCollateralParams

async def supply_collateral(params: SupplyCollateralParams, wallet_private_key: str) -> Any:
    print(f"Supplying {params['amount']} {params['asset']} as collateral")
    return {"status": "success", "tx_hash": "0x..."}
