import os
from typing import Optional, List
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class FuelDeepSeekAgent:
    """
    A real Fuel AI Agent powered by DeepSeek.
    Unlike competitors, this implementation uses actual tool-calling logic.
    """
    
    def __init__(
        self, 
        api_key: str, 
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-chat"
    ):
        self.llm = ChatOpenAI(
            model=model,
            openai_api_key=api_key,
            openai_api_base=base_url,
            temperature=0
        )
        self.tools = []
        self.agent_executor = None

    def setup_agent(self, tools: List):
        """Bind tools and create the real agent executor."""
        self.tools = tools
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a specialized Fuel Blockchain Agent. Use your tools to help users with on-chain operations."),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        
        agent = create_openai_tools_agent(self.llm, self.tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)

    async def run(self, user_input: str):
        """Execute the agent loop with real blockchain tools."""
        if not self.agent_executor:
            # Auto-setup with our real tools if not already done
            from .tools.transfer_tool import fuel_transfer_tool
            self.setup_agent(tools=[fuel_transfer_tool])
            
        return await self.agent_executor.ainvoke({"input": user_input})

