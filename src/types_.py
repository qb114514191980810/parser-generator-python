"""
Help types
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any

class Position:
    """
    The position in the file the lexer at.

    Attributes:
        column: the column the cursor at.
        row: the row the cursor at.
    """
    def __init__(self, column:int=0, row:int=0):
        self.column = column
        self.row = row
    def advance(self, length:int):
        """
        Move the cursor.

        Args:
            length: Count of the characters advanced.
        """
        self.column += length
    def linefeed(self):
        """
        Move the cursor to the next line.

        Note that it will also move the cursor to the start of the line."""
        self.row += 1
        self.column = 0

@dataclass
class Token:
    """
    Tokens generated from Lexer.

    Attributes:
        type_: The token's type.
        value: The token's value.
    """
    def __init__(self, type_: Enum, value: Any):
        self.type_ = type_
        self.value = value
