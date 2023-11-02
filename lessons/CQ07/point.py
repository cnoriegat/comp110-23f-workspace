"""Intro To Object Oriented Programming."""


from __future__ import annotations
__author__ = "730621572"


class Point:
    """Representing a point on an (x,y) coordinate graph."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that belongs to the Point class and mutates a Point."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point: 
        """Method that belongs to the Point class and creates a new Point."""
        self.x *= factor
        self.y *= factor
        return Point