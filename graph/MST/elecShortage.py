import sys
input = sys.stdin.readline

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

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    N = [Node(i) for i in range(n)]
    graph = [list(map(int,input().split())) for _ in range(m)]
    graph.sort(key=lambda x:x[2])

    total = 0
    ans = 0
    for a,b,c in graph:
        total += c
        if N[a].find() != N[b].find():
            N[a].union(N[b])
            ans += c
    print(total - ans)