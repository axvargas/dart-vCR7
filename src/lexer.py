import ply.lex as lex


tokens = [
    # Enmanuel Magannales
    'AND',
    'ARROW',  # @ replace => in arrow function
    'ASSIGN',
    'ASIGSUM',
    'ASIGTIMES',
    'ASIGDIV',
    'MOD',
    'COMMA',
    'DIVISION',
    'DDOTS',
    'EQ',
    'EQ_V',
    'GT',
    'DOT',
    # Andres Vargas
    'GTE',
    'IDENT',
    'INT',
    'FLOAT',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LT',
    'LTE',
    'NEGATION',
    'NE',
    # Josue Cobos
    'MINUS',
    'MINUSMINUS',
    'OR',
    'ASIGMINUS',
    'TIMES',
    'LPAREN',
    'PLUS',
    'PLUSPLUS',
    'RPAREN',
    'SEMICOLON',
    'STRING',
    'VIR'
]

reserved_words = {
    # Josue Cobos
    'abstract': 'ABSTRACT',
    'as': 'AS',
    'assert': 'ASSERT',
    'async': 'ASYNC',
    'await': 'AWAIT',
    'bool': 'BOOLEAN',
    'break': 'BREAK',
    'dynamic': 'DYNAMIC',
    'double': 'DOUBLE_TYPE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'export': 'EXPORT',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'interface': 'INTERFACE',
    'super': 'SUPER',
    'switch': 'SWITCH',
    'case': 'CASE',
    # Andres Vargar
    'catch': 'CATCH',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'do': 'DO',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    # Enmanuel Magallanes
    'int': 'INT_TYPE',
    'return': 'RETURN',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE',
    'false': 'FALSE',
    'finally': 'FINALLY',
    'true': 'TRUE',
    'typedef': 'TYPEDEF',
    'siu': 'PRINT',
    'String': 'STRING_TYPE',
    'List': 'LIST',
    'Map': 'MAP',
    'Set': 'SET',
    'clear': 'CLEAR_FUNC',
    'toString': 'TOSTRING_FUNC',
    'remove': 'REMOVE_FUNC',
    'trim': "TRIM_FUNC",
    'endsWith': "ENDSWITH_FUNC",
    'substring': "SUBSTRING_FUNC"
}
tokens = tokens + list(reserved_words.values())

# Andres Vargas
t_ignore = ' \t\x0c'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ_V = r'='
t_COMMA = r','
t_DIVISION = r'/'
t_EQ = r'=='
t_GT = r'>'
# Josue Cobos
t_GTE = r'>='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LT = r'<'
t_LTE = r'<='
t_NEGATION = r'!'
t_NE = r'!='
# Enmanuel Magallanes
t_SEMICOLON = r';'
t_ARROW = r'@'
t_DDOTS = r':'
t_VIR = r'~'
t_ASIGSUM = r'\+='
t_ASIGMINUS = r'-='
t_ASIGTIMES = r'\*='
t_ASIGDIV = r'/='
t_MOD = r'%'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_AND = r'&&'
t_OR = r'\|\|'
t_DOT = r'\.'

#re_SIG = t_MINUS + r'?'
t_INT = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_STRING = r'(\"|\')([^\\\n]|(\\.))*?(\"|\')'

def t_IDENT(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_words.get(t.value, 'IDENT')
    return t


""" @TOKEN(re_INT)
def _INT(t):
    t.value = int(t.value)
    return t

@TOKEN(re_FLOAT)
def _FLOAT(t):
    t.value = float(t.value)
    return t """


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value)
    t.lexer.skip(1)


def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

# Josue Cobos
lexer = lex.lex()
data = '''
int goals;
int goals = 5;
double distance = 5.78;
bool is_mvp = true;
String = 'double qoute'
var best_players = ['CR7', 'Kanté',     'Mbappe'];
List best_players_2 = ['CR7', 'Kanté',   
  'Mbappe'];
List<int> numbers = [7, 10, 7];
var position = {
    'MCO': 'Noboa'
    'MD': 'Plata'
    'MI': 'Ibarra'
}
muster + 2;
muster - 2;
muster * 3;
muster / 7;
muster ~/ 7;
muster += 6;
muster -= 7;
muster *= 7;
muster /= 7;
muster % 2;
muster == 35;
muster != 44;
muster < 44;
muster <= 33;
44 > muster;
muster >= 23;
++muster;
mustet++;
--muster;
muster--;
true && muster;
true || muster;
!true;
siu('test', 43);
'''

func = '''
int sum(int a,int b) {
    return a+b;
}
'''

callFunc = '''
sum(3,4)
'''

main = '''
void main() { 
    var num = 12; 
    if (num % 2==0) { 
        siu("Even"); 
    } else { 
        siu("Odd"); 
    } 
}
'''
for_data = '''
for( var i = 0 ; i <= 10; i++ ) { 
    siu(i); 
}
'''
while_data = '''
var i = 0;
while(i <= 10) { 
    siu(i);
    i++; 
} 

'''
if __name__ == "__main__":
    print('''
        

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

Welcome to Dart CR7 v.0.1 REPL the programming language based on EL BICHO SIIIUUUUU

''')
    toTest = [func, callFunc]
    for testText in toTest:
        lex.runmain(lexer, testText)
        print('\n')
