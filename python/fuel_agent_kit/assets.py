"""Asset management utilities for Fuel Agent Kit."""

import httpx
from functools import lru_cache
from dataclasses import dataclass
from typing import Optional

from .constants import VERIFIED_ASSETS_URL


@dataclass
class FuelAsset:
    symbol: str
    asset_id: str
    decimals: int


@lru_cache(maxsize=1)
def get_verified_assets() -> list[dict]:
    """Fetch verified Fuel assets with caching."""
    response = httpx.get(VERIFIED_ASSETS_URL, timeout=30)
    response.raise_for_status()
    return response.json()


def get_fuel_assets() -> list[FuelAsset]:
    """Get all verified Fuel assets with their IDs and decimals."""
    all_assets = get_verified_assets()
    fuel_assets = []
    for asset in all_assets:
        symbol = asset.get("symbol", "")
        for network in asset.get("networks", []):
            if network.get("type") == "fuel" and network.get("chainId") == 0:
                fuel_assets.append(
                    FuelAsset(
                        symbol=symbol,
                        asset_id=network.get("assetId", ""),
                        decimals=network.get("decimals", 9),
                    )
                )
                break
    return fuel_assets


def find_asset(
    symbol: str, assets: Optional[list[FuelAsset]] = None
) -> FuelAsset:
    """Find an asset by its symbol."""
    if assets is None:
        assets = get_fuel_assets()
    for asset in assets:
        if asset.symbol == symbol:
            return asset
    raise ValueError(f"Asset {symbol} not found")


def get_explorer_url(tx_id: str) -> str:
    """Get the explorer URL for a transaction."""
    return f"https://app.fuel.network/tx/{tx_id}/simple"
