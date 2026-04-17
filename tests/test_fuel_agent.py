"""Tests for FuelAgent."""

import pytest
from decimal import Decimal
from fuel_agent import FuelAgent, FuelAgentConfig


class TestFuelAgent:
    """Test suite for FuelAgent."""
    
    def test_init_requires_private_key(self):
        """Test that initialization requires private key."""
        with pytest.raises(ValueError, match="private key is required"):
            FuelAgent(FuelAgentConfig(wallet_private_key=""))
    
    def test_init_success(self):
        """Test successful initialization."""
        config = FuelAgentConfig(
            wallet_private_key="test-key",
            model="gpt-4",
            openai_api_key="test-openai-key"
        )
        agent = FuelAgent(config)
        assert agent is not None
        
        creds = agent.get_credentials()
        assert creds["model"] == "gpt-4"
        assert creds["has_openai"] is True
        assert creds["has_anthropic"] is False
    
    @pytest.mark.asyncio
    async def test_execute_returns_response(self):
        """Test that execute returns a response."""
        config = FuelAgentConfig(
            wallet_private_key="test-key",
            model="gpt-4",
        )
        agent = FuelAgent(config)
        
        response = await agent.execute("Hello")
        assert "input" in response
        assert "output" in response
        assert "action" in response


class TestFuelAgentOperations:
    """Test DeFi operations."""
    
    @pytest.mark.asyncio
    async def test_swap_exact_input(self):
        """Test swap operation."""
        config = FuelAgentConfig(wallet_private_key="test-key")
        agent = FuelAgent(config)
        
        result = await agent.swap_exact_input(
            from_token="USDC",
            to_token="ETH",
            amount=Decimal("100")
        )
        
        assert result["success"] is True
        assert result["from_token"] == "USDC"
        assert result["to_token"] == "ETH"
    
    @pytest.mark.asyncio
    async def test_transfer(self):
        """Test transfer operation."""
        config = FuelAgentConfig(wallet_private_key="test-key")
        agent = FuelAgent(config)
        
        result = await agent.transfer(
            to_address="0x123...",
            token="ETH",
            amount=Decimal("1.5")
        )
        
        assert result["success"] is True
        assert result["to"] == "0x123..."
    
    @pytest.mark.asyncio
    async def test_get_balance(self):
        """Test balance check."""
        config = FuelAgentConfig(wallet_private_key="test-key")
        agent = FuelAgent(config)
        
        result = await agent.get_balance("ETH")
        
        assert result["success"] is True
        assert result["token"] == "ETH"
        assert "balance" in result
