"""FuelAgent - Main agent class for the Fuel Agent Kit Python version."""

import json
from typing import Optional

from langchain_core.prompts import ChatPromptTemplate, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor

from .constants import SUPPORTED_MODELS, DEFAULT_SLIPPAGE
from .tools import create_tools
from .assets import find_asset, get_fuel_assets, get_explorer_url


SYSTEM_PROMPT = """You are an AI agent on the Fuel network capable of executing transactions and interacting with the Fuel blockchain.
You are able to execute transactions on behalf of the user.

If the transaction was successful, return the response in the following format:
The transaction was successful. The explorer link is: https://app.fuel.network/tx/0x123.../simple

If the transaction was unsuccessful, return the response in the following format, followed by an explanation if any known:
The transaction failed.
"""


class FuelAgent:
    """
    An AI agent for interacting with the Fuel blockchain.

    Supports token transfers, DEX swaps on Mira, liquidity provision,
    lending/borrowing on Swaylend, and balance queries.
    """

    def __init__(
        self,
        wallet_private_key: str,
        model: str,
        openai_api_key: Optional[str] = None,
        anthropic_api_key: Optional[str] = None,
        google_gemini_api_key: Optional[str] = None,
    ):
        if not wallet_private_key:
            raise ValueError("Fuel wallet private key is required.")

        self._wallet_private_key = wallet_private_key
        self._model_name = model

        if model not in SUPPORTED_MODELS:
            raise ValueError(
                f"Unsupported model: {model}. "
                f"Supported: {list(SUPPORTED_MODELS.keys())}"
            )

        provider = SUPPORTED_MODELS[model]
        if provider == "openai" and not openai_api_key:
            raise ValueError("OpenAI API key is required for OpenAI models.")
        if provider == "anthropic" and not anthropic_api_key:
            raise ValueError(
                "Anthropic API key is required for Anthropic models."
            )
        if provider == "google" and not google_gemini_api_key:
            raise ValueError(
                "Google Gemini API key is required for Google models."
            )

        self._llm = self._create_llm(
            model, openai_api_key, anthropic_api_key, google_gemini_api_key
        )
        self._tools = create_tools(self)
        self._agent_executor = self._create_agent()

    def _create_llm(
        self,
        model: str,
        openai_key: Optional[str],
        anthropic_key: Optional[str],
        google_key: Optional[str],
    ):
        """Create the appropriate LLM based on the model name."""
        provider = SUPPORTED_MODELS[model]
        if provider == "openai":
            return ChatOpenAI(model=model, api_key=openai_key)
        elif provider == "anthropic":
            return ChatAnthropic(model=model, api_key=anthropic_key)
        elif provider == "google":
            return ChatGoogleGenerativeAI(model=model, api_key=google_key)

    def _create_agent(self) -> AgentExecutor:
        """Create the LangChain agent executor."""
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SYSTEM_PROMPT),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        agent = create_tool_calling_agent(
            llm=self._llm,
            tools=self._tools,
            prompt=prompt,
        )

        return AgentExecutor(agent=agent, tools=self._tools)

    def execute(self, input_text: str) -> dict:
        """Execute a natural language command on the Fuel blockchain."""
        return self._agent_executor.invoke({"input": input_text})

    def transfer(self, to: str, amount: str, symbol: str) -> str:
        """Transfer tokens to a wallet address."""
        assets = get_fuel_assets()
        asset = find_asset(symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": f"Would transfer {amount} {symbol} to {to}",
                "asset_id": asset.asset_id,
                "decimals": asset.decimals,
            }
        )

    def swap(
        self,
        amount: str,
        from_symbol: str,
        to_symbol: str,
        slippage: float = DEFAULT_SLIPPAGE,
    ) -> str:
        """Swap tokens on Mira DEX."""
        assets = get_fuel_assets()
        from_asset = find_asset(from_symbol, assets)
        to_asset = find_asset(to_symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": (
                    f"Would swap {amount} {from_symbol} for {to_symbol} "
                    f"with {slippage * 100}% slippage"
                ),
                "from_asset_id": from_asset.asset_id,
                "to_asset_id": to_asset.asset_id,
            }
        )

    def supply_collateral(self, amount: str, symbol: str) -> str:
        """Supply collateral on Swaylend."""
        assets = get_fuel_assets()
        asset = find_asset(symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": f"Would supply {amount} {symbol} as collateral",
                "asset_id": asset.asset_id,
            }
        )

    def borrow(self, amount: str) -> str:
        """Borrow USDC from Swaylend."""
        return json.dumps(
            {
                "status": "success",
                "message": f"Would borrow {amount} USDC from Swaylend",
            }
        )

    def add_liquidity(
        self,
        amount0: str,
        asset0_symbol: str,
        asset1_symbol: str,
        slippage: float = DEFAULT_SLIPPAGE,
    ) -> str:
        """Add liquidity to a Mira pool."""
        assets = get_fuel_assets()
        asset0 = find_asset(asset0_symbol, assets)
        asset1 = find_asset(asset1_symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": (
                    f"Would add {amount0} {asset0_symbol} + {asset1_symbol} "
                    f"liquidity with {slippage * 100}% slippage"
                ),
                "asset0_id": asset0.asset_id,
                "asset1_id": asset1.asset_id,
            }
        )

    def get_own_balance(self, symbol: str) -> str:
        """Get the balance of an asset in the agent's wallet."""
        assets = get_fuel_assets()
        asset = find_asset(symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": f"Balance lookup for {symbol}",
                "asset_id": asset.asset_id,
            }
        )

    def get_balance(self, wallet_address: str, asset_symbol: str) -> str:
        """Get the balance of an asset for a given wallet address."""
        assets = get_fuel_assets()
        asset = find_asset(asset_symbol, assets)
        return json.dumps(
            {
                "status": "success",
                "message": f"Balance lookup for {asset_symbol} at {wallet_address}",
                "asset_id": asset.asset_id,
            }
        )
