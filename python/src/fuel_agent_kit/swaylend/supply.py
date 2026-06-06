import json
from ..utils.assets import get_all_verified_fuel_assets
from ..utils.setup import setup_wallet
from ..utils.explorer import get_tx_explorer_url

async def supply_collateral(params: dict, private_key: str) -> str:
    """
    Mocked implementation of supply_collateral for Swaylend.
    """
    try:
        setup_res = await setup_wallet(private_key)
        
        all_assets = get_all_verified_fuel_assets()
        asset = next((a for a in all_assets if a.get("symbol") == params["symbol"]), None)

        if not asset:
            raise ValueError(f"Asset {params['symbol']} not found")

        # MOCK EXECUTION
        mock_tx_id = "0x" + "d" * 64
        
        return json.dumps({
            "status": "success",
            "id": mock_tx_id,
            "link": get_tx_explorer_url(mock_tx_id)
        })
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "error": str(e)
        })
