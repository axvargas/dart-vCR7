import ply.yacc as yacc

from .lexer import tokens

def p_ifstm(p):
  '''
  ifstm : IF LPAREN condition RPAREN LBRACE RBRACE
  '''

def p_condition(p):
  '''
  condition : preposition operator preposition
  '''

def p_condition_more(p):
  '''
  condition :  preposition operator preposition operator condition
  '''