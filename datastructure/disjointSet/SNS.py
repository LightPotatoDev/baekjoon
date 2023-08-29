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

T = int(input())
for tc in range(1,T+1):
    print(f"Scenario {tc}:")

    n = int(input())
    N = [Node(i) for i in range(n)]

    k = int(input())
    for _ in range(k):
        a,b = map(int,input().split())
        N[a].union(N[b])

    m = int(input())
    for _ in range(m):
        u,v = map(int,input().split())
        print(int(N[u].find() == N[v].find()))
    print('')