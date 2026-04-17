"""Type definitions for Fuel Agent Kit."""

from typing import Literal, Dict, Type
from enum import Enum


class ModelMapping:
    """Supported AI models."""
    
    OPENAI_GPT4 = "gpt-4"
    OPENAI_GPT4_TURBO = "gpt-4-turbo-preview"
    OPENAI_GPT35 = "gpt-3.5-turbo"
    ANTHROPIC_CLAUDE3 = "claude-3-opus-20240229"
    ANTHROPIC_CLAUDE3_SONNET = "claude-3-sonnet-20240229"
    GOOGLE_GEMINI = "gemini-pro"


ModelType = Literal[
    "gpt-4",
    "gpt-4-turbo-preview", 
    "gpt-3.5-turbo",
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "gemini-pro"
]
