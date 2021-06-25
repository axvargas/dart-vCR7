'''
Created Date: Thursday June 24th 2021 11:08:16 pm
Author: Andrés X. Vargas
-----
Last Modified: Friday June 25th 2021 12:36:23 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''

from ply.yacc import yacc
from lexer import tokens

def p_body(p):
  '''body : forstmt
          | listassign'''

def p_listassign(p):
    '''listassign : VAR IDENT EQ_V list SEMICOLON
    '''

def p_listassign_diamonds(p):
    '''listassign : LIST LT typedata GT IDENT EQ_V list SEMICOLON
    '''

def p_typedata(p):
    '''typedata : INT_TYPE
                | DOUBLE_TYPE
                | BOOLEAN
                | STRING_TYPE
    '''

def p_listassign_list(p):
    '''listassign : LIST IDENT EQ_V list SEMICOLON
    '''

def p_list(p):
    '''list : LBRACKET element RBRACKET 
    '''
def p_list_void(p):
    '''list : LBRACKET RBRACKET
    '''

def p_element_single(p):
    '''element : typre
    '''
def p_element(p):
    '''element : typre COMMA typre
    '''

def p_element_more(p):
    '''element : typre COMMA typre moreelements
    '''

def p_moreelements(p):
    '''moreelements : COMMA typre
                    | COMMA typre moreelements
    '''

# ! Delete this
def p_typre(p):
  '''typre : STRING
           | INT
           | TRUE
           | FALSE
           | FLOAT
           | IDENT
  '''

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
