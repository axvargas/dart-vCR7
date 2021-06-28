from ply.yacc import yacc
from lexer import tokens

def p_body(p):
  '''body : nonColStms
          | colStms SEMICOLON'''

def p_nonColStms(p):
  '''nonColStms : ifstm
          | whilestm
		  | forstmt'''
          
def p_colStms(p):
  '''colStms :  idmap
          | stringstm
          | varfunc
          | stringfunc
		      | listassign'''

def p_ifstm(p):
  '''ifstm : IF LPAREN condition RPAREN LBRACE RBRACE'''

def p_whilestm(p):
  '''whilestm : WHILE LPAREN condition RPAREN LBRACE RBRACE'''

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
              | SET
              | STRING'''

def p_string(p):
  '''stringstm : STRING_TYPE IDENT EQ_V STRING'''

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

def p_listassign(p):
    '''listassign : VAR IDENT EQ_V list
    '''

def p_listassign_diamonds(p):
    '''listassign : LIST LT typedata GT IDENT EQ_V list
    '''

def p_typedata(p):
    '''typedata : INT_TYPE
                | DOUBLE_TYPE
                | BOOLEAN
                | STRING_TYPE
    '''

def p_listassign_list(p):
    '''listassign : LIST IDENT EQ_V list
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

def p_varfunc(p):
  '''varfunc : IDENT DOT function'''

def p_stringfunc(p):
  '''stringfunc : STRING DOT function'''

def p_function_clear(p):
  '''function : CLEAR_FUNC LPAREN RPAREN'''

def p_function_remove(p):
  '''function : REMOVE_FUNC LPAREN STRING RPAREN'''

def p_function_tostring(p):
  '''function : TOSTRING_FUNC LPAREN RPAREN'''

def p_function_trim(p):
  '''function : TRIM_FUNC LPAREN RPAREN'''

def p_function_endsWith(p):
  '''function : ENDSWITH_FUNC LPAREN STRING RPAREN'''

def p_function_substring(p):
  '''function : SUBSTRING_FUNC LPAREN INT RPAREN'''

def p_function_substring_2(p):
  '''function : SUBSTRING_FUNC LPAREN INT COMMA INT RPAREN'''

def p_function_join(p):
	'''function : JOIN_FUNC LPAREN STRING RPAREN'''

def p_function_contains(p):
	'''function : CONTAINS_FUNC LPAREN  typre RPAREN'''

def p_function_elementat(p):
	'''function : ELEMENTAT_FUNC LPAREN INT RPAREN'''


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

