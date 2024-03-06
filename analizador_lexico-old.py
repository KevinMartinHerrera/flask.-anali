import ply.lex as lex

# Lista de tokens 
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
}

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',
    'LEFT_BRACKET', 
    'RIGHT_BRACKET', 
    'LEFT_BRACE', 
    'RIGHT_BRACE',  
    'ID',
] + list(reserved.values())

# Reglas de expresiones regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+(\.\d+)?'  
t_EQUALS = r'='
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_LEFT_BRACKET = r'\['  
t_RIGHT_BRACKET = r'\]'  
t_LEFT_BRACE = r'\{'  
t_RIGHT_BRACE = r'\}'  
t_ignore = ' \t'  

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    t.lineno = t.lexer.lineno  
    return t

lexer = lex.lex()