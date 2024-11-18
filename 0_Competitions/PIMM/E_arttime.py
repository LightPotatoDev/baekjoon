import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.color = 0
        self.lastcol = data

    def find(self):
        root = self
        while root != root.next:
            root = root.next
        return root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1 == root2:
            return

        if root1.rank >= root2.rank:
            root2.next = root1
            root1.lastcol = max(root1.lastcol,root2.lastcol)
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.lastcol = max(root1.lastcol,root2.lastcol)

    def __repr__(self):
        return str(self.color)


def nearUnion(node,i):
    if 0<i<=n and N[i].color != 0:
        node.union(N[i])

n,q = map(int,input().split())
N = [0] + [Node(i) for i in range(1,n+1)]

for _ in range(q):
    a,b,x = map(int,input().split())
    i = a
    while i <= b:
        if N[i].color == 0:
            N[i].color = x
            nearUnion(N[i],i-1)
            nearUnion(N[i],i+1)
        else:
            i = N[i].find().lastcol + 1

print(*N[1:])
