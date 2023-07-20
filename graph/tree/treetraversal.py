from collections import deque

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def addChild(self,child,pos):
        if pos == 'L':
            self.left = child
        else:
            self.right = child

    def preorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def postorderTraversal(self,root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res



n = int(input())
nodes = deque([])
inserted = [0] * 26
inserted[0] = Node('A')
root = inserted[0]

for _ in range(n):
    nodes.append(input().split())

while nodes:
    ind = ord(nodes[0][0])-65
    if inserted[ind] != 0:
        parent = inserted[ind]

        if nodes[0][1] != ".":
            child = Node(nodes[0][1])
            parent.addChild(child,'L')
            inserted[ord(nodes[0][1])-65] = child
        if nodes[0][2] != ".":
            child = Node(nodes[0][2])
            parent.addChild(child,'R')
            inserted[ord(nodes[0][2])-65] = child

        nodes.popleft()
    else:
        nodes.rotate(-1)

print(''.join(root.preorderTraversal(root)))
print(''.join(root.inorderTraversal(root)))
print(''.join(root.postorderTraversal(root)))

""" by mapsosa

n=int(input())
s={}
for i in range(n):
    a,b,c=input().split()
    s[a]=[b,c]

def preorder(i):
    if i!='.':
        print(i, end="")
        preorder(s[i][0])
        preorder(s[i][1])

def inorder(i):
    if i!='.':
        inorder(s[i][0])
        print(i, end="")
        inorder(s[i][1])

def postorder(i):
    if i!='.':
        postorder(s[i][0])
        postorder(s[i][1])
        print(i, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")

"""