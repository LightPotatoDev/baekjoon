class Node:

    def __init__(self,data,parent=None):
        self.children = []
        self.data = data
        self.parent = parent

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

root = Node(1)
a = Node(2,parent = root)
root.add_child(a)

print(a.parent.data)