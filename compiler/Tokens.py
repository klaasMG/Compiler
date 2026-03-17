from enum import Enum
from dataclasses import dataclass

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
    SemiColon = ";"
    Empty = 0
    
@dataclass
class Token:
    TokenType: TokenType
    value: str | Keyword
