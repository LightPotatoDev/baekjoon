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

T = int(input())

for _ in range(T):
    n = int(input())
    N = [0]+[Node(i) for i in range(1,n+1)]
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        N[a].union(N[b])

    groups = set()
    flag = True
    for i in range(1,n+1):
        root = N[i].find()
        if root.isTree == True:
            groups.add(root)
        else:
            flag = False

    if len(groups) == 1 and flag == True:
        print("tree")
    else:
        print("graph")