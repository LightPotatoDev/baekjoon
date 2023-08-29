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

n = int(input())
m = int(input())

L = [Node(i) for i in range(n)]
for i in range(n):
    linked = list(map(int,input().split()))
    for j,x in enumerate(linked):
        if x == 1:
            L[i].union(L[j])

trips = list(map(int,input().split()))
standard = L[trips[0]-1].find()
for i in trips[1:]:
    if L[i-1].find() != standard:
        print("NO")
        exit()
print("YES")
