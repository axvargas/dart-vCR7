from src.lexer import Lexer


def start_repl() -> None:
    while (source := input('\n~#@❯ ')) != 'salir();':
        lexer: Lexer = Lexer(source)

        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)
