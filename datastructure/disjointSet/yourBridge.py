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
N = [0]+[Node(i) for i in range(1,n+1)]

for _ in range(n-2):
    a,b = map(int,input().split())
    N[a].union(N[b])

S = set()
for i in N[1:]:
    S.add(i.find())
    if len(S) == 2:
        print(*S)
        break