

class Node():
    parent = None
    state = None

    def __init__ (self,state,parent):
        self.state = state
        self.parent = parent



node1 = Node((1,2), None)

print(node1.state)
print(node1.parent)
