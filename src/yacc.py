from ply.yacc import yacc
from lexer import tokens

def p_ifstm(p):
  '''ifstm : IF LPAREN condition RPAREN LBRACE RBRACE'''

def p_condition(p):
  '''condition : preposition operator preposition'''

def p_condition_more(p):
  '''condition :  preposition operator preposition morecond'''

def p_morecond(p):
  '''morecond : operator preposition
              | operator preposition morecond
  '''

def p_operator(p):
  '''operator : EQ
              | NE
              | AND
              | OR
  '''

def p_preposition(p):
  '''preposition : typre'''

def p_preposition_not(p):
  '''preposition : NEGATION typre'''

def p_typre(p):
  '''typre : STRING
           | INT
           | TRUE
           | FALSE
           | FLOAT
           | IDENT
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
  if not data: continue
  result = parser.parse(data)
  print(result)