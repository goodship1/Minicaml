import ply.yacc as yacc
from lexer import tokens
from ast import *
from table import SymbolTable
from functable import FunctionSymbolTable 

symbol = SymbolTable()
function =  FunctionSymbolTable()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'MODULO'),
)


# Start symbol
start = 'program'

# Grammar rules

def p_program(p):
    '''program : expression'''
    p[0] = ProgramNode(p[1])

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = VariableDeclarationNode(p[1], None)


def p_expression_statement(p):
    '''statement : expression
                 | if_statement'''
    p[0] = p[1]

def p_expression_integer(p):
    '''expression : INTEGER'''
    p[0] = IntegerLiteralNode(p[1])

def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] = FloatLiteralNode(p[1])

def p_expression_string(p):
    '''expression : STRING_LITERAL'''
    p[0] = StringLiteralNode(p[1])

def p_expression_bool(p):
    '''expression : BOOL'''
    p[0] = BooleanLiteralNode(p[1])

def p_expression_char(p):
    '''expression : CHAR_LITERAL'''
    p[0] = CharLiteralNode(p[1])

def p_expression_binary_operation(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression EQUAL expression
                  | expression NOT_EQUAL expression
                  | expression LESS_THAN expression
                  | expression LESS_THAN_EQUAL expression
                  | expression GREATER_THAN expression
                  | expression GREATER_THAN_EQUAL expression'''
    if p[2] == '+':
        p[0] = AdditionNode(p[1], p[3])
    elif p[2] == '-':
        p[0] = SubtractionNode(p[1], p[3])
    elif p[2] == '*':
        p[0] = MultiplicationNode(p[1], p[3])
    elif p[2] == '/':
        p[0] = DivideNode(p[1], p[3])
    elif p[2] == '%':
        p[0] = ModuloNode(p[1], p[3])
    elif p[2] == '==':
        p[0] = EqualNode(p[1], p[3])
    elif p[2] == '!=':
        p[0] = NotEqualNode(p[1], p[3])
    elif p[2] == '<':
        p[0] = LessThanNode(p[1], p[3])
    elif p[2] == '<=':
        p[0] = LessThanEqualNode(p[1], p[3])
    elif p[2] == '>':
        p[0] = GreaterThanNode(p[1], p[3])
    elif p[2] == '>=':
        p[0] = GreaterThanEqualNode(p[1], p[3])

def p_list(p):
    '''expression : LBRACKET expression_list RBRACKET'''
    p[0] = LisstNode(p[2])

def p_expression_function_call(p):
    '''expression : IDENTIFIER LPAREN expression_list RPAREN'''
    p[0] = FunctionCallNode(p[1], p[3])

def p_expression_function(p):
    '''expression : FUNCTION IDENTIFIER LPAREN parameter_list RPAREN EQUAL expression'''
    p[0] = FunctionNode(p[2], p[4], p[7])

def p_expression_let(p):
    '''expression : LET IDENTIFIER EQUAL expression IN expression'''
    p[0] = VariableDeclarationNode(p[2], p[4])

def p_parameter_list(p):
    '''parameter_list : IDENTIFIER
                      | IDENTIFIER COMMA parameter_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]



def p_expression_function_declaration(p):
    '''expression : LET IDENTIFIER parameter_list EQUAL FUNCTION expression'''
    p[0] = FunctionNode(p[2], p[3], p[6])




def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''
    if len(p) == 2:
        p[0] = ExpressionListNode([p[1]])
    else:
        p[0] = ExpressionListNode([p[1]] + p[3])


def p_parameter(p):
    '''parameter : IDENTIFIER
                 | IDENTIFIER COMMA parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression_variable_declaration(p):
		'''expression : LET IDENTIFIER EQUAL expression'''
		variable_name = p[2]
		variable_value = p[4]
		symbol.add_variable(variable_name, variable_value)
		p[0] = VariableDeclaration(variable_name,variable_value) 

	



def p_function_declaration(p):
    '''expression : LET IDENTIFIER  parameter_list EQUAL expression'''
    func_name =  p[2]
    parameters = p[3]
    code_block  = p[5]
    function.add_function(func_name,parameters,code_block)
    p[0] = FunctionNode(func_name,parameters,code_block)


def p_record_fields(p):
    '''record_fields : record_field
                     | record_field COMMA record_fields'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_record_field(p):
    '''record_field : IDENTIFIER COLON expression'''
    p[0] = (p[1], p[3]) 

def p_expression_record(p):
    '''expression : LBRACE record_fields RBRACE'''
    p[0] = RecordNode(p[2])

def p_if_then_expression(p):
    '''if_statement : IF expression THEN statement'''
    p[0] = IfStatementNode(p[2],p[4])



# Error handling
def p_error(p):
    print("Syntax error:", p)

# Build the parser
parser = yacc.yacc(start = "expression")

# Test the parser
data = "let add x , y =  x + y" 

result = parser.parse(data)
print(result)
