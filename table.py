class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.current =  None
    
    def start_scope(self):
        scope  = {}
        if self.current:
            new_scope["parent"] = self.current
        self.current  = new_scope
    
    def exit_scope(self):
        if self.current:
            self.current = self.current.get("parent")
    
    def add_to_table(self,names,value):
        if self.current:
            self.current[name] =  value
        else:
            raise Exception("not in scope")

    def lookup_symbol(self,name):
        scope = self.current
        while scope:
            if name in scope:
                return scope[name]
            scope =  scope.get("parent")
        raise Exception("not in scope")

    def print_table(self):
        print("Symbol table")
        for data , scope in enumerate(reversed(self.get_scopes()),start=1):
            print(data)
        for name , value in scope.items():
            print(value)

    def get_scopes(self):
        scopes = []
        scope = self.current
        while scope:
            scopes.append(scope)
            scope = scope.get("parent")
        return scopes



