"""Wallet transfers"""
from typing import Any
from ..types import TransferParams

async def transfer(params: TransferParams, wallet_private_key: str) -> Any:
    asset = params.get('asset', 'ETH')
    print(f"Transferring {params['amount']} {asset} to {params['to']}")
    return {"status": "success", "tx_hash": "0x..."}
