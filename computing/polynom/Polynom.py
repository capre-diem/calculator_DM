from __future__ import annotations
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer
from computing.rational.Rational import Rational


class Polynom:
    data: list[Rational]
    degree: int

    def __init__(self, value: list[Rational]) -> None:
        self.data = value
        while len(self.data) > 1 and self.data[-1] == 0:
            self.data.pop()
        self.degree = len(value)

    def __str__(self):
        s = ", ".join(str(x) for x in self.data)
        return f"[{s}]"

    def __repr__(self):
        return f"Polynom({self})"

    def add(self: Polynom, other: Polynom) -> Polynom:
        from .add import add
        return add(self, other)
