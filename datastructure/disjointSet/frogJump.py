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
            return True

        if root1.rank >= root2.rank:
            root2.next = root1
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2

    def __repr__(self):
        return str(self.data)

n,q = map(int,input().split())
L = [list(map(int,input().split())) + [i] for i in range(1,n+1)] #x1,x2,y,n
L.sort(key = lambda x:(x[0],x[1]))
N = [0]+[Node(i) for i in range(1,n+1)]

x1,x2,y1,n1 = L[0]
for i in range(1,n):
    x3,x4,y2,n2 = L[i]
    if x2>=x3:
        N[n1].union(N[n2])
    else:
        x1 = x3
    x2 = max(x2,x4)
    n1 = n2

for _ in range(q):
    a,b = map(int,input().split())
    print(int(N[a].find() == N[b].find()))