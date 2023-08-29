import sys
input = sys.stdin.readline
from itertools import combinations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.pos = [0,0]
        self.rad = 0

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

T = int(input())
for _ in range(1,T+1):
    n = int(input())
    N = [Node(i) for i in range(n)]
    for i in range(n):
        x,y,r = map(int,input().split())
        N[i].pos = [x,y]
        N[i].rad = r

    comb = combinations(N,2)
    for n1,n2 in comb:
        x1,y1 = n1.pos
        x2,y2 = n2.pos
        d = (x2-x1)**2 + (y2-y1)**2
        if d <= (n1.rad+n2.rad)**2:
            n1.union(n2)

    S = set()
    for n in N:
        S.add(n.find())
    print(len(S))