from typing import List

from Token import Token, TokenType

def ScanTokens(src: str) -> List[Token] :
    '''
    ScanTokens is the scanner/lexer
    '''
    tokens: List[Token] = []
    start: int = 0
    current: int = 0
    line: int = 1

    def isAtEnd() -> bool:
       return current == len(src)

    for char in src:
        current += 1

        if isAtEnd(): tokens.append(Token(TokenType.EOF, "", None, line)); break
        if char == '\n': line += 1


        # Check for single char tokens and add the token to the list
        if char == '(':tokens.append(Token(TokenType.LEFT_PAREN, char, None, line))
        if char == ')':tokens.append(Token(TokenType.RIGHT_PAREN, char, None, line))
        if char == '[':tokens.append(Token(TokenType.LEFT_BRACE, char, None, line))
        if char == ']':tokens.append(Token(TokenType.RIGHT_BRACE, char, None, line))
        if char == ',': tokens.append(Token(TokenType.COMMA, char, None, line))
        if char == '.': tokens.append(Token(TokenType.DOT, char, None, line))
        if char == '-': tokens.append(Token(TokenType.MINUS, char, None, line))
        if char == '+': tokens.append(Token(TokenType.PLUS, char, None, line))
        if char == ';': tokens.append(Token(TokenType.SEMICOLON, char, None, line))
        if char == '/': tokens.append(Token(TokenType.SLASH, char, None, line))
        if char == '*': tokens.append(Token(TokenType.STAR, char, None, line))

    return tokens

