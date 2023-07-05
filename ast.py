class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

class ListNode:
    def __init__(self,elements):
        self.elements = elements

class RecordNode:
    def __init__(self,fields):
        self.fields =  fields



class VariableDeclarationNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class IntegerLiteralNode:
      def __init__(self,value):
         self.value =  value
	


class AdditionNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class SubtractionNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class MultiplicationNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ModuloNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right


class GreaterThanNode:
    def __init__(self,left,right):
        self.left = left 
        self.right = right

class LessThanNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right



class VariableDeclaration:
    def __init__(self,name,value):
        self.name =  name
        self.value = value


class DivideNode:
    def __init__(self,left,right):
        self.left =  left
        self.right = right

class GreaterThanEqualNode:
    def __init__(self,left,right):
        self.left =  left
        self.right = right

class LessThanEqualNode:
    def __init__(self,left,right):
        self.left =  left
        self.right = right

class NotEqualNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right

class FunctionNode:
    def __init__(self,name,parameters,body):
        self.name = name
        self.parameters = parameters
        self.body = body


