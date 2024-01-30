from typing import final

from TokenType import TokenType

@final
class Token:
    # this is python code
    def __init__(self, type, lexeme, literal, line):
        self.type: TokenType = type
        self.lexeme: str = lexeme
        self.literal: object = literal
        self.line: int = line

    def toString(self):
        return f"{self.type} {self.lexeme} {self.literal}"
