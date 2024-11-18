import sys
import heapq
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.child = [self]

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
            root1.child.extend(root2.child)
        else:
            root1.next = root2
            root2.child.extend(root1.child)

    def __repr__(self):
        return str(self.data)

n,e,p = map(int,input().split())
points = [list(map(float,input().split())) for _ in range(n)]
nodes = [Node(i) for i in range(n)]
dists = [] #(dist,p1,p2)
for i in range(n):
    x1,y1 = points[i]
    for j in range(n):
        x2,y2 = points[j]
        dists.append((((x1-x2)**2 + (y1-y2)**2) ** 0.5, i, j))
dists.sort()
for i in range(e-1):
    nodes[i].union(nodes[i+1])
for _ in range(p):
    a,b = map(int,input().split())
    nodes[a-1].union(nodes[b-1])

ans = 0
for d,i,j in dists:
    if nodes[i].find() != nodes[j].find():
        nodes[i].union(nodes[j])
        ans += d

print(ans)