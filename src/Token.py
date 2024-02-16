from enum import Enum, auto
from typing import final

@final
class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type: TokenType = type
        self.lexeme: str = lexeme
        self.literal: object = literal
        self.line: int = line

    def toString(self) -> str: 
        '''
        return token info for debug purposes
        '''
        return f"{self.type} {self.lexeme} {self.literal}"


class TokenType(Enum):
# Single-character tokens.
	LEFT_PAREN = auto()
	RIGHT_PAREN = auto()
	LEFT_BRACE = auto()
	RIGHT_BRACE = auto()
	COMMA = auto()
	DOT = auto()
	MINUS = auto()
	PLUS = auto()
	SEMICOLON = auto()
	SLASH = auto()
	STAR = auto()

# One or two character tokens.
	BANG = auto()
	BANG_EQUAL = auto()
	EQUAL = auto()
	EQUAL_EQUAL = auto()
	GREATER = auto()
	GREATER_EQUAL = auto()
	LESS = auto()
	LESS_EQUAL = auto()

  # Literals.
	IDENTIFIER = auto()
	STRING = auto()
	NUMBER = auto()

# Keywords.
	AND = auto()
	CLASS = auto()
	ELSE = auto()
	FALSE = auto()
	FUN = auto()
	FOR = auto()
	IF = auto()
	NIL = auto()
	OR = auto()
	PRINT = auto()
	RETURN = auto()
	SUPER = auto()
	THIS = auto()
	TRUE = auto()
	VAR = auto()
	WHILE = auto()

	EOF = auto()
