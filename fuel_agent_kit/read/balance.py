"""Balance query"""
from typing import Any
from ..types import GetOwnBalanceParams

async def get_own_balance(params: GetOwnBalanceParams, wallet_private_key: str) -> Any:
    print(f"Getting balance for {params['asset']}")
    return {"balance": "100.0", "asset": params['asset']}
