import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.isTree = True

    def find(self):
        root = self
        while root != root.next:
            root = root.next
        return root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1 == root2:
            root1.isTree = False
            root2.isTree = False
            return

        if root1.rank >= root2.rank:
            root2.next = root1
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2

    def __repr__(self):
        return str(self.data)

tc = 0
while True:
    tc += 1
    n,m = map(int,input().split())
    if n == 0:
        break

    N = [0]+[Node(i) for i in range(1,n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        N[a].union(N[b])

    groups = set()
    trees = 0
    for i in range(1,n+1):
        g = N[i].find()
        if not g in groups and g.isTree == True:
            groups.add(g)
            trees += 1

    print(f"Case {tc}: ",end = '')
    if trees == 0:
        print("No trees.")
    elif trees == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {trees} trees.")