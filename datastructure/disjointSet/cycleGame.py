import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.size = 1

    def find(self):
        root = self
        while root != root.next:
            root = root.next
        return root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1 == root2:
            return True

        if root1.rank >= root2.rank:
            root2.next = root1
            root1.size += root2.size
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.size += root1.size

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
L = [Node(i) for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    if L[a].union(L[b]) == True:
        print(i+1)
        exit()
print(0)