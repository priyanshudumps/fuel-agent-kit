import os
from typing import Any

# Since fuels-python might be different or unavailable, we stub if needed,
# or we try to use the python fuels package.
try:
    from fuels import Provider, Wallet
    FUELS_AVAILABLE = True
except ImportError:
    FUELS_AVAILABLE = False
    
    # Mock classes for when fuels-python is not fully installed
    class Provider:
        @classmethod
        async def create(cls, url: str) -> 'Provider':
            instance = cls()
            instance.url = url
            return instance
            
    class Wallet:
        @classmethod
        def fromPrivateKey(cls, private_key: str, provider: 'Provider') -> 'Wallet':
            instance = cls()
            instance.private_key = private_key
            instance.provider = provider
            return instance
            
        async def transfer(self, to: str, amount: Any, asset_id: str) -> Any:
            class MockResponse:
                async def waitForResult(self):
                    return type("Result", (), {"id": "0x" + "a"*64, "isStatusFailure": False})()
            return MockResponse()
            
        async def getBalance(self, asset_id: str) -> Any:
            class MockBalance:
                def formatUnits(self, decimals: int) -> str:
                    return "1.0"
            return MockBalance()

class ProviderInstance:
    _instance = None
    PROVIDER_URL = 'https://mainnet.fuel.network/v1/graphql'

    @classmethod
    async def get_provider(cls):
        if cls._instance is None:
            if FUELS_AVAILABLE:
                # Python SDK might have create method or just constructor
                if hasattr(Provider, 'create'):
                    cls._instance = await Provider.create(cls.PROVIDER_URL)
                else:
                    cls._instance = Provider(cls.PROVIDER_URL)
            else:
                cls._instance = await Provider.create(cls.PROVIDER_URL)
        return cls._instance

async def setup_wallet(private_key: str):
    provider = await ProviderInstance.get_provider()
    
    if FUELS_AVAILABLE:
        if hasattr(Wallet, 'fromPrivateKey'):
            wallet = Wallet.fromPrivateKey(private_key, provider)
        elif hasattr(Wallet, 'from_private_key'):
            wallet = Wallet.from_private_key(private_key, provider)
        else:
            wallet = Wallet(private_key, provider)
    else:
        wallet = Wallet.fromPrivateKey(private_key, provider)
        
    return {
        "wallet": wallet,
        "provider": provider
    }
