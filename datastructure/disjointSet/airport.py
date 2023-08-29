import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.occupied = False
        self.leastGate = data

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
            root1.leastGate = min(root1.leastGate, root2.leastGate)
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.leastGate = min(root1.leastGate, root2.leastGate)

    def __repr__(self):
        return str(self.leastGate)


def nearUnion(node,i):
    if 1<=i<=g and N[i].occupied == True:
        node.union(N[i])

g = int(input())
N = [0]+[Node(i) for i in range(1,g+1)]
p = int(input())

for i in range(p):
    ind = int(input())
    node = N[ind]

    if node.occupied:
        nextGate = node.find().leastGate-1
        if nextGate == 0:
            print(i)
            exit()
        else:
            node = N[nextGate]
            ind = nextGate

    node.occupied = True
    nearUnion(node,ind-1)
    nearUnion(node,ind+1)

print(p)
