import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.coords = []

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
            root1.coords.extend(root2.coords)
        else:
            root1.next = root2
            root2.coords.extend(root1.coords)

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
N = [0]+[Node(i) for i in range(1,n+1)]
for i in range(1,n+1):
    N[i].coords.append(list(map(int,input().split())))

for _ in range(m):
    a,b = map(int,input().split())
    N[a].union(N[b])

D = dict()
for i in range(1,n+1):
    root, coords = N[i].find().data, N[i].find().coords
    D[root] = coords

peri = int(1e10)
for coords in D.values():
    minX = min(coords, key=lambda x:x[0])[0]
    minY = min(coords, key=lambda x:x[1])[1]
    maxX = max(coords, key=lambda x:x[0])[0]
    maxY = max(coords, key=lambda x:x[1])[1]

    peri = min(peri,(maxX-minX+maxY-minY)*2)
print(peri)