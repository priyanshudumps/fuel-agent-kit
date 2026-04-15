"""
Tests for FuelAgent Python version

Run with: python3 -m pytest tests/test_fuel_agent.py -v
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fuel_agent_kit import FuelAgent, FuelAgentConfig
from fuel_agent_kit.types import (
    SwapExactInputParams,
    AddLiquidityParams,
    SupplyCollateralParams,
    BorrowAssetParams,
    TransferParams,
    GetOwnBalanceParams,
)


class TestFuelAgentConfig:
    """Test FuelAgentConfig class"""
    
    def test_config_creation(self):
        """Test successful config creation"""
        config = FuelAgentConfig(
            wallet_private_key="test_private_key_12345",
            model="openai",
            openai_api_key="test_openai_key"
        )
        assert config.wallet_private_key == "test_private_key_12345"
        assert config.model == "openai"
        assert config.openai_api_key == "test_openai_key"
    
    def test_config_default_model(self):
        """Test default model is openai"""
        config = FuelAgentConfig(
            wallet_private_key="test_key"
        )
        assert config.model == "openai"
    
    def test_config_missing_private_key(self):
        """Test config raises error when private key is missing"""
        with pytest.raises(ValueError) as excinfo:
            config = FuelAgentConfig(
                wallet_private_key=""
            )
        assert "private key is required" in str(excinfo.value)


class TestFuelAgent:
    """Test FuelAgent class"""
    
    def test_agent_initialization(self):
        """Test successful agent initialization"""
        config = FuelAgentConfig(
            wallet_private_key="test_key_12345",
            model="openai"
        )
        agent = FuelAgent(config)
        assert agent is not None
        assert agent.wallet_private_key == "test_key_12345"
        assert agent.model == "openai"
    
    def test_agent_missing_private_key(self):
        """Test agent initialization fails without private key"""
        with pytest.raises(ValueError) as excinfo:
            config = FuelAgentConfig(wallet_private_key="")
            FuelAgent(config)
        assert "private key is required" in str(excinfo.value)
    
    def test_get_credentials(self):
        """Test getting credentials"""
        config = FuelAgentConfig(
            wallet_private_key="secret_key_123",
            model="openai",
            openai_api_key="sk_test_123",
            anthropic_api_key="anthropic_test_456",
            google_gemini_api_key="google_test_789"
        )
        agent = FuelAgent(config)
        creds = agent.get_credentials()
        
        assert creds["wallet_private_key"] == "secret_key_123"
        assert creds["openai_api_key"] == "sk_test_123"
        assert creds["anthropic_api_key"] == "anthropic_test_456"
        assert creds["google_gemini_api_key"] == "google_test_789"
    
    def test_get_credentials_empty_values(self):
        """Test getting credentials with empty optional values"""
        config = FuelAgentConfig(
            wallet_private_key="key_123",
            model="openai"
        )
        agent = FuelAgent(config)
        creds = agent.get_credentials()
        
        assert creds["wallet_private_key"] == "key_123"
        assert creds["openai_api_key"] == ""
        assert creds["anthropic_api_key"] == ""
        assert creds["google_gemini_api_key"] == ""


@pytest.mark.asyncio
class TestFuelAgentAsyncMethods:
    """Test FuelAgent async methods"""
    
    async def test_swap_exact_input(self):
        """Test swap exact input method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "amount": "1.5",
            "from_asset": "ETH",
            "to_asset": "USDC",
            "slippage": 0.5
        }
        result = await agent.swap_exact_input(params)
        
        assert result is not None
        assert result["status"] == "success"
        assert "tx_hash" in result
    
    async def test_add_liquidity(self):
        """Test add liquidity method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "amount0": "100",
            "amount1": "200",
            "asset0": "ETH",
            "asset1": "USDC"
        }
        result = await agent.add_liquidity(params)
        
        assert result is not None
        assert result["status"] == "success"
    
    async def test_supply_collateral(self):
        """Test supply collateral method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "amount": "50",
            "asset": "ETH"
        }
        result = await agent.supply_collateral(params)
        
        assert result is not None
        assert result["status"] == "success"
    
    async def test_borrow_asset(self):
        """Test borrow asset method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "amount": "100",
            "asset": "USDC"
        }
        result = await agent.borrow_asset(params)
        
        assert result is not None
        assert result["status"] == "success"
    
    async def test_transfer(self):
        """Test transfer method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "to": "0x1234567890abcdef1234567890abcdef12345678",
            "amount": "10",
            "asset": "ETH"
        }
        result = await agent.transfer(params)
        
        assert result is not None
        assert result["status"] == "success"
    
    async def test_get_own_balance(self):
        """Test get balance method"""
        config = FuelAgentConfig(
            wallet_private_key="test_key",
            model="openai"
        )
        agent = FuelAgent(config)
        
        params = {
            "asset": "ETH"
        }
        result = await agent.get_own_balance(params)
        
        assert result is not None
        assert "balance" in result
        assert result["asset"] == "ETH"


class TestTypeDefinitions:
    """Test type definitions"""
    
    def test_swap_params_type(self):
        """Test SwapExactInputParams type"""
        params: SwapExactInputParams = {
            "amount": "1.0",
            "from_asset": "ETH",
            "to_asset": "USDC",
            "slippage": 0.5
        }
        assert params["amount"] == "1.0"
        assert params["from_asset"] == "ETH"
    
    def test_liquidity_params_type(self):
        """Test AddLiquidityParams type"""
        params: AddLiquidityParams = {
            "amount0": "100",
            "amount1": "200",
            "asset0": "ETH",
            "asset1": "USDC"
        }
        assert params["amount0"] == "100"
    
    def test_supply_params_type(self):
        """Test SupplyCollateralParams type"""
        params: SupplyCollateralParams = {
            "amount": "50",
            "asset": "ETH"
        }
        assert params["amount"] == "50"
    
    def test_borrow_params_type(self):
        """Test BorrowAssetParams type"""
        params: BorrowAssetParams = {
            "amount": "100",
            "asset": "USDC"
        }
        assert params["amount"] == "100"
    
    def test_transfer_params_type(self):
        """Test TransferParams type"""
        params: TransferParams = {
            "to": "0xaddress",
            "amount": "10",
            "asset": "ETH"
        }
        assert params["to"] == "0xaddress"
    
    def test_balance_params_type(self):
        """Test GetOwnBalanceParams type"""
        params: GetOwnBalanceParams = {
            "asset": "ETH"
        }
        assert params["asset"] == "ETH"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
