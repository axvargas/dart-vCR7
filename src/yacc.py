from ply.yacc import yacc
from lexer import tokens

def p_body(p):
  '''body : colstms'''

def p_empty(p):
  '''empty :'''
  pass

def p_nonColtypes(p):
  '''nonColtypes : ifstm
                 | elstm
                 | whilestm
		             | forstmt
                 | func'''

def p_colstms_no(p):
  '''colstms : nonColtypes
             | nonColtypes colstms'''

def p_coltypes(p):
  '''coltypes : idmap
              | stringstm
              | listfunc
              | varfunc
              | dicfunc
              | stringfunc
              | listassign
              | operation
              | siuprint'''

def p_colstms(p):
  '''colstms : coltypes SEMICOLON
             | coltypes SEMICOLON colstms'''

def p_siuprint(p):
  '''siuprint : PRINT LPAREN printable RPAREN'''

def p_printable(p):
  '''printable : STRING
               | IDENT'''

def p_ifstm(p):
  '''ifstm : ifelse LPAREN condition RPAREN LBRACE RBRACE
           | ifelse LPAREN condition RPAREN LBRACE body RBRACE'''

def p_elstm(p):
  '''elstm : ELSE LBRACE body RBRACE'''

def p_ifelse(p):
  '''ifelse : IF
            | ELSE IF'''

def p_whilestm(p):
  '''whilestm : WHILE LPAREN condition RPAREN LBRACE RBRACE
            | WHILE LPAREN condition RPAREN LBRACE body RBRACE'''

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
              | GT
              | GTE
              | LT
              | LTE
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

def p_dicfunc(p):
  '''dicfunc : dictionary DOT functionmap'''

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
           | tymap
           | listassigntype'''

def p_listassign(p):
    '''listassign : VAR IDENT EQ_V list
    '''

def p_listassign_diamonds(p):
    '''listassign : LIST LT typedata GT IDENT EQ_V list
    '''
  
def p_listassigntype(p):
  '''listassigntype : LIST LT typedata GT IDENT EQ_V list
    '''

def p_typedata(p):
    '''typedata : INT_TYPE
                | DOUBLE_TYPE
                | BOOLEAN
                | STRING_TYPE
    '''

def p_retornable(p):
  '''retornable : INT_TYPE
                | DOUBLE_TYPE
                | BOOLEAN
                | STRING_TYPE
                | VOID
                | LIST
                | MAP
                | SET
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
                | FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE body RBRACE
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

def p_func(p):
  '''func : retornable IDENT LPAREN param RPAREN LBRACE RBRACE
          |  retornable IDENT LPAREN param RPAREN LBRACE body RBRACE 
          | retornable IDENT LPAREN RPAREN LBRACE RBRACE
          |  retornable IDENT LPAREN RPAREN LBRACE body RBRACE
  '''

def p_param_single(p):
  '''param : typedata IDENT
  '''

def p_param(p):
  '''param : typedata IDENT COMMA typedata IDENT
  '''

def p_param_more(p):
  '''param : typedata IDENT COMMA typedata IDENT moreparam
  '''

def p_more_params(p):
  '''moreparam : COMMA typedata IDENT
                | COMMA typedata IDENT moreparam
  '''

def p_varfunc(p):
  '''varfunc : IDENT DOT function'''

def p_stringfunc(p):
  '''stringfunc : STRING DOT function'''

def p_listfunc(p):
  '''listfunc : list DOT function'''

def p_functionmap_clear(p):
  '''function : CLEAR_FUNC LPAREN RPAREN'''

def p_functionmap_addAll(p):
  '''function : ADD_ALL_FUNC LPAREN dictionary  RPAREN'''

def p_functionmap_containsKey(p):
  '''function : CONTAINS_DICT_FUNC LPAREN key RPAREN'''

def p_functionmap_containsValue(p):
  '''function : CONTAINS_VALUE_FUNC LPAREN value RPAREN'''

def p_functionmap_remove(p):
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

### SPRINT 3
def p_operation(p):
  '''operation : arit oparit arit
  '''

def p_operation_p(p):
  '''operation : LPAREN arit oparit arit RPAREN
  '''

def p_operation_m(p):
  '''operation : arit oparit arit moreArit
  '''

def p_operation_mp(p):
  '''operation : LPAREN arit oparit arit moreAritP
  '''

def p_moreArit(p):
  '''moreArit : oparit arit
              | oparit arit moreArit
              | empty
  '''

def p_moreAritP(p):
  '''moreAritP : oparit arit RPAREN
               | oparit arit moreAritP
               | empty
  '''

def p_arit(p):
  '''arit : FLOAT
          | INT
          | operation
  '''

def p_oparit(p):
  '''oparit : PLUS
            | MINUS
            | TIMES
            | DIVISION
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

""" while True:
  try:
    data = input('CR7>>> ')
  except EOFError as e:
    print(e)
    break
  if not data: continue
  result = parser.parse(data)
  print(result) """


with open('./src/testing/data.dart') as data:
  data = data.read()
  print(f'DATA:\n\n{data}\n\n')
  result = parser.parse(data)
  if not result:
    print('SIIUUU!')
  else:
    print('Error :(')
