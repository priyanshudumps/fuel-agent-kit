import logging
from typing import List, Dict, Any, Callable
from .tools import Tool

class Agent:
    def __init__(self, name: str = "FuelAgent", tools: List[Tool] = None, llm: Callable = None):
        self.name = name
        self.tools = tools or []
        self.llm = llm
        self.memory = []
        self.logger = logging.getLogger(__name__)

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def get_tool_descriptions(self) -> str:
        return "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])

    def run(self, task: str) -> str:
        self.memory.append({"role": "user", "content": task})
        prompt = self._build_prompt(task)
        response = self.llm(prompt) if self.llm else "I need an LLM to process this task."
        self.memory.append({"role": "assistant", "content": response})
        return response

    def _build_prompt(self, task: str) -> str:
        tools_desc = self.get_tool_descriptions()
        return f"Task: {task}\n\nAvailable tools:\n{tools_desc}\n\nHow would you solve this task?"
