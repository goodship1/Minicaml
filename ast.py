class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

class VariableDeclarationNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

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

class DivideNode:
    def __init__(self,left,right):
        self.left =  left
        self.right  = right
