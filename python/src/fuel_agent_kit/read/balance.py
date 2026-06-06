import json
from ..utils.assets import get_all_verified_fuel_assets
from ..utils.setup import setup_wallet, ProviderInstance

async def get_own_balance(params: dict, private_key: str) -> str:
    try:
        setup_res = await setup_wallet(private_key)
        wallet = setup_res["wallet"]
        
        all_assets = get_all_verified_fuel_assets()
        asset = next((a for a in all_assets if a.get("symbol") == params["symbol"]), None)
        
        if not asset:
            raise ValueError(f"Asset {params['symbol']} not found")
            
        asset_id = asset.get("assetId")
        balance_obj = await wallet.getBalance(asset_id)
        
        if hasattr(balance_obj, "formatUnits"):
            balance_str = balance_obj.formatUnits(asset.get("decimals", 9))
        else:
            # Fallback if no formatUnits (e.g. integer returned directly or mocked)
            decimals = asset.get("decimals", 9)
            if isinstance(balance_obj, int):
                balance_str = str(balance_obj / (10 ** decimals))
            else:
                balance_str = str(balance_obj)
        
        return json.dumps({
            "status": "success",
            "balance": balance_str
        })
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "error": str(e)
        })

async def get_balance(params: dict) -> str:
    try:
        provider = await ProviderInstance.get_provider()
        
        all_assets = get_all_verified_fuel_assets()
        asset = next((a for a in all_assets if a.get("symbol") == params["assetSymbol"]), None)
        
        if not asset:
            raise ValueError(f"Asset {params['assetSymbol']} not found")
            
        asset_id = asset.get("assetId")
        wallet_address = params["walletAddress"]
        
        # provider might not have getBalance in the exact same format
        if hasattr(provider, "get_balance"):
            balance_obj = await provider.get_balance(wallet_address, asset_id)
        elif hasattr(provider, "getBalance"):
            balance_obj = await provider.getBalance(wallet_address, asset_id)
        else:
            balance_obj = 0
        
        if hasattr(balance_obj, "formatUnits"):
            balance_str = balance_obj.formatUnits(asset.get("decimals", 9))
        else:
            decimals = asset.get("decimals", 9)
            if isinstance(balance_obj, int):
                balance_str = str(balance_obj / (10 ** decimals))
            else:
                balance_str = str(balance_obj)
                
        return json.dumps({
            "status": "success",
            "balance": balance_str
        })
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "error": str(e)
        })
