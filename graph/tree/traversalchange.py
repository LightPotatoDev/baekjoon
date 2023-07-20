import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def postorder(self,root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
        return res

def insert(node,data):
    if node == None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node

first = True
root = None

while True:
    n = input().rstrip()
    if n == "":
        break
    n = int(n)

    if first == True:
        root = insert(root,n)
        first = False
    else:
        insert(root,n)

for i in root.postorder(root):
    print(i)