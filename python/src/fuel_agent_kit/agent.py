from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from .tools import create_tools
from .utils.models import MODEL_MAPPING

SYSTEM_MESSAGE = SystemMessage(content=''' You are an AI agent on Fuel network capable of executing all kinds of transactions and interacting with the Fuel blockchain.
You are able to execute transactions on behalf of the user.

If the transaction was successful, return the response in the following format:
The transaction was successful. The explorer link is: https://app.fuel.network/tx/0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef/simple

If the transaction was unsuccessful, return the response in the following format, followed by an explanation if any known:
The transaction failed.
''')

prompt = ChatPromptTemplate.from_messages([
    SYSTEM_MESSAGE,
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

def create_agent(fuel_agent, model_name: str, openai_api_key: str = None, anthropic_api_key: str = None, google_gemini_api_key: str = None) -> AgentExecutor:
    provider = MODEL_MAPPING.get(model_name)
    
    selected_model = None
    if provider == "openai":
        if not openai_api_key:
            raise ValueError("OpenAI API key is required")
        from langchain_openai import ChatOpenAI
        selected_model = ChatOpenAI(model=model_name, api_key=openai_api_key)
    elif provider == "anthropic":
        if not anthropic_api_key:
            raise ValueError("Anthropic API key is required")
        try:
            from langchain_anthropic import ChatAnthropic
            selected_model = ChatAnthropic(model=model_name, api_key=anthropic_api_key)
        except ImportError:
            raise ImportError("langchain-anthropic is not installed")
    elif provider == "gemini":
        if not google_gemini_api_key:
            raise ValueError("Google Gemini API key is required")
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            selected_model = ChatGoogleGenerativeAI(model=model_name, api_key=google_gemini_api_key, convert_system_message_to_human=True)
        except ImportError:
            raise ImportError("langchain-google-genai is not installed")
    else:
        raise ValueError(f"Model {model_name} not supported or recognized")

    tools = create_tools(fuel_agent)
    
    agent = create_tool_calling_agent(
        llm=selected_model,
        tools=tools,
        prompt=prompt
    )
    
    return AgentExecutor(agent=agent, tools=tools)
