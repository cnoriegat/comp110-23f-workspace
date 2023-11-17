"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730621572"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor."""
        self.values = values
        return None