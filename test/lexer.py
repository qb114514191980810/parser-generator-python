import enum
import io
import unittest

from src.lexer import Lexer
from src.types_ import Token
from src.types_ import Position

class TokenEnum(enum.Enum):
    CASE_A = 1
    CASE_B = 2

class TestLexer(unittest.TestCase):
    def test_normal(self):
        stream=io.StringIO("ABA")
        lexer = Lexer({
            "A":(lambda x, y:Token(TokenEnum.CASE_A, 1, Position(0,0), Position(0,0))),
            "B":(lambda x, y:Token(TokenEnum.CASE_B, 2, Position(0,0), Position(0,0))),
        }, stream)
        next_iter_lexer = next(iter(lexer))
        self.assertEqual(next_iter_lexer, Token(TokenEnum.CASE_A, 1, Position(0,0), Position(0,0)))
        self.assertEqual(next(iter(lexer)), Token(TokenEnum.CASE_B, 2, Position(0,0), Position(0,0)))
        self.assertEqual(next(iter(lexer)), Token(TokenEnum.CASE_A, 1, Position(0,0), Position(0,0)))
        with self.assertRaises(StopIteration):
            next(iter(lexer))
    def test_invalid_stream(self):
        with self.assertRaises(TypeError):
            Lexer({}, None)

unittest.main()
