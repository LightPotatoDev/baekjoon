import sys
input = sys.stdin.readline

class Node:
    def __init__(self, cost):
        self.cost = cost
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
            root1.cost = min(root1.cost, root2.cost)
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.cost = min(root1.cost, root2.cost)

    def __repr__(self):
        return str(self.cost)

n,m,k = map(int,input().split())
A = list(map(int,input().split()))
N = [Node(i) for i in A]
for _ in range(m):
    v,w = map(int,input().split())
    N[v-1].union(N[w-1])

groups = set()
for i in N:
    groups.add(i.find())
totalcost = sum([node.cost for node in groups])
if totalcost <= k:
    print(totalcost)
else:
    print("Oh no")