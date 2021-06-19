import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'ASSIGN',
    'COMMA',
    'DIVISION',
    'ELSE',
    'EOF ',
    'EQ',
    'FALSE',
    'FUNCTION',
    'GT',
    'G_EQ_T',
    'IDENT ',
    'IF',
    'ILLEGAL',
    'INT',
    'LBRACE',
    'LET ',
    'LT',
    'L_EQ_T',
    'NEGATION',
    'NOT_EQ',
    'MINUS',
    'TIMES',
    'LPAREN',
    'PLUS',
    'RBRACE',
    'RETURN',
    'RPAREN',
    'SEMICOLON',
    'TRUE',
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
}

tokens = tokens + list(reserved_words.values())

t_ignore = '\t'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
