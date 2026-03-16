from dataclasses import dataclass
from enum import Enum, auto
import numpy as np

def read_file(file_name):
    input_file:str = ""
    with open(file_name, 'r') as file:
        input_file = file.read()
    return input_file

class Keyword(Enum):
    Int = "int"
    Empty = 0
    
class TokenType(Enum):
    Keyword = "keyword"
    Identifier = "identifier"
    Plus = "+"
    Minus = "-"
    Multiply = "*"
    Divide = "/"
    Equal = "="
    Empty = 0

@dataclass
class Token:
    TokenType: TokenType
    value: str | Keyword
class Tokeniser:
    def __init__(self):
        self.token_pos: int = 0
        self.tokens: list[Token] = []
        self.text: str = ""
    
    def tokenize(self, input_file:str)->list[Token]:
        self.text = input_file
        while self.peek_token() != "":
            char = self.peek_token()
            token: Token = Token(TokenType.Empty, "")
            if char.isnumeric():
                self.get_token()
                number = char
                while self.peek_token() != "" and self.peek_token().isnumeric():
                    number += self.get_token()
                token = Token(TokenType.Integer, number)
            elif char.isalpha():
                self.get_token()
                ident = char
                while self.peek_token() != "" and self.peek_token().isalpha():
                    ident += self.get_token()
                is_keyword: bool = False
                keyword: Keyword = Keyword.Empty
                for key in Keyword:
                    if key.value == ident:
                        keyword = key
                        is_keyword = True
                        break
                if is_keyword:
                    token = Token(TokenType.Keyword, keyword)
                else:
                    token = Token(TokenType.Identifier, ident)
            else:
                self.get_token()
                token_type: TokenType = TokenType.Empty
                for tok in TokenType:
                    if tok.value == char:
                        token_type = tok
                token = Token(token_type, "")
            self.tokens.append(token)
            
        return self.tokens
    
    def reset_tokeniser(self):
        self.tokens = []
        self.token_pos = 0
        self.text = ""
        
    def peek_token(self):
        if self.token_pos > len(self.text):
            return ""
        return self.text[self.token_pos]
    
    def get_token(self):
        peek_token = self.peek_token()
        self.token_pos += 1
        return peek_token

def main():
    pass

if __name__ == '__main__':
    main()