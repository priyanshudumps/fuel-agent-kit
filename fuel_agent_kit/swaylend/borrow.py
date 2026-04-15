"""Swaylend - Borrow asset"""
from typing import Any
from ..types import BorrowAssetParams

async def borrow_asset(params: BorrowAssetParams, wallet_private_key: str) -> Any:
    print(f"Borrowing {params['amount']} {params['asset']}")
    return {"status": "success", "tx_hash": "0x..."}
