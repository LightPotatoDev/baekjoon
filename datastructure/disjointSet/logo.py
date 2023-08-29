import sys
input = sys.stdin.readline
from itertools import combinations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.rect = [0,0,0,0]

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
crossO = False
N = [Node(i) for i in range(n)]

def rectIntersect(r1,r2):
    x1,y1,x2,y2 = r1
    x3,y3,x4,y4 = r2
    dx = min(x2-x3, x4-x1)
    dy = min(y2-y3, y4-y1)
    include1 = x1<x3 and x4<x2 and y1<y3 and y4<y2
    include2 = x3<x1 and x2<x4 and y3<y1 and y2<y4
    return (dx >= 0 and dy >= 0) and not(include1 or include2)

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    verti = (x1 == 0 or x2 == 0) and (y1 <= 0 and y2 >= 0)
    hori  = (y1 == 0 or y2 == 0) and (x1 <= 0 and x2 >= 0)
    if verti or hori:
        crossO = True
    N[i].rect = [x1,y1,x2,y2]

for n1,n2 in combinations(N,2):
    if rectIntersect(n1.rect,n2.rect):
        n1.union(n2)

S = {N[i].find() for i in range(n)}
print(len(S)-int(crossO))