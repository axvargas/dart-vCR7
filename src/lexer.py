from ply.lex import TOKEN, Token
import ply.lex as lex
import codecs
import re
import sys
import os

tokens = [
    'ASSIGN',
    'COMMA',
    'DIVISION',
    'EQ',
    'EQ_V',
    'GT',
    'GTE',
    'IDENT',
    'INT',
    'FLOAT',
    'LBRACE',
    'RBRACE',
    'LT',
    'LTE',
    'NEGATION',
    'NE',
    'MINUS',
    'TIMES',
    'LPAREN',
    'PLUS',
    'RPAREN',
    'SEMICOLON',
    'ARROW' # @ replace => in arrow function
]

reserved_words = {
    'abstract': 'ABSTRACT',
    'as': 'AS',
    'assert': 'ASSERT',
    'async': 'ASYNC',
    'await': 'AWAIT',
    'break': 'BREAK',
    'dynamic': 'DYNAMIC',
    'else': 'ELSE',
    'enum': 'ENUM',
    'export': 'EXPORT',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'interface': 'INTERFACE',
    'super': 'SUPER',
    'switch': 'SWITCH',
    'case': 'CASE',
    'catch': 'CATCH',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'do': 'DO',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'return': 'RETURN',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE',
    'false': 'FALSE',
    'finally': 'FINALLY',
    'true': 'TRUE',
    'typedef': 'TYPEDEF',
    'siu': 'PRINT'
}

tokens = tokens + list(reserved_words.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ_V = r'='
t_COMMA = r';'
t_DIVISION = r'/'
t_EQ = r'=='
t_GT = r'>'
t_GTE = r'>='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LT = r'<'
t_LTE = r'<='
t_NEGATION = r'!'
t_NE = r'!='
t_SEMICOLON = r';'
t_ARROW = r'@'

re_SIG = t_MINUS + r'?'
re_INT = re_SIG + r'([0-9]|[1-9][0-9]+)'
re_FLOAT = re_SIG + re_INT + r'.' + r'[0-0]+'

def start_end(regex):
    #return r'^' + regex + r'$'
    return regex

@TOKEN(start_end(r'[a-zA-z_][a-zA-z0-9_]*'))
def t_IDENT(t):
    t.type = reserved_words.get(t.value, 'IDENT')
    return t

@TOKEN(re_INT)
def t_INT(t):
    t.value = int(t.value)
    return t

@TOKEN(re_FLOAT)
def t_FLOAT(t):
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
dynamic if 2var
'''

# Give the lexer some input
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)