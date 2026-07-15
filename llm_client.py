"""Thin wrapper around the OpenAI chat completions API with retry and usage tracking."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

from openai import OpenAI, RateLimitError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

if TYPE_CHECKING:
    from collections.abc import Generator

logger = logging.getLogger(__name__)

SYSTEM_PROMPT_PATH = Path(__file__).parent / "system.md"


def _load_system_prompt() -> str | None:
    try:
        content = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None
    return content or None


class LLMClient:
    """Streaming chat completions client for a single OpenAI-compatible model."""

    def __init__(self, model: str) -> None:
        """Store the model name and create the underlying OpenAI client."""
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.last_usage = None

    @retry(
        retry=retry_if_exception_type(RateLimitError),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=10),
    )
    def stream(self, prompt: str, max_tokens: int = 2000) -> Generator[str]:
        """Stream a completion for prompt, yielding text deltas as they arrive."""
        self.last_usage = None
        messages = []
        system_prompt = _load_system_prompt()
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            stream_options={"include_usage": True},
            max_completion_tokens=max_tokens,
        )
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
            if chunk.usage:
                self.last_usage = chunk.usage
