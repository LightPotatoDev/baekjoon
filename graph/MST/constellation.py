import sys
input = sys.stdin.readline
from itertools import combinations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.weight = 0

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
Stars = [[i]+list(map(float,input().split())) for i in range(n)]
N = [Node(i) for i in range(n)]
graph = []
comb = combinations(Stars,2)
for s1,s2 in comb:
    n1,x1,y1 = s1
    n2,x2,y2 = s2
    dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    graph.append([n1,n2,dist])
graph.sort(key=lambda x:x[2])

ans = 0
for a,b,c in graph:
    if N[a].find() != N[b].find():
        N[a].union(N[b])
        ans += c
print(ans)