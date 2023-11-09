"""Intro To Object Oriented Programming."""


from __future__ import annotations


__author__ = "730621572"


class Point:
    """Class to represent (x,y) coordinate point."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Construct a point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Modify (or mutate) a point."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point: 
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Printing points in a readable way."""
        p_string: str = f"x: {self.x}; y: {self.y}"
        return p_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplying each point to a factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Adding each point to a factor."""
        return Point(self.x + factor, self.y + factor)