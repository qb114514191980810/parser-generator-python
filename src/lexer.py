"""
A module contains the lexer.
"""

from typing import Any, Callable
import io
import re

from src.types_ import Position, Token

class Lexer:
    """
    A lexer.

    Iterable
    Attributes:
        stream: StringIO object of the parsing stream.
        pos: The position the lexer at at start.
        EOFed: Is the lexer parsed to an EOF.
    """
    def __init__(
            self, condition:dict[re.Pattern, Callable[[Any, str], Token]],
            stream:io.TextIOBase, pos:Position=Position(0,0),
    ):
        self.__stream = stream # I hate pylint
        self.stream = stream # Go to setter for value checking
        self.pos = pos
        self.eof_ed = False
        self.condition = condition
    def __iter__(self):
        return self
    def __next__(self) -> Token:
        parsing_string = ""
        find = None
        while not self.eof_ed:
            prev_pos = self.stream.tell()
            new_char = self.stream.read(1)
            if new_char == '':
                new_char = '<<EOF>>'
                self.eof_ed = True
            parsing_string += new_char
            for i in self.condition.keys():
                if re.fullmatch(i, parsing_string):
                    find=i
                    break
            else:
                if find:
                    self.stream.seek(prev_pos)
                    retval = self.condition[find](self, parsing_string)
                    if retval:
                        return retval
        raise StopIteration
    @property
    def stream(self) -> io.TextIOBase:
        """
        The current stream of the lexer.
        """
        return self.__stream
    @stream.setter
    def stream(self, value:io.TextIOBase):
        if not isinstance(value, io.TextIOBase):
            raise TypeError("Invalid type for Lexer.stream"
                            f" (want TextIOBase, got '{type(value)}')")
        if not (value.seekable() and value.readable()):
            raise RuntimeError("Cannot seek/read the stream")
        self.__stream = value
        self.pos = Position(0,0)
