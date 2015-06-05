#include <iostream>

class GetSet(object):
    def __init__(self):
        self.myVar = 0
        
    def get(self):
        print(self.myVar)
        return self.myVar
        
    def set(self, var):
        self.myVar = var
        
        
g = GetSet()
g.get()
g.set(1)
g.get()