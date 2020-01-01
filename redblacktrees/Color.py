from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2

    def __str__(self):
        if self == Color.RED:
            return "R"
        elif self == Color.BLACK:
            return "B"
        else:
            return "U"