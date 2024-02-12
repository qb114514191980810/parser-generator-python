import enum
import io
import unittest

from src.lexer import Lexer
from src.types_ import Token

class TokenEnum(enum.Enum):
    CASE_A = 1
    CASE_B = 2

class TestLexer(unittest.TestCase):
    def test_normal(self):
        stream=io.StringIO("ABA")
        lexer = Lexer({
            "A":(lambda x, y:Token(TokenEnum.CASE_A, 1)),
            "B":(lambda x, y:Token(TokenEnum.CASE_B, 2)),
        }, stream)
        self.assertEqual(next(iter(lexer)), Token(TokenEnum.CASE_A, 1))
        self.assertEqual(next(iter(lexer)), Token(TokenEnum.CASE_B, 2))
        self.assertEqual(next(iter(lexer)), Token(TokenEnum.CASE_A, 1))
        with self.assertRaises(StopIteration):
            next(iter(lexer))
    def test_invalid_stream(self):
        with self.assertRaises(TypeError):
            Lexer({}, None)

unittest.main()
