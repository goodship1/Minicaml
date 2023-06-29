class FunctionSymbolTable:
    def __init__(self):
        self.functions = {}

    def add_function(self, name, parameters, return_type):
        if name in self.functions:
            raise Exception("already defined")
        self.functions[name] = {
            'name': name,
            'parameters': parameters,
            'return_type': return_type
        }

    def get_function(self, name):
        if name not in self.functions:
            raise Exception("Function  not found")
        return self.functions[name]



