from enum import Enum


class Type(Enum):
    TABLE = 0
    A = 1
    B = 2
    C = 3

    def __str__(self) -> str:
        return self.name


class Block:
    def __init__(self, name: Type, below: Type):
        self.name = name
        self.below = below

    def __str__(self):
        return "Below Block " + str(self.name) + " is " + str(self.below)

    def set_name(self, name: Type) -> None:
        self.name = name

    def set_below(self, below: Type) -> None:
        self.below = below

    def __eq__(self, aux) -> bool:
        return self.name == aux.name
