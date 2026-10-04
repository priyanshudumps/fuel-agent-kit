from fuel_agent_kit import Agent, Tool, setup_logging

def search_web(query: str) -> str:
    return f"Searching web for: {query}"

def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def main():
    setup_logging()
    
    search_tool = Tool(
        name="search_web",
        description="Search the web for information",
        func=search_web
    )
    
    calc_tool = Tool(
        name="calculate",
        description="Perform mathematical calculations",
        func=calculate
    )
    
    agent = Agent(
        name="WebResearchAgent",
        tools=[search_tool, calc_tool],
        llm=lambda prompt: f"Agent response to: {prompt[:50]}..."
    )
    
    result = agent.run("What is the weather in Paris?")
    print(result)

if __name__ == "__main__":
    main()
