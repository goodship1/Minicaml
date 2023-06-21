import ply.lex as lex

# List of token names
tokens = [
    'INTEGER',
    'FLOAT',
    'STRING',
    'BOOL',
    'CHAR',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'EQUAL',
    'NOT_EQUAL',
    'LESS_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN',
    'GREATER_THAN_EQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'ARROW',
    'FUNCTION',
    'IF',
    'THEN',
    'ELSE',
    'LET',
    'IN',
    'TRUE',
    'FALSE',
    'STRING_LITERAL',
    'CHAR_LITERAL',
    'LIST',
    'TUPLE',
    'OPTION',
    'ARRAY',
    'RECORD',
]

# Reserved keywords
reserved = {
    'fun': 'FUNCTION',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'let': 'LET',
    'in': 'IN',
    'true': 'TRUE',
    'false': 'FALSE',
    'list': 'LIST',
    'tuple': 'TUPLE',
    'option': 'OPTION',
    'array': 'ARRAY',
    'record': 'RECORD',
}

# Regular expression rules for tokens
t_INTEGER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'"([^"\\]|\\.)*"'
t_BOOL = r'true|false'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_EQUAL = r'='
t_NOT_EQUAL = r'<>'
t_LESS_THAN = r'<'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN = r'>'
t_GREATER_THAN_EQUAL = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_ARROW = r'->'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

def t_CHAR_LITERAL(t):
    r"'([^'\\]|\\.)'"
    t.value = t.value[1:-1]  # Remove the single quotes
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
