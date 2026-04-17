"""Model configuration for supported AI providers."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ModelProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"


MODEL_MAPPING: dict[str, ModelProvider] = {
    "gpt-4o": ModelProvider.OPENAI,
    "gpt-4o-mini": ModelProvider.OPENAI,
    "claude-3-5-sonnet-latest": ModelProvider.ANTHROPIC,
    "claude-3-5-haiku-latest": ModelProvider.ANTHROPIC,
    "gemini-1.5-flash": ModelProvider.GEMINI,
    "gemini-2.0-flash-exp": ModelProvider.GEMINI,
}


@dataclass
class ModelConfig:
    """Configuration for AI model selection."""

    model: str = "gpt-4o-mini"
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None

    @property
    def provider(self) -> ModelProvider:
        if self.model not in MODEL_MAPPING:
            raise ValueError(
                f"Unknown model: {self.model}. "
                f"Supported: {list(MODEL_MAPPING.keys())}"
            )
        return MODEL_MAPPING[self.model]

    def get_api_key(self) -> str:
        provider = self.provider
        if provider == ModelProvider.OPENAI:
            if not self.openai_api_key:
                raise ValueError("openai_api_key is required for OpenAI models")
            return self.openai_api_key
        elif provider == ModelProvider.ANTHROPIC:
            if not self.anthropic_api_key:
                raise ValueError("anthropic_api_key is required for Anthropic models")
            return self.anthropic_api_key
        elif provider == ModelProvider.GEMINI:
            if not self.google_api_key:
                raise ValueError("google_api_key is required for Gemini models")
            return self.google_api_key
        raise ValueError(f"Unknown provider: {provider}")
