from ply.yacc import yacc
from lexer import tokens

def p_body(p):
  '''body : ifstm
          | idmap
          | varfunc'''

def p_ifstm(p):
  '''ifstm : IF LPAREN condition RPAREN LBRACE RBRACE'''

def p_condition_single(p):
  '''condition : preposition'''

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

def p_idmap(p):
  '''idmap : tymap IDENT EQ_V dictionary'''

def p_tymap(p):
  '''tymap : MAP
           | MAP LT tykey COMMA tyvalue GT'''

def p_tykey(p):
  '''tykey : STRING_TYPE
           | DOUBLE_TYPE
           | INT_TYPE'''

def p_tyvalue(p):
  '''tyvalue : STRING_TYPE
             | DOUBLE_TYPE
             | INT_TYPE
             | BOOLEAN
             | IDENT
             | iterable
             | tymap'''

def p_iterable(p):
  '''iterable : LIST
              | SET'''

def p_dictionary(p):
  '''dictionary : LBRACE item RBRACE'''

def p_item(p):
  '''item : key DDOTS value
          | key DDOTS value COMMA item'''

def p_key(p):
  '''key : STRING
         | INT
         | FLOAT'''

def p_value(p):
  '''value : STRING
           | FLOAT
           | INT
           | FALSE
           | TRUE
           | IDENT
           | iterable
           | tymap'''

def p_varfunc(p):
  '''varfunc : IDENT DOT function'''

def p_function_clear(p):
  '''function : CLEAR_FUNC LPAREN RPAREN'''

def p_function_remove(p):
  '''function : REMOVE_FUNC LPAREN STRING RPAREN'''

def p_function_tostring(p):
  '''function : TOSTRING_FUNC LPAREN RPAREN'''


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