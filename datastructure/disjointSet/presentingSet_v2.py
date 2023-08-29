import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1

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
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
L = [Node(i) for i in range(n+1)]

for _ in range(m):
    cmd,n1,n2 = map(int,input().split())
    if cmd == 0:
        L[n1].union(L[n2])
    else:
        if L[n1].find() == L[n2].find():
            print("YES")
        else:
            print("NO")