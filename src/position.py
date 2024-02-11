"""
A module for class Position.
"""
class Position(object):
    """
    The position in the file the lexer at.

    Attributes:
        x: the column the cursor at.
        y: the row the cursor at.
    """
    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y
    def advance(self, length:int):
        """
        Move the cursor.

        Args:
            length: Count of the characters with 
        """
        self.x += length
    def linefeed(self):
        """
        Move the cursor to the next line.

        Note that it will also move the cursor to the start of the line."""
        self.y += 1
        self.x = 0
