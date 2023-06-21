import ply.lex as lex

# List of token names
tokens = [
    'INTEGER',
    'FLOAT',
    'STRING',
    'BOOL',
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
    'I32',
    'I64',
    'U32',
    'U64',
]

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
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_ARROW = r'->'
t_FUNCTION = r'fun'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_LET = r'let'
t_IN = r'in'
t_TRUE = r'true'
t_FALSE = r'false'
t_I32 = r'i32'
t_I64 = r'i64'
t_U32 = r'u32'
t_U64 = r'u64'


reserved = {
    'fun': 'FUNCTION',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'let': 'LET',
    'in': 'IN',
    'true': 'TRUE',
    'false': 'FALSE',
}



def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
data = '''
let x: i32 = 10;
let y: f64 = 3.14;
let message: string = "Hello, world!";
if x > 5 then
    print_int(x)
else
    print_string("Condition not met.")
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
import ply.lex as lex

# List of token names
tokens = [
    'INTEGER',
    'FLOAT',
    'STRING',
    'BOOL',
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
    'I32',
    'I64',
    'U32',
    'U64',
]

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
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_ARROW = r'->'
t_FUNCTION = r'fun'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_LET = r'let'
t_IN = r'in'
t_TRUE = r'true'
t_FALSE = r'false'
t_I32 = r'i32'
t_I64 = r'i64'
t_U32 = r'u32'
t_U64 = r'u64'


reserved = {
    'fun': 'FUNCTION',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'let': 'LET',
    'in': 'IN',
    'true': 'TRUE',
    'false': 'FALSE',
}



def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
data = '''
let x: i32 = 10;
let y: f64 = 3.14;
let message: string = "Hello, world!";
if x > 5 then
    print_int(x)
else
    print_string("Condition not met.")
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
