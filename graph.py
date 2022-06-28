


class Node:
    
    def __init__(self):
        self.parents = dict()
        self.children = dict()
        self.value = None
        
        
    def add_child(self, key, value):
        self.children[key] = value
        
    def add_parent(self, key, value):
        self.parents[key] = value
        

