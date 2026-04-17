"""Tests for FuelAgent."""

import pytest
from fuel_agent_kit import FuelAgent, ModelConfig


@pytest.fixture
def agent():
    return FuelAgent(
        config=type(
            "Config",
            (),
            {
                "wallet_private_key": "0x" + "a" * 64,
                "model": "gpt-4o-mini",
                "openai_api_key": "sk-test",
                "anthropic_api_key": None,
                "google_api_key": None,
                "provider_url": "https://mainnet.fuel.network/v1/graphql",
            },
        )()
    )


def test_agent_creation(agent):
    assert agent is not None
    assert agent._private_key == "0x" + "a" * 64


def test_get_own_balance(agent):
    result = agent.get_own_balance("ETH")
    assert result["status"] == "pending"
    assert result["symbol"] == "ETH"


def test_transfer(agent):
    result = agent.transfer("0x" + "b" * 64, "1.5", "USDC")
    assert result["status"] == "pending"
    assert result["amount"] == "1.5"
    assert result["symbol"] == "USDC"


def test_swap_exact_input(agent):
    result = agent.swap_exact_input("0.1", "USDC", "ETH")
    assert result["status"] == "pending"
    assert result["from"] == "USDC"
    assert result["to"] == "ETH"


def test_add_liquidity(agent):
    result = agent.add_liquidity("1", "ETH", "USDC")
    assert result["status"] == "pending"
    assert result["asset0"] == "ETH"
    assert result["asset1"] == "USDC"


def test_supply_collateral(agent):
    result = agent.supply_collateral("100", "USDT")
    assert result["status"] == "pending"
    assert result["symbol"] == "USDT"


def test_borrow_asset(agent):
    result = agent.borrow_asset("50")
    assert result["status"] == "pending"
    assert result["amount"] == "50"


def test_explorer_url(agent):
    url = agent.get_explorer_url("abc123")
    assert "abc123" in url
    assert "fuel.network" in url


def test_model_config():
    config = ModelConfig(model="gpt-4o-mini", openai_api_key="sk-test")
    assert config.provider.value == "openai"
    assert config.get_api_key() == "sk-test"


def test_model_config_invalid():
    config = ModelConfig(model="invalid-model")
    with pytest.raises(ValueError, match="Unknown model"):
        _ = config.provider
