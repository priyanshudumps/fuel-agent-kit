import requests
import time
from typing import List, Dict, Any, Optional

class CacheData:
    def __init__(self, timestamp: float, data: List[Dict[str, Any]]):
        self.timestamp = timestamp
        self.data = data

assets_cache: Optional[CacheData] = None
CACHE_TTL = 3600  # 1 hour in seconds

def get_verified_assets() -> List[Dict[str, Any]]:
    global assets_cache
    if assets_cache and (time.time() - assets_cache.timestamp) < CACHE_TTL:
        return assets_cache.data
    
    response = requests.get('https://verified-assets.fuel.network/assets.json')
    response.raise_for_status()
    all_assets = response.json()
    
    assets_cache = CacheData(timestamp=time.time(), data=all_assets)
    return all_assets

def get_asset_id_and_decimals(symbol: str, assets: List[Dict[str, Any]]) -> Dict[str, Any]:
    asset = next((a for a in assets if a.get("symbol") == symbol), None)
    if not asset:
        raise ValueError(f"Asset {symbol} not found")
        
    networks = asset.get("networks", [])
    # In python, we can just look for type 'fuel' and chainId 0
    fuel_network = next((n for n in networks if n.get("type") == "fuel" and n.get("chainId") == 0), None)
    
    if not fuel_network:
        raise ValueError(f"Asset {symbol} not found on Fuel")
        
    return {
        "assetId": fuel_network.get("assetId"),
        "decimals": fuel_network.get("decimals")
    }

def get_all_verified_symbols(assets: List[Dict[str, Any]]) -> List[str]:
    return [asset.get("symbol") for asset in assets if "symbol" in asset]

def get_all_verified_fuel_assets() -> List[Dict[str, Any]]:
    all_assets = get_verified_assets()
    symbols = get_all_verified_symbols(all_assets)
    
    assets = []
    for symbol in symbols:
        try:
            asset_info = get_asset_id_and_decimals(symbol, all_assets)
            assets.append({
                "symbol": symbol,
                "assetId": asset_info["assetId"],
                "decimals": asset_info["decimals"]
            })
        except ValueError:
            continue
            
    return assets
