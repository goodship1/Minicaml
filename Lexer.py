import ply.lex as scanner

tokens = (
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'COMMA',
)#tokens which should be lexed 

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LAND = r'&&'
t_LOR = r'\|\|'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_ASSIGN = r'='
t_COLON = r':'
t_ARROW = r'->'
t_PIPE = r'\|'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_UNDERSCORE = r'_'
#simple tokens should be lexed

def t_FLOAT(t):
    #Float lexer rule
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    #Integer lexer rules
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    #Char lexer rule
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remove the surrounding quotes
    return t

def t_STRING(t):
    #String lexer rules
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove the surrounding quotes
    return t

def t_ID(t):
    #Id rule of lexer 
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t
