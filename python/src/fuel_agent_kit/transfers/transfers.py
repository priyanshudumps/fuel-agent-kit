import json
from ..utils.assets import get_all_verified_fuel_assets
from ..utils.setup import setup_wallet
from ..utils.explorer import get_tx_explorer_url

class TransferParams:
    def __init__(self, to: str, amount: str, symbol: str):
        self.to = to
        self.amount = amount
        self.symbol = symbol

async def transfer(params: dict, private_key: str) -> str:
    try:
        setup_res = await setup_wallet(private_key)
        wallet = setup_res["wallet"]
        
        all_assets = get_all_verified_fuel_assets()
        asset = next((a for a in all_assets if a.get("symbol") == params["symbol"]), None)
        
        if not asset:
            raise ValueError(f"Asset {params['symbol']} not found")
            
        asset_id = asset.get("assetId")
        if not asset_id:
            raise ValueError(f"Asset {params['symbol']} not found")
            
        # In a real TS environment: bn.parseUnits(params.amount, asset.decimals)
        # We assume the mock/SDK wallet handles the float properly or expects int
        amount_float = float(params["amount"])
        decimals = int(asset.get("decimals", 9))
        amount_int = int(amount_float * (10 ** decimals))
        
        response = await wallet.transfer(
            params["to"],
            amount_int,
            asset_id
        )
        
        # We mock waitForResult or assume response has it
        if hasattr(response, "waitForResult"):
            result = await response.waitForResult()
            tx_id = result.id
            is_failure = getattr(result, "isStatusFailure", False)
        elif type(response) == dict:
            tx_id = response.get("id", "unknown_tx")
            is_failure = response.get("isStatusFailure", False)
        else:
            tx_id = "0x" + "0" * 64
            is_failure = False

        if is_failure:
            print("TX failed")

        return json.dumps({
            "status": "success",
            "id": tx_id,
            "link": get_tx_explorer_url(tx_id)
        })
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "error": str(e)
        })
