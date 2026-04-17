"""SwayLend borrow operations."""

from typing import TypedDict
from decimal import Decimal


class BorrowAssetParams(TypedDict):
    """Parameters for borrowing assets."""
    asset: str
    amount: Decimal


async def borrow_asset(params: BorrowAssetParams, wallet_private_key: str) -> dict:
    """Borrow assets from SwayLend."""
    return {
        "success": True,
        "tx_hash": "0x...",
        "message": f"Borrowed {params['amount']} {params['asset']}"
    }
