'''
Created Date: Thursday June 24th 2021 11:08:16 pm
Author: Andrés X. Vargas
-----
Last Modified: Thursday June 24th 2021 11:11:04 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''

from ply.yacc import yacc
from lexer import tokens

def p_body(p):
  '''body : forstmt'''

def p_forstmt(p):
    '''forstmt : FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE RBRACE
    '''


def p_assign(p):
    '''assign : IDENT EQ_V INT
    '''


def p_comparisonint(p):
    '''comparisonint : IDENT comparisonop INT
    '''


def p_varincredecre(p):
    '''varincredecre : incredecre IDENT
                                     | IDENT incredecre
    '''


def p_incredecre(p):
    '''incredecre : PLUSPLUS
                              | MINUSMINUS
    '''


def p_comparisonop(p):
    '''comparisonop : EQ
                        | GT
                        | GTE
                        | LT
                        | LTE
                        | NE
    '''


parser = yacc()

print(
    '''

    ██████╗░░█████╗░██████╗░████████╗  ░█████╗░██████╗░███████╗
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗╚════██║
    ██║░░██║███████║██████╔╝░░░██║░░░  ██║░░╚═╝██████╔╝░░░░██╔╝
    ██║░░██║██╔══██║██╔══██╗░░░██║░░░  ██║░░██╗██╔══██╗░░░██╔╝░
    ██████╔╝██║░░██║██║░░██║░░░██║░░░  ╚█████╔╝██║░░██║░░██╔╝░░
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░╚═╝░░░

        ██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗
        ██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║
        ╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║
        ░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║
        ░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║
        ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝

Welcome to Dart CR7 v.0.1 REPL the programming language based on EL BICHO (SIIIUUUUU)

'''
)

while True:
    try:
        data = input('CR7>>> ')
    except EOFError:
        break
    if not data:
        continue
    result = parser.parse(data)
    print(result)
