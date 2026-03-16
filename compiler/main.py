from Tokeniser import Tokeniser, read_file
from Tokens import Token

def main():
    code_file = read_file("code.txt")
    tokeniser = Tokeniser()
    tokens: list[Token] = tokeniser.tokenize(code_file)

if __name__ == '__main__':
    main()