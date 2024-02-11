from typing import Dict, Any
import io

from position import Position

class Lexer(object):
    """
    A lexer.

    Iterable
    Attributes:
        stream: StringIO object of the parsing stream.
        pos: The position the lexer at at start.
        EOFed: Is the lexer parsed to an EOF.
    """
    def __init__(
            self, stream:io.TextIOBase, pos:Position=Position(0,0),
            condition:Any # TODO: Not implemented yet
        ):
        self.stream = stream # Go to setter for value checking
        self.pos = pos
        self.EOFed = False
        self.condition = condition
    def __iter__(self):
        return self
    def __next__(self):
        if self.EOFed:
            raise StopIteration
        # TODO: Not implemented yet
        raise NotImplementedError()
    @property
    def stream(self):
        return self.__stream
    @stream.setter
    def stream(self, value:io.TextIOBase):
        if not isinstance(value, io.TextIOBase):
            raise TypeError(f"Invalid type for Lexer.stream"
                             " (want TextIOBase, got '{type(value)}')")
        self.__stream = value
