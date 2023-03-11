"""Utilities for response."""

from typing import Generator


def get_response_text(response_gen: Generator) -> str:
    """Get response text."""
    return "".join(response_gen)
