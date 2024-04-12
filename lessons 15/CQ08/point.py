"""Intro To Object Oriented Programming!"""

from __future__ import annotations


class Point:
    """Create class point!"""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Define the init function!"""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutate point by scale!"""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Mutate point scale!"""
        my_point: Point = Point(self.x, self.y)
        my_point.x = my_point.x * factor
        my_point.y = my_point.y * factor
        return my_point