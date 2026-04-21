"""Model provider utilities."""

from typing import Optional
from enum import Enum


class ModelProvider(Enum):
    """AI model providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"


def get_model_provider(model: str) -> ModelProvider:
    """Get the provider for a given model."""
    if "gpt" in model.lower():
        return ModelProvider.OPENAI
    elif "claude" in model.lower():
        return ModelProvider.ANTHROPIC
    elif "gemini" in model.lower():
        return ModelProvider.GOOGLE
    else:
        raise ValueError(f"Unknown model: {model}")
