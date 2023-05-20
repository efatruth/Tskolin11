class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, d):
        if self.value == d:
            return False
        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def find(self, f): # Fall sem checkar hvort talan sé nú þegar til í trénu
        if self.root.insert(f) == False:
            return True
        else:
            return False


t = Tree()
print(t.insert(6))
print(t.insert(2))
print(t.insert(3))
print(t.insert(7))


print(t.find(6)) # Skilar True
print(t.find(2)) # Skilar True
print(t.find(3)) # Skilar True
print(t.find(7)) # Skilar True
print(t.find(1)) # Skilar False
print(t.find(4)) # Skilar False
print(t.find(5)) # Skilar False
